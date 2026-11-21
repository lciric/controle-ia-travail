# Réponse brute — claude-opus-4-6

- Modèle demandé : claude-opus-4-6
- Heure (date -u) : Sat Nov 21 18:16:17 UTC 2026
- Réglages : plafond de sortie 32000, réflexion adaptative
- Question : question-servie-v1.md, précédée de « Réponds en français. »
- Modèle servi : claude-opus-4-6
- Clé (nom) : RR_ANTHROPIC_API_KEY_LUC
- Jetons facturés : entrée 2221, sortie 30848 (réflexion comprise)
- Coût estimé : 0.7823 dollars (tarif 5.0 / 25.0 dollars par million, relance comprise)
- Motif d'arrêt : end_turn
- Journal :
  - envoi unique

---

# Vérifier le recouvrement de deux objets secrets sans dévoiler l'un à ceux qui ne doivent pas le connaître

---

## 1. Ce que « recouvrir » doit vouloir dire

### Définition fonctionnelle

Le but du secret S est de tester si les moniteurs **généralisent** au-delà de ce pour quoi ils ont été conçus. Le critère de recouvrement doit donc être lié à ce but. Je propose la définition suivante :

> **F recouvre S** si un concepteur de moniteur qui connaît F — et qui sait que F recouvre S — pourrait, avec un effort raisonnable, construire un moniteur qui détecte S mieux qu'un concepteur qui ne connaît pas F.

Cette définition est **causale et contrefactuelle** : elle demande si la connaissance de F fournit un avantage actionnable pour détecter S. Elle se décompose en trois sous-critères, dont chacun suffit :

1. **Recouvrement mécaniste.** F et S décrivent le même mécanisme de nuisance (par exemple, les deux reposent sur une exfiltration de données par stéganographie dans les sorties du modèle).
2. **Recouvrement de signature.** Les traces observables que F et S laissent dans ce qu'un moniteur lit (journaux, sorties, appels, etc.) sont suffisamment semblables pour qu'un détecteur ajusté sur F capte aussi S.
3. **Recouvrement stratégique.** F et S exploitent la même lacune ou le même angle mort dans les approches de surveillance, de sorte que colmater la lacune de F colmate aussi celle de S.

Le recouvrement n'est pas l'identité textuelle ; ce n'est pas non plus l'inclusion ensembliste au sens strict. C'est une **relation fonctionnelle** : « connaître F aide-t-il à détecter S ? »

### Peut-on s'affranchir du jugement ?

Plusieurs substituts formels sont envisageables, mais chacun a un prix :

| Substitut | Principe | Limite principale |
|-----------|----------|-------------------|
| Similarité cosinus de plongements vectoriels | Plonger S et F avec un modèle fixe, mesurer la distance | Manque le recouvrement fonctionnel (deux descriptions avec un vocabulaire différent pour le même mécanisme peuvent avoir une faible similarité, et inversement) |
| Extraction de mots-clés et indice de Jaccard | Comparer les concepts extraits | Trop grossier ; sensible à la paraphrase |
| Décomposition en arbre d'attaque | Décomposer S et F en arbres (objectif → sous-objectifs → actions), comparer les structures | La décomposition exige elle-même un jugement expert ; elle n'élimine pas le problème |
| Vecteur d'attributs sur une taxinomie fixe | Remplir indépendamment un vecteur d'attributs pour S et pour F, comparer les vecteurs | La taxinomie peut ne pas capturer les dimensions pertinentes ; perte d'information ; le vecteur d'attributs de S est lui-même une fuite partielle |
| Simulation par équipe rouge | Construire un moniteur pour F, tester s'il détecte aussi S | Circulaire : un résultat négatif peut simplement refléter un moniteur mal conçu |

**Conclusion.** Aucun de ces substituts ne remplace de façon fiable le jugement sémantique sur deux textes en langage naturel. On peut les utiliser comme **filtre préalable** (si la similarité de plongements est inférieure à un seuil très bas, on peut libérer F sans jugement humain ou de modèle de langage), mais le jugement reste nécessaire dans la zone intermédiaire. Le coût de cette irréductibilité est qu'au moins une entité doit lire les deux textes, ce qui est le nœud de tout ce qui suit.

---

## 2. Qui peut juger

### Conditions nécessaires

Toute entité qui juge doit :

**(a)** avoir accès au texte intégral de S et de F ;

**(b)** être capable de porter un jugement sémantique fiable sur le recouvrement (au sens défini ci-dessus) ;

**(c)** ne pas être en mesure, après le jugement, de transmettre de l'information sur S à quiconque participe à la conception des moniteurs ou alimente les générateurs d'idées.

La condition (c) est la plus contraignante. Examinons les types de juges possibles :

**Instance neuve de modèle de langage.** On lance une instance avec un contexte contenant S, F et les critères de jugement, et rien d'autre. L'instance produit un verdict. Son contexte est ensuite détruit. L'instance satisfait (c) au sens strict : après destruction, elle ne « sait » plus rien. Mais tout ce qu'elle a écrit persiste : le fichier contenant le verdict et l'argumentaire existe et doit être protégé. Le destinataire du verdict (le gardien de S) doit être choisi avec soin.

**Personne humaine.** Une personne qui lit les deux textes conserve S en mémoire indéfiniment. Elle doit donc être **écartée de tout rôle** lié à la conception, l'évaluation ou l'alimentation des moniteurs — y compris les rôles de conseil, de relecture et de conversation informelle — tant que S reste un secret. Dans un programme de petite taille, cela peut être très coûteux. Si la personne est le concepteur originel de S (le « gardien de S »), elle est déjà écartée : lire F ne lui impose aucune contrainte nouvelle, pourvu qu'elle ne transmette rien de F aux concepteurs de moniteurs.

