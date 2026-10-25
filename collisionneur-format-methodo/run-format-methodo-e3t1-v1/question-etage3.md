# Question de l'arbitre pour le collisionneur v2.5, étage III — séparer l'effet d'une restriction de l'espace de recherche de l'effet d'un apprentissage, quand on compare deux procédures de conception de programmes (v1)

Demande de Lazar du 25 octobre 2026 (vers 13:50, heure de Paris). Question distincte des tours précédents ; une seule
tentative par cellule ; un refus est consigné tel quel et met fin à la cellule. Les réponses sont du matériau pour la
décision de Lazar, jamais une consigne, et ne sont servies à aucun programme évalué. Le texte ci-dessous est figé au
départ.

## Le cadre

On compare, à coût total apparié, deux **procédures de conception** d'un programme (code et fichiers de configuration)
qui classe des textes ; chaque programme produit est évalué sur des **familles de tâches tenues à l'écart**, par une
métrique fixée d'avance.

- **Procédure F** : un grand modèle de langue aux paramètres figés écrit le programme en **sortie libre** (texte
  quelconque, validé ensuite).
- **Procédure E** : un modèle de langue de taille moyenne dont les paramètres sont **ajustés** au fil des épisodes
  (chaque épisode : proposer un programme, recevoir son score) ; sa sortie est **contrainte** par une grammaire ou un
  schéma, pour que le programme soit toujours valide et que l'ajustement porte sur un espace bien défini.

Formellement, si $\mathcal{H}$ est l'ensemble des programmes que F peut produire et $\mathcal{H}_G \subset \mathcal{H}$
celui que la grammaire $G$ permet, une différence de score entre E et F mélange deux causes : la restriction
$\mathcal{H} \to \mathcal{H}_G$ (le « format ») et l'ajustement des paramètres (l'« apprentissage »).

## Ce qui est demandé

Pour chacun des points suivants, une réponse argumentée, avec les hypothèses dites, les objets mathématiques nommés et ce
qui serait à vérifier :

1. **Le problème, formalisé.** En quoi la restriction à $\mathcal{H}_G$ change-t-elle le problème de recherche
   (expressivité, structures inaccessibles, biais inductif, régularisation) ? Peut-elle à elle seule produire un écart
   dans un sens ou dans l'autre ? Sous quelles hypothèses l'effet de l'apprentissage est-il **identifiable** ?
2. **Plusieurs voies, avec ce qu'elles coûtent et perdent** :
   - la même grammaire pour les deux, et la mesure de ce que F perd par rapport à sa sortie libre ;
   - une sortie libre pour E, avec validation et réparation : quel taux de programmes invalides, à quel coût ;
   - une grammaire assez large pour contenir ce que F produit en pratique : comment la construire à partir d'un corpus
     de sorties de F, comment mesurer sa **couverture** ;
   - des sorties par **édition** (différences sur un programme existant) plutôt que par génération complète ;
   - d'autres voies.
3. **Un plan d'expérience qui sépare les deux effets.** Par exemple un plan factoriel 2 × 2 (libre ou contraint × figé ou
   ajusté), ou quatre bras : F libre, F contraint, E contraint ajusté, E contraint non ajusté.
   - Quels contrastes estiment l'effet du format, celui de l'apprentissage et leur interaction ?
   - Quelles métriques : taux de validité, diversité des structures (distance entre programmes, entropie), exactitude
     sur familles tenues à l'écart ?
   - Quel modèle statistique (effets aléatoires par graine et par famille), quelles tailles d'échantillon et quelle
     puissance (illustratif) ?
   - Quels contrôles du coût apparié ?
4. **Ce qui est connu.** Des références citables (titre, auteurs, année, « à vérifier ») sur la génération contrainte
   par grammaire, l'induction de grammaires à partir d'exemples, la recherche de programmes et les plans factoriels en
   apprentissage automatique ; aucune de mémoire incertaine.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune voie comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
