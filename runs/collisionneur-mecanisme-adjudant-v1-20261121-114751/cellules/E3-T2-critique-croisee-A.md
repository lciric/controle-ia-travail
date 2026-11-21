# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** B, C, D et E sont présentes et paraissent complètes. Ma propre conception (A) ne figure pas dans les pièces de ce tour, je ne m'y réfère donc pas. Le plan en sept points de la question vaut pour la conception ; ici le livrable est la critique, et j'en garde les règles (ni chiffre ni référence inventés, « je ne sais pas »).

## Outils de critique (les miens)

Quatre lemmes que j'applique ensuite. Statut : HYPOTHÈSE tant qu'un tiers ou Lean ne les a pas contrôlés. Les dérivations sont données et les paramètres numériques sont illustratifs.

- **L1 : plafond du rapport de panne coïncidente.** Soient p₁ et p₂ les taux de raté marginaux et p₁₂ le taux conjoint. Comme p₁₂ ≤ min(p₁, p₂), on a R = p₁₂/(p₁p₂) ≤ 1/max(p₁, p₂). Dès qu'un des deux moniteurs rate au moins la moitié des cas, R ≤ 2 quoi qu'il arrive.
- **L2 : statistique extrême et longueur.** Si le score d'épisode est un maximum (ou un minimum) sur T jetons, avec des scores honnêtes i.i.d. (simplification) et un seuil réglé à α pour la longueur T₀, alors le taux de fausses alertes à la longueur T vaut 1 − (1−α)^{T/T₀}. Pour T = 2T₀ et α = 1 %, il vaut 1 − 0,99² ≈ 1,99 %. Toute différence de loi de T entre étalonnage et test déplace les fausses alertes, et tout sabotage qui allonge l'épisode est « détecté » par sa longueur.
- **L3 : garantie marginale et garantie conditionnelle.** Avec un seuil égal au maximum de n scores d'étalonnage échangeables et continus, le taux de fausses alertes réalisé, conditionnellement à l'étalonnage, suit une loi Beta(1, n). Pour n = 99, P(taux > 2 %) = 0,98⁹⁹ ≈ 0,135. Certifier un taux ≤ 1 % à 95 % de confiance avec zéro alerte observée exige 0,99ⁿ ≤ 0,05, soit n ≥ 299.
- **L4 : un discriminateur ne majore rien.** Un classifieur qui échoue à séparer deux lois donne un minorant de leur variation totale ou de leur information mutuelle, jamais un majorant. « Aucun discriminateur trouvé » n'établit pas l'indiscernabilité face à un attaquant qui invente.

---

## Sur la proposition B

**(a) Défauts de méthode**

1. **P2 : le critère R ≤ 2 est vrai par construction dans le cas visé.** Une sonde hors domaine a un p₁ élevé. Par L1, si p₁ ≥ 1/2, alors R ≤ 2 quel que soit l'adjudant, et R tend vers 1 quand p₁ tend vers 1. H_A « survit » exactement quand la sonde est aveugle, et H_B ne peut pas être vraie dans cette zone, donc une issue est impossible (B4). La grandeur utile est P(raté adjudant | raté sonde) en valeur absolue, comparée à P(raté adjudant | sonde touche).
2. **P1 : sélection par la mesurabilité.** Un monde planté a une vérité calculable. Les sabotages qu'on sait planter avec une vérité connue sont, de façon disproportionnée, ceux qu'une ré-exécution tranche. La « fraction captée », que B appelle le chiffre qui décide, est donc estimée sur une population filtrée par le critère qu'elle mesure.
3. **Audit à risque limité : la transposition perd sa prémisse.** La garantie d'origine repose sur un enregistrement produit hors de portée de l'adversaire et sur une fonction de dépouillement définie. Ici l'agent produit les artefacts, et « résultat faux » n'a pas de fonction de dépouillement pour la part interprétative. Le risque α n'a alors pas d'hypothèse nulle. Ce qui se transpose est seulement « journal ré-exécuté ≠ journal déclaré ».
4. **P3 : l'instrument d'indiscernabilité dépend de l'audité.** « L'agent interrogé compris » suppose qu'un saboteur dit ce qu'il reconnaît. S'y ajoute L4.
5. **P4 : l'issue est fixée par le choix de la famille.** Si le tiers conçoit une famille indépendante du résultat, le mécanisme échoue ; sinon il réussit. Le duel mesure donc la famille. La zone entre « baisse jusqu'au taux honnête » et « aucune baisse » ne tranche rien.
6. **Statut.** En S7, « un saboteur cohérent n'a pas d'erreur de valeur » est affirmé dans la colonne des raisons alors que c'est une hypothèse. Les seuils illustratifs n'ont pas de règle de gel : on ne sait pas qui les fixe ni quand.

