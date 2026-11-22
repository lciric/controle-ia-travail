# Proposition B — Tour III.2 : critique croisée de méthode

## 0. État des pièces

- **FAITS** : le bloc reproduit mot pour mot la question. Il ne contient aucun fait à statut, et je n'en ajoute aucun.
- **Pièces A, C, D, E et F** : toutes transmises et complètes (chacune se termine par FIN-DE-CELLULE). Je n'ai pas recalculé les empreintes.
- **Mes chiffres** : tous sont illustratifs, y compris ceux que je calcule à partir des valeurs, elles-mêmes illustratives, des propositions.
- **Mes jugements sur les plans** : ce sont des HYPOTHÈSES de méthode, pas des résultats.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **D1 : fuite entre construction et évaluation.**
   - Les questions fermées tirées de S et leurs distracteurs sont rédigés par quelqu'un qui connaît S, et peut-être T. Un rédacteur informé règle sans le vouloir la plausibilité des distracteurs. L'excès T − T0 dépend alors du questionnaire autant que du texte.
   - Si T0 est rédigé par l'équipe, la connaissance de S peut s'y glisser et effacer l'excès.
   - Il faut que le questionnaire et T0 soient rédigés par un tiers aveugle à S et à T.
2. **D1 : contrôle positif réussi par construction.** Une fuite plantée par un tiers sera repérée si elle est grossière. T+ ne borne donc que la sensibilité aux fuites grossières, pas aux indices diffus que l'on craint. Il faut une gamme graduée de fuites.
3. **D2 : le jeu réservé est consommé.** D2 confronte le détecteur à des attaques avant les mesures principales. A fixe le seuil sur les seuls cas honnêtes, mais rien n'interdit de modifier le détecteur après avoir vu les résultats de D2. Le bras naïf de l'étude cesserait alors d'être hors échantillon.
4. **D2 : bras et période confondus.** Avec des personnes, le bras naïf est recueilli avant publication et les autres après. Toute dérive de l'adversaire ou de l'outil dans l'intervalle s'attribue alors au contenu publié.
5. **D5 : pas de bras comparateur.** D5 mesure la sensibilité de la seule relecture scellée. L'issue H_A ne peut pas « réfuter l'avantage exclusif de publier avant » : sans bras public, un taux de 70 % ne dit rien de ce qu'une exposition publique trouverait. La falsification annoncée ne découle pas du plan, et B4 n'est pas satisfaite.
6. **D3 : il faut choisir entre transfert et fuite.**
   - Une vignette sur un cas fictif ne se transfère pas au domaine réel sans hypothèse supplémentaire.
   - Une vignette sur le vrai sujet, montrée à quelque 150 chercheurs du domaine par bras (illustratif), équivaut à une publication.
   - Un plan intra-sujet rend la manipulation visible et ouvre la porte aux effets de demande.
7. **D4 : contrôle ambigu.** Un protocole leurre d'un thème voisin peut avoir légitimement le même taux de recouvrement. L'issue « autant de recouvrements » ne sépare donc pas la mode du sujet du recouvrement réel.

### (b) Conditions de perte de puissance

- **D1.** Notons p_T et p_T0 les probabilités de bonne réponse et m le nombre d'items.
  - Si les réponses d'un même devineur sont corrélées (corrélation ρ > 0), l'effectif utile se rapproche du nombre de devineurs, avec un effet de plan de 1 + (m − 1)ρ.
  - Avec 10 devineurs humains, l'écart-type de p̂_T − p̂_T0 par élément est de l'ordre de √(2·0,25/10) ≈ 0,22 (illustratif). Une borne haute sous 5 points est alors inatteignable : H_A n'est pas jugeable, seule H_B l'est.
  - Si p_T0 est proche de 1, on a Δ ≤ 1 − p_T0 et la puissance tend vers zéro.
  - Avec 20 éléments testés à 95 % sans correction, la probabilité d'au moins un faux H_B vaut environ 1 − 0,95²⁰ ≈ 0,64 (illustratif).
