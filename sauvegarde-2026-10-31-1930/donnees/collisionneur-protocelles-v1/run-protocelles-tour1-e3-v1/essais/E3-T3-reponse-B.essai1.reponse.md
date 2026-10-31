# Proposition B — Tour III.3 : Réponse aux critiques

---

## Préambule

Les critiques croisées proviennent de C et D. La pièce A est absente ; aucun contenu n'est inventé pour elle. Je traite chaque critique adressée à B, une par une.

---

## (a) Réponses aux critiques de C sur B

### C-B.1 : Confusion entre prévalence d'équilibre et charge d'erreur (Prédiction 1)

**Acceptée.**

C a raison. Le plafond ln 2 du Théorème 2 (VÉRIFIÉ, p. 4) porte sur le seuil critique $U_c$ — un paramètre du modèle — et non sur un rapport de fractions fonctionnelles observées. Mon seuil « si le gain en fraction fonctionnelle dépasse $\exp(\ln 2) = 2$ » est une erreur : pour $\theta \geq 1$, le pool bien mélangé a $U_{\text{mix}} = 0$ (VÉRIFIÉ, p. 3, Éq. 2), donc toute survie dans les lots donne un rapport infini par construction. Le test proposé ne discrimine pas entre le plafond du papier et un effet trivial de compartimentation.

**Correction :** La Prédiction 1 est retirée dans sa forme actuelle. Un test du plafond $\ln 2$ exigerait de faire varier $U$ (le taux d'erreur par copie) de manière contrôlée, ce qui n'est pas faisable dans l'organisme d'idéation où $q$ n'a pas de correspondant univoque (comme je l'avais moi-même noté en (a) de ma proposition initiale).

---

### C-B.2 : Simulation du contrôle « bien mélangé » par permutation post-hoc

**Acceptée.**

C a raison que la permutation des étiquettes de lots *a posteriori* conserve la somme globale des fiches fonctionnelles et produit un rapport moyen de 1 par construction. Mon contrôle était mal conçu. Un vrai contrôle du mélange exigerait un brassage *pendant* l'exécution, entre les étapes de fusion, pour que les parasites puissent effectivement diluer les paires fonctionnelles dans tous les lots.

**Correction :** Le contrôle par permutation post-hoc est retiré. Un contrôle valide serait une course parallèle où les fiches sont redistribuées aléatoirement entre lots à chaque round *avant* les fusions (coût : une course supplémentaire).

---

### C-B.3 : Variables confondantes dans le test de la loi d'échelle (Prédiction 2)

**Acceptée.**

C identifie trois problèmes : (i) à $N_{\text{tot}} = 18$, faire $n = 12$ donne 0,75 lots — absurde ; (ii) varier $n$ confond la loi d'échelle intra-lot avec la dérive inter-lots ; (iii) le seuil « 50 % fonctionnelles » est faux, la fraction au seuil de viabilité étant $\approx 3,41/(2n)$ (VÉRIFIÉ, Appendice S1, p. 28), soit $\sim 14\%$ à $n = 12$.

**Correction :** La Prédiction 2 est retirée dans sa forme actuelle. Tester la loi d'échelle $R_{\min} \propto n$ exigerait un nombre de lots $M$ suffisant à chaque $n$, donc un $N_{\text{tot}}$ qui croît avec $n$, et un budget de fusions contrôlé indépendamment de la taille des lots. La course 2 ($M = 3$, $n = 3$) ne peut pas tester cette prédiction.

---

### C-B.4 : Fuite entre construction de $\theta'$ et évaluation de la viabilité (Prédiction 3)

**Acceptée partiellement, transformée en test.**

C a raison que mesurer $\theta'$ par le taux d'utilisation *sur les mêmes rounds* où l'on observe la survie du lot crée une corrélation inverse par construction : quand $F$ chute, les fiches non fonctionnelles (dont les inachevées) sont mécaniquement plus souvent tirées. L'estimateur est endogène.

**Ce qui survit :** La prédiction qualitative — garder un fragment rapide est plus coûteux que le jeter — reste une conséquence du papier (Fig. 6, p. 10). Mais le test quantitatif que j'avais proposé est biaisé.

**Correction :** Mesurer $\theta'$ *avant* de lancer l'évolution du lot, sur un échantillon de fusions pilote où le produit inachevé est présenté au bisociateur à côté d'une fiche complète, dans des lots distincts de ceux où la survie sera mesurée. Alternativement, fixer $\theta'$ exogènement en contrôlant le poids d'échantillonnage de la fiche inachevée dans le bisociateur.