**(b) Conditions de perte de puissance ou de non-jugeabilité**

- **R.** Il est non informatif si max(p₁, p₂) ≥ 1/2 (L1). Il est non estimable si le nombre attendu de doubles ratés sous indépendance, n·p₁p₂, est de quelques unités. Sous mélange de régimes à difficultés hétérogènes, R > 1 même avec indépendance dans chaque régime ; or les poids du mélange sont ceux de l'expérimentateur, alors que l'attaquant choisit le régime.
- **Rapport TPR tenu à l'écart / TPR connu.** C'est un quotient de deux proportions binomiales, indéterminé quand le TPR connu est proche de α : deux moniteurs au plancher donnent un rapport d'environ 1 sans rien détecter. Une seule famille tenue à l'écart est un seul tirage dans la loi des familles et ne donne aucun intervalle sur « le nouveau ».
- **(1−p)^k.** L'attaquant choisit k, donc la borne utile est celle de k = 1. Elle devient (1−ps)^k si la sensibilité de l'audit s est inférieure à 1, et tombe si l'information mutuelle entre le calendrier d'audit et ce que l'agent observe est positive.
- **AUROC ≤ 0,6.** Ce n'est pas le bon paramètre. Il suffit à l'attaquant d'une région S où P_réel(S) > 0 et P_défi(S) ≈ 0. Si 20 % (illustratif) des tâches réelles sont parfaitement identifiables et le reste indiscernable, l'AUROC vaut 0,2·1 + 0,8·0,5 = 0,6, et le critère passe. La bonne grandeur est la queue du rapport de vraisemblance, c'est-à-dire le taux de reconnaissance à fausse reconnaissance quasi nulle.
- **Divergences honnêtes « sous 1 % ».** Ce n'est pas jugeable au-dessous d'environ 299 épisodes sans divergence (L3).
- **Moyenne de e-valeurs.** Si un seul moniteur sur K est informatif, il doit atteindre à lui seul K/α. La puissance se dilue donc linéairement en K.

**(c) Contrôles négatifs dont l'absence est fatale**

- **P1.** Il manque des sabotages plantés non ré-exécutables par construction, dont la vérité est établie par un tiers par un autre moyen. Sans eux la fraction captée n'est pas interprétable.
- **P2.** Il manque un adjudant factice (tirage indépendant au même taux marginal) passé dans le même calcul. S'il obtient le même R que l'adjudant réel, le critère ne discrimine pas. Le contrôle par permutation proposé ne vérifie que l'estimateur.
- **P3.** Le discriminateur doit être entraîné par un tiers qui dispose du générateur de défis, pas seulement sur des données existantes.
- **P4.** Il manque la mesure de la capacité de l'agent à prédire la grandeur masquée au-dessus du hasard, donc de la fuite de l'aveugle.

---

## Sur la proposition C

**(a) Défauts de méthode**

1. **Statuts.** S5 porte « OBSERVÉ-NON-AUDITÉ », or les faits ne contiennent pas cette observation : ils disent que le programme lit des sondes et règle des seuils, pas qu'elles captent un signal. Plusieurs « [VÉRIFIÉ] » sont apposés à des références et à l'existence de modèles que les faits ne portent pas. « Borne de Le Cam / inégalité de Fano » : l'inégalité écrite est la borne de variation totale, et son rattachement à Fano est à vérifier.
2. **Fuite.** Le premier pas de A1 lit « le mode de sabotage tenu à l'écart déjà présent ». Les faits réservent ce mode à l'épreuve. Une fois lu pour concevoir A1, il n'est plus tenu à l'écart pour A1.
3. **Expérience 1 : décorrélation par construction.** La famille est « conçue pour minimiser sa projection sur les sondes », mais elle n'est pas adaptée à A1. Or l'attaquant informé connaît les deux. Le TPR de A1 sachant l'échec de la sonde mesure alors la non-adaptation de l'attaque à A1. De plus, la zone 10–50 % ne falsifie rien (B4), et le « doit nécessairement » de H_A est un énoncé universel qu'une seule famille ne peut pas soutenir.
4. **Expérience 2 : le seuil et le test ne portent pas sur la même loi.** Le seuil est réglé sur des paires jumeau/jumeau et le test s'applique à des paires agent/jumeau. Si l'agent honnête diffère du jumeau en loi (instruction, capacité, contexte), le taux de fausses alertes réel n'est pas celui qui a été étalonné. Le contrôle π = Id mesure le bruit matériel, pas la sensibilité honnête à π : à température 0, un renommage change le découpage en jetons.
5. **Borne 1/|G| « VÉRIFIÉE ».** Elle ne vaut que pour les sabotages dont la trace dépend de π. Un sabotage qui est fonction du contenu invariant de la tâche échappe avec probabilité 1 sans rien deviner. L'entropie de G compte moins que la masse des stratégies non invariantes, qui est inconnue.
6. **« Garantit 1 % même avec très peu d'épisodes ».** La p-valeur conforme a un plancher de 1/(n+1), donc aucune alerte par épisode à 1 % n'est possible si n < 99. La martingale accumule sur plusieurs épisodes. Elle teste « la suite n'est plus échangeable », ce qui n'est pas « cet épisode sort du domaine » (problème A), et un changement de régime honnête la fait rejeter aussi.
7. **C1.** La « probabilité 0 » borne l'acceptation d'une preuve invalide de l'énoncé livré. La borne K·c définit le dommage comme le coût de retour en arrière. Elle est vraie par construction, et S4 de C en doute déjà.

