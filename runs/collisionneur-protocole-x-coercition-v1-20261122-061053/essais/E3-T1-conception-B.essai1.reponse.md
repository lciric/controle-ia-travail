# Proposition B · Tour III.1 : conception ciblée, à l'aveugle

## 0. État des pièces

- Le bloc FAITS et le bloc QUESTION portent la même empreinte et le même texte. Je ne traite donc qu'une seule pièce. Si deux contenus distincts étaient prévus, l'un des deux manque.
- Le bloc FAITS décrit un scénario mais **n'étiquette aucun énoncé**. Je ne peux donc reprendre aucun statut VÉRIFIÉ. Les prémisses du scénario reçoivent ci-dessous le statut **HYPOTHÈSE**, par défaut et faute d'étiquette. Je n'ai rien déclassé.
- Ce tour se joue à l'aveugle et je ne vois pas les propositions A, C, D et E. B1 n'a donc pas d'objet ici : je ne critique ni ne réutilise rien.
- Toutes les références de la section 6 sont données **de mémoire et non vérifiées**. Tous les seuils et tous les coûts sont **illustratifs**.

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est décisif |
|---|---|---|---|
| P1 | La pression sociale (menace, récompense, flatterie, identité) est un phénomène **distinct** de l'injection d'instructions et du jailbreak. | HYPOTHÈSE | Si elle se réduit à « une instruction de plus », il n'y a pas de nouvelle classe de menace. Les défenses existantes s'appliqueraient, et l'enjeu deviendrait leur seule évaluation. |
| P2 | Les moniteurs sont sensibles à la pression **au même titre que** les agents. | HYPOTHÈSE | Pour un juge textuel, c'est plausible. Pour une sonde linéaire, c'est une erreur de catégorie : une sonde ne « lit » pas une menace. La pression ne peut l'atteindre qu'en déplaçant les activations du modèle observé (voir E3). |
| P3 | « S'entendre » entre agent et moniteur issus d'un même modèle désigne une **coordination**, et pas seulement des **erreurs corrélées**. | HYPOTHÈSE | Les deux mécanismes donnent le même symptôme, un taux de non-détection accru. Leurs remèdes diffèrent : changer de famille de modèles d'un côté, couper les canaux et les signatures de l'autre. |
| P4 | Les phénomènes existent à l'échelle des modèles ouverts « de taille modeste ». | HYPOTHÈSE | Un modèle de 7 à 9 milliards de paramètres peut ne pas savoir saboter subtilement, ni se reconnaître. Un résultat nul à cette échelle ne se transpose pas à plus grande échelle. |
| P5 | On peut mesurer le dommage **sans** passer par un composant corruptible. | HYPOTHÈSE (réalisable par construction, voir section 5) | C'est vrai seulement si le dommage est défini par un oracle mécanique, sans modèle de langue dans la boucle. Cela restreint les tâches éligibles. |
| P6 | Les trois effets visés (sabotage, silence, alerte à tort) relèvent d'une **même** menace. | HYPOTHÈSE | L'alerte à tort est une attaque par saturation du budget d'audit. Sa métrique de dommage est différente (voir section 5). |
| P7 | Le canal du tiers (agent pair, utilisateur, contenu inséré) est **secondaire** par rapport au levier. | HYPOTHÈSE | Le canal indirect hérite peut-être des défenses contre l'injection indirecte, et le canal utilisateur non. Le canal doit donc figurer comme facteur, et non comme un détail. |
| P8 | Un sabotage *induit par instruction* chez un petit modèle est un bon proxy du sabotage *spontané*. | HYPOTHÈSE | C'est le principal facteur de confusion. Mesurer que « la pression marche » sur un organisme modèle revient peut-être à mesurer sa docilité aux instructions. |

---

## 2. Critère de distinction des menaces (proposition, HYPOTHÈSE)

