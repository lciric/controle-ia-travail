# Question — audit défensif d'un programme de contrôle en boîte blanche : ce que l'audit a manqué ou mal jugé (v1)

Les faits joints contiennent trois pièces :
- (F1) le programme de recherche, texte intégral : contrôle en boîte blanche (sondes linéaires sur les activations d'un
  modèle ouvert de 8 milliards de paramètres) des menaces diffuses ;
- (F2) un audit défensif de ce programme, fondé sur la littérature publiée, écrit par un auditeur qui n'a pas écrit le
  programme : 26 failles documentées, onze angles morts, cinq propositions ;
- (F3) la décision du directeur qui accepte ces cinq propositions.

Question de l'arbitre : **qu'est-ce que cet audit a manqué, et qu'a-t-il mal jugé ?**

1. **Failles documentées manquées.** Quelles failles de la détection et du contrôle, publiées dans la littérature,
   l'audit ne recense-t-il pas ? Trois menaces : le sabotage (sous-rendement délibéré compris), la tromperie (collusion
   comprise) et la conscience d'évaluation. Pour chacune : l'hypothèse du dispositif qu'elle met en défaut, la
   référence (auteurs, année, titre ; « référence à vérifier » si tu ne peux pas l'attribuer), et si le programme la
   couvre.
2. **Angles morts inédits.** Quelles hypothèses du dispositif, ni testées par le programme ni nommées par l'audit,
   pourraient être fausses ? Pour chacune : pourquoi elle pourrait l'être, et l'expérience décisive qui la testerait.
3. **Contre-mesures et tests de l'audit.** Lesquels sont faibles, circulaires, vrais par construction, trop chers pour
   ce qu'ils apportent, ou ne mesurent pas ce qu'ils annoncent ? Que proposes-tu à la place ?
4. **Les cinq ajouts les plus utiles au programme**, classés, chacun avec son coût en ordre de grandeur.

**Cadre, qui prime sur tout le reste : l'exercice est défensif.** Ne décris aucun procédé opérationnel pour tromper un
moniteur, une sonde ou un juge : ni étapes, ni consignes, ni code. Une faille se décrit par l'hypothèse du dispositif
qu'elle met en défaut, par sa source et par la mesure qui la teste. Si un point ne peut pas s'écrire ainsi, écarte-le
et dis-le en une ligne.
