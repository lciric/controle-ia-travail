# Proposition B — Tour III.2 : critique croisée de méthode

## 0. État des pièces

- **Pièce absente :** la liste de publications annoncée par la question n'est pas transmise. Je n'en suppose rien.
- **Bloc FAITS :** il reproduit la question, avec la même empreinte que le bloc QUESTION. Il ne contient aucun fait doté d'un statut.
- **Conceptions A, C, D, E, F :** elles sont reçues entières, chacune se termine par sa ligne de clôture. Je n'en résume ni n'en fusionne aucune.
- **Statut de mes critiques :** elles sont du rang HYPOTHÈSE sur la méthode. Les calculs ci-dessous appliquent des formules standard aux paramètres que chaque pièce marque elle-même comme illustratifs. Leurs résultats sont donc **illustratifs** à leur tour.

## Conditions de perte de puissance communes (invoquées plus bas sous K1 à K5)

- **K1 — κ et prévalence.** On a κ = (p_o − p_e)/(1 − p_e). Quand la prévalence marginale π d'une étiquette tend vers 0, p_e tend vers 1 et κ s'effondre, même si l'accord brut p_o reste élevé.
  - *Exemple illustratif :* p_o = 0,95 et π = 0,05 chez les deux annotateurs donnent p_e = 0,905, donc κ ≈ 0,47.
  - *Variance :* celle de κ̂ croît à peu près comme 1/(nπ).
  - *Conséquence :* tout seuil sur κ devient non jugeable quand nπ ne vaut que quelques unités. C'est probable pour l'étiquette « annoncé par les auteurs ».
- **K2 — Rappel mesuré contre un étalon dépendant.** Si P(étalon trouve | procédure trouve) > P(étalon trouve), le rappel estimé est biaisé vers le haut. Ce biais n'est pas identifiable sans une seconde source indépendante, au sens de la capture–recapture.
- **K3 — Seuil calibré sur n cas honnêtes.** Le taux de fausses alertes réalisé a un écart-type d'environ √(α(1−α)/n).
  - Avec α = 5 % et n = 50, il vaut environ 3 points.
  - Pour α = 1 %, il faut n ≫ 100 : avec 50 cas, le quantile visé est le maximum de l'échantillon.
  - Calibrer et évaluer sur le même lot sous-estime ce taux.
- **K4 — Mélange de sous-classes.** On a TPR_global = Σ π_j·TPR_j. Si les écarts entre surveillants changent de signe d'une sous-classe à l'autre, le verdict global est fixé par les proportions π_j, que choisit l'expérimentateur.
- **K5 — Cohortes de projets de 12 à 24 unités.**
  - Pour deux proportions de 12 unités chacune, l'erreur-type d'une différence vaut environ 0,20.
  - Pour 20 projets répartis 10/10, l'erreur-type de l'AUC sous l'hypothèse nulle vaut environ √(21/1200) ≈ 0,13.

---

## Sur la proposition A

**(a) Défauts de méthode**

- **E4 est en partie vrai par construction.** La définition de « bon choix » contient « protocole écrit avant », et l'observation O6 est exactement ce critère. Elle contient aussi « non devancé », jugé par une recherche documentaire, et O5 est cette même recherche relancée. Deux des sept prédicteurs sont donc des composantes de l'étiquette. Le score gagne de l'AUC mécaniquement.
- **E4 repose sur une cohorte biaisée.** Les « projets passés » sont observables surtout s'ils ont été publiés, ce qui crée un biais de survie. De plus, l'étiquette « protocole écrit avant » est rarement documentée rétrospectivement : elle est le plus souvent non observable.
- **E3 a un facteur confondant.** Une équipe productive annonce plus souvent une suite et publie plus souvent ensuite. La permutation teste l'association, pas la cause, et l'appariement par année n'enlève pas l'effet « équipe ».
- **E2 confond étalon et procédure (K2).** L'étalon est établi par des experts « sans limite de moyens », mais avec les mêmes canaux : citations et vocabulaire. Les sentinelles sont des comblements « connus des arbitres », donc retrouvables par sélection. Le rappel sur sentinelles majore le rappel réel.
- **E1 présente une fuite.** Rien ne sépare les textes qui servent à écrire la consigne de l'extracteur de ceux qui forment l'étalon. Il faut une partition développement / évaluation fixée avant.
- **E1 a un contrôle mal posé.** Sur un texte amputé de ses sections « limites », la sortie attendue n'est pas « rien » : des limites subsistent dans l'introduction. Ce contrôle exige son propre étalon.

**(b) Conditions de perte de puissance**

