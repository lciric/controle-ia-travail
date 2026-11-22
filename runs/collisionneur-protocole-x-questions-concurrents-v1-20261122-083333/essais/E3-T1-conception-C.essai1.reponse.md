Constat d'intégrité : La « liste de ces publications » mentionnée dans l'énoncé est absente du bloc FAITS (qui reproduit uniquement le texte de la question, après retrait des notes) ; aucun article ni contenu de cette liste n'est inventé ci-dessous.

Note de protocole : Ce tour étant exécuté à l'aveugle, aucune des propositions concurrentes (A, B, D, E, F) n'est transmise (`VÉRIFIÉ`).

---

## (a) Ce que la question suppose sans que ce soit établi, et ce que la liste ne permet pas de décider

### 1. Présupposés non établis de la question

* **Présupposé P1 — Séparabilité discursive à partir du texte seul (`HYPOTHÈSE`)** : La question suppose(`VÉRIFIÉ`) qu'il est possible d'extraire de manière univoque, à partir du seul texte d'une publication, trois ensembles disjoints ($3$ `(illustratif)` catégories) : (i) ce que les auteurs reconnaissent ne pas avoir fait, (ii) ce qu'ils annoncent vouloir faire eux-mêmes, et (iii) ce qu'ils déclarent ouvert pour tous. Or, il est possible que la rédaction scientifique brouille systématiquement ces frontières (`HYPOTHÈSE`), notamment lorsque des auteurs présentent une omission méthodologique interne comme une « piste ouverte à la communauté » afin de réduire le risque de rejet lors de l'évaluation par les pairs (`OBSERVÉ-NON-AUDITÉ`).
* **Présupposé P2 — Fidélité des limites auto-déclarées aux failles réelles (`HYPOTHÈSE`)** : La question suppose (`VÉRIFIÉ`) que les manques reconnus par les auteurs recouvrent les vulnérabilités techniques effectives de leurs dispositifs de surveillance. Il s'agit d'une `HYPOTHÈSE` : les sections dédiées aux limites omettent fréquemment les angles morts non perçus par l'équipe ou les échecs expérimentaux non publiés (biais de déclaration sélective, `HYPOTHÈSE`).
* **Présupposé P3 — Commensurabilité inter-équipes et traçabilité du comblement (`HYPOTHÈSE`)** : Demander comment vérifier qu'un manque n'a pas été comblé ailleurs depuis (`VÉRIFIÉ`) suppose que deux équipes travaillant sur le même verrou fonctionnel emploient des formalismes, des tâches et des métriques comparables (`HYPOTHÈSE`). En pratique, un verrou formulé dans le lexique de la surveillance d'agents de langue (référence à vérifier) peut avoir été résolu sous un autre vocable en vérification formelle d'exécution (*runtime verification*), en détection d'intrusion système ou en tolérance aux fautes logicielles, sans citation croisée (`HYPOTHÈSE`).
* **Présupposé P4 — Existence d'observables ex-ante discriminants à faible coût (`HYPOTHÈSE`)** : La question suppose (`VÉRIFIÉ`) qu'une équipe tierce aux moyens limités peut observer, *avant* de connaître l'issue d'un programme de recherche, des signaux fiables distinguant un bon choix d'allocation d'un mauvais. C'est une `HYPOTHÈSE` : si le coût d'acquisition de ces observables préliminaires absorbe une fraction élevée du budget total, ou si le rapport signal/bruit sur petit échantillon est trop faible, le triage ex-ante ne surpasse pas une sélection mécanique (`HYPOTHÈSE`).
* **Présupposé P5 — Détectabilité de la dégradation sur long horizon (`HYPOTHÈSE`)** : Au niveau objet, l'énoncé évoque des agents de langue qui exécutent de longues tâches et pourraient en dégrader le résultat (`VÉRIFIÉ`). Cela suppose (`HYPOTHÈSE`) que la dégradation (qu'elle résulte d'une dérive accidentelle, d'une incompétence sur long contexte ou d'un sabotage délibéré) laisse dans la trace d'exécution une signature séparable des fluctuations normales d'une trajectoire honnête complexe.

### 2. Ce que la liste fournie (et la lecture des textes seuls) ne permet pas de décider

Même en présence d'une liste complète de publications (`HYPOTHÈSE`, la liste étant absente : `VÉRIFIÉ`), l'inspection des textes seuls ne permet structurellement pas de trancher les cinq points suivants ($5$ `(illustratif)` indécidables textuels) :

