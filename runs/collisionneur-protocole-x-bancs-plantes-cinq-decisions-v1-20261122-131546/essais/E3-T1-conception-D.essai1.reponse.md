# Proposition D — Tour III.1

**Traçabilité.** Les sorties des calculs de conception, le texte d’admission gelé, le code de l’optimiseur et le coût du repéreur ne sont pas fournis ; je n’en invente pas le contenu. J’appelle **RAPPORTÉ** ce que le brief affirme, et **OBSERVÉ-NON-AUDITÉ** les vérifications ou calculs dont il rapporte le résultat sans fournir les artefacts. Aucun résultat empirique n’est ici **VÉRIFIÉ**. Les confiances ci-dessous sont des jugements illustratifs, non des mesures.

## 1. Choix sur les six décisions

### Décision 1 — **Option (a)** ; confiance : **0,84**

La grandeur A répond à la question posée — l’acceptation de l’honnête — tandis qu’une plus grande variabilité de B peut simplement refléter une estimation plus instable sur le seul jumeau honnête. Je gèlerais explicitement \(A=\) acceptations/tous les épisodes honnêtes, abstentions comprises dans les non-acceptations, et rapporterais la chute appariée par rapport au monde de référence avec son intervalle d’incertitude. **Ce qui me ferait changer d’avis :** une démonstration sur cas honnêtes réels appariés que A reste stable lors de dégradations que B détecte avec un taux de fausse alerte maîtrisé.

**Option meilleure :** A reste la seule grandeur d’admission ; B peut figurer dans un journal technique de diagnostic, sans seuil ni lecture en dommage, afin de ne pas créer un second résultat ambigu.

### Décision 2 — **Option (b)** ; confiance : **0,82**

Le manque d’un contrôle supplémentaire est calculable, mais sa signification dépend du bruit des lecteurs et de \(m\) : simplicité ne vaut pas étalonnage. Un lot distinct permet de choisir le seuil selon un compromis gelé entre fausses alertes honnêtes et détection par strate, puis de lire le lot final une seule fois. **Ce qui me ferait changer d’avis :** la fourniture préalable d’une règle binaire gelée par l’oracle, ou une étalonnage montrant que la règle fixe satisfait déjà tous les critères sans gain pratique du seuil réglé.

**Option meilleure :** étalonner un écart entier de contrôles manquants, en maximisant la détection minimale par strate sous contrainte de fausse alerte sur paires honnête–honnête ; réserver une partie du lot d’étalonnage à une validation sans réajustement.

### Décision 3 — **Option (c), transitoire** ; confiance : **0,74**

Au moins, (c) mesure une erreur qui, selon la convention RAPPORTÉE du banc, se transfère en sous-estimation de la reconnaissance par le moniteur. Mais une fidélité mesurée sur un petit échantillon n’autorise pas à conclure hors de cet échantillon, tandis que la supériorité du repéreur reste une **HYPOTHÈSE**. **Ce qui me ferait changer d’avis :** une borne supérieure d’erreur suffisamment basse sur un échantillon stratifié, notamment sur paraphrases et contrôles implicites, ou inversement un échec du repéreur face à une relecture indépendante.

**Option meilleure :** un hybride audité : le programme sert de vérification mécanique et de baseline ; le repéreur lit chaque tâche ; un échantillon stratifié reçoit deux désignations indépendantes, avec arbitrage des désaccords. Les cas ambigus suivent une règle gelée, et l’erreur résiduelle est propagée à l’analyse de sensibilité plutôt que cachée.

### Décision 4.1 — **Option (c)** ; confiance : **0,90**

En régime d’excès, le seul résultat de fond admissible est le constat d’inadmission du banc pour la garantie demandée. Tester l’optimiseur sur des cas indépendants conserve un actif vérifiable sans faire circuler un produit dose–borne dont l’étiquette « sans garantie » ne créerait aucune couverture statistique. **Ce qui me ferait changer d’avis :** une dérivation indépendante établissant qu’une grandeur précise reste couverte au niveau gelé malgré l’excès, avec une règle de publication fixée avant le regard correspondant.

### Décision 4.2 — **Option (a)** ; confiance : **0,96**