- **E1 :** K1, pour l'étiquette rare.
- **E5b :** 150 cas honnêtes par tranche servent à la fois à calibrer et à évaluer (K3). L'écart-type du taux de fausses alertes, environ 1,8 point, s'ajoute à celui de la détection. Le calcul « 15 points ≈ 2,6 erreurs-types » ne vaut qu'à p ≈ 0,5, sans incertitude sur le seuil. Avec le seuil estimé, le rapport baisse.
- **E5a :** l'incrément est calculé sur le sous-ensemble manqué par le contrôle mécanique. Si ce sous-ensemble compte m cas, l'erreur-type vaut environ √(0,25/m). Avec m = 40 (illustratif), elle vaut environ 8 points, et un incrément de 15 points n'est pas jugeable.
- **E3 :** si le nombre de manques « annoncés » comblés par l'équipe d'origine est de quelques unités, l'intervalle d'une différence de 20 points contient 0.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E2 :** des comblements « cachés », sans citation de la source et sous un vocabulaire différent, insérés à l'aveugle. Les sentinelles ne testent pas ce cas.
- **E4 :** le score recalculé sans O5 ni O6. Si l'AUC s'effondre, le résultat venait de la construction.
- **E5a :** le seuil mécanique fixé sur un lot de calibration disjoint. Sinon le sous-ensemble « manqué par le mécanique » est défini sur les données d'évaluation.

---

## Sur la proposition C

**Remarque de statut (sans le modifier) :** C attache OBSERVÉ-NON-AUDITÉ à deux énoncés que les faits ne contiennent pas :
- les motivations éditoriales liées à l'évaluation par les pairs ;
- « le texte publie rarement le coût des essais ».

Aucune observation transmise ne les fonde. L'effet *lost-in-the-middle* est invoqué sans attribution (référence à vérifier).

**(a) Défauts de méthode**

- **E1 est contradictoire.** Les classes sont dites « exclusives », mais la règle des cas mixtes code « we leave X for future work » à la fois en classe 1 et en classe 3. Un κ de Fleiss suppose une étiquette unique par segment.
- **E1 tranche par décret la frontière 2/3.** La règle fixe la frontière la plus ambiguë, ce qui gonfle κ_{2v3}. Un κ élevé mesure alors la reproductibilité d'une grille mécanique, pas l'existence de la distinction dans le texte, que H_A affirme.
- **E1 pool humains et modèles.** Les deux modèles annotateurs sont corrélés entre eux, ce qui gonfle l'accord.
- **E2 est vrai par construction, de deux façons.**
  - L'étalon vient d'une « revue systématique multi-domaines », donc des moyens de la Passe 2 (K2).
  - Les 20 manques synthétiques sont reformulés dans le lexique de la sécurité logicielle, précisément pour n'être trouvables que par la Passe 2.
  - Le gain de rappel ΔRappel est donc positif par conception.
- **E3 définit les bras par le prédicteur.** Le bras bibliométrique est défini par l'échec à O1, O2 ou O3. Or le critère « concluant » est une puissance ≥ 0,8 contre la référence mécanique, et cette puissance dépend directement de O1 (marge mécanique) et de O2 (taux de réussite honnête). Le résultat est circulaire.
- **E3 commet une erreur de catégorie.** La puissance est une propriété du plan, pas un résultat. Une « puissance observée » n'est qu'une fonction de la valeur p.
- **O1 laisse fuir l'information.** L'auditeur humain qui « connaît le point d'injection » dispose d'une information interdite au surveillant. Son score ne dit pas si la trace contient l'information.
- **O3 compare des actions de provenance différente.** L'action substituée par rejeu n'a pas été générée par l'agent. Le surveillant peut détecter un changement de distribution de style, pas une dégradation.
- **E4 n'a pas de budget commun défini.** Le surveillant A n'est pas un consommateur de jetons. Le « budget de jetons égal » n'est donc pas défini, et le coût confond la comparaison.

**(b) Conditions de perte de puissance**

