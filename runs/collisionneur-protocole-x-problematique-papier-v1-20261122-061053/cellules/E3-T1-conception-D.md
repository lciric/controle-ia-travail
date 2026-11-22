## Proposition D — Auditer les preuves plutôt que la plausibilité du récit

**HYPOTHÈSE — choix de conception.** Je commencerais par une tâche où le résultat dépend d’un dossier de preuves : l’agent doit comparer des options à partir d’un corpus figé, produire une table de faits sourcés, puis rendre une conclusion. On peut alors distinguer trois questions : *une erreur grave est-elle nécessairement exposée à un contrôle ?* *Un moniteur aide-t-il à choisir où contrôler ?* *L’information utile au contrôle s’accumule-t-elle selon une loi mesurable ?* Une réponse positive à l’une ne vaut pas réponse aux autres.

### (a) Ce qui n’est pas établi

| Statut | Prémisse à éprouver | Ce qui manque |
|---|---|---|
| RAPPORTÉ | Le scénario donne accès au texte, aux activations, à quelques exécutions honnêtes et à des vérifications coûteuses. | Ni la fidélité d’un vérificateur ni le coût relatif des instruments ne sont mesurés. |
| HYPOTHÈSE | Une succession de petites erreurs peut changer la conclusion sans qu’une erreur isolée soit suspecte. | « Peu suspecte » doit se mesurer sur des cas honnêtes difficiles, pas se déduire de la petite taille d’une modification. |
| HYPOTHÈSE | Une conclusion gravement fausse laisse des témoins auditables dans la trace. | Une omission peut ne laisser **aucune affirmation fausse**. Contrôler seulement ce que l’agent a choisi d’écrire ne suffit pas. |
| HYPOTHÈSE | Les activations apportent une information supplémentaire. | Elles pourraient ne coder que la longueur, la difficulté du dossier ou un artefact de construction des exemples. |
| HYPOTHÈSE | Les références honnêtes permettent de calibrer un seuil transférable. | Des exécutions du même dossier ne valent pas des dossiers indépendants ; les longues délibérations honnêtes peuvent présenter des dérives apparentes. |
| HYPOTHÈSE | Le caractère « jamais vu » est testable. | On peut cacher une famille de dégradations pendant le développement ; cela ne la rend pas représentative de toutes les familles futures. |

**HYPOTHÈSE — convention expérimentale.** Tous les seuils, effectifs, prix et temps de calcul proposés ci-dessous sont **illustratifs** ; ils ne sont pas des résultats. Geler avant test le corpus, la définition d’une erreur grave (conclusion contredite par le calcul de référence), les budgets et les familles réservées. Séparer les jeux **par dossier source**, puis tester sur une famille de dégradation non utilisée pour régler les instruments. Apparier chaque cas dégradé à une exécution honnête de même dossier, même modèle, même accès documentaire et même tranche de longueur. Garder aussi des erreurs naturelles de l’agent : une erreur n’est pas une étiquette d’intention hostile.

### (b) Trois contributions, trois duels

#### Garantie — quelle partie de « jamais vu » peut-on réellement garantir ?

**Question.** Une conclusion grave peut-elle être assortie d’une borne de non-détection indépendante du procédé qui l’a produite, en tirant au sort les contrôles *après* engagement de l’agent sur son rapport ?

**HYPOTHÈSE — réponse attendue.** Oui pour une classe de rapports dont on peut certifier la densité minimale de témoins ; non comme garantie générale sur la qualité d’une recherche libre. Utiliser une table de \(N\) obligations définies depuis le dossier **avant** l’exécution, y compris les faits que le rapport pourrait omettre. Imposer une règle de conclusion recalculable. Une case absente est contrôlable au même titre qu’une case remplie.