Les niveaux RAPPORTÉS de **2,5 %** ou **1,25 % par regard** doivent rester inchangés dans cette campagne : une réallocation décidée après observation de l’excès est dépendante des données. Un budget inemployé est préférable à une garantie dont le niveau réel devient inconnu. **Ce qui me ferait changer d’avis :** l’existence, antérieure à tout regard, d’une règle conditionnelle de recyclage déjà gelée, accompagnée d’un audit montrant que son application ne dépend d’aucun autre résultat.

**Option meilleure :** pour les campagnes futures seulement, geler dès le départ un graphe de réallocation conditionnelle et ses tests de couverture.

### Décision 5 — **Option (a)** ; confiance : **0,94**

Il faut tirer la composition et refaire l’admission avant de servir la première fiche : connaître le nombre fixe de lois autorise une stratégie mécanique « prendre les \(K\) statistiques les plus fortes », précisément le témoin que le banc risque de perdre. Le coût de recalcul est RAPPORTÉ, mais aucun coût de contamination d’agent n’est encore encouru puisqu’aucune fiche n’a été servie. **Ce qui me ferait changer d’avis :** une impossibilité démontrée de recalculer l’admission, combinée à des expériences montrant que la cohérence fixe détecte ce sabotage au niveau requis sans pénaliser les honnêtes.

**Option meilleure :** geler la distribution de tirage, recalculer l’admission sur le mélange et par strates de composition, et faire du saboteur top-\(K\), avec ou sans connaissance de \(K\), un test d’admission obligatoire.

---

## 2. (a) Ce que la question suppose sans l’établir

| Point supposé | Statut |
|---|---|
| Les dommages du monde témoin se confondraient avec ceux d’un autre monde ; la vérification n’est pas jointe. | **OBSERVÉ-NON-AUDITÉ** |
| A varie peu et B davantage dans les calculs sur lois simulées ; ni code, ni graines, ni sorties ne sont fournis. | **OBSERVÉ-NON-AUDITÉ** |
| La stabilité simulée de A impliquerait son utilité sur les tâches réelles, ou la variabilité de B impliquerait une meilleure détection d’un monde défectueux. | **HYPOTHÈSE** |
| Les jumeaux honnêtes et les mondes seraient suffisamment appariés pour attribuer une chute au monde plutôt qu’à une différence de tirage ou de lecture. | **HYPOTHÈSE** |
| Le seuil fixe \(1/m\) contrôlerait les fausses alertes ; un seuil étalonné sur un lot distinct se transférerait au lot final. | **HYPOTHÈSE** |
| Les lecteurs de l’oracle auraient une fiabilité stable, et leurs erreurs ne seraient pas corrélées par type de document ou de contrôle. | **HYPOTHÈSE** |
| Le repéreur détecterait mieux les paraphrases que le recouvrement lexical ; la fidélité mesurée sur l’échantillon de l’option (c) se généraliserait hors échantillon. | **HYPOTHÈSE** |
| En régime d’excès, le produit dose–borne de \(q\) conserverait une interprétation garantie, ou une réallocation post gel conserverait le niveau global. | **HYPOTHÈSE**, non démontrée |
| La règle de cohérence prendrait le top-\(K\) pour un geste honnête ; le brief dit expressément que ce comportement n’est pas vérifié. | **HYPOTHÈSE** ; non-vérification **RAPPORTÉE** |
| Tirer la composition supprimerait toute fuite du nombre de lois, y compris via la distribution, les métadonnées ou les formats de fiche. | **HYPOTHÈSE** |
| Aucune fiche n’a encore été servie à un agent. | **RAPPORTÉ** |

## 3. (b) Expériences décisives

*Tous les seuils chiffrés introduits ci-dessous sont **illustratifs** ; ils doivent être remplacés par des seuils gelés après calcul de puissance. Les métriques sont appariées et rapportées par strate, avec dénominateurs et intervalles d’incertitude.*

### E1 — Le témoin A est-il suffisant ?