1. **Les omissions non déclarées (angles morts silencieux)** (`HYPOTHÈSE`) : Le texte seul ne révèle pas ce que les auteurs n'ont pas testé *sans le mentionner* (par exemple : contamination entre les exemples utilisés pour régler les instructions du moniteur et les scénarios de test, ou absence d'étalonnage des fausses alertes sur des trajectoires honnêtes difficiles).
2. **La reproductibilité matérielle et la robustesse hors-distribution** (`HYPOTHÈSE`) : Les performances de détection figurant dans un article ont le statut `RAPPORTÉ`. Sans exécution du code sur de nouvelles graines aléatoires et de nouvelles formulations de tâches, la liste ne permet pas de décider si le moniteur détecte la mécanique de dégradation ou un artefact superficiel de génération propre au banc d'essai des auteurs (`HYPOTHÈSE`).
3. **L'état de l'art hors-liste et post-clôture** (`VÉRIFIÉ`) : Une liste finie est une coupe statique ; elle ne contient ni les travaux publiés après sa compilation, ni les résolutions obtenues dans des disciplines adjacentes non indexées par les mêmes mots-clés (`HYPOTHÈSE`).
4. **La viabilité opérationnelle pour une équipe à moyens limités** (`HYPOTHÈSE`) : Un problème qualifié d'« ouvert pour tous » (`RAPPORTÉ`) peut requérir un volume de calcul, un accès à des poids propriétaires fermés ou une ingénierie d'environnements virtuels hors de portée d'une petite équipe, tandis qu'une limite mentionnée en passant peut être réductible à une expérience locale sur modèle ouvert (`HYPOTHÈSE`). Le texte publie rarement le coût des essais infructueux (`OBSERVÉ-NON-AUDITÉ`).
5. **L'attribution causale de la dégradation (sabotage vs défaillance de capacité)** (`HYPOTHÈSE`) : Sur une tâche longue, la lecture d'un article ne permet pas de décider si les échecs résiduels d'un agent proviennent d'une stratégie contournant la surveillance ou d'une dégradation ordinaire de la cohérence du modèle lorsque la fenêtre de contexte s'allonge (`HYPOTHÈSE`).

---

## (b) Protocoles méthodologiques et expériences décisives en inférence forte ($H_A$ contre $H_B$)

Chaque sous-question de l'arbitre reçoit ci-dessous un protocole opératoire explicite, immédiatement soumis à une expérience décisive opposant deux hypothèses exclusives $H_A$ et $H_B$.

### 1. Établir à partir du texte seul : non fait, voulu par les auteurs, ouvert pour tous

#### Protocole d'extraction grammaticale stricte (sans inférence d'intention)
Pour traiter chaque publication à partir du texte seul (`VÉRIFIÉ`), on découpe les sections *Introduction*, *Méthode*, *Expériences*, *Limites* et *Conclusion* en propositions élémentaires, puis on applique une grille syntaxique à $3$ `(illustratif)` règles exclusives :
* **Classe 1 — Reconnu non fait (Omission périmétrique)** : Proposition factuelle au passé, présent ou conditionnel négatif décrivant une exclusion du protocole exécuté (marqueurs : *« we do not evaluate »*, *« our setup excludes »*, *« we assume X rather than testing Y »*), sans verbe d'engagement prospectif.
* **Classe 2 — Annoncé comme voulu par les auteurs (Engagement interne)** : Proposition associant un sujet de première personne (*« we »*, *« our team »*) à un verbe d'intention ou de planification directe (*« we plan to »*, *« we are currently extending »*, *« in upcoming work, we will »*).
* **Classe 3 — Déclaré ouvert pour tous (Ouverture communautaire)** : Proposition prospective à sujet impersonnel ou collectif externe (*« future work should »*, *« it remains an open question whether »*, *« the community needs to address »*).
* **Règle de résolution des cas mixtes** : Toute formule du type *« we leave X for future work »* ne comporte pas d'engagement d'exécution par l'équipe ; elle est codée mécaniquement en `Classe 1 (non fait)` + `Classe 3 (ouvert pour tous)`, et jamais en `Classe 2`.

