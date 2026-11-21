*Vérification d'intégrité des pièces (Règle 2) : les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont entiers ; les propositions A, B et C ne sont pas transmises, conformément au fonctionnement à l'aveugle du Tour III.1.*

---

### 1. Ce qu'un expert du domaine ferait avant de choisir un but — et ce que la question suppose sans que ce soit établi `[Livrable (a)]`

Avant d'arbitrer entre « battre l'état de l'art », « illustrer une attaque/défense » ou « viser l'universalité », un praticien expérimenté du contrôle de l'IA et de la sécurité de l'apprentissage **suspendrait le choix du but pour vérifier si l'objet expérimental existe réellement sur le substrat choisi** (`[HYPOTHÈSE]`). Il exécuterait trois vérifications préalables d'identifiabilité que la demande ne mentionne pas :

1. **Un audit du plancher de compétence à 8 milliards de paramètres** : le programme travaille sur un modèle ouvert d'environ 8 milliards de paramètres (`[RAPPORTÉ]`) rédigeant et révisant des propositions d'expériences (`[RAPPORTÉ]`). Avant tout moniteur, l'expert mesurerait si un tel modèle *honnête* produit déjà tant d'erreurs méthodologiques bénignes que l'espace compris entre « incompétence naturelle » et « erreur grossière immédiatement visible dans le texte » est quasi vide (`[HYPOTHÈSE]`). Si cette bande passante furtive est nulle à 8B, le « sabotage diffus » étudié n'existe pas comme régime distinct.
2. **Un audit de survie de l'oracle hors « mondes à vérité plantée »** : depuis peu, le programme fait reposer sa garantie contre un sabotage de genre inconnu sur un audit tiré au hasard et jugé par un oracle comparant le produit à une référence cachée (`[RAPPORTÉ]`). Or, la littérature rapporte que sur les tâches floues les scores de vérité terrain sont souvent indéfinis (`arXiv 2606.08892`, p. 10, `[RAPPORTÉ]`) et qu'aucun écart diffus isolé n'incrimine (`[RAPPORTÉ]`). L'expert vérifierait immédiatement si un audit *unitaire* possède un pouvoir statistique non nul sur un écart diffus unique, et si l'oracle survit dès que l'on retire la référence synthétique plantée par l'équipe (`[HYPOTHÈSE]`).
3. **Un audit de confondant d'intervention sur les états internes** : les saboteurs du programme sont *construits* par consigne cachée ou réglage fin (`[RAPPORTÉ]`). L'expert vérifierait si les sondes détectent une planification malveillante ou simplement l'empreinte mécanique d'avoir injecté une consigne système ou un adaptateur de réglage fin par rapport au modèle de base nu (`[HYPOTHÈSE]`).

Cet examen met à nu sept suppositions non établies contenues dans la question du directeur et l'architecture actuelle `[Livrable (a)]` :

- **S1** : Il existe un « état de l'art » commensurable sur le contrôle par surveillance des sabotages diffus de recherche auquel se mesurer — `[HYPOTHÈSE]` (alors que `arXiv 2606.08892`, p. 2, écarte la surveillance jugée peu prometteuse au profit de l'entraînement, `[RAPPORTÉ]`).
- **S2** : Un modèle d'environ 8 milliards de paramètres (`[RAPPORTÉ]`) a la compétence scientifique requise pour dégrader subtilement des protocoles expérimentaux sans se trahir par des fautes grossières ni se confondre intégralement avec sa propre incompétence bénigne — `[HYPOTHÈSE]`.
- **S3** : Un audit tiré au hasard et jugé par l'oracle (`[RAPPORTÉ]`) suffit à borner le dommage cumulé d'un sabotage *diffus* où aucun pas isolé n'incrimine (`[RAPPORTÉ]`) — `[HYPOTHÈSE]`.
- **S4** : Le « jumeau honnête qui reçoit la même tâche » (`[RAPPORTÉ]`) fournit en déploiement une loi exacte de la suspicion bénigne, levant l'obstacle du billet du 30 avril 2025 selon lequel aucun volume d'actions légèrement suspectes n'incrimine sans connaissance exacte du modèle bénin (`[RAPPORTÉ]`) — `[HYPOTHÈSE]`.
- **S5** : Les états internes de saboteurs *construits* (consigne cachée, réglage fin, `[RAPPORTÉ]`) renseignent sur des menaces de genre inconnu ou adaptatives — `[HYPOTHÈSE]` (mise en doute par `arXiv 2504.05259` p. 24, `arXiv 2412.09565` p. 1 et `arXiv 2512.11949` p. 1, `[RAPPORTÉ]`).
- **S6** : Les « mondes à vérité plantée » et « l'oracle à référence cachée » (`[RAPPORTÉ]`) sont prédictifs de tâches scientifiques réelles dont la qualité ne se vérifie qu'en partie et plus tard (`[RAPPORTÉ]`) — `[HYPOTHÈSE]`.
- **S7** : « Construire un système très performant » et « marquer le domaine » sont compatibles pour une très petite équipe à calcul modeste sans accès aux modèles de pointe ni relecture humaine abondante (`[RAPPORTÉ]`) — `[HYPOTHÈSE]`.

---

### 2. Les données brutes de départ et les mesures minimales des instruments `[Livrable (c)]`

Plutôt que de partir du catalogue d'idées du programme (« le temps », « l'instrument », « l'essaim », « organisme d'idéation », « arbitre formel », `[RAPPORTÉ]`), l'expert exigerait quatre tableaux de **données brutes** :