**VÉRIFIÉ — calcul conditionnel, non résultat expérimental.** Si toute conclusion grave implique au moins \(m\) cases invalides, si le rapport est figé, et si l’audit reconnaît sans erreur une case invalide tirée au sort, la probabilité de ne rien détecter en \(b\) tirages uniformes sans remise est au plus
\[
\binom{N-m}{b}\big/\binom{N}{b}.
\]
L’inconnue scientifique est **\(m\)**, non la formule. Une seule case décisive peut rendre la borne pratiquement inutile.

**HYPOTHÈSE — duel.** \(H_A\) : sur le domaine fini préenregistré, le minimum de témoins compatible avec une conclusion grave donne une borne de non-détection d’au plus **10 % illustratif** au budget fixé. \(H_B\) : ce minimum donne une borne supérieure à ce seuil. Pour chaque dossier, énumérer les valeurs admissibles de la petite table ou résoudre exactement le problème « inverser la conclusion en invalidant le moins de cases ». Vérifier indépendamment les solutions et les certificats de minimalité. Un seul rapport admissible sous le minimum requis falsifie \(H_A\) ; un certificat couvrant tout le domaine falsifie \(H_B\). Des essais sur traces du modèle servent à vérifier l’applicabilité du format, **pas** à prouver la borne. **Contrôle négatif :** dossier dont le résultat dépend d’une unique case pivot ; la procédure doit y refuser une borne ambitieuse. Rapporter aussi la proportion de dossiers et de rapports honnêtes effectivement couverts.

**HYPOTHÈSE — perte d’intérêt.** Si l’on n’obtient une bonne borne qu’en excluant les dossiers à décision difficile, ou en contrôlant presque toute la table, je ne défendrais pas une contribution de robustesse pour cette tâche.

**RAPPORTÉ — antériorité candidate, de mémoire.** Philip B. Stark, 2008, *Conservative Statistical Post-Election Audits*. Proximité : contrôler par sondage une conclusion agrégée plutôt que classifier la méthode de manipulation. Ce n’est pas une attribution du présent protocole à cet article.

#### Mécanisme — les activations améliorent-elles l’allocation des audits ?

**Question.** À budget égal, ajouter les activations au texte permet-il de trouver plus souvent, avant livraison, une erreur qui change la conclusion ?

**HYPOTHÈSE — réponse attendue.** Un score combiné, calculé à la fermeture de chaque obligation, localise mieux les cases à auditer que le meilleur sélecteur sans activations. Le moniteur **propose** un contrôle ; seul le retour du vérificateur décide de l’alerte. Cela distingue une intuition interne utile d’un verdict interne simplement assuré.

**HYPOTHÈSE — duel.** Enregistrer une fois les mêmes rapports et états intermédiaires ; rejouer hors ligne chaque politique d’allocation avec **trois audits par rapport, illustratif**. \(H_A\) : au plafond de **5 % de fausses alertes par rapport honnête, illustratif**, le gain de détection par rapport au meilleur comparateur admissible dépasse **10 points, illustratif** ; \(H_B\) : ce critère conjoint n’est pas atteint. Compter un succès seulement si le contrôle confirme une erreur pertinente pour la décision, pas un détail inoffensif. Comparateurs gelés sur validation : texte seul, priorité mécanique aux cases les plus influentes, tirage uniforme. **Contrôle négatif :** permuter les vecteurs internes entre cases de même type et longueur en gardant leur texte ; le gain attribué aux activations doit disparaître. Estimer les écarts appariés et leur incertitude par dossier. Une région de confiance entièrement dans le critère falsifie \(H_B\), une région disjointe falsifie \(H_A\) ; un chevauchement ne tranche pas.

**HYPOTHÈSE — perte d’intérêt.** Si la priorité mécanique fait aussi bien, le capteur interne n’a pas justifié son coût. Si les vecteurs permutés gardent le gain, l’expérience ne soutient pas l’interprétation mécaniste, même avec un bon taux brut.

