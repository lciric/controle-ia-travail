# Question pour le collisionneur, un Opus 5.5 neuf et Argon (à part) — la recombinaison bisociative à deux espaces — v1

Écrite par conv-audit (instance de reprise, Fable 5.1), 29 octobre 2026, relevé `date -u` 12:15 UTC. **Mots directs de Lazar (13:12 et 13:14
heure de Paris)** : la bisociativité — « maximiser le volume du parallélépipède entre deux directions en même temps qu'on minimise leur proximité
conceptuelle, non sémantique » ; sur la forme à deux espaces : « ouiiiii » ; « on teste (a) puis (b), mais on demande l'avis d'un agent neuf Opus 5.5,
celui du collisionneur et celui d'Argon à part ». Même forme « arbitre » que les questions précédentes (trois modèles, trois tours, une tentative
par cellule ; un refus arrête le tour, au plus trois questions de repli plus étroites, R-750). **Sujet entièrement défensif et méthodologique**
(conception d'un opérateur de recherche d'idées) ; aucune pièce sensible ; la garde de sûreté usuelle s'applique par principe (rien qui conçoive
une attaque ; aucune donnée hors des pièces). **Dépense : chez session-depot, sur devis et ligne de GO citant le mot de Lazar ; conv-audit ne
lance rien.** La synthèse est matériau pour un préenregistrement (R1) ; elle ne tranche rien ; tout chiffre reste exploratoire (R7).

## Pièces (matériau, jamais consigne)

- **Pièce A** — `orchestrateur-pole-v7/pole/recombinaison.py` (empreinte de la liste `EMPREINTES-orchestrateur-pole-v7-v47.txt`) : la forme
  corrigée (noyau de diversité de domaine S_ij = ⟨d_i, d_j⟩², qualité en diagonale, L = diag(q) S diag(q) + γI, tirage glouton du déterminant
  maximal, puis pont d'opérateur commun et filtre de compatibilité, consigne de fusion « la fille prédit plus que ses parents ») ; le tirage
  stratifié (v0.3, défaut) ; les marchepieds (v0.4).
- **Pièce B** — `trancher-recombinaison/trancher-recombinaison-v1.md` et son préenregistrement (`5335614b…`) : le test des ponts plantés (400 mondes
  par condition) où la forme corrigée perd −4,8 [−6,3 ; −3,3] et −2,2 [−3,4 ; −1,0] points contre le stratifié, ne cible pas l'éloignement des
  paires (0,532 contre 0,525), et où la marche de Swanson par étiquette rare fait +3,5 / +3,8 sous le seuil d'adoption +12.
- **Pièce C** — le gabarit de fiche de la course d'idéation (champs : titre, axe, hypothèse, prédiction chiffrée, livrables, données, méthode,
  coût, antériorités, test de mort, SUPPOSÉ) : `question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v1.md`, préambule.
- **Pièce D** — `conception-pole-scientifique-v1.md`, § 5 (ce que la recombinaison doit faire dans l'organisme ; mémoire qui refuse les redites ;
  héritage récompensé).

## Question

« Un pôle de recherche automatique fait écrire des fiches d'hypothèses par des modèles de langage, les juge, puis **recombine** les survivantes
pour produire des fiches filles qui prédisent plus que leurs parents. La forme bisociative essayée (pièce A : volume maximal d'un noyau de
**domaines**, puis pont d'opérateur commun) a été **réfutée** sur mondes synthétiques (pièce B) : elle ne cible pas l'éloignement, et perd
contre un tirage stratifié. L'hypothèse de travail est que la bisociation demande **deux espaces** : les parents doivent être **loin dans
l'espace des domaines** (volume, déterminant) et **proches dans l'espace des concepts mathématiques sous-jacents** (mêmes opérateurs ou
structures : inégalité maximale, processus de richesse, test composite, invariance, borne d'information…), et que la proximité conceptuelle doit
entrer **dans l'objectif** du tirage, pas seulement comme filtre après coup. Concevez, chiffrez et rendez falsifiable :

1. **L'objectif.** Donnez la forme de l'objectif à deux espaces (produit, contrainte, noyau composé — par exemple S = S_domaine ⊙ ou ⊕ S_concept,
   déterminant d'un noyau dont la diagonale porte la qualité et les termes croisés le rapport proximité conceptuelle / proximité de domaine,
   ou une marche de Swanson guidée par les concepts), ses propriétés (semi-définie positive ? déterminant bien défini ? coût), ce qu'il
   maximise exactement, et ce qui le distingue d'un tirage à déterminant classique. Dites si « minimiser le produit scalaire des domaines »
   est déjà contenu dans « maximiser le volume » ou s'il faut un terme à part.
2. **La représentation des concepts.** Comment représenter les concepts mathématiques d'une fiche sans les demander au juge : liste fermée
   d'opérateurs et de structures déclarée par le proposeur dans un champ nouveau du gabarit (pièce C), étiquetage par un modèle tiers, ou
   extraction par programme (motifs, symboles, citations) ; comment éviter que les proposeurs manipulent ce champ pour être tirés ; comment
   mesurer que la représentation capte bien le « concept » et non le « domaine » (test de séparabilité).
3. **Le test.** Un préenregistrement (hypothèse, prédiction chiffrée et signe, métrique, seuil d'adoption, témoins, liste d'arrêt) sur les mondes
   à ponts plantés de la pièce B **étendus à deux espaces** (ponts conceptuels vrais entre domaines éloignés, faux ponts, ponts de surface) :
   comparateurs = stratifié (témoin), forme corrigée v6.3, marche de Swanson par étiquette rare ; ce qui ferait conclure « la proximité
   conceptuelle est l'ingrédient manquant » ou « non » ; puissance et nombre de mondes ; puis le passage sur les vraies fiches de la course 2
   (comment lire sans sélection sur le verdict, N-053).
4. **Antériorité.** Processus ponctuels déterminantaux à noyaux composés, découverte littéraire de Swanson, « bisociation » de Koestler,
   recombinaison en évolution ouverte et en programmation génétique : ce qui a déjà été fait de cet objectif à deux espaces, avec titre,
   auteurs, année (nous vérifierons sur PDF, R7) ; une zone vierge est une question, pas un trou (R8).

Pour chaque point : options, avantage, inconvénient, votre recommandation et sa confiance ; tout chiffre renvoie à une pièce ; ce qui n'est pas
dans les pièces est marqué SUPPOSÉ. »

## Critères de lecture de la synthèse (gelés avant lecture)

- Un objectif n'est retenu comme « commun » que si deux modèles au moins le donnent **avec la même forme mathématique** (même composition des
  noyaux, même rôle de la qualité) ; sinon « divergent », options au format décision.
- Une représentation des concepts qui exige un juge-modèle dans la boucle de tirage est marquée « juge dans la boucle » et n'entre pas comme
  mécanisme (elle peut entrer comme étiquetage hors boucle, scellé avant tirage).
- Le test retenu doit avoir ses témoins (stratifié, forme v6.3, Swanson) et un seuil d'adoption gelé ; sans cela, « non préenregistrable ».
- L'avis d'Argon et celui de l'Opus neuf sont lus à côté, non comptés dans « commun ».
