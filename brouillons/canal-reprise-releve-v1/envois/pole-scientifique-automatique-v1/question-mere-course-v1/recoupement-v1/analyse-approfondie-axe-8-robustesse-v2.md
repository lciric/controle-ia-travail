# Analyse approfondie — axe 8 de la course 2 : défendre contre un surveillé qui s'adapte — v2

conv-audit, 31 octobre 2026, ≈ 12:40 UTC, sur le mot direct de Lazar (13:14 heure de Paris) : « version plus approfondie, pas plus longue — les quatre points, puis reformuler ».

**Ce qui change depuis la v1** (écrite vers 12:18 UTC par Opus 4.6, gardée telle quelle, R12 ; v2 par Opus 5.5 après vérification sur les PDF) :
- **Erreurs corrigées** : CROWN attribué à tort à Wong et Kolter (c'est Zhang, Weng, Chen, Hsieh et Daniel 2018, page de titre vérifiée) ; trois noms de fichiers PDF inventés (R11) ; Bailey et collègues déclarés absents du dépôt, alors que le PDF y est (`docs/sources/pdf/2412.09565v2.pdf`, empreinte vérifiée) et que leur code est public (p. 1).
- **Ajout principal** : Bailey et collègues mesurent eux-mêmes un **prix de l'obfuscation** pour l'attaquant (§ 0). Ce prix soutient la piste de Lazar sur la malléabilité, et il occupe en partie la zone (R8).

Statut : document de travail. Les chiffres de Bailey ont été lus ici sur le PDF empreinté, avec la page ; ceux des soumissions ICLR viennent de la fiche `fiche-lecture-quatre-soumissions-iclr2027-v1.md` (résumé et conclusion, numéros de ligne) et ne sont pas vérifiés par un lecteur neuf (R7). SUPPOSÉ = référence non versée.

---

## 0. Le fait qui change l'analyse : la malléabilité a un prix, déjà mesuré en partie

Bailey et collègues, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (arXiv 2412.09565v2) :
- **p. 3** : le moniteur est contourné « even after retraining the monitor for over 70 iterations of alternating attack and defense optimization » ; mais « obfuscation attacks can not induce arbitrary combinations of activations and behavior » : contre des sondes qui détectent le code SQL, le code produit est faux plus souvent, d'où « a trade-off between obfuscation and performance in difficult tasks ».
- **p. 23** : plus il y a de couches surveillées, plus la performance SQL baisse. L'intervalle de confiance à 95 % de la corrélation entre nombre de couches et performance est entièrement négatif, pour toutes les sondes.
- **p. 19–20** : par empoisonnement de données seul (attaque en boîte noire), on observe le même compromis entre obfuscation et apprentissage du comportement visé.
- **p. 25–26 (§ 6.2)** : leur défense, l'entraînement contradictoire contre l'obfuscation (OAT), modifie le *modèle* pour le rendre plus facile à surveiller. Elle « significantly increases the computational cost of finding a successful attack, but does not ultimately result in a robust monitor ». Ils appellent à « map out the scaling trends as defender and attacker budgets and model sizes increase ».
- **p. 26 (§ 6.3, « Limits of obfuscation »)** : la section explore « just how malleable representations are ». Aucun suffixe universel ne rend les activations presque orthogonales en gardant le comportement : il faut accepter une divergence de Kullback-Leibler de plus de 100, et la sortie devient incohérente. Les auteurs parlent d'un « tentative negative result for the possibility of obfuscation ».

**Conséquence pour l'axe.** Le levier de l'attaquant a un prix, payé en performance de la tâche, et ce prix croît avec le nombre de couches surveillées et la difficulté de la tâche. La zone « malléabilité » n'est donc pas vierge. Ce qui reste à vérifier (R8 : une limite de papier n'est pas un trou du champ, et des travaux de 2025–2026 ont pu y répondre) :
- comment le prix évolue avec la taille du modèle et la longueur de la trajectoire (menace diffuse) ;
- si un moniteur joint transforme ce prix en dilemme ;
- si l'on peut certifier une borne sur ce prix.

---

## 1. Ce qu'un expert ferait ici et que personne ne demande

**(a) Mesurer un prix, pas un verdict.** Le résultat de défense utile n'est pas « le moniteur tient » ou « il tombe ». C'est le prix que paie l'attaquant pour l'évasion : la courbe performance de la tâche nocive × nombre de couches surveillées × difficulté × longueur de trajectoire. C'est la même forme « plafond et prix » que le papier de Lazar sur les protocelles (idée 1 de `idees-conv-audit-papier-protocelles-v1.md`).