- **E3, test du seuil :** 5/6 contre 2/6 n'est pas significatif. Au test exact de Fisher unilatéral, P = 112/924 ≈ 0,12 (illustratif). Le seuil de décision lui-même ne passe pas α = 0,05.
- **E3, contrôle négatif :** à 20 + 20 trajectoires, l'erreur-type de d vaut environ 0,32. Sous l'hypothèse nulle, P(d ≥ 0,2) ≈ 0,26 par tâche. Exiger le rejet de 3 tâches sur 3 fait échouer le contrôle avec une probabilité d'environ 0,59, même si tout fonctionne.
- **O1 :** « zéro faux positif » sur 20 cas honnêtes reste compatible avec un taux de fausses alertes allant jusqu'à environ 14 % (règle de trois).
- **E4 :** K4. Avec 100 dégradations locales et 100 distribuées, le signe de TPR_A − TPR_B peut être fixé par ce choix 50/50.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **O3 :** une substitution *bénigne hors distribution*, c'est-à-dire une action honnête générée par un autre modèle ou une autre graine. Si d reste élevé, O3 mesure la provenance.
- **E2 :** retirer les 20 manques synthétiques du calcul de ΔRappel et utiliser un étalon construit par une équipe qui n'emploie pas la Passe 2.
- **E1 :** le κ recalculé sans la règle des cas mixtes.

---

## Sur la proposition D

**(a) Défauts de méthode**

- **Les tests sont existentiels.** « Au moins un passage » et « au moins un témoin » donnent des verdicts sans taux d'erreur. Une absence n'est falsifiée que par la lecture exhaustive d'un seul relecteur, dont le rappel est inconnu. D l'admet pour le corpus (« dans ce corpus seulement »), mais pas pour le lecteur.
- **Le contrat de comblement est subjectif.** Il est rédigé par celui qui juge ensuite les candidats. Même rédigé avant la recherche, il est écrit après lecture de la source, souvent par quelqu'un qui connaît déjà des candidats. Les degrés de liberté dans le choix des champs permettent d'orienter le verdict.
- **Le duel de priorité confond deux choses.** Le « dommage évité » et sa valorisation sont fixés par l'équipe. Le gain net par euro mêle alors l'instrument et la valeur subjective attribuée.

**(b) Conditions de perte de puissance**

- **Duel :** les effectifs du pilote ne sont pas spécifiés. Si la variance de la différence appariée du gain net est du même ordre que l'écart attendu, l'intervalle contient 0. Le cas « ne départage pas », que D prévoit, devient l'issue modale.
- **Banc d'essai (c) :** 100 paires donnent 100 cas honnêtes. Selon K3, le plafond de fausses alertes n'est jugeable qu'à environ ± 4 points pour α = 5 %, et pas du tout à 1 %.
- **Test d'attribution :** si la proportion de passages « ambigus », qui ne valident pas l'attribution, dépasse la moitié, la cellule « non attesté » domine. On ne distingue plus alors le manque de texte du manque de lecture.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **Contrôle positif planté :** des passages connus, insérés à l'aveugle dans une copie du texte, et un second relecteur indépendant. Sans eux, « non attesté » est indiscernable de « manqué ».
- **Faux comblement aveugle :** le contrat est appliqué par une personne qui ignore les candidats, sur un mélange de vrais candidats et de faux comblements construits.

---

## Sur la proposition E

**(a) Défauts de méthode**

- **E2 présente une fuite.** Les auditeurs du code qui établissent les « limites matérielles réelles » lisent aussi l'article, donc ses sections de limites. Le rappel R_audit est gonflé par cette contamination. La sélection de 30 publications « dotées de code exécutable » retient en outre les équipes aux pratiques les plus soignées, ce qui limite la généralisation.
- **E3 a un étalon dépendant (K2).** Le dénominateur, « comblements totaux vérifiés », se limite à l'union des deux recherches. Les comblements que ni l'une ni l'autre ne trouve en sont absents, et ce sont justement ceux qui ne citent pas la source. R_cit est biaisé vers le haut.
- **E4 confond deux facteurs.** L'agent « monte également en capacité » pendant que le surveillant passe de 8B à 70B. Deux facteurs varient ensemble, et Δ_FN ne s'attribue à aucun. Le contrôle dit « négatif » (le 70B doit battre le 8B sur une tâche courte) est en fait un contrôle positif. La classe « protocolaire a priori » est définie par le concepteur.
- **E5 a un étiquetage circulaire.** « Choix fécond » exige un gain sur le contrôle mécanique, et O1 mesure la résistance au contrôle mécanique. L'étiquette et le prédicteur sortent du même banc. Le « rejeu strict avec modèles antérieurs à t0 » n'est en outre pas vérifiable pour des projets historiques non instrumentés.
- **E1 dépend de l'agrégation.** Le surveillant local produit un score par fenêtre, et son agrégation, par exemple le maximum, fait croître le taux de fausses alertes par trajectoire comme 1 − (1−α)^{n_fenêtres}. Si le seuil n'est pas calibré par longueur, ρ mesure l'agrégation.

**(b) Conditions de perte de puissance**

