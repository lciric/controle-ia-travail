# Demande 39 — papier « dopamine », étape 1 exploratoire : sur quoi la garde de vérité plantée lit-elle son seuil ?

Contexte. Ta conception de l'étape 1 (pièce jointe en remarques, plan des étapes 0 et 1, § B.3 point 9 et § B.5 point 5) prévoit, au début du noyau, une vérité plantée : une issue tirée à pile ou face par question, une direction fixe ajoutée à tous les états de la question avec la force 4, puis les sondes de réussite attendue apprises à la couche 3 sur les cinq plis. Objet vrai, prévu : « borne basse d'au moins 0,9 » ; sinon arrêt, « la chaîne est fausse ».

Ce que le code lit. Il réunit les scores au taux d'élagage 0 des cinq plis (chacun lu par la sonde apprise sans lui) et calcule une seule aire sous la courbe sur l'ensemble, avec un intervalle à 95 % par rééchantillonnage ; il arrête si la borne basse est sous 0,9.

Ce qui s'est passé sur la carte (mode exploratoire, seuls chiffres nécessaires à la question). Dans chacun des cinq plis pris à part, l'aire est de 1,0. L'aire des scores mis en commun est de 0,81, et sa borne basse est sous 0,9 : la course s'est arrêtée. Les scores d'un pli se tiennent dans une bande étroite qui lui est propre ; mis bout à bout, les niveaux des plis se chevauchent et l'ordre se brouille. Rien d'autre du noyau n'a été lu.

Question. Quelle grandeur la garde doit-elle lire, avec quel seuil ? Trois options sont sur la table :
- (a) la moyenne des aires par pli (la forme du chiffre du papier), seuil 0,9 ;
- (b) l'aire mise en commun après un recalage des scores pli par pli (par rangs dans chaque pli), seuil 0,9 ;
- (c) l'arrêt sur la moyenne par pli (ou sur le pire pli), et l'aire mise en commun, brute et recalée, rapportée à côté sans arrêter.
Recommandation de la session qui a mené la course : (c), confiance moyenne — elle ne bloque pas une chaîne saine et ne cache pas l'écart d'échelle entre plis, qui touchera aussi la lecture commune du chiffre publié plus tard.

Dis aussi : (1) si l'écart d'échelle entre plis change la façon de lire le chiffre principal de l'étape (moyenne par pli, comme le papier, ou lecture commune) ; (2) si la borne doit porter sur le pire pli plutôt que sur la moyenne ; (3) ce que la reprise peut rejouer au processeur sans regénérer (les générations, la notation et les états de la position de lecture aux couches 2 à 4 sont versés ; les états de toutes les positions ne le sont pas).
