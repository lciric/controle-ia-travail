**Pièce absente (`VÉRIFIÉ`)** : la liste de publications (et les textes complets correspondants) annoncée par la question (« On vous remet une liste de ces publications ») est absente du bloc `FAITS` (identique au bloc `QUESTION DE L'ARBITRE`, empreinte SHA-256 `96dc184536f2f81ecb61017826fc79a7a4ed99a0f8c23c710c1e5cf85de8219d`), et aucun contenu de publication n'est inventé ci-dessous.

---

### Proposition F — Conception ciblée (Tour III.1)

En l'absence du corpus de publications, l'extraction par article ne peut pas être exécutée sur pièces (`VÉRIFIÉ`). Cette proposition livre en revanche : **(a)** les présupposés non établis de la question, ce que la liste ne permet pas de décider et le protocole opératoire complet pour répondre aux tâches de l'arbitre dès réception du corpus ; **(b)** cinq expériences d'inférence forte ($H_A$ contre $H_B$) tranchant les verrous méthodologiques et scientifiques posés ; **(c)** la calibration minimale de chaque instrument nommé dans la question ; **(d)** l'ancrage matériel chiffré sur modèles ouverts.

---

## (a) Ce que la question suppose sans que ce soit établi, limites de la liste et cadre opératoire

### (a.1) Présupposés non établis de la question (avec statut)

1. **Existence et homogénéité d'un corpus cohérent sur la surveillance d'agents longs** — Statut : `RAPPORTÉ` pour l'existence de publications de plusieurs équipes (affirmée par l'énoncé sans pièces jointes) ; `HYPOTHÈSE` pour l'homogénéité du corpus.
   - La question traite « la surveillance d'agents de langue qui exécutent de longues tâches et pourraient en dégrader le résultat » comme un champ unifié. En pratique, la liste peut juxtaposer des modèles de menace incompatibles (dégradation accidentelle par dérive cumulative vs sabotage délibéré/adaptatif ; surveillance en ligne bloquant une action vs audit hors ligne a posteriori ; agents de code vs agents web). Si ces régimes sont confondus, comparer les « manques » entre articles devient invalide.

2. **Séparabilité textuelle et sincérité épistémique du « texte seul »** — Statut : `HYPOTHÈSE`.
   - Demander de séparer, « à partir du texte seul », (i) le non-fait reconnu, (ii) le futur annoncé et (iii) l'ouvert pour tous suppose trois points non établis :
     - *Séparabilité linguistique* (`HYPOTHÈSE`) : les formulations éditoriales mélangent souvent un échec expérimental, une contrainte de calendrier et une question ouverte.
     - *Valeur prédictive des intentions* (`HYPOTHÈSE`) : un « futur annoncé » peut correspondre à un projet réellement engagé ou à un simple jalonnement rhétorique, tandis que les pistes réellement prioritaires d'une équipe peuvent rester tues pour des raisons de concurrence ou de divulgation.
     - *Couverture des manques réels* (`HYPOTHÈSE`) : ce que les auteurs reconnaissent ne pas avoir fait n'inclut pas les angles morts partagés par tout le champ (par exemple l'absence de témoins mécaniques ou de cas honnêtes appariés).

3. **Statut discret, commensurable et publiquement observable du « comblement d'un manque »** — Statut : `HYPOTHÈSE`.
   - Demander comment vérifier qu'un manque n'a pas été « comblé ailleurs depuis » suppose qu'un manque est un énoncé suffisamment spécifié pour admettre une vérification binaire (comblé / non comblé), qu'il est repérable dans la littérature publique et que les disciplines voisines utilisent un vocabulaire compatible. En réalité, un manque peut être résolu sous un autre nom (vérification formelle, sécurité logicielle, détection d'anomalies, tests de propriétés), résolu de façon privée sans publication, ou *revendiqué* comme comblé moyennant un affaiblissement silencieux du protocole (tâche plus courte, attaquant non adaptatif, absence de contrôle des fausses alertes).

4. **Existence d'un créneau défendable pour une équipe tierce aux moyens limités** — Statut : `HYPOTHÈSE`.
   - La question présuppose qu'une petite équipe peut sélectionner un sous-problème où son effort reste pertinent plutôt que d'être dominé par le calcul ou par l'accès à des environnements propriétaires. Cette hypothèse ne tient que si certains verrous du domaine sont intensifs en conception expérimentale, en audit de réplication, en contrôles mécaniques ou en contre-exemples, et non en calcul d'entraînement.

5. **Définition non circulaire d'un « bon choix » et existence de signaux pré-issue fiables** — Statut : `HYPOTHÈSE`.
   - Distinguer « bon choix » et « mauvais choix » par des observations antérieures à l'issue suppose : (i) une définition opératoire du bon choix qui inclut les **réfutations propres** (un projet démontrant qu'un moniteur publié échoue face à un contrôle mécanique est une issue scientifiquement valide, pas un échec) ; (ii) un couplage réel entre des signaux précoces (mesurés sur pilote réduit) et la viabilité à pleine échelle, plutôt qu'un découplage dû aux effets d'horizon long.