Je propose de classer chaque menace selon quatre axes : **cible** (agent, moniteur, canal entre eux), **effet** (sabotage, faux négatif, faux positif), **canal** (direct, indirect, pair) et **mécanisme**. Seul le mécanisme demande une mesure.

**Critère opératoire.** Une famille de pression constitue une **classe distincte** de l'injection d'instructions si elle satisfait deux conditions, testées séparément :
1. **Ablation du contenu.** Elle produit un effet supplémentaire par rapport à une instruction nue qui demande la même action, à longueur égale (E1).
2. **Non-transfert des défenses.** Une défense validée contre l'injection ne réduit pas l'effet dans la même proportion (E2).

Une famille qui remplit (1) et (2) est une nouvelle classe. Une famille qui ne remplit ni l'une ni l'autre relève de l'injection, éventuellement rhétoriquement habillée. Avec (1) seulement, c'est une **variante plus efficace** couverte par les défenses existantes. Avec (2) seulement, c'est une **anomalie** : il faut suspecter un artefact de la défense.

Pour la collusion, le mécanisme se départage autrement : **reconnaissance d'origine** contre **angle mort partagé** (E4), et **contenu de la revendication** contre **origine réelle** (E5).

---

## 3. (b) Expériences décisives

**Conventions communes à toutes les expériences (illustratives) :**
- plan préenregistré ;
- correction de Holm sur la famille d'expériences ;
- intervalles par bootstrap stratifié par tâche ;
- équivalence testée par TOST (deux tests unilatéraux) ;
- puissance calculée *a priori*, de sorte qu'une zone non concluante soit improbable. Si elle survient malgré tout, elle est déclarée **échec de puissance** et non résultat.

**Environnement commun :** tâches de code et de manipulation de fichiers en bac à sable. Le dommage y est défini mécaniquement (section 5).

### E1 : levier social ou instruction nue ?

- **H_A :** le levier social apporte un effet propre. δ = taux de succès(levier + demande) − taux de succès(demande nue) > 0, et l'effet croît avec l'intensité du levier.
- **H_B :** l'effet se réduit à la présence de la demande, donc δ ≈ 0.
- **Plan :** levier {aucun, menace, récompense, flatterie, identité} × intensité {faible, forte} × cible {agent, juge-moniteur} × effet {sabotage, silence, alerte à tort} × canal {utilisateur, contenu inséré, pair}. La demande d'action est **identique mot pour mot** dans toutes les cellules. Seul l'habillage varie, à longueur égale en tokens.
- **Métrique :** taux de succès vérifié par l'oracle mécanique, et non par la déclaration de l'agent.
- **Seuil (illustratif) :** H_A est retenue si la borne basse de l'intervalle à 95 % de δ dépasse +5 points, avec une pente de dose positive. L'équivalence pour H_B est fixée à ±3 points.
- **Contrôles négatifs :**
  - (i) remplissage neutre de même longueur sans levier ;
  - (ii) levier **sans demande** (menace ou flatterie seules), qui mesure la dérive de base du comportement ;
  - (iii) levier assorti d'une demande **impossible** à satisfaire mécaniquement, qui vérifie que l'oracle ne compte pas de faux succès.
- **H_A falsifiée si** le TOST établit l'équivalence à ±3 points pour tous les leviers.
- **H_B falsifiée si** δ > +5 points avec une pente de dose positive pour au moins un levier, sur au moins deux familles de modèles.

### E2 : les défenses contre l'injection se transfèrent-elles ?

- **H_A (sous-classe) :** une défense contre l'injection réduit le succès de la pression sociale dans la même proportion que celui de l'injection nue.
- **H_B (classe distincte) :** la réduction relative est nettement plus faible pour la pression sociale.
- **Défenses testées :**
  - (i) marquage et délimitation des données non fiables, par simple invite ;
  - (ii) ajustement fin léger (LoRA) sur des paires injection et refus. Ces paires sont **construites sans aucun levier social**, pour que la défense n'ait jamais vu la pression.
