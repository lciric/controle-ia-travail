# Réponse de conv-audit à la question 1 (chapelles) — version 2

- Version 2, 31 octobre 2026, rédigée de 01:25 à 02:10 heure UTC par un sous-agent neuf (Opus 5.5, lignée conv-audit), qui n'a écrit ni la v1, ni les relectures, ni la synthèse du collisionneur. La v1 (`reponse-conv-audit-question-1-v1.md`) reste intacte. Les erreurs de la v1 sont listées dans `erratum-reponses-v1-v1.md`.
- Niveau méthode ; aucune décision. Statuts : « vérifié sur PDF » (page lue par moi ou par une fiche vérifiée), « page en ligne » (lue par une pièce, non opposable, R7), « notice seulement », « SUPPOSÉ » (mémoire).
- Pièces intégrées (sha256sum) :
  - `question-1-chapelles-v1.md` — `3df53fd41a3ea354847ca66bf9b370a956223137a4d74125aa9c61c6d378ef9f`
  - `reponse-conv-audit-question-1-v1.md` — `11dbecb0aeb462decfe3c86ea6f769c8355721b41509f80e3ba6539eec00a825`
  - `relecture-fable-reponse-1-v1.md` — `069c021660e8b4ad374f7dd282ae7b9615aac488df36eae543e1cff92198915d`
  - `reponse-fable-independante-question-1-v1.md` — `f0a507bbbb91808ef16365b13fe22138728ca9ef0c59b7f6874c451399a57e36`
  - `revue-biblio-fertilite-v1.md` — `307b4f2fe6e53dcfa517c6da5d2591a6cee1e1508cd8197f4778fe014d6b718f`
  - `lecture-reponse-argon-bisociation-v1.md` — `3271d0e25cafa6a5df048547249debf958bd9a830c0099afd38cac4a88de8b96`
  - réponse d'Argon, lue dans le commit `b1a21a07` (le fichier n'existe pas sur la branche `canal/conv-audit-n04`, vérifié sur disque et par `git cat-file`, R11) — `c2a991060f0ef87887e97e482009a754121ce29415d1f2a2159df24d35159ed7`
  - `docs/notes/bisociation-litterature-reelle-v1/collisionneur-bisociation-lot-v1/synthese-bisociation-lot-v2.md` — `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86`
  - `registres/decisions.md`, ligne R-609.

## Réponse courte

La chapelle (courant qui ne parle pas à un autre) est une meilleure unité que le domaine, mais **mesurer l'éloignement entre groupes et le tester sur des ponts datés n'est pas neuf** (Swanson, Burt, Vilhena, Uzzi, Shi-Evans, Sourati-Evans, Rzhetsky-Foster-Evans). Ce qui peut rester propre au programme : un **profil à couches** (communication faible, prémisses distinctes, structure mathématique commune), converti en un **score unique gelé avant lecture**, qui doit **battre la distance entre domaines et la popularité** sur une base de ponts postérieurs à 1991, avec les six garde-fous de la synthèse. S'il ne les bat pas, on garde la distance entre domaines.

## Ce qui change par rapport à la v1

