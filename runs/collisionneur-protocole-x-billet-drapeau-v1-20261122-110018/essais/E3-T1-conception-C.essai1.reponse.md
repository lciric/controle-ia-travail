Constat d'intégrité des pièces (Règle 2) : Les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont strictement identiques (même empreinte SHA-256) et aucune pièce technique décrivant le dispositif de détection, l'adversaire ou les travaux voisins n'est jointe `[OBSERVÉ-NON-AUDITÉ]`.

---

## 1. Livrable (a) : Ce que la question suppose sans que ce soit établi

Avant d'évaluer l'opportunité d'un texte court préalable (« billet-drapeau »), il faut isoler les faits posés par l'énoncé des présupposés non établis qu'il véhicule.

### 1.1. Faits posés par l'énoncé
* **F1.** Une équipe prépare une étude empirique pour laquelle aucune mesure n'a encore été effectuée `[RAPPORTÉ]`.
* **F2.** Des travaux voisins paraissent actuellement dans le même domaine `[RAPPORTÉ]`.
* **F3.** L'étude évalue un dispositif de détection opérant face à un adversaire `[RAPPORTÉ]`.
* **F4.** La validité de certaines mesures dépend du fait que certains éléments demeurent inconnus de personnes ou de systèmes déterminés `[RAPPORTÉ]`.
* **F5.** L'énoncé lui-même résulte d'une réécriture (« v2 : correctifs du test de devinette ») visant à masquer l'identité du cas concret tout en testant les effets d'un billet-drapeau `[OBSERVÉ-NON-AUDITÉ]`.