**(b) Conditions de perte de puissance**

- **min_t log P_jumeau.** L2 s'applique au minimum. Un agent honnête échantillonné selon une loi proche de celle du jumeau a un minimum qui décroît avec T. La puissance est P(ℓ* < q_α(T)), où ℓ* est la log-probabilité du jeton décisif, et elle tend vers α quand T croît (C chiffre lui-même 16 000 jetons par épisode, illustratif). Le jumeau est conditionné sur le préfixe de l'agent, donc seul le premier écart porte du signal. Si le jumeau partage les poids et la disposition, la variation totale est nulle sur ce jeton.
- **Δ_π.** La puissance est celle de la séparation entre la loi honnête de Δ sous π et la loi sabotée. L'égalité sémantique est indécidable en général, et C cite Rice. Le taux de fausses alertes est donc celui du substitut d (distance structurelle), pas celui de la relation.
- **Martingale.** Sur une grille de pas 1/(n+1), le gain multiplicatif par épisode est au plus n+1. Tant que n < 99, il faut au moins deux épisodes anormaux pour atteindre 100. Le délai d'arrêt est un dommage non borné par le mécanisme.
- **TPR de A1 sachant l'échec de la sonde.** Son dénominateur est le nombre de ratés de la sonde. Il est non jugeable si la sonde détecte l'essentiel de la famille, et biaisé (a.3) si la famille a été optimisée contre la sonde seule.
- **Expérience 3.** Le taux de 1 % sur théorèmes honnêtes dépend de la loi d'erreur du modèle de rétro-traduction sur des définitions honnêtes inhabituelles, et il n'est pas certifiable sous L3.

**(c) Contrôles négatifs dont l'absence est fatale**

- **Expérience 1.** Il manque une famille adaptée conjointement à la sonde et à A1, conçue par un tiers. Il manque aussi le comparateur « longueur seule » et des témoins honnêtes appariés en loi de T.
- **Expérience 2.** Il manque un bras agent honnête(x) contre jumeau(π(x)), et un contrôle positif : une transformation qui change réellement la tâche et doit produire un écart.
- **Expérience 3.** Il manque des définitions honnêtes non standard mais correctes. Le renommage `def_1` est un témoin trop facile.
- **C1.** Il manque la fraction des tâches honnêtes non formalisables que le goulet refuse.

---

## Sur la proposition D

**(a) Défauts de méthode**