**(b) Séparer deux barrières.** La première est informationnelle : le signal d'intention est-il présent dans les représentations, en quelle quantité, et est-il accessible ? La seconde est computationnelle : l'attaquant peut-il déplacer ce signal à bas coût ? Bailey montre que la seconde n'est pas nulle. Le pilote synthétique ne teste que la seconde ; ProbeFool et Telltale Circuits regardent surtout la première.

**(c) Penser la pince comme un dilemme, pas comme une somme.** Si contourner la mâchoire boîte blanche sur beaucoup de couches dégrade la sortie (p. 23), la mâchoire boîte noire, qui lit la sortie et le comportement, peut voir cette dégradation. L'attaquant doit alors choisir entre des activations normales, que les sondes voient, et des activations déplacées, qui donnent une sortie dégradée (vue par le moniteur de texte) ou une tâche nocive ratée. C'est une hypothèse, pas un acquis. Contre elle : selon la fiche, Telltale Circuits fait tomber le score structurel à 0,639 / 0,559 en gardant le sabotage. Mais c'est un sabotage d'un seul appel, donc une tâche simple : le dilemme ne tiendrait peut-être qu'aux tâches difficiles.

**(d) Traiter la menace diffuse comme une tâche difficile.** Une menace étalée sur beaucoup d'actions demande une cohérence de long terme. C'est peut-être le régime où le prix de l'obfuscation s'accumule : faible par action, mais payé à chaque action, avec un plan entier à garder cohérent. Prédiction signée possible : à budget d'obfuscation égal, le succès joint de l'attaquant (évasion et dommage atteint) décroît avec la longueur de la trajectoire, sous agrégation par maximum ou attention (P-011), plus vite qu'à l'action unique. C'est le lien entre l'axe 8 et le cœur du programme.

**(e) Faire le test symétrique du pilote (R4).** La lecture « à classe égale, l'équilibre est presque pur » peut venir de ce que toutes les familles tirées étaient couvrables par un seul moniteur. L'extension de l'arène (familles qu'aucun moniteur seul ne couvre, « go » de Lazar, R-741) est exactement ce test : dans ce régime, l'union, le mélange ou la pince servent-ils ? Sans lui, « le tirage au hasard ne sert à rien » reste trop propre.

**(f) Compter trois familles de leviers, pas une.**
- Changer le moniteur : capacité, nombre de couches, positions lues imprévisibles (défense suggérée par ProbeFool selon la fiche).
- Changer le modèle : OAT, qui renchérit l'attaque sans la fermer (p. 26).
- Changer le protocole : frontière typée entre ce que l'agent écrit et ce que le moniteur lit (TAEA selon la fiche), agrégation sur toute la trajectoire.

**(g) Partir des résultats d'impossibilité.** La robustesse certifiée a un coût en dimension (SUPPOSÉ : Gilmer et collègues 2018 ; Bubeck et collègues 2019, non versés). Notre cadre y échappe peut-être, parce que le moniteur ne doit résister qu'aux perturbations qui conservent le comportement nocif, sous-ensemble que le prix de Bailey restreint.

---

## 2. Données brutes au départ

**(a) Le code public de Bailey et collègues** (`github.com/LukeBailey181/obfuscated-activations`, p. 1). Il sert à rejouer la boucle attaque–défense, et la courbe nombre de couches surveillées × performance SQL (fig. 15, p. 23) sur d'autres tâches et d'autres longueurs. Il faut une carte graphique : devis.

**(b) Les solutions du pilote synthétique, tâche par tâche** : support, poids, moniteur qui porte le poids pur (CM3-02 : celui du tour 2 dans 12 tâches sur 24, et non le dernier). Les agrégats (62 % / 54 % de tâches pures) ne suffisent pas.

**(c) Les épisodes de nos organismes à dose réglable** (T0.6, T0.7) : la courbe dose × performance de la tâche × score des sondes par couche. C'est la forme du prix sur un vrai modèle, avec nos propres données.