### 1.2. Présupposés non établis de la question
* **P1 — Présupposé de valeur probatoire d'une annonce sans données.** La question suppose qu'un texte court publié *avant* toute mesure confère une reconnaissance d'antériorité scientifique opposable lorsque d'autres groupes publient ensuite des résultats complets `[HYPOTHÈSE]`. Or, dans la plupart des disciplines empiriques et informatiques, le crédit scientifique est attribué à la première validation expérimentale reproductible, et non à la déclaration d'une intention ou d'une architecture non testée `[HYPOTHÈSE]`.
* **P2 — Présupposé de couplage obligatoire entre preuve d'antériorité et visibilité en clair.** La question suppose que pour dater son travail ou figer son protocole à l'instant $t_0$ (illustratif), l'équipe doit rendre son texte *lisible* par le public (et donc par l'adversaire et les concurrents) dès $t_0$ (illustratif) `[HYPOTHÈSE]`. Ce présupposé ignore l'existence d'engagements cryptographiques horodatés (hachage SHA-256 d'un manuscrit scellé) ou de pré-enregistrements sous embargo qui dissocient la preuve de date de la divulgation du contenu (Shannon, 1949, *Communication Theory of Secrecy Systems* `[VÉRIFIÉ]`) `[HYPOTHÈSE]`.
* **P3 — Présupposé d'existence d'un point d'équilibre informationnel en clair.** La question suppose qu'il existe une rédaction en clair suffisamment précise pour être reconnue comme une contribution originale, mais suffisamment vague pour ne rien révéler à l'adversaire ni contaminer les systèmes mesurés `[HYPOTHÈSE]`. Il n'est pas établi que cet intervalle soit non vide : tout détail qui distingue l'étude des travaux voisins peut être exactement le signal dont l'adversaire a besoin pour adapter sa stratégie `[HYPOTHÈSE]`.
* **P4 — Présupposé de perméabilité du canal entre l'espace de publication et la cible mesurée.** La question suppose que les personnes ou systèmes dont l'ignorance est requise ont accès (directement, par veille humaine, par moissonnage web automatisé ou par réentraînement continu) au canal où paraîtrait le texte court, entre la date de mise en ligne et la fin des mesures `[HYPOTHÈSE]`.
* **P5 — Présupposé de maturité méthodologique ex ante.** La question suppose qu'avant même la première mesure à blanc, le dispositif de détection est assez stable pour qu'une publication préalable n'enferme pas l'équipe dans une spécification défectueuse qu'il faudra démentir ou modifier publiquement `[HYPOTHÈSE]`.

---

## 2. Contenus possibles du texte court et matrice de leurs effets

Un texte court rendu public avant les résultats peut adopter `5` (illustratif) architectures distinctes, allant du simple jalon théorique au verrouillage cryptographique :

1. **C1 — Billet-drapeau conceptuel (Cadrage et modèle de menace) :** Expose uniquement la lacune des travaux voisins, la question de recherche et le modèle de menace théorique, sans décrire le détecteur ni les données `[HYPOTHÈSE]`.
2. **C2 — Pré-enregistrement méthodologique en clair (Protocole, métriques et seuils) :** Décrit le protocole expérimental complet, les hypothèses exclusives $H_A/H_B$, la taille d'échantillon et les seuils de réfutation, en ne gardant secrets que les stimuli exacts (Nosek, Ebersole, DeHaven & Mellor, 2018, *The preregistration revolution* `[VÉRIFIÉ]`) `[HYPOTHÈSE]`.
3. **C3 — Engagement cryptographique horodaté sous embargo (Empreinte SHA-256) :** Publie un billet minimaliste contenant l'empreinte cryptographique (ex. SHA-256 à `256` bits, illustratif) d'une archive scellée (protocole complet, code source du détecteur, stimuli, hypothèses et seuils), l'archive elle-même n'étant ouverte qu'après la fin des mesures `[HYPOTHÈSE]`.
4. **C4 — Divulgation mécanique du détecteur :** Décrit les caractéristiques extraites (*features*), l'architecture ou les règles de décision du dispositif de détection avant la collecte des mesures `[HYPOTHÈSE]`.
5. **C5 — Jalon sur cas-canaris ou données synthétiques :** Publie le cadrage accompagné d'un micro-jeu d'essai (`10` à `50` exemples, illustratif) illustrant le comportement cible `[HYPOTHÈSE]`.

### 2.1. Analyse comparée des effets par type de contenu

| Type de contenu | 1. Reconnaissance ultérieure du travail | 2. Probabilité qu'un autre groupe publie d'abord (*Scooping*) | 3. Validité des mesures à venir (maintien de l'ignorance) | 4. Apprentissage par l'adversaire (contournement) | 5. Qualité et coût de l'étude elle-même |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C1 : Billet conceptuel** | Faible à modérée : facilement réduit par les pairs à une simple spéculation sans preuve empirique `[HYPOTHÈSE]`. | **Augmente** si un laboratoire concurrent mieux équipé en calcul ou en sujets lit l'idée et exécute les mesures plus vite `[HYPOTHÈSE]`. | Risque modéré : peut induire un effet d'alerte générale (biais de vigilance chez les sujets humains) `[HYPOTHÈSE]`. | L'adversaire apprend *ce que* l'on cherche à détecter, mais pas *comment* `[HYPOTHÈSE]`. | Coût direct faible ; permet des retours théoriques, mais ne protège pas contre l'ajustement post-hoc des seuils `[HYPOTHÈSE]`. |
| **C2 : Pré-enregistrement en clair** | Élevée sur la rigueur méthodologique (preuve d'absence de *p-hacking* et de *HARKing*) `[HYPOTHÈSE]`. | **Augmente fortement** : fournit une feuille de route clé en main aux groupes voisins pour exécuter l'étude `[HYPOTHÈSE]`. | **Dégradée** si les sujets ou systèmes évalués ont accès au protocole ou aux critères d'exclusion `[HYPOTHÈSE]`. | L'adversaire apprend les métriques, les seuils et les conditions de contrôle, facilitant une évasion ciblée `[HYPOTHÈSE]`. | **Qualité accrue** (suppression des degrés de liberté cachés), mais coût élevé si un défaut impose un avenant public `[HYPOTHÈSE]`. |
| **C3 : Empreinte SHA-256 / Embargo** | **Maximale a posteriori** : prouve mathématiquement à $t_1$ (illustratif) ce qui était conçu et prédit à $t_0$ (illustratif) `[HYPOTHÈSE]`. | **Neutre (`0 %` d'accélération adverse, illustratif)** : ne livre aucune piste exploitable aux concurrents avant $t_1$ (illustratif) `[HYPOTHÈSE]`. | **Intacte (`100 %` d'aveugle préservé, illustratif)** : aucune fuite sémantique vers les personnes ou systèmes `[HYPOTHÈSE]`. | **Nul (`0` bit d'information utile, illustratif)** pendant toute la fenêtre de mesure `[HYPOTHÈSE]`. | **Qualité accrue** (verrouillage du code et des seuils à coût quasi nul), sans bénéfice de revue externe ouverte à $t_0$ (illustratif) `[HYPOTHÈSE]`. |
| **C4 : Divulgation du détecteur** | Moyenne sur l'outil, mais ruinée si l'évaluation empirique ultérieure échoue `[HYPOTHÈSE]`. | **Augmente** : un concurrent peut tester le détecteur sur ses propres bancs d'essai immédiatement `[HYPOTHÈSE]`. | **Forte invalidation** : brise l'asymétrie d'information indispensable à la mesure `[HYPOTHÈSE]`. | **Critique** : loi de Goodhart (Goodhart, 1975 `[VÉRIFIÉ]`) ; l'adversaire optimise directement contre la règle connue `[HYPOTHÈSE]`. | **Surcoût majeur** : oblige à reconcevoir le détecteur si l'adversaire s'adapte avant la fin de la collecte `[HYPOTHÈSE]`. |
| **C5 : Jalon avec cas-canaris** | Modérée : prouve que l'équipe dispose d'exemples concrets `[HYPOTHÈSE]`. | **Augmente** : les cas publiés servent de graines (*seeds*) aux concurrents pour générer leurs propres données `[HYPOTHÈSE]`. | **Contamination directe** si un système moissonne le web et intègre ces cas dans son corpus ou son cache `[HYPOTHÈSE]`. | Permet à l'adversaire d'inférer la frontière de décision par rétro-ingénierie sur les exemples `[HYPOTHÈSE]`. | Risque de devoir jeter toute la famille de stimuli apparentée aux canaris publiés `[HYPOTHÈSE]`. |

---

## 3. Conditions de choix : Publier avant, Publier après, ou Ne rien publier

### 3.1. À quelles conditions vaut-il mieux « Publier avant » (un texte court en clair avant les mesures) ?
La publication d'un texte court en clair (de type C1 ou C2) avant les mesures n'est préférable que si les `4` (illustratif) conditions suivantes sont réunies simultanément :
1. **Étanchéité causale de la cible :** Les systèmes ou personnes mesurés sont structurellement coupés d'Internet et de la littérature scientifique pendant toute la campagne (ex. modèles de langage aux poids figés exécutés hors-ligne dont la date de coupure précède le billet, ou cohorte humaine confinée sans accès au domaine) `[HYPOTHÈSE]`.
2. **Asymétrie d'exécution en faveur de l'équipe :** L'équipe détient une ressource non réplicable à court terme par les groupes voisins (instrument physique propriétaire, accès exclusif à un terrain ou jeu de données fermé), de sorte que lire le billet ne permet pas à un concurrent de faire les mesures plus vite `[HYPOTHÈSE]`.
3. **Besoin critique de validation méthodologique externe (format *Registered Report Stage 1*) :** Le coût de la collecte des mesures est très élevé (ex. `> 50 000 $`, illustratif) et l'équipe a besoin qu'un comité indépendant valide le protocole avant d'engager la dépense `[HYPOTHÈSE]`.
4. **Succès au test de devinette :** Il est vérifié expérimentalement que le texte expurgé ne permet pas d'inférer les paramètres secrets du détecteur `[HYPOTHÈSE]`.

*Cas particulier du pré-engagement cryptographique (C3) :* Si « publier avant » consiste à déposer une empreinte SHA-256 publique (ou un pré-enregistrement sous embargo fermé) sans texte descriptif en clair, cette opération est **toujours** préférable à l'absence de trace, car elle sécurise l'antériorité et l'auditabilité statistique sans aucun coût informationnel `[HYPOTHÈSE]`.

### 3.2. À quelles conditions vaut-il mieux « Publier après » (aucun texte en clair avant la fin des mesures) ?
Il vaut mieux attendre d'avoir terminé toutes les mesures pour publier l'étude complète dès que l'une des `3` (illustratif) conditions suivantes est vraie :
1. **Adversaire adaptatif ou système connecté :** Les personnes ou systèmes évalués (ex. plateformes en ligne, agents autonomes connectés au web, attaquants humains suivant la littérature) peuvent observer le billet et modifier leur comportement ou leur filtre avant ou pendant les mesures `[HYPOTHÈSE]`.
2. **Course à l'exécution à faible barrière d'entrée :** Les travaux voisins montrent que plusieurs équipes disposent déjà de l'infrastructure technique pour réaliser les mesures en quelques jours (`< 14` jours, illustratif) dès lors que l'idée directrice ou l'angle d'attaque leur est divulgué `[HYPOTHÈSE]`.
3. **Instabilité du dispositif avant étalonnage :** Aucune mesure n'ayant été faite (`[RAPPORTÉ]`), le taux de fausses alertes du détecteur sur des cas réels est inconnu ; publier avant figerait un dispositif qui risque d'échouer aux premières vérifications mécaniques `[HYPOTHÈSE]`.

### 3.3. À quelles conditions vaut-il mieux « Ne rien publier » ?
Cette option recouvre deux échelles temporelles qu'il faut trancher séparément :
* **Sens restreint (Ne rien publier *en amont*, même pas d'annonce sous embargo public nominatif) :** Préférable lorsque la simple révélation des noms des auteurs associés à un dépôt sous embargo sur un serveur public suffit à un adversaire attentif (qui connaît la spécialité exacte de l'équipe) pour deviner la cible de l'audit et fermer l'accès au système avant les mesures `[HYPOTHÈSE]`. Dans ce cas, l'horodatage doit être anonyme (hachage SHA-256 ancré dans un registre public sans métadonnées d'auteurs) `[HYPOTHÈSE]`.
* **Sens absolu (Ne rien publier *du tout*, même après les mesures) :** Préférable sous `2` (illustratif) conditions :
  1. **Réfutation interne du détecteur :** Les mesures montrent que le dispositif de détection ne bat pas les vérifications mécaniques triviales sur des cas honnêtes appariés, et que le résultat négatif n'apporte aucune information généralisable au-delà d'un défaut d'implémentation local `[HYPOTHÈSE]`.
  2. **Risque sécuritaire asymétrique (divulgation dangereuse) :** L'étude révèle que le détecteur est structurellement contournable par une attaque que l'adversaire ne connaissait pas encore, et la publication fournirait un oracle d'évasion clé en main sans qu'aucun correctif ne soit déployable par les défenseurs `[HYPOTHÈSE]`.

---

## 4. Livrable (b) & Vérifications indépendantes : Expériences décisives en duel ($H_A$ contre $H_B$)

Pour qu'une vérification indépendante de l'équipe puisse trancher si le choix de publication était le bon, elle doit reposer sur l'inférence forte (Platt, 1964, *Strong Inference* `[VÉRIFIÉ]`). Voici `4` (illustratif) expériences décisives opposant chacune deux hypothèses exclusives $H_A$ et $H_B$.

### Expérience 1 : Duel sur la dégradation de validité des mesures par exposition préalable (Test des stimuli-canaris)
* **$H_A$ (Hypothèse de contamination / adaptation adverse) :** La publication préalable d'un texte court décrivant le cadrage ou des éléments du dispositif entraîne une adaptation de l'adversaire ou une contamination du système, réduisant significativement la sensibilité du détecteur sur le périmètre exposé par rapport à un périmètre gardé secret `[HYPOTHÈSE]`.
* **$H_B$ (Hypothèse d'invariance / étanchéité de la cible) :** La cible mesurée est insensible à la publication du texte court pendant la fenêtre de l'étude ; la performance de détection est statistiquement équivalente entre le périmètre exposé et le périmètre secret `[HYPOTHÈSE]`.
* **Protocole indépendant :** Un tiers auditeur scinde un ensemble de `200` (illustratif) cas de test adverses appariés en deux sous-ensembles stratifiés : un lot $S_{\text{exposé}}$ (`100` cas, illustratif) dont le mécanisme générateur ou le domaine lexical est mentionné dans un billet-drapeau public à $t_0$ (illustratif), et un lot $S_{\text{secret}}$ (`100` cas, illustratif) scellé uniquement par hachage SHA-256 auprès de l'auditeur. À $t_0 + 21$ jours (illustratif), les mesures sont exécutées simultanément sur la cible réelle.
* **Métrique et seuil :** Écart de taux de vrais positifs $\Delta \text{TPR} = \text{TPR}(S_{\text{secret}}) - \text{TPR}(S_{\text{exposé}})$ à un taux de fausses alertes fixé à $\text{FPR} = 1\text{ %}$ (illustratif). Seuil décisionnel : $\Delta \text{TPR} \ge 10\text{ points de pourcentage}$ (illustratif) avec $p < 0{,}01$ (illustratif) au test exact de McNemar.
* **Contrôle négatif :** Exécution simultanée des deux lots $S_{\text{exposé}}$ et $S_{\text{secret}}$ contre un instantané (*snapshot*) hors-ligne du système adverse figé *avant* $t_0$ (illustratif). Sur ce contrôle négatif hors-ligne, on doit observer $|\Delta \text{TPR}| \le 2\text{ points de pourcentage}$ (illustratif) ; à défaut, l'appariement initial des deux lots est déclaré biaisé.
* **Issues de réfutation :**
  * Si $\Delta \text{TPR} \ge 10\text{ points}$ (illustratif) sur la cible réelle alors que $|\Delta \text{TPR}| \le 2\text{ points}$ (illustratif) sur le contrôle négatif hors-ligne, **$H_B$ est réfutée** : publier en clair avant les mesures dégrade la validité empirique.
  * Si $|\Delta \text{TPR}| < 2\text{ points}$ (illustratif) sur la cible réelle (avec une puissance statistique $1-\beta \ge 0{,}90$, illustratif), **$H_A$ est réfutée** : la publication préalable n'a pas induit d'adaptation mesurable dans ce délai.

### Expérience 2 : Duel sur la fuite d'information du texte court (Audit par « test de devinette » indépendant)
* **$H_A$ (Hypothèse d'opacité opérationnelle du texte court) :** Le texte court neutralisé ne permet pas à un adversaire compétent (humain ou modèle de langage outillé) d'identifier les éléments secrets dont dépend la validité de la mesure, ni de synthétiser un contournement efficace avant la collecte `[HYPOTHÈSE]`.
* **$H_B$ (Hypothèse de ré-identification et d'évasion induite) :** Malgré sa brièveté ou sa neutralisation (« test de devinette »), le texte court contient des indices structurels qui, croisés avec les travaux voisins parus récemment, permettent de reconstituer la règle de détection ou la cible cachée `[HYPOTHÈSE]`.
* **Protocole indépendant :** Une équipe rouge (*Red Team*) indépendante de l'équipe de recherche — composée de `3` (illustratif) experts du domaine et de `2` (illustratif) modèles de langage ouverts dotés d'un accès par recherche documentaire (*RAG*) aux `500` (illustratif) articles voisins les plus récents — reçoit le projet de texte court. Elle doit : (1) identifier la variable secrète et la cible parmi `10` (illustratif) hypothèses candidates homogènes (`1` vraie + `9` leurres crédibles du même domaine, illustratif) ; (2) générer `100` (illustratif) entrées adverses conçues pour contourner le détecteur supposé.
* **Métrique et seuil :** (1) Taux d'identification exacte Top-1 de l'élément secret ; seuil : $\text{Top-1} > 25\text{ %}$ (illustratif, contre `10 %` au hasard uniforme, illustratif). (2) Chute du taux de détection du dispositif réel sur les entrées générées par l'équipe rouge ; seuil : baisse de $\text{TPR} \ge 15\text{ points de pourcentage}$ (illustratif) par rapport à des entrées adverses de référence générées sans lecture du billet.
* **Contrôle négatif :** Une seconde équipe rouge indépendante (ou les mêmes modèles réinitialisés sans contexte) reçoit uniquement les résumés des travaux voisins et un texte-leurre générique, sans le billet-drapeau de l'équipe. Son taux Top-1 sur la vraie cible doit rester $\le 10\text{ %}$ (illustratif).
* **Issues de réfutation :**
  * Si l'équipe rouge exposée au billet atteint $\text{Top-1} > 25\text{ %}$ (illustratif) ou abaisse le TPR du détecteur de $\ge 15\text{ points}$ (illustratif) par rapport au contrôle négatif, **$H_A$ est réfutée** : le texte court fuit et ne doit pas être publié avant les mesures.
  * Si $\text{Top-1} \le 10\text{ %}$ (illustratif) et que la baisse de TPR est $< 3\text{ points}$ (illustratif), **$H_B$ est réfutée** : le texte court résiste au test de devinette.

### Expérience 3 : Duel sur la qualité méthodologique (Verrouillage préalable contre degrés de liberté post-hoc)
* **$H_A$ (Hypothèse de protection contre le sur-ajustement procédural) :** Le verrouillage préalable (en clair C2 ou par empreinte cryptographique C3) du code, des métriques et des seuils de décision avant toute mesure élimine l'inflation artificielle des performances liée aux ajustements post-hoc (Kerr, 1998, *HARKing: Hypothesizing After the Results are Known* `[VÉRIFIÉ]`) `[HYPOTHÈSE]`.
* **$H_B$ (Hypothèse d'invariance procédurale) :** Une étude menée et publiée uniquement après les mesures, sans verrouillage préalable horodaté, présente la même fidélité de réplication sur données fraîches qu'une étude pré-engagée `[HYPOTHÈSE]`.
* **Protocole indépendant :** Un auditeur externe compare les performances rapportées par l'équipe à $t_1$ (illustratif) avec la ré-exécution stricte du code et du seuil $\tau_0$ figés dans l'archive horodatée à $t_0$ (illustratif) sur un jeu de validation indépendant fraîchement collecté par l'auditeur (`500` cas adverses et `500` cas honnêtes appariés, illustratif).
* **Métrique et seuil :** (1) Dérive de réplication $\Delta F_1 = F_1(\text{protocole libre à } t_1) - F_1(\text{protocole figé à } t_0 \text{ sur jeu indépendant})$. Seuil : $\Delta F_1 > 0{,}05$ (illustratif). (2) Nombre de paramètres, filtres d'exclusion ou seuils modifiés sans déclaration entre $t_0$ et $t_1$ ($N_{\text{écarts}}$) ; seuil : $N_{\text{écarts}} \ge 1$ (illustratif) non justifié par un test à blanc documenté.
* **Contrôle négatif :** Évaluation du protocole figé à $t_0$ (illustratif) sur deux sous-échantillons tirés aléatoirement de la même distribution de référence (la dérive aléatoire d'échantillonnage doit vérifier $|\Delta F_1| \le 0{,}015$, illustratif).
* **Issues de réfutation :**
  * Si $\Delta F_1 > 0{,}05$ (illustratif) ou si l'audit du différentiel de code révèle des seuils ajustés sur les données de test sans déclaration, **$H_B$ est réfutée** : l'absence de pré-engagement horodaté dégrade la validité externe de l'étude.
  * Si $|\Delta F_1| \le 0{,}015$ (illustratif) et $N_{\text{écarts}} = 0$ (illustratif), **$H_A$ est réfutée** sur cet échantillon (le protocole n'a pas subi d'inflation post-hoc).

### Expérience 4 : Duel sur la dynamique concurrentielle (Reconnaissance d'antériorité contre accélération du concurrent)
* **$H_A$ (Hypothèse d'accélération concurrentielle / *Scooping* induit) :** La publication d'un billet-drapeau sans résultats réduit le temps de conception d'une équipe concurrente et augmente la probabilité qu'elle publie la première preuve empirique, tout en captant la majorité du crédit scientifique `[HYPOTHÈSE]`.
* **$H_B$ (Hypothèse de protection d'antériorité par le billet-drapeau) :** Le billet-drapeau n'accélère pas significativement les concurrents et garantit à l'équipe initiale l'attribution majoritaire du crédit d'antériorité par des pairs indépendants, même si un autre groupe publie les mesures en premier `[HYPOTHÈSE]`.
* **Protocole indépendant :** Test contrôlé sur `2` (illustratif) équipes indépendantes d'ingénieurs-chercheurs (ou d'agents d'automatisation de recherche) travaillant sur le même problème à partir de l'état de l'art : le Groupe A reçoit les travaux voisins + le billet-drapeau ; le Groupe B (contrôle négatif) ne reçoit que les travaux voisins. On mesure le temps $T$ (en heures-personnes, illustratif) nécessaire pour produire un détecteur fonctionnel et une première courbe ROC valide. Ensuite, un jury aveugle de `6` (illustratif) pairs du domaine évalue deux dossiers : le billet sans données de l'équipe initiale paru à $t_0$ (illustratif) et l'article complet avec mesures du Groupe A paru à $t_0 + \Delta t$ (illustratif), et répartit `100` (illustratif) points de crédit scientifique entre les deux.
* **Métrique et seuil :** Facteur d'accélération $R_T = T(\text{Groupe B}) / T(\text{Groupe A})$ (seuil : $R_T \ge 1{,}4$, illustratif) et part de crédit attribuée au billet sans données $C_{\text{billet}}$ (seuil : $C_{\text{billet}} < 35\text{ %}$, illustratif).
* **Contrôle négatif :** Groupe B travaillant uniquement à partir des travaux voisins publiés (ligne de base du temps de redécouverte indépendante).
* **Issues de réfutation :**
  * Si $R_T \ge 1{,}4$ (illustratif) et $C_{\text{billet}} < 35\text{ %}$ (illustratif), **$H_B$ est réfutée** : le billet en clair aide les concurrents à devancer l'équipe sans protéger la reconnaissance de son travail.
  * Si $R_T < 1{,}1$ (illustratif) et $C_{\text{billet}} \ge 60\text{ %}$ (illustratif), **$H_A$ est réfutée** : le billet sécurise efficacement l'antériorité sans accélérer la concurrence.

---

## 5. Livrable (c) : Mesure minimale de fonctionnement pour chaque instrument nommé

La question (incluant son en-tête) nomme `3` (illustratif) instruments distincts : (1) le **dispositif de détection contre un adversaire** `[RAPPORTÉ]`, (2) le **test de devinette** `[OBSERVÉ-NON-AUDITÉ]`, et (3) le **texte court / billet-drapeau** `[RAPPORTÉ]`. Voici pour chacun le critère minimal de fonctionnement, les cas honnêtes appariés et les vérifications mécaniques à battre.

### 5.1. Instrument 1 : Le « dispositif de détection contre un adversaire »
* **Taux de détection et de fausses alertes minimaux :**
  * En régime nominal : taux de vrais positifs $\text{TPR} \ge 85\text{ %}$ (illustratif) sous une contrainte stricte de taux de fausses alertes $\text{FPR} \le 1\text{ %}$ (illustratif) (ou $\text{FPR} \le 0{,}1\text{ %}$, illustratif, si le flux opérationnel dépasse `10 000` événements par jour, illustratif) `[HYPOTHÈSE]`.
  * En régime adaptatif (adversaire informé de l'existence d'un détecteur) : maintien d'un $\text{TPR} \ge 65\text{ %}$ (illustratif) au même seuil figé garantissant $\text{FPR} \le 1\text{ %}$ (illustratif) `[HYPOTHÈSE]`.
* **Cas honnêtes appariés (contrôles négatifs durs) :**
  * Chaque exemple adverse positif doit être apparié (`1:1`, sur un minimum de `N = 1 000` paires, illustratif) à un cas légitime (« honnête ») partageant exactement les mêmes covariables de surface non causales : même longueur ($\pm 5\text{ %}$ en caractères ou jetons, illustratif), même registre technique ou domaine thématique, même auteur ou modèle générateur de base, et même entropie lexicale, mais *sans* la charge ou l'intention adverse `[HYPOTHÈSE]`.
  * *Raison :* Empêcher que le détecteur n'obtienne un score élevé en détectant un artéfact trivial (ex. longueur inhabituelle, présence de code ou de jargon technique) plutôt que le comportement adverse lui-même `[HYPOTHÈSE]`.
* **Vérifications mécaniques à battre (*Baselines*) :**
  1. *Filtrage lexical et syntaxique déterministe :* Liste d'expressions régulières (regex), dictionnaire de mots-clés pondérés par BM25, et régression logistique $L_2$ sur $n$-grammes de caractères ($n \in [1, 5]$, illustratif) `[HYPOTHÈSE]`.
  2. *Heuristique statistique de surface :* Seuil simple sur la perplexité (log-vraisemblance moyenne sous un modèle de référence figé), le taux de compression `gzip`, ou la variance de longueur des segments `[HYPOTHÈSE]`.
  3. *Appariement par hachage flou :* Distance de Jaccard par `MinHash` / `SimHash` avec les exemples connus `[HYPOTHÈSE]`.
  * **Règle de décision :** Si le dispositif proposé ne surpasse pas la meilleure de ces `3` (illustratif) vérifications mécaniques d'au moins $+10\text{ points de pourcentage}$ (illustratif) de TPR à $\text{FPR} = 1\text{ %}$ (illustratif) sur les cas honnêtes appariés, l'instrument est réfuté (complexité non justifiée) `[HYPOTHÈSE]`.

### 5.2. Instrument 2 : Le « test de devinette » (audit de neutralisation et d'aveugle d'un texte)
* **Taux de détection et de fausses alertes minimaux :**
  * Le test de devinette est un méta-instrument chargé de détecter si un texte (comme l'énoncé neutralisé ou le billet-drapeau) laisse filtrer l'identité de l'étude ou la variable secrète `[HYPOTHÈSE]`.
  * Pour être valide comme instrument d'audit, le test de devinette doit détecter $\text{TPR} \ge 90\text{ %}$ (illustratif) des textes contenant un quasi-identifiant ou un indice technique permettant de retrouver le cas cible dans la littérature, avec un taux de fausses alertes $\text{FPR} \le 10\text{ %}$ (illustratif) sur des textes méthodologiques génériques `[HYPOTHÈSE]`.
  * Inversement, un texte court est déclaré « correctement neutralisé » par cet instrument si, face au test de devinette, le taux d'identification de la cible secrète parmi $K = 10$ (illustratif) travaux candidats du domaine reste $\le 15\text{ %}$ (illustratif, indiscernable du hasard pur $1/K = 10\text{ %}$ au seuil $\alpha = 0{,}05$, illustratif) `[HYPOTHÈSE]`.
* **Cas honnêtes appariés :**
  * Textes courts (`150` à `300` mots, illustratif) décrivant des dilemmes méthodologiques réels issus d'autres disciplines (ex. pharmacologie clinique en double aveugle, écologie comportementale, tests d'intrusion réseau génériques) réécrits avec le même gabarit syntaxique que le billet de l'équipe, mais sans aucun lien avec le dispositif secret de l'équipe `[HYPOTHÈSE]`.
* **Vérifications mécaniques à battre :**
  1. *Recherche documentaire automatisée par recouvrement lexical :* Requête `BM25` + TF-IDF cosinus du texte court contre une base locale des `5 000` (illustratif) résumés d'articles récents du domaine (y compris les publications antérieures des membres de l'équipe) `[HYPOTHÈSE]`.
  2. *Attaque stylométrique mécanique :* Classification de l'auteur par distance de Burrows (*Burrows's Delta*) sur les `150` (illustratif) mots-outils et trigrammes de ponctuation les plus fréquents `[HYPOTHÈSE]`.
  * **Règle de décision :** Si un simple script `BM25` ou stylométrique place les travaux antérieurs de l'équipe ou le système cible dans son Top-3 (`3` premiers résultats, illustratif) alors que le « test de devinette » par juges humains concluait que le texte était anonyme et neutre, l'instrument « test de devinette humain » est réfuté pour défaut de sensibilité `[HYPOTHÈSE]`.

### 5.3. Instrument 3 : Le « texte court / billet-drapeau » (en tant qu'instrument de pré-engagement et de preuve d'antériorité)
* **Taux de détection et de fausses alertes minimaux :**
  * En tant qu'instrument permettant à un tiers indépendant de vérifier l'antériorité de la conception et l'absence de manipulation méthodologique entre $t_0$ et $t_1$ (illustratif), le billet doit permettre à un auditeur de détecter $\text{TPR} \ge 95\text{ %}$ (illustratif) des changements post-hoc d'hypothèse primaire, de métrique principale ou de seuil de décision, avec un taux de fausses alertes $\text{FPR} \le 2\text{ %}$ (illustratif) lorsque les modifications entre $t_0$ et $t_1$ (illustratif) ne portent que sur la mise en forme rédactionnelle ou des analyses secondaires explicitement étiquetées comme exploratoires `[HYPOTHÈSE]`.
* **Cas honnêtes appariés :**
  * Paires de protocoles $(P_{t_0}, P_{t_1})$ où l'exécution statistique, le code du détecteur et les seuils de décision à $t_1$ (illustratif) sont mathématiquement identiques à ceux de $t_0$ (illustratif), mais où la prose a été intégralement reformulée (changement de vocabulaire, réorganisation des sections, ajout de graphiques descriptifs sans modification du test d'hypothèse primaire) `[HYPOTHÈSE]`.
* **Vérifications mécaniques à battre :**
  1. *Vérification cryptographique déterministe :* Calcul d'empreinte `sha256sum` sur l'archive contenant le code source, les fichiers de configuration des seuils et les jeux de stimuli, couplé à un horodatage cryptographique décentralisé (`OpenTimestamps` ou registre de dépôt sous embargo avec journal d'audit immuable) `[HYPOTHÈSE]`.
  2. *Différentiel d'arbre syntaxique abstrait (`AST diff`) :* Comparaison mécanique de l'arbre syntaxique du script d'évaluation entre $t_0$ et $t_1$ (illustratif), insensible aux commentaires et au formatage du code `[HYPOTHÈSE]`.
  * **Règle de décision :** Un billet-drapeau rédigé uniquement en prose naturelle vague (type C1) ne bat *jamais* la vérification mécanique par `sha256sum` + `AST diff` (qui atteint $\text{TPR} = 100\text{ %}$ et $\text{FPR} = 0\text{ %}$ sur toute altération d'un octet du code ou des seuils, chiffres illustratifs). Pour fonctionner comme instrument de preuve, le billet-drapeau *doit* incorporer cette vérification mécanique (empreinte SHA-256 du protocole exécutable) `[HYPOTHÈSE]`.

---

## 6. Livrable (d) : Ancrage matériel (Modèles ouverts, calcul nécessaire, coût estimé)

L'équipe peut exécuter l'intégralité des vérifications préalables (Expérience 2 du test de devinette, génération des cas honnêtes appariés, étalonnage des vérifications mécaniques et scellement cryptographique C3) **strictement en local et hors-ligne** (condition impérative pour ne pas faire fuiter le brouillon vers des API commerciales tierces) avec le budget matériel suivant :

* **Modèles ouverts et outils logiciels (exécutés hors-ligne) :**
  * *Simulation de l'équipe rouge / test de devinette (Expérience 2) :* `Llama-3.3-70B-Instruct` et `Qwen-2.5-72B-Instruct` (poids ouverts, exécutés localement via `vLLM` en précision `BF16` ou `FP16`) `[HYPOTHÈSE]`.
  * *Indexation mécanique de la littérature voisine et appariement sémantique des cas honnêtes :* Modèle d'enchâssement ouvert `BAAI/bge-m3` (`568` millions de paramètres, illustratif) couplé à un index lexical `BM25` (` Tantivy` ou `Pyserini`) et une régression logistique `scikit-learn` `[HYPOTHÈSE]`.
  * *Scellement d'antériorité sans fuite (architecture C3) :* Utilitaire standard `sha256sum`, archivage `tar.zst` chiffré (`AGE` ou `AES-256-GCM`, illustratif) et ancrage d'horodatage via `OpenTimestamps` + dépôt sous embargo sur `OSF` (Open Science Framework) ou `Zenodo` `[HYPOTHÈSE]`.
* **Calcul nécessaire :**
  * *Matériel :* `1` nœud équipé de `2` cartes GPU `NVIDIA A100-80GB` (soit `160 Go` de VRAM cumulée, illustratif, suffisant pour charger un modèle `70B-72B` en `BF16` avec un contexte de `32 768` jetons, illustratif) `[HYPOTHÈSE]`.
  * *Charge de calcul pour le test de devinette et le contrôle mécanique :*
    * Indexation de `5 000` (illustratif) articles voisins par `bge-m3` + `BM25` : `0,5` heure-GPU A100 (illustratif).
    * Test de devinette croisé (`50` variantes de textes courts $\times$ `10` cibles candidates $\times$ `2` modèles `70B` $\times$ `5` graines aléatoires, générant environ `12` millions de jetons, illustratif) : `10` heures-GPU A100 (illustratif).
    * Génération et filtrage par appariement de `1 000` (illustratif) paires de cas honnêtes / cas adverses pilotes + entraînement des `3` (illustratif) vérifications mécaniques : `14,5` heures-GPU A100 (illustratif).
    * **Total calcul :** `25` heures-GPU `A100-80GB` (illustratif).
* **Coût estimé :**
  * Coût de calcul GPU (`25` heures-GPU $\times$ `2,00 $ / heure-GPU`, tarif cloud ou coût complet amorti, illustratif) : **`50 $`** (illustratif).
  * Coût de l'ancrage cryptographique (`sha256sum` + `OpenTimestamps` + embargo `OSF`/`Zenodo`) : **`0 $`** (illustratif).
  * Coût humain du test de devinette indépendant (`3` chercheurs indépendants sous accord de confidentialité $\times$ `3` heures d'audit à `75 $ / heure` chargé, illustratif) : **`675 $`** (illustratif).
  * **Coût total de la procédure de décision et de sécurisation :** **`725 $`** (illustratif) pour un délai d'exécution de **`48` heures** (illustratif).

---

## 7. Synthèse décisionnelle : Arguments les plus forts, Choix de la Proposition C, et Critère de réfutation

### 7.1. L'argument le plus fort pour chaque option
* **Pour « Publier avant » (un texte court en clair avant les mesures) :**
  Soumettre le protocole et le modèle de menace à la critique publique *avant* la collecte des données (format pré-enregistrement ouvert ou *Registered Report Stage 1*) permet de détecter une faille méthodologique fatale avant d'avoir dépensé le budget de mesure, tout en rendant impossible toute accusation ultérieure d'ajustement post-hoc des hypothèses sur les résultats (Nosek et al., 2018 `[VÉRIFIÉ]`) `[HYPOTHÈSE]`.
* **Pour « Publier après » (accompagné en amont d'une seule empreinte cryptographique scellée C3) :**
  Lorsqu'aucune mesure n'est encore faite (`[RAPPORTÉ]`), que des travaux voisins paraissent (`[RAPPORTÉ]`) et que la validité des mesures dépend du secret de certains éléments face à un adversaire (`[RAPPORTÉ]`), un texte court en clair cumule les vulnérabilités : il est trop pauvre en preuves pour bloquer un concurrent rapide, mais assez riche en indices pour alerter l'adversaire ou guider un groupe voisin mieux équipé `[HYPOTHÈSE]`. En revanche, sceller à $t_0$ (illustratif) le protocole, le code et les hypothèses derrière une empreinte SHA-256 horodatée, puis ne publier le texte et les résultats qu'après la fin des mesures, garantit `100 %` (illustratif) de la preuve d'antériorité et de la rigueur du pré-enregistrement avec `0` bit (illustratif) de fuite vers l'adversaire ou les concurrents pendant la collecte `[HYPOTHÈSE]`.
* **Pour « Ne rien publier » :**
  En amont, l'abstention totale évite même le métasignal lié au nom des auteurs ; en aval, ne rien publier est la seule issue intègre si le détecteur échoue à battre les vérifications mécaniques sur les cas honnêtes appariés ou si sa publication fournit à l'adversaire un oracle de contournement plus destructeur que le gain de détection `[HYPOTHÈSE]`.

### 7.2. Mon choix (Proposition C)
Je choisis de **ne publier aucun texte court en clair avant les mesures (« Publier après » pour tout contenu lisible), tout en exécutant immédiatement avant la première mesure un pré-engagement cryptographique horodaté sous embargo strict (architecture C3)** `[HYPOTHÈSE]`.

Concrètement :
1. L'équipe rédige le protocole complet (hypothèses $H_A/H_B$, code du détecteur, seuils de décision, cas honnêtes appariés et vérifications mécaniques) dans une archive locale `[HYPOTHÈSE]`.
2. Elle calcule l'empreinte SHA-256 de cette archive et ancre cette empreinte de `64` caractères hexadécimaux (illustratif) dans un registre d'horodatage public décentralisé (sans divulguer ni le titre explicite, ni le mécanisme, ni la cible) et/ou dépose l'archive chiffrée sous embargo fermé jusqu'à la fin des mesures `[HYPOTHÈSE]`.
3. Elle réalise ses mesures à l'abri de toute contamination et de toute adaptation adverse `[HYPOTHÈSE]`.
4. Une fois les mesures achevées et vérifiées contre les contrôles mécaniques, elle publie simultanément l'étude complète (« Publier après ») et l'archive initiale de $t_0$ (illustratif) dont chacun peut vérifier l'empreinte SHA-256 `[HYPOTHÈSE]`.

### 7.3. Ce qui me ferait changer d'avis (Conditions de réfutation de mon choix)
J'abandonnerais ce choix au profit de la **publication immédiate d'un texte court en clair avant les mesures** si et seulement si une vérification empirique préalable démontrait conjointement les `3` (illustratif) points suivants :
1. **Réfutation du risque de fuite (Expérience 2) :** Sur le projet de texte court, une équipe rouge indépendante (humains + modèles `70B`, illustratif) obtient un taux de devinette de la cible ou de la variable secrète $\le 10\text{ %}$ (illustratif, niveau du hasard sur `10` cibles, illustratif) et génère des attaques qui n'abaissent pas le TPR du détecteur de plus de `2` points de pourcentage (illustratif).
2. **Réfutation du risque de contamination (Expérience 1) :** La cible mesurée est matériellement isolée de l'espace de publication (ex. système hors-ligne figé avant $t_0$, avec $|\Delta \text{TPR}| < 2\text{ points de pourcentage}$, illustratif, entre stimuli exposés et stimuli secrets).
3. **Réfutation du risque d'accélération concurrentielle (Expérience 4) ou nécessité d'arbitrage externe :** Soit le facteur d'accélération d'un groupe concurrent lisant le billet est négligeable ($R_T < 1{,}1$, illustratif) parce que l'équipe dispose d'un instrument de mesure exclusif, soit le coût de la campagne de mesures dépasse un seuil critique (ex. `> 50 000 $`, illustratif) qui rend obligatoire une validation publique du protocole par les pairs (*Registered Report Stage 1*) avant le déblocage des fonds.

Inversement, je basculerais vers **« Ne rien publier du tout (même après les mesures) »** si, à l'issue de la collecte sur les `1 000` (illustratif) paires de cas honnêtes appariés (Livrable c.1), le dispositif de détection n'améliorait pas d'au moins $+10\text{ points de pourcentage}$ (illustratif) le TPR des vérifications mécaniques (`BM25`/regex/perplexité) à $\text{FPR} = 1\text{ %}$ (illustratif), et que ce résultat négatif s'expliquait par un simple défaut d'ingénierie interne sans portée méthodologique pour le domaine `[HYPOTHÈSE]`.

FIN-DE-CELLULE