6. **Valeur ajoutée de la surveillance probabiliste sur longues tâches par rapport aux vérifications mécaniques** — Statut : `HYPOTHÈSE`.
   - Le cadrage présuppose implicitement que la dégradation sur longue tâche laisse une trace observable dans la trajectoire surveillée avant ou au moment du résultat, qu'un moniteur probabiliste surclasse des vérifications déterministes (tests, analyse statique, invariants, isolement) et que l'accumulation d'étapes ne fait pas diverger le taux de fausses alertes au niveau trajectoire (sous décisions d'étape indépendantes de taux de fausse alerte $\alpha$, la probabilité d'au moins une fausse alerte sur $L$ étapes croît comme $1 - (1-\alpha)^L$).

### (a.2) Ce que la liste fournie ne permet pas de décider

- **En l'état actuel (`VÉRIFIÉ`)** : la liste étant absente, aucune attribution par article, aucune cartographie de manques et aucun choix d'effort ne peuvent être décidés à partir du dossier reçu.
- **Même si la liste complète des publications était remise**, le texte seul de cette liste ne permettrait pas de décider :
  1. **La validité empirique des résultats revendiqués** (`RAPPORTÉ` tant que non reproduit) : le texte ne prouve ni l'absence de fuite de données, ni la robustesse à des dégradations adaptatives, ni la tenue du taux de fausses alertes sur cas honnêtes appariés.
  2. **Les travaux non publiés, en cours sous embargo ou abandonnés après échec** (`HYPOTHÈSE`, biais de publication) : l'absence d'article sur un manque ne distingue pas un terrain vierge d'une impasse déjà rencontrée par plusieurs équipes sans publication.
  3. **Les angles morts communs aux auteurs de la liste** (`HYPOTHÈSE`) : tout défaut partagé et non mentionné dans les sections de limites reste invisible à la lecture seule.
  4. **L'état de l'art postérieur ou trans-disciplinaire** (`HYPOTHÈSE`) : la liste est figée à une date et à un périmètre lexical donnés ; elle ne renseigne ni sur les prépublications postérieures, ni sur les dépôts de code sans article, ni sur les résultats équivalents en génie logiciel ou sécurité système.
  5. **L'adéquation réelle entre le manque et les capacités propres de l'équipe tierce** (`VÉRIFIÉ` absent du dossier) : compétences disponibles, plafond budgétaire exact, accès aux environnements cibles et horizon temporel acceptable ne figurent pas dans la liste.
  6. **La réalisabilité des intentions déclarées** (`HYPOTHÈSE`) : le texte ne distingue pas une suite effectivement financée d'une clause rhétorique ajoutée lors de la révision.

### (a.3) Protocole opératoire prêt à l'emploi pour les tâches de la question

