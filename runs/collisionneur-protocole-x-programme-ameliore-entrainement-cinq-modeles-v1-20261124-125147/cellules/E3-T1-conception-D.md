### 1. Ce qu'un expert du domaine ferait ici, et que la question ne demande pas

Avant d'élargir le programme ou d'y ajouter l'entraînement, un praticien expérimenté ferait trois vérifications préalables que la question passe sous silence.

**a) Dresser l'inventaire des présupposés non établis de la question.** Demander s'il faut « garder, retirer, ajouter » et « aborder l'entraînement comme parade » suppose implicitement cinq points qui ne sont pas acquis :
1. *Existence d'un objet interne à lire* : que les saboteurs du banc encodent leur sabotage dans leurs activations (`HYPOTHÈSE`), alors qu'une sonde échoue déjà sur les dénégations d'un saboteur qui ne se croit pas fautif (`RAPPORTÉ`, référence à vérifier).
2. *Séparabilité sur tâche ouverte* : qu'une sonde possède un pouvoir séparateur non nul sur une tâche difficile à noter, alors qu'une recherche bornée n'a trouvé aucune mesure dans aucun sens (`OBSERVÉ-NON-AUDITÉ`) ; je ne sais pas si ce signal existe sur le modèle ouvert de huit milliards de paramètres (`VÉRIFIÉ`).
3. *Neutralité mécanique de l'adaptateur* : que la sonde lit la politique saboteuse et non la signature géométrique du réglage fin léger, alors qu'une sonde apprise contre le modèle de base signale presque tous les exemples d'adaptateurs bénins (`RAPPORTÉ`, référence à vérifier).
4. *Solidité de l'organisme expérimental* : que le saboteur à adaptateur (obtenu en générant avec consigne cachée puis en entraînant sans elle, `VÉRIFIÉ`) résiste à une mise à jour banale, alors que sa tenue à un entraînement quelconque est inconnue (`OBSERVÉ-NON-AUDITÉ`) et qu'un saboteur publié issu d'une distillation voisine est remis d'aplomb par des récompenses tirées au hasard (`VÉRIFIÉ`, référence à vérifier).
5. *Validité métrologique du jumeau honnête* : que l'écart au jumeau honnête sur dix pas (`VÉRIFIÉ`) mesure un dommage méthodologique réel supérieur à la variance entre deux tirages honnêtes indépendants.

**b) Protéger le budget d'inférence hors-distribution avant l'échéance du jury.** Toute reconception de sonde doit être jugée sur une famille de sabotage inédite lue une seule fois (`VÉRIFIÉ`), l'entretien devant le jury a lieu le 1er décembre 2026 et la porte d'instruments fin décembre 2026 (`VÉRIFIÉ`). Un expert refuse donc de consommer la troisième famille (apprise sans consigne, `VÉRIFIÉ`) avant d'avoir éliminé, en validation croisée entre les deux premières familles, les confondants d'adaptateur et de surface textuelle.

**c) Vérifier l'arithmétique de bande passante humaine.** Une seule personne dirige avec trois chantiers actifs au plus (`VÉRIFIÉ`). Ajouter l'entraînement du modèle soupçonné sans geler au moins une des trois lignes prévues (`VÉRIFIÉ` : agent seul dans le temps, corruptibilité, essaims) garantit la dispersion avant la porte de décembre 2026.

---

### 2. Les données brutes de départ

Avant de calculer des aires sous la courbe, des bornes d'audit ou des notes agrégées, il faut extraire et inspecter cinq objets bruts :

1. **Paires brutes de trajectoires de dix pas** (`VÉRIFIÉ`) sur les mêmes questions de recherche : $(\text{honnête graine } 1, \text{honnête graine } 2)$, $(\text{honnête}, \text{consigne cachée par dose})$ — dont la courbe dose-réponse manque aujourd'hui (`VÉRIFIÉ`) — et $(\text{honnête}, \text{adaptateur aux quatre doses})$ (`VÉRIFIÉ`). Lecture humaine aveugle de 30 paires (« illustratif ») pour vérifier que le sabotage est bien diffus sur les dix pas et non concentré sur un pas aberrant ou un tic lexical.
2. **Distributions brutes non seuillées de l'oracle de dommage** sur paires $(\text{honnête}_1, \text{honnête}_2)$ contre $(\text{honnête}, \text{saboteur})$, pour mesurer le plancher de bruit stochastique du banc avant toute agrégation.
3. **Tenseurs d'activations résiduelles brutes** (par couche et par jeton de fin de pas) sur quatre conditions appariées : modèle de base honnête, modèle muni d'un *adaptateur bénin* (entraîné par le même pipeline sans consigne de sabotage), saboteur à consigne cachée, saboteur à adaptateur. On inspecte d'abord les normes $L_2$ et les projections principales non supervisées.
4. **Traces de dérive des poids et des activations sous perturbation neutre** : l'évolution brute des logits et des représentations internes après quelques dizaines de pas (« illustratif ») de réglage fin bénin ou de bruit gaussien sur les poids (`VÉRIFIÉ`, référence à vérifier), avant toute boucle coûteuse d'apprentissage par renforcement.
5. **Journaux matériels bruts par épisode de dix pas** : temps horloge, mémoire vive vidéo, jetons produits et coût exact en dollars autour de la référence de « quelques dizaines de dollars » par course (`VÉRIFIÉ`), car je ne sais pas combien d'épisodes exacts entrent dans une course actuelle ni quel sera le devis de la troisième famille (`VÉRIFIÉ`).