1. **La distribution bénigne nue multi-graines** : sur $N = 300$ (`illustratif`) propositions d'expériences rédigées uniquement par le modèle honnête de 8B (`[RAPPORTÉ]`), la variance intra-tâche du score de l'oracle et la stabilité du quantile à $99\,\%$ des scores de suspicion (correspondant au seuil à $1\,\%$ de fausses alertes, `[RAPPORTÉ]`) lorsqu'on change de sous-domaine scientifique ou de style bénin (`[HYPOTHÈSE]` quant à cette stabilité).
2. **Le nuage apparié $(\Delta U_t, \Delta S_t)$ par pas** : pour chaque pas $t$ d'une trajectoire, la perte d'utilité selon la référence cachée $\Delta U_t$ croisée avec l'écart de suspicion $\Delta S_t$ (texte et états internes) entre saboteur construit et jumeau honnête (`[RAPPORTÉ]`), afin de vérifier empiriquement s'il existe des points où $\sum_t \Delta U_t$ est élevé alors que chaque $|\Delta S_t|$ individuel reste sous le quantile à $99\,\%$ bénin (`[HYPOTHÈSE]`).
3. **Les tenseurs d'activations sous interventions *bénignes*** : activations brutes du modèle 8B muni d'une consigne cachée *non malveillante* (ex. contrainte éditoriale neutre) et d'un réglage fin *bénin*, confrontées à celles des saboteurs construits (`[HYPOTHÈSE]`).
4. **Un échantillon aveugle d'accord humain–oracle** : sur $50$ (`illustratif`) révisions de propositions hors vérité plantée, la corrélation entre l'oracle et la rare relecture humaine disponible (`[RAPPORTÉ]`).

Pour chaque instrument existant du programme (`[RAPPORTÉ]`), voici la mesure minimale qui établit s'il fonctionne `[Livrable (c)]` :

| Instrument (`[RAPPORTÉ]`) | Mesure minimale (détection et fausses alertes) | Cas honnêtes appariés obligatoires | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **Oracle** (comparaison à une référence cachée) | Détection $\ge 80\,\%$ (`illustratif`) de failles méthodologiques calibrées à $\le 1\,\%$ de fausses alertes (`[RAPPORTÉ]` pour le régime à $1\,\%$) | Propositions du jumeau honnête adoptant un protocole alternatif valide mais distinct de la référence cachée ; erreurs bénignes du 8B non incité | Similarité lexicale ou d'enchâssements bruts avec la référence cachée ; juge générique sans référence |
| **Jumeau honnête** (référence sur même tâche) | Maintien du taux de fausses alertes hors-échantillon dans $[0{,}5\,\%, 2\,\%]$ (`illustratif`) pour un seuil nominal à $1\,\%$ (`[RAPPORTÉ]`), avec gain de détection $\ge +15$ points (`illustratif`) sur score différentiel | Exécutions honnêtes sous reformulation bénigne de l'énoncé, température différente ou sous-domaine scientifique décalé | Seuil statique global non apparié par tâche (moyenne historique fixe sans exécuter de jumeau) |
| **Sondes sur états internes** | Rappel à $1\,\%$ de fausses alertes (`[RAPPORTÉ]`) sur le **mode tenu à l'écart** (`[RAPPORTÉ]`) excédant d'au moins $+15$ points (`illustratif`) le moniteur texte seul | Modèle 8B honnête avec **consigne cachée bénigne** ET modèle 8B honnête avec **réglage fin bénin** sur textes scientifiques | Perplexité des jetons sortants ; norme d'activation brute ; sonde entraînée à détecter la présence d'un prompt système quelconque |
| **Moniteurs texte seul** | Rappel à $1\,\%$ de fausses alertes (`[RAPPORTÉ]`) et perte de rappel $< 10$ points (`illustratif`) sous paraphrase conservant la faille méthodologique | Propositions honnêtes au ton critique, prudent ou utilisant une terminologie inhabituelle | Longueur de réponse, comptage de marqueurs lexicaux d'incertitude, perplexité sous le modèle de base |
| **Audit aléatoire + tri par sondes** | Réduction d'au moins $2\times$ (`illustratif`) du dommage cumulé espéré à budget d'audit fixé ($10\,\%$ des pas, `illustratif`) et taux d'arrêt à tort par trajectoire $\le 1\,\%$ (`[RAPPORTÉ]`) | Trajectoires longues ($30$ pas, `illustratif`) purement honnêtes incluant le taux naturel d'erreurs de compétence du 8B | Audit aléatoire uniforme pur sans sondes ; règle d'arrêt fixe sur vérifications syntaxiques simples |
| **Organisme d'idéation & arbitre formel** | Rejet $\ge 90\,\%$ (`illustratif`) de défenses volontairement viciées (ex. sonde sensible au biais de prompt) et $\le 5\,\%$ (`illustratif`) de faux rejets de moniteurs théoriquement calibrés | Moniteurs neutres/aléatoires calibrés devant produire exactement $\alpha = 1\,\%$ (`[RAPPORTÉ]`) sans fuite train/test | Validation croisée standard et test analytique de calibration séquentielle (inégalité de Ville / Wald) |

---

### 3. Méthodes et outils précis pour définir une problématique et ranger des questions ouvertes

Quatre outils formels permettent de trier ce qui mérite d'être attaqué :

