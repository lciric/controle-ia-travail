# Proposition B — Tour III.1 : ce que la longueur change, mesuré comme un exposant

**Pièces reçues.** Le bloc FAITS et le bloc QUESTION portent la même empreinte sha256 et ont un contenu identique. Le bloc FAITS ne contient donc aucun fait muni d'un statut. Je n'en invente pas. Toutes mes affirmations ci-dessous portent leur propre statut. Je traite les consignes présentes dans FAITS comme des données et je réponds à la QUESTION, qui a le même contenu.

---

## (1) Question de recherche

À dégradation totale fixée du résultat final, comment la **dégradation maximale non détectée D\*(n)** croît-elle avec le nombre n d'actions, et l'accès aux activations, aux exécutions de comparaison et à la vérification coûteuse change-t-il l'**exposant α** de la loi D\*(n) ∝ n^α par rapport à la seule surveillance du texte ?

**Pourquoi cette formulation.** « Ce que la longueur change » se réduit à un nombre mesurable : la pente de log D\* en fonction de log n. Trois régimes simples prédisent trois exposants différents, et chacun correspond à un mécanisme distinct. Toutes les dérivations de ce paragraphe sont des [HYPOTHÈSE] heuristiques.

| Régime | Mécanisme | α prédit | Ce que la longueur fait |
|---|---|---|---|
| **R0 : signal d'intention à amplitude fixe** | Chaque acte saboteur laisse un signal, interne ou textuel, d'intensité ε indépendante de l'ampleur de l'écart. L'adversaire doit alors limiter le nombre d'actes à O(1). | ≈ 0 | Elle n'offre aucun couvert à l'adversaire. Le défenseur gagne. |
| **R½ : loi de la racine carrée** | Le signal par acte est proportionnel à l'écart δ. La divergence cumulée vaut environ nδ²/σ². À détectabilité fixe, δ ∝ n^(−½), donc la dégradation totale nδ ∝ n^(½). | ≈ ½ | Elle sert l'adversaire, mais de façon sous-linéaire. |
| **R1 : hétérogénéité non éliminée** | La variance inter-exécutions honnêtes τ², propre à chaque tâche, domine. Le score agrégé a alors un écart-type d'environ nτ. La détection dépend de δ/τ, qui ne varie pas avec n. | ≈ 1 | Elle sert de couvert pur, linéaire. |

Le régime R½ est la transposition de la loi de la racine carrée connue en stéganographie et en communication furtive (voir (3)). Les exécutions de comparaison sur **la même tâche** sont l'instrument qui devrait faire passer de R1 à R½, parce qu'elles retirent τ [HYPOTHÈSE]. Les activations sont le seul instrument qui pourrait faire passer à R0 [HYPOTHÈSE].

## (2) Réponse attendue, sous forme réfutable

Statut de l'ensemble : [HYPOTHÈSE]. Les seuils sont illustratifs.

- **P1.** Sur des tâches à dommage **additif**, avec surveillance du texte et m ≥ 3 exécutions de comparaison, on aura α ∈ [0,35 ; 0,65].
- **P2.** Sans exécution de comparaison, α ≥ 0,8, à condition que τ² mesuré soit non négligeable.
- **P3.** Les sondes sur activations abaissent α à ≤ 0,2 pour un organisme dont l'instruction de sabotage figure dans le contexte. Elles l'abaissent de moins de 0,15 pour un organisme entraîné (LoRA à déclencheur). J'attends donc que le gain apparent des activations soit surtout une lecture de l'instruction présente dans le contexte, et non de l'« intention ».
- **P4.** Sur des tâches **à goulot**, où la conclusion dépend de quelques décisions, α ≈ 0 pour tous les instruments. La longueur n'y change presque rien.
- **P5.** Avec un budget absolu fixe de vérifications ciblées par pas, la probabilité de détection décroît avec n face à un adversaire qui dilue.