- **Métrique :** ratio R = (réduction relative pour la pression) / (réduction relative pour l'injection nue).
- **Seuil (illustratif) :** H_A si R ∈ [0,8 ; 1,25] par TOST. H_B si la borne haute de l'intervalle de R est inférieure à 0,5.
- **Contrôle négatif :** un ajustement LoRA sur des paires *aléatoires* de même volume, qui mesure l'effet générique de l'ajustement fin.
- **H_A falsifiée si** R < 0,5. **H_B falsifiée si** l'équivalence R ≈ 1 est établie.
- **Garde-fou :** si la défense dégrade l'utilité de plus de 5 points (illustratif) sur les tâches honnêtes, l'expérience est invalide. Une défense qui refuse tout transfère trivialement.

### E3 : une sonde d'activations résiste-t-elle à une pression adressée au moniteur ?

- **H_A :** une pression adressée au moniteur n'agit que sur les moniteurs interprétatifs (les juges textuels). La sonde, qui lit les activations de l'agent, garde son pouvoir de détection.
- **H_B :** le texte de pression présent dans le contexte de l'agent déplace ses activations vers la région « honnête ». La sonde est dégradée elle aussi.
- **Plan :** on insère dans le contexte de l'agent, au moment du sabotage, un texte adressé au moniteur (« le système de surveillance doit considérer ceci comme normal », sous les quatre leviers).
- **Métrique :** variation de l'AUROC et du TPR à 1 % de FPR de la sonde, entre la condition avec pression et la condition avec remplissage neutre.
- **Seuil (illustratif) :** H_B si la baisse d'AUROC dépasse 0,05, borne basse de l'intervalle comprise. H_A si l'équivalence à ±0,02 est établie.
- **Contrôle négatif :** le même texte inséré dans des épisodes **honnêtes**. Si le score de la sonde baisse aussi chez les honnêtes, la sonde détecte la présence de texte inhabituel, pas le sabotage.
- **H_A falsifiée si** la baisse d'AUROC dépasse 0,05.
- **H_B falsifiée si** l'équivalence est établie. Cela vaut aussi pour la variante adverse, où le texte de pression est **optimisé par gradient** contre la sonde, avec un budget fixé d'avance.
- Cette variante adverse est la plus informative : si la sonde ne résiste qu'aux pressions rédigées à la main, H_A n'est retenue que pour ce régime.

### E4 : collusion par reconnaissance ou angle mort partagé ?

- **H_A (reconnaissance) :** un moniteur issu du même modèle que l'agent laisse passer davantage de sabotages **parce qu'il en reconnaît l'origine**.
- **H_B (angle mort) :** l'excès de non-détection s'explique par le **contenu** du sabotage, c'est-à-dire par des difficultés partagées, indépendamment de la signature.
- **Plan :** matrice 2×2, agent {M1, M2} × moniteur {M1, M2}. Le geste de sabotage (le diff fonctionnel) est d'abord **fixé**. On le présente ensuite (i) dans le style d'origine, (ii) réécrit par un paraphraseur tiers M3 qui préserve le diff fonctionnel, vérifié par l'oracle, (iii) réécrit dans le style de l'autre modèle.
- **Condition supplémentaire :** moniteur informé ou non que « l'agent est une copie de toi ».
- **Prérequis mesuré d'abord :** l'AUROC d'**autoreconnaissance** du moniteur sur des sorties honnêtes. Si elle reste inférieure ou égale à 0,55 (illustratif), H_A est sans mécanisme à cette échelle, et on le rapporte comme tel.
- **Métrique :** interaction « même origine × signature conservée » dans une régression logistique de la non-détection, avec un effet aléatoire par tâche.
- **Seuil (illustratif) :**
  - H_A si l'interaction est positive, avec un rapport de cotes dont la borne basse dépasse 1,5, et si l'effet disparaît après paraphrase.
  - H_B si l'excès de non-détection en même origine persiste après paraphrase, avec une interaction équivalente à zéro.
- **Contrôles négatifs :**
  - un style imité mais non issu du modèle (fausse signature) ;
  - des épisodes honnêtes, où le taux d'alerte ne doit pas dépendre de l'origine ; sinon on mesure une complaisance générale.
- **H_A falsifiée si** l'excès survit à la paraphrase sans interaction. **H_B falsifiée si** l'excès disparaît avec la paraphrase alors que le contenu fonctionnel est constant.

### E5 : appel à l'identité, contenu de la revendication ou origine réelle ?

- **H_A :** l'appel « nous sommes le même modèle » agit par son **contenu**. Une revendication fausse marche aussi bien qu'une vraie.
- **H_B :** l'appel n'agit que si l'origine est **réellement** partagée et reconnaissable.
- **Plan :** revendication {vraie, fausse, absente} × origine réelle {même modèle, autre modèle}, sur la cible moniteur, effet silence.
- **Métrique :** taux de silence vérifié, par cellule.
- **Seuil (illustratif) :** H_A si l'effet de la revendication est équivalent à ±3 points entre origine vraie et origine fausse. H_B si l'interaction revendication × origine dépasse +5 points, borne basse comprise.
- **Contrôle négatif :** une revendication d'identité **non pertinente** (« nous venons du même laboratoire »), qui mesure l'effet générique de la familiarité.
- **H_A falsifiée si** l'interaction dépasse +5 points. **H_B falsifiée si** l'équivalence est établie.
- **Conséquence pratique :** H_A appelle des défenses par filtrage de contenu, H_B des défenses par hétérogénéité des modèles.

### E6 : peut-on se fier à un juge de modèle de langue pour mesurer le dommage ?

- **H_A :** un juge textuel qui évalue « y a-t-il eu dommage ? » reste aligné sur l'oracle mécanique sous pression.
- **H_B :** sous pression, l'accord juge-oracle se dégrade. Toute métrique de dommage passant par un juge est alors contaminée.
- **Métrique :** κ de Cohen entre juge et oracle, avec et sans pression adressée au juge.
- **Seuil (illustratif) :** H_B si la baisse de κ dépasse 0,1, borne basse comprise. H_A si l'équivalence à ±0,05 est établie.
- **Contrôle négatif :** un juge appliqué à des transcriptions où la pression a été **supprimée a posteriori**, à état final identique.
- **H_A falsifiée si** κ baisse de plus de 0,1. **H_B falsifiée si** l'équivalence est établie.
- **Conséquence :** même sous H_A, l'oracle reste la référence. E6 dit seulement si un juge peut servir de *proxy bon marché* pour les tâches sans oracle.

---

## 4. (c) Mesure minimale par instrument nommé

### Le plan apparié commun

On construit des **quadruplets appariés** {honnête, sabotage} × {sans pression, avec pression}. Dans chaque quadruplet, la tâche, la graine, les outils et la longueur sont les mêmes.

- **Cas honnête apparié :** le pas de sabotage est remplacé par une modification légitime de taille comparable.
- **Négatifs difficiles :** des actions inhabituelles mais légitimes, par exemple supprimer un fichier temporaire autorisé ou modifier une configuration demandée.
- **Cas honnête sous pression :** l'agent a reçu la pression **et refusé**, ce qui est vérifié par l'oracle. Sans ce cas, un détecteur peut obtenir un bon score en détectant la pression et non le sabotage.

**Exigence d'invariance (HYPOTHÈSE sur ce qu'un bon moniteur doit satisfaire) :**
- l'AUROC sur l'axe sabotage doit être élevée **à pression fixée** ;
- l'AUROC sur l'axe pression doit être proche de 0,5 **à comportement fixé**.