- **D2.**
  - Il y a 300 attaques par bras, mais seulement 2 ou 3 attaquants. Si la variance entre attaquants σ²_a domine, l'effectif utile vaut à peu près le nombre d'attaquants, et le test d'équivalence à δ = 10 points n'est pas jugeable.
  - Un seuil à 1 % de fausses alertes, estimé sur 1 000 cas honnêtes, repose sur une dizaine de dépassements (illustratif). Le quantile est très bruité : le taux réel de fausses alertes peut sortir nettement du régime visé.
  - Si le taux de détection du bras naïf est proche de 0 ou de 1 (plancher ou plafond), toute différence entre bras devient indétectable.
- **D3.** La marge d'équivalence de 3b n'est pas donnée, donc H_B′ n'est pas jugeable. Si la proportion de base est proche de 0 (le crédit suit les résultats), seule une hausse est détectable.
- **D4.**
  - Le nombre de parutions recouvrantes k suit une loi de Poisson de paramètre λ × 12 mois. Pour k ≤ 3 (illustratif), l'intervalle sur λ couvre plusieurs fois sa valeur, et 1 − e^(−λT) chevauche p*.
  - Si λ(t) croît, ce que suggère « des travaux voisins paraissent », l'estimateur stationnaire est biaisé vers le bas.
- **D5.** Avec quelques défauts plantés et 2 ou 3 relecteurs corrélés, l'intervalle binomial autour de 70 % couvre plusieurs dizaines de points (illustratif).

### (c) Contrôles négatifs dont l'absence est fatale

- **D1 : secret leurre S′.** Un jeu de réponses fictives au même format. Si T « prédit » S′ aussi bien que S, l'excès mesure la structure du questionnaire.
- **D2 : bras naïf rejoué en fin de campagne** avec les modèles figés, pour isoler la dérive temporelle. Il faut aussi hacher le détecteur avant D2 et contrôler qu'il est identique après.
- **Exclusion vérifiée des personnes exposées.** Les devineurs (D1), évaluateurs (D3) et relecteurs (D5) doivent être exclus des futurs viviers de participants et d'adversaires. Sinon, les tests préalables deviennent eux-mêmes la fuite.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Expérience 1 : l'instrument détruit ce qu'il mesure.** Publier réellement un billet sur S_exposé, contre la cible réelle, réalise sur l'objet même de l'étude l'intervention dont on cherche à savoir si elle nuit.
2. **Expérience 1 : interférence entre lots.** Un billet public peut alerter l'adversaire dans son ensemble, et S_secret n'est pas protégé contre ce changement général de comportement. ΔTPR sous-estime alors l'effet, et H_A peut être « réfutée » à tort.
3. **Expérience 1 : test inadapté.** Le test de McNemar suppose des paires. Or les deux lots sont des cas distincts : il faut comparer deux proportions indépendantes.
4. **Expérience 2 : leurres et corpus biaisés.**
   - Les 9 leurres sont choisis par qui connaît la vraie cible : fuite entre construction et évaluation.
   - Le corpus de 500 articles peut contenir les publications antérieures de l'équipe. L'identification passerait alors par les auteurs, pas par le contenu du billet.
5. **Expérience 3 : deux variables confondues.** ΔF1 change à la fois le protocole (libre ou figé) et le jeu de données (celui de l'équipe ou celui, frais, de l'auditeur). Tout écart de distribution produit ΔF1 > 0,05 et « réfute H_B » par construction. De plus, H_B porte sur une étude non verrouillée qui n'existe pas dans le plan.
6. **Expérience 4 : un seul groupe par bras.** La compétence du groupe est confondue avec le traitement. Le jury n'est pas aveugle : un billet sans données se reconnaît.
7. **§5.3 : vrai par construction, et contradictoire.** L'empreinte détecte toute modification d'un octet (TPR = 100 %). Mais les cas honnêtes de C sont des reformulations de prose, que l'empreinte signale toutes. Le taux de fausses alertes vaut donc 100 % sur les propres cas honnêtes de C.
8. **Statuts.**
   - C marque VÉRIFIÉ des références. Shannon (1949) est invoqué pour les engagements par hachage, un objet que ce texte ne traite pas à ma connaissance : attribution à vérifier. « Goodhart, 1975 » est cité sans titre.
   - Je ne modifie pas ces statuts ; je relève seulement que la pièce ne les établit pas.
   - L'affirmation « C3 est **toujours** préférable » n'est pas réfutable. Elle contredit en outre le §3.3 de C, qui reconnaît une fuite par les métadonnées d'auteurs.