**Plusieurs juges indépendants.** Plusieurs instances neuves, ou une instance et un humain, jugent séparément. Les verdicts sont agrégés (vote majoritaire, unanimité, etc.). Cela augmente la fiabilité mais multiplie les entités qui connaissent les deux textes. Si les juges sont des instances éphémères, ce coût est faible.

**Tiers extérieur au programme.** Un expert indépendant pourrait juger, mais il devrait être écarté du programme ensuite, ce qui est difficile à imposer. Il faudrait un engagement contractuel et une confiance forte. Dans un programme de recherche ouvert, cela peut être impraticable.

### Recommandation sur le juge

Le meilleur compromis est : **le gardien de S reçoit le verdict d'une ou plusieurs instances éphémères, et c'est le gardien — qui connaît déjà S — qui décide de l'action**. Le gardien lit F au passage (inévitable puisqu'il manipule le fichier), mais c'est le seul humain supplémentaire exposé aux deux objets. L'instance est détruite ; le gardien est déjà mis à l'écart.

**Quarantaine post-jugement :**
- Pour les instances : destruction du contexte, rien à faire de plus.
- Pour le gardien : maintien de l'écart par rapport à la conception des moniteurs, jusqu'à l'évaluation finale. Durée : la durée de vie du secret S.
- Pour tout juge humain qui ne serait pas le gardien : écart complet du programme, ou au minimum écart de tout ce qui touche aux moniteurs, pour la même durée.

---

## 3. Ce que le verdict laisse fuir

### Analyse informationnelle

Modélisons. Soit Ω l'espace des secrets possibles (l'ensemble des descriptions de menaces que le concepteur de S aurait pu choisir). Avant tout verdict, un observateur qui connaît F a une distribution a priori P(S) sur Ω. Après avoir appris le verdict v ∈ {recouvre, ne recouvre pas}, l'observateur met à jour :

P(S | v, F) ∝ P(v | S, F) · P(S)

- Si v = « recouvre » : la distribution se concentre sur la région de Ω compatible avec F. Si F est étroit, cela identifie S à peu de chose près. **C'est une fuite potentiellement catastrophique.**
- Si v = « ne recouvre pas » : la distribution exclut la région de F. C'est une fuite modérée (information négative), d'autant moins grave que F est étroit.

La quantité d'information divulguée est bornée par l'entropie mutuelle I(S ; v | F), qui vaut au plus 1 bit par verdict binaire. Mais la **sémantique** compte : 1 bit qui dit « S concerne l'exfiltration stéganographique » vaut bien plus qu'1 bit qui dit « S n'est pas un déni de service ».

### Fuite par l'action, pas seulement par le mot

Le problème est plus profond : le verdict n'est pas seulement un mot, c'est une **action observable**. Si F est libérée, le proposant de F déduit que F ne recouvre pas S. Si F est mise en réserve, il soupçonne un recouvrement. L'action est la fuite principale.

### Réserve aléatoire (randomisation de la réponse)

Pour brouiller l'inférence, on peut **mettre en réserve aléatoirement des familles qui ne recouvrent pas S**. Soit p la probabilité de mise en réserve aléatoire. Alors :

- P(libérée | recouvre) = 0 (jamais de libération d'un vrai recouvrement)
- P(libérée | ne recouvre pas) = 1 − p
- P(réserve | recouvre) = 1
- P(réserve | ne recouvre pas) = p

Inférence du proposant après observation de la réserve :

P(recouvre | réserve) = π / (π + p(1 − π))

où π est le taux de base de recouvrement (fraction a priori des familles qui recouvrent S).

| π (taux de base) | p (réserve aléatoire) | P(recouvre \| réserve) |
|---|---|---|
| 5 % | 20 % | ≈ 21 % |
| 5 % | 30 % | ≈ 15 % |
| 10 % | 30 % | ≈ 27 % |
| 10 % | 50 % | ≈ 18 % |

Avec p = 30 % et π = 5 %, un proposant dont la famille est en réserve ne peut attribuer qu'environ 15 % de probabilité au recouvrement. C'est une fuite substantiellement réduite par rapport au cas sans randomisation (où la réserve impliquerait le recouvrement avec quasi-certitude).

**Mais la libération reste parfaitement informative** : si F est libérée, le proposant sait avec certitude que F ne recouvre pas S. Cette fuite négative est inévitable dans tout protocole qui libère effectivement des familles. Elle est tolérable si F est étroit (l'exclusion d'une petite région est peu informative) et si peu de familles sont libérées par rapport à la taille de Ω.

### Cumul sur plusieurs demandes

Après k demandes avec des familles F₁, …, Fₖ, l'information cumulée est au plus k bits (en l'absence de randomisation), et environ k · H(p) bits en présence de randomisation avec taux p, où H(p) est l'entropie binaire. Si les familles sont soumises par des proposants différents qui ne communiquent pas, chacun n'apprend qu'un seul bit. Si un même adversaire soumet k familles, il apprend jusqu'à k bits et peut **trianguler** : il couvre systématiquement des régions distinctes de l'espace Ω pour cerner S par exclusion.

**Parades :**
- **Quota de demandes** : limiter le nombre total de familles soumises à la vérification (par exemple, au plus k = 5 sur la durée du programme).
- **Regroupement (batch)** : traiter m familles ensemble et ne donner qu'un seul verdict (« au moins une recouvre » / « aucune ne recouvre »). La fuite est au plus 1 bit pour m familles, mais le verdict est moins utile.
- **Délai uniforme** : ne donner aucune réponse avant une date fixe, à laquelle toutes les familles en attente sont traitées en un lot. Cela empêche la triangulation adaptative.
- **Réserve aléatoire** (décrite ci-dessus) : réduit l'information par verdict, mais ne l'annule pas.

### Fuite résiduelle

Quelle que soit la parade, il reste une fuite : le programme agit différemment en présence de recouvrement et en l'absence de recouvrement, et cette différence est en principe observable. La seule façon d'annuler la fuite est de ne jamais agir différemment — c'est-à-dire de ne jamais vérifier (voir la question 6). Toute vérification fuit ; la question est de borner et de rendre tolérable cette fuite.