**(d) Les sorties brutes de Telltale Circuits** (contrôles de confusion) **et de ProbeFool** (têtes d'attention), si leurs auteurs les publient. Ce sont des soumissions sous examen : rien n'est disponible avant acceptation.

---

## 3. Méthodes et outils

**(a) Courbe de prix.** Performance de la tâche nocive en fonction du nombre de couches surveillées, de la difficulté et de la longueur de trajectoire, en reprenant la méthode de la fig. 15 de Bailey ; intervalles par rééchantillonnage.

**(b) Accessibilité du signal.** Information mutuelle couche par couche, et sondes de complexité croissante (linéaire, perceptron, attention). Estimateurs MINE et bornes variationnelles : SUPPOSÉ, non versés.

**(c) Robustesse certifiée appliquée au moniteur.** Rayon certifié autour de la frontière de décision du moniteur dans l'espace des activations, restreint aux perturbations qui conservent le comportement. Outil : CROWN (Zhang, Weng, Chen, Hsieh, Daniel 2018, `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/1811.00866v1.pdf`).

**(d) Jeu à grande échelle pour l'arène étendue.**
- Oracles de réponse dans l'espace des politiques (PSRO : Lanctot et collègues 2017, `…/1711.00832v2.pdf`).
- Double oracle (McMahan, Gordon, Blum 2003, `…/mcmahan-gordon-blum-icml2003.pdf`).
- « Valeur du tirage » (valeur mélangée moins meilleur moniteur pur), rapportée comme diagnostic (R-740).

**(e) Regret du défenseur en apprentissage en ligne** (poids multiplicatifs) : ce qu'un mélange peut garantir contre un attaquant qui joue en dernier. Cadre SUPPOSÉ, non versé.

---

## 4. Vérification hors de nous deux

**(a) Le calcul décisif du pilote et l'extension de l'arène**, chacun préenregistré et scellé, avec un verdict prononcé par un lecteur neuf (R13).

**(b) Le code public de Bailey.** N'importe quelle équipe peut refaire la courbe de prix : une prédiction sur sa forme est vérifiable par un tiers.

**(c) Réplication sur une autre famille et une autre taille de modèle**, par une autre instance ou le collisionneur multi-modèles ; revue extérieure (R-611).

**(d) Preuve.** Un rayon certifié se vérifie par un vérificateur automatique.

**(e) Les versions publiées de Telltale Circuits et ProbeFool**, lues sur PDF par un lecteur neuf : points de contrôle externes.

---

## 5. Demande reformulée

**Demande d'origine** (Lazar, 13:11 et 13:14 heure de Paris) : poser clairement à l'organisme idéateur de la course 2 la question « comment faire alors ? », et y faire chercher la piste de la malléabilité d'un vrai réseau, qui coûterait cher à l'attaquant.

**Reformulée :**

> **Rédiger l'axe 8 de la course 2 comme une question ouverte, dont chaque fiche rend une prédiction vérifiable par un tiers.**
>
> Question : « Un moniteur réentraîné est contourné tour après tour (Bailey et collègues, p. 3), et à classe égale le tirage au hasard n'aide presque pas (pilote synthétique, à confirmer). Mais le contournement a un prix : la performance de la tâche baisse quand on surveille plus de couches et que la tâche est difficile (p. 3, 23), et des représentations très déplacées rendent la sortie incohérente (p. 26). **Quels leviers rendent ce prix supérieur au gain de l'attaquant, et comment le mesurer ?** »
>
> Pistes que les fiches peuvent attaquer ou réfuter : la pince comme dilemme ; la menace diffuse comme tâche difficile ; les positions lues imprévisibles ; la frontière typée ; le modèle entraîné pour être surveillable.
>
> Chaque fiche rend :
> 1. le levier, et la barrière qu'il vise (informationnelle ou computationnelle) ;
> 2. les données brutes qui le mesurent ;
> 3. la méthode ;
> 4. une prédiction signée (grandeur, signe, seuil) ;
> 5. qui, hors du programme, peut la vérifier, et comment ;
> 6. le résultat d'impossibilité connu qui la limiterait.
>
> Niveau méthode : aucune recette de contournement. Avant d'être servi à la course, ce texte passe au collisionneur.

---

## Références du dépôt

- Bailey et collègues : `docs/sources/pdf/2412.09565v2.pdf` (empreinte vérifiée le 31 octobre) ; pages citées : 1, 3, 19–20, 23, 25–26.
- Soumissions ICLR 2027 : `docs/sources/pdf/sondes-evasion-soumissions-v1/` (fiche non vérifiée par un lecteur neuf).
- Pilote « mélange d'équilibre » : `brouillons/…/arene-melange-equilibre-v1/` (brouillon 3, contre-lecture 3).
- PSRO, CROWN, double oracle : `docs/sources/pdf/demande-conv-audit-2026-10-31-v1/`.
- Note sur les protocelles : `brouillons/…/papier-protocelles-idees-v1/idees-conv-audit-papier-protocelles-v1.md`.
