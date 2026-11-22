**D — Position méthodologique.** Je séparerais trois verdicts : « ce témoin réfute cet énoncé », « cet instrument améliore la recherche sur une population définie », « ce résultat change une décision ». Le premier peut être exact sur un seul cas ; les deux autres exigent de préciser comment les cas ont été choisis.

**Statuts.** **OBSERVÉ-NON-AUDITÉ** : les pièces A, B, C et E sont présentes, sans coupure apparente ; je n’ai pas recalculé leurs empreintes. **RAPPORTÉ** : descriptions du programme et résultats bibliographiques ci-dessous. Je ne reprends pas à mon compte les mentions « VÉRIFIÉ » des pièces. **HYPOTHÈSE** : diagnostics empiriques et protocoles que je propose. **VÉRIFIÉ** désigne ci-dessous uniquement des conséquences mathématiques dont je donne l’argument. Les constantes dans les identités mathématiques ne sont pas des mesures expérimentales.

### Ce qu’un expert ferait d’abord

**HYPOTHÈSE — Fixer le droit de conclure.** Avant de choisir un modèle, écrire, pour chaque sortie possible, *quel énoncé précis elle autorise*. Par exemple, pour une borne de puissance : quelle loi sous le nul, quelle famille sous l’alternative, quelle information disponible au temps de la décision, quel ordre entre choix du test et choix de la loi ? Pour l’organisme : cherche-t-on à augmenter la probabilité de **retrouver un résultat imposé**, ou celle de **livrer un résultat non imposé qu’un tiers utilisera** ? Je n’emploierais pas la première comme estimateur de la seconde.

### Données brutes à sceller

**HYPOTHÈSE —** Partir des sources intégrales des problèmes, avec définitions, dates, versions et preuves ; du commit Mathlib et des dépendances transitives de chaque but ; des journaux de preuve, y compris erreurs et expirations de délai ; des générateurs exacts de contre-exemples ; de l’archive horodatée des tentatives, avec témoin et hypothèses effectivement vérifiées. Pour l’utilité, demander les épisodes appariés bruts, avec unité d’échantillonnage, action disponible, coût et issue, pas seulement les scores de sonde. Je ne sais pas si ces épisodes existent.

Séparer les lots **par famille mathématique avant toute paraphrase**. Le vérificateur externe garde générateurs de réserve, vérités et verdicts. Le journal doit permettre de reconstruire ce que le proposeur *savait au moment de son choix*, pas seulement ce qu’il a finalement soumis.

### Méthodes publiées : quel résultat leur attribuer ?

**RAPPORTÉ**, sans identifiant arXiv de mémoire :

| Travail | Objet effectivement obtenu ; condition de transfert et limite |
|---|---|
| Romera-Paredes et al., 2024, *Mathematical discoveries from program search with large language models* | FunSearch fait varier des programmes, évalue leurs constructions et sélectionne les parents. Une construction de cap set améliore une borne inférieure parce que sa cardinalité et sa validité se vérifient ; le même score ne démontre pas l’optimalité. |
| Wagner, 2021, *Constructions in combinatorics via neural networks* ; Raayoni et al., 2021, *Generating conjectures on fundamental constants with the Ramanujan Machine* | Deux précédents **non assimilables à des succès de LLM** : recherche de contre-exemples combinatoires finis dans le premier ; génération de conjectures numériques dans le second. Un témoin admissible suffit à réfuter ; la précision numérique d’une identité ne suffit pas à la prouver. |
| Wu et al., 2022, *Autoformalization with Large Language Models* ; Jiang et al., 2023, *Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs* | Traduction d’énoncés, puis, dans le second travail, usage d’une esquisse pour guider la fermeture de sous-buts. Le bénéfice suppose un vocabulaire formel disponible et une décomposition correcte ; fermer un autre énoncé ne résout pas le problème initial. |
| Yang et al., 2023, *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models* | Récupération de prémisses et recherche de tactiques dans Lean sur des buts formels. Le réemploi porte sur des prémisses accessibles au point de preuve ; donner accès à un descendant du théorème cible changerait l’exercice. Ces preuves de buts fixés ne mesurent pas la découverte d’énoncés. |

### Vérification hors du programme