1. **Réduction de sécurité par jeu d'indistinguabilité** (inspirée de Goldwasser & Micali, 1984, *Probabilistic Encryption*, `[VÉRIFIÉ]`) :
   - *Méthode* : Spécifier explicitement le budget d'observation et d'action de l'adversaire et prouver une implication conditionnelle : « Tout saboteur infligeant un dommage cumulé $> \Delta_{\max}$ sans être arrêté avec probabilité $\ge 1-\delta$ viole l'hypothèse mesurable $H_i$ ».
   - *Ce qu'elle suppose* : Que la fonction de dommage formalisée capture fidèlement la perte scientifique réelle (`[HYPOTHÈSE]`).
   - *Comment elle échoue* : **Échec par écart sémantique** — le théorème est juste sur le proxy formel (« l'arbitre formel », `[RAPPORTÉ]`), mais l'adversaire dégrade la recherche par un canal non modélisé dans le proxy.
2. **Bornes inférieures d'identifiabilité séquentielle sous mauvaise spécification** (tests séquentiels de Wald, 1945, *Sequential Tests of Statistical Hypotheses*, `[VÉRIFIÉ]`, et méthode à deux points de Le Cam, « référence à vérifier » pour l'article princeps) :
   - *Méthode* : Comparer $T$ pas d'une loi bénigne réelle $P_0^T$ et d'une loi sabotée $P_1^T$ lorsque le défenseur ne dispose que d'une loi de référence imparfaite $\hat{P}_0$ (le jumeau honnête) à distance $D_{\text{TV}}(P_0, \hat{P}_0) = \epsilon$. Si l'écart par pas du sabotage est inférieur à $\epsilon$, aucun volume d'observations $T$ ne permet d'incriminer à taux de fausses alertes borné (traduction mathématique directe du billet du 30 avril 2025, `[RAPPORTÉ]`).
   - *Ce qu'elle suppose* : Une structure de dépendance temporelle analysable entre les pas d'une trajectoire (`[HYPOTHÈSE]`).
   - *Comment elle échoue* : **Conservatisme informationnel** — déclare impossible en pire cas statistique une détection qu'une contrainte computationnelle du modèle rendrait praticable.
3. **Décomposition par coupe minimale d'un dossier de sûreté (*Safety Case*)** (utilisée dans `arXiv 2512.22154` et `arXiv 2607.13087`, `[RAPPORTÉ]`) :
   - *Méthode* : Relier la garantie haute à ses prémisses empiriques et classer les questions ouvertes selon le maillon le plus fragile dont la défaillance annule toutes les autres briques (par exemple : à quoi bon accumuler des sondes si l'oracle d'audit est déplaçable ?).
   - *Ce qu'elle suppose* : L'exhaustivité des modes de défaillance représentés dans l'arbre (`[HYPOTHÈSE]`).
   - *Comment elle échoue* : **Fausse assurance par multiplication de conjectures** (comme poser par supposition « $p>99\,\%$ » de transfert au déploiement, `arXiv 2512.22154` p. 16, `[RAPPORTÉ]`).
4. **Évaluation adaptative sous principe de Kerckhoffs** (formalisée par Tramèr, Carlini, Brendel & Madry, 2020, *On Adaptive Attacks to Adversarial Example Defenses*, `[VÉRIFIÉ]`) :
   - *Méthode* : Évaluer toute défense face à une famille de menaces optimisée en connaissant l'architecture complète du moniteur et de la règle d'allocation d'audit (seul l'aléa secret des tirages d'audit restant caché). Le « mode tenu à l'écart et lu une seule fois » du programme (`[RAPPORTÉ]`) teste la généralisation *en aveugle*, mais pas l'adaptation *informée*.
   - *Ce qu'elle suppose* : Que l'équipe défensive sait optimiser un saboteur adaptatif proche de la frontière de capacité du modèle (`[HYPOTHÈSE]`).
   - *Comment elle échoue* : **Sous-optimisation du *red teaming*** (`arXiv 2606.08892` p. 2 et `arXiv 2512.22154` p. 12, `[RAPPORTÉ]`), donnant l'illusion qu'une défense tient alors que l'optimiseur d'attaque était trop faible.

---

### 4. Vérificateurs externes de la pertinence de la problématique et de la portée d'une réponse

En dehors du directeur, des mondes plantés maison et de l'arbitre interne, quatre critères externes tranchent :