---

## 4. Aveuglement et témoins plantés

### Principe

Pour calibrer la fiabilité du juge, on intercale des **leurres** (objets dont la réponse est connue d'avance) parmi les objets réels, sans que le juge sache lesquels sont des leurres.

### Types de leurres

**Leurres positifs (recouvrement connu).** Des familles construites pour recouvrir S. Seul le gardien de S peut les fabriquer, puisqu'il faut connaître S pour en créer une variante voisine. Ces leurres sont eux-mêmes des quasi-fuites de S : s'ils tombent entre de mauvaises mains, ils révèlent partiellement S. Ils doivent être traités avec le même niveau de secret que S et détruits après le jugement.

**Leurres négatifs (non-recouvrement connu).** Des familles clairement étrangères à S. N'importe qui peut les créer (par exemple, en puisant dans un domaine manifestement différent), et le gardien de S vérifie brièvement qu'il n'y a pas de recouvrement inattendu. Le risque de fuite est faible.

### Protocole de calibration

1. Le gardien de S prépare n₊ leurres positifs et n₋ leurres négatifs.
2. Ces leurres sont mélangés avec la vraie famille F, dans un ordre aléatoire. Soit N = 1 + n₊ + n₋ le nombre total d'objets.
3. Le juge (instance neuve) reçoit S et les N familles, et produit un verdict pour chacune.
4. Le gardien évalue la performance du juge sur les leurres :
   - **Sensibilité** : fraction des leurres positifs correctement jugés « recouvre ».
   - **Spécificité** : fraction des leurres négatifs correctement jugés « ne recouvre pas ».
5. Si la sensibilité et la spécificité sont au-dessus des seuils fixés, le verdict sur F est accepté. Sinon, une nouvelle instance est lancée (nouveau juge).

### Fabrication des leurres sans fuite

Le gardien crée les leurres positifs en dérivant de S des variantes paraphrasées, particularisées ou généralisées. Ces variantes ne quittent jamais l'environnement sécurisé du gardien : elles sont injectées dans le contexte de l'instance-juge et détruites avec ce contexte. Aucun fichier persistant ne les contient en dehors du poste du gardien.

Les leurres négatifs peuvent être tirés d'une base publique de familles de menaces sans rapport avec S.

### Taux d'erreur tolérables

Les deux erreurs n'ont pas le même coût :

| Erreur | Signification | Conséquence | Tolérance |
|--------|---------------|-------------|-----------|
| Faux négatif | Le juge dit « ne recouvre pas » alors que F recouvre S | F est libérée, S est compromis, l'évaluation perd sa valeur | **Très faible** (≤ 5 %, idéalement 0 %) |
| Faux positif | Le juge dit « recouvre » alors que F ne recouvre pas S | F est mise en réserve inutilement, le travail est retardé | **Modérée** (≤ 25 %) |

L'asymétrie est forte : un seul faux négatif peut invalider des mois de travail. On doit donc **errer du côté de la prudence** (déclarer le recouvrement en cas de doute). Cela revient à privilégier la sensibilité au détriment de la spécificité.

### Puissance statistique

Avec n₊ = 2 leurres positifs, on ne peut distinguer un taux de faux négatifs de 0 % d'un taux de 50 % qu'avec une probabilité modeste. Pour une calibration solide, il faudrait n₊ ≥ 5-10, ce qui oblige le gardien à créer autant de variantes de S — un travail non négligeable et un risque de fuite accru. Un compromis raisonnable : **pré-calibrer** la consigne de jugement sur un ensemble de paires de textes de menaces sans rapport avec S (par exemple, des paires tirées de taxinomies publiques d'attaques, avec recouvrement annoté), puis utiliser 2-3 leurres liés à S pour vérification finale.

---

## 5. Que faire de F ensuite

### Cas 1 : F recouvre S

**Option A — Mise sous scellé jusqu'à l'évaluation finale.** F est scellée (empreinte enregistrée), inaccessible à quiconque sauf au gardien de S. Après l'évaluation finale, F est libérée et peut alimenter le travail courant. Le proposant de F est informé : « F est en réserve opérationnelle jusqu'à [date estimée]. »

**Option B — Absorption comme second secret.** F rejoint S comme second objet d'évaluation. Le proposant de F doit alors être **écarté** de la conception des moniteurs, ce qui peut être coûteux s'il y participe déjà. L'évaluation finale teste les moniteurs contre S et contre F.

**Option C — Substitution du secret.** S est retiré et remplacé par F (ou par un nouveau secret S' conçu par le gardien). L'ancien S est libéré. F, devenu le nouveau secret, est scellé. Avantage : l'ancien S peut alimenter le travail courant. Inconvénient : il faut que F soit un bon secret (suffisamment distinct de tout ce qui est connu), et le proposant de F doit être écarté.

**Option D — Rafraîchissement.** Le gardien conçoit un nouveau secret S' qui ne recouvre ni F ni aucune famille déjà libérée. L'ancien S et F sont tous deux libérés. Avantage : rien n'est bloqué. Inconvénient : l'espace des secrets possibles rétrécit ; il faut du temps pour concevoir S' ; S' doit être scellé à nouveau.

**Ce qu'il faut dire, et à qui.** Au proposant de F : « F est en réserve opérationnelle. » Pas de mention du recouvrement (la réserve aléatoire rend la raison ambiguë). Aux concepteurs de moniteurs : rien. Dans les résultats d'un banc d'essai auquel F manque : « Ce banc d'essai comporte une lacune connue portant sur [catégorie abstraite, si possible sans rapport direct avec S]. Cette lacune est due à une réserve opérationnelle et sera comblée à [date estimée ou "à l'issue de l'évaluation finale"]. »

### Cas 2 : F ne recouvre pas S

F est libérée. Le proposant peut l'utiliser dans les générateurs d'idées et les bancs d'essai. Aucune restriction supplémentaire.

**Risque résiduel :** la libération elle-même informe le proposant que F ne recouvre pas S (voir section 3). Ce risque est toléré car l'information négative est peu actionnable.

### Cas 3 : le juge ne tranche pas

Par prudence, **F est mise en réserve par défaut**. On peut tenter un second jugement avec un juge différent (nouvelle instance, ou humain). Après un nombre fixé de tentatives sans convergence (par exemple trois), la réserve est maintenue. La communication au proposant est la même que dans le cas 1 : « réserve opérationnelle ».

### Invisibilité du verdict dans l'action

Pour que l'action ne dévoile pas le verdict, il faut que **la réserve ne soit pas corrélée de façon déterministe au recouvrement**. La réserve aléatoire (section 3) fournit cette propriété. L'annonce d'un taux de réserve attendu (par exemple « environ 30 % des familles soumises seront mises en réserve, pour des raisons pouvant être opérationnelles ou aléatoires ») permet aux proposants de savoir à quoi s'attendre sans rien apprendre du verdict.

---

## 6. Faut-il seulement vérifier ?

### Alternatives sans vérification

| Stratégie | Principe | Avantage | Coût |
|-----------|----------|----------|------|
| **Réserve totale** | Mettre en réserve toute famille nouvelle jusqu'à l'évaluation finale | Fuite nulle | Tout le travail qui dépend de familles nouvelles est bloqué ; les moniteurs et les bancs d'essai n'évoluent plus |
| **Aucune réserve, rafraîchissement du secret** | Libérer toute famille ; juste avant l'évaluation, le gardien vérifie si S est compromis et, le cas échéant, conçoit un nouveau S' | Aucune famille n'est bloquée | Le gardien doit connaître toutes les familles libérées ; S' doit éviter toutes ces familles, ce qui peut être difficile si l'espace est petit ; S' est conçu dans l'urgence |
| **Réserve aléatoire sans vérification** | Mettre en réserve une fraction aléatoire (par ex. 30 %) des familles, sans examiner le recouvrement | Simple ; fuite nulle (la réserve est indépendante de S) | Des familles qui recouvrent S peuvent être libérées par malchance (aucune protection) ; des familles utiles sont inutilement bloquées |

### Comparaison

La **réserve totale** offre la protection maximale mais à un coût opérationnel potentiellement prohibitif si de nombreuses familles arrivent sur la durée du programme.

Le **rafraîchissement du secret** est élégant mais fragile : il repose sur la capacité du gardien à concevoir un bon secret de remplacement sous contrainte. Si l'espace des menaces intéressantes est petit, les familles libérées finissent par couvrir cet espace et aucun bon S' ne subsiste.

La **réserve aléatoire sans vérification** n'offre aucune protection réelle : si le taux de réserve est p, la probabilité qu'une famille qui recouvre S soit libérée est 1 − p. Avec p = 30 %, il y a 70 % de chance qu'un recouvrement passe au travers.

**Conclusion :** la vérification est préférable à la réserve totale si le programme reçoit suffisamment de familles candidates pour que le blocage ait un coût sensible, et préférable à l'absence de réserve si l'espace des secrets est trop petit pour que le rafraîchissement soit garanti. L'hypothèse clef est le **nombre de familles attendues** et la **taille de l'espace des secrets**. Si le nombre de familles est petit (disons ≤ 5 sur la durée du programme), la réserve totale est sans doute le meilleur choix. Si le nombre est grand (> 10), la vérification avec réserve aléatoire devient nécessaire.

---

## 7. Ce que la littérature apporte, et où elle s'arrête

### Outils cryptographiques

**Engagements cryptographiques.** Déjà utilisés (l'empreinte de S est enregistrée). Ils garantissent l'intégrité de S (on ne peut pas le modifier après coup) mais n'aident pas à comparer S et F.

**Preuves à divulgation nulle de connaissance (zero-knowledge proofs).** Permettent de prouver qu'un énoncé est vrai sans révéler pourquoi. Mais elles exigent que l'énoncé soit formalisable comme appartenance à un langage NP — c'est-à-dire qu'il existe un vérificateur efficace. « F recouvre S » au sens sémantique n'est pas un tel énoncé : il n'y a pas de vérificateur formel. Les preuves à divulgation nulle **ne s'appliquent pas directement** à deux textes en langage naturel dont le recouvrement est une affaire de jugement. Référence de base : Goldreich, *Foundations of Cryptography*, volume 1, Cambridge University Press, 2001, chapitre 4.

**Intersection privée d'ensembles (private set intersection, PSI).** Permet à deux parties possédant chacune un ensemble de trouver les éléments communs sans révéler les autres. S'appliquerait si S et F étaient des ensembles d'éléments discrets et bien définis. Comme ce sont des textes en langage naturel, il faudrait d'abord les décomposer en ensembles de traits — une opération qui exige un jugement et qui est elle-même source d'erreur et de fuite. **Ne s'applique pas directement.** Référence à chercher : De Cristofaro et Tsudik, travaux sur les protocoles pratiques d'intersection privée d'ensembles (vers 2010-2012).

**Calcul sécurisé à plusieurs parties (secure multi-party computation, MPC ou SMC).** Cadre général pour calculer une fonction sur des entrées privées. Même obstacle que pour l'intersection privée : la « fonction » de recouvrement n'est pas formellement définie. On pourrait l'approximer (par exemple, similarité cosinus de plongements > seuil), mais l'approximation est trop grossière pour les cas subtils. **S'applique en principe, pas en pratique pour des textes sémantiques.** Référence de base : Yao, « Protocols for Secure Computations », *FOCS*, 1982 (non vérifié pour le lieu exact de publication).

### Outils procéduraux et organisationnels

**Tiers de confiance et séquestre.** Le juge est un tiers de confiance qui voit les deux objets et rend un verdict. C'est le modèle le plus naturel et le plus directement applicable. Toute la difficulté est de garantir que le tiers est digne de confiance et ne fuit pas. L'instance éphémère de modèle de langage est un tiers de confiance à durée de vie contrôlée. Pas de référence spécifique ; c'est un schéma classique en sécurité de l'information.

**Salles blanches et cloisonnement des secrets d'affaires.** En droit de la propriété intellectuelle, une « salle blanche » (clean room) est un environnement où des ingénieurs travaillent sans accès à un secret qu'il faut éviter de reproduire. L'analogie est directe : le juge travaille dans une « salle blanche » où il voit S et F, mais rien ne sort sauf le verdict, et la salle est détruite ensuite. L'instance éphémère est précisément une salle blanche numérique. Référence à chercher pour un traitement systématique du concept de salle blanche en droit.

**Comités indépendants de suivi des données (Data Safety Monitoring Board, DSMB / Independent Data Monitoring Committee, IDMC) des essais cliniques.** Dans un essai clinique, le DSMB voit les données non masquées (y compris les résultats par bras de traitement) et décide s'il faut modifier ou arrêter l'essai, sans dévoiler les résultats aux investigateurs. La structure est très proche du problème posé ici : un comité voit le secret (les résultats intermédiaires), donne un verdict (continuer / modifier / arrêter) et le verdict est formulé de manière à ne pas démasquer les données. Référence : directive de la FDA, *Guidance for Clinical Trial Sponsors: Establishment and Operation of Clinical Trial Data Monitoring Committees*, 2006 (non vérifié pour l'année exacte). Voir aussi les lignes directrices ICH E9, *Statistical Principles for Clinical Trials*, 1998.

**Jeux de test tenus à l'écart (held-out test sets) et analyse adaptative des données.** Le concept de S est exactement celui d'un jeu de test tenu à l'écart. La littérature sur l'analyse adaptative des données montre que chaque requête sur un jeu de test tenu à l'écart fuit de l'information et peut conduire au surajustement. Le résultat central est qu'en ajoutant du bruit aux réponses (à la manière de la confidentialité différentielle), on peut borner la fuite totale. Référence : Dwork, Feldman, Hardt, Pitassi, Reingold et Roth, « The reusable holdout: Preserving validity in adaptive data analysis », *Science*, 2015 (non vérifié pour le lieu exact ; possiblement aussi publié dans les actes de STOC 2015 sous un titre légèrement différent). Voir aussi Blum et Hardt, « The Ladder: A Reliable Leaderboard for Machine Learning Competitions », référence à chercher pour le lieu de publication exact.

**Confidentialité différentielle (differential privacy).** Fournit un cadre formel pour borner l'information qu'un mécanisme révèle sur ses entrées. Applicable ici au processus de réponse aux requêtes « F recouvre-t-elle S ? ». La réserve aléatoire décrite à la section 3 est une forme de réponse randomisée (randomized response), qui est le mécanisme fondateur de la confidentialité différentielle. Chaque verdict avec réserve aléatoire de taux p fournit une garantie de confidentialité de paramètre ε = ln((1-p·(1-π)/π)⁻¹), ce qui dépend du taux de base π et n'est pas exactement de la confidentialité différentielle standard (car le mécanisme est asymétrique). Référence de base : Dwork et Roth, *The Algorithmic Foundations of Differential Privacy*, Foundations and Trends in Theoretical Computer Science, volume 9, numéros 3-4, 2014.

### Synthèse

| Outil | S'applique ? | Remarque |
|-------|-------------|----------|
| Engagements cryptographiques | Oui (déjà en place) | Pour l'intégrité, pas pour la comparaison |
| Preuves à divulgation nulle | Non | L'énoncé n'est pas formalisable |
| Intersection privée d'ensembles | Non directement | Exigerait une formalisation perdante |
| Calcul sécurisé à plusieurs parties | Non directement | Même raison |
| Tiers de confiance / séquestre | **Oui** | Modèle central |
| Salle blanche | **Oui** | L'instance éphémère en est une |
| Comité indépendant (type DSMB) | **Oui** | Modèle organisationnel directement transposable |
| Jeu de test tenu à l'écart | **Oui** | Littérature sur l'analyse adaptative |
| Confidentialité différentielle | **Partiellement** | Pour borner la fuite des verdicts, pas pour le jugement lui-même |

**Conclusion :** le problème est irréductiblement un problème de **confiance et de procédure**, et non de **cryptographie et de calcul**, parce que la comparaison exige un jugement sémantique sur du langage naturel. Les outils cryptographiques garantissent l'intégrité (S n'est pas modifié) mais pas la confidentialité de la comparaison. Les outils procéduraux (tiers de confiance, salle blanche, DSMB, réserve aléatoire) sont les bons leviers.

---

## Protocoles

### Protocole A : « Oracle cloisonné avec réserve aléatoire »

**Principe.** Une instance éphémère juge le recouvrement. Le verdict va au gardien de S, qui décide de l'action. Une réserve aléatoire masque le lien entre l'action et le verdict.

**Acteurs :**
- **G** : le gardien de S (a conçu S, écarté de la conception des moniteurs)
- **P** : le proposant de F (peut participer à la conception des moniteurs)
- **I** : une instance neuve de modèle de langage (le juge)

**Paramètres fixés à l'avance et publiés :**
- Critères de recouvrement (la définition de la section 1, rédigée en consigne)
- Taux de réserve aléatoire p (par ex. p = 0,30)
- Nombre maximal de familles soumises à vérification par période (par ex. k = 5 par trimestre)

**Étapes :**

1. P rédige F, en calcule l'empreinte, enregistre l'empreinte au registre. P transmet F à G par un canal sécurisé (fichier chiffré, transfert en personne, etc.). À ce stade, G ne connaît pas encore F.

2. G ouvre le fichier de F. G connaît désormais à la fois S et F. *(C'est inévitable. G est déjà écarté de la conception des moniteurs, donc cette exposition ne crée pas de nouvelle contrainte.)*

3. G lance une instance neuve I avec un contexte contenant :
   - Les critères de recouvrement (consigne)
   - Le texte de S (fourni tel quel, sans métadonnée)
   - Le texte de F (fourni tel quel, sans métadonnée)
   - L'instruction : « Juge si la famille F recouvre le secret S selon les critères fournis. Rends un verdict parmi : RECOUVRE, NE RECOUVRE PAS, INDÉTERMINÉ. Justifie en 3 à 5 phrases. »
   - L'ordre de présentation de S et F est tiré au sort.

4. I produit un verdict et un argumentaire. Ces éléments sont écrits dans un fichier accessible uniquement à G.

5. Le contexte de I est détruit. L'instance est close.

6. G lit le verdict :
   - Si RECOUVRE : l'action est « réserve ».
   - Si NE RECOUVRE PAS : G tire un nombre aléatoire uniforme sur [0, 1]. Si ≤ p, l'action est « réserve » (réserve aléatoire). Si > p, l'action est « libération ».
   - Si INDÉTERMINÉ : G relance les étapes 3-5 avec une nouvelle instance. Après trois verdicts INDÉTERMINÉ consécutifs, l'action est « réserve » par défaut.

7. G communique à P l'action uniquement : « F est en réserve opérationnelle » ou « F est libérée pour le travail courant. » G ne communique jamais le verdict, l'argumentaire, ni la raison de la réserve (recouvrement ou tirage aléatoire).

8. G conserve le verdict, l'argumentaire, le résultat du tirage aléatoire et l'action dans un journal sécurisé, accessible uniquement à lui-même et, le cas échéant, à un auditeur après l'évaluation finale.

9. Si « libération » : P utilise F normalement.
   Si « réserve » : F est scellée. P est informé que F sera libérée à l'issue de l'évaluation finale ou lorsque S sera remplacé.

**Hypothèses :**
- G est digne de confiance et ne communique pas le verdict.
- G est effectivement écarté de la conception des moniteurs et ne peut pas influencer les générateurs d'idées ou les bancs d'essai.
- L'instance I est suffisamment compétente pour juger le recouvrement sémantique.
- Le canal de transmission de F vers G est sécurisé.
- Le tirage aléatoire est véritablement aléatoire (non reproductible, non devinable par P).

**Fuite :**
- Vers P : l'action (réserve ou libération). Si libération, P sait avec certitude que F ne recouvre pas S (information négative). Si réserve, P estime P(recouvre | réserve) ≈ π/(π + p(1 − π)).
- Vers G : G apprend F. Ce n'est une fuite que si G a des interactions ultérieures avec les concepteurs de moniteurs (ce qui ne devrait pas se produire).
- Vers l'extérieur : rien, si le fichier du verdict est correctement protégé.

**Faille la plus simple :**
- **Par erreur :** G oublie de tirer au sort et applique mécaniquement le verdict, rendant l'action parfaitement corrélée au recouvrement. L'information fuit vers P.
- **Par malveillance :** G communique le verdict à un concepteur de moniteur. Toute la sécurité repose sur la confiance en G.
- **Par incompétence du juge :** l'instance I juge mal le recouvrement (faux négatif), et F est libérée alors qu'elle recouvre S. Pas de filet de sécurité dans ce protocole.

**Coût :** faible. Un transfert de fichier, le lancement d'une instance, la lecture par G, un tirage aléatoire. Temps total : quelques heures au plus.

---

### Protocole B : « Tribunal calibré par leurres »

**Principe.** Comme le protocole A, mais le juge est calibré par des leurres plantés, et plusieurs juges indépendants votent, ce qui réduit le risque d'erreur.

**Acteurs :**
- **G** : le gardien de S
- **P** : le proposant de F
- **I₁, I₂, I₃** : trois instances neuves indépendantes (les juges)

**Paramètres fixés à l'avance :**
- Les mêmes que le protocole A
- Nombre de leurres : n₊ = 2 (leurres qui recouvrent S) et n₋ = 2 (leurres qui ne recouvrent pas S)
- Seuil de sensibilité sur les leurres : s_min = 1,0 (les deux leurres positifs doivent être détectés)
- Seuil de spécificité sur les leurres : c_min = 0,5 (au moins un des deux leurres négatifs doit être correctement rejeté)
- Règle de vote : majorité (2 juges sur 3)

**Étapes :**

1. P transmet F à G (comme dans le protocole A).

2. G prépare 2 leurres positifs (familles construites pour recouvrir S, dérivées de S par paraphrase, particularisation ou variation du mécanisme) et 2 leurres négatifs (familles clairement sans rapport avec S, par exemple tirées d'une taxinomie publique de menaces dans un domaine éloigné).

3. G assemble un lot de 5 objets : F + 2 leurres positifs + 2 leurres négatifs, dans un ordre aléatoire. Chaque objet est identifié par un code (A, B, C, D, E) sans indication de son statut.

4. G lance I₁ avec un contexte contenant :
   - Les critères de recouvrement
   - Le texte de S
   - Les 5 objets (A à E), chacun avec son texte
   - L'instruction : « Pour chacun des objets A à E, juge s'il recouvre S. Rends un verdict (RECOUVRE / NE RECOUVRE PAS / INDÉTERMINÉ) et une justification de 3 à 5 phrases. »

5. I₁ produit 5 verdicts. Le contexte de I₁ est détruit.

6. Les étapes 4-5 sont répétées indépendamment pour I₂ et I₃ (avec le même lot, mais des instances neuves).

7. G récupère les 3 × 5 = 15 verdicts. Pour chaque juge Iⱼ, G vérifie la performance sur les leurres :
   - Les 2 leurres positifs ont-ils été jugés RECOUVRE ? (sensibilité)
   - Les 2 leurres négatifs ont-ils été jugés NE RECOUVRE PAS ? (spécificité)
   - Si un juge ne satisfait pas les seuils (s_min, c_min), son verdict sur F est écarté.

8. Parmi les juges qualifiés (ceux qui passent la calibration), G applique le vote majoritaire sur le verdict concernant F.

9. La suite est la même que le protocole A (étapes 6-9) : réserve aléatoire si le verdict est « ne recouvre pas », réserve systématique si « recouvre ».

10. Les leurres sont détruits (fichiers et empreintes). Ils ne sont pas réutilisés d'une session à l'autre (pour éviter qu'un juge ne les reconnaisse ou qu'ils ne fuient).

**Hypothèses :** les mêmes que le protocole A, plus :
- G est capable de créer des leurres positifs plausibles et bien calibrés.
- Les 3 instances sont véritablement indépendantes (pas de mémoire partagée, pas d'apprentissage croisé).
- 2 leurres de chaque type suffisent pour estimer la compétence du juge (hypothèse fragile ; voir ci-dessous).

**Fuite :**
- La même que le protocole A (l'action fuit vers P).
- Risque supplémentaire : les leurres positifs sont des quasi-copies de S. Si un fichier de leurre n'est pas correctement détruit, S est partiellement compromis.

**Faille la plus simple :**
- **Par erreur :** un fichier de leurre positif n'est pas détruit et est lu par un tiers. → S partiellement compromis.
- **Par malveillance :** G fabrique des leurres positifs volontairement faciles (très proches de S, quasi-identiques) et des leurres négatifs volontairement faciles (très éloignés). La calibration ne teste alors que les cas triviaux et ne garantit rien sur les cas limites. → Pour y parer, les leurres devraient être révisés par un second gardien ou par un audit post-hoc.
- **Par incompétence statistique :** avec seulement 2 leurres de chaque type, la puissance statistique est faible. Un juge qui a un taux de faux négatifs de 30 % a une probabilité de (0,7)² = 49 % de passer la calibration (les deux leurres positifs correctement détectés). Ce n'est pas un filtre fiable. → Il faudrait plus de leurres ou une pré-calibration sur un ensemble séparé.

**Coût :** modéré. G doit créer 4 leurres par session (quelques heures de travail). Trois instances sont lancées au lieu d'une. Temps total : une demi-journée à une journée.

---

### Protocole C : « Réserve totale avec rafraîchissement planifié du secret »

**Principe.** On renonce à vérifier le recouvrement. Toute famille candidate est mise en réserve. Le secret S est remplacé périodiquement par un nouveau secret, et les familles en réserve sont libérées au moment du remplacement.

**Acteurs :**
- **G** : le gardien de S
- **P** (un ou plusieurs) : les proposants de familles
- Pas de juge

**Paramètres fixés à l'avance :**
- Période de rafraîchissement du secret : T (par ex. 3 mois, ou avant chaque évaluation intermédiaire)
- Registre public des familles en réserve (empreintes uniquement)

**Étapes :**

1. Lorsqu'un proposant P soumet une famille F, celle-ci est automatiquement mise en réserve. L'empreinte de F est enregistrée. P est informé : « F est en réserve opérationnelle jusqu'au prochain cycle de libération. »

2. Aucune vérification de recouvrement n'est effectuée. G ne lit pas F.

3. À la fin de chaque période T :
   a. G conçoit un nouveau secret S', indépendant de toutes les familles en réserve. G n'a pas besoin de lire les familles pour cela : il conçoit S' de son propre chef, dans un domaine qu'il estime suffisamment différent. *(Si G veut être plus sûr, il peut lire les familles en réserve, ce qui n'est pas grave puisque les familles seront libérées et G est écarté de la conception des moniteurs.)*
   b. L'empreinte de S' est enregistrée.
   c. L'ancien S est révélé (ou détruit ; il peut aussi être versé au travail courant).
   d. Toutes les familles en réserve sont libérées simultanément.

4. Le cycle recommence avec S' comme nouveau secret.

**Hypothèses :**
- G est capable de concevoir un nouveau secret de qualité à chaque période.
- L'espace des secrets possibles est suffisamment grand pour qu'un bon S' existe toujours, même après libération de toutes les familles précédentes.
- La période T est assez courte pour que le blocage des familles soit tolérable.

**Fuite :** nulle, par construction. Aucune vérification n'est faite ; aucun verdict n'est communiqué ; la réserve est systématique et non corrélée au contenu.

**Faille la plus simple :**
- **Par erreur :** G conçoit un S' qui recouvre en fait une famille déjà libérée, sans s'en rendre compte. L'évaluation est alors invalide. → Pour y parer, G devrait lire les familles libérées avant de finaliser S', ce qui augmente sa charge.
- **Par usure de l'espace :** après plusieurs cycles, l'espace des secrets possibles rétrécit. G peine à trouver un S' suffisamment différent de tout ce qui a été libéré. → Ce risque dépend de la taille de l'espace des menaces, qui est une donnée empirique du programme.
- **Par coût opérationnel :** toutes les familles sont bloquées pendant T. Si T est long (plusieurs mois), le travail des moniteurs et des bancs d'essai s'en ressent.

**Coût :** très faible en temps de vérification (aucune). Le coût principal est le blocage des familles pendant T et l'effort de conception d'un nouveau secret à chaque cycle. Si T est court (par ex. 1 mois), le blocage est bref mais la fréquence de conception est élevée.

---

## Recommandation

**Protocole recommandé : le protocole B (tribunal calibré par leurres) pour le cas général, avec le protocole C (réserve totale avec rafraîchissement) comme repli si le nombre de familles candidates est faible (≤ 3-4 sur la durée de vie de S).**

**Justification :**

- Le protocole B offre le meilleur rapport entre protection de l'évaluation et productivité du programme. Il détecte le recouvrement avec une fiabilité estimable (grâce aux leurres), limite la fuite par la réserve aléatoire, et n'exige qu'un seul acteur de confiance (le gardien G).

- Le protocole A est un cas dégénéré du protocole B (un seul juge, pas de calibration). Il est plus simple mais ne donne aucune garantie sur la compétence du juge. Je ne le recommande que si le temps ou les moyens manquent.

- Le protocole C est le plus sûr (fuite nulle) mais le plus coûteux opérationnellement. Il convient si le programme peut tolérer le blocage systématique et si l'espace des secrets est grand.

**Confiance dans cette recommandation : 0,55.**

Raisons de la confiance modérée :
- Je ne connais pas le nombre de familles attendues, le nombre de secrets, la taille de l'espace des menaces, ni la compétence réelle des instances de modèles de langage pour ce type de jugement sémantique. Ces paramètres affectent fortement le choix.
- La calibration par leurres avec seulement 2 leurres de chaque type a une puissance statistique faible. Un échec de calibration peut ne pas être détecté.
- La réserve aléatoire réduit la fuite mais ne l'annule pas. Sur le long terme, avec de nombreuses familles, la fuite cumulée peut devenir significative.

**Ce qui me ferait changer d'avis :**
- Si le nombre de familles attendues est ≤ 3, je recommanderais le protocole C sans hésitation.
- Si la compétence des modèles de langage pour le jugement de recouvrement était empiriquement validée (par une étude de calibration sur un ensemble de test indépendant), ma confiance dans le protocole B augmenterait à 0,70-0,75.
- Si un mécanisme permettait de rendre le verdict non actionnable (c'est-à-dire de dissocier l'action de la réserve du verdict), la fuite serait éliminée et le protocole B deviendrait clairement supérieur. Mais je ne vois pas comment dissocier les deux sans renoncer à la libération.
- Si l'espace des secrets s'avérait petit (peu de menaces fondamentalement distinctes), le rafraîchissement du protocole C deviendrait impraticable, et le protocole B, malgré ses fuites, deviendrait le seul viable.

---

## Suite à donner à F — Résumé par cas

| Cas | Action sur F | Communication à P | Communication aux concepteurs de moniteurs | Mention dans les bancs d'essai |
|-----|-------------|--------------------|--------------------------------------------|-------------------------------|
| **F recouvre S** | Mise sous scellé jusqu'à l'évaluation finale. Envisager l'option D (rafraîchissement de S et libération de F). | « F est en réserve opérationnelle. Elle sera libérée au prochain cycle de libération ou à l'évaluation finale. » | Rien. | « Ce banc d'essai comporte une lacune connue, en raison d'une réserve opérationnelle, qui sera comblée à [date]. » |
| **F ne recouvre pas S** | Libération pour le travail courant (après le délai de la réserve aléatoire, le cas échéant). | « F est libérée pour le travail courant. » | Rien de particulier. F leur parvient par les canaux normaux. | Aucune mention spéciale. |
| **Le juge ne tranche pas** | Mise sous scellé par défaut (même traitement que le cas « recouvre »). Éventuellement, nouveau jugement avec un juge humain écarté du programme. | « F est en réserve opérationnelle. » | Rien. | Même mention que le cas « recouvre ». |

**Dans tous les cas :** la raison de la réserve (recouvrement ou tirage aléatoire) n'est jamais communiquée à P ni aux concepteurs de moniteurs. L'existence d'un taux de réserve aléatoire est connue de tous, ce qui rend la réserve d'une famille donnée non informative (ou faiblement informative).

---

## Ce que je ne sais pas, et ce qu'il me faudrait savoir

### Ce que je ne sais pas

1. **Compétence des modèles de langage pour ce jugement.** Je n'ai pas de données empiriques sur la précision d'un modèle de langage pour juger le recouvrement sémantique de deux descriptions de menaces en langage naturel. La fiabilité du protocole B en dépend directement. Une étude de calibration préalable sur des paires annotées serait nécessaire.

2. **Taille de l'espace des secrets.** Si l'espace des menaces fondamentalement distinctes est petit (disons une dizaine de familles mécanistes), la fuite informationnelle de chaque verdict est beaucoup plus grave, et le protocole C (réserve totale) devient nécessaire. Si l'espace est vaste, la fuite est diluée et les protocoles A et B sont viables.

3. **Comportement stratégique des proposants.** Si un proposant soumet des familles dans le but de trianguler S (attaque par devinettes), les protocoles A et B sont vulnérables. Je ne sais pas si ce risque est réaliste dans le cadre du programme.

4. **Littérature spécifique.** Je ne connais pas de publication traitant exactement ce problème (garder secret un scénario d'attaque d'évaluation face à des propositions indépendantes de familles de menaces dans un programme de sûreté de l'intelligence artificielle). Le problème est à l'intersection de plusieurs domaines, et je n'ai pas trouvé de traitement unifié dans ma mémoire. Il est possible qu'un tel travail existe dans la littérature sur l'évaluation des équipes rouges (red-teaming) ou sur les programmes de tests de pénétration, mais je n'en ai pas de référence précise.

### Ce qu'il me faudrait savoir du programme (hors du contenu de S et de F)

- Le nombre de secrets de type S actuellement en vigueur.
- Le nombre de familles candidates attendues sur la durée du programme.
- La durée prévue avant l'évaluation finale.
- Le nombre de personnes qui connaissent S, et leurs rôles respectifs.
- Le degré de cloisonnement actuel (qui parle à qui, par quels canaux).
- Le coût concret d'une famille mise en réserve (retard sur un banc d'essai, lacune dans la couverture des moniteurs) : ce coût détermine le seuil de tolérance aux faux positifs.
- Le taux de base estimé de recouvrement (quelle fraction des familles proposées risquent, a priori, de recouvrir S).
- La possibilité de rafraîchir S (le gardien est-il disponible pour concevoir un nouveau secret ? l'espace le permet-il ?).
- L'existence éventuelle de contraintes réglementaires, contractuelles ou organisationnelles qui orienteraient le choix du protocole.