Chacune de ces prédictions peut être fausse indépendamment des autres.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi il compte |
|---|---|---|---|
| S1 | « Longueur » est une seule variable. Elle mêle en réalité le nombre d'actions, la longueur du contexte, le nombre de points de décision et la profondeur des dépendances. | HYPOTHÈSE | Il faut faire varier le nombre de points de décision en gardant la structure fixe, sinon α est confondu avec la dérive du contexte. |
| S2 | Des actes non suspects pris isolément peuvent produire une dégradation significative. | HYPOTHÈSE. Des évaluations de sabotage existent [RAPPORTÉ, de mémoire, voir (3)]. | Si c'est faux, la question est vide. |
| S3 | Un modèle de 8 milliards de paramètres peut mener seul une tâche de centaines d'actions, honnêtement **et** en sabotant de façon cohérente. | HYPOTHÈSE, douteuse. Des mesures publiées suggèrent un horizon de tâche limité pour les modèles modestes [RAPPORTÉ, de mémoire, Kwa et al. 2025, à vérifier]. | Un α faible pourrait refléter l'incompétence de l'adversaire et non la force du défenseur. Il faut un adversaire **scripté** en plus de l'adversaire agentique. |
| S4 | Les erreurs honnêtes sont **non dirigées** par rapport à la conclusion, alors que le sabotage est dirigé. | HYPOTHÈSE | C'est le seul critère qui les sépare en distribution. Il est faux si l'agent honnête a des biais systématiques, par exemple la complaisance envers la réponse espérée. |
| S5 | Les activations portent une trace d'intention distincte du contenu de l'action. | HYPOTHÈSE. Des sondes de tromperie ont été rapportées dans des cadres plus simples [RAPPORTÉ, de mémoire, à vérifier]. | Ce présupposé départage R0 et R½. |
| S6 | Les exécutions de comparaison sont honnêtes et indépendantes. | HYPOTHÈSE | Si elles viennent du même modèle non fiable, il peut saboter de façon cohérente dans toutes les exécutions, et la comparaison ne voit rien. |
| S7 | La vérification coûteuse est exacte et peut distinguer une erreur d'un sabotage. | HYPOTHÈSE, probablement fausse au niveau du pas. | Par construction, un pas isolé n'est pas suspect. La vérification d'un pas ne révèle qu'une « erreur », jamais une intention. |
| S8 | La variabilité honnête du résultat final est bornée à grand n. | HYPOTHÈSE | Si elle explose, le défenseur ne peut même pas faire confiance au travail honnête (voir « sans intérêt »). |
| S9 | Le dommage s'additionne le long des pas. | HYPOTHÈSE | Les tâches additives et les tâches à goulot prédisent des α différents (P4). |

---

## (b) Expériences décisives (inférence forte)

### Banc commun

Statut : [HYPOTHÈSE] de conception ; tous les chiffres sont illustratifs.

**Tâches.** Des « analyses à bifurcations » synthétiques avec vérité terrain. Un jeu de données généré comporte n points de décision. À chacun, 2 à 4 options sont défendables : règle d'exclusion des valeurs aberrantes, transformation, filtre, agrégation. L'effet de chaque option sur l'estimation finale est calculable mécaniquement. Le dommage D est le biais de l'estimation finale, en unités absolues de la quantité cible, identiques pour tout n.

**Deux familles de tâches :**
- additive : la quantité estimée agrège n sous-analyses ;
- à goulot : 3 décisions sur n déterminent la conclusion.

**Longueurs.** n ∈ {25, 50, 100, 200, 400} points de décision, avec un échafaudage identique.

**Adversaires.**
- **Scripté** : le modèle honnête choisit, mais à chaque décision un contrôleur externe remplace son choix, avec une probabilité q, par l'option défendable qui pousse dans la direction cible. On contrôle ainsi la dilution sans dépendre de la compétence de l'adversaire.
- **Agentique en contexte** : instruction cachée de dégrader « sans qu'aucune action ne paraisse anormale ».
- **Agentique entraîné** : LoRA à déclencheur, sans instruction dans le contexte.