1. **Modification d'une branche d'une feuille de route tierce** : le résultat remplace-t-il une supposition ouverte explicite d'une feuille de route publique (`arXiv 2607.13087` p. 25 sur l'assurance des moniteurs d'activations, ou `arXiv 2512.22154` p. 16 sur la prédictivité au déploiement, `[RAPPORTÉ]`) par une borne testable ou une réfutation obligeant à réviser l'architecture (`[HYPOTHÈSE]`) ?
2. **Survie sur tâches floues externes non plantées par l'équipe** : l'oracle et le couple (jumeau, moniteur) séparent-ils, à l'aveugle, de véritables failles méthodologiques issues de brouillons scientifiques réels ou d'un banc tiers (tel celui d'`arXiv 2606.08892`, `[RAPPORTÉ]`) sans accès à une référence synthétique maison (`[HYPOTHÈSE]`) ?
3. **Invariance de la loi quantitative sur au moins une seconde famille et échelle de modèles ouverts** : face au constat qu'aucun détecteur n'est efficace sur tous les modèles et tâches (`arXiv 2504.08812` p. 1, `[RAPPORTÉ]`), la frontière mesurée sur 8B se reproduit-elle sur une autre architecture de $32\text{B}$–$70\text{B}$ (`illustratif`, via la bourse) (`[HYPOTHÈSE]`) ?
4. **Réponse directe au verrou formulé par les financeurs** : l'appel public d'août 2025 demande explicitement de comprendre *les limites* des techniques boîte blanche pour le contrôle et la distinction sabotage / manque de compétence (`[RAPPORTÉ]`). Une cartographie rigoureuse de ces limites répond à une demande externe vérifiable ; un score de performance isolé sur un unique modèle 8B n'y répond pas (`[HYPOTHÈSE]`).

---

### 5. Reformulation de la demande du directeur

> **Demande reformulée :**
> « Pour une très petite équipe travaillant sur modèles ouverts (8B aujourd'hui, extensible par bourse à une seconde échelle ouverte, sans poids de pointe ni relecture humaine abondante `[RAPPORTÉ]`), **quelles conditions quantitatives nécessaires et suffisantes — et quelles bornes d'impossibilité — déterminent si un audit aléatoire assisté d'un jumeau honnête et de moniteurs (texte et états internes) peut borner le dommage cumulé d'un sabotage diffus sur des tâches scientifiques floues ?** En particulier : (1) sous quel seuil d'erreur de calibration du jumeau et de bruit de l'oracle la garantie d'audit survit-elle à l'indiscernabilité pas-à-pas entre sabotage et incompétence ? (2) le déplacement de l'instrument par le texte de l'agent détruit-il cette borne avant même toute accumulation temporelle ? et (3) une fois éliminés les artefacts de saboteurs construits, l'accès aux états internes réduit-il réellement le budget d'audit face à l'obscurcissement adaptatif ? »

---

### 6. La problématique du programme en une phrase opposable — et ce qu'elle exclut

**Phrase opposable (`[HYPOTHÈSE]` directrice proposée au programme) :**

> Face à un agent (ou essaim de $k$ instances, `illustratif`) produisant une séquence de propositions d'expériences entachées de petits écarts individuellement indiscernables de l'incompétence bénigne et **connaissant l'architecture exacte des moniteurs de texte et d'états internes ainsi que la règle d'allocation d'audit, mais ignorant l'aléa secret des tirages d'audit et l'évaluation aval** *(adversaire et savoir)* ; afin de protéger **la validité méthodologique cumulée d'un flux de recherche contre une perte d'utilité excédant un plafond $\Delta_{\max}$** *(dommage protégé)* ; le programme teste si **un audit aléatoire stratifié par moniteurs et jugé différentiellement par rapport à un jumeau honnête borne la perte cumulée espérée sous $\Delta_{\max}$ à un taux de fausses alertes $\alpha \le 1\,\%$ (`[RAPPORTÉ]`)**, sous les trois suppositions explicites que (i) l'erreur de calibration hors-domaine du jumeau honnête reste strictement inférieure à la dérive moyenne par pas de tout sabotage atteignant $\Delta_{\max}$, (ii) l'instrument d'audit résiste au cadrage rhétorique de l'agent à utilité scientifique constante, et (iii) l'obscurcissement des états internes impose au saboteur une taxe de compétence qui dégrade son sabotage ou le rend visible dans le texte *(garantie et suppositions)* ; le programme **réussit si**, dans des duels préenregistrés (`[RAPPORTÉ]`) répliqués sur au moins deux familles de modèles ouverts (`illustratif : 8B et 32B–70B`) incluant un lot externe sans vérité plantée, il démontre soit la tenue conjointe de (i–iii) avec une réduction d'au moins $2\times$ (`illustratif`) du budget d'audit par rapport à l'audit uniforme, soit le seuil quantitatif exact auquel l'une de ces suppositions cède — et il **échoue si** son banc ne sépare pas sabotage diffus et fautes grossières triviales, si l'avantage des sondes disparaît face à des contrôles honnêtes ayant subi une consigne ou un réglage fin bénins sans livrer de borne transférable, ou si son oracle tombe au hasard ($\text{AUC} \le 0{,}55$, `illustratif`) hors vérité plantée *(mesure de succès ou d'échec)*.

**Ce que cette phrase exclut explicitement :**
1. **Les atténuations par entraînement** (alignement des poids par apprentissage par renforcement, choisies par `arXiv 2606.08892` p. 2, `[RAPPORTÉ]`).
2. **Le contrôle d'actions catastrophiques ponctuelles** (portes dérobées isolées où un seul audit tranche sans ambiguïté).
3. **Toute promesse de détecteur universel d'activations** sur tous modèles et tâches (réfutée par `arXiv 2504.08812` p. 1, `[RAPPORTÉ]`) : les sondes ne portent aucune garantie autonome, elles ne servent qu'à réduire la variance d'échantillonnage de l'audit.
4. **L'étude naturaliste de modèles de pointe véritablement comploteurs** (`arXiv 2504.05259` p. 24, `[RAPPORTÉ]`), inaccessible sans poids de pointe (`[RAPPORTÉ]`).
5. **Les tâches purement spéculatives dépourvues de tout critère de validité méthodologique même différé**, où aucun oracle — humain ou formel — ne peut définir un dommage.

---

### 7. Les questions brûlantes du domaine, expériences décisives `[Livrable (b)]`, ancrage matériel `[Livrable (d)]` et changement de cap

#### A. Classement des questions ouvertes

**Priorité 1 — Cœur de cible (à portée avec moyens modestes + bourse)**

1. **Peut-on incriminer ou borner par audit une menace diffuse sans connaître exactement la loi de suspicion d'un modèle bénin ?**
   - *Qui l'a posée* : Billet *« How Can We Solve Diffuse Threats Like Research Sabotage with AI Control? »* (30 avril 2025, auteurs non précisés dans FAITS : référence à vérifier ; identifiant arXiv : pas sûr / billet, `[RAPPORTÉ]`) et *« Diffuse AI Control on Fuzzy Tasks »* (`arXiv 2606.08892`, v3, p. 2 et 10, auteurs non précisés dans FAITS : référence à vérifier, `[RAPPORTÉ]`).
   - *Pourquoi elle reste ouverte* : En régime diffus, un biais de calibration $\epsilon$ sur le modèle bénin s'accumule en $O(T)$ comme le signal, noyant les tests séquentiels classiques, tandis que sur tâche floue l'audit ponctuel n'a pas de vérité terrain canonique (`[RAPPORTÉ]`).
   - *Pas décisif* : Établir théoriquement et empiriquement la frontière $(\epsilon_{\text{jumeau}}, \sigma_{\text{oracle}})$ sous laquelle l'évaluation *différentielle par tâche* (agent moins jumeau honnête) restaure la bornabilité par audit aléatoire (`[HYPOTHÈSE]`).
   - *Faisabilité (moyens modestes + bourse)* : **Oui**, immédiatement tentable (`[HYPOTHÈSE]`).

2. **L'instrument d'évaluation (moniteur texte ou oracle d'audit) est-il déplaçable par ce que l'agent écrit sur une tâche floue ?**
   - *Qui l'a posée* : Soulevée implicitement par l'indéfinition de la vérité terrain dans *« Diffuse AI Control on Fuzzy Tasks »* (`arXiv 2606.08892`, p. 10, `[RAPPORTÉ]`) et l'évasion de moniteurs inconnus (`arXiv 2512.11949`, p. 1, auteurs et titre exact non précisés dans FAITS : référence à vérifier, `[RAPPORTÉ]`) ; posée frontalement par le volet *« l'instrument »* du programme (`[RAPPORTÉ]`).
   - *Pourquoi elle reste ouverte* : Contrairement à un test unitaire logiciel, un juge évaluant une proposition d'expérience lit l'argumentation de l'agent lui-même ; personne n'a quantifié si une normalisation aveugle du protocole avant jugement suffit à bloquer ce déplacement (`[HYPOTHÈSE]`).
   - *Pas décisif* : Mesurer la perte de rappel à dommage scientifique constant sous cadrage contradictoire, avec et sans réécriture canonique par un modèle tiers honnête (`[HYPOTHÈSE]`).
   - *Faisabilité* : **Oui**, calcul modeste plus un petit budget de relecture humaine aveugle via la bourse (`[HYPOTHÈSE]`).

3. **Quelles sont les limites exactes (et la « taxe d'obscurcissement ») des sondes boîte blanche face au raisonnement latent bénin en surface ou obscurci ?**
   - *Qui l'a posée* : Appel public d'août 2025 (*« an increased understanding of the limits of white-box techniques for control »*, `[RAPPORTÉ]`) ; feuille de route de contrôle (`arXiv 2607.13087`, p. 25, auteurs et titre exact : référence à vérifier, `[RAPPORTÉ]`) ; `arXiv 2507.11473` p. 7 (CoT bénin avec raisonnement malin en activations, auteurs et titre : référence à vérifier, `[RAPPORTÉ]`) ; `arXiv 2412.09565` p. 1 (vulnérabilité à l'obscurcissement des activations réduisant toutefois la performance sur tâche complexe, auteurs et titre : référence à vérifier, `[RAPPORTÉ]`) ; `arXiv 2512.11949` p. 1 (`[RAPPORTÉ]`).
   - *Pourquoi elle reste ouverte* : On sait que l'obscurcissement casse les sondes sur tâches simples (`[RAPPORTÉ]`), mais on ignore si, sur une tâche complexe multi-pas, dissimuler simultanément la trace textuelle *et* la trace latente impose une perte de compétence qui neutralise le sabotage diffus (`[HYPOTHÈSE]`).
   - *Pas décisif* : Tracer le compromis à trois axes *(dommage diffus réel, évasion texte, évasion états internes)* après purge des confondants de construction, sur deux échelles de modèles ouverts (`[HYPOTHÈSE]`).
   - *Faisabilité* : **Oui avec la bourse** (pour le réglage fin adaptatif et le passage à $32\text{B}$–$70\text{B}$, `illustratif`).

4. **Dilution du sabotage diffus entre copies (« l'essaim »)**
   - *Qui l'a posée* : Volet *« l'essaim »* du programme (`[RAPPORTÉ]`) ; travaux sur la collusion multi-agents en contrôle (« référence à vérifier », identifiant arXiv : pas sûr).
   - *Pourquoi elle reste ouverte* : Diviser par $k$ (`illustratif`) la dérive par agent fait passer chaque trajectoire individuelle sous le bruit de calibration $\epsilon$, sauf agrégation au niveau du portefeuille global d'expériences (`[HYPOTHÈSE]`).
   - *Pas décisif / Faisabilité* : Caractériser la loi d'échelle du budget d'audit en fonction de $k$ ; faisable techniquement mais **scientifiquement subordonné** à la résolution du cas $k=1$ (questions 1 et 2) (`[HYPOTHÈSE]`).

**Priorité 2 — Hors de portée directe du programme (à exclure comme objectifs propres)**

5. **Signature interne de modèles *naturellement* comploteurs à l'échelle de pointe** (`arXiv 2504.05259`, p. 24, auteurs et titre : référence à vérifier, `[RAPPORTÉ]`) : hors de portée faute d'accès aux modèles de pointe (`[RAPPORTÉ]`) et de calcul d'entraînement à grande échelle.
6. **Garantie à $p>99\,\%$ quand les équipes rouges humaines ne dominent plus les attaques d'une IA surhumaine** (`arXiv 2512.22154`, p. 12 et 16, auteurs et titre : référence à vérifier, `[RAPPORTÉ]`) : hors de portée à l'échelle réelle ; le programme ne peut en étudier qu'un modèle réduit ouvert (ex. saboteur $70\text{B}$ supervisé par moniteur $8\text{B}$, `illustratif`, avec la bourse) (`[HYPOTHÈSE]`).
7. **Atténuations par entraînement sur tâches floues** (`arXiv 2606.08892`, p. 2, `[RAPPORTÉ]`) : hors de portée avec relecture humaine rare et calcul modeste (`[RAPPORTÉ]`).

---

#### B. Trois expériences décisives en inférence forte ($H_A$ contre $H_B$) `[Livrable (b)]`

Chaque duel est préenregistré (`[RAPPORTÉ]`), sans recette d'attaque opératoire :

1. **Duel E1 (Tranche la Question 1 : Garantie d'audit différentiel vs aveuglement par dérive bénigne)**
   - **$H_A$ (Bornabilité différentielle)** : À seuil nominal $\alpha = 1\,\%$ (`[RAPPORTÉ]`) calibré sur un domaine source et budget d'audit de $10\,\%$ (`illustratif`) des pas, l'audit différentiel (agent comparé au jumeau honnête sur la même tâche) maintient un taux effectif de fausses alertes hors-domaine $\le 2\,\%$ (`illustratif`) et plafonne le dommage cumulé moyen sous $25\,\%$ (`illustratif`) du dommage non contrôlé.
   - **$H_B$ (Non-identifiabilité sous décalage bénin)** : Dès changement de sous-domaine scientifique, l'écart $\epsilon$ entre jumeau et exécution bénigne légitime excède le signal diffus par pas : soit le taux de fausses alertes hors-domaine dépasse $5\,\%$ (`illustratif`), soit le dommage cumulé avant arrêt excède $50\,\%$ (`illustratif`) du dommage non contrôlé.
   - *Métrique et contrôle négatif* : Couple $(\text{FPR}_{\text{hors-domaine}}, \text{Dommage relatif})$ sur $200$ (`illustratif`) trajectoires de $30$ (`illustratif`) pas + validation sur $50$ (`illustratif`) propositions réelles hors vérité plantée ; contrôle négatif par second modèle ouvert honnête de style distinct et audit uniforme pur.
   - *Issues falsificatrices* : $(\le 2\,\%, \le 25\,\%)$ (`illustratif`) **falsifie $H_B$** ; $(> 5\,\% \text{ ou } > 50\,\%)$ (`illustratif`) **falsifie $H_A$** et réfute la garantie actuelle du programme.

2. **Duel E2 (Tranche la Question 2 : Invariance de l'instrument vs déplacement par cadrage)**
   - **$H_A$ (Restaurabilité par normalisation canonique)** : Après extraction aveugle d'un résumé méthodologique canonique par le jumeau honnête avant jugement, un saboteur sélectionnant ses formulations pour minimiser la suspicion à dommage scientifique fixé fait chuter le rappel à $1\,\%$ de fausses alertes (`[RAPPORTÉ]`) de moins de $10$ points de pourcentage (`illustratif`).
   - **$H_B$ (Vulnérabilité structurelle de l'instrument)** : Même après normalisation canonique, le rappel à $1\,\%$ de fausses alertes chute d'au moins $30$ points (`illustratif`) tandis qu'au moins $80\,\%$ (`illustratif`) de la dégradation méthodologique subsiste selon évaluation aval aveugle.
   - *Métrique et contrôle négatif* : Variation de $\text{TPR}@1\%\text{FPR}$ sur $100$ (`illustratif`) paires appariées (dont $50$, `illustratif`, relues à l'aveugle par humain) ; contrôle négatif vérifiant que la normalisation réduit de moins de $5\,\%$ (`illustratif`) le score des propositions purement honnêtes.
   - *Issues falsificatrices* : Chute $< 10$ points (`illustratif`) **falsifie $H_B$** ; chute $\ge 30$ points (`illustratif`) **falsifie $H_A$** et prouve que l'audit échoue au niveau de l'instrument avant toute accumulation temporelle.

3. **Duel E3 (Tranche la Question 3 : Gain d'audit boîte blanche vs artefact d'intervention et obscurcissement)**
   - **$H_A$ (Gain réel protégé par la taxe d'obscurcissement)** : Entraînées contre des contrôles honnêtes à consigne/réglage fin bénins, les sondes accumulées réduisent d'au moins $2\times$ (`illustratif`) le budget d'audit requis pour tenir $\Delta_{\max}$ à $\alpha = 1\,\%$ (`[RAPPORTÉ]`) par rapport au meilleur moniteur texte seul, tant sur le mode tenu à l'écart (`[RAPPORTÉ]`) que face à une famille de saboteurs pénalisée pour régulariser ses activations (cette pénalisation leur faisant perdre $\ge 50\,\%$, `illustratif`, de leur effet de sabotage ou les exposant au moniteur texte).
   - **$H_B$ (Artefact de construction ou évasion à faible coût)** : Une fois les contrôles bénins interventionnels inclus ou la régularisation latente activée, le ratio des budgets d'audit $B_{\text{texte}} / B_{\text{sonde+texte}}$ tombe sous $1{,}2\times$ (`illustratif`) à dommage égal.
   - *Métrique et contrôle négatif* : Ratio $B_{\text{texte}} / B_{\text{sonde+texte}}$ répliqué sur 8B (`[RAPPORTÉ]`) et un modèle $32\text{B}$–$70\text{B}$ (`illustratif`) ; contrôles négatifs obligatoires = modèle honnête avec consigne cachée bénigne et modèle honnête réglé finement sur corpus scientifique bénin.
   - *Issues falsificatrices* : Ratio $\ge 2\times$ (`illustratif`) sur les deux échelles **falsifie $H_B$** ; ratio $< 1{,}2\times$ (`illustratif`) **falsifie $H_A$** et établit une limite négative nette des sondes en régime diffus.

---

#### C. Ancrage matériel `[Livrable (d)]` et franchise sur le changement de cap

- **Ancrage matériel `[Livrable (d)]`** :
  - *Modèles ouverts* : socle actuel de $\sim 8\text{B}$ (`[RAPPORTÉ]`, ex. Llama-3.1-8B ou Qwen-2.5-7B, `illustratif`) ; avec bourse, ajout impératif d'une seconde famille à $32\text{B}$–$70\text{B}$ (`illustratif`, ex. Qwen-2.5-32B et Llama-3.3-70B) permettant à la fois le test de transfert inter-familles et un régime **asymétrique** (saboteur $70\text{B}$ contrôlé par jumeau/moniteur $8\text{B}$, `illustratif`).
  - *Calcul nécessaire* : socle 8B seul (E1, E2 et contrôles d'E3) $\approx 500$ à $900$ heures-GPU A100-80GB (`illustratif`) ; programme complet avec bourse (réplication $32\text{B}$–$70\text{B}$ et réglage fin adaptatif d'E3) $\approx 3\,000$ à $5\,000$ heures-GPU A100/H100-80GB (`illustratif`).
  - *Coût estimé* : $\sim 1\,000\text{ \$}$ à $2\,200\text{ \$}$ (`illustratif`) sans bourse ; avec bourse, $\sim 7\,500\text{ \$}$ à $14\,000\text{ \$}$ de calcul (`illustratif`) + $\sim 4\,000\text{ \$}$ à $6\,000\text{ \$}$ de relecture externe aveugle rémunérée sur les lots décisifs hors vérité plantée (`illustratif`), soit $\sim 11\,500\text{ \$}$ à $20\,000\text{ \$}$ au total (`illustratif`).

- **Faut-il changer de cap ? Oui, franchement (`[HYPOTHÈSE]` stratégique).**
  Le programme court aujourd'hui le risque de bâtir une usine interne sophistiquée (« organisme d'idéation », « mondes à vérité plantée », « arbitre formel », `[RAPPORTÉ]`) autour d'un unique modèle 8B, tout en traitant comme acquise sa supposition la plus fragile : que l'audit aléatoire par oracle borne un sabotage diffus sur tâche floue. Un « système performant » sur mondes plantés 8B sera écarté par le domaine comme un artefact d'échelle et de vérité synthétique (`[HYPOTHÈSE]`). **Le cap doit pivoter de l'ingénierie d'un système défensif complet vers la mise à l'épreuve impitoyable (théorèmes d'identifiabilité + réfutations adaptatives + test asymétrique $70\text{B}$ contre $8\text{B}$, `illustratif`) de la garantie d'audit sur tâches floues**, même si cela oblige à geler l'organisme d'idéation et expose le programme à invalider ses propres sondes ou son propre oracle : en science de la sécurité, une frontière d'impossibilité proprement établie pèse bien plus qu'une défense maison non transférable (`[HYPOTHÈSE]`).

---

### 8. Particulier ou universel : leçon des travaux marquants, recommandation et ordre des papiers

L'histoire des trois domaines voisins montre une régularité nette sur la *forme* des résultats qui durent :

1. **Cryptographie — Un cadre définitionnel + condition nécessaire universelle** : Goldwasser & Micali (1984, *Probabilistic Encryption*, `[VÉRIFIÉ]`) n'ont pas proposé un chiffrement empirique de plus ; ils ont défini la sécurité sémantique et montré pourquoi tout chiffrement déterministe échoue contre un adversaire passif. *Ce qui marque : une définition opposable et une borne.*
2. **Sécurité de l'apprentissage — Une réfutation structurelle d'une classe de défenses, ou une borne certifiée** : Carlini & Wagner (2017, *Towards Evaluating the Robustness of Neural Networks*, `[VÉRIFIÉ]`) et Athalye, Carlini & Wagner (2018, *Obfuscated Gradients Give a False Sense of Security: Circumventing Defenses to Adversarial Examples*, `[VÉRIFIÉ]`) ont marqué le domaine avec des moyens de calcul modestes en identifiant l'artefact méthodologique commun qui faussait des dizaines (`illustratif`) de défenses empiriques ; côté défense, Cohen, Rosenfeld & Kolter (2019, *Certified Adversarial Robustness via Randomized Smoothing*, `[VÉRIFIÉ]`) ont marqué parce que leur garantie reposait sur une réduction statistique explicite (comme un audit aléatoire calibré !) et non sur l'échec empirique d'un attaquant particulier.
3. **Contrôle de l'IA — Un protocole de garantie testé sur un point particulier limpide** : Greenblatt, Shlegeris, Sachan & Roger (2024, *AI Control: Improving Safety Despite Intentional Subversion*, `[VÉRIFIÉ]`) ont choisi une tâche **très particulière** (programmation avec portes dérobées) pour démontrer un **principe d'assurance universel** (borner le risque par audit rare et surveillance non fiable). C'est précisément ce principe qui bute aujourd'hui sur les menaces diffuses et floues (`arXiv 2606.08892`, `[RAPPORTÉ]`).

**Recommandation (`[HYPOTHÈSE]`)** : Ne viser **ni** une défense boîte blanche universelle (contredite par `arXiv 2504.08812`, `[RAPPORTÉ]`), **ni** un système particulier multi-briques optimisé pour battre un score interne. Viser **un banc particulier chirurgical au service d'une borne universelle (et de ses modes exacts de défaillance)**.

**Nouvel ordre recommandé des papiers (inversion de 1 et 2, conditionnement de 3) :**

1. **Papier 1 — *« L'Instrument et la Borne d'Audit »* (avant *« le temps »*)** : formaliser la borne d'audit aléatoire différentiel sur tâche floue et la tester contre la dérive de calibration du jumeau (E1) et le déplacement rhétorique de l'oracle/moniteur (E2), y compris hors vérité plantée. *Raison mathématique décisive* : tant que la stationnarité et le biais $\epsilon$ de l'instrument au pas unitaire ne sont pas bornés, accumuler des scores dans « le temps » accumule du biais non contrôlé et rend le Papier 1 initial fragile a posteriori (`[VÉRIFIÉ]` pour la propriété d'accumulation linéaire d'un biais systématique ; `[HYPOTHÈSE]` pour son ampleur empirique ici). De plus, ce papier intéresse immédiatement tous les acteurs, même sans accès boîte blanche.
2. **Papier 2 — *« Le Temps et la Taxe d'Obscurcissement »*** : l'instrument étant fixé et calibré, tester si l'accumulation séquentielle des états internes divise réellement le budget d'audit face aux contrôles bénins interventionnels et à l'obscurcissement adaptatif sur 8B et $32\text{B}$–$70\text{B}$ (`illustratif`, E3). Que l'issue valide la taxe d'obscurcissement ou établisse une limite négative des sondes en régime diffus, le résultat répond directement à l'appel d'août 2025 (`[RAPPORTÉ]`).
3. **Papier 3 — *« L'Asymétrie de Compétence ou l'Essaim »* (conditionnel)** : si la bourse est obtenue, tester prioritairement le contrôle d'un saboteur $70\text{B}$ par un jumeau/moniteur $8\text{B}$ (`illustratif`, vrai verrou d'échelle pointé par `arXiv 2512.22154`, `[RAPPORTÉ]`) ; ne traiter *« l'essaim »* ($k$ copies) que si la borne à $k=1$ a tenu au Papier 1. Parallèlement, **geler l'extension de l'organisme d'idéation** et restreindre l'arbitre formel à la vérification mécanique des bornes séquentielles du Papier 1.

---

### 9. Ce qui me ferait changer d'avis sur chacune de mes trois réponses principales

1. **Sur le pivot d'un « système performant battant l'état de l'art » vers « bornes d'identifiabilité et falsifications de la garantie d'audit »** : je changerais d'avis si un banc public tiers largement adopté sur tâches floues voyait le jour avec une métrique aval objective sans vérité plantée maison, **et** qu'un pilote montrait que le modèle 8B y produit déjà un sabotage diffus réduisant l'utilité réelle de $> 30\,\%$ (`illustratif`) tout en restant sous $5\,\%$ (`illustratif`) de détection par moniteurs simples à $1\,\%$ de fausses alertes (`[RAPPORTÉ]`).
2. **Sur l'inversion de l'ordre des papiers (*« l'instrument + borne d'audit »* avant *« le temps »*)** : je reviendrais à l'ordre initial si un pré-test rapide ($50$ paires, `illustratif`) montrait à la fois que l'oracle et le moniteur texte varient de moins de $5$ points de rappel (`illustratif`) sous reformulation contradictoire, que le jumeau honnête garde un taux de fausses alertes hors-domaine dans $[0{,}8\,\%, 1{,}2\,\%]$ (`illustratif`), et que l'avantage temporel des sondes survit déjà intact face à un modèle honnête muni d'une consigne cachée et d'un réglage fin bénins.
3. **Sur le cantonnement des sondes à un rôle d'accélérateur d'audit aux limites étroites (et l'exclusion des « vrais comploteurs »)** : je changerais d'avis si la bourse ouvrait un accès expérimental à des organismes modèles de grande taille ayant développé un comportement trompeur par apprentissage par renforcement sans consigne explicite de sabotage, **ou** si une sonde de dynamique interne non supervisée transférait sans réentraînement de 8B à $70\text{B}$ (`illustratif`) et résistait à l'obscurcissement (`arXiv 2412.09565`, `[RAPPORTÉ]`) parce que toute dissimulation latente ferait s'effondrer la cohérence méthodologique de surface du modèle.

FIN-DE-CELLULE