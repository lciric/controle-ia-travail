**Recommandation**

Je recommande une **cadence intermédiaire de 4 appels simultanés, sans pause**, pour les deux lecteurs. Elle obtient l'essentiel du gain de temps de l'option (b) tout en divisant par deux le risque lié aux limites de débit non vérifiées et l'exposition aux appels coupés.

### 1. Arbitrage pour les lecteurs : pourquoi 4 appels simultanés sans pause

**Durée totale.** L'option (a) est excessivement longue : 7,0 à 12,3 jours par lecteur, dont environ 42 heures d'attente pure dues à la pause de 10 s. Étaler la collecte sur une à deux semaines accroît le risque d'incidents réseau, matériels ou humains. À 4 appels simultanés sans pause, chaque lecteur s'exécute en **31,5 h (1,3 jour)** à 30 s par appel, et en **63,1 h (2,6 jours)** à 60 s. On économise ainsi environ 80 % du temps de l'option (a), pour un allongement limité face à l'option (b) (15,8 h à 31,5 h).

**Exposition aux appels coupés.** Avec 4 appels en vol, le pire cas immobilisé passe d'environ 1,24 USD à **environ 4,97 USD** chez le fournisseur concerné (contre ~9,94 USD en (b)), et la marge utile de la plus grosse ligne reste autour de **2,9 fois** le coût attendu (contre 3 en (a) et 2,8 en (b)). Ce surcoût de réserve est marginal, à condition d'empêcher qu'un incident durable n'enchaîne les troncatures.

**Limites de débit (*rate limits*) et conduite à tenir.** C'est le principal point faible de l'option (b) : ses besoins estimés (~16 requêtes/min et ~149 000 jetons/min à 30 s) n'ont pas été vérifiés. Or, la durée d'un appel n'étant pas mesurée, une latence réelle de 15 s doublerait le débit (~300 000 jetons/min), au risque de saturer des paliers commerciaux courants. À 4 appels simultanés, le besoin tombe à **~8 requêtes/min et ~74 500 jetons/min** à 30 s, offrant une marge d'un facteur 2 si les réponses sont plus rapides que prévu. Avant le lancement, il convient de vérifier les plafonds de compte dans la console de chaque fournisseur (sans modifier le protocole).

Si une limite de débit (erreur HTTP 429) survient néanmoins :
1. **Libérer la réservation du compteur** pour l'appel rejeté en amont : non exécuté par le modèle, il ne doit pas être compté comme un appel coupé facturable ;
2. **Appliquer une pause partagée** à l'ensemble des envois — en suivant l'en-tête `Retry-After` s'il existe, sinon par temporisation exponentielle avec gigue (*backoff* avec *jitter*) — afin que les autres appels en file ne continuent pas de saturer l'API ;
3. **Réessayer systématiquement** sans jamais écarter un texte de l'échantillon ; si les erreurs 429 persistent après plusieurs cycles de temporisation, interrompre proprement la collecte pour la relancer à une cadence moindre (par exemple 2).

**Simplicité.** L'option (a) est la plus simple (une boucle séquentielle sans verrou). Au-delà d'un appel en vol, la complexité technique est identique pour 4 ou 8 appels simultanés : une file bornée, une réservation atomique (verrouillée) sur le compteur et une écriture persistante au fil de l'eau. Maintenir un plafond fixe à 4 évite toute logique d'auto-adaptation complexe.

**Validité de la mesure.** Les appels étant indépendants et lancés dans l'ordre pré-tiré, la parallélisation n'affecte pas la validité, à deux conditions : enregistrer chaque réponse sous son identifiant de texte (l'ordre de retour pouvant différer de l'ordre d'envoi) et ne jamais abandonner un texte en erreur temporaire (ce qui introduirait un biais de non-réponse, plus probable sur les textes longs). Mieux encore, ramener la collecte de 7–12 jours à 1,3–2,6 jours **protège la validité temporelle** en réduisant l'exposition à une mise à jour silencieuse ou à une dérive des modèles commerciaux.

### 2. Cadence pour le juge (80 appels)

**Non**, le juge doit fonctionner **1 appel à la fois** (sans pause, ou avec une pause minimale). Pour 80 appels, l'exécution séquentielle ne dure que **40 minutes** à 30 s et **1 h 20** à 60 s (53 min à 1 h 33 avec une pause de 10 s). Paralléliser un lot aussi court n'apporte presque rien en délai, mais augmente inutilement le poids relatif des réservations simultanées sur une ligne au plafond probablement beaucoup plus modeste. Il suffit de réutiliser le même script avec un paramètre de concurrence fixé à 1.

### 3. Garde-fou à ajouter

J'ajouterais un **disjoncteur automatique (*circuit breaker*) dédié aux appels coupés et défaillances corrélées**, appuyé sur une journalisation atomique de l'état sur disque. Le compteur actuel borne la dépense globale, mais ne distingue pas le budget consommé par des jugements exploitables de celui absorbé par des estimations prudentes lors d'une panne réseau ou d'une troncature répétée de l'API. À 4 appels simultanés, un incident non détecté pourrait rapidement grignoter la marge de sécurité.

Le script doit donc stopper immédiatement tout nouvel envoi — tout en laissant se terminer les appels en vol et en sauvegardant l'état exact pour reprise — dès qu'un seuil est atteint : **4 à 5 appels coupés ou en échec consécutifs** (une vague complète), un **sous-plafond cumulé dédié aux estimations d'appels coupés** (par exemple 2 % du budget de la ligne), ou **3 cycles successifs d'erreurs 429**.

### 4. Niveau de confiance

**Confiance : moyenne.** La confiance est élevée sur la structure du plan (écarter l'option (a) pour les lecteurs, exécuter le juge en séquentiel, ajouter le disjoncteur et traiter les 429 sans perte d'observations). Elle demeure moyenne sur le nombre exact de 4 appels simultanés, car deux paramètres décisifs ne sont pas encore mesurés : les quotas réels de jetons par minute des fournisseurs et la durée effective d'un appel. Vérifier les paliers de compte puis observer les premières minutes d'exécution permettra de confirmer ce réglage ou de l'ajuster légèrement (2–3 ou 6–8).