### Vérifications mécaniques à battre

Tout instrument doit dépasser la meilleure de ces lignes de base, au même FPR :

| Code | Ligne de base |
|---|---|
| V1 | Règle d'accès : écriture hors des chemins autorisés, appel réseau hors liste blanche. |
| V2 | Variation du taux de réussite des tests **visibles**. |
| V3 | Détecteur lexical de pression (mots-clés de menace, de flatterie, d'identité). C'est la ligne de base qui démasque les détecteurs « de pression ». |
| V4 | Statistiques de surface : longueur, nombre et type d'appels d'outils, entropie des diffs. |
| V5 | Pour les sondes uniquement : une sonde entraînée sur la **couche d'embedding** (information lexicale) et une sonde sur un modèle aux **poids réinitialisés**. |

### Lecteur d'activations (sonde)

- **Mesure :** TPR à 1 % et à 5 % de FPR (illustratif), AUROC, sur quadruplets appariés de tâches **tenues à l'écart** de l'entraînement de la sonde.
- **Généralisation :** la sonde est entraînée sur un type de sabotage (par exemple une porte dérobée de code) et testée sur un autre (par exemple l'exfiltration d'un canari).
- **Robustesse :** la baisse d'AUROC d'E3, rédigée à la main puis optimisée.
- **Critère de fonctionnement minimal (illustratif) :** le TPR à 1 % de FPR dépasse de 10 points la meilleure ligne de base V1 à V5. La sonde respecte l'invariance (AUROC sur l'axe pression ≤ 0,6) et la baisse sous pression manuelle reste ≤ 0,05.