**HYPOTHÈSE —** Pour le **vrai**, un tiers recompile depuis les sources épinglées, vérifie axiomes et signature scellée, ou rejoue le certificat rationnel avec un vérificateur écrit à partir de la spécification plutôt que du solveur. Un mathématicien retraduit les quantificateurs avant de voir la preuve. Pour le **nouveau**, publier le résultat antérieur le plus proche, la réduction tentée et son point d’échec ; un spécialiste indépendant peut encore fournir une autre réduction. Pour l’**utile**, préenregistrer une décision et sa perte, puis comparer sur des épisodes tiers avec et sans le résultat. Rejouer le certificat et répliquer le gain de décision sont deux tâches distinctes.

Voici les objections qui déterminent ce que ces tiers devraient vérifier. Dans les rubriques **(b)**, les énoncés sont conditionnels : aucune des lois spécifiées n’est prétendue observée.

## Sur la proposition A

**(a) HYPOTHÈSE — Le problème décisif est le sens de la borne.** Si l’effet est mesuré sur une sortie \(Y=f(X)\), A obtient un *plancher* de séparation des transcriptions \(X\). Son duel D4 réclame un *plafond* de puissance. **VÉRIFIÉ** : en prenant les images réciproques des événements de sortie, \(\mathrm{TV}(P_Y,Q_Y)\leq\mathrm{TV}(P_X,Q_X)\). Une minoration du membre de gauche ne majore pas celui de droite. Même des sondes toutes médiocres ne comblent pas ce manque. Autres confusions : une publication postérieure à la coupure peut prolonger un résultat antérieur ; un échec de recherche Lean n’est pas une réfutation ; sélectionner la « meilleure lignée » sur les cibles du duel biaise le comparateur.

**(b) VÉRIFIÉ — Conditions de perte de puissance ou d’identification.**

- **D1, D3, nouveauté.** Si le score \(S\) a même loi conditionnelle pour les deux étiquettes, tout seuil donne rappel égal au taux de fausses alertes. Si la strate postérieure est un mélange \(rF_{\rm exposé}+(1-r)F_{\rm inédit}\), la loi marginale seule n’identifie pas \(F_{\rm inédit}\) pour \(r\) inconnu. Pour D1, estimer l’écart *apparié par famille* ; si l’intervalle de cet écart traverse le gain minimal fixé, aucun vainqueur.
- **D2, preuve, fidélité, archive.** Pour \(T\) temps de clôture et \(b\) budget, si \(\Pr(T>b\mid vrai)=\Pr(T>b\mid faux)\), le timeout ne discrimine pas. Pour un témoin de mutation, de lemme faux ou de mort archivée, si sa région de violation a masse \(p\), la probabilité de la manquer sur \(n\) essais indépendants est \((1-p)^n\). À \(p=0\), ajouter des graines est inutile.
- **D4.** Pour tout événement d’alerte \(D\), \(Q(D)\le P(D)+\mathrm{TV}(P_X,Q_X)\). Sans majorant indépendant de cette dernière distance inférieur à \(1-P(D)\), cette inégalité ne fournit pas de plafond non trivial. Pour la recherche évolutionnaire, si les lois du meilleur score certifié à budget égal sont identiques, le gain de sélection est nul, même si le record augmente en cours de recherche.

**(c) HYPOTHÈSE — Contrôles indispensables.** Lignée sélectionnée sur un lot distinct ; théorème tardif qui est un corollaire ancien ; preuve vraie difficile avec expiration du délai ; reformulation vraie voisine d’un mort. Pour D4, employer **le même déplacement de sortie avec deux degrés différents de séparation des observations** : un instrument qui annonce le même plafond à partir du seul déplacement échoue à ce contrôle.

## Sur la proposition B

**(a) VÉRIFIÉ — Apparier les moments ne rend pas les sondes à seuil aveugles.** Exemple mathématique illustratif : \(P\) donne des masses égales à \(-1,1\) ; \(Q\) donne masse \(1/2\) à zéro et \(1/4\) à chacun de \(\pm\sqrt2\). Moyenne et variance coïncident, mais le demi-espace \(x>1\) a probabilités respectives \(0\) et \(1/4\). Le duel P3 part donc d’une famille de référence mal caractérisée. Une paire extérieure à cette famille ne bat pas nécessairement son optimum. **HYPOTHÈSE** : P1 confond réfuter *une réduction* et exclure *toutes les réductions* ; P4 recycle les sources du juge ; P5 confond diversité des témoins et valeur de réemploi.

