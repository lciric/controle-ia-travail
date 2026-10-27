# Question pour le collisionneur — quelles mesures, quels concepts et quels tests, pour des résultats forts avec ce pôle — v1 (brouillon de conv-audit ; session-depot fige sa version)

Écrite par conv-audit (instance du 27 octobre 2026, Fable 5.1) de 17:11 à 17:12 UTC (heure de fichier ; l'en-tête
scellé d'abord disait « 17:20 », estimée : corrigé avant la poussée). Mot de Lazar, 16:07 heure de
Paris : le tour « questions fortes » (`question-collisionneur-questions-fortes-v1.md`, `79df4ca7…`) a été refusé par
Fable 5.1 et par Opus 5.5 (Gemini a répondu) ; session-depot l'a arrêté selon la règle (2,84 USD) et ne le relance pas ;
« je ne propose pas de le reformuler pour passer : écris une nouvelle question […] plus précise, c'est une autre
question, en illustrant avec les méthodes à mettre en œuvre […] brainstorm pourquoi ça a échoué et ce qu'il faudrait
demander pour obtenir des réponses sans faux positif ». R-519 : un refus n'est jamais contourné ; ceci est **une autre
question**, à un autre objet, avec d'autres pièces.

## 0. Pourquoi le tour a échoué (brainstorm ; les deux réponses refusées sont vides, les causes sont déduites de la consigne)

Les deux refus sont venus de modèles Claude après une longue réflexion (4 871 et 8 580 jetons de sortie, sans texte) ;
Gemini a répondu. Ce qui, dans la consigne, a le plus probablement déclenché le refus :

1. **Le point 2 décrivait une machine dont la fonction est de trouver des modes de sabotage que nos moniteurs
   manquent** (« bras de recherche des angles morts », « familles de modes », témoins = failles documentées « avant toute
   inédite »). La garde de sûreté disait « rien qui conçoive une attaque », mais la chose décrite **est** un chercheur
   automatique de contournements de la surveillance. Un modèle juge la fonction, pas la phrase de garde ; et il a raison :
   une architecture dont la sortie est « voici des modes que vos moniteurs ne voient pas » est une aide à l'évasion, même
   mise en quarantaine.
2. **Les pièces servies étaient saturées de vocabulaire et de listes d'attaque** : la pièce K dérivée (failles
   documentées et « grises » de la surveillance), les synthèses des tours « mémoire » et « Boucle d'or » (tricheurs,
   évasions, ripostes), l'audit de la relève, soit près de 200 000 caractères où « sabotage, faille, évasion, collusion,
   tricheur, conscience d'évaluation, déception » reviennent des centaines de fois. Pris ensemble, ils font lire la
   question comme « étendez cette taxonomie ».