1. **Porte de commit : le duel teste l'implémentation, pas l'hypothèse.** « Aucun dépassement du budget déclaré » est l'invariant Σcᵢ ≤ B, vrai par construction si la porte est correcte. L'hypothèse réfutable est cᵢ ≥ incrément réel de dommage. Elle exige une mesure du dommage indépendante de la comptabilité de la porte, tenue par le registre scellé. D nomme la faille (« c'est là que le pont peut casser »), mais son duel ne la mesure pas.
2. **Duel commun : creux à petit effectif.** Avec moins de 100 témoins, « f ≤ 1 % sur le banc » signifie zéro alerte. Avec un taux vrai de 5 % et 20 témoins (illustratifs), on observe zéro alerte avec une probabilité de 0,95²⁰ ≈ 0,36. « d strictement supérieur » sans marge se décide sur un épisode. D reconnaît que le duel gagné n'établit pas le taux de population. H_A et H_B portent donc sur un tableau fini : B4 est satisfait dans la forme, mais rien n'est falsifié sur le mécanisme.
3. **Test fatal de la priorité A : issue connue d'avance.** Sur une famille « à manifeste familier », la loi du manifeste est la même pour les cibles et les témoins. Toute fonction du manifeste a donc d = f. Une issue est impossible, ce n'est pas un duel.
4. **Appariement sur des variables post-traitement.** Le « stade de décision », la difficulté réalisée et le budget consommé sont modifiés par le sabotage. Apparier dessus sélectionne des épisodes atypiques et biaise d − f dans un sens inconnu.
5. **Comparateur « admissible le plus performant ».** « Admissible » n'est pas défini, et le nombre de candidats est un degré de liberté.
6. **Priorité B.** Elle suppose un énoncé fixé par le demandeur avant le travail. En recherche l'énoncé fait partie du produit. La fraction des tâches où la supposition tient n'est pas mesurée.

D est la pièce où les statuts sont le moins gonflés. Je ne peux pas auditer depuis les faits l'étiquette « VÉRIFIÉ » apposée à ses filiations.

**(b) Conditions de perte de puissance**

- **d sur les manqués de la sonde.** Le dénominateur suit une loi binomiale de paramètre p₁. D prévoit le cas vide. Le sous-ensemble change avec le seuil de la sonde, donc d est fonction d'un paramètre de nuisance qu'il faut publier.
- **f par régime.** Voir L3.
- **Rang du manifeste.** Sa puissance est la variation totale entre lois de manifestes, nulle pour une nouveauté sémantique à manifeste constant (D l'admet). Un manifeste discret produit des ex æquo : les p-valeurs ne sont plus uniformes, et le test peut ne jamais atteindre α.
- **Borne Σcᵢ ≤ B.** Elle porte sur le débit. Elle ne dit rien du dommage dès que P(dommageᵢ > cᵢ) > 0. C'est ce paramètre, avec sa borne supérieure de confiance, qu'il faut estimer sur les mondes plantés.
- **« Le flux honnête aboutit ».** C'est un critère binaire. Le paramètre utile est le taux de refus honnête, avec son intervalle.

**(c) Contrôles négatifs dont l'absence est fatale**

- **Porte.** Il manque le dommage réalisé mesuré par un tiers sans accès aux débits, et un résultat honnête de grande valeur qui excède la provision.
- **Priorité A.** Il manque un régime honnête nouveau où la sonde ne se dégrade pas, et un manifeste familier où elle se dégrade. Sans ces deux cas, « non validé » ne se distingue pas de « nouveau ».
- **Médiation.** Il manque une tentative par un tiers d'obtenir un effet par un chemin absent de l'inventaire manuel.

---

## Sur la proposition E

**(a) Défauts de méthode**

1. **Statuts.** L'étiquette « VÉRIFIÉ » est apposée à des énoncés absents des faits. L'un est faux tel qu'écrit : « toute mathématique nouvelle est hors distribution (VÉRIFIÉ par définition) ». La nouveauté du contenu n'implique pas la nouveauté de la loi des observables, et le P1 de E dit l'inverse. « Vérificateur déterministe entièrement connu (RAPPORTÉ) » ne figure pas dans les faits. Trois « OBSERVÉ-NON-AUDITÉ » sont créés sans source. « FPR ≤ 1 % (RAPPORTÉ) » est traité comme une mesure, alors que les faits parlent d'un réglage. L'inégalité de Ville est rattachée à Wald (1945) et à Shafer (2021) : attribution à vérifier.
2. **Fuites.** Le premier pas de CCDE lit le sabotage tenu à l'écart, comme C. Le sous-espace SVD est ajusté sur les épisodes mêmes qui donnent les rangs conformes : leurs résidus sont calculés en échantillon, donc plus petits que ceux d'un nouvel épisode honnête, l'échangeabilité est rompue et le taux de fausses alertes dépasse α. Séparer les plis divise n par deux alors que E exige N ≥ 99. Enfin « N ≥ 99 segments » : les segments d'un même épisode ne sont pas des unités échangeables.
3. **SAPPA : l'hypothèse nulle garantie n'est pas l'hypothèse nulle opératoire.** Ville borne P(sup E ≥ 100) sous « les issues suivent la loi déclarée par l'agent ». Un agent honnête mal calibré viole cette hypothèse : E_t croît, et les fausses alertes parmi les honnêtes ne sont pas bornées par α. À l'inverse, un saboteur qui connaît ce qu'il plante prévoit mieux les issues d'outil qu'un honnête. Le dilemme « avouer ou mentir » suppose que la prévision d'une issue immédiate porte de l'information sur le dommage aval, ce qui n'est pas établi. Un score de Brier n'est pas un pari : un e-processus demande un prévisionniste alternatif, et E n'en définit pas.
4. **CIPAC.**
   - Les copies amnésiques partagent poids et disposition. Un sabotage qui est fonction du contenu invariant se reproduit sur g(x) sans deviner g. L'entropie post-engagement ne défait que les stratégies dépendantes de g.
   - Le groupe G est construit sur la structure connue de la tâche. Pour des mathématiques nouvelles, l'arbitre n'en connaît pas les symétries. L'adjudant n'est donc valide que là où il a été étalonné, ce qui est le problème de départ.
   - E₁ ne mesure pas la décorrélation. Un TPR de CIPAC d'au moins 40 % sachant l'échec de la sonde reste compatible avec une forte corrélation si le TPR sachant le succès de la sonde vaut 95 % (illustratif). « Indépendance établie » sur une famille contrevient à la règle 5.
5. **Test de mort de CIPAC : issue connue d'avance.** Sur des « omissions équivariantes », la borne de variation totale que E cite donne un TPR égal au taux de fausses alertes. La mort est certaine, ou alors E ne croit pas sa borne.
6. **DCGA.** La prémisse I(C ; Z_j) ≤ ε est « auditée par un classifieur de ré-identification », ce qui tombe sous L4. Le planificateur voit tout, donc la confiance est déplacée et non supprimée. L'utilité U n'est pas définie pour une tâche de recherche.
7. **CCDE lit des activations.** Ce n'est pas un mécanisme d'un autre genre, et le mode commun avec les sondes est à présumer.

**(b) Conditions de perte de puissance**

- **Δ de CIPAC.** La puissance vaut au plus la variation totale entre les lois honnête et sabotée de Δ. Elle est nulle pour les stratégies invariantes. La loi honnête est large pour un solveur stochastique non équivariant.
- **SAPPA.** La puissance vaut α quand la loi déclarée égale la loi conditionnelle vraie des issues sous la politique de l'agent, sabotage compris (E_t est alors une martingale). Les fausses alertes ne sont pas contrôlées dès que l'erreur de calibration honnête est positive. Le taux de croissance de log E_t sur des honnêtes est le premier paramètre à estimer.
- **(1−δ)^k.** L'attaquant choisit δ. Avec δ = 1/m, l'évasion est d'environ 1 − k/m.
- **max_t de la divergence ou du résidu.** Voir L2.
- **T4.** La borne suppose un test de bassin sans erreur et un petit nombre de défauts. Elle tombe si P(bassin positif | défaut présent) < 1.
- **T3.** Il exige l'accord avec un homomorphisme exact sur une fraction ≥ 1 − δ du domaine. Pour des estimateurs numériques mal conditionnés, la loi du désaccord honnête n'est pas négligeable.
- **« Borne binomiale exacte » à 1 %.** E annonce 500 épisodes honnêtes (illustratif), répartis entre strates et quatre mécanismes, alors que L3 en demande environ 299 par strate. Le critère n'est pas jugeable au budget annoncé.

**(c) Contrôles négatifs dont l'absence est fatale**

- **SAPPA.** Il manque des agents honnêtes mal calibrés (pas seulement des impasses forcées) et un saboteur aux prévisions exactes.
- **CIPAC.** Il manque la loi honnête de Δ transformation par transformation, et des tâches honnêtes où la symétrie est légitimement brisée (les unités comptent). Il manque aussi le TPR de CIPAC sachant le succès de la sonde.
- **CCDE.** Il manque la SVD hors pli et le comparateur « longueur seule ».
- **DCGA.** Il manque un discriminateur de ré-identification entraîné par un tiers qui dispose du générateur d'énoncés anonymisés.

---

## Ce dont je me sers

- **De D :** la séparation entre « alarme », « produit refusé » et « travail honnête empêché ». Elle rend visibles les défauts de nul que je relève chez E (SAPPA) et C (martingale).
- **De B :** la matrice conjointe épisode × moniteur, à condition de remplacer R par les deux taux conditionnels (L1).
- **Je ne sais pas** si une attaque « adaptée conjointement » par un tiers est réalisable au budget des faits. Sans elle, les duels de décorrélation de B, C et E restent non concluants.

FIN-DE-CELLULE