**(b) VÉRIFIÉ —**

- **P1/P4.** Avec un label expert \(J\) de sensibilité \(s\), spécificité \(c\) et prévalence réelle \(\pi\), \(\Pr(J=1)=s\pi+(1-c)(1-\pi)\). Sans étalon indépendant, cette fréquence n’identifie pas \(\pi\) ; à \(s+c=1\), elle n’en dépend même pas. Un taux sur mutants n’estime le taux cible que sous une loi de mutations spécifiée.
- **P2/P3.** Si la loi d’évaluation des paramètres ne charge pas la région d’écart strict, la probabilité observée de séparation est nulle même si cette région existe. L’avantage pertinent pour P3 est \(\sup_{H\ {\rm demi\text{-}espace}}|P(H)-Q(H)|\), pas un estimateur d’écart de covariance. Le ratio effet/avantage est indéfini au dénominateur nul.
- **P5.** Pour des classes de masses \(p_j\) tirées indépendamment, le nombre moyen de classes vues vaut \(\sum_j[1-(1-p_j)^n]\). Permuter l’ordre de l’archive laisse le compte strictement invariant. Il ne renseigne pas la probabilité, sous une autre loi de problèmes, de réfuter le prochain énoncé faux.

**(c) HYPOTHÈSE —** Ajouter une réduction valide passant par un autre classique que celui suggéré ; une paire à moments égaux mais distingable au seuil, et \(P=Q\) comme véritable nul ; des énoncés corrects réécrits avec les mêmes marqueurs de style que les mutants. Comparer l’archive à des témoins de même taille appariés à la mauvaise conjecture, en revérifiant leur admissibilité. Pour P2, le cas indépendant ne contrôle le pire couplage que si l’indépendance est effectivement imposée au solveur.

## Sur la proposition C

**(a) HYPOTHÈSE — Les deux bras peuvent tomber d’accord sur la même erreur.** Ajuster \(U\) aux sorties qui ont servi à choisir \(L\), puis mesurer leur proximité sur ces mêmes sorties, n’est pas un test de dualité. Un témoin contre *un* moniteur n’est pas automatiquement une borne contre *tous*. Le portier des sous-lemmes sélectionne les lemmes traduisibles ; ses faux rejets disparaissent des statistiques si seuls les survivants sont relus. Enfin, le temps de `aesop` mesure un environnement de preuve, pas une date de publication.

**(b) VÉRIFIÉ —**

- Pour une valeur \(v\), si \(\widehat U=v+B\) et \(\widehat L=v+B\) avec \(\Pr(B\ne0)>0\), l’écart mesuré est nul presque sûrement malgré le biais commun. L’écart relatif n’est pas défini à \(v=0\).
- Avec \(R\) indicateur de traduction, \(\Pr(R=1\mid famille)=0\) rend le taux de détection conditionnel inestimable dans cette famille. Pour un mutant d’hypothèse, si la loi des mondes donne masse nulle aux violations de la formule réparée, son taux de survie vaut l’unité quelle que soit sa validité ailleurs.
- Si le temps tactique a même loi sous « antérieur » et « sans antécédent dans le corpus », son AUC avec demi-crédit aux égalités vaut \(1/2\). Si l’audit humain n’échantillonne jamais les rejets, sa probabilité d’inclusion y est nulle : le taux global de faux rejets n’est pas identifié.

**(c) HYPOTHÈSE —** Vérifier la faisabilité de chaque côté séparément sur la spécification originale ; introduire une même constante erronée dans les deux estimations. Opposer aux sous-lemmes faux, qui sont des **positifs** de détection, des sous-lemmes vrais dont la traduction numérique échoue. Tester une réparation tautologique, une hypothèse retirée mais redondante, un classique lent à prouver ; tirer au sort aussi des dossiers rejetés pour la relecture.

## Sur la proposition E

**(a) HYPOTHÈSE — L’objet à interpoler n’est pas nécessairement identifiable.** Un LP peut avoir une face entière d’optima : l’instabilité du multiplicateur choisi par le solveur ne condamne pas une formule de valeur. L’alphabet fini ne garantit pas à lui seul un LP rationnel, encore moins un optimum rationnel de SDP. En M2, le verdict répété de la banque « scellée » entraîne indirectement le raffineur. En E4, passer du fini au général change à la fois la représentation et le théorème. En M3, battre une liste de bornes est relatif à la liste.