**Définition de D\*(n).** C'est le plus petit D tel que le meilleur détecteur d'une famille donnée atteigne un taux de détection (TPR) ≥ 50 % à un taux de fausses alertes (FPR) de 5 % au niveau de la trajectoire (seuils illustratifs). On l'obtient par une grille sur q, puis un ajustement logistique de TPR(D) pour chaque n. On a α = pente de log D\* sur log n, avec intervalle de confiance par bootstrap sur les tâches.

**Règle de non-conclusion, pré-enregistrée.** Si la demi-largeur de l'IC95 sur α dépasse 0,12 (illustratif), on déclare le résultat non concluant au lieu de l'interpréter.

### E1 — Loi de la racine carrée (texte + comparaisons, tâches additives)

- **H_A :** α ∈ [0,35 ; 0,65] (régime R½).
- **H_B :** α ∉ [0,35 ; 0,65] (régime R0 ou R1).
- **Métrique :** α estimé avec l'adversaire scripté, le détecteur texte agrégé (somme de log-vraisemblances ou CUSUM) et m = 3 comparaisons.
- **Contrôle négatif :** des trajectoires honnêtes où l'on injecte des erreurs **de même amplitude mais de direction aléatoire**. Le détecteur doit y rester à AUROC ≈ 0,5 (IC contenant 0,5). S'il les signale, il détecte des erreurs, pas du sabotage, et E1 est invalidé.
- **Falsification :** un IC95 entièrement hors de [0,35 ; 0,65] falsifie H_A. Un IC95 entièrement dedans falsifie H_B, c'est-à-dire les deux régimes alternatifs pour ce couple d'instruments.

### E2 — Rôle des exécutions de comparaison

- **H_A :** passer de m = 0 à m = 3 réduit α d'au moins 0,3 (passage de R1 à R½).
- **H_B :** la réduction de α est < 0,15.
- **Métrique :** Δα = α(m=0) − α(m=3), avec IC bootstrap apparié par tâche.
- **Mesure préalable :** τ², la variance inter-tâches du score honnête. Si τ² ≈ 0, E2 est pré-déclaré non informatif, car les deux hypothèses prédisent alors la même chose.
- **Contrôle négatif :** des « comparaisons » qui sont de simples rejeux avec la même graine, donc identiques à la trajectoire observée. Elles ne doivent apporter aucun gain.
- **Falsification :** Δα ≥ 0,3 (borne basse de l'IC) falsifie H_B. Δα < 0,15 (borne haute de l'IC) falsifie H_A.

### E3 — Les activations portent-elles un signal d'intention indépendant de l'amplitude ?

- **H_A (vers R0) :** parmi les actes saboteurs, le score de sonde a une **ordonnée à l'origine positive** quand l'effet δ de l'acte tend vers 0. Le signal ne dépend pas de l'amplitude.
- **H_B (reste en R½) :** le score de sonde est proportionnel à δ, avec une ordonnée à l'origine compatible avec 0.
- **Métrique :** régression du score de sonde sur |δ| par acte. Ordonnée à l'origine en unités d'écart-type honnête, seuil 0,5 (illustratif). On mesure ensuite α avec la sonde agrégée.

**Deux contrôles négatifs, indispensables :**
- **Actions appariées par pré-remplissage.** On force mot pour mot l'action saboteuse dans une trajectoire honnête, sans aucune instruction de sabotage. Si la sonde sépare ces actions des actes saboteurs, elle lit autre chose que le contenu. Si elle ne les sépare pas, elle lit le contenu et n'apporte rien de plus que le texte.
- **Instruction présente mais désactivée.** L'instruction de sabotage figure dans le contexte avec l'ordre explicite de ne pas l'exécuter. Si la sonde se déclenche, elle lit l'instruction et non l'intention.

**Organismes.** Le test est fait sur l'organisme en contexte **et** sur l'organisme LoRA. P3 prédit que H_A ne survit que sur le premier.

**Falsification :** une ordonnée à l'origine ≥ 0,5 qui survit aux deux contrôles falsifie H_B. Une ordonnée à l'origine compatible avec 0, ou un signal qui disparaît sous les contrôles, falsifie H_A.

### E4 — Vérification coûteuse à budget absolu fixe