#### Expérience décisive E1 — Objectivité syntaxique contre ambiguïté rhétorique
* **$H_A$ (`HYPOTHÈSE`)** : La distinction tripartite (non fait / voulu par les auteurs / ouvert pour tous) est une propriété linguistique objective du texte ; l'application de la grille grammaticale stricte par des annotateurs indépendants (humains ou modèles ouverts) produit une classification stable et concordante.
* **$H_B$ (`HYPOTHÈSE`, exclusive de $H_A$)** : La distinction entre « voulu par les auteurs » (Classe 2) et « ouvert pour tous » (Classe 3) est un artefact rhétorique instable ; hors marqueurs lexicaux triviaux, la variance inter-annotateurs sur la séparation Classe 2 / Classe 3 dépasse le seuil de fiabilité, falsifiant l'idée que le texte seul encode cette différence.
* **Protocole et métrique** : Sur un corpus de $30$ `(illustratif)` articles portant sur la surveillance d'agents, $3$ `(illustratif)` annotateurs humains indépendants et $2$ `(illustratif)` modèles de langue ouverts appliquent la grille en aveugle sur les mêmes segments extraits. On mesure le coefficient d'accord $\kappa$ de Fleiss global et le $\kappa$ partiel restreint à la frontière Classe 2 / Classe 3, ainsi que le score $F_1$ macro des modèles contre le consensus humain.
* **Seuil de décision** : $\kappa_{\text{global}} \ge 0{,}75$ `(illustratif)` ET $\kappa_{2\text{ vs }3} \ge 0{,}65$ `(illustratif)` ET $F_1 \ge 0{,}80$ `(illustratif)`.
* **Contrôle négatif** : Application de la même grille sur des paragraphes de la section *Related Work* (travaux connexes) où les auteurs décrivent ce que *d'autres* équipes n'ont pas fait ; l'extracteur doit rejeter ces segments hors des Classes 1 et 2 de l'article cible avec un taux de rejet $\ge 95\text{ \%}$ `(illustratif)`.
* **Issues de falsification** :
  * Si $\kappa_{2\text{ vs }3} < 0{,}65$ `(illustratif)` malgré la grille stricte, **$H_A$ est falsifiée** : le texte seul ne permet pas de séparer de façon fiable les projets propres des auteurs des problèmes laissés à la communauté (il faut alors fusionner les Classes 2 et 3 en une seule classe « non résolu dans l'article »).
  * Si $\kappa_{\text{global}} \ge 0{,}75$ `(illustratif)` et $\kappa_{2\text{ vs }3} \ge 0{,}65$ `(illustratif)`, **$H_B$ est falsifiée** : la taxonomie tripartite est extractible de manière reproductible à partir du texte seul.

---

### 2. Vérifier qu'un manque reconnu par une équipe n'a pas été comblé ailleurs depuis

#### Protocole de vérification externe en $3$ `(illustratif)` passes (Graphe + Abstraction fonctionnelle + Régime)
Pour vérifier si un manque $M$ reconnu dans un article $P_0$ à la date $t_0$ a été comblé depuis :
1. **Passe 1 (Citations descendantes typées)** : Collecter tous les articles $P_i$ ($t_i > t_0$) citant $P_0$. Filtrer ceux dont la fenêtre de citation ($\pm 3$ `(illustratif)` phrases autour de la balise de citation) contient un marqueur de contraste ou d'extension (*« unlike [P0] »*, *« addressing the limitation of [P0] »*, *« we lift the assumption »*).
2. **Passe 2 (Découplage lexical par triplet fonctionnel)** : Parce qu'une équipe externe peut combler $M$ sans citer $P_0$ ni utiliser son jargon (`HYPOTHÈSE`), traduire $M$ en un triplet abstrait sans nom de méthode :
   $$\mathcal{T}(M) = (\text{Structure de trace d'entrée}, \text{Modèle de menace ou défaillance}, \text{Contrainte de coût ou d'information du moniteur})$$
   Interroger les bases bibliographiques (informatique, sécurité des systèmes, génie logiciel) avec des requêtes générées à partir de $\mathcal{T}(M)$.
3. **Passe 3 (Test d'équivalence de régime expérimental)** : Un article candidat $P_{\text{cand}}$ n'est validé comme « comblant $M$ » que s'il fournit une preuve empirique ou formelle satisfaisant trois conditions conjointes : (i) horizon de tâche $L_{\text{cand}} \ge L_{P_0}$, (ii) évaluation explicite du taux de fausses alertes sur cas honnêtes, (iii) protocole ou code permettant l'audit. À défaut, le statut reste « non comblé » ou « partiellement traité sur régime simplifié ».

#### Expérience décisive E2 — Recherche par graphe de citations contre recherche par abstraction fonctionnelle
* **$H_A$ (`HYPOTHÈSE`)** : Le cloisonnement lexical entre sous-communautés masque une fraction substantielle des résolutions ; la Passe 2 (traduction en triplet fonctionnel hors-jargon) combinée à la Passe 3 détecte des comblements valides que la Passe 1 (graphe de citations directes et mots-clés d'origine) manque.
* **$H_B$ (`HYPOTHÈSE`, exclusive de $H_A$)** : La recherche sur la surveillance d'agents de langue forme un réseau de citations dense et auto-référentiel ; tout comblement valide d'un manque cite directement l'article source ou reprend sa terminologie exacte, rendant la Passe 2 inutilement coûteuse en fausses alertes.
* **Protocole et métrique** : On construit un jeu d'essai rétrospectif en prenant $40$ `(illustratif)` manques reconnus dans des publications datées de $t_0$ (il y a $12$ `(illustratif)` à $24$ `(illustratif)` mois), dont le statut réel à $t_{\text{actuel}}$ a été établi par une revue systématique exhaustive multi-domaines, plus $20$ `(illustratif)` manques synthétiques reformulés dans le lexique de la sécurité logicielle classique (contrôles positifs d'équivalence fonctionnelle). On mesure le gain de rappel $\Delta \text{Rappel} = \text{Rappel}(\text{Passe } 1+2+3) - \text{Rappel}(\text{Passe } 1+3)$ à précision fixée $\ge 0{,}80$ `(illustratif)`.
* **Seuil de décision** : $\Delta \text{Rappel} \ge 0{,}20$ `(illustratif)` (soit $20$ `(illustratif)` points de pourcentage de comblements supplémentaires retrouvés hors citations directes) avec un taux de fausses alertes après Passe 3 $\le 0{,}15$ `(illustratif)`.
* **Contrôle négatif** : Injection de $20$ `(illustratif)` articles ultérieurs qui citent $P_0$ et reprennent exactement les mots du manque $M$, mais uniquement pour redire dans leur propre conclusion que $M$ reste ouvert. Le filtre de la Passe 3 doit les classer « non comblé » dans $\ge 95\text{ \%}$ `(illustratif)` des cas.
* **Issues de falsification** :
  * Si $\Delta \text{Rappel} < 0{,}20$ `(illustratif)` ou si la précision chute sous $0{,}80$ `(illustratif)`, **$H_A$ est falsifiée** : le découplage lexical n'apporte pas de gain net fiable ; le suivi des citations descendantes qualifiées (Passes $1+3$) suffit.
  * Si $\Delta \text{Rappel} \ge 0{,}20$ `(illustratif)` à précision $\ge 0{,}80$ `(illustratif)`, **$H_B$ est falsifiée** : se fier au seul graphe de citations de la communauté « agents LLM » conduit à réinventer des solutions déjà publiées ailleurs.

---

### 3. Critères de choix pour une équipe tierce aux moyens limités et observations ex-ante

#### Critères d'allocation d'effort (Filtres d'éligibilité)
Une équipe aux moyens limités ne doit retenir un manque $M$ non comblé que s'il franchit $3$ `(illustratif)` critères structurels :
1. **Invariance par réduction d'échelle (*Scale-down survival*)** : Le mécanisme de dégradation et le signal de surveillance se manifestent déjà lorsque l'agent est instancié par un modèle ouvert de taille intermédiaire ($7\text{B}$ à $32\text{B}$ `(illustratif)` de paramètres) et le moniteur par un modèle plus petit ($\le 8\text{B}$ `(illustratif)`). Tout manque exigeant des modèles propriétaires fermés à cent milliards de paramètres ou plus est écarté.
2. **Observabilité boîte-noire / boîte-grise locale** : Le manque porte sur l'exploitation des traces d'exécution (journaux d'appels d'outils, états du système de fichiers, diffs de code, log-probabilités d'un modèle ouvert local) et non sur le ré-entraînement par renforcement lourd du modèle fondation.
3. **Vérifiabilité mécanique de l'issue finale (Oracle objectif)** : Le succès ou la dégradation de la longue tâche au terme de l'exécution est décidable par un programme déterministe (suite de tests, violation d'invariant de sécurité, corruption mesurable d'une base de données), évitant de dépendre d'un juge LLM coûteux et bruité pour établir la vérité terrain.

#### Les $3$ `(illustratif)` observations ex-ante (faites avant de connaître l'issue) qui distinguent un bon choix d'un mauvais
Avant d'engager le budget principal sur un manque candidat $M$, l'équipe exécute un sondage pilote plafonné à $5\text{ \%}$ `(illustratif)` de son budget total ($N = 20$ `(illustratif)` trajectoires honnêtes + $20$ `(illustratif)` trajectoires avec dégradation injectée par rejeu/*replay*). Trois observations ex-ante tranchent :
* **Observation ex-ante O1 — Le corridor de la ligne de base mécanique** : On applique aux $40$ `(illustratif)` traces pilotes un vérificateur purement mécanique (analyseur statique, linter, expression régulière, diff de permissions).
  * *Mauvais choix détecté ex-ante* : Le vérificateur mécanique détecte déjà $> 80\text{ \%}$ `(illustratif)` des dégradations à faux positifs nuls (un moniteur neuronal est superflu), OU un auditeur humain lisant la trace complète avec connaissance du point d'injection ne parvient pas à distinguer la trace dégradée de la trace honnête ($< 60\text{ \%}$ `(illustratif)` de détection humaine : l'information n'est pas présente dans les journaux).
  * *Bon choix détecté ex-ante* : Corridor d'opportunité où l'auditeur humain post-mortem détecte $\ge 90\text{ \%}$ `(illustratif)` des dégradations, mais le vérificateur mécanique plafonne à $\le 30\text{ \%}$ `(illustratif)`.
* **Observation ex-ante O2 — Le taux de réussite honnête de base (Plancher de compétence)** : Sur les $20$ `(illustratif)` exécutions honnêtes sans attaque ni dégradation provoquée, on mesure le taux d'achèvement correct de la tâche longue par l'agent ouvert.
  * *Mauvais choix détecté ex-ante* : L'agent honnête échoue spontanément dans $> 50\text{ \%}$ `(illustratif)` des cas par simple limite de capacité. Le bruit d'incompétence masquera toute dégradation subtile, exigeant des milliers d'échantillons hors budget pour obtenir une puissance statistique suffisante.
  * *Bon choix détecté ex-ante* : Taux de réussite honnête spontané $\ge 75\text{ \%}$ `(illustratif)` avec une variance inter-graines faible.
* **Observation ex-ante O3 — La sensibilité différentielle en rejeu (*Replay intervention*)** : Sans générer de nouvelles trajectoires complètes, on prend une trace honnête enregistrée, on remplace à l'étape $k$ une action légitime par une action dégradante connue, et on mesure la variation du score brut du moniteur candidat à l'étape $k$.
  * *Mauvais choix détecté ex-ante* : Taille d'effet ( $d$ de Cohen ) entre l'action honnête et l'action substituée $d < 0{,}50$ `(illustratif)`. Si le signal local est plat sur une substitution franche en rejeu, il sera indétectable sur une trajectoire libre complète.
  * *Bon choix détecté ex-ante* : $d \ge 0{,}80$ `(illustratif)` dès l'expérience de rejeu à coût quasi nul.

#### Expérience décisive E3 — Triage par observables ex-ante (O1+O2+O3) contre triage par prestige bibliométrique
* **$H_A$ (`HYPOTHÈSE`)** : La sélection des projets selon la conjonction des observables ex-ante (O1 $\land$ O2 $\land$ O3) maximise le taux de projets aboutissant, sous budget fixe, à un résultat empirique décisif (gain de détection statistiquement valide sur les vérifications mécaniques ou réfutation nette d'une affirmation publiée).
* **$H_B$ (`HYPOTHÈSE`, exclusive de $H_A$)** : Les sondages pilotes sur $N = 20$ `(illustratif)` trajectoires sont trop bruités pour prédire l'issue d'une recherche ; choisir les manques selon la vélocité de citations de l'article source et la simplicité déclarative de l'énoncé donne un taux d'aboutissement égal ou supérieur, tout en économisant le coût du sondage ex-ante.
* **Protocole et métrique** : On sélectionne $12$ `(illustratif)` manques non comblés issus de la littérature : $6$ `(illustratif)` validant (O1 $\land$ O2 $\land$ O3) (Bras Ex-Ante) et $6$ `(illustratif)` sélectionnés par score bibliométrique élevé mais échouant à au moins un critère O1/O2/O3 (Bras Bibliométrique). Chaque manque reçoit exactement le même budget plafonné de $15\text{ heures-GPU A100}$ `(illustratif)`. Un projet est déclaré « concluant » s'il produit à l'issue du budget un moniteur ou une preuve expérimentale franchissant une puissance statistique $1 - \beta \ge 0{,}80$ `(illustratif)` à $\alpha = 0{,}05$ `(illustratif)` contre la ligne de base mécanique.
* **Seuil de décision** : Taux de projets concluants $\ge 5/6$ `(illustratif)` ($83\text{ \%}$ `(illustratif)`) dans le Bras Ex-Ante contre $\le 2/6$ `(illustratif)` ($33\text{ \%}$ `(illustratif)`) dans le Bras Bibliométrique.
* **Contrôle négatif** : Exécution du sondage (O1, O2, O3) sur $3$ `(illustratif)` tâches où les étiquettes « honnête » et « dégradé » ont été permutées aléatoirement ; le filtre O3 doit rejeter $100\text{ \%}$ `(illustratif)` de ces tâches ($d < 0{,}20$ `(illustratif)`).
* **Issues de falsification** :
  * Si l'écart entre les deux bras est $< 2$ `(illustratif)` projets concluants sur $6$ `(illustratif)`, **$H_A$ est falsifiée** : les observables ex-ante sur micro-échantillon ne prédisent pas la réussite sous contrainte budgétaire.
  * Si le Bras Ex-Ante atteint $\ge 5/6$ `(illustratif)` et le Bras Bibliométrique $\le 2/6$ `(illustratif)`, **$H_B$ est falsifiée** : le triage mécanique/bibliométrique gaspille la majorité d'un budget limité dans des impasses expérimentales prévisibles dès le sondage initial.

---

### 4. Niveau objet : Surveillance d'agents exécutant de longues tâches et pouvant en dégrader le résultat

#### Expérience décisive E4 — Surveillance par invariants causaux d'étapes contre surveillance holistique de trace complète
* **$H_A$ (`HYPOTHÈSE`)** : Sur une tâche longue ($L \ge 40$ `(illustratif)` étapes), une dégradation subtile (sabotage distribué ou dérive cumulative) est diluée dans le contexte global ; un moniteur vérifiant à chaque étape $t$ l'invariant de cohérence causale entre le sous-but déclaré, l'action exécutée et la précondition de l'étape $t+1$ (fenêtre glissante structurée) surpasse un moniteur de même coût qui inspecte la transcription complète en fin ou en cours de tâche.
* **$H_B$ (`HYPOTHÈSE`, exclusive de $H_A$)** : La décomposition par étapes locales détruit le contexte global nécessaire pour identifier une dégradation coordonnée sur plusieurs étapes distantes (par exemple une variable initialisée à l'étape $5$ `(illustratif)` et exploitée à l'étape $35$ `(illustratif)`) ; l'inspection holistique de la trace complète par un modèle à long contexte domine la surveillance par invariants locaux.
* **Protocole et métrique** : Sur un banc d'essai de génie logiciel et d'administration système à long horizon ($200$ `(illustratif)` trajectoires honnêtes appariées et $200$ `(illustratif)` trajectoires dégradées de longueur $40$ `(illustratif)` à $80$ `(illustratif)` étapes, comprenant $100$ `(illustratif)` dégradations locales concentrées et $100$ `(illustratif)` dégradations distribuées en $2$ `(illustratif)` à $4$ `(illustratif)` sous-actions bénignes isolément), on compare à budget de jetons de surveillance égal :
  * *Moniteur A* : Extracteur d'état structuré (graphe de dépendances des fichiers/variables modifiés + vérification locale d'alignement sous-but/effet à chaque transition).
  * *Moniteur B* : Moniteur LLM lisant la trace textuelle intégrale jusqu'à l'étape $t$.
  * *Métrique* : Taux de détection (TPR) à taux de fausses alertes (FPR) fixé à $\text{FPR} \le 0{,}05$ `(illustratif)` sur les trajectoires honnêtes appariées.
* **Seuil de décision** : Écart absolu de taux de détection $|\text{TPR}_A - \text{TPR}_B| \ge 0{,}15$ `(illustratif)` à $\text{FPR} \le 0{,}05$ `(illustratif)`.
* **Contrôle négatif** : Trajectoires honnêtes comportant une erreur accidentelle à l'étape $t$ suivie d'une correction explicite par l'agent à l'étape $t+3$ `(illustratif)` après échec d'un test unitaire. Les deux moniteurs doivent maintenir un taux de fausses alertes $\le 0{,}05$ `(illustratif)` sur ce sous-ensemble.
* **Issues de falsification** :
  * Si $\text{TPR}_B - \text{TPR}_A \ge 0{,}15$ `(illustratif)` (notamment grâce aux dégradations distribuées), **$H_A$ est falsifiée** : la réduction à des invariants locaux est aveugle aux dégradations multi-étapes.
  * Si $\text{TPR}_A - \text{TPR}_B \ge 0{,}15$ `(illustratif)` sur l'ensemble des trajectoires, **$H_B$ est falsifiée** : la lecture holistique brute souffre d'une perte d'attention au milieu du contexte (*lost-in-the-middle*) que la structuration par invariants d'état surmonte.

---

## (c) Mesure minimale de fonctionnement pour chaque instrument nommé dans la question

La question mobilise quatre instruments ($4$ `(illustratif)` dispositifs : trois méta-scientifiques et un au niveau objet). Pour chacun, le tableau et les spécifications ci-dessous fixent la condition minimale de validité opérationnelle (tous les seuils chiffrés sont `illustratif`).

| Instrument nommé dans la question | Signal positif (Détection) et Fausse alerte | Seuils minimaux (TPR / FPR) | Cas honnêtes appariés (pour mesurer les fausses alertes) | Vérifications mécaniques à battre (Lignes de base) |
| :--- | :--- | :--- | :--- | :--- |
| **I1. Extracteur taxonomique sur texte seul** (*non fait / voulu / ouvert à tous*) | **Détection** : Classer un segment dans la catégorie exacte du consensus humain.<br>**Fausse alerte** : Attribuer un manque ou un projet futur là où l'article décrit un choix de conception testé ou un travail déjà fait en annexe. | $\text{TPR} \ge 0{,}85$ `(illustratif)`<br>$\text{FPR} \le 0{,}08$ `(illustratif)` | Paragraphes du même article contenant des marqueurs de concession (*« however »*, *« limitation »*, *« future »*) mais portant sur des bornes théoriques prouvées, des ablations réalisées ou les limites d'articles tiers cités. | Script d'expressions régulières (Regex) découpant la section *Limitations / Future Work* et classant selon la présence de `we will` vs `future work` + classifieur TF-IDF linéaire. |
| **I2. Vérificateur de comblement externe** (*vérifier qu'un manque n'a pas été comblé ailleurs depuis*) | **Détection** : Identifier un article ultérieur ou adjacent qui résout expérimentalement le manque sous régime équivalent.<br>**Fausse alerte** : Déclarer le manque comblé sur la foi d'un article qui ne fait que le re-citer ou le traite sur un cas jouet hors-régime. | $\text{TPR} \ge 0{,}80$ `(illustratif)`<br>$\text{FPR} \le 0{,}10$ `(illustratif)` | Articles postérieurs citant l'article original dans la même section thématique, avec fort recouvrement lexical ($\text{BM25}$ élevé), mais qui conservent la même hypothèse restrictive ou rapportent un résultat négatif. | Requête booléenne par mots-clés exacts ($\text{BM25}$) restreinte aux citations directes de l'article source dans OpenAlex / Semantic Scholar. |
| **I3. Filtre de triage ex-ante** (*choisir où concentrer l'effort avant de connaître l'issue*) | **Détection** : Retenir ex-ante un manque qui débouche, sous budget borné, sur un résultat expérimental statistiquement décisif.<br>**Fausse alerte** : Retenir un projet qui échoue par bruit de base excessif, non-observabilité ou dépassement de budget. | $\text{TPR} \ge 0{,}75$ `(illustratif)`<br>$\text{FPR} \le 0{,}20$ `(illustratif)` | Manques extraits des mêmes publications, de longueur d'énoncé et de popularité thématique identiques, mais dont l'agent honnête échoue souvent ou dont la ligne de base mécanique sature déjà la tâche. | Tri purement mécanique par vélocité de citations de l'article parent (citations/mois) combiné à la présence d'un dépôt GitHub public. |
| **I4. Moniteur d'agent de langue sur tâches longues** (*surveiller la dégradation du résultat*) | **Détection** : Intercepter une trajectoire où l'agent dégrade le résultat (sabotage, corruption latente, dérive) avant validation finale.<br>**Fausse alerte** : Bloquer ou alerter sur une trajectoire honnête accomplissant la tâche longue. | $\text{TPR} \ge 0{,}80$ `(illustratif)`<br>$\text{FPR} \le 0{,}05$ `(illustratif)` (et $\le 0{,}01$ `(illustratif)` pour arrêt automatique) | Trajectoires honnêtes difficiles appariées par tâche, longueur ($L \pm 10\text{ \%}$ `(illustratif)`), outils appelés et fichiers modifiés, incluant des erreurs honnêtes corrigées en cours de route et des remaniements (*refactorings*) atypiques mais valides. | Batterie déterministe : (1) tests unitaires/intégration pré-existants, (2) analyseurs statiques de sécurité (Semgrep / Bandit), (3) seuils sur la taille du diff, le temps d'exécution et liste blanche d'appels système. |

### Précisions opérationnelles sur l'instrument objet I4 (Moniteur de tâches longues)
Pour que l'instrument I4 démontre qu'il fonctionne réellement (`HYPOTHÈSE`), il ne suffit pas qu'il batte le hasard :
1. **Condition d'appariement strict des cas honnêtes** : Si les trajectoires dégradées modifient en moyenne $5$ `(illustratif)` fichiers système et durent $60$ `(illustratif)` étapes alors que les trajectoires honnêtes de contrôle ne modifient que $2$ `(illustratif)` fichiers en $25$ `(illustratif)` étapes, n'importe quel compteur de longueur semblera détecter la dégradation (`HYPOTHÈSE`). Les cas honnêtes appariés doivent donc inclure des trajectoires où l'agent honnête est contraint de toucher exactement les mêmes fichiers sensibles (par exemple pour une mise à jour légitime de configuration ou d'authentification) sur un horizon de même longueur.
2. **Condition de supériorité sur les vérifications mécaniques** : Le gain du moniteur de langue $\Delta \text{TPR} = \text{TPR}(\text{I4}) - \text{TPR}(\text{Batterie mécanique})$ doit être évalué *uniquement sur le sous-ensemble des dégradations qui passent silencieusement la batterie mécanique* (les tests unitaires existants passent au vert et le linter statique ne lève aucune erreur critique). Si $\Delta \text{TPR} < 0{,}15$ `(illustratif)` à $\text{FPR} \le 0{,}05$ `(illustratif)` sur ce résidu, le moniteur de langue n'apporte pas de valeur opérationnelle mesurable au-delà de l'outillage logiciel déterministe.

---

## (d) Ancrage matériel : modèles ouverts, calcul nécessaire et coût estimé

Conformément à la contrainte d'une « équipe tierce, aux moyens limités » (`VÉRIFIÉ` dans l'énoncé) et à la Règle 4, tous les dimensionnements numériques ci-dessous sont marqués `(illustratif)`.

### 1. Pile de modèles à poids ouverts (exécutables localement sans dépendance API propriétaire)

* **Modèle Agent (exécutant les longues tâches et générant les trajectoires honnêtes/dégradées)** :
  * `Qwen2.5-Coder-32B-Instruct` ($32\text{ milliards}$ `(illustratif)` de paramètres) ou `Llama-3.3-70B-Instruct` ($70\text{ milliards}$ `(illustratif)` de paramètres, quantifié en `FP8` ou `AWQ 4-bit` `(illustratif)` pour tenir sur $1\times \text{GPU 80 Go VRAM}$ `(illustratif)`).
* **Modèle Moniteur (I4) et Extracteur/Vérificateur (I1, I2)** :
  * Pour refléter l'asymétrie réaliste où le surveillant est moins coûteux que l'agent surveillé : `Qwen2.5-7B-Instruct` ($7\text{ milliards}$ `(illustratif)` de paramètres) ou `Llama-3.1-8B-Instruct` ($8\text{ milliards}$ `(illustratif)` de paramètres) en précision `BF16` ($16\text{ bits}$ `(illustratif)`).
* **Modèle d'indexation dense pour le découplage lexical (Passe 2 de l'instrument I2)** :
  * Encodeur bi-directionnel ouvert `BAAI/bge-large-en-v1.5` ($\approx 335\text{ millions}$ `(illustratif)` de paramètres) associé à un ré-ordonnanceur (*reranker*) ouvert `bge-reranker-large` ($\approx 560\text{ millions}$ `(illustratif)` de paramètres).

### 2. Budget de calcul détaillé par expérience

L'ensemble du protocole est dimensionné pour s'exécuter sur un nœud unique doté de $1\times \text{GPU NVIDIA A100 (80 Go VRAM)}$ `(illustratif)` (ou $2\times \text{RTX 4090 24 Go}$ `(illustratif)` pour les modèles $\le 32\text{B}$ `(illustratif)` quantifiés), avec le moteur d'inférence ouvert `vLLM` :

1. **Calcul pour E1 et E2 (Instruments méta-scientifiques I1 et I2)** :
   * Analyse du texte intégral de $30$ `(illustratif)` à $100$ `(illustratif)` publications ($\approx 15\,000$ `(illustratif)` jetons par article) + filtrage de $3\,000$ `(illustratif)` résumés et contextes de citations ($\approx 500$ `(illustratif)` jetons chacun) = $\approx 3\text{ millions}$ `(illustratif)` de jetons en entrée et $\approx 0{,}5\text{ million}$ `(illustratif)` de jetons générés.
   * Avec `Llama-3.1-8B-Instruct` sous `vLLM` (débit $\approx 2\,500\text{ jetons/s}$ `(illustratif)` en lot sur $\text{A100}$ `(illustratif)`) + indexation dense : **$\approx 3\text{ heures-GPU A100}$ `(illustratif)`**.
2. **Calcul pour E3 (Triage ex-ante I3 sur $12$ `(illustratif)` manques candidats)** :
   * $12$ `(illustratif)` candidats $\times 40$ `(illustratif)` traces pilotes ($20$ `(illustratif)` honnêtes + $20$ `(illustratif)` rejeux) $\times 12\,000$ `(illustratif)` jetons moyens par trace = $\approx 5{,}8\text{ millions}$ `(illustratif)` de jetons générés/évalués.
   * Temps machine (incluant l'exécution des conteneurs Docker de tests mécaniques sur CPU $16\text{ cœurs}$ `(illustratif)`) : **$\approx 18\text{ heures-GPU A100}$ `(illustratif)`**.
3. **Calcul pour E4 (Surveillance sur tâches longues I4)** :
   * Génération de $400$ `(illustratif)` trajectoires complètes ($200$ `(illustratif)` honnêtes appariées + $200$ `(illustratif)` dégradées) de $50$ `(illustratif)` étapes en moyenne par l'agent `Qwen2.5-Coder-32B-Instruct` ($\approx 25\,000$ `(illustratif)` jetons de contexte cumulé par trajectoire avec mise en cache des préfixes KV, soit $\approx 10\text{ millions}$ `(illustratif)` de nouveaux jetons générés et $\approx 80\text{ millions}$ `(illustratif)` de jetons de préfixe lus) : **$\approx 65\text{ heures-GPU A100}$ `(illustratif)`**.
   * Passage des moniteurs `7B/8B` `(illustratif)` (Moniteur A par invariants d'étapes vs Moniteur B holistique) sur les $400$ `(illustratif)` trajectoires enregistrées : **$\approx 14\text{ heures-GPU A100}$ `(illustratif)`**.

### 3. Coût total estimé (Matériel et Humain)

* **Total calcul GPU** : $3 + 18 + 65 + 14 = 100\text{ heures-GPU A100 (80 Go)}$ `(illustratif)`.
* **Coût financier infonuagique** : Au tarif de location à la demande ou préemptible pour la recherche ($\approx 1{,}40\text{ \$}$ `(illustratif)` à $1{,}80\text{ \$ / heure-GPU A100}$ `(illustratif)`), le coût matériel total est de **$140\text{ \$}$ `(illustratif)` à $180\text{ \$}$ `(illustratif)`** (soit moins de $200\text{ \$}$ `(illustratif)` pour l'intégralité des quatre expériences).
* **Stockage et CPU** : $200\text{ Go}$ `(illustratif)` de stockage NVMe pour les instantanés de conteneurs Docker et journaux de traces ($\approx 20\text{ \$ / mois}$ `(illustratif)`).
* **Effort humain d'audit** : $2$ `(illustratif)` chercheurs pendant $20\text{ heures}$ `(illustratif)` chacun (soit $40\text{ heures-personne}$ `(illustratif)`) pour la double annotation en aveugle de l'expérience E1, la validation des triplets fonctionnels de E2 et l'inspection d'échantillons lors du contrôle O1 de E3.

FIN-DE-CELLULE