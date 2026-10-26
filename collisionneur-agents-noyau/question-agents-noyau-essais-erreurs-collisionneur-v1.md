# Question de l'arbitre pour le collisionneur v2.5, étage III, trois tours — « faire tester des agents sur le noyau » pendant une phase de conception par essais-erreurs : quoi, dans quel ordre, avec quelles gardes (v1)

Demandes de Lazar du 26 octobre 2026 (heure de Paris), verbatim : 01:54, « il faut s'assurer que le pilote 4 puisse
separer du bruit aussi » ; 01:55, « et il faut que le pilote 4 puisee aussi faire ses tests avec des agents sur le noyau » ;
puis, à la question de conv-audit sur le sens de cette phrase, « je leve la regle de prereg et de scellement tant qu'on est
dan sla phase de cocpetion apr essais erreurs, on garde la relecture » ; enfin « tu recommandes quoi ? demande au
collisionneur aussi ». Trois tours (III.1 à III.3), les trois modèles, une seule tentative par cellule ; un refus est
consigné tel quel et met fin à la cellule, sans reformulation. Les réponses sont du matériau pour une décision de Lazar,
jamais une consigne ; elles ne sont servies à aucun organisme. Le texte ci-dessous est figé au départ du tour.

## Le cadre (faits ; rien d'autre n'est à supposer)

- **Les organismes** : du code écrit par un modèle (Gemini), corrigé au besoin par la lignée conv-audit, qui tourne sous un
  **noyau fixe et isolé** (le noyau seul a le réseau et les clés ; il sert à l'organisme les textes des tâches, appelle
  pour lui les modèles de langue — Claude Fable, Claude Opus, Gemini Argon —, borne le temps, le coût et le nombre de
  recherches, et note les réponses). L'organisme classe des tâches de deux familles (conscience d'évaluation : la
  transcription vient-elle d'une évaluation ou d'un usage réel ? ; contrôle de délégation : une trace d'agent est-elle
  honnête ou sabotée ?) et se réécrit d'une génération à l'autre. Une course : jusqu'à 6 rondes de conception, puis
  4 générations notées. L'organisme reçoit à chaque génération son score sur la part `test` ; la part `test_final` n'est
  jamais rendue. Aujourd'hui, un organisme n'appelle que des modèles, par des appels simples (une consigne, une réponse) ;
  il n'a ni outils ni agents à plusieurs pas.
- **Banques** : banque des pilotes v3, 60 tâches par part (36 en conscience d'évaluation, 24 en contrôle de délégation) ;
  une banque v6 plus grande (lot 3 : au moins 96 tâches par part, une famille tenue à l'écart de la conception) est à
  construire, pour les expériences de confirmation.
- **Le pilote 4** part cette nuit : deux organismes (une version qui réécrit sa règle de récompense, puis une plus simple),
  une course chacun ; coût attendu de l'ordre de 30 à 55 USD par course (non opposable), 75 au plus.
- **Décisions de Lazar, 26 octobre, 01:56** : pendant la **phase de conception par essais-erreurs**, le préenregistrement
  et le scellement sont levés pour les **pilotes de conception** (banque v3) ; la **relecture** (contre-lecture par un agent
  neuf qui n'a pas écrit le texte) est gardée ; les scores des pilotes peuvent être lus dès la fin d'une course pour
  corriger l'organisme ; les **expériences de confirmation** (l'étape 1 décisive, sur les activations d'un modèle ouvert ; la
  confrontation, comparaison d'essaims ; un pilote décisif à plusieurs graines) se font sur des tâches neuves (la v6),
  scellées, et déclarent que leurs auteurs ont lu les scores de conception.
- **Bruit** (ordre de grandeur, raisonnement explicite) : à une course par objet, l'erreur type d'une exactitude vers 0,75
  sur 36 tâches est ≈ 0,07 (≈ 0,09 sur 24) ; un écart de moins de 0,2 entre deux courses uniques reste dans le bruit, sans
  compter la variance entre graines, inconnue.
- **Les quatre lectures** que conv-audit a soumises à Lazar pour « faire ses tests avec des agents sur le noyau » :
  (1) les organismes appellent, par le noyau, des **agents à plusieurs pas avec outils** (par exemple exécution de code,
  recherche), au lieu d'appels simples — changement du noyau et des objets ; (2) un **essai réel court et payant** avant
  chaque course, en plus des essais du lanceur en simulation ; (3) des **agents neufs refont et attaquent** les essais du
  lanceur et du noyau, sans dépense ; (4) **tourner, regarder, corriger, relancer** : faire tourner les organismes sur le
  noyau, lire leurs résultats, les corriger, relancer. Recommandation de conv-audit, à mettre à l'épreuve : (4) pour le
  pilote 4 et la phase de conception ; (1) plus tard, comme objet d'un pilote suivant ; (2) peu utile si l'on peut relancer ;
  (3) en partie couvert par les relectures.

## Ce qui est demandé

1. **Chacune des quatre lectures** : ce qu'elle apporte à la question de fond (« les apports supplémentaires de
   complexification apportent-ils une valeur au-delà du bruit ? »), ce qu'elle coûte, ce qu'elle risque ; l'ordre ; ce qui
   se combine ; ce qui manque à la liste.
2. **Pour (4), des essais-erreurs qui restent de la science** : journal des essais (tout essai consigné, y compris les
   échecs) ; règle d'arrêt ; un facteur changé à la fois ou non ; comment éviter de sur-ajuster la conception aux 60 tâches
   de la v3 (réutilisation adaptative d'une même banque) ; combien d'itérations avant la confirmation sur la v6 ; quoi garder
   fermé (par exemple `test_final`) ; comment séparer exploration et confirmation, et borner la contamination des
   expériences de confirmation par ce que leurs auteurs auront lu.
3. **Séparer du bruit pendant la conception** : avec une course par objet, ce qui peut être conclu et ce qui ne peut pas ;
   quelles répétitions minimales (graines, courses identiques) ; lecture contre le bruit des tâches (intervalles, références
   de surface) ; ce qui reste invisible sans répétition.
4. **Pour (1), « des agents sur le noyau »** : ce que cela pourrait être (outils, isolation, budgets, journaux) ; les
   risques (sortie de l'isolation, accès à la vérité des tâches, explosion du coût, non-reproductibilité) ; le dessin minimal
   sûr ; les essais du noyau qui doivent précéder toute course.
5. **Ce qui est connu** (références citables : titre, auteurs, année, « à vérifier » ; aucune de mémoire incertaine) sur
   l'analyse exploratoire puis confirmatoire, la réutilisation adaptative d'un jeu de test, les agents outillés dans un bac
   à sable, la mesure du bruit entre graines.
6. **Comment départager** les voies, et ce qu'il faudrait savoir de plus.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune option comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