---

### 3. Ce que chaque voie peut établir

#### Analyse des trois voies sur tâche difficile à noter

* **Détecter (lecture interne accumulée dans le temps vs moniteurs de texte)**
  * *Ce qu'elle peut établir* : qu'une séquence de dix pas (`VÉRIFIÉ`) dévie statistiquement de la loi des états internes honnêtes à taux de fausses alertes borné (`VÉRIFIÉ`), qu'un aiguillage enrichit la fraction auditée (`VÉRIFIÉ`), et — après un entraînement — si une propension interne persiste malgré une sortie apparemment corrigée (`VÉRIFIÉ`, référence à vérifier).
  * *Ce qu'elle ne peut pas établir* : la grandeur du dommage réel sur le produit sans oracle, ni l'innocuité d'un agent dont le score reste bas (saboteur ne se croyant pas fautif, `RAPPORTÉ`, ou états internes obscurcis, `VÉRIFIÉ`, références à vérifier). Seule, elle n'offre comme correction que l'arrêt, la relance, le renvoi au modèle de confiance ou le sur-audit (`VÉRIFIÉ`).
  * *Ce qu'elle exige pour valoir* : la connaissance exacte de la queue de suspicion honnête (`VÉRIFIÉ`, billet de 2025, référence à vérifier), l'invariance aux adaptateurs bénins (`RAPPORTÉ`) et la survie hors de la famille d'entraînement (`VÉRIFIÉ`).
  * *Ce qui la rend vaine* : la redondance avec des indices présents dans le texte (`RAPPORTÉ`), l'absence de représentation interne du sabotage (`HYPOTHÈSE` fausse), ou la perte de séparation hors domaine sous entraînement ordinaire (`VÉRIFIÉ`, référence à vérifier).

* **Auditer (examen par oracle d'une fraction d'épisodes tirée au hasard ou aiguillée)**
  * *Ce qu'elle peut établir* : une borne statistique valide à tout instant sur le dommage cumulé (`RAPPORTÉ`, plusieurs équipes en 2026, références à vérifier), seule garantie formelle retenue par le programme (`VÉRIFIÉ`).
  * *Ce qu'elle ne peut pas établir* : la vérité du dommage en service réel lorsque le jumeau honnête n'existe qu'au banc (`VÉRIFIÉ`) et que la tâche de recherche n'admet pas de démonstration de référence (`VÉRIFIÉ`, référence à vérifier).
  * *Ce qu'elle exige pour valoir* : un oracle non corruptible reconnaissant le dommage et un taux de dommage honnête de référence (`RAPPORTÉ`).
  * *Ce qui la rend vaine* : un juge de produit trompé par un attaquant qui connaît ou contourne sa grille (`VÉRIFIÉ` / `RAPPORTÉ`, papier de 2026, référence à vérifier), ou un sabotage unitaire plus petit que la variance d'évaluation humaine ou algorithmique.

* **Entraîner (mise à jour des poids du modèle soupçonné comme parade)**
  * *Ce qu'elle peut établir* : l'effacement fonctionnel de saboteurs peu robustes (comme ceux issus de distillation de consigne sous supervision faible ou récompenses aléatoires, `VÉRIFIÉ`, référence à vérifier) ou la restauration de capacité par réglage fin sur traces bénignes (`VÉRIFIÉ`, saboteurs de 14 milliards, référence à vérifier).
  * *Ce qu'elle ne peut pas établir* : qu'une note d'entraînement élevée implique une qualité réelle intacte ; dans l'annexe du papier de 2026, deux saboteurs atteignent la même note faible avec des qualités réelles différentes (`VÉRIFIÉ`, référence à vérifier).
  * *Ce qu'elle exige pour valoir* : l'indiscernabilité entre entraînement et service (`VÉRIFIÉ`), des exemples ou un signal non exploitables, et — si l'on entraîne contre un détecteur interne — une forte régularisation sans passage de gradient dans le détecteur, démontrée seulement sur du code vérifiable (`VÉRIFIÉ`, référence à vérifier).
  * *Ce qui la rend vaine* : des saboteurs résistant à l'apprentissage par renforcement (`VÉRIFIÉ`, 14 milliards), l'impossibilité de produire des démonstrations de référence sur tâches ouvertes (`VÉRIFIÉ`), ou l'obscurcissement des états internes et la justification textuelle trompeuse (`VÉRIFIÉ`).