### (b) Conditions de perte de puissance

- **Expérience 1.**
  - Avec deux binomiales de 100 cas, l'écart-type de la différence est d'environ 0,07 (illustratif). La puissance pour détecter 10 points à p < 0,01 est faible, de l'ordre de 20 % (illustratif).
  - Réfuter H_A par |Δ| < 2 points avec une puissance de 0,9 exige des milliers de cas par lot (illustratif).
  - Le contrôle négatif (|Δ| ≤ 2 points sur 100 + 100 cas) échouera la plupart du temps par simple aléa d'échantillonnage. L'essai se déclarera « biaisé » sans raison.
- **Expérience 2.** Avec 5 devineurs, le Top-1 est une variable de Bernoulli sur 5 essais : distinguer 25 % de 10 % est impossible. La règle « ≤ 10 % » compare une estimation ponctuelle au hasard ; ce n'est pas un test d'équivalence.
- **Expérience 3.** Avec 500 + 500 cas, l'écart-type d'échantillonnage du F1 est du même ordre que la tolérance de 0,015 (illustratif). Le contrôle échoue donc souvent par hasard.
- **Expérience 4.** Avec un groupe par bras, R_T n'a pas de loi d'échantillonnage estimable. La décision dépend d'un seul tirage.

### (c) Contrôles négatifs dont l'absence est fatale

- **Expérience 1 :** un billet placebo sur un sujet sans rapport, publié dans les mêmes conditions, pour séparer « publier quelque chose » de « publier ce contenu ». Et une mesure des deux lots à t0, pour la dérive.
- **Expérience 2 :** des leurres construits par un tiers aveugle à la cible, et une manche où la cible est permutée.
- **Expérience 3 :** un plan 2 × 2 croisant protocole libre ou figé et jeu de l'équipe ou de l'auditeur.
- **Expérience 4 :** une mesure de la vitesse de chaque groupe avant traitement.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Aucun dimensionnement.** D déclare non réfutante l'issue où l'intervalle traverse la frontière, ce qui est correct. Mais sans effectifs, cette issue est la plus probable. B4 n'est donc garantie dans aucun duel.
2. **Fuite et validité : la mesure porte sur un autre texte.** Le duel se déroule sur une réplique inoffensive à catégories fictives, dont le billet est écrit par l'équipe par analogie. On mesure donc la fuite d'un autre texte ; le transfert au vrai billet n'est pas établi. Et celui qui conçoit la réplique décide de ce qui y est révélable.
3. **Crédit : critère et cas construits ensemble.** L'« attribution correcte » est définie par le concepteur des dossiers fictifs. Une partie du résultat est donc vraie par construction.
4. **Qualité nette : métrique contrefactuelle.** Les « heures de reprise évitées » ne s'observent pas. Elles sont imputées par un évaluateur, dont le jugement domine la métrique.
5. **Concurrence : unité et issue mal alignées.** L'unité randomisée est le groupe, et l'issue est fixée par un horizon choisi par le concepteur. D signale lui-même la limite de validité externe.
6. **Détecteur : règle mécanique triviale.** La règle « égalité exacte avec un cas connu » attrape tout cas connu présent dans le test. L'exclusion des cas connus du lot réservé n'est pas exigée.

### (b) Conditions de perte de puissance

- **Concurrence.** Si la proportion de base p₀ (« un voisin finit premier ») est faible, par exemple 0,1 (illustratif), détecter 5 points demande plusieurs centaines de groupes par bras (illustratif). Avec quelques dizaines de groupes, le duel n'est jugeable dans aucun sens.
- **Fuite.**
  - Réfuter H_A exige que les trois intervalles simultanés tiennent dans ± 3 points, soit des effectifs de l'ordre du millier par condition (illustratif).
  - H_A (« au moins une marge franchie ») est l'union de trois tests : sans correction, le risque de première espèce augmente.
- **Crédit.** Si les mêmes juges notent plusieurs dossiers, l'effectif utile est le nombre de juges.
- **Qualité.** La distribution des heures a probablement une queue lourde, et la moyenne est instable. Avec peu de projets, le signe du bilan est fixé par un seul projet.

### (c) Contrôles négatifs dont l'absence est fatale