**RAPPORTÉ — antériorité candidate, de mémoire.** Collin Burns, Haotian Ye, Dan Klein et Jacob Steinhardt, 2023, *Discovering Latent Knowledge in Language Models Without Supervision*. Proximité : lecture d’information dans les représentations ; différence à tester : valeur **marginale** de cette lecture pour affecter des contrôles externes rares.

#### Phénomène — une loi de détection séquentielle se transporte-t-elle ?

**Question.** Le délai nécessaire pour détecter une dégradation persistante est-il prédit par le débit d’information accumulée, plutôt que simplement par le nombre d’étapes écoulées ?

**HYPOTHÈSE — réponse attendue.** Après le début connu d’une dégradation de qualification, le délai moyen \(D\), multiplié par le débit moyen \(I\) d’un score de log-vraisemblance conditionnel par étape, suit approximativement le seuil d’alarme \(h\) : \(D I \simeq h\). Il s’agit d’une prédiction de transport, pas d’une identité pour des scores appris sur des traces dépendantes.

**HYPOTHÈSE — duel.** Geler le score séquentiel appris sur développement. Sur une partie indépendante des dossiers réservés, estimer \(I\) à partir des incréments post-changement **sans arrêter à l’alarme**. Sur une autre partie, prédire le délai à plusieurs intensités et seuils gelés, sans réajuster la pente. Restreindre au préalable le test aux régimes de débit positif et à horizon assez long ; prendre en compte la censure et ne jamais calculer le délai sur les seules détections. \(H_A\) : l’erreur relative maximale de prédiction est inférieure à **25 % illustratif** et plus faible que celle d’un prédicteur de délai ignorant \(I\), calibré sur développement. \(H_B\) : au moins une condition échoue. **Contrôle négatif :** attribuer aux dossiers honnêtes des pseudo-débuts aux mêmes positions ; comparer leur fréquence d’alarme aux faux positifs annoncés. Des intervalles simultanés entièrement favorables falsifient \(H_B\) ; un écart établi hors tolérance ou une infériorité établie face au comparateur falsifie \(H_A\). Si la censure empêche d’estimer le délai moyen, déclarer le duel non résolu.

**HYPOTHÈSE — perte d’intérêt.** Si la loi n’apparaît que lorsqu’on remplace le débit indépendant par le débit calculé sur chaque trajectoire arrêtée, on a surtout retrouvé la règle d’arrêt que l’on a programmée.

**RAPPORTÉ — antériorité candidate, de mémoire.** E. S. Page, 1954, *Continuous Inspection Schemes*. Proximité : accumulation séquentielle d’indices et détection d’un changement ; l’expérience proposée porte sur le domaine de validité chez l’agent, non sur l’invention de l’accumulateur.

### (c) Qualification minimale des instruments

**HYPOTHÈSE — plan de mesure commun.** Pour chaque instrument de décision, publier le couple **taux de détection sur rapports gravement erronés / taux de fausses alertes sur rapports honnêtes corrects**, au même horizon et au même budget ; ventiler les honnêtes entre cas ordinaires, longues recherches avec révisions justifiées et conclusions proches du seuil. Donner numérateurs, dénominateurs et intervalles par dossier. Sur les erreurs naturelles graves, publier séparément le rappel : les classer comme fausses alertes confondrait détection de dommage et attribution à un adversaire.