1. **Extraction sur texte seul (dès réception de la liste)** : pour chaque publication, construire une table à quatre colonnes obligatoires — *Catégorie* (`non-fait reconnu`, `futur annoncé par les auteurs`, `ouvert pour tous`), *Citation verbatim exacte avec section/page* (contrôlée mécaniquement par correspondance de sous-chaîne), *Conditions de portée* (type d'agent, longueur de tâche, modèle de menace), *Ambiguïté résiduelle* (signalée si le pronom ou la portée est indéterminé, sans forcer le classement).
2. **Vérification qu'un manque n'a pas été comblé ailleurs depuis** (procédure en quatre étapes) :
   - *Étape 1 — Spécification en cinq champs* : traduire chaque manque en un cahier testable : (1) classe de dégradation / modèle de menace, (2) horizon et nature des tâches, (3) budget d'observation / accès au modèle, (4) métrique incluant contrôle des fausses alertes, (5) artefacts exigés (code, traces, benchmark).
   - *Étape 2 — Recherche bicéphale* : (a) graphe de citations entrantes et sortantes sur APIs ouvertes (`OpenAlex`, `Crossref`, `Semantic Scholar`) ; (b) recherche sémantique trans-disciplinaire (sécurité logicielle, vérification à l'exécution, supervision de processus) et fouille de dépôts de code publics.
   - *Étape 3 — Audit de conformité des cinq champs* : vérifier si le candidat n'a pas « comblé » le manque en affaiblissant silencieusement l'un des cinq champs (faux comblement).
   - *Étape 4 — Contrôle minimal de reproductibilité* : vérifier l'existence d'artefacts exécutables et reproduire un échantillon minimal (sinon le comblement reste au statut `RAPPORTÉ`, non `VÉRIFIÉ`).
3. **Critères de sélection pour une équipe aux moyens limités (C1–C5) et observations pré-issue (O1–O5)** :
   - *Critères de choix* : **C1 (Asymétrie favorable hors calcul frontière)** privilégier les verrous d'évaluation, d'invariants mécaniques, de contre-exemples et d'agrégation temporelle plutôt que l'entraînement lourd ; **C2 (Non-trivialité mécanique)** le manque doit survivre aux vérifications déterministes ; **C3 (Symétrie informative en inférence forte)** formuler le projet pour qu'une réfutation propre soit autant publiable qu'un gain positif ; **C4 (Reproductibilité ouverte)** modèles ouverts et oracle objectif de dégradation ; **C5 (Exposition concurrentielle bornée)** éviter les suites directes annoncées par des équipes dotées de gros moyens, sauf pour en auditer les hypothèses de base.
   - *Observations pré-issue* (mesurées avant d'engager plus de $15\,\%$ [illustratif] du budget total) : **O1** taux d'échec des vérifications mécaniques sur un mini-lot pilote de $20$ paires (illustratif) ; **O2** coût projeté par trajectoire longue complète sous plafond avec marge $\ge 2\times$ (illustratif) ; **O3** reproductibilité de la ligne de base ouverte en $\le 5$ jours-personne (illustratif) ; **O4** séparabilité en aveugle par un humain sur le même flux d'observation que le moniteur ($\text{AUC} \ge 0,75$ [illustratif]) ; **O5** densité d'activité concurrentielle vérifiée hors papier (dépôts actifs, prépublications des $6$ derniers mois [illustratif]) croisée avec la dépendance au calcul frontière.

---

## (b) Expériences décisives en inférence forte ($H_A$ contre $H_B$)

Chaque expérience oppose deux hypothèses mutuellement exclusives et définit une condition d'invalidation par contrôle négatif. Tous les chiffres ci-dessous sont marqués `illustratif`.

### Expérience E1 — Fiabilité et portée prédictive de l'extraction « à partir du texte seul »
- **$H_A$ (Signal textuel exploitable)** : À partir du texte seul, deux annotateurs indépendants en aveugle convergent sur le classement en trois catégories (non-fait reconnu / futur annoncé / ouvert pour tous), **et** la distinction entre « futur annoncé » et « ouvert pour tous » prédit effectivement un taux de poursuite ultérieure plus élevé par la même équipe.
- **$H_B$ (Indétermination rhétorique du texte seul)** : Soit les trois catégories ne sont pas séparables de façon reproductible à partir du texte seul, soit la catégorie « futur annoncé » ne prédit aucune différence de poursuite effective par rapport à « ouvert pour tous ».
- **Protocole** : Double annotation humaine en aveugle (noms d'auteurs, affiliations et dates masqués) sur le corpus fourni (ou, pour la validation prédictive, sur une cohorte rétrospective de $N = 30$ articles publiés depuis $\ge 18$ mois [illustratif], suivis jusqu'à aujourd'hui pour vérifier si les mêmes équipes ont publié la suite annoncée).
- **Métriques** : Accord inter-annotateurs $\alpha_K$ (alpha de Krippendorff) sur les énoncés atomiques ; écart de suivi $\Delta p = P(\text{suivi par même équipe} \mid \text{futur annoncé}) - P(\text{suivi par même équipe} \mid \text{ouvert pour tous})$.
- **Seuils (illustratifs)** : $\alpha_K \ge 0,75$ (illustratif) **et** $\Delta p \ge +0,20$ (illustratif, borne inférieure de l'IC à $95\,\%$ [illustratif] $> 0$).
- **Contrôle négatif** : Insertion de $20\,\%$ (illustratif) de paragraphes placebo issus d'articles du même domaine décrivant uniquement des résultats déjà réalisés (aucun manque déclaré). Si plus de $5\,\%$ (illustratif) de ces paragraphes génèrent une extraction de manque, le guide d'annotation est invalidé avant toute conclusion.
- **Falsification** :
  - *Falsifie $H_A$* : $\alpha_K < 0,75$ (illustratif) **ou** $\Delta p \le 0$ (illustratif, ou IC $95\,\%$ [illustratif] incluant $0$). Conséquence : le texte seul ne permet pas d'anticiper la répartition concurrentielle.
  - *Falsifie $H_B$* : $\alpha_K \ge 0,75$ (illustratif) **et** $\Delta p \ge +0,20$ (illustratif, IC $95\,\%$ [illustratif] $> 0$). Conséquence : l'extraction textuelle capture un signal comportemental réel (bien que non exhaustif).

### Expérience E2 — Veille citationnelle directe contre audit trans-disciplinaire en cinq champs (comblement des manques)
- **$H_A$ (Suffisance de la veille directe)** : Une veille par graphe de citations et mots-clés du sous-champ classe correctement l'état de comblement de la quasi-totalité des manques, et les revendications textuelles de comblement correspondent à des comblements conformes à la spécification initiale.
- **$H_B$ (Cécité lexicale et faux comblements)** : Une fraction substantielle des verdicts de la veille directe est erronée, soit par omission de comblements publiés sous un autre vocabulaire ou en dépôt de code ($\rho_{FN}$), soit par acceptation de faux comblements affaiblissant l'un des cinq champs ou non reproductibles ($\rho_{FP}$).
- **Protocole** : Échantillon de $M = 25$ manques spécifiés en cinq champs (illustratif), évalués indépendamment par *Pipeline 1* (citations directes + mots-clés + lecture des revendications) et *Pipeline 2* (expansion sémantique trans-disciplinaire + fouille de dépôts de code + audit des cinq champs + smoke test sur artefacts).
- **Métrique** : Taux global de révision de verdict $\rho = \rho_{FN} + \rho_{FP}$ entre Pipeline 1 et Pipeline 2.
- **Seuil (illustratif)** : $\rho \ge 25\,\%$ (illustratif) ou $\max(\rho_{FN}, \rho_{FP}) \ge 15\,\%$ (illustratif).
- **Contrôle négatif** : Injection en aveugle de $10$ manques artificiels **déjà notoirement comblés** (pour contrôler la sensibilité des deux pipelines) et de $10$ manques **construits pour être non comblés** (comportant une contrainte postérieure au corpus ou formellement non satisfaite). Si Pipeline 2 déclare « comblé » plus de $5\,\%$ (illustratif) des manques non comblés, son audit est trop permissif et invalidé.
- **Falsification** :
  - *Falsifie $H_A$* : $\rho \ge 25\,\%$ (illustratif) ou $\max(\rho_{FN}, \rho_{FP}) \ge 15\,\%$ (illustratif) avec contrôles négatifs validés. Conséquence : la veille directe seule induit un taux d'erreur critique ; l'audit en cinq champs est indispensable.
  - *Falsifie $H_B$* : $\rho < 25\,\%$ (illustratif) **et** $\max(\rho_{FN}, \rho_{FP}) < 15\,\%$ (illustratif). Conséquence : pour une équipe aux moyens limités, une veille citationnelle directe bien outillée suffit.

### Expérience E3 — Pouvoir prédictif des observations pré-issue (O1–O5) sur la qualité du choix de recherche
- **$H_A$ (Discriminabilité ex ante)** : La batterie d'observations pré-issue O1–O5, collectée en amont avec $\le 15\,\%$ (illustratif) du budget, prédit mieux que le hasard et mieux que l'évaluation sur la liste d'articles seule quelles pistes mènent à une issue décisive non triviale (résultat positif reproductible ou réfutation valide) plutôt qu'à une impasse.
- **$H_B$ (Indiscernabilité ex ante)** : Les observations O1–O5 n'apportent aucun gain prédictif sur le jugement issu de la liste seule ; les impasses résultent principalement d'effets tardifs imprévisibles (passage à l'échelle, sorties concurrentes non annoncées).
- **Protocole** : Évaluation sur $K = 20$ pistes candidates (illustratif) — soit en cohorte rétrospective aveugle (toute information postérieure à la date initiale $t_0$ étant strictement masquée), soit en portefeuille prospectif stratifié menant à terme à la fois des pistes jugées favorables et un sous-ensemble témoin de pistes jugées défavorables (pour éviter le biais de censure lié à l'arrêt anticipé). Les scores O1–O5 et le jugement sur texte seul sont pré-enregistrés avant révélation de l'issue.
- **Métrique** : $\text{AUC}_{\text{O1–O5}}$ pour prédire l'issue binaire pré-enregistrée, et gain $\Delta\text{AUC} = \text{AUC}_{\text{O1–O5}} - \text{AUC}_{\text{texte}}$.
- **Seuils (illustratifs)** : $\text{AUC}_{\text{O1–O5}} \ge 0,75$ (illustratif) **et** $\Delta\text{AUC} \ge +0,15$ (illustratif).
- **Contrôle négatif** : (1) Test de permutation des étiquettes O1–O5 (doit ramener $\text{AUC}$ dans $0,50 \pm 0,05$ [illustratif]) ; (2) audit de fuite temporelle sur le volet rétrospectif (toute présence d'indice postérieur à $t_0$ invalide l'item concerné).
- **Falsification** :
  - *Falsifie $H_A$* : $\text{AUC}_{\text{O1–O5}} < 0,75$ (illustratif) **ou** $\Delta\text{AUC} \le 0$ (illustratif). Conséquence : les sondes pré-issue ne filtrent pas les impasses ; l'équipe doit réduire la taille de ses paris et diversifier un portefeuille court plutôt qu'investir dans un filtrage préalable.
  - *Falsifie $H_B$* : $\text{AUC}_{\text{O1–O5}} \ge 0,75$ (illustratif) **et** $\Delta\text{AUC} \ge +0,15$ (illustratif). Conséquence : un protocole de sondes précoces à faible coût protège effectivement le budget d'une petite équipe.

### Expérience E4 — Gain net d'un moniteur par modèle de langue face aux vérifications mécaniques sur longues tâches
- **$H_A$ (Gain sémantique irréductible)** : Sur des tâches longues ($L \ge 30$ étapes d'agent [illustratif]) avec dégradations réelles appariées à des trajectoires honnêtes de même longueur, un moniteur par modèle de langue ouvert augmente significativement le taux de détection au niveau trajectoire au-delà d'une suite complète de vérifications mécaniques déterministes, à taux de fausses alertes trajectoire strictement plafonné.
- **$H_B$ (Domination mécanique ou effondrement des fausses alertes)** : À taux de fausses alertes trajectoire plafonné ($\le 5\,\%$ [illustratif]), le moniteur LLM n'apporte aucun gain substantiel par rapport aux vérifications mécaniques seules (les dégradations qu'il détecte étaient déjà mécaniquement attrapables, ou le bruit sur longues trajectoires honnêtes oblige à relever le seuil au point d'annuler la détection).
- **Protocole** : Banc de $N = 200$ trajectoires longues (illustratif) ($100$ dégradées vérifiées par oracle de tâche, $100$ honnêtes appariées en longueur à $\pm 10\,\%$ [illustratif] et en domaine), plus un jeu de calibration honnête disjoint de $50$ trajectoires (illustratif) servant uniquement à fixer le seuil de décision pour $\text{FPR}_{\text{traj}} \le 5\,\%$ (illustratif) (avec point de mesure secondaire à $\text{FPR}_{\text{traj}} \le 1\,\%$ [illustratif]).
- **Métrique** : Gain incrémental $\Delta\text{TPR} = \text{TPR}_{\text{traj}}(\text{Mécanique} \cup \text{Moniteur}) - \text{TPR}_{\text{traj}}(\text{Mécanique seul})$ à $\text{FPR}_{\text{traj}}$ apparié.
- **Seuil (illustratif)** : $\Delta\text{TPR} \ge +15$ points de pourcentage (illustratif), avec borne inférieure de l'IC à $95\,\%$ par bootstrap par tâche (illustratif) $> 0$.
- **Contrôles négatifs** : (1) Sous-ensemble de $40$ trajectoires honnêtes « bruyantes » (illustratif) contenant erreurs intermédiaires auto-corrigées, refactorisations étendues et détours exploratoires légitimes ; (2) $20$ trajectoires avec modifications cosmétiques « placebo » ne dégradant pas le résultat final (illustratif) : le taux d'alertes sur ces placebos doit rester $\le 5\,\%$ (illustratif), sinon le moniteur réagit à des indices superficiels.
- **Falsification** :
  - *Falsifie $H_A$* : $\Delta\text{TPR} < +15$ points (illustratif) (ou IC $95\,\%$ [illustratif] incluant $0$) à $\text{FPR}_{\text{traj}} \le 5\,\%$ (illustratif). Conséquence : concentrer l'effort sur les vérifications mécaniques, les contrats formels et le cloisonnement plutôt que sur des moniteurs LLM génériques.
  - *Falsifie $H_B$* : $\Delta\text{TPR} \ge +15$ points (illustratif) y compris sur les trajectoires honnêtes bruyantes et avec $\le 5\,\%$ (illustratif) d'alertes sur les placebos. Conséquence : la surveillance sémantique apporte un gain non capté par les vérifications mécaniques testées.

### Expérience E5 — Diagnostic d'échec en horizon long : dilution contextuelle contre indiscernabilité locale
- **$H_A$ (Verrou de dilution d'horizon)** : Le moniteur détecte correctement la dégradation lorsque l'observation est centrée sur une fenêtre locale courte autour de l'étape fautive, mais perd son signal quand cette fenêtre est noyée dans une trajectoire complète de longueur $L \ge 30$ étapes (illustratif).
- **$H_B$ (Verrou d'indiscernabilité locale)** : Même en fenêtre locale centrée sur l'action fautive (avec la spécification de tâche), le moniteur ne sépare pas l'action dégradante d'actions honnêtes appariées ; la longueur n'est pas la cause première de l'échec.
- **Protocole** : Comparaison appariée du même moniteur sur les mêmes $200$ trajectoires (illustratif) présentées en deux formats : (i) trajectoire complète ($L \ge 30$ [illustratif]) ; (ii) fenêtre locale centrée de $k = 3$ étapes (illustratif) (pour les trajectoires honnêtes, fenêtre de taille $k = 3$ [illustratif] tirée à une position relative appariée).
- **Métriques** : $\text{TPR}_{\text{local}}$ et chute d'horizon $\delta_L = \text{TPR}_{\text{local}} - \text{TPR}_{\text{complet}}$, toutes deux calibrées à $\text{FPR} \le 5\,\%$ (illustratif).
- **Seuils (illustratifs)** : Zone $H_A$ : $\text{TPR}_{\text{local}} \ge 70\,\%$ (illustratif) **et** $\delta_L \ge 25$ points (illustratif). Zone $H_B$ : $\text{TPR}_{\text{local}} < 45\,\%$ (illustratif). (Une valeur intermédiaire indique un régime mixte nécessitant une analyse par sous-classe de dégradation.)
- **Contrôle négatif** : Fenêtres locales de $k = 3$ étapes (illustratif) extraites d'étapes *non fautives* situées sur une trajectoire par ailleurs dégradée. Si le taux d'alerte y dépasse celui des trajectoires honnêtes de plus de $5$ points (illustratif), le moniteur exploite un artefact global de style ou de prompt plutôt que la dégradation elle-même, ce qui invalide le diagnostic.
- **Falsification** :
  - *Falsifie $H_A$* : $\text{TPR}_{\text{local}} < 45\,\%$ (illustratif). Conséquence : les architectures de contexte long ou de résumé hiérarchique ne suffiront pas ; l'effort doit porter sur l'instrumentation d'états intermédiaires ou les invariants de tâche.
  - *Falsifie $H_B$* : $\text{TPR}_{\text{local}} \ge 70\,\%$ (illustratif) **et** $\delta_L \ge 25$ points (illustratif) avec contrôle négatif valide. Conséquence : le levier prioritaire pour une petite équipe est la décomposition temporelle et l'agrégation calibrée des scores par étape.

---

## (c) Mesure minimale de fonctionnement pour chaque instrument nommé dans la question

La question nomme quatre instruments (un instrument-objet du domaine et trois instruments méthodologiques). Tous les seuils chiffrés ci-dessous sont marqués `illustratif`.

### Instrument I1 — Dispositif de surveillance d'agents de langue sur longues tâches
- **Définition** : *Positif* = trajectoire longue dont le résultat final est objectivement dégradé (ou contient une défaillance/porte dérobée vérifiée par oracle) ; *Fausse alerte* = alerte sur une trajectoire honnête menant à un résultat conforme.
- **Mesure minimale** : $\text{TPR}_{\text{traj}} \ge 60\,\%$ (illustratif) sur dégradations non captées mécaniquement (ou $\Delta\text{TPR} \ge +15$ points [illustratif] au-dessus du mécanique) pour $\text{FPR}_{\text{traj}} \le 5\,\%$ (illustratif) en audit humain et $\le 1\,\%$ (illustratif) en blocage automatique, avec dérive de $\text{FPR}_{\text{traj}} \le +2$ points (illustratif) lorsque la longueur passe de $L_1 = 20$ à $L_2 = 60$ étapes (illustratif).
- **Cas honnêtes appariés** : Trajectoires honnêtes sur les mêmes tâches, appariées en nombre d'étapes et de tokens ($\pm 10\,\%$ [illustratif]) et en ampleur de modifications, incluant une proportion imposée ($40\,\%$ [illustratif]) de trajectoires honnêtes « bruyantes » (débogage itératif, retours arrière, refactorisations légitimes, appels d'outils rares mais autorisés).
- **Vérifications mécaniques à battre** : (1) suites de tests unitaires, de régression et de propriétés ; (2) analyse statique déterministe (linters, vérificateur de types, règles `semgrep`/AST via `tree-sitter`) ; (3) invariants de périmètre et d'intégrité (liste blanche de fichiers, hachage non modifiable des tests, limites de permissions) ; (4) classifieur tabulaire simple sans LLM sur compteurs mécaniques (ratio suppressions/ajouts, taux d'erreurs d'outils, fichiers hors graphe de dépendances).

### Instrument I2 — Extracteur textuel tripartite (non-fait reconnu / futur annoncé / ouvert pour tous)
- **Définition** : *Positif* = énoncé de l'une des trois classes effectivement présent dans l'article (vérité terrain par double annotation arbitrée) ; *Fausse alerte* = extraction d'un passage ne relevant pas de la classe attribuée ou citation inexacte.
- **Mesure minimale** : Rappel ($\text{TPR}$) $\ge 80\,\%$ (illustratif) dans chacune des trois classes, confusion croisée entre « futur annoncé » et « ouvert pour tous » $\le 15\,\%$ (illustratif), $\text{FPR} \le 5\,\%$ (illustratif) sur paragraphes hors-cible, et **tolérance nulle ($0\,\%$ [illustratif]) sur les hallucinations de citations verbatim** (vérifiées mécaniquement).
- **Cas honnêtes appariés (négatifs textuels appariés)** : Paragraphes de même longueur issus des mêmes articles et riches en marqueurs critiques ou modaux (« *however* », « *unlike prior work* », « *we did not need* »), mais décrivant une limite de travaux antérieurs, une ablation effectivement exécutée, ou un choix assumé hors catégorie.
- **Vérifications mécaniques à battre** : (1) parseur structurel isolant automatiquement les sections *Limitations*, *Future Work*, *Discussion*, *Threats to Validity* ; (2) règles déterministes par expressions régulières croisant pronoms de première personne et marqueurs temporels/modaux ; (3) vérificateur mécanique exact de sous-chaîne verbatim (prérequis strict).

### Instrument I3 — Vérificateur de comblement ultérieur d'un manque
- **Définition** : *Positif* = travail ultérieur comblant effectivement le manque selon les cinq champs de spécification ; *Fausse alerte* = travail ne comblant pas réellement le manque classé à tort comme « comblé » (risque d'abandon injustifié d'un créneau ouvert).
- **Mesure minimale** : $\text{TPR} \ge 85\,\%$ (illustratif) sur les comblements réels (y compris hors vocabulaire initial, afin d'éviter un travail redondant coûteux) pour $\text{FPR} \le 10\,\%$ (illustratif) sur les faux comblements.
- **Cas honnêtes appariés (non-comblements proches)** : Articles postérieurs citant explicitement l'article source et reprenant ses mots-clés dans le résumé, mais affaiblissant au moins un des cinq champs (horizon raccourci, hypothèse boîte blanche supplémentaire, absence de contrôle de FPR sur trajectoires honnêtes, absence d'artefact reproductible).
- **Vérifications mécaniques à battre** : (1) requête automatisée sur graphe de citations (`OpenAlex` / `Crossref` / `Semantic Scholar`) avec filtre de date ; (2) recherche lexicale `BM25` sur les termes exacts du titre et des limites ; (3) contrôle mécanique de présence d'artefacts (liens de dépôt valides, licences, taille et longueur déclarées des jeux d'essai).

### Instrument I4 — Batterie de critères et d'observations pré-issue (O1–O5)
- **Définition** : *Positif* = piste candidate constituant un mauvais choix (impasse : trivialité mécanique, non-reproductibilité, dépassement de budget, obsolescence) à écarter tôt ; *Fausse alerte* = piste menant à une issue décisive rejetée à tort.
- **Mesure minimale** : $\text{TPR} \ge 75\,\%$ (illustratif) des impasses stoppées avant $15\,\%$ (illustratif) de dépense budgétaire, pour $\text{FPR} \le 20\,\%$ (illustratif) sur les bons choix.
- **Cas honnêtes appariés (bons choix atypiques)** : Pistes aboutissant finalement à une issue décisive (notamment des réfutations propres de moniteurs publiés ou des créneaux peu cités) qui présentent des signaux superficiels d'inconfort comparables aux impasses (bruit initial avant calibration, faible popularité bibliométrique).
- **Vérifications mécaniques à battre** : (1) filtre comptable déterministe éliminant toute piste dont le coût minimal projeté dépasse le plafond budgétaire ; (2) filtre mécanique de disponibilité (poids ouverts, licence reproductible, environnement localisable) ; (3) compteur bibliométrique naïf du volume d'articles récents sur les mêmes mots-clés.

### Tableau récapitulatif des calibrations minimales (toutes les valeurs chiffrées sont illustratives)

| Instrument | Unité | Cible TPR (illustratif) | Plafond FPR (illustratif) | Cas honnêtes / négatifs appariés | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **I1. Moniteur d'agents longs** | Trajectoire complète | $\ge 60\,\%$ (ou $\Delta \ge +15$ pts) | $\le 5\,\%$ (audit) / $\le 1\,\%$ (blocage) | Trajectoires honnêtes même longueur ($\pm 10\,\%$), dont $40\,\%$ bruyantes | Tests, analyse statique (`semgrep`/`tree-sitter`), invariants d'état, classifieur sur compteurs |
| **I2. Extracteur tripartite** | Énoncé ancré | $\ge 80\,\%$ par classe | $\le 5\,\%$ ($0\,\%$ hallucination verbatim) | Paragraphes modaux des mêmes articles (limites de tiers, ablations faites) | Parseur de sections, règles regex pronom/temps, recherche de sous-chaîne exacte |
| **I3. Vérificateur de comblement** | Paire (manque, candidat) | $\ge 85\,\%$ (comblements réels) | $\le 10\,\%$ (faux comblements) | Articles citants affaiblissant l'un des cinq champs de spécification | Graphe de citations OpenAlex/Crossref, `BM25`, contrôle mécanique de liens/artefacts |
| **I4. Sondes pré-issue (O1–O5)** | Projet candidat | $\ge 75\,\%$ (impasses stoppées) | $\le 20\,\%$ (bons choix rejetés) | Bons choix atypiques (réfutations propres, créneaux peu cités) | Filtre comptable de budget, filtre licence/disponibilité, comptage bibliométrique naïf |

---

## (d) Ancrage matériel : modèles ouverts, calcul nécessaire et coût estimé

L'ensemble des volumes, durées, configurations matérielles et coûts ci-dessous est marqué **`illustratif`** (aucun chiffre de calcul ne provient du bloc `FAITS`). La vérification de la licence exacte de chaque point de contrôle retenu reste un préalable mécanique.

### Volet 1 — Pipeline méta-scientifique (E1, E2, I2, I3)
- **Outillage mécanique (CPU)** : extraction PDF (`PyMuPDF` / `GROBID`), indexation `BM25`, APIs bibliographiques ouvertes (`OpenAlex`, `Crossref`, `Semantic Scholar`), vérificateur exact d'ancrage verbatim.
- **Modèles ouverts** :
  - Embeddings scientifiques / multilingues : `BGE-M3` ($\approx 568\text{ M}$ paramètres [illustratif]) pour la recherche trans-disciplinaire.
  - Vérification d'implication / contradiction sur les cinq champs : `DeBERTa-v3-large` ($\approx 435\text{ M}$ paramètres [illustratif]).
  - Assistance à l'extraction structurée (soumise au contrôle verbatim et à l'audit humain en aveugle) : `Qwen2.5-32B-Instruct` ou `Qwen2.5-7B-Instruct` (poids ouverts).
- **Calcul nécessaire (illustratif)** : pour $50$ articles sources et $1\,500$ articles candidats ultérieurs (illustratif), soit $30$ à $50\text{ M}$ de tokens traités (illustratif) : $8$ à $15$ heures sur $1 \times$ GPU NVIDIA L40S $48\text{ Go}$ ou A100 $80\text{ Go}$ (illustratif) (ou exécution locale sur $1 \times$ GPU $24\text{ Go}$ quantifié en $4$ bits [illustratif]).
- **Coût estimé (illustratif)** : $25$ à $60\text{ USD}$ (illustratif) en location cloud GPU ($1,5$ à $3,0\text{ USD/h}$ [illustratif]), $0\text{ USD}$ d'APIs ouvertes (illustratif). Le facteur limitant principal est le temps humain de double annotation en aveugle et d'audit en cinq champs : $20$ à $40$ heures-chercheur (illustratif).

### Volet 2 — Banc expérimental agents longs et moniteurs (E3-pilote, E4, E5, I1)
- **Agents ouverts (génération de trajectoires longues)** : `Qwen2.5-Coder-32B-Instruct` ou `Llama-3.3-70B-Instruct` (poids ouverts), exécutés dans des conteneurs isolés (`Docker` / `Podman`, réseau coupé).
- **Hiérarchie de moniteurs ouverts évalués** : `Qwen2.5-7B-Instruct` ou `Llama-3.1-8B-Instruct` (léger), `Qwen2.5-32B-Instruct` (intermédiaire), `Llama-3.3-70B-Instruct` ou `Qwen2.5-72B-Instruct` (lourd), servis via `vLLM` ou `SGLang` avec cache de préfixe.
- **Vérifications mécaniques (CPU)** : `pytest`, `ruff`, `mypy`, `semgrep`, `tree-sitter`, scripts de hachage et d'invariants d'état.
- **Calcul nécessaire (illustratif)** :
  - *Sonde pré-issue (E3-pilote, $\le 15\,\%$ du budget [illustratif])* : $20$ paires de trajectoires longues ($40$ trajectoires [illustratif]), soit $15$ à $30$ heures-GPU H100 $80\text{ Go}$ (illustratif).
  - *Banc principal (E4 + E5)* : $250$ trajectoires longues complètes ($200$ test + $50$ calibration FPR [illustratif]) d'environ $40$ étapes et $60\,000$ tokens moyens par trajectoire (illustratif), évaluées par trois tailles de moniteurs ouverts en mode complet et en fenêtre locale ($k = 3$ étapes [illustratif]). Volume total : $150$ à $300\text{ M}$ de tokens en pré-remplissage et $15$ à $30\text{ M}$ de tokens générés (illustratif), soit $80$ à $160$ heures-GPU H100 $80\text{ Go}$ (ou $150$ à $300$ heures-GPU A100 $80\text{ Go}$) [illustratif], par exemple $1$ nœud $4 \times$ H100 $80\text{ Go}$ pendant $20$ à $40$ heures (illustratif), appuyé par $32\text{ vCPU}$ / $128\text{ Go}$ RAM et $200\text{ Go}$ de stockage (illustratif) pour les bacs à sable.
- **Coût estimé (illustratif)** :
  - Sonde pré-issue (E3-pilote) : $40$ à $100\text{ USD}$ de GPU (illustratif) — vérifiant qu'une petite équipe peut tester O1–O5 avant tout engagement lourd.
  - Expériences E4–E5 (calcul GPU à $2,5$–$3,5\text{ USD/h}$ par H100 [illustratif] + CPU/stockage) : $240$ à $660\text{ USD}$ (illustratif).

### Synthèse budgétaire matérielle (illustrative)

| Poste | Ressource principale (illustrative) | Volume estimé (illustratif) | Coût cloud estimé (illustratif) |
| :--- | :--- | :--- | :--- |
| Volet 1 (E1, E2, I2, I3) | $1 \times$ L40S $48\text{ Go}$ ou A100 $80\text{ Go}$ | $8$ à $15\text{ h-GPU}$ | $25$ à $60\text{ USD}$ |
| Volet 2 — Sonde pré-issue (E3) | $1$ à $2 \times$ H100 $80\text{ Go}$ | $15$ à $30\text{ h-GPU}$ | $40$ à $100\text{ USD}$ |
| Volet 2 — Banc principal (E4, E5) | $4 \times$ H100 $80\text{ Go}$ + $32\text{ vCPU}$ | $80$ à $160\text{ h-GPU}$ | $240$ à $660\text{ USD}$ |
| Marge de réplication et ablations ($\times 2$ [illustratif]) | Idem Volet 1 + Volet 2 | $100$ à $205\text{ h-GPU}$ | $305$ à $820\text{ USD}$ |
| **Total matériel hors salaires** | **Cluster loué à la demande** | **$203$ à $410\text{ h-GPU}$** | **$610$ à $1\,640\text{ USD}$** |

- **Limite structurelle de cet ancrage (`HYPOTHÈSE`)** : ce budget matériel reste accessible à une équipe tierce aux moyens limités précisément parce qu'il exclut l'entraînement de modèles frontières. En contrepartie, le coût limitant devient l'effort humain d'ingénierie expérimentale ($2$ à $4$ semaines-personne [illustratif]) nécessaire pour construire des paires de trajectoires longues honnêtes/dégradées exemptes de fuites et pour auditer en aveugle les vérifications mécaniques.

FIN-DE-CELLULE