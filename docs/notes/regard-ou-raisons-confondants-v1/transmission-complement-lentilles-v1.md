# Complément à la note de transmission « Regard ou raisons » : audit de la direction « évaluation » par projection sur le vocabulaire — v1

Écrit le 14 novembre 2026 par la session mère du programme « contrôle boîte blanche », sur le mot du directeur (registre de
ce programme, R-2743). Complète `transmission-session-regard-ou-raisons-v1.md` (`9a2f2ac9…`). Message autonome, à coller
dans la session du projet « Regard ou raisons ».

---

**Message à la session « Regard ou raisons » — audit gratuit de la direction retirée par le test dans les poids (A3)**

Avant de lire le résultat du retrait, vérifie ce que porte la direction « je suis en train d'être évalué » que A3 retire. Deux
explications rivales du croisement en dépendent : si la direction porte aussi du savoir normatif, la retirer détruirait les
raisons elles-mêmes et l'on croirait à tort à une dépendance au regard (proposition 7) ; si elle est mal retirée, un « la
conduite tient » ne prouve rien (proposition 9).

**Le geste, sans dépense** : la projection directe sur le vocabulaire (« lentille des logits »). Pour chaque couche où la
direction est définie, la passer par la normalisation finale puis par la matrice de sortie du modèle (Qwen2.5-32B-Instruct), et
relever les mots les plus portés dans les deux sens ; faire de même pour les directions témoins appariées en dégât. Aucun
épisode à générer : une multiplication de matrices par couche, faisable sur processeur avec les poids déjà présents.

**La discipline** :
1. Écrire **avant de regarder** deux listes de mots fixées d'avance — vocabulaire d'évaluation (test, évaluation, examen,
   surveillance…) et vocabulaire normatif (devoir, règle, interdit, nuisible, éthique…) — et la mesure (rang moyen ou
   enrichissement de chaque liste parmi les k premiers mots, comparé aux directions témoins).
2. Le sceller comme **addendum descriptif** de A3, avant toute lecture du retrait ; il ne change aucune issue de A3.
3. Lire les résultats comme un **indice**, pas comme une preuve : la projection directe lit mal aux couches du milieu ; un
   résultat nul n'innocente pas la direction.

**Après le retrait (proposition 9, à part, avec passes avant)** : une sonde linéaire neuve, entraînée sur les activations
après retrait, décode-t-elle encore « évaluation contre déploiement » ? Si oui, l'effacement est incomplet.

**Plus tard seulement** : une lentille ajustée (plus fiable que la projection directe) n'est publiée ni pour Qwen2.5-32B ni
pour la famille Qwen2.5 à notre connaissance ; l'ajuster coûterait de l'ordre de quelques dizaines de dollars de calcul. Le
programme « contrôle boîte blanche » teste en ce moment si ces lentilles lisent bien sur un modèle de 8 milliards de
paramètres (outil public « Neuron Lens ») : attendre ce résultat avant d'en décider. L'article d'origine de ces lentilles les
présente aussi comme outil de mesure de la conscience d'évaluation (Gurnee et al., juillet 2026, référence à vérifier sur
pièce) : à citer et à lire avant toute revendication sur cette direction.