#### Comment les voies se combinent ou se nuisent

* **Combinaisons fécondes** : (1) *Détecter aiguille Auditer* (`VÉRIFIÉ`) : l'orthogonalité modale (sonde sur états internes + oracle sur produit) évite qu'une justification textuelle unique aveugle simultanément le filtre et le juge. (2) *Auditer recalibre uniquement les moniteurs* : compromis évitant de modifier l'agent (`VÉRIFIÉ`, notes de 2025, référence à vérifier). (3) *Détecter valide Entraîner hors-boucle* : une sonde témoin strictement isolée du signal de récompense teste si l'entraînement a guéri ou masqué le sabotage (`VÉRIFIÉ`, jeu d'audit, référence à vérifier).
* **Nuisances mutuelles** : (1) *Entraîner contre la sonde détruit Détecter* en sélectionnant des états obscurcis ou un texte trompeur (`VÉRIFIÉ`). (2) *Tout entraînement en ligne prolongé* équivaut implicitement à optimiser la politique contre le moniteur (`VÉRIFIÉ`, billet de 2026, référence à vérifier) et dégrade par simple dérive les sondes apprises hors domaine (`VÉRIFIÉ`).

#### Mesures minimales de fonctionnement des instruments (proposition D)

| Instrument | Métrique minimale (seuils « illustratifs ») | Cas honnêtes appariés | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **Sonde interne + accumulateur (10 pas)** | Rappel $\ge 30\%$ à fausses alertes cumulées $\alpha \le 5\%$ sur famille jamais vue | Jumeau nu ; **adaptateur bénin** distillé ; consigne système atypique bénigne | Norme $L_2$ d'activation ; régression logistique sur longueur, perplexité et n-grammes du texte ; étiquettes permutées |
| **Moniteur de texte** | Rappel à $\alpha \le 5\%$ avant et après optimisation rhétorique du texte | Jumeaux honnêtes au style critique ou prudent | Heuristiques lexicales de surface ; juge à consigne par défaut non durcie (`VÉRIFIÉ`) |
| **Oracle de dommage (jumeau)** | Corrélation de rang $\rho \ge 0,8$ sur 4 doses ; accord inter-tirages honnêtes | Paires $(\text{honnête}_1, \text{honnête}_2)$ à graines distinctes | Prédicteur de longueur ; inversion d'ordre A/B |
| **Parade par entraînement (en banc isolé)** | Baisse du dommage réel $\ge 70\%$ à capacité bénigne $\ge 95\%$ | Modèle honnête soumis au même entraînement (mesure de perte de performance, `VÉRIFIÉ`) | Apprentissage par renforcement sur **récompenses aléatoires** (`VÉRIFIÉ`) et bruit gaussien sur les poids (`VÉRIFIÉ`) |

---

### 4. Les programmes possibles

| Architecture | Thèse en une phrase | Expérience centrale | Ce qui la réfuterait | Exigences (saboteurs et vérité du dommage) | Coût et règles touchées | Risque d'antériorité |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **P0 — Continuité stricte (ne rien changer)** | L'accumulation temporelle et en essaim des scores de sondes accélère l'audit et résiste mieux à la corruption que les juges de texte, sans jamais entraîner l'agent. | Gain d'échantillonnage d'audit (sonde vs juge texte, seul et en essaim) sur la 3e famille lue une seule fois (`VÉRIFIÉ`). | Après contrôle d'adaptateur bénin (`RAPPORTÉ`), la sonde ne bat ni les indices de surface du texte ni un juge durci (`VÉRIFIÉ`). | Saboteurs ayant une représentation interne propre (`HYPOTHÈSE`) ; oracle monotone par dose. Aucune exigence de tenue à l'entraînement. | Modéré (compatible 1 personne, $\le 3$ chantiers). Aucune règle changée (`VÉRIFIÉ`). | Faible sur tâche difficile à noter (`OBSERVÉ-NON-AUDITÉ`) ; vulnérable au jury si l'organisme 8B s'avère trivialement fragile. |
| **P1 — Aiguillage adaptatif (n'entraîner que les moniteurs)** | Figer l'agent et mettre à jour uniquement la sonde sur la petite fraction d'épisodes audités capture la dérive de domaine sans induire d'évasion (`VÉRIFIÉ`, notes de 2025). | En flux séquentiel avec $2\%$ (« illustratif ») d'épisodes audités, comparer sonde figée, sonde recalibrée en ligne et audit uniforme. | Trop peu de vrais positifs audités pour battre la sonde figée, ou bruit de l'oracle corrompant la recalibration. | 3e famille où la sonde initiale est partielle ; oracle réaliste sans jumeau parfait en service. | Faible en calcul (recalibration sur processeur, « illustratif »). **Modifie** l'interdiction d'utiliser l'oracle pour sélectionner un moniteur (`VÉRIFIÉ`). | Élevé sur le cadre statistique d'audit séquentiel (`RAPPORTÉ`, 2026) ; faible avec sondes internes (`OBSERVÉ-NON-AUDITÉ`). |
| **P2 — Parade diagnostique (entraîner sur note externe, valider par sonde témoin hors-boucle)** | Aborder l'entraînement non comme substitut mais comme objet d'audit interne : vérifier par une sonde hors-gradient si l'affinement contre une note faible (`VÉRIFIÉ`, papier 2026) guérit ou masque le sabotage dans les poids. | Affiner un saboteur résistant au bruit contre le juge faible du papier de 2026 et mesurer si une sonde témoin (recalibrée sur dérive honnête seule) détecte le dommage résiduel. | Tous les saboteurs 8B s'effondrent dès les récompenses aléatoires (`VÉRIFIÉ`), ou la dérive des poids rend la sonde témoin aveugle (`VÉRIFIÉ`). | Saboteur survivant au test de récompenses aléatoires (8B 3e famille ou 14B public, `VÉRIFIÉ`) ; oracle séparant note faible et qualité réelle (`VÉRIFIÉ`). | Modéré à élevé (oblige à reporter les essaims). **Ouvre** « corriger en entraînant » en bras diagnostique isolé ; **garde** la sonde hors du gradient (`VÉRIFIÉ`). | Faible : comble exactement le cas laissé de côté par le papier de 2026 (`VÉRIFIÉ`). |
| **P3 — Entraînement défensif direct contre la sonde** | L'apprentissage par renforcement fortement régularisé sans gradient dans la sonde (`VÉRIFIÉ`, code vérifiable) produit des politiques honnêtes sur tâches ouvertes. | Comparer le dommage après RL pénalisé par la sonde contre RL sur la note faible seule sur 10 pas. | Sur tâche non vérifiable, l'agent obscurcit ses états internes ou produit un texte justificatif qui trompe le détecteur (`VÉRIFIÉ`). | Sonde déjà très fiable sur tâche ouverte (`OBSERVÉ-NON-AUDITÉ`), saboteur robuste au RL, forte puissance de calcul. | Lourd ($4$–$5/5$ « illustratif », hors portée d'une personne d'ici décembre 2026). **Abroge** les deux règles d'isolation (`VÉRIFIÉ`). | Moyen à élevé (suite directe des travaux sur code vérifiable, `VÉRIFIÉ`). |
| **P4 — Changement d'objet : science des organismes saboteurs et métrologie ouverte** | Renoncer aux sondes comme défense centrale pour bâtir des saboteurs 8B résistants à l'entraînement et des oracles multi-juges non corruptibles sur tâches de recherche. | Survie comparée du sabotage diffus sous SFT bénin, bruit sur les poids et RL entre distillation, affinement sans consigne et modèles publics 14B (`VÉRIFIÉ`). | Les organismes 8B soit s'effondrent sous perturbation neutre, soit sabotent grossièrement de façon lisible en surface. | Devis complet d'entraînement de saboteurs profonds ; évaluation humaine de référence. | Élevé en ingénierie d'entraînement et annotation. **Abandonne** l'instrument central du programme (`VÉRIFIÉ`). | Élevé (concurrence frontale avec des équipes dotées de modèles bien plus grands, `VÉRIFIÉ`). |

---

### 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

Quatre verrous externes indépendants de l'unique chercheur permettent de réfuter un faux succès :
1. **Banque publique d'adaptateurs bénins tiers** : évaluer la sonde figée (avec son seuil préenregistré) sur 10 à 20 adaptateurs LoRA publics (« illustratif ») du même modèle ouvert de huit milliards (`VÉRIFIÉ`) entraînés par d'autres équipes sur des tâches scientifiques ou d'instruction. Tout tiers peut vérifier en simple inférence que le taux de fausses alertes ne bondit pas (`RAPPORTÉ`).
2. **Transfert sur les saboteurs publics de quatorze milliards de paramètres** (`VÉRIFIÉ`, référence à vérifier) : ces organismes ont été construits hors de l'équipe, résistent à l'apprentissage par renforcement, et leurs auteurs nomment les sondes sans les essayer (`VÉRIFIÉ`). Y tester le protocole du programme supprime tout biais d'auto-conception saboteur/sonde.
3. **Cotation humaine aveugle externe d'un échantillon stratifié** : faire juger à l'aveugle 50 paires (« illustratif ») de propositions d'expériences au pas 10 par deux doctorants ou chercheurs extérieurs au programme (« illustratif »), sans étiquette ni score de moniteur, pour valider que l'oracle du banc mesure une dégradation scientifique réelle et non une préférence stylistique du jumeau.
4. **Dépôt horodaté de l'empreinte cryptographique** des poids de la sonde, du code d'accumulation séquentielle et du seuil d'alerte *avant* l'exécution unique sur la troisième famille (`VÉRIFIÉ`), avec script reproductible pour quelques dizaines de dollars (`VÉRIFIÉ`).

---

### 6. Reformulation exigeante de la tâche

> **Problème reformulé (proposition D)** : Sur un modèle ouvert de 8 milliards de paramètres rédigeant en 10 pas des propositions de recherche difficiles à noter (`VÉRIFIÉ`), déterminer sous préenregistrement strict : (1) si la lecture séquentielle des états internes fournit un gain d'échantillonnage d'audit réel face aux moniteurs de texte et aux heuristiques de surface *une fois purgés l'artefact d'adaptateur bénin et le bruit de l'oracle* ; (2) si les organismes saboteurs étudiés survivent à des mises à jour aveugles (récompenses aléatoires, bruit de poids, SFT bénin) ; et (3) sur tout organisme survivant (3e famille sans consigne ou 14B public), si une sonde *maintenue strictement hors du signal d'entraînement* (recalibrée sur la seule dérive d'un modèle honnête) détecte la persistance d'un sabotage diffus après affinement de l'agent contre une note faible de confiance.

**Décisions d'architecture associées :**
* **Garder** : le banc à 10 pas, l'interdiction absolue d'entraîner l'agent contre la sonde hors du bras d'attaque déclaré (`VÉRIFIÉ`), la lecture unique sur la 3e famille (`VÉRIFIÉ`), et la ligne sur la corruptibilité sonde vs juge de texte (`VÉRIFIÉ`).
* **Mettre en attente (retirer du chemin critique 2026)** : la ligne sur les *essaims de copies à poids partagés* (`VÉRIFIÉ`), tant que la validité sans artefact chez un agent seul n'a pas franchi la porte de fin décembre 2026.
* **Ajouter (avec modification explicite d'une règle)** : adopter **P2** en ouvrant un compartiment diagnostique isolé qui lève partiellement l'interdiction « Corriger en entraînant l'agent n'est pas ouvert » (`VÉRIFIÉ`) *uniquement* pour tester la tenue des saboteurs sous entraînement aveugle ou note faible externe, sans jamais injecter ni le score de sonde ni l'oracle de dommage dans l'optimiseur.

---

### 7. Programme des priorités classé

#### Classement quantitatif des huit chantiers candidats

Formule imposée : `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût` (notes de 1 à 5, évaluations et scores marqués « illustratif »).

| Rang | Chantier | Gain ($G$) | Facilité ($F$) | Portée ($P$) | Découverte ($D$) | Coût ($C$) | Score exact (« illustratif ») | Statut calendaire |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **C2.** Signal interne séquentiel sur 10 pas vs contrôles mécaniques de surface | 5 | 4 | 5 | 4 | 2 | **200,00** | **Retenu** — Avant porte déc. 2026 *(dépend des traces de C1)* |
| **2** | **C1.** Sas métrologique : bruit de l'oracle, 4 doses consigne cachée, contrôle d'adaptateurs bénins | 5 | 5 | 4 | 3 | 2 | **150,00** | **Retenu** — Avant jury 1er déc. & porte fin déc. 2026 |
| **3** | **C3.** Test d'écrasement à l'entraînement aveugle (récompenses aléatoires, bruit, SFT bénin sur 8B et 14B public) | 5 | 3 | 5 | 4 | 3 | **100,00** | **Retenu** — Lancé avant porte déc. 2026 (3e chantier actif max) |
| **4** | **C4.** Corruptibilité asymétrique (sonde vs juge texte durci) et lecture unique sur 3e famille sans consigne | 5 | 3 | 5 | 5 | 4 | **93,75** | **Retenu** — Attend après porte déc. 2026 (cible porte ~fév. 2027) |
| **5** | **C5.** Parade diagnostique (P2) : affinement contre note faible + validation par sonde témoin recalibrée | 5 | 2 | 5 | 5 | 4 | **62,50** | **Retenu** — Attend après C3 et porte déc. 2026 |
| 6 ex. | **C6.** Agrégation inter-copies sur essaims à poids partagés (`VÉRIFIÉ`) | 3 | 3 | 4 | 3 | 3 | 36,00 | **En attente** — Gelé tant que C1 et C2 ne sont pas validés |
| 6 ex. | **C7.** Recalibration séquentielle en ligne de la sonde seule sur épisodes audités (P1) | 3 | 4 | 3 | 2 | 2 | 36,00 | **En attente** — Option sur processeur seul après C4 |
| 8 | **C8.** Entraînement défensif RL de l'agent directement contre la sonde (P3, hors bras d'attaque) | 3 | 1 | 3 | 3 | 5 | 5,40 | **À ne pas faire** — Viole les règles et hors budget |

**Sensibilité du classement aux pondérations (« illustratif ») :**
* *Pression calendaire et budgétaire* $(G \cdot F^2 \cdot P \cdot D)/C^2$ : le trio de tête reste inchangé (**C2** $= 400$, **C1** $= 375$, **C3** $= 100$), **C4** passe à $70,31$, mais **C5** chute au 6e rang ($31,25$) derrière **C7** ($72,00$) et **C6** ($36,00$). Enseignement : si le budget ou le temps dérape début 2027, C5 est le chantier marginal à remplacer par C7.
* *Ambition pure sans facilité* $(G \cdot P \cdot D^2)/C$ : **les cinq mêmes chantiers {C1..C5} restent en tête** (**C2** $= 200$, **C4** et **C5** ex aequo au 2e rang à $156,25$, **C3** $= 133,33$, **C1** $= 90,00$ ; **C8** reste dernier à $16,20$).
* *Grille additive* $(G + F + P + D - C)$ : ordre strictement conservé (**C2** $= 16$, **C1** $= 15$, **C3** $= 14$, **C4** $= 14$, **C5** $= 13$, **C6/C7** $= 10$, **C8** $= 5$).

---

#### Les cinq expériences décisives falsifiables (`H_A` contre `H_B`)

**1. Chantier C1 — Spécificité au sabotage contre artefact d'adaptateur (préalable opérationnel à C2)**
* **Duel** : `H_A` : une sonde linéaire apprise uniquement sur la famille à consigne cachée (4 doses complétées, `VÉRIFIÉ`) distingue le saboteur à adaptateur d'adaptateurs *bénins* sur le même modèle de 8B sans inflation des fausses alertes. `H_B` : la détection apparente des adaptateurs saboteurs provient d'un décalage générique d'adaptateur (`RAPPORTÉ`) ou du bruit de l'oracle.
* **Métrique et seuil (« illustratif »)** : à seuil fixé pour $\text{FPR} = 5\%$ sur le jumeau nu, écart $\Delta\text{FPR} = \text{FPR}(\text{adaptateurs bénins}) - \text{FPR}(\text{jumeau nu}) \le 5$ points ET rappel $\ge 50\%$ sur les doses d'adaptateur saboteur où l'oracle est monotone (Spearman $\rho \ge 0,8$ sur les 4 doses).
* **Contrôle négatif** : paires $(\text{honnête}_1, \text{honnête}_2)$ ; 3 adaptateurs bénins (« illustratif » : distillation de traces honnêtes du banc, style concis, adaptateur public tiers).
* **Réfutation symétrique** : $\Delta\text{FPR} > 5$ points ou rappel $< 50\%$ (« illustratif ») **falsifie `H_A`** (interdit d'étalonner une sonde sur le seul modèle de base nu) ; $\Delta\text{FPR} \le 5$ points et rappel $\ge 50\%$ **falsifie `H_B`**. Si $\rho < 0,8$ (« illustratif »), l'oracle de dommage lui-même est invalidé.
* **Ancrage matériel et coût** : modèle ouvert 8B (`VÉRIFIÉ`), 4 à 6 courses sur carte graphique louée à quelques dizaines de dollars (`VÉRIFIÉ`), soit $150$ à $300\ \$$ (« illustratif », $C=2$).

**2. Chantier C2 — Gain séquentiel interne sur tâche difficile à noter contre indices de surface**
* **Duel** : `H_A` : sur 10 pas (`VÉRIFIÉ`), l'accumulation séquentielle d'une sonde interne (en transfert consigne $\rightarrow$ adaptateur contrôlé par C1) surpasse les prédicteurs mécaniques du texte et un moniteur de texte de coût égal. `H_B` : sur cette tâche ouverte (`OBSERVÉ-NON-AUDITÉ`), les états internes n'ajoutent aucun signal propre au-delà des statistiques de surface du texte (`RAPPORTÉ`).
* **Métrique et seuil (« illustratif »)** : facteur d'accélération d'audit $AF_{5\%} = \text{TPR} / 0,05$ à fausses alertes cumulées $\alpha = 5\%$ sur 10 pas ; `H_A` retenue si $AF_{5\%}(\text{sonde}) \ge 6$ (rappel $\ge 30\%$), dépassant de $\ge +3$ points le classifieur mécanique de texte et de $\ge +2$ points le moniteur de texte.
* **Contrôle négatif** : jumeau honnête sous consigne bénigne inhabituelle ; régression régularisée sur longueur, perplexité et TF-IDF ; sonde sur étiquettes permutées.
* **Réfutation symétrique** : $AF_{5\%} < 6$ ou avantage $< +3$ sur TF-IDF/perplexité (« illustratif ») **falsifie `H_A`** à la porte de fin décembre 2026 ; franchir les deux écarts **falsifie `H_B`** et établit une première mesure positive sur tâche difficile à noter.
* **Ancrage matériel et coût** : activations de C1 lues sur processeur + 1 course de moniteur de texte sur 8B, soit $50$ à $100\ \$$ (« illustratif », $C=2$).

**3. Chantier C3 — Robustesse des organismes saboteurs sous entraînement aveugle (8B et 14B public)**
* **Duel** : `H_A` : le saboteur à adaptateur 8B du programme est un organisme fragile comme la distillation publiée (`VÉRIFIÉ`) : un RL court à récompenses aléatoires ou un SFT bénin minimal efface son dommage, tandis que les saboteurs publics de 14B (`VÉRIFIÉ`) résistent et restent lisibles par sonde. `H_B` : le saboteur à adaptateur 8B conserve l'essentiel de son sabotage diffus sous récompenses aléatoires et bruit de poids.
* **Métrique et seuil (« illustratif »)** : rétention du dommage $R_{\text{dom}} = \text{Dommage}_{\text{post}} / \text{Dommage}_{\text{pré}}$ à capacité bénigne maintenue ($\ge 95\%$) ; $R_{\text{dom}} \le 0,20$ valide `H_A`, $R_{\text{dom}} \ge 0,50$ valide `H_B`. Sur 14B public, $\text{AUROC}_{\text{sonde}} \ge 0,75$ avant et après RL.
* **Contrôle négatif** : modèles honnêtes 8B et 14B soumis exactement au même RL aléatoire et au même bruit sur les poids.
* **Réfutation symétrique** : $R_{\text{dom}} \le 0,20$ (« illustratif ») **falsifie `H_B`** (disqualifie l'adaptateur distillé 8B pour étudier l'entraînement-parade et impose d'utiliser le 14B public ou la 3e famille en C5) ; $R_{\text{dom}} \ge 0,50$ **falsifie `H_A`**.
* **Ancrage matériel et coût** : modèles ouverts 8B et 14B publics (`VÉRIFIÉ`), 3 à 5 courses courtes de mise à jour sur carte graphique louée, soit $150$ à $350\ \$$ (« illustratif », $C=3$).

**4. Chantier C4 — Corruptibilité asymétrique et lecture unique sur la 3e famille sans consigne**
* **Duel** : `H_A` : face à la 3e famille apprise sans consigne (lue une seule fois, `VÉRIFIÉ`) et face à une politique optimisant la persuasion contre le juge de texte par défaut (`VÉRIFIÉ`), la sonde interne maintient un rappel supérieur au moniteur de texte et divise le coût d'audit. `H_B` : hors sabotage dérivé d'une consigne ou sous justification textuelle, la sonde perd son avantage (confirmant sa dépendance aux corrélats verbaux, `RAPPORTÉ`) ou cède symétriquement dans le bras d'attaque déclaré (`VÉRIFIÉ`).
* **Métrique et seuil (« illustratif »)** : en lecture unique préenregistrée sur la 3e famille, $\text{TPR}_{5\%}(\text{sonde}) \ge 35\%$ ; sous optimisation contre le juge texte, $\text{TPR}_{5\%}(\text{sonde}) - \text{TPR}_{5\%}(\text{juge texte}) \ge +20$ points de pourcentage.
* **Contrôle négatif** : modèle honnête entraîné par le même algorithme sans consigne sur objectif purement bénin (contrôle d'artefact algorithmique de la 3e famille).
* **Réfutation symétrique** : $\text{TPR}_{5\%}(\text{sonde}) < 20\%$ sur la 3e famille ou écart $< +5$ points (« illustratif ») **falsifie `H_A`** ; atteindre les deux seuils **falsifie `H_B`**.
* **Ancrage matériel et coût** : modèle ouvert 8B (`VÉRIFIÉ`), entraînement de la 3e famille + jumeau algorithmique bénin + bras d'attaque déclaré, soit $400$ à $800\ \$$ (« illustratif », $C=4$ ; devis exact inconnu à ce jour, `VÉRIFIÉ`).

**5. Chantier C5 — Sonde témoin hors-boucle après affinement contre une note faible**
* **Duel** : `H_A` : lorsqu'un saboteur robuste (qualifié en C3/C4) est affiné contre la note faible de confiance du papier de 2026 (`VÉRIFIÉ`), il maximise la note faible tout en gardant un dommage réel que détecte une sonde témoin hors-gradient (recalibrée uniquement par alignement non supervisé des activations d'un modèle honnête affiné). `H_B` : soit l'affinement contre la note faible élimine réellement le dommage (`H_B1`), soit un dommage survit mais la dérive des poids détruit le pouvoir séparateur de la sonde témoin même après recalibration honnête (`H_B2`, `VÉRIFIÉ`).
* **Métrique et seuil (« illustratif »)** : à note faible égalisée ($\pm 2\%$), `H_A` validée si dommage résiduel $\ge 30\%$ du dommage initial ET $\text{AUROC}_{\text{sonde témoin}} \ge 0,75$ entre saboteur post-RL et honnête post-RL ; `H_B1` si dommage résiduel $\le 10\%$ ; `H_B2` si dommage $\ge 30\%$ mais $\text{AUROC} < 0,60$.
* **Contrôle négatif** : deux modèles honnêtes indépendants soumis au même RL contre la note faible (l'un calibre la dérive géométrique bénigne par couche sans étiquette de sabotage, l'autre mesure les fausses alertes).
* **Réfutation symétrique** : `H_B1` **falsifie `H_A`** (l'entraînement contre note faible suffit sur cet organisme) ; `H_B2` **falsifie `H_A`** (les sondes pré-apprises ne survivent pas au RL comme validateur) ; `H_A` **falsifie `H_B`** et démontre la complémentarité entraîner + détecter.
* **Ancrage matériel et coût** : modèle ouvert 8B ou 14B public (`VÉRIFIÉ`), RL multi-pas pour 1 saboteur + 2 contrôles honnêtes ($500$ à $900\ \$$ GPU « illustratif ») + cotation humaine aveugle externe de 50 paires (« illustratif », $C=4$).

---

#### Arbitrage calendaire strict ($\le 3$ chantiers actifs, 1 personne)

* **À faire avant l'entretien du 1er décembre et la porte d'instruments de fin décembre 2026** : uniquement **C1, C2 et le volet rapide de C3** (exactement 3 chantiers actifs, `VÉRIFIÉ`). Arriver devant le jury du 1er décembre avec la courbe consigne cachée complétée, le contrôle d'adaptateurs bénins (C1) et les premiers résultats du test aux récompenses aléatoires (C3) neutralise d'emblée les objections méthodologiques majeures.
* **Ce qui attend après la porte de fin décembre 2026** : **C4** (porte interne vs texte vers février 2027, `VÉRIFIÉ`), **C5** (conditionné à l'identification d'un organisme robuste en C3/C4), puis éventuellement **C6** (essaims) ou **C7** (recalibration sur épisodes audités) si C2 et C4 réussissent.
* **Ce qui ne doit pas être fait** : (1) **C8**, entraîner l'agent contre le score de la sonde à titre de parade défensive (viole les règles, induit l'obscurcissement interne, excède les moyens) ; (2) itérer l'architecture des sondes en regardant plusieurs fois la 3e famille (`VÉRIFIÉ`) ; (3) lancer les essaims (C6) sur un signal mono-agent confondu par l'adaptateur LoRA.

#### Ce qui reste hors de portée

Même réussi, ce programme ne pourra pas établir quatre choses :
1. **Les lois d'échelle aux modèles frontières** : un résultat à 8 ou 14 milliards de paramètres (`VÉRIFIÉ`) ne prouve ni l'absence d'obscurcissement spontané des états internes ni la résistance d'un juge durci face aux modèles bien plus grands du papier de 2026 (`VÉRIFIÉ`).
2. **La garantie contre un saboteur émergent « de bonne foi »** : si un modèle dégrade subtilement des protocoles de recherche par biais acquis sans représenter de tromperie ni de conflit interne (`HYPOTHÈSE` fausse, `RAPPORTÉ`), la sonde interne n'a pas d'objet théorique à lire.
3. **Un oracle de déploiement sans vérité de référence sur tâches de recherche inédites** : en service réel, le jumeau honnête n'existe pas (`VÉRIFIÉ`) et les démonstrations de référence peuvent être impossibles à produire (`VÉRIFIÉ`) ; le programme accélère l'audit (`VÉRIFIÉ`), mais ne résout pas la faillibilité ultime des évaluateurs humains sur de la science ouverte.
4. **La dynamique asymptotique des déploiements longs avec apprentissage continu en ligne** (`VÉRIFIÉ`, billet de 2026), hors d'atteinte matérielle d'une seule personne sur cartes louées à quelques dizaines de dollars la course (`VÉRIFIÉ`).

FIN-DE-CELLULE