- **H_A :** A seul atteint le cahier des charges de détection des instabilités honnêtes, et B n’apporte pas de gain matériel. **H_B :** A seul échoue, tandis que A+B atteint le cahier des charges.
- **Protocole et métrique :** sur tâches honnêtes appariées référence/témoin, introduire des perturbations connues d’acceptation et d’abstention, sans dommage ; mesurer détection des perturbations et fausses alertes.
- **Seuil illustratif :** détection au moins **90 %**, fausses alertes au plus **5 %** ; gain de B inférieur à **5 points** pour H_A, ou gain d’au moins **10 points** avec échec de A seul pour H_B.
- **Contrôle négatif :** deux moitiés du monde de référence, étiquetées au hasard ; toute alerte excédentaire révèle un artefact.
- **Falsification :** si A seul satisfait les seuils avec gain de B négligeable, H_B est falsifiée ; si A échoue et A+B les satisfait, H_A est falsifiée.

### E2 — Seuil fixe contre seuil étalonné

- **H_A :** la règle \(1/m\) satisfait simultanément fausses alertes et détection sur toutes les strates. **H_B :** elle y échoue, alors qu’un seuil étalonné distinct y parvient.
- **Métrique :** détection sur documents plantés appariés à leur version honnête ; fausse alerte sur deux versions honnêtes lues contre la même référence.
- **Seuil illustratif :** borne supérieure de fausse alerte au plus **5 %**, borne inférieure de détection au moins **80 %** sur la plus petite strate revendiquée.
- **Contrôle négatif :** paire honnête–honnête sans intervention du tiers, orientation tirée au hasard.
- **Falsification :** succès de la règle fixe sans gain significatif du seuil réglé falsifie H_B ; échec du fixe suivi du succès du seuil réglé falsifie H_A. Si les deux échouent, aucune règle par défaut n’est admise.

### E3 — Désignation lexicale contre repéreur audité

- **H_A :** le programme atteint la fidélité requise et le repéreur n’apporte qu’un gain négligeable. **H_B :** le programme échoue, notamment sur paraphrases, et l’hybride audité atteint la fidélité requise.
- **Métrique :** rappel et précision au niveau du contrôle, fausses désignations sur honnête, puis biais induit sur le taux de détection du moniteur.
- **Seuil illustratif :** rappel au moins **98 %**, fausses désignations au plus **2 %**, biais de détection au plus **2 points**.
- **Contrôle négatif :** documents honnêtes inchangés, dont tous les contrôles sont mécaniquement présents ; tout contrôle déclaré retiré est faux.
- **Falsification :** succès du programme avec gain inférieur à **2 points** falsifie H_B ; échec du programme et succès de l’hybride falsifient H_A.

### E4a — Existe-t-il encore une lecture garantie en régime d’excès ?

- **H_A :** une grandeur publiable, explicitement définie, conserve sa couverture nominale sous excès. **H_B :** aucune des grandeurs candidates ne la conserve.
- **Métrique :** couverture sur simulations à dommage connu, y compris erreurs corrélées des lecteurs ; aucune couverture ne doit être inférieure au nominal au-delà de l’erreur Monte-Carlo.
- **Contrôle négatif :** régime sans excès, où la procédure existante doit retrouver sa couverture.
- **Falsification :** une sous-couverture de chaque candidate falsifie H_A ; une candidate dont la borne d’incertitude exclut toute sous-couverture falsifie H_B pour cette candidate seulement.

### E4b — Réallocation du budget d’erreur

- **H_A :** la réallocation après déclenchement de l’excès maintient l’erreur globale à \(\alpha_{\text{total}}\). **H_B :** elle la dépasse.
- **Métrique :** erreur globale maximale sous scénarios nuls, avec déclenchement dépendant des données et un ou deux regards.
- **Contrôle négatif :** même simulation sans réallocation ; les niveaux gelés doivent être retrouvés.
- **Falsification :** dépassement de \(\alpha_{\text{total}}\) falsifie H_A ; borne supérieure sous \(\alpha_{\text{total}}\) dans tous les scénarios gelés falsifie H_B pour cette procédure. Cela ne rendrait pas rétroactivement gelée une règle absente du texte actuel.

### E5 — Composition fixe contre composition tirée