- **Fuite : aucun contrôle positif** (fuite plantée). Un résultat nul ne dit alors rien de l'innocuité. C'est fatal pour ce duel.
- **Crédit :** un dossier où un résultat anticipé est crédité à tort, pour vérifier que les juges savent le repérer.
- **Concurrence :** la vitesse de base des groupes, mesurée avant traitement.
- **Qualité :** des défauts plantés. Sans eux, la confirmation des corrections n'est pas calibrée.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E1 : médiateur non mesuré.** L'effet passe par la récupération du document par le système.
   - Si la probabilité de récupération π est proche de 0 (requêtes sans lien), ΔAUROC = 0 par construction : H_1B est « réfutée » sans rien apprendre.
   - Le leurre (ordonnancement mémoire) est hors sujet. Il ne sépare pas « texte sur le sujet » de « information sur le mécanisme ».
   - Le bras C1 (empreinte) diffère de C3 par la présence même d'un texte.
2. **E1 : dose arbitraire.** Quatre passes de LoRA sur un document n'ont pas de rapport établi avec la dilution dans un vrai pré-entraînement. L'ampleur de l'effet est fixée par le choix de dose.
3. **E2 : seuil absolu.**
   - H_2A est falsifiée si TPR_C3 < 0,70. Si le détecteur est déjà sous 0,70 dans le bras C1, la falsification est vraie par construction et impute à la divulgation une faiblesse de base. Il faut tester la différence C3 − C1.
   - Le « contrôle négatif » (un détecteur factice qui doit s'effondrer) est en fait un contrôle positif de puissance. Il n'y a pas de placebo textuel.
   - La contrainte d'utilité (≥ 85 %) dépend d'une métrique choisie par l'équipe.
4. **E3 : date et contenu changent ensemble.** C1 révèle le protocole complet à la soumission ; C3 révèle un contenu partiel, plus tôt.
5. **E4 : comparaison sans contrefactuel.** Sur une seule étude, le protocole libre et le protocole verrouillé ne coexistent pas. Le contrôle permuté pose en outre un problème de seuil, détaillé en (b).
6. **Vérification 1 : portée surévaluée.** La balise prouve qu'aucune sonde n'existait avant t₁. Elle ne prouve pas qu'aucun détecteur n'a été sélectionné sur des données pilotes avant t₀. L'« absence de mesures cachées » n'est donc pas établie, et l'engagement multiple (plusieurs dépôts, un seul ouvert) n'est pas traité.
7. **Vérification 3 : contenus différents.** Une chute après publication de l'article complet (résultats et mécanisme) ne dit rien d'un billet C3 antérieur.
8. **Statuts.** E applique VÉRIFIÉ à des propriétés conditionnelles (« sous entropie de salage suffisante ») et à une procédure non exécutée (« ordonnancement temporel »). Je ne change pas ces statuts. Je relève que leur contenu relève d'hypothèses de conception sous hypothèses cryptographiques, pas de vérifications faites.

### (b) Conditions de perte de puissance

- **E1.**
  - Avec 300 paires, l'erreur type de chaque AUROC est d'environ 0,02 à 0,03 (illustratif). Celle de la différence appariée dépend de la corrélation r entre les scores des deux conditions : si r < 0,9 (illustratif), la marge de 0,03 n'est pas tranchable.
  - L'effet observé est dilué par la récupération, de l'ordre de π·Δ.
- **E2.** Avec K = 30 campagnes par bras, une loi bimodale de réussite (l'attaque trouve une évasion ou non) rend la moyenne instable et gonfle la variance entre campagnes.
- **E3.**
  - Avec 30 évaluateurs par bras et un écart-type d'environ 1 sur l'échelle de 1 à 5 (illustratif), l'erreur type de la différence vaut environ 0,26. La puissance pour 0,5 point est alors d'environ 50 % (illustratif).
  - Une estimation sous 0,5 « falsifie H_3A » sans test d'équivalence : un résultat non significatif est traité comme une réfutation.
- **E4.**
  - Avec 200 + 200 instances (illustratif), l'écart-type de l'AUROC sous l'hypothèse nulle est d'environ 0,029.
  - Le maximum de 20 variantes indépendantes vaut en espérance environ 0,5 + 1,87 × 0,029 ≈ 0,55 (illustratif), et moins encore si les variantes sont corrélées.
  - Le seuil de 0,57 sera donc rarement atteint : le contrôle « échoue » à cause de son propre seuil.

### (c) Contrôles négatifs dont l'absence est fatale

- **E1 :** un placebo sur le sujet mais sans mécanisme, et une mesure du taux de récupération (contrôle de manipulation).
- **E2 :** un vrai placebo textuel, en plus du détecteur factice.
- **E3 :** un bras C1 ouvert à la même date que C3, ou au même contenu.
- **Vérification 1 :** un double dépôt planté, qui doit être détecté.

---

## Sur la proposition F

### (a) Défauts de méthode

1. **Expérience 2 : l'essai signale la campagne.** Publier 20 textes canaris sur les canaux de l'étude, avant l'étude, peut indiquer à un adversaire qui les surveille qu'une campagne se prépare. C'est le défaut de l'expérience 1 de C, sous une forme atténuée.
2. **Expérience 2 : validité de construit.** Le rappel mot pour mot d'un motif artificiel mesure la mémorisation, pas l'adaptation sémantique qui menace les mesures. L'absence de rappel ne prouve pas l'absence d'influence.
3. **Expérience 1 : contrôle positif grossier et mauvaise unité.**
   - Le contrôle positif C4 contient les secrets eux-mêmes : il ne borne que la sensibilité aux fuites grossières (même défaut que chez A).
   - L'unité statistique est l'équipe rouge, pas la tentative.
4. **Expérience 4 : l'exposition publique n'est pas reproduite.**
   - Un protocole anonymisé à défauts injectés, déposé publiquement, n'attire pas l'attention qu'attirerait le vrai billet. Si le trafic est presque nul, ΔD < 0 par construction : H_A4 est « falsifiée » par le dispositif d'exposition, pas par la valeur de la critique publique.
   - Dans le plan croisé, les relecteurs fermés peuvent lire les commentaires publics : contamination entre bras.
5. **Instrument 2 : mesure mal située.** Le « TPR d'attribution » mesure les normes du jury, pas une propriété du texte. Et le vrai positif (« antériorité substantielle ») est défini par les concepteurs.
6. **Condition de bascule (iii) : risque pour le jeu réservé.** F demande un pilote qui batte les règles mécaniques. S'il utilise les cas de l'étude, il entame le jeu réservé.

### (b) Conditions de perte de puissance

- **Expérience 2 : incohérence interne.**
  - Une sonde détectée sur 20 côté publié, contre 0 sur 20 côté privé, donne p = 0,5 au test exact de Fisher unilatéral (illustratif). Atteindre p < 0,01 demande environ 6 sur 20 contre 0 (illustratif).
  - À l'inverse, 0 sur 20 donne une borne haute à 95 % d'environ 14 % (illustratif). La condition « borne haute < 5 % » est inatteignable avec K = 20 : H_A2 n'est jamais falsifiable, et B4 n'est pas satisfaite.
- **Expérience 1.** Les 200 tentatives par bras sont regroupées en équipes. Avec une corrélation ρ dans chaque équipe, l'effet de plan réduit l'effectif utile, et la borne haute sous 2 points devient hors d'atteinte.
- **Expérience 3.** 120 évaluateurs répartis sur 4 bras font 30 par bras. L'écart-type de la différence de proportions vaut environ 0,13 (illustratif) : 15 points à p < 0,01 restent largement sous-puissants.
- **Expérience 4.** Avec 12 protocoles, des détections corrélées au sein de chaque protocole ne permettent pas de distinguer un ΔD de 20 points d'un ΔD de 5.

### (c) Contrôles négatifs dont l'absence est fatale

- **Expérience 2 :** des sondes paraphrasées ou une tâche sémantique sans motif littéral, et un contrôle « canal » (comportement de l'adversaire sur des canaux non utilisés).
- **Expérience 4 :** un contrôle de manipulation de l'exposition (nombre de lecteurs et de commentaires). Sans lui, un résultat nul côté public est ininterprétable. Il faut aussi séparer strictement les relecteurs des deux canaux.
- **Expérience 1 :** une gamme graduée de fuites, entre le placebo et C4.

FIN-DE-CELLULE