---

### C-B.5 : Tautologie dans l'évaluation du bisociateur (Section (e))

**Acceptée.**

C a raison que le bisociateur est un opérateur génératif, pas un classifieur, et que réutiliser le même juge pour définir les entrées fertiles et évaluer les sorties fertiles crée une fuite. Ma formulation en termes de « taux de fausses alertes » était un calque inapproprié.

**Correction :** L'évaluation du bisociateur doit utiliser un juge *séparé* de celui qui sélectionne les fiches, sur des paires tirées de mondes à vérité plantée dont le statut est fixé avant l'expérience et non déterminé par le même juge.

---

### C-B (contrôles négatifs) 1 : Contrôle de survie par parent unique (clonage sans bisociation)

**Acceptée.**

C a raison que mon contrôle par concaténation est insuffisant : si un seul parent fertile suffit à engendrer une fiche fertile par simple reformulation, on est dans le régime d'auto-copie $c > 0$ du papier (Table 1, p. 6), où il n'y a pas de seuil à fécondité infinie. Il faut un contrôle où le générateur reformule un seul parent, sans partenaire.

**Correction ajoutée :** Un bras de contrôle « cis » où le bisociateur reçoit une seule fiche et la reformule, sans partenaire de fusion.

---

### C-B (contrôles négatifs) 2 : Contrôle de charge de contexte sur les fusions inachevées

**Acceptée.**

C a raison que les fiches inachevées, étant plus courtes, consomment moins de jetons dans la fenêtre de contexte, et que cet avantage mécanique est confondu avec l'avantage de modèle $\theta'$.

**Correction ajoutée :** Les fiches inachevées retirées doivent être remplacées par du rembourrage inerte de même longueur, ou le budget de jetons doit être égalisé.

---

### C-B (contrôles négatifs) 3 : Contrôle d'aveuglement du juge aux marqueurs de génération

**Acceptée.**

C a raison que des traces stylistiques cumulées par le bisociateur (longueur croissante, structure standardisée) peuvent faire croître la fraction « fonctionnelle » jugée au fil des rounds, même sans amélioration conceptuelle.

**Correction ajoutée :** Le juge évalue dans le désordre des fiches de rounds mélangés, normalisées en format, et un contrôle de fusions de fiches *toutes fausses* vérifie que la fraction fonctionnelle reste à zéro au fil des rounds.

---

## (b) Réponses aux critiques de D sur B

### D-B.1 : La prédiction globale utilise des paramètres que B vient de déclarer non définis

**Acceptée partiellement.**

D a raison que je déclare $q$ sans correspondant dans l'organisme puis calcule $q > 0,638$. La contradiction est réelle : j'avais voulu illustrer l'exigence du modèle à $n = 3$ pour montrer qu'elle est inaccessible, mais l'illustration repose sur un paramètre que j'avais moi-même déclaré non défini.

La lecture $n = 3$ (six fiches par lot, taille à la naissance $n = 3$ si le lot se divise en deux de taille 3) est une hypothèse de correspondance, pas un fait. D a raison que le protocole de division n'est pas décrit dans les faits.

**Ce qui survit :** La prédiction de non-allumage reste mon meilleur jugement, mais elle est qualitative (les hypothèses du papier sont massivement violées), pas une conséquence quantitative du modèle. Je reformule en conséquence en (c).

---

### D-B.2 : La première « prédiction » confond charge d'erreur et fraction fonctionnelle