| Constat | Sort | Correction |
|---|---|---|
| RL1-01 Swanson manqué (littératures disjointes) | accepté | Swanson et la découverte fondée sur la littérature sont l'antériorité du cas « chapelles qui s'ignorent » ; la v2 s'inscrit dans cette lignée. |
| RL1-02 le test « ponts datés plus témoins, coupure » est standard | accepté | Présenté comme antériorité, pas comme apport. Collision d'antériorité déjà remontée à Lazar (R-609) : nœud, non tranché ici. |
| RL1-03 Sourati-Evans mal décrit | accepté | Hypergraphe auteurs, matériaux, propriétés ; densité d'experts ; aucune détection de communautés ; leur résultat principal favorise le **proche** de l'expertise humaine (relecture 1, page arXiv 2306.01495 ; revue, section 2.2). |
| RL1-04 classiques non marqués | accepté | Tous marqués SUPPOSÉ ; date du pont de Hopfield fixée par un lecteur aveugle, pas par la légende. |
| RL1-05 Marshall-Warren rangé comme pont | accepté | Deux bases étiquetées : « s'ignorent » (transfert d'outil) et « se contredisent » (expérience cruciale) ; Marshall-Warren va dans la seconde. |
| RL1-06 dénominateur, ligne de base, dynamique, littérature de la genèse absents | accepté | Taux de base des paires à profil prometteur ; comparaison obligatoire à la distance entre domaines ; partition recalculée à chaque coupure ; corpus de la genèse borné (section 5). |
| RL1-07 données incompatibles avec les ponts 1938–1984 | accepté | Base de ponts postérieurs à 1991 à constituer ; les ponts anciens servent d'illustration, pas de test. |
| RL1-08 « profil » contre « distance » confus | accepté | Le profil devient un score par poids gelés avant lecture, ou par sélection sur la frontière de Pareto (réponse Fable indépendante 2, section 3). |
| RL1-09 pas de critère de mort ; indépendance des lecteurs fictive | accepté | Critère de mort chiffré ci-dessous ; lecteurs humains ou familles de modèles distinctes, isolés du dépôt, seuil d'accord gelé. |
| RL1-10 périmètre et coût irréalistes | accepté | Un pilote sur un domaine ; aucune durée promise. |
| RL1-11 modèle nul et résolution | accepté | Modèle nul de configuration à degrés conservés ; résolution fixée d'avance. |
| Synthèse, défaut A0 (trou lu dans le flux de citations : retour à la moyenne) | accepté | Rétrodiction inversée obligatoire ; étiquette de pont indépendante des citations. |
| Synthèse, appariement des témoins sur la distance textuelle « retire la variable testée » (T2-A, T2-C) | accepté | Témoins appariés en taille, âge, croissance ; jamais sur la variable testée. |

## 1. Ce qui définit une chapelle

Une chapelle n'est pas une partition unique mais un accord entre partitions faites **couche par couche** (réponse Fable indépendante 1 ; Argon, section A ; v1) :

- **sociale** : citations et cosignatures, communautés détectées avec stabilité par rééchantillonnage ;
- **lexicale** : vocabulaires, termes absents chez les voisins (la mesure de Vilhena 2014 est de ce type) ;
- **méthodologique** : instruments, échelles, formalismes déclarés dans les sections de méthode ;
- **des prémisses** : énoncés tenus pour acquis, codés par une grille fixe ; c'est la couche la plus fragile ; si elle n'est pas reproductible, on le dit et on s'en tient aux autres (réserve de la réponse Fable 1, reprise) ;
- **structurale** : objets mathématiques partagés. Le LaTeX brut ne donne pas d'isomorphismes sans résolveur symbolique (synthèse, A, T1-C a2) ; la distance d'édition d'arbres syntaxiques d'équations proposée par Argon est une proposition non testée.

Deux réserves de la synthèse : un modèle de blocs sur la couche sociale « regroupe les adversaires qui se citent » (T1-C a1), donc confond les deux relations ci-dessous ; et les chapelles détectées restent une **HYPOTHÈSE** (T1-B P1, T1-D).

## 2. Deux relations à ne pas fondre

- **S'ignorer** : même objet ou même structure, aucun flux. Appelle un transfert d'outil. C'est le cas de Swanson.
- **Se contredire** : même objet, prémisses opposées ; souvent beaucoup de citations, négatives. Appelle une expérience cruciale. Les chapelles cosmologiques de Lazar sont de ce type.

La non-communication est **asymétrique** (A peut lire B sans réciproque) : une divergence, pas une métrique (réponse Fable 1).

## 3. Du profil au score

Le pont prometteur est « loin sur la communication et les prémisses, proche sur la structure ». Pour choisir des paires, il faut un ordre : poids gelés avant toute lecture de la base de verdict, ou frontière de Pareto. Le canal (capacité : personnes, revues, conférences communes) se mesure **à part** du flux (citations observées) : un flux faible sans canal est un vrai trou ; un flux faible sans structure commune est une vraie distance (relecture 2, RL2-17).

## 4. Étalonnage

- Base de ponts **postérieurs à 1991**, deux types étiquetés, constituée par un lecteur qui ne connaît pas les définitions.
- Six garde-fous de la synthèse (décision proposée n° 1, non tranchée ici) : étiquette de pont indépendante du canal (réutilisation hors des citations) ; rétrodiction inversée ; graphe amputé des ponts ; bras « popularité seule » ; jeux disjoints par niche et par période ; calcul de puissance préalable.
- Référence à battre : la distance entre domaines déjà préenregistrée, la popularité seule, et une mesure publiée (Sourati-Evans ou Shi-Evans), comme le demande la réponse Fable 1 (section 4, point 4).