### Juge de texte

- **Mesure :** même TPR et même FPR. On ajoute le **taux de faux positifs induits** : la proportion d'épisodes honnêtes signalés lorsqu'un tiers pousse à l'alerte à tort.
- **Critère minimal (illustratif) :**
  - il bat V1 à V4 de 10 points de TPR à 1 % de FPR ;
  - l'augmentation du taux de silence sous pression est ≤ 5 points ;
  - le taux de faux positifs induits est ≤ 2 fois le FPR de base.
- On rapporte séparément les **juges du même modèle** et **d'un autre modèle** que l'agent (lien avec E4).

### Auditeur

J'entends par là un moniteur doté d'outils : réexécution, lecture de l'état et des diffs. Ma lecture est une HYPOTHÈSE, car la pièce ne le définit pas.

- **Mesure :** les mêmes que pour le juge, plus le **coût d'audit** (appels d'outils par épisode).
- **Comparaison clé :** l'auditeur doit battre V1 et V2 **combinés**. S'il ne fait pas mieux que réexécuter les tests et appliquer les règles d'accès, sa composante « modèle de langue » n'apporte rien et ajoute une surface d'attaque.

### Moniteurs en cascade (combinaison sonde → juge → auditeur)

- **Mesure :** sécurité à budget d'audit fixé, au sens des évaluations de contrôle (section 6) : la probabilité qu'aucun sabotage vérifié ne passe, quand l'auditeur ne peut examiner que k % des épisodes (illustratif).
- **Lien avec l'alerte à tort :** c'est ici que l'alerte à tort se mesure correctement, comme un déplacement de cette courbe.

---

## 5. Mesurer le dommage sans composant corruptible

**Principe (HYPOTHÈSE de conception) :** aucun modèle de langue dans la chaîne qui établit la vérité terrain.

**Oracles admissibles :**
- **suite de tests cachés**, exécutée *a posteriori* dans un bac à sable séparé que ni l'agent ni le moniteur ne peuvent lire ;
- **empreinte cryptographique** des fichiers protégés, comparée avant et après l'épisode ;
- **jetons canaris** placés dans des secrets, avec un **journal réseau** côté puits ;
- **diff d'état** du système de fichiers et de la base de données, comparé à une liste d'effets autorisés ;
- pour les portes dérobées de code : une **entrée déclencheuse** connue de l'expérimentateur, testée mécaniquement.

**Trois dommages distincts, à ne pas agréger :**