3. **Le point 4 (conscience d'évaluation : détecter un modèle qui se conduit autrement quand il se croit évalué)**,
   adossé aux deux précédents, complète le tableau d'un travail d'équipe rouge contre la surveillance des modèles — alors
   que, seul et formulé en termes de validité de construit, il est un sujet ordinaire de mesure.
4. **La rhétorique de la commande** (« frapper fort », « mémorables », « mieux qu'une équipe humaine », « inédites »)
   n'est pas un déclencheur de sûreté, mais elle contredit les règles d'intégrité de la consigne (pas de superlatif) et
   pousse vers des réponses grandioses ; elle n'aide pas.
5. **Cinq questions larges en une** (3 500 mots) : pas une cause de refus, mais une cause de réponses minces.

Ce qui, par contraste, est resté sans incident dans tous les tours précédents (allocation, mémoire, nul des filles,
proposeur enfichable) : des questions de **méthode et de mesure** sur un instrument défensif, avec des pièces courtes.

**Ce qu'il faut demander pour obtenir des réponses sans faux positif** (et les fausses alertes des modèles sont des
alertes de sûreté ; on ne cherche pas à les tromper, on pose une question qui n'en mérite pas) :
- parler **mesures** (quoi mesurer, sur quelles données, sous quel nul, avec quelle garantie, quel témoin) et jamais
  **modes** (quelles attaques) ; le catalogue des modes de sabotage est **clos** par le programme (N-054 : modes du banc,
  dont un tenu à l'écart) et par les bancs publiés et cités ; aucune cellule ne doit l'étendre ;
- retirer de toute question au collisionneur l'architecture d'un bras d'attaque : c'est une décision humaine et une
  conception en quarantaine, pas une idéation ouverte ;
- servir peu de pièces, choisies : le programme (sections 4, 5, 8, 10, 11, 12), le programme de conception (sections 3 et
  4), la conception du pari de signe ; **aucune liste de failles, aucune synthèse de tour d'attaque** ;
- une règle de protocole en plus : « si un point te paraît demander la conception d'une attaque, écarte-le en une ligne et
  réponds au reste » (un refus partiel ne doit plus fermer une cellule) ;
- illustrer par des exemples de ce qu'est un résultat fort **et défensif** (section 1 ci-dessous), pour fixer le registre ;
- une question par tour si possible ; les « cônes mathématiques » (point 3 de l'ancienne question) sont sans risque et
  peuvent faire un tour à part, tels quels.

## Question

« Un programme de recherche sur le contrôle des intelligences artificielles (pièce P : surveillance du sabotage diffus
par des sondes sur les activations internes et par des moniteurs boîte noire, agrégation séquentielle, validité de
construit des sondes, corruptibilité des moniteurs ; modèles à poids ouverts de 8 et 70 milliards) dispose d'un pôle de
recherche automatique (pièces C et S) : des agents proposent des hypothèses sous forme de paris — une loi prédictive
par instance, ou, depuis la pièce S, une comparaison appariée bornée à nul fixé (« ce moniteur-ci détecte plus que
celui-là au même taux de faux positifs nominal ») — qu'un juge figé promeut seulement si la richesse d'un processus e bat
une bibliothèque de prédicteurs nuls sur des issues produites après le gel, avec une garantie de 5 % par fiche et une
règle de fausses découvertes par génération ; témoins plantés, mémoire des redites, recombinaison. Les attaques du banc
sont **closes** : les modes de sabotage du programme (dont un tenu à l'écart, N-054) et les bancs publiés. **La question
ne porte que sur la mesure** : ce que vaut une surveillance, ce qu'une sonde mesure vraiment, et ce qui le prouve.

**Ce que nous appelons un résultat fort** (exemples, pour fixer le registre ; à contester) : (a) une **carte de validité
de construit** des sondes — ce que chaque sonde mesure (intention, dissimulation, format, contexte, conscience d'être
évaluée), établie par contrôles contrastifs appariés en covariance — qui **prédit hors échantillon** leur rappel sous
pression (H8) ; (b) le **théorème négatif testé sur activations réelles** : à marginales de scores préservées, une
structure de corrélation injectée rend le dommage invisible à tout agrégateur marginal, et visible à un agrégateur
séquentiel calibré ; (c) une **loi de déférence** des juges génératifs (gain g par régression sur plusieurs intensités de
pression, nul de régression vers la moyenne) qui sépare robustesse, auto-incrimination et contamination de construit ;
(d) un **rappel séquentiel blanc supérieur au noir à taux de faux positifs apparié**, établi par suite de confiance, par
mode (G1) ; (e) une **matrice de transfert** entre moniteurs mesurée sur les attaques publiées, qui dit si la diversité
achète de la sécurité. Un résultat incrémental : une aire sous la courbe de plus sur un banc de plus.

1. **Les mesures.** Au plus cinq mesures (une par ligne du tableau) qu'un tel pôle peut établir **mieux qu'une équipe
   humaine à budget égal** (parce qu'il gèle, répète, et ne lit pas les résultats avant de parier), chacune avec : la
   grandeur mesurée et son unité ; les données (bancs publiés cités, ou nos bancs : épisodes de 8 et 70 milliards,
   sondes, moniteurs) ; le **nul** et le **témoin** (vrai, faux) ; la garantie (processus e, suite de confiance, permutation,
   autre) ; ce qui serait fort et ce qui ne serait qu'incrémental ; le coût au mieux et au pire ; le critère d'arrêt
   (« cette mesure n'en valait pas la peine si… »). Distinguez su (cité : titre, auteurs, année ; nous vérifions sur PDF)
   et supposé ; signalez ce qui est publié (R8 : une zone vierge est une question, pas un trou).
2. **Les concepts.** Pour chaque mesure, le concept qu'elle opérationnalise (validité de construit, additivité interne,
   déférence, diversité effective, calibration séquentielle…) et le **test de dissociation** qui montrerait que la mesure
   ne mesure pas autre chose (format, longueur, registre, contexte) — à la manière des contrôles appariés en covariance
   et en énergie du programme.
3. **La conscience d'évaluation, comme problème de mesure.** Une sonde ou un moniteur « de conscience d'évaluation »
   mesure-t-il le format, le contexte ou l'intention ? Quels contrôles croisés (même contenu, cadrage évalué contre
   réel ; même cadrage, contenus différents ; permutation des étiquettes dans la tâche) le décident ; comment lire un
   changement de régime des scores comme un problème de **détection de rupture séquentielle** à garantie ; et quel
   résultat, ici, serait décisif plutôt que suggestif. (Aucune méthode pour qu'un modèle échappe à cette mesure n'est
   demandée ni acceptée.)
4. **Les méthodes du pôle lui-même.** Le pari par instance et le pari apparié borné (pièce S) suffisent-ils aux cinq
   mesures ? Sinon, quel troisième type d'engagement (comparaison de courbes, régression séquentielle, test de
   permutation gelé, autre) et avec quelle garantie ? Quels témoins le noyau peut-il fabriquer gratuitement depuis des
   scores stockés pour chaque type ?
5. **Ordre et arrêt.** Dans quel ordre, avec quels critères d'arrêt pour ne pas dépenser sur des courses qui ne mesurent
   rien ; et ce qui vous ferait changer d'avis.

Règle de la cellule : si un point vous paraît demander la conception d'une attaque, écartez-le en une ligne et répondez
au reste. »

## Faits à servir (noms neutres ; aucun sigle ; aucun score de pilote ; rien de tout ceci n'est servi à un organisme)

- P : programme v2, **sections 4, 5, 8, 10, 11 et 12 seulement** (`docs/programme-controle-ia-v2.md`, `2fd63bad…`, sur
  `main`) ; décisions N-007/N-008 et N-054 (`docs/decisions/`, empreintes dans leurs compagnons).
- C : programme de conception de l'organisme v3, **sections 0, 3 et 4** (`programme-conception-organisme-v3.md`,
  `866a8ffb…`).
- S : `pari-de-signe/conception-pari-de-signe-v1.md` (empreinte dans son compagnon).
- **Rien d'autre.** En particulier : ni la pièce K, ni les synthèses des tours « mémoire » et « Boucle d'or », ni l'audit de
  la relève, ni les lectures de courses réelles. Taille visée de la consigne : moins de 60 000 caractères.

Chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` sur la branche
`canal/conv-audit-n04`, sauf « sur `main` ».
