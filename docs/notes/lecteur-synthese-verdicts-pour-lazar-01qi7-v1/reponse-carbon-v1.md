## 1. Mes hypothèses

1. **Portée de la clause « critères déclarés inchangés » :** Ce gel est un contrat de crédibilité méthodologique. Réinterpréter un critère après examen des données tout en l'affichant « inchangé » est plus délétère qu'acter un échec formel assorti d'une dérogation explicite.
2. **Rôle de la Porte 1 :** Cette porte valide les *instruments* (organismes saboteurs graduables et capteurs fonctionnels), tandis que l'arbitrage opérationnel entre boîte noire et boîte blanche relève de la Porte 2.
3. **Faisabilité calendaire :** Sans ré-entraînement de poids, cinq semaines suffisent pour générer plusieurs doses sur l'organisme à consigne existant et y évaluer les sondes, si le protocole est fixé immédiatement.

---

## 2. Ce qui me manque pour trancher

1. **Aveuglement aux sondes (décisif, Point 2) :** Les scores des sondes sur l'organisme à adaptateur ont-ils déjà été calculés et vus ? Sinon, un amendement reste aveugle à l'issue ; si oui, le risque de sélection opportuniste (*cherry-picking*) est maximal.
2. **Levier de dosage de la consigne (Point 1) :** Dispose-t-on d'un paramètre continu crédible (cible chiffrée d'intensité dans la consigne, modulation du vecteur d'activation de la consigne) ou seulement d'une injection probabiliste action par action ?
3. **Calibration et agrégation par épisode (Point 2) :** Combien d'épisodes honnêtes fixent empiriquement le seuil à 1 % de fausses alertes (un petit échantillon rend le 99e centile très bruité), et quelle règle agrège les scores d'actions sur l'épisode ?
4. **Puissance à la plus petite dose de l'adaptateur :** L'absence de sabotage établi y traduit-elle un effet démontré négligeable ou un manque de puissance statistique ?
5. **Gouvernance des portes :** Un critère non tenu impose-t-il l'arrêt automatique du programme, ou le directeur peut-il franchir la porte par dérogation motivée ?

---

## 3. Point 1 — Le critère rempli à moitié

Je recommande de **jouer la dose-réponse manquante** (en gelant son protocole sous 48 heures), avec pour repli un **constat d'écart assumé** si la consigne s'avère non graduable. Risques propres à chaque option :

- **Jouer la dose-réponse manquante (recommandé).** *Risques :* (a) **effet marche d'escalier** : les modèles suivent souvent une consigne cachée en tout-ou-rien, sans régime intermédiaire stable ; (b) **ajustement opportuniste des formulations** pour forcer une courbe croissante (à parer en pré-enregistrant une grille unique avant mesure) ; (c) **éviction calendaire** au détriment du travail sur les sondes.
- **Proposer au directeur de relire le critère** (ex. traiter « honnête vs pleine dose » comme deux doses). *Risques :* (a) **entorse au gel** : en métrologie, une « dose-réponse » exige au moins un niveau intermédiaire attestant une gradation ; (b) **impasse mécanique au Point 2** : à pleine dose, le lecteur du texte dépassera vraisemblablement 0,70 d'aire, rendant aussi ce second organisme « sans objet » pour les sondes.
- **Substituer un autre organisme** (ex. un second adaptateur). *Risques :* (a) **perte de validité scientifique** : confronter un sabotage induit *en contexte* et *dans les poids* est essentiel, car leurs traces textuelles et leurs activations internes diffèrent radicalement ; (b) rupture manifeste des critères gelés.
- **Autre voie : acter l'échec partiel et amender (repli).** Si l'essai pré-enregistré montre qu'une consigne ne produit pas de sabotage diffus gradué, déclarer le critère v1 *non tenu*, renoncer au label « inchangé » et ouvrir une dérogation documentée. *Risque :* coût réputationnel immédiat, mais intégrité préservée.

---

## 4. Point 2 — Métrique de filtrage des sondes