## 5. Revue de la genèse

Revue bornée : corpus de départ, critères d'inclusion, règle d'arrêt écrits avant la recherche. Trois corpus : philosophie et sociologie des sciences ; psychologie de la créativité ; science des sciences. Livrable : un inventaire de mécanismes (migration d'un chercheur, importation d'un instrument, analogie formelle, controverse forcée), chacun traduit en règle candidate (réponse Fable 1, section 3). « Exhaustif » n'est pas une promesse tenable (synthèse, F, T1-D).

## Convergences et divergences avec la réponse Fable indépendante 1

- **Convergent** : couches séparées ; témoins et étalon avant mesure ; structure lue dans les équations ; un modèle de langue peut extraire des prémisses, jamais juger la distance.
- **Divergent** : Fable propose un étalon de trente paires étiquetées par des personnes du domaine, plus dix paires qui communiquent ; la v1 partait de ponts historiques. La v2 garde les deux : l'étalon d'experts pour valider la partition, la base de ponts pour valider le score.

## Antériorités

| Auteur, année | Support | Statut |
|---|---|---|
| Swanson 1986 | *Perspectives in Biology and Medicine* | notice seulement (relecture 1, recherche web) |
| Burt 1992 ; 2004 | livre ; *American Journal of Sociology* | SUPPOSÉ |
| Vilhena et collègues 2014 | *Sociological Science* | page en ligne (revue v1, page du laboratoire) |
| Uzzi, Mukherjee, Stringer, Jones 2013 | *Science* | PDF versé (`docs/sources/pdf/bisociation-fertilite-v1/`), pages citées par la revue v1, non relues ici |
| Shi et Evans 2023 | *Nature Communications* | page en ligne (revue v1) |
| Sourati et Evans 2023 | *Nature Human Behaviour* (arXiv 2306.01495) | page en ligne (relecture 1, revue v1) |
| Rzhetsky, Foster, Foster, Evans 2015 | *PNAS* | notice seulement |
| Tshitoyan et collègues 2019 | *Nature* | notice seulement |
| Krenn et Zeilinger 2020 | *PNAS* | notice seulement |
| Kuhn 1962 ; Lakatos 1978 ; Fleck 1935 ; Galison 1997 ; Knorr Cetina 1999 ; Marr 1982 ; Holton 1973 ; Laudan 1977 ; Gentner 1983 | ouvrages, articles | SUPPOSÉ |
| Fortunato et collègues 2018 | *Science* | SUPPOSÉ |

## Critère de mort chiffré

Tous les seuils sont **proposés, à geler** dans un préenregistrement ; ils viennent des cellules du collisionneur, qui les disent illustratifs (synthèse, section iii).

Mesure : E1′ de la synthèse, appliquée au profil « chapelles ». L'hypothèse « la distance entre chapelles choisit mieux que la distance entre domaines » meurt si l'une de ces issues se produit sur la base tenue à l'écart :

1. le coefficient du profil (β₂, à canal et popularité contrôlés) n'a pas un intervalle à 90 % qui exclut zéro, bootstrap par niches (T3-A) ;
2. le gain du profil sur la distance entre domaines en précision dans les 100 premiers est inférieur à 20 %, intervalle à 95 % par blocs (variante T3-C) ;
3. la rétrodiction inversée atteint le score prospectif moins δ₀ = 0,03 (T3-B) : suspension, le signal est un retour à la moyenne.

Préalable : le calcul de puissance fixe la taille de la base avant le lancement. Si la puissance n'est pas atteinte, le test n'a pas lieu ; on ne lit pas un pilote sous-dimensionné.

## Ce qui reste ouvert

- La forme de l'étiquette de pont indépendante des citations : trois variantes dans les cellules (A, C, D), aucune choisie.
- La couche des prémisses peut-elle être codée de façon reproductible ? Rien ne le montre encore.
- La collision d'antériorité (R-609) attend la décision de Lazar.
- « Distance entre paradigmes » séparée de « distance entre objets » : aucune mesure lue ne les sépare (revue, section 4, point 5) ; c'est une question, pas un trou (R8).