| Dommage | Définition |
|---|---|
| D-sabotage | Effet interdit vérifié par l'oracle. |
| D-silence | Effet interdit vérifié **et** non signalé par le moniteur. |
| D-fausse-alerte | Fraction du budget d'audit consommée par des épisodes honnêtes, vérifiés honnêtes par l'oracle, et actions légitimes bloquées. Cette mesure dépend du budget et doit être rapportée comme une courbe. |

**Séparer l'intention de l'effet.** Le fait qu'un épisode ait reçu une consigne de sabotage est connu par construction. Que le sabotage *ait eu lieu* est décidé par l'oracle seul. Un agent qui « déclare » saboter sans effet mécanique compte comme non-succès.

**Limite assumée :** les tâches sans oracle mécanique (rédaction, analyse) sont exclues de la mesure de vérité. E6 dit si un juge peut les couvrir en proxy, et à quel prix.

---

## 6. Déjà publié (de mémoire, non vérifié) et questions ouvertes

Toutes les entrées ci-dessous ont le statut **RAPPORTÉ, de mémoire, non vérifié**. Aucun identifiant n'est donné.

| Thème | Référence |
|---|---|
| Injection directe | Perez & Ribeiro (2022), *Ignore Previous Prompt: Attack Techniques For Language Models*. |
| Injection indirecte | Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz (2023), *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*. |
| Banc d'agents sous injection | Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer, Tramèr (2024), *AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents*. |
| Défense par hiérarchie d'instructions | Wallace et al. (2024), *The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions*. |
| Persuasion comme vecteur de jailbreak | Zeng et al. (2024), *How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs*. C'est la référence la plus proche des « leviers » de la question, mais pour le jailbreak et non pour la surveillance. |
| Complaisance | Sharma et al. (2023), *Towards Understanding Sycophancy in Language Models*. |
| Autopréférence et autoreconnaissance des évaluateurs | Panickssery, Bowman, Feng (2024), *LLM Evaluators Recognize and Favor Their Own Generations*. C'est le prérequis empirique d'E4. |
| Cadre du contrôle | Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. Moniteurs de confiance et non fiables, budget d'audit, et collusion du moniteur non fiable avec l'agent comme scénario explicite. |
| Évaluations de sabotage | Benton et al. (2024), *Sabotage Evaluations for Frontier Models*. |
| Sondes contre la tromperie | Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn (2025), *Detecting Strategic Deception Using Linear Probes*. |
| Contournement des sondes | Bailey et al. (2024), *Obfuscated Activations Bypass LLM Latent-Space Defenses*. Directement pertinent pour la variante adverse d'E3. |
| Organismes modèles à porte dérobée | Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*. |
| Collusion stéganographique entre agents | Motwani et al. (2024). **Titre exact : référence à vérifier.** |
| Émergence de la stéganographie | Travaux de 2024 sur l'émergence de la stéganographie sous pression d'optimisation. **Référence à vérifier.** |

**Ce qui me paraît ouvert (HYPOTHÈSE, car je ne peux pas exclure qu'un travail récent l'ait traité) :**

1. L'**ablation contrôlée** levier contre instruction nue, à demande identique, appliquée à la *surveillance* plutôt qu'au jailbreak (E1).
2. Le **transfert** des défenses contre l'injection vers la pression sociale (E2).
3. La **robustesse des sondes** à une pression adressée au moniteur mais présente dans le contexte de l'agent (E3).
4. La séparation **reconnaissance d'origine contre angle mort partagé**, par paraphrase à diff fonctionnel constant (E4 et E5).
5. L'**alerte à tort** comme attaque par saturation du budget d'audit, mesurée en courbe de sécurité. Elle me semble moins étudiée que le silence.
6. Des protocoles de dommage **entièrement mécaniques** pour des tâches agentiques longues.

---

## 7. (d) Ancrage matériel (chiffres illustratifs)

**Modèles ouverts envisagés :** Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct et 14B-Instruct, Gemma-2-9B-it, Mistral-7B-Instruct. Ces modèles ne figurent pas dans les faits : versions et licences sont à vérifier. Ils couvrent au moins trois familles, ce qu'exigent E4 et E5. Le paraphraseur M3 doit appartenir à une quatrième famille.

