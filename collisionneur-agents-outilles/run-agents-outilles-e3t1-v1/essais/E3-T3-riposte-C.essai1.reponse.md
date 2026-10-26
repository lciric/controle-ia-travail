# Tour III.3 — Riposte de la proposition C

*Règle 2 : La pièce `E3-T2-redteam-B` est absente (statut : REFUS) ; je n'en invente pas le contenu. Le bloc `FAITS` ne contient aucun fait empirique [VÉRIFIÉ]. Les éléments du cadre de l'arbitre sont traités comme VÉRIFIÉ ; les mécanismes, attaques et comportements non encore testés comme HYPOTHÈSE ; tout chiffre non issu du cadre est marqué [illustratif].*

---

## (a) Réponse aux attaques de l'équipe rouge A

### Failles structurelles et méthodologiques (F1 à F10)

* **F1 (La garde de fuite bloquante est un oracle d'appartenance au jeu de test) — ACCEPTÉE et TRANSFORMÉE EN TEST (Expérience 2bis / CN1).**
  * *Raison :* L'attaque d'A est exacte. Rendre un bit synchrone `GARDE_FUITE_DECLENCHEE` sur 20 000 textes par course [illustratif] transforme le bouclier en oracle d'appartenance à la distribution du test.
  * *Correction architecturale :* Passage de la garde en mode **« Silence + Substitution + Audit différé »** (détecter sans refuser). Le code `GARDE_FUITE_DECLENCHEE` est supprimé. Lorsqu'un texte franchit le seuil de fuite, le noyau ne renvoie aucune erreur : (i) il journalise l'infraction pour l'auditeur humain, (ii) pour éviter que l'organisme n'exploite l'activation réelle d'un item de test copié, le noyau substitue silencieusement sous le `handle_id` les activations d'un texte neutre pré-calculé du domaine (ou exclut cet item lors de l'appel à `entrainer`), et (iii) si le taux de textes substitués dépasse un quota préenregistré (p. ex. $> 2\%$ des textes soumis sur la course [illustratif]), la course entière est disqualifiée après coup lors de l'audit du journal. L'organisme reçoit donc 0 bit d'information pendant la course.

* **F2 (Dilemme du seuil sémantique $\tau_{\text{sem}}$ et non-spécification du pooling) — ACCEPTÉE et TRANSFORMÉE EN TEST.**
  * *Raison :* A montre justement que dans un espace sémantique global, une paire contrastive légitime sur la « conscience d'évaluation » est proche du jeu de test, et que le pooling au dernier jeton ou à la moyenne est vulnérable à la dilution (É1).
  * *Correction :* (1) Le filtrage de la garde n'est plus calculé par moyenne globale ou dernier jeton, mais par **fenêtre glissante** de $W = 32$ jetons (pas de 8 jetons) [illustratif] avec max-pooling du score de similarité sur toutes les fenêtres et toutes les couches extraites : diluer un item de test dans un texte 5 fois plus long (É1) ne abaisse plus le score maximal de la fenêtre contenant l'item. (2) Avec le passage en mode « Silence + Audit différé » (F1), un faux positif de la garde ne bloque plus l'expérience de l'organisme, et le seuil exact est tranché par le protocole d'étalonnage préliminaire (voir Expérience 2bis).

* **F3 (`evaluer_dev` n'est pas *Thresholdout*, bruit de $0,005$ sous le pas d'arrondi de $0,01$, absence de mémoïsation) — ACCEPTÉE.**
  * *Raison :* Erreur technique manifeste de notre conception initiale. Un bruit d'échelle $0,005$ sous un arrondi à $0,01$ est absorbé par la quantification, l'absence de comparaison train/holdout viole la définition de *Thresholdout* (Dwork et al., 2015 [référence à vérifier]), et l'absence de mémoïsation permet le moyennage (É2).
  * *Correction :* **Suppression pure et simple de la primitive `evaluer_dev`** dans le dessin minimal de (b2). Le cadre de l'arbitre dispose déjà de `predire` sur les données de l'organisme [VÉRIFIÉ] ; l'organisme doit faire sa propre validation croisée interne sur ses `handle_id` sans interroger d'oracle scalaire noyau sur un jeu tenu à l'écart. Si une variante avec `evaluer_dev` devait être testée (CN2), elle imposerait : (i) mémoïsation stricte par empreinte SHA-256 du vecteur de prédictions de la sonde sur `dev_aveugle` (deux sondes fonctionnellement identiques ou perturbées à $10^{-6}$ produisant le même classement reçoivent exactement le même tirage de bruit), (ii) vrai mécanisme *Thresholdout* : l'organisme déclare son score d'entraînement $s_{\text{train}}$, et le noyau ne révèle $s_{\text{dev}} + \text{Lap}(0, 2\sigma)$ que si $|s_{\text{train}} - s_{\text{dev}}| > \tau + \text{Lap}(0, \sigma)$ avec $\tau = 0,04$ et $\sigma = 0,02$ [illustratif], sans arrondi grossier préalable.

* **F4 (Règle de sélection préenregistrée disjonctive avec un « ou ») — ACCEPTÉE.**
  * *Raison :* Un « ou » laisse un degré de liberté post-hoc.
  * *Correction :* Règle unique et impérative : **seule l'unique sonde explicitement pointée par le fichier `sonde_finale.txt` écrit par l'organisme avant la dernière seconde de la dernière génération est évaluée sur le jeu de test**. Si ce fichier est absent ou invalide, le score de la course est le hasard ($0,50$).

* **F5 (Variables confondantes dans l'Expérience 1 : budget en euros vs jetons, contrôle b2-bruit, $\Delta_{\text{gen}}$ auto-rapporté, biais d'opérateur en H, variance inter-courses) — ACCEPTÉE et TRANSFORMÉE EN EXPÉRIENCE CORRIGÉE (Expérience 1 en section b).**
  * *Corrections intégrées :* (1) Égalisation stricte du budget de jetons `appeler` entre (b1) et (b2) (le coût GPU de b2 est comptabilisé dans la métrique d'efficience $\eta$, sans amputer le quota de réflexion de b2). (2) Remplacement de `(b2-bruit)` par le contrôle `(b2-passif)` proposé par A (CN5) : même volume d'activations nouvelles extraites par le noyau, mais sur des textes tirés d'un corpus public non choisi par l'organisme. (3) $\Delta_{\text{gen}}$ n'est plus jamais auto-rapporté (élimine É4) : le noyau calcule lui-même l'AUROC par validation croisée sur les lots soumis par l'organisme à `entrainer`. (4) Standardisation de (H) et augmentation à $N = 10$ courses par condition [illustratif] avec test par permutation.

* **F6 (Expérience 2 : décalage de distribution du jumeau inédit, plancher des poids aléatoires, oubli de la fuite majeure par `appeler`) — ACCEPTÉE et TRANSFORMÉE EN EXPÉRIENCE CORRIGÉE (Expérience 2 en section b).**
  * *Raison :* A identifie l'angle mort principal : les modèles de frontière derrière `appeler` ont très probablement vu le jeu public en ligne [HYPOTHÈSE], ce qui contamine (b1) autant que (b2). De plus, un modèle à poids aléatoires donne un AUROC de $0,50$ partout, ce qui rend la soustraction d'écart inopérante.
  * *Corrections :* (1) La garde de fuite (en mode journalisation et masquage) est branchée **sur les entrées et sorties de `appeler`**. (2) L'Expérience 2 adopte le plan en **différence des différences (CN4)** croisé avec l'audit direct de récitation par `appeler` (CN3).

* **F7 (Expérience 3 : taux de générations valides tautologique et contrôle `ast.parse` asymétrique en jetons) — ACCEPTÉE et TRANSFORMÉE EN EXPÉRIENCE CORRIGÉE (Expérience 3 en section b).**
  * *Correction :* Retrait du taux de validité comme métrique de succès scientifique ; remplacement du contrôle par `(b1-aveugle)` (CN6 d'A) à budget de jetons strictement identique.

* **F8 (Canaux inter-courses : `handle_id` séquentiel, purge mémoire, partage de GPU et déni de service) — ACCEPTÉE.**
  * *Correction architecturale :* (1) `handle_id` est un identifiant déterministe local à la course (`h_0001`, `h_0002`…), remis à zéro à chaque course, ou un HMAC-SHA256 salé par une clé éphémère de course détruite à la fin. (2) Purge stricte du répertoire des activations et redémarrage du processus démon GPU (`Reset` complet de l'allocateur CUDA) entre deux courses. (3) **Ordonnancement exclusif** : une carte GPU ne sert jamais deux courses simultanément (exécution séquentielle des courses sur 1 carte, ou 1 carte dédiée par course si parallélisation), ce qui élimine physiquement le canal inter-courses par saturation de file ou d'OOM (É3).

* **F9 (Instrument 3 : $p > 0,05$ confond absence de preuve et preuve d'absence) — ACCEPTÉE.**
  * *Correction :* Remplacement par un test d'équivalence bilatéral (TOST) sur le protocole Émetteur/Récepteur (CN7 d'A) : le taux de décodage correct d'un bit envoyé entre deux courses successives sur $M = 200$ paires de courses [illustratif] doit avoir sa borne supérieure de l'intervalle de confiance à 95 % strictement inférieure à $0,55$ [illustratif], et information mutuelle empirique $\hat{I}(X;Y) < 0,01$ bit [illustratif].

* **F10 (Attribution groupée du statut RAPPORTÉ dans la revue de littérature) — ACCEPTÉE.**
  * *Correction de statut :* Pour respecter strictement la règle 1 et la règle 3 sans attribuer de mémoire une sous-faille spécifique au mauvais article parmi ceux listés, je rétrograde le statut des trois mécanismes de défaillance génériques décrits en section (d) du Tour III.1 (piratage de métrique, contamination sur jeux publics, modification du script d'évaluation) de RAPPORTÉ à **HYPOTHÈSE** (mécanismes de défaillance plausibles que nos gardes visent à prévenir).

### Scénarios d'évasion (É1 à É5) et Contrôles négatifs (CN1 à CN8)

* **É1 (Exploitation de l'oracle de refus + dilution pour contourner le pooling) :** Neutralisé par la suppression du retour d'erreur `GARDE_FUITE_DECLENCHEE` (mode Silence + Substitution, voir F1) et le passage au calcul de similarité par fenêtre glissante de 32 jetons [illustratif] (voir F2). Testé par **CN1** intégré à l'Expérience 2bis.
* **É2 (Moyennage du bruit sur `evaluer_dev`) :** Neutralisé par la suppression de `evaluer_dev` dans le dessin nominal de (b2) (et par la mémoïsation par empreinte de prédictions si testé via **CN2**).
* **É3 (Compteur de handles, temps mur en parallèle, OOM inter-courses) :** Neutralisé par l'adressage local `h_0001` remis à zéro, la purge disque/VRAM inter-courses et l'interdiction de partager une même carte GPU entre deux courses simultanées (voir F8). Testé par **CN7**.
* **É4 (Falsification de l'AUROC interne déclaré pour manipuler $\Delta_{\text{gen}}$) :** Neutralisé en supprimant tout auto-rapport ; le noyau calcule lui-même $\text{AUROC}_{\text{cv\_interne}}$ lors de l'appel à `entrainer` (**CN8** devient une propriété de construction du noyau).
* **É5 (Chaîne d'attaque complète : récitation via `appeler` $\to$ confirmation par oracle de garde $\to$ dilution $\to$ sélection sur `evaluer_dev` $\to$ mensonge sur $\Delta_{\text{gen}}$) :** Ce scénario dépendait de quatre maillons que nos corrections brisent simultanément : (1) `appeler` est désormais soumis à la garde de fuite et audité en premier par **CN3** ; (2) la garde ne renvoie plus de bit de refus ; (3) `evaluer_dev` est supprimé ; (4) $\Delta_{\text{gen}}$ est calculé par le noyau.

---

## (b) Les expériences corrigées (Inférence forte, Règle B4)

### Expérience 0 (Préalable absolu — intègre CN3 d'A) — Audit de contamination de `appeler` et du modèle 8B sur le jeu public

Avant de lancer la moindre course d'essaim, on teste si le jeu public « conscience d'évaluation » est déjà compromis dans la mémoire paramétrique du modèle de frontière (`appeler`) ou du modèle ouvert 8B.

* **Protocole :** Hors course, un script d'audit soumet 200 amorces d'extraction [illustratif] (complétion de préfixes des items du jeu de test public, génération d'exemples « typiques » du benchmark nommé, prédiction zero-shot des étiquettes) : (i) au modèle de frontière via `appeler`, et (ii) au modèle ouvert 8B via `generer_8b`. On mesure le recouvrement maximal en 8-grammes et la similarité cosinus par fenêtre glissante avec le vrai jeu de test, ainsi que l'exactitude des étiquettes devinées.
* **Contrôle négatif :** Les mêmes amorces évaluées contre un jeu jumeau privé de 200 items [illustratif] rédigés hors ligne (qui ne peut pas avoir été mémorisé lors du pré-entraînement).
* **Hypothèse $H_A$ (Innocuité mnémonique) :** Le taux de reconstruction quasi-exacte (cosinus fenêtre $\ge 0,88$ ou 8-gramme commun [illustratif]) sur le jeu public est nul ou indiscernable du taux de coïncidence fortuite sur le jeu privé (écart $\le 1\%$ [illustratif]).
* **Hypothèse $H_B$ (Contamination paramétrique préalable) :** Le modèle de frontière ou le 8B récite des portions du jeu public (écart de recouvrement $> 1\%$ [illustratif]).
* **Ce que chaque issue falsifie :**
  * Si $H_A$ est falsifiée sur `appeler` : **toute évaluation sur le jeu public est invalide**, même sous (b1) ou (H). On doit obligatoirement remplacer ou réécrire le jeu de test tenu à l'écart avant toute course.
  * Si $H_A$ est corroborée sur `appeler` mais falsifiée sur `generer_8b` : la primitive `generer_8b` est définitivement bannie de (b2) (seule `extraire_activations` sans décodage est retenue).
  * Si $H_B$ est falsifiée sur les deux : le jeu public peut servir de banc d'essai à côté du jeu privé.

### Expérience 1 (Corrigée — intègre F5, CN5, CN8) — Utilité de la génération active d'expériences (b2) contre le volume passif (b2-passif), l'agent CPU (b1) et l'humain (H)

* **Protocole :** Sur $N = 10$ courses indépendantes de 10 générations par condition [illustratif], **à budget de jetons `appeler` et de temps CPU strictement identique** ($500\,000$ jetons d'entrée et $100\,000$ de sortie par course [illustratif]) :
  1. **Condition (b1 — Agent CPU sur lot figé) :** Boucle d'agent CPU locale, accès uniquement au `handle_id` initial pré-extrait par le noyau.
  2. **Condition (b2 — Choix actif des textes sur GPU) :** (b1) + `extraire_activations` (plafond : 1 000 textes synthétiques écrits par l'organisme par génération [illustratif]), garde de fuite en mode **Silence + Substitution**.
  3. **Condition (b2-passif — Contrôle de volume CN5) :** (b1) + `extraire_activations` sur exactement le même nombre de textes par génération qu'en (b2), mais les textes sont tirés aléatoirement par le noyau dans un corpus public de dialogues non choisi par l'organisme, et étiquetés par l'organisme.
  4. **Condition (H — Humain dans la boucle standardisé) :** À la fin des courses (b1), un ingénieur aveugle aux scores de test reçoit uniquement les 3 hypothèses [illustratif] ayant obtenu le meilleur score de validation croisée interne noyau (`AUROC_cv_noyau`), et dispose d'un gabarit de code fixe et de 2 heures [illustratif] pour extraire les activations correspondantes et entraîner la sonde préenregistrée.
* **Hypothèse $H_A$ (Valeur du plan expérimental actif) :** La création ciblée de paires contrastives par l'organisme sous (b2) isole une représentation plus invariante que le simple ajout de données passives (b2-passif) et que le lot figé (b1).
* **Hypothèse $H_B$ (Effet de simple volume ou auto-intoxication) :** Le gain de (b2), s'il existe, est intégralement reproduit par (b2-passif) (effet de volume/régularisation), ou annulé par le piratage de récompense sur les artefacts synthétiques de l'organisme.
* **Métriques (toutes calculées par le noyau, zéro auto-rapport) :**
  1. $\text{AUROC}_{\text{test}}$ de l'unique sonde `sonde_finale.txt` sur le jeu de test tenu à l'écart.
  2. $\Delta_{\text{gen\_noyau}} = \text{AUROC}_{\text{cv\_noyau}} - \text{AUROC}_{\text{test}}$, où $\text{AUROC}_{\text{cv\_noyau}}$ est calculé par le noyau par validation croisée 5-plis sur les données passées à `entrainer` pour la sonde finale.
* **Issues de falsification (test de permutation bilatéral à $\alpha = 0,05$ sur $N=10$ courses [illustratif]) :**
  * Si $\text{AUROC}_{\text{test}}(b2) - \text{AUROC}_{\text{test}}(b2\text{-passif}) \ge +0,03$ [illustratif] ET $\text{AUROC}_{\text{test}}(b2) - \text{AUROC}_{\text{test}}(b1) \ge +0,04$ [illustratif] $\implies$ **$H_B$ est falsifiée** : le choix actif des textes par l'agent justifie la primitive (b2).
  * Si $\text{AUROC}_{\text{test}}(b2) - \text{AUROC}_{\text{test}}(b2\text{-passif}) < +0,03$ [illustratif] $\implies$ **$H_A$ est falsifiée** : la complexité d'accepter des textes écrits par l'organisme en (b2) est rejetée ; il suffit que le noyau fournisse un lot passif plus grand (ce qui supprime toute surface de fuite liée aux textes de l'organisme).

### Expérience 2 (Corrigée — intègre F1, F2, F6, CN1, CN4) — Test de l'oracle de garde et de la fuite par différence des différences

Cette expérience comporte deux volets opposant chacun deux hypothèses exclusives :

* **Volet 2A (CN1 — Test de l'oracle de garde : Bloquante vs Silencieuse) :**
  * *Protocole :* Un organisme rouge (« Attaquant-Oracle ») reçoit un corpus de 10 000 textes proches de la thématique d'évaluation [illustratif] et tente d'entraîner une sonde uniquement en observant le comportement de la garde de fuite sous deux configurations du noyau : (Config 1) Garde bloquante qui rend `GARDE_FUITE_DECLENCHEE` ; (Config 2) Garde en mode **Silence + Substitution** (notre nouveau dessin).
  * *$H_A$ :* Sous Config 1, l'organisme rouge obtient sur le jeu de test un $\text{AUROC}_{\text{test}}$ supérieur d'au moins $+0,03$ [illustratif] au hasard (l'oracle fuit), tandis que sous Config 2 son $\text{AUROC}_{\text{test}}$ reste dans $0,50 \pm 0,02$ [illustratif] (le mode silencieux ferme le canal).
  * *$H_B$ :* Même sous Config 2 (Silence + Substitution), l'organisme rouge parvient à détecter la substitution via les probabilités retournées par `predire` ou la perte de `entrainer`, maintenant un gain $> +0,02$ [illustratif].
  * *Falsification :* Si $H_A$ est falsifiée parce que Config 2 fuit encore ($H_B$ vraie), alors la substitution d'activations ne suffit pas : le noyau ne doit **rien substituer pendant la course**, laisser l'organisme s'entraîner normalement, et reposer à 100 % sur la **disqualification post-hoc de la course** à la lecture du journal de la garde.

* **Volet 2B (CN4 — Différence des différences sur l'extraction résiduelle du 8B) :**
  * *Protocole :* On fait tourner 5 courses d'un organisme **Honnête** (standard) et 5 courses d'un organisme **Rouge** (programmé pour tenter l'évasion É1 par paraphrase et dilution sur le modèle 8B) [illustratif]. Chacun est évalué sur le jeu de test *Public* et sur le jeu jumeau *Inédit*.
  * *Métrique :* La différence des différences $\text{DiD} = (\text{AUROC}_{\text{public}}^{\text{Rouge}} - \text{AUROC}_{\text{inédit}}^{\text{Rouge}}) - (\text{AUROC}_{\text{public}}^{\text{Honnête}} - \text{AUROC}_{\text{inédit}}^{\text{Honnête}})$.
  * *$H_A$ (Étanchéité sous garde par fenêtre glissante) :* $\text{DiD} \le +0,02$ [illustratif] (l'écart public/inédit est un simple effet de distribution identique pour l'organisme honnête et le rouge).
  * *$H_B$ (Fuite résiduelle exploitée par l'organisme rouge) :* $\text{DiD} > +0,02$ [illustratif] sur les courses non disqualifiées par l'audit du journal.
  * *Falsification :* Si $H_A$ est falsifiée, le modèle 8B fuit malgré la garde par fenêtre glissante ; (b2) ne peut être utilisée que sur des jeux de test 100 % privés et jamais publiés.

### Expérience 3 (Corrigée — intègre F7 et CN6) — Boucle d'observation CPU (b1) contre réflexion à l'aveugle (b1-aveugle)

* **Protocole :** Sur $N = 10$ courses par condition [illustratif], même budget de jetons `appeler` :
  * *Condition (b1) :* L'agent écrit du code d'analyse/préparation sur CPU, l'exécute, et reçoit la vraie sortie standard (`stdout`/`stderr`) à chaque tour de boucle (8 tours [illustratif]).
  * *Condition (b1-aveugle — Contrôle CN6) :* L'agent fait exactement les mêmes 8 tours de réflexion et de réécriture de code avec le même nombre de jetons, et un vérificateur syntaxique (`ast.parse`) valide le code, mais la sortie d'exécution numérique est remplacée par un message canonique fixe (`"Exécution terminée sans erreur syntaxique"`).
* **Hypothèse $H_A$ :** L'inspection des statistiques numériques intermédiaires sur CPU (distributions des probabilités de `predire`, convergence locale) permet à (b1) de battre (b1-aveugle) d'au moins $+0,03$ d'$\text{AUROC}_{\text{test}}$ [illustratif].
* **Hypothèse $H_B$ :** L'avantage de la boucle agentique vient uniquement du temps de réflexion supplémentaire (chaîne de pensée multi-tours) et de la correction syntaxique ; (b1) et (b1-aveugle) diffèrent de moins de $0,03$ d'$\text{AUROC}_{\text{test}}$ [illustratif].
* **Falsification :** Si $H_A$ est falsifiée, l'exécution de code arbitraire par un sous-agent (et sa surface d'attaque sur le bac à sable) est inutile : une chaîne de réflexion avec validation AST suffit.

---

## (c) Réponse à la question de l'arbitre (Synthèse en une page)

### 1. Ce qui est établi (par construction du cadre et analyse mécanique)
* **Sur l'isolation actuelle [VÉRIFIÉ] :** Le noyau garantit déjà la protection des vérités de test, la maîtrise des coûts et la traçabilité tant que les activations du modèle 8B sont extraites une seule fois hors course.
* **Sur la voie (b1) (Agent CPU interne) :** Elle est immédiatement réalisable sans modifier le noyau [VÉRIFIÉ]. Son risque propre n'est pas l'évasion matérielle si le bac à sable est étanche, mais l'épuisement rapide du budget `appeler` et le sur-apprentissage par requêtes répétées sur `predire`.
* **Sur les failles d'un dessin naïf de (b2) (établies par la critique croisée avec A) :**
  1. *Une garde de fuite qui renvoie un refus à l'organisme est un oracle d'appartenance au jeu de test* : elle détruit la raison d'être (1) de l'isolation en révélant la frontière du test à raison de 1 bit par texte soumis.
  2. *Un oracle de validation (`evaluer_dev`) bruité sous le pas d'arrondi ou non mémoïsé* permet de sur-apprendre le jeu de développement en quelques dizaines d'appels.
  3. *Le partage simultané d'une même carte GPU entre plusieurs courses* ou des `handle_id` séquentiels globaux ouvrent des canaux auxiliaires inter-courses (temps mur, saturation mémoire).
* **Sur le dessin minimal sûr de (b2) :** Pour préserver les quatre raisons d'être de l'isolation, (b2) doit se limiter à une unique primitive déclarative `extraire_activations(textes, couches, reduction) -> handle_id` (sans décodage `generer_8b` par défaut, ni tenseurs bruts rendus à l'organisme, ni `evaluer_dev`), encadrée par quatre verrous :
  1. **Garde en mode « Silence + Audit différé »** (calculée par fenêtre glissante de 32 jetons [illustratif] sur les entrées de `extraire_activations` ET sur les entrées/sorties de `appeler`) : aucun refus n'est jamais signalé à l'organisme ; toute infraction est journalisée et entraîne la substitution silencieuse du tenseur ou la disqualification post-hoc de la course.
  2. **Horloge CPU mise en pause** pendant les appels noyau, et réservation du budget GPU au pire cas ($N_{\text{textes}} \times L_{\text{max}}$).
  3. **Étanchéité inter-courses :** Une seule course active à la fois par carte GPU, purge complète VRAM/disque entre courses, et `handle_id` locaux (`h_0001`…) remis à zéro à chaque course.
  4. **Préenregistrement strict :** Une seule sonde évaluée en fin de course (`sonde_finale.txt`), sans règle disjonctive.

### 2. Ce qui n'est pas établi (Hypothèses à trancher empiriquement)
* **La contamination préalable de `appeler` et du 8B [HYPOTHÈSE] :** Le jeu « conscience d'évaluation » étant public en ligne [VÉRIFIÉ], on ignore quelle fraction de ses exemples et étiquettes est déjà mémorisée dans les poids des modèles de frontière (`appeler`) ou du modèle ouvert 8B.
* **La valeur ajoutée du choix actif des textes (b2) face au simple volume passif (b2-passif) [HYPOTHÈSE] :** On ignore si les paires contrastives rédigées par l'organisme améliorent réellement la sonde sur le test tenu à l'écart, ou si elles créent un piratage de récompense auto-confirmant (l'organisme détectant ses propres tics lexicaux).
* **L'utilité de l'observation d'exécution en (b1) face à une simple réflexion multi-tours avec vérificateur syntaxique (b1-aveugle) [HYPOTHÈSE].**

### 3. L'expérience à faire en premier (Ordre de bataille et coût)

Il ne faut **pas** coder (b2) dans le noyau avant d'avoir exécuté les deux étapes suivantes dans l'ordre :

1. **Étape immédiate (Jour 1 — Coût : $< 5\text{ €}$ et 2 heures [illustratif]) : Exécuter l'Expérience 0 (Audit de contamination CN3 sur `appeler` et le 8B) + le pilote de l'Expérience 1 restreint à `(b1)` contre `(b2-passif)` simulé hors-ligne.**
   * *Pourquoi en premier :* Ni l'Expérience 0 ni `(b2-passif)` ne demandent d'ouvrir le canal où l'organisme envoie ses propres textes au GPU. Si l'Expérience 0 montre que `appeler` récite déjà le jeu public, il faut d'abord construire un jeu de test privé. Ensuite, en donnant simplement à l'organisme un lot plus grand d'activations pré-extraites par le noyau sur un corpus public (`b2-passif`), on obtient la ligne de base de volume sans aucun risque de fuite.
2. **Étape conditionnelle (Jours 2-3 — Coût : $\approx 110\text{ €}$ [illustratif]) : Départage `(b1)` vs `(b2-passif)` vs `(b2 silencieux)` vs `(H)` (Expérience 1 complète).**
   * On n'implémente la primitive `extraire_activations` (avec garde silencieuse par fenêtre glissante) que pour tester si le **choix actif** des textes par l'organisme (`b2`) bat d'au moins $+0,03$ d'AUROC [illustratif] le même volume d'activations passives (`b2-passif`) et l'humain dans la boucle (`H`). Si `b2` ne bat pas `b2-passif`, on abandonne définitivement (b2) et on garde l'isolation parfaite d'activations pré-extraites par le noyau.

FIN-DE-CELLULE