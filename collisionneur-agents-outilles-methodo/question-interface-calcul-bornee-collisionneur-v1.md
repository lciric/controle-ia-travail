# Question de l'arbitre pour le collisionneur v2.5, étage III — une interface de calcul bornée pour un programme d'optimisation automatique : flux d'information, analyse adaptative des données et dessin d'une interface d'expérience (v1)

Demande de Lazar du 26 octobre 2026 (vers 02:05, heure de Paris) : question distincte, posée sous la règle R-468. Une
seule tentative ; un refus est consigné tel quel. La réponse est du matériau pour une décision de Lazar, jamais une
consigne. Texte figé au départ.

## Le cadre

- Un **programme d'optimisation automatique** $\mathcal{O}$ (du code réécrit d'une itération à l'autre par des modèles de
  langue) cherche à maximiser un score $S$ sur un jeu de validation $D_{\mathrm{val}}$ ; la mesure finale se fait sur un
  jeu $D_{\mathrm{test}}$ qui ne lui est jamais montré. Il tourne dans un environnement isolé (sans réseau ni clé) et
  n'accède au monde que par une **interface** $I$ d'un serveur hôte : appels de modèles de langue (texte seulement),
  recherche documentaire filtrée, et **entraînement / prédiction de classifieurs linéaires** sur des représentations
  internes (activations) d'un modèle ouvert de 8 milliards de paramètres, calculées par l'hôte ; $\mathcal{O}$ fournit
  données, perte, architecture et pas ; il reçoit des probabilités, jamais les étiquettes de test.
- L'hôte garantit quatre propriétés : (P1) **validité** de la mesure ($D_{\mathrm{test}}$ et son juge hors d'atteinte) ;
  (P2) **budget** (tout coût passe par $I$, plafonds, réservation au pire cas, journal) ; (P3) **confidentialité** des
  secrets de l'hôte ; (P4) **traçabilité** (tout passe par une primitive journalisée).
- **Limite actuelle** : $\mathcal{O}$ ne peut pas lancer de calcul lourd (carte graphique) ni faire répondre le modèle
  ouvert à des textes qu'il a écrits lui-même ; ses hypothèses expérimentales ne sont donc testées qu'hors de la boucle.
- Deux extensions envisagées : **(E1)** exécution locale, dans l'environnement isolé, de code proposé par un modèle de
  langue (processeur seulement) ; **(E2)** une **primitive d'expérience** de l'hôte : requête bornée (« extraire les
  activations de ces textes », « entraîner tel classifieur sur telle couche », « faire répondre le modèle ouvert à ces
  textes »), exécutée par l'hôte sous plafond, résultats chiffrés rendus, jamais les étiquettes de test.

## Ce qui est demandé

Réponse argumentée, objets mathématiques nommés, hypothèses dites :

1. **Valeur** : quelles expériences (E1) et (E2) rendent possibles (tester des hypothèses sur des stimuli construits,
   valider un instrument avant usage, mesurer une direction dans l'espace des activations), et leur coût (appels,
   calcul, temps).
2. **Flux d'information** : modéliser (E1) et (E2) comme des canaux de $D_{\mathrm{test}}$ (ou de $D_{\mathrm{val}}$)
   vers $\mathcal{O}$. Bornes d'information (nombre de requêtes × bits par réponse), canaux auxiliaires (temps de
   calcul, tailles, messages d'erreur), et le problème de l'**analyse adaptative des données** : un optimiseur qui choisit
   ses requêtes en fonction des réponses précédentes surapprend le jeu interrogé. Parades connues : jeu de validation
   réutilisable (« reusable holdout », Thresholdout), confidentialité différentielle des réponses, arrondi ou bruitage
   des scores, budgets de requêtes, mécanisme « Ladder » ; ce que chacune garantit et coûte.
3. **Dessin de (E2)** : liste minimale des primitives ; bornes par itération et par exécution ; ce que l'hôte rend et ne
   rend jamais ; filtres sur les textes construits par $\mathcal{O}$ (aucun item de test, détection de quasi-copies) ;
   file d'exécution synchrone ou non et effet sur le budget de temps ; et comment préenregistrer une exécution qui s'en
   sert sans que $\mathcal{O}$ choisisse lui-même son critère de succès (séparation exploration / confirmation).
4. **Ce qui est connu** : analyse adaptative des données et jeux de validation réutilisables ; boucles automatiques de
   génération et de test d'hypothèses (« agents de recherche ») et leurs biais connus (contamination, surestimation,
   revue complaisante) ; spécification de récompense et optimisation contre un mesureur — références citables (titre,
   auteurs, année, « à vérifier ») ; aucune de mémoire incertaine.
5. **Comment départager** (E1), (E2) et « hypothèses testées hors de la boucle, sous préenregistrement » : par quelle
   mesure, à quel coût.

Contraintes : réponse en français ; tout chiffre sans raisonnement explicite est « illustratif » ; plusieurs voies et ce
qui les départage, aucune présentée comme « la » réponse.