**Acceptée.** (Même critique que C-B.1, que j'ai déjà acceptée.)

D ajoute un point juste : la permutation impose l'hypothèse de division aveugle au lieu de la tester. J'avais présenté la permutation comme un test de cette hypothèse ; c'est l'inverse. Retiré.

---

### D-B.3 : Le test du prix ne teste pas la linéarité et confond taille et budget

**Acceptée.** (Recoupe C-B.3, déjà acceptée ; D ajoute que la croissance non linéaire n'est pas discriminée par mes seuils, ce qui est correct.)

---

### D-B.4 : Le proxy de $\theta'$ mesure la politique de réutilisation, pas l'avantage du fragment

**Acceptée partiellement.**

D a raison que le taux de réutilisation est confondu avec longueur, ancienneté, exposition, sujet, tireur et juge.

D note aussi une « contradiction interne » : j'affirme qu'un fragment très fertile envahit, mais dans le modèle du papier les tronqués ne régénèrent jamais de réplicase. C'est exact : le mécanisme du papier fait que les tronqués sont copiés en tronqués (parasites), pas en réplicases. Un fragment d'idée réellement « fertile » — qui engendre des idées complètes fonctionnelles — serait, dans les termes du papier, non pas un parasite rapide mais une réplicase de courte longueur. Les deux cas ont des conséquences opposées. J'avais confondu « recopié vite » (toxique dans le papier) et « productif » (bénéfique).

**Correction :** La Prédiction 3 (section « fragments fertiles ») est corrigée : un fragment qui *produit des descendantes fonctionnelles* n'est pas un parasite au sens du papier ; un fragment qui est *recopié sans produire de fonctionnelles* l'est. La distinction opérationnelle est : « la descendance du fragment est-elle elle-même fonctionnelle ? » Si oui, ce n'est pas un parasite. Si non, c'est un parasite rapide, et le papier prédit la toxicité.

---

### D-B.5 : Le bain lent et le sort perdu sont fusionnés à tort

**Acceptée.**

D a raison que le coût exact $1/(1-\tau)$ ne concerne que le sort perdu (Identité (i), p. 56). Le bain lent (Appendice S9, p. 57–60) est un régime distinct, avec des conditions propres (pas de re-troncation, $\theta' < 2(1-\tau)$). Ma réponse « jeter si $\theta' > 2$, garder sinon » omet la re-troncation et la fertilité résiduelle.

**Correction de la réponse au directeur :** « T'es sûr ? » La réponse complète est un arbre à trois branches, qui dépend de ce que *devient* le produit inachevé :

1. **Perdu** (jeté, jamais archivé) : coût $1/(1-\tau)$ en fécondité, exact, négligeable pour $\tau < 5\%$. Politique robuste par défaut.
2. **Recopiable et plus lent que la réplicase** ($\theta' < 2(1-\tau)$ sans re-troncation, Appendice S9 pp. 57–60) : forme un bain inerte ; le coût est un décalage de charge $\ln(1-\tau)$, exact (Identité (ii), p. 56, pour $\theta' = \theta$). Garder est tolérable.
3. **Recopiable et plus rapide** ($\theta' > 2$) : toxique au-delà de $\sim 1,5$ produit par cycle de division (Fig. 6A, p. 10), avec un coût qui croît avec la taille du lot. Jeter est impératif.

Et : si les copies du fragment s'arrêtent elles-mêmes (re-troncation), le bain se vide vers les classes les plus courtes et le seuil $\tau_c$ décroît comme $1/n$ (Appendice S9, p. 59, Fig. S1C). La re-troncation dans l'organisme correspondrait à ce que le bisociateur, recevant un fragment, produise lui-même un fragment encore plus court — ce qui dépend du protocole.

---

### D-B.6 : Le même juge pour construire et évaluer

**Acceptée.** (Même critique que C-B.5, déjà acceptée.)

---

## (b) Expériences corrigées

Après les critiques acceptées, les Prédictions 1 et 2 sont retirées. Il reste :

### Expérience E-B1 (corrigée) : Sort des fusions inachevées

**H_A :** Conserver dans le vivier les produits de fusions inachevées dont les descendantes ne sont pas fonctionnelles (parasites rapides, $\theta' > 2$) augmente le risque d'extinction des lots.

**H_B :** Conserver ces produits ne change pas le risque d'extinction.

**Protocole :**
- Mesurer $\theta'$ *avant* l'expérience, sur un échantillon pilote de fusions avec le produit inachevé comme entrée, dans des lots distincts. Le proxy est le nombre de descendants du fragment par unité de temps, rapporté au même nombre pour une fiche complète.
- Deux courses parallèles, attribuées aléatoirement : (i) produits inachevés jetés ; (ii) produits inachevés conservés mais remplacés par du rembourrage inerte de même longueur dans (i) pour égaliser le budget de jetons.
- Critère de survie : lot contenant $\geq 2$ fiches fonctionnelles (jugées par un juge séparé, aveugle au traitement) après $K$ rounds.
- Le juge évalue les fiches dans le désordre, normalisées en format.

**Issue :** Une fraction de lots survivants significativement plus basse dans la condition (ii) falsifie H_B. Pas de différence significative falsifie H_A.

**Avertissement statistique (intégrant la critique C-B, conditions (b)) :** Avec $M \leq 3$ lots par bras, un test exact de Fisher au seuil $\alpha = 0,05$ est de puissance nulle (la plus petite p-value atteignable est 0,10, VÉRIFIÉ dans la critique de C). Le test exige $M \geq 6$ lots par bras pour que la p-value puisse descendre sous 0,05 dans le cas extrême ; $M \geq 10$ pour une puissance raisonnable. Si la course 2 a $M = 3$, cette prédiction est **non jugeable** sur ses données. Elle nécessite une course dédiée.

**Contrôles négatifs :**
- Bras « cis » : le bisociateur reformule un seul parent, sans partenaire.
- Bras « tout faux » : fusions de fiches toutes fausses, la fraction fonctionnelle doit rester à zéro.
- Rembourrage inerte de même longueur pour les fiches retirées.

### Expérience E-B2 (nouvelle) : Correspondance trans vs cis

**H_A :** La production de fiches fonctionnelles exige la fusion de deux parents (trans) ; la reformulation d'un seul parent (cis) ne suffit pas.

**H_B :** La reformulation d'un seul parent suffit ($c > 0$ dans le papier, pas de seuil à haute fécondité).

**Protocole :** Comparer la fraction de descendantes fonctionnelles issues de fusions à deux parents vs reformulation à un parent, sur les mêmes parents, juge séparé, mondes à vérité plantée.

**Issue :** Si la reformulation à un parent produit autant de descendantes fonctionnelles, le modèle trans du papier ne s'applique pas (H_B). Si le taux est significativement plus bas, le mécanisme trans est nécessaire (H_A), et le plafond $\ln 2$ est le bon.

---

## (c) Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi (dans le papier)

1. **Le plafond $\ln 2$** sur la charge tolérable, pour une division aveugle à l'identité moléculaire, à toute taille et fécondité (Théorème 2, p. 4 ; VÉRIFIÉ). Le mécanisme est la paire catalyseur–modèle comme unité reproductive (Fig. 2C, p. 3).
2. **Le prix** : la fécondité requise croît linéairement avec la taille de la protocelle, $R_{\min} \approx n / \psi^{-1}(U + \ln\theta)$ (Éq. 3, p. 8 ; prouvé pour $R > n$, Théorème 4, pp. 7–9).
3. **Le sort des copies inachevées** détermine lequel des trois coûts s'applique : perte en fécondité, décalage en charge, ou effondrement (Identités (i)–(iii), Appendice S8, pp. 55–56 ; Fig. 6, p. 10).
4. **Les ribozymes mesurées** sont à un facteur 10–250 en fécondité et 1,1–3,6 en charge du plafond (Table 2, p. 12 ; OBSERVÉ-NON-AUDITÉ pour les conversions).

### Ce qui n'est pas établi

1. **La correspondance papier–organisme n'est pas structurelle** : 5 hypothèses des théorèmes sont violées ou probablement violées dans l'organisme (copie en trans, un seul type de parasite, division binomiale, division aveugle, population infinie). Le papier ne peut pas prédire l'allumage de l'organisme.
2. **La correspondance papier–arène** est invalide : la dynamique adversariale viole la neutralité de la division.
3. **Les paramètres $q$, $\theta$, $R$ ne sont pas identifiés** dans l'organisme d'idéation, ce qui rend toute prédiction chiffrée non fondée.
4. **La taille de la course 2** ($M = 3$ bras, $n = 3$ fiches) rend la plupart des tests statistiques non jugeables au seuil conventionnel (critique C, acceptée).
5. **L'hypothèse (H2)** de la loi d'échelle reste ouverte pour $y > 95/32$ (prouvée pour $y \leq 23/8$ et $47/16 \leq y \leq 95/32$, Appendice S3, pp. 37–40).

### L'expérience à faire en premier

**E-B2 : trans vs cis.** C'est la première chose à mesurer car elle ne coûte rien (elle utilise les mêmes fiches et le même bisociateur que la course 2) et elle tranche la question la plus fondamentale : **le mécanisme du papier (reproduction de paires en trans) est-il le bon modèle pour l'organisme, ou la production d'idées fonctionnelles passe-t-elle par la reformulation d'un seul parent (cis) ?**

- Si cis suffit, le plafond $\ln 2$ ne s'applique pas et le papier n'est pas le bon cadre. Il n'y a pas de seuil d'erreur pour l'organisme au sens du papier.
- Si cis ne suffit pas, la compartimentation en lots et la fécondité deviennent les variables pertinentes, et les prédictions du papier (plafond, prix, sort des inachevées) ont un domaine d'application potentiel — sous réserve des violations identifiées.

Ce test est le garde-fou contre l'erreur d'appliquer un modèle trans à un système qui fonctionne en cis.

FIN-DE-CELLULE