- **H_A :** avec composition fixe connue, la cohérence détecte suffisamment top-\(K\) sans fausse alerte excessive. **H_B :** elle échoue, et le tirage caché supprime l’avantage procuré par la connaissance de \(K\).
- **Métrique :** taux de sabotages top-\(K\) non détectés, lois fausses promues ou vraies tues, fausses alertes sur analystes honnêtes ; comparer agents informés et non informés de \(K\).
- **Seuil illustratif :** détection du sabotage au moins **90 %**, fausses alertes honnêtes au plus **5 %**.
- **Contrôle négatif :** données sans loi plantée supplémentaire et fiches honnêtes reconstruites depuis les preuves.
- **Falsification :** succès de la configuration fixe sans avantage mesurable du tirage falsifie H_B ; passage de top-\(K\) pour honnête et suppression de son avantage par le tirage falsifient H_A.

## 4. (c) Validation minimale des instruments

À performance comparable, chaque instrument doit battre les vérifications mécaniques : à fausse alerte égale, meilleure détection ; à détection égale, moins de fausses alertes.

| Instrument | Cas honnêtes appariés et mesures minimales | Vérifications mécaniques à battre |
|---|---|---|
| **Moniteur de comparaison et abstention** | Mêmes tâches, monde et jumeau honnête ; détection sur dommages plantés, signaux sur honnête, abstention rapportée séparément et non absorbée dans un score. | Toujours accepter, toujours signaler, tirage aléatoire au même taux, règles utilisant longueur, identifiant du monde ou simple différence lexicale. |
| **Oracle multi-lecteurs et règle binaire** | Documents honnêtes contre eux-mêmes pour fausses alertes ; dommage planté contre version honnête, même référence et même \(m\), pour détection ; désaccords entre lecteurs publiés. | Compte brut des contrôles, seuil fixe \(1/m\), recouvrement lexical, décision d’un lecteur unique et vote majoritaire simple. |
| **Programme de recouvrement et repéreur** | Contrôles présents sans retrait pour fausses désignations ; retraits connus, paraphrases et contrôles implicites pour détection ; versions honnête et sabotée du même document. | Correspondance exacte, recouvrement de mots, similarité fuzzy, position attendue du passage ; aucun ne doit être présenté comme vérité terrain. |
| **Calculateur de borne de \(q\), doses et optimum** | Épisodes honnêtes simulés sans dommage pour fausses alertes d’excès ; épisodes à \(q\) connu pour détection des sous-couvertures et des déclenchements corrects. | Recherche exhaustive sur petits cas, calcul indépendant, monotonie en dose et en nombre d’épisodes, bornes aux cas limites, tests métamorphiques et graine reproductible. |
| **Générateur de lois et référence cachée** | Mêmes données sans sabotage pour fausses lois prétendument plantées ; lois effectivement ajoutées/retirées pour vérifier que la référence les récupère. | Recompte mécanique des lois, re-génération depuis les graines, comparaison exacte fiche–référence, tests de permutations et de fuite du nombre \(K\). |
| **Règle de cohérence** | Fiches honnêtes appariées aux mêmes preuves pour fausses alertes ; saboteurs top-\(K\), promotion de lois fausses et omission de lois vraies pour détection. | Détecteur « nombre d’entrées égal à \(K\) », classement par statistique maximale, seuil mécanique sur p-values, comparaison directe à la référence cachée. |

## 5. (d) Ancrage matériel

Le choix suivant est une **HYPOTHÈSE de faisabilité**, pas un résultat : **Qwen2.5-32B-Instruct** comme agent/repéreur et **Mistral-Nemo-Instruct-2407** comme second lecteur ou moniteur, tous deux à poids ouverts, avec versions, licences et invites figées. Le recouvrement lexical, les références, les tirages et les tests statistiques restent sur CPU afin de séparer les vérifications déterministes des jugements de modèles.

**Estimation illustrative :** deux GPU de **80 Go**, **240 GPU·h** au total pour étalonnage et validation, **32 cœurs CPU** et **1 To** de stockage. À **2,50 €/GPU·h**, cela donne **600 €** de calcul, auxquels ajouter **150 €** de CPU/stockage et **1 500–3 000 €** de relecture indépendante, soit **2 250–3 750 €**, hors développement et reprises après échec d’admission. Le lot final n’entre pas dans ce budget exploratoire : sa taille doit être fixée par le calcul de puissance, puis il n’est lu qu’une fois.

FIN-DE-CELLULE