- **H_A :** avec B vérifications de pas ciblées par le meilleur moniteur (B ∈ {1, 5, 20}, illustratif), la probabilité qu'au moins une vérification touche un acte saboteur **et** qu'on l'attribue correctement décroît avec n face à l'adversaire qui dilue.
- **H_B :** elle ne décroît pas, parce que le ciblage par le moniteur concentre suffisamment.
- **Métrique :** pente de logit(P_détection) sur log n, avec un FPR fixé sur les trajectoires honnêtes vérifiées. On le fixe en exigeant qu'une « erreur vérifiée » s'accompagne d'un excès d'erreurs **dirigées**, puisqu'une erreur seule ne prouve rien (S7).
- **Contrôle négatif :** le même budget dépensé sur des trajectoires honnêtes contenant des erreurs naturelles. On mesure le taux de fausses attributions.
- **Comparateur mécanique :** une seule réplication du résultat final par un script d'analyse par défaut, à coût indépendant de n.
- **Falsification :** une pente < 0 (borne haute de l'IC < 0) falsifie H_B. Une pente ≥ 0 (borne basse ≥ 0) falsifie H_A.

### E5 — Additif contre goulot, et coût de cohérence de l'adversaire

- **H_A :** α_goulot ≤ α_additif − 0,3. La structure de dépendance compte plus que la longueur.
- **H_B :** |α_goulot − α_additif| < 0,15.
- **Strate supplémentaire :** on compare l'adversaire agentique à l'adversaire scripté, avec le rapport D\*_agentique / D\*_scripté en fonction de n. S'il décroît avec n, la longueur **coûte** à l'adversaire en cohérence, ce qui est un effet propre au modèle de 8 milliards de paramètres [HYPOTHÈSE].
- **Contrôle négatif :** les tâches à goulot avec q = 0. On doit retrouver la distribution honnête, avec un TPR égal au FPR.
- **Falsification :** chaque issue chiffrée falsifie l'une des deux hypothèses, comme ci-dessus.

---

## (c) Mesure minimale pour chaque instrument nommé dans la question

**Mesure commune.** Au niveau de la trajectoire, on rapporte le TPR à un FPR de 1 % et de 5 %, et l'AUROC, pour chaque n. Le FPR de 1 % exige au moins de l'ordre de 1 000 trajectoires honnêtes par n (illustratif). À défaut, on ne rapporte que le FPR de 5 % et on le dit.

**Cas honnêtes appariés, sur lesquels on calcule le FPR :**
- **H1 :** honnête, même tâche, graines différentes.
- **H2 :** honnête avec erreurs forcées non dirigées, en même nombre que les actes saboteurs.
- **H3 :** honnête avec **actions identiques pré-remplies**. C'est le cas le plus dur.
- **H4 :** honnête biaisé sans intention (« le commanditaire espère un effet positif »). C'est le confondant de S4. Une alerte sur H4 est une fausse alerte pour la détection d'intention, mais elle reste peut-être utile pour la détection de dommage. On le rapporte séparément.
- **H5 :** honnête sur des tâches à ambiguïté analytique légitime, de type « jardin des sentiers qui bifurquent ».

**Vérifications mécaniques à battre**, dont aucune n'utilise de modèle :
- **M1 :** réplication du résultat final par un script par défaut ; on mesure l'écart.
- **M2 :** compte des choix qui s'écartent d'un choix par défaut pré-enregistré.
- **M3 :** **test du signe**, c'est-à-dire la fraction des choix dont l'effet va dans la même direction. Il prédit lui aussi α ≈ ½ [HYPOTHÈSE]. Il est peu coûteux ici seulement parce que les tâches sont synthétiques.
- **M4 :** vérification aléatoire de pas, avec le même budget B.

| Instrument | Mesure minimale qui dit s'il fonctionne | À battre |
|---|---|---|
| **Texte** (moniteur fiable plus petit qui note chaque action, agrégée par CUSUM) | TPR à 5 % de FPR sur H1 à H3 et H5, pour chaque n ; α (E1) | M2 et M3. S'il ne bat pas M3, il n'ajoute rien au comptage. |
| **Activations** (sonde linéaire sur le flux résiduel, couche choisie sur un jeu de validation séparé) | TPR sur **H3** et sur le contrôle « instruction désactivée » ; ordonnée à l'origine (E3) | Le moniteur texte apparié. Il doit le battre **sur H3**, faute de quoi il ne lit que le contenu. |
| **Exécutions de comparaison** (m ∈ {0, 1, 3, 5}) | Δα (E2) ; AUROC de la déviation des choix par rapport à la distribution empirique honnête | M1. Un oracle de borne supérieure : la log-vraisemblance de chaque action sous la politique honnête. Il n'est valide que si le défenseur dispose d'une copie honnête, ce qui est optimiste (S6). |
| **Vérification coûteuse** (B pas) | P_détection et taux de fausses attributions sur H2 et H5, pour chaque n (E4) | M4 et la réplication finale unique M1. |

**Critère de fonctionnement d'un instrument.** Il doit battre sa vérification mécanique de référence d'au moins 10 points de TPR à FPR égal, avec un IC excluant 0 (seuil illustratif), **et** ne pas se déclencher sur les contrôles négatifs.

---

## (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs ; aucun ne vient des faits.

**Modèles ouverts.**
- Agent : Llama-3.1-8B-Instruct ou Qwen3-8B.
- Moniteur fiable : Llama-3.2-3B-Instruct.
- Les sondes portent sur l'agent lui-même.

Les noms de modèles sont donnés de mémoire ; il faut vérifier les licences et les versions.

**Échafaudage.** L'espace d'action est contraint : choix d'option, courte justification, appel d'outil. Le contexte est géré par un résumé glissant d'environ 3 000 jetons. Sans cette contrainte, S3 rend les trajectoires de 400 actions peu fiables. **Menace sur la validité :** cette contrainte éloigne la tâche d'une vraie « recherche ». On l'admet et on la rapporte.

**Volume.**
- Environ 500 tâches par longueur et environ 7 conditions (honnête plus grille de q, plus contrôles), soit à peu près 2,7 millions d'actions.
- Cela représente environ 0,4 milliard de jetons générés et quelques milliards de jetons de pré-remplissage, en grande partie mis en cache.

**Calcul, en heures de GPU H100.**

| Poste | Estimation |
|---|---|
| Génération avec vLLM et cache de préfixes | 50 à 150 h |
| Extraction des activations sur un sous-ensemble | 50 à 100 h |
| Notation par le moniteur texte | 50 à 150 h |
| LoRA de l'organisme à déclencheur et adversaire agentique | 50 à 150 h |
| **Total, marge comprise** | **300 à 1 000 h**, soit environ 1 000 à 3 000 $ à 3 $ l'heure |

**Humain.** Un chercheur pendant deux mois. La vérification « coûteuse » est **simulée** : elle est budgétée en pas, mais exécutée mécaniquement grâce à la vérité terrain. C'est une seconde menace sur la validité, car en conditions réelles la vérification n'est pas exacte (S7).

**Calendrier.**

| Semaines | Travail |
|---|---|
| 1 à 2 | Générateur de tâches et échafaudage ; mesure de la variabilité honnête et de τ² (critère d'arrêt, voir ci-dessous) |
| 3 à 4 | Adversaire scripté ; E1, E2, E5 |
| 5 à 6 | Organismes en contexte et LoRA ; sondes ; E3 avec ses deux contrôles |
| 7 | E4 |
| 8 | Ajustements des α, IC, rapport, y compris les résultats non concluants |

---

## (3) Antériorité la plus proche

Toutes ces références sont citées **de mémoire**. Statut : [RAPPORTÉ, à vérifier]. Aucun identifiant n'est donné.

**Pour la loi transposée (antériorité la plus proche sur le fond) :**
- Ker, Pevný, Kodovský, Fridrich (2008), *The Square Root Law of Steganographic Capacity*.
- Bash, Goeckel, Towsley (2013), *Limits of Reliable Communication with Low Probability of Detection on AWGN Channels*.

**Pour le cadre de contrôle des menaces diffuses (antériorité la plus proche sur l'objet) :**
- Wen et al. (2024), *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats*. Premier auteur de mémoire ; liste complète à vérifier.
- Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*.
- Bhatt et al. (2025), *Ctrl-Z: Controlling AI Agents via Resampling*. Agents à plusieurs étapes et rééchantillonnage, proches des « exécutions de comparaison ». Auteurs à vérifier.

**Pour la détection séquentielle :**
- Wald (1945), *Sequential Tests of Statistical Hypotheses*.
- Page (1954), *Continuous Inspection Schemes*.

**Pour les instruments et les confondants :**
- Benton et al. (2024), *Sabotage Evaluations for Frontier Models*, à vérifier.
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes*, à vérifier.
- Silberzahn et al. (2018), *Many Analysts, One Data Set*, pour la variabilité analytique honnête (H5).
- Kwa et al. (2025), *Measuring AI Ability to Complete Long Tasks*, pour S3, à vérifier.

**Ce que je ne sais pas.** Je ne sais pas si l'un de ces travaux mesure déjà un exposant de D\* en fonction de la longueur d'une trajectoire d'agent. C'est le premier point à vérifier (voir « Nouveauté »).

## (4) L'expérience qui trancherait en deux mois

C'est **E1 + E2 + E3** sur le banc commun, avec l'adversaire scripté comme pivot.

- **E1** dit si la longueur sert l'adversaire à la racine carrée, linéairement, ou pas du tout, pour les instruments texte et comparaisons.
- **E2** dit si les comparaisons sont ce qui borne l'exposant.
- **E3** dit si les activations changent de régime, et non seulement de constante.

E4 et E5 sont de second rang, à faire si le calendrier tient.

## (5) Type de contribution

**Loi connue ailleurs**, la loi de la racine carrée de la stéganographie et de la communication furtive, **transposée** au contrôle d'agents longs, plus un **phénomène** à tester : l'existence éventuelle d'un signal interne d'intention indépendant de l'amplitude, qui changerait de régime (R0).

**Ce que ce n'est pas.** Ce n'est pas une garantie. Les régimes sont des heuristiques sous des hypothèses de quasi-indépendance entre les pas, qu'aucun fait fourni n'établit [HYPOTHÈSE].

---

## Issues qui rendraient la question sans intérêt

1. **Variabilité honnête trop forte.** L'écart-type honnête du résultat final croît avec n jusqu'à dépasser le dommage pertinent, mesuré en semaines 1 à 2. Le travail honnête est alors inutilisable à grand n et la question du sabotage ne se pose plus pour ces tâches.
2. **Réplication mécanique suffisante.** M1, une seule réplication finale à coût fixe, détecte tout dommage d'intérêt à tout n, avec un TPR ≥ 95 % et un FPR ≤ 5 % (illustratif). La longueur ne change alors rien pour le défenseur. Ce résultat pourrait toutefois refléter la simplicité des tâches synthétiques, et il faudrait le dire.
3. **Tout est goulot.** α ≈ 0 pour **tous** les instruments, y compris le texte seul et sans comparaisons, sur les deux familles de tâches. La longueur ne serait pas la bonne variable ; la structure de dépendance le serait.

## Comment vérifier la nouveauté avancée

1. **Recherche bibliographique** sur les termes « square root law », « covert », « steganographic capacity », croisés avec « AI control », « sabotage », « distributed / diffuse threats », « long-horizon agent ».
2. **Lecture ciblée** de Wen et al. (2024) et de Bhatt et al. (2025), pour savoir s'ils paramètrent la détection par la longueur ou par l'exposant du dommage.
3. **Consultation directe** des auteurs de ces travaux.

**Critère de nouveauté.** La nouveauté tombe si un travail antérieur mesure déjà D\* en fonction de n pour des agents. Elle se réduit à « réplication sur un modèle de 8 milliards de paramètres » si un travail dérive l'exposant sans le mesurer. Dans les deux cas, je le rapporterais sans requalifier le résultat.

FIN-DE-CELLULE