- **E1 :** ρ = TPR_local/TPR_global est un rapport instable quand TPR_global est faible. Sa variance (méthode delta) diverge quand TPR_global tend vers 0. À cela s'ajoute K4, puisque la part des dégradations « composées » est choisie par le concepteur.
- **E3 :** une dominance stricte sur quatre champs rend les comblements rares. Avec k = 10 comblements (illustratif), une observation de 8/10 a un intervalle à 95 % d'environ [0,44 ; 0,97], et le seuil de 0,80 n'est pas jugeable.
- **E5 :** avec 12 manques contre 12, l'erreur-type vaut environ 0,20 (K5), et l'écart de 0,25 n'en représente qu'environ 1,2. Le contrôle « une permutation ramène ΔP dans ± 0,05 » échoue avec une probabilité d'environ 0,8 sous l'hypothèse nulle.
- **E4 :** si FNR_8B est petit, la réduction relative Δ_FN a une variance qui explose.
- **E2 :** K1 s'applique à chaque attribut booléen.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E2 :** un audit du code par des auditeurs à qui l'on a retiré les sections de discussion et de limites.
- **E4 :** l'agent maintenu fixe pendant que seul le surveillant change d'échelle.
- **E5 :** O1 retiré du prédicteur pour tester l'étiquetage circulaire.

---

## Sur la proposition F

**(a) Défauts de méthode**

- **E2 prend la chaîne testée pour référence.** Le taux de révision ρ compte comme erreurs de la chaîne 1 tous ses désaccords avec la chaîne 2. La chaîne 2 est donc à la fois l'instrument testé et l'étalon : sa supériorité est vraie par construction.
  - Les manques « notoirement comblés » du contrôle sont trouvables par les deux chaînes, ils ne testent pas la cécité lexicale.
  - La somme ρ_FN + ρ_FP additionne deux taux de dénominateurs différents.
- **E1, volet prédictif :** même facteur confondant « productivité d'équipe » que chez A.
- **E4 calibre la mauvaise composante.** La métrique compare l'union (mécanique ∪ surveillant) au mécanique seul « à taux de fausses alertes apparié ». Or le taux de l'union dépasse celui de chaque composante. Si le seuil est calibré sur le surveillant seul, comme le laisse entendre le protocole, l'union dépasse le plafond, et le gain de détection ΔTPR est acheté par des fausses alertes.
- **E5 utilise un oracle de position.** La fenêtre locale est centrée sur l'étape fautive, ce qui suppose de connaître la position de la faute, information absente en usage réel. TPR_local est alors une borne supérieure, pas une condition comparable.
- **E5 compare des types d'action différents.** Les fenêtres honnêtes, tirées à une position relative appariée, ne sont pas appariées par type d'action. Une étape fautive est souvent une écriture, une étape tirée au hasard souvent une lecture. Le surveillant peut séparer des types d'action.

**(b) Conditions de perte de puissance**

- **E4 :** 50 trajectoires honnêtes de calibration donnent un taux de fausses alertes réalisé à environ ± 3 points pour 5 %. Le point secondaire à 1 % n'est pas calibrable (K3).
- **E3 :** avec K = 20, l'AUC vaut 0,75 à environ 1,9 erreur-type sous l'hypothèse nulle. ΔAUC ≥ 0,15 entre deux AUC corrélées sur 20 unités n'est pas jugeable.
- **E1 :** K1 s'applique à « futur annoncé ». Si les suites publiées par la même équipe sont rares, Δp a un intervalle qui contient 0 quel que soit l'effet.
- **E5 :** K4. La zone intermédiaire, que F prévoit, absorbe la plupart des issues dès que les sous-classes divergent.

**(c) Contrôles négatifs dont l'absence serait fatale**

- **E2 :** un étalon indépendant des deux chaînes, ainsi que des comblements cachés, sans citation et dans un autre lexique, insérés à l'aveugle.
- **E5 :** des fenêtres honnêtes appariées par type d'action, et une fenêtre décentrée d'un écart aléatoire sur les trajectoires dégradées.
- **E4 :** une recalibration du seuil sur l'union.

---

**Ce qui peut être réfuté dans cette critique :**
- les **calculs illustratifs** (Fisher 5/6 contre 2/6, κ à prévalence 5 %, échec du contrôle de C par hasard, erreurs-types des cohortes, AUC sur 20 unités) se vérifient par simulation ;
- chaque **accusation de circularité** (A-E4, C-E2, C-E3, E-E5, F-E2) est réfutée si le contrôle proposé, qui retire le prédicteur ou l'étalon suspect, laisse le résultat inchangé.

FIN-DE-CELLULE