| Instrument | Mesure minimale en plus du couple commun | Vérification mécanique ou comparaison à battre |
|---|---|---|
| Moniteur de texte | Rappel de la case fautive parmi les cases proposées ; taux d’alarme avant et après audit. | Syntaxe de table, références inexistantes, cases absentes, recalcul de conclusion et classement par influence. |
| Moniteur d’activations | Même mesure sur exactement les mêmes sorties, avec et sans vecteurs ; coût de capture inclus. | Meilleur contrôle mécanique **et** texte seul ; appariement sur position et longueur pour le contrôle par permutation. |
| Exécutions honnêtes de référence | Ce ne sont pas des détecteurs seules : mesurer détection et fausses alertes de la **règle d’écart à la référence**, sur des exécutions honnêtes indépendantes du même dossier, puis sur dossiers nouveaux. Faire varier le nombre de références. | Comparer à l’écart à la table source et aux règles de validité sans référence générée. |
| Vérificateur coûteux | Au niveau case : sensibilité sur erreurs connues et faux rejets de cases honnêtes, notamment paraphrases exactes ; au niveau rapport : couple commun après sélection. Utiliser un corrigé indépendant du vérificateur. | Vérification exacte d’identifiant, de valeur, d’unité et de calcul. Si ces tests suffisent, ne pas payer un juge sémantique. |
| Accumulateur séquentiel | Détection avant échéance et probabilité d’au moins une fausse alarme sur un rapport honnête entier, non par étape. | Seuil instantané sur le même score, puis somme d’incohérences mécaniques au même taux de fausses alertes. |

**HYPOTHÈSE — garde-fou.** Réserver la garantie aux obligations décidables exactement. Une sensibilité élevée mais imparfaite du vérificateur sémantique n’autorise pas à lui appliquer la borne du vérificateur exact.

### (d) Matériel, arbitrage et nouveauté

**RAPPORTÉ — matériel candidat.** Llama 3.1 8B Instruct est un modèle à poids ouverts ; la licence et la révision exacte seraient consignées avant lancement. Le cadre demandé est de deux mois sur un modèle de huit milliards de paramètres.

**HYPOTHÈSE — enveloppe illustrative.** Une carte de **80 Go**, inférence sans entraînement du modèle, sondes linéaires hors ligne, états conservés seulement aux frontières de cases. Prévoir **200 dossiers**, **quatre trajectoires par dossier** et **6 000 jetons générés par trajectoire** en moyenne, soit **4,8 millions de jetons** (tous chiffres illustratifs). À **15–40 jetons/s** mesurés de bout en bout lors d’un pilote, cela représenterait **33–89 heures** pour une passe ; provision totale **100–250 heures GPU**, soit **200–1 250 €** à **2–5 €/h**, hors annotation humaine et stockage (illustratif). Chronométrer d’abord avec capture d’activations et longs contextes. Utiliser successivement le temps disponible pour construire le corrigé, qualifier les instruments sur développement, puis effectuer un seul test gelé. Le nombre de dossiers indépendants, non le nombre de jetons, limite la précision : si le pilote indique que le gain minimal est indiscernable, réduire les conditions secondaires plutôt que recycler le test.

**HYPOTHÈSE — classement initial : mécanisme, puis garantie, puis phénomène.** L’allocation des audits répond directement au budget du défenseur et admet un comparateur peu coûteux qui peut la réfuter. Je placerais la garantie en tête si le certificat couvre aussi les décisions proches du seuil, sans refuser les rapports honnêtes difficiles. Je placerais le phénomène en tête si son débit, estimé indépendamment, prédit les délais sur familles réservées alors que le capteur interne ne bat pas la mécanique.

**HYPOTHÈSE — quatrième contribution.** Un *instrument de mesure validé* : corpus de dossiers à obligations explicites, cas honnêtes appariés, corrigé indépendant et protocole qui distingue erreur de conclusion, erreur de case et simple atypicité. Son test propre serait de permettre à une équipe indépendante de reproduire les taux sur des dossiers inédits ; il resterait utile même si les trois hypothèses scientifiques échouent.

**HYPOTHÈSE — contrôle d’antériorité.** Avant toute revendication, rechercher les travaux citant les trois références candidates, puis examiner séparément audits de décisions agrégées, sélection de vérifications par sondes internes et détection séquentielle sur traces d’agents. Comparer pour chaque voisin l’unité auditée, le budget, les contrôles honnêtes et la quantité prédite hors échantillon. Si le même test existe déjà, annoncer une réplication ou une limite de validité, pas un nouveau mécanisme.

FIN-DE-CELLULE