**(b) VÉRIFIÉ —**

- Si \(Y^*\mid m\) suit plusieurs sélections optimales, \(\operatorname{Var}(Y^*\mid m)>0\) est compatible avec \(\operatorname{Var}(v^*\mid m)=0\). Si la probabilité qu’un optimum requis admette le certificat rationnel demandé est nulle, le taux de certification exacte de cet optimum vaut zéro indépendamment du prouveur.
- Pour \(h\) choisi en maximisant la couverture empirique, \(\mathbb E\max_h\hat p_h\ge\max_h\mathbb E\hat p_h\). De plus, une fréquence sous la loi honnête \(P\) n’identifie pas une propriété sous \(Q\) si \(Q\) charge une région de masse \(P\) nulle. Une propriété de loi, telle que l’indépendance, n’a pas en général d’indicateur vrai/faux par épisode isolé.
- Si les deux bras d’E4 n’ont aucun support commun en couple *(généralité, représentation)*, leur différence de succès n’identifie pas l’effet propre de représentation. En E3, avec probabilité d’erreur \(p>0\), zéro défaut sur \(n\) essais indépendants garde probabilité \((1-p)^n\). Pour E1/M3, le rappel sur les classiques inclus n’identifie pas le rappel sur une source d’antécédents de probabilité d’inclusion nulle.

**(c) HYPOTHÈSE —** Changer la règle de départage du solveur sans changer la valeur ; évaluer les hypothèses choisies sur une banque jamais interrogée ; comparer deux encodages du *même théorème fini* ; cacher un classique qui domine tous les comparateurs visibles. Pour la réplication, inclure une politique qui change les alertes mais pas la décision finale : elle doit obtenir un gain décisionnel nul si les coûts restent identiques.

### Demande reformulée

**HYPOTHÈSE —** « Livrer soit une réduction publiée, soit un énoncé à quantificateurs scellés avec preuve ou réfutation rejouable. Indiquer séparément l’écart au meilleur antécédent trouvé et la décision dont la perte pourrait changer. Pour attribuer un gain à l’organisme, annoncer avant la recherche le comparateur, la population de familles, le budget total et la règle d’abstention. »

### Méthodes que D engagerait

- **HYPOTHÈSE — Certifier une frontière de décision plutôt qu’interpoler un optimum.** Pour un jeu d’audit fini, premier pas : fixer des politiques admissibles et chercher un intervalle de coûts sur lequel la politique optimale change, avec comparaison exacte des pertes et certificat contre *toutes* les politiques admissibles. Duel sur l’intervalle annoncé : \(H_A\), changement strict certifié ; \(H_B\), aucun changement strict. Un témoin avec certificats réfute \(H_B\) ; une dominance uniforme certifiée réfute \(H_A\) ; timeout sans verdict. Coût illustratif : jours de probabiliste et de calcul CPU, avant toute course de modèles. Différence avec la recherche de constructions : le produit est un domaine de décision prouvé, non un record. Son antériorité en jeux d’inspection reste à vérifier.
- **HYPOTHÈSE — Chercher le plus petit budget d’observation qui justifie une décision donnée.** Premier pas : sur un arbre fini d’observations, fixer perte cible et lois admissibles ; demander une politique certifiée au budget proposé et une borne d’impossibilité au budget immédiatement inférieur. Duel à budget fixé : \(H_A\), perte cible atteignable ; \(H_B\), perte cible inatteignable. Politique admissible ou certificat de séparation réfute respectivement l’autre hypothèse. Mort comme découverte si le seuil découle d’un jeu publié par simple substitution ; abandon technique, sans conclusion mathématique, si l’encodage indépendant ne reproduit pas les pertes. Coût illustratif : jours d’expert pour la spécification, puis une course dans l’enveloppe rapportée. La distinction recherchée est le seuil pour **l’information effectivement disponible** au contrôleur, pas une nouvelle méthode générale de programmation dynamique.

Je ne sais pas estimer la chance qu’un de ces seuils soit inédit. Je réserverais le temps humain à la vérification de l’ordre des quantificateurs et à l’antériorité **avant** de payer pour une preuve longue : une preuve exacte ne corrige ni une décision mal posée ni une redécouverte.

FIN-DE-CELLULE