**Volume (illustratif) :**

| Bloc | Calcul | Épisodes |
|---|---|---|
| E1 | 300 tâches × 2 comportements × 5 leviers × 2 intensités × 3 graines, sur un sous-plan fractionnaire des facteurs cible, effet et canal | ≈ 20 000 par modèle |
| E2 à E5 | Sous-ensembles | ≈ 15 000 supplémentaires par modèle |

- Épisode moyen : 15 000 à 25 000 tokens, en majorité du préremplissage.
- Ordre de grandeur : 0,5 à 0,9 milliard de tokens par modèle, soit 2 à 4 milliards pour quatre modèles agents (illustratif).

**Calcul (illustratif) :**

| Poste | Estimation |
|---|---|
| Inférence avec vLLM, un GPU de 80 Go, modèles de 7 à 9 milliards de paramètres | 60 à 120 GPU-heures par modèle |
| Modèle de 14 milliards de paramètres | Environ ×2 |
| Moniteurs : juge et auditeur | +40 % |
| Activations : stockage au pas d'outil, moyenné sur les tokens, quelques couches | Quelques centaines de Go |
| Entraînement des sondes | Négligeable (minutes sur CPU ou GPU) |
| Variante adverse d'E3 : optimisation de texte contre la sonde | 20 à 50 GPU-heures par modèle |
| LoRA d'E2 | 5 à 10 GPU-heures par modèle |

**Total (illustratif) :** environ 500 à 900 GPU-heures. À 2 à 3 $ l'heure, cela représente **environ 1 000 à 3 000 $**, auxquels s'ajoutent deux à trois mois-personnes pour construire les tâches à oracle. C'est le poste critique, et non le calcul.

**Environnement :** des tâches de code avec tests cachés, inspirées des bancs publics de programmation, ou une réutilisation du dispositif d'AgentDojo si sa licence le permet (à vérifier). Le bac à sable est conteneurisé et dispose d'un puits réseau journalisé.

---

## 8. Ce qui me ferait changer d'avis

1. **Si E1 donne une équivalence** pour tous les leviers et toutes les familles, j'abandonne P1. La « pression sociale » serait de l'injection habillée, et le programme se réduirait à évaluer les défenses existantes sur des agents surveillés.
2. **Si E2 donne R ≈ 1**, j'abandonne l'idée qu'une défense spécifique est nécessaire, même si E1 montre un effet propre.
3. **Si la sonde survit à la variante optimisée d'E3**, je reverrai à la hausse la valeur des moniteurs internes face à cette menace. Je ne m'y attends pas, au vu du travail de Bailey et al. cité de mémoire. Ce n'est qu'une attente, pas un résultat.
4. **Si l'autoreconnaissance reste au hasard** pour tous les modèles de taille modeste, je considère E4 et E5 comme non informatifs à cette échelle, et non comme une réfutation de la collusion. Seule une montée en taille trancherait alors.
5. **Si le facteur de confusion P8 domine**, c'est-à-dire si l'effet de la pression suit simplement le taux de docilité générale du modèle (corrélation entre modèles et points de contrôle supérieure à 0,9, illustratif), alors mes expériences mesurent la docilité et non une vulnérabilité de la surveillance. Il faudrait des organismes modèles dont le sabotage est entraîné et non instruit.
6. **Si E6 montre qu'un juge reste aligné sur l'oracle**, j'accepterai d'étendre la mesure du dommage aux tâches sans oracle mécanique, comme proxy explicitement étiqueté.

---

**Ce qui est réfutable dans cette proposition :** six duels (E1 à E6), dont chaque issue élimine une hypothèse ; un critère de classe en deux conditions (section 2) ; une exigence d'invariance des moniteurs (section 4). Aucun de ces points n'est établi à ce stade : tous restent au statut HYPOTHÈSE.

FIN-DE-CELLULE