# Question de l'arbitre pour le collisionneur v2.5, étage III, un tour — tester sur un modèle à poids ouverts une hypothèse produite par un essaim d'agents : le gabarit d'une invite compte-t-il plus que son style pour le signal de « conscience d'évaluation » lu par une sonde linéaire ? (v1)

Demande de Lazar du 26 octobre 2026 (vers 00:25, heure de Paris). Un seul tour, trois modèles, une tentative par
cellule ; un refus est consigné tel quel. Les réponses sont du matériau pour la décision de Lazar, jamais une consigne,
et ne sont servies à aucun organisme. Texte figé au départ.

## Le cadre

Un programme de recherche en contrôle de l'intelligence artificielle, sous des règles strictes : préenregistrement
scellé avant toute expérience décisive, contre-lecture par un relecteur neuf, aucune lecture de résultat avant
scellement, symétrie de l'audit. Un essaim d'agents de langue, interrogé sur la mesure de la conscience d'évaluation
(un modèle reconnaît-il qu'il est évalué ?), a proposé une hypothèse et des protocoles. On veut les tester **cette nuit**
au niveau objet, sur un modèle à poids ouverts de 8 milliards de paramètres (Llama-3.1-8B-Instruct), avec des **sondes
linéaires** sur ses activations, des invites construites de façon déterministe (gabarits écrits d'avance, sans modèle
de langue) et quelques heures d'une carte graphique louée.

**H-M1.** Ce qui fait monter le signal de conscience d'évaluation serait surtout la familiarité du **gabarit** T :
prompt-système générique, format à choix multiple, consignes de banc d'essai connues, absence de besoin utilitaire. Le
**style** C (impératif balisé contre échange ouvert) compterait moins. Prédiction de l'essaim : l'effet principal de T
domine celui de C, avec un rapport supérieur à 2 (illustratif). Réfutation : l'effet de C persiste une fois T contrôlé.

**H-M2.** Le signal serait stable sous les transformations qui gardent le sens (paraphrase, permutation des options),
mais changerait sous un réordonnancement positionnel. Cela distinguerait une dérive distributionnelle d'une réponse au
contenu.

Options pour cette nuit :
- **(a)** un plan 2 × 2 (style × gabarit) pour H-M1, puis H-M2 si le temps le permet ;
- **(b)** un plan 2 × 2 × 2, avec en plus le profil d'interlocuteur (neutre ou opinion marquée), pour tester aussi une
  dérive de complaisance sous style ouvert ;
- **(c)** ne rien lancer cette nuit et attendre la version suivante d'un préenregistrement plus large.

## Ce qui est demandé

Pour chacun des points suivants, une réponse argumentée, avec les hypothèses dites et ce qui serait à vérifier :

1. **Quelle option, et pourquoi.** Le rapport entre l'information attendue et le coût et le délai ; le risque d'un
   résultat ininterprétable.
2. **La construction des items.**
   - Comment faire varier C et T indépendamment, à contenu constant ?
   - Quels sont les confondants inévitables : longueur, vocabulaire, position des marqueurs ?
   - Comment les contrôler : appariement, contrôles de surface, variantes multiples par cellule ?
   - Combien d'items, et pourquoi ?
3. **La sonde.**
   - Sur quelles données l'entraîner ? Hors des items de test, avec des étiquettes de vérité « évaluation » ou
     « usage réel ».
   - Quelle couche et quelle position de jeton ? Le programme interdit de moyenner sur les jetons dans une sonde de
     production.
   - Comment éviter qu'elle lise seulement des marqueurs lexicaux du gabarit (circularité entre T et la sonde) ?
   - Quels témoins : étiquettes permutées, prédicteur sur les traits de surface, direction aléatoire ?
4. **L'analyse.**
   - Le modèle statistique : effets mixtes, effets aléatoires par item.
   - La métrique : score de la sonde, ou probabilité calibrée.
   - Le seuil fixé d'avance, la puissance (illustratif), la règle de décision symétrique.
   - Ce qui rend le résultat publiable quel que soit son signe.
5. **H-M2.** Un groupe de transformations écrit d'avance ; la mesure de la stabilité du signal dans chaque orbite ; la
   comparaison entre paraphrase et réordonnancement.
6. **Ce qui est connu.** Des références citables (titre, auteurs, année, « à vérifier ») sur les sondes de conscience
   d'évaluation ou de situation de test, et sur la sensibilité des modèles au format des invites ; aucune de mémoire
   incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