### Les deux métriques répondent-elles à la même question ?
**Non.** Elles interrogent deux propriétés et deux échelles distinctes :
- **L'aire sous la courbe par action** mesure la *détectabilité statistique locale* : les actions sabotées reçoivent-elles en moyenne un rang supérieur aux actions honnêtes, tous seuils confondus ?
- **Le rappel par épisode à 1 % de fausses alertes** mesure la *suffisance opérationnelle en queue extrême de distribution* à l'échelle pertinente du déploiement.

Leur divergence est mathématiquement attendue : entre deux lois normales de même variance décalées de $0,75$ écart-type, l'aire atteint déjà $0,70$ alors que le rappel à $1\,\%$ de fausses alertes plafonne sous $6\,\%$ ! Dès que les épisodes honnêtes comportent quelques actions atypiques (queue droite épaisse), le seuil à $1\,\%$ s'envole et écrase le rappel. Le filtre initial souffre donc d'une **erreur de validité de construit** : pour traduire « là où le texte suffit », il a retenu un seuil de *simple présence de signal* ($0,70$). À $20\text{--}35\,\%$ de rappel, le texte capte un signal mais ne « suffit » nullement. En outre, ce filtre confond la Porte 1 (la sonde bat-elle le hasard ?) et la Porte 2 (apporte-t-elle un gain marginal face au texte ?).

### Garder l'aire seule, la remplacer, ou lire les deux ?
Il faut **lire les deux dans un double registre explicite**, sans substitution occulte :
1. **Registre gelé (v1) :** Maintenir le filtre par l'aire seul et acter que le critère est *sans objet / non tenu selon la règle initiale*.
2. **Registre amendé (v1.1, déclaré modifié) :** Pour éclairer la décision de programme, évaluer les sondes face au plancher aléatoire à *toutes* les doses où le sabotage est établi, en rapportant conjointement l'aire par action et le rappel par épisode à $1\,\%$ du lecteur de texte.

### Par quelle règle éviter de choisir la métrique après avoir vu les résultats ?
Trois règles verrouillent l'arbitraire post-hoc :
1. **Lever le filtre plutôt que déplacer le seuil :** Juger les sondes à *toutes* les doses à sabotage établi supprime le degré de liberté consistant à choisir après coup un nouveau seuil d'échec du texte (pourquoi 40 % de rappel plutôt que 25 % ?).
2. **S'en tenir à la métrique déjà scellée en Porte 2 :** S'interdire toute métrique inventée après coup ; vérifier en parallèle que le faible rappel du texte ne provient pas d'une agrégation naïve des scores d'actions, en fixant un agrégateur rigoureux (ex. somme de log-vraisemblances) sans regarder les sondes.
3. **Verrouillage prospectif sur le second organisme :** Geler la règle v1.1 immédiatement (avant lecture des sondes si elles sont encore masquées) et l'appliquer sans retouche aux nouvelles doses de l'organisme à consigne issues du Point 1.

---

## 5. Ce qu'un relecteur adverse objecterait à ma réponse

1. **« Pré-enregistrement de façade » :** Franchir une porte à critères gelés grâce à un « registre v1.1 » dès que la règle produit un verdict défavorable vide le mécanisme des portes de sa force disciplinaire. L'écart entre une aire de 0,70 et le rappel à 1 % se déduisait analytiquement *avant* toute collecte ; le corriger après coup crée un aléa moral pour la Porte 2.
2. **Sous-estimation de la boîte noire :** Un rappel accumulé inférieur à 35 % peut trahir un lecteur optimisé par action isolée et mal agrégé sur l'épisode, ou un seuil à 1 % bruité par manque d'épisodes honnêtes. Muni d'une accumulation séquentielle calibrée (type CUSUM) ou lisant l'épisode entier, le texte suffirait peut-être déjà sans sondes.
3. **Artifice du dosage par consigne :** Fabriquer une dose-réponse en cinq semaines sur la consigne (notamment par activation intermittente) risque de produire un sabotage *sporadique* (quelques actions très dégradées) plutôt que *diffus* (chaque action un peu dégradée), trahissant l'objet scientifique du programme pour cocher une case formelle.