# Équipe rouge croisée — Cellule C (Tour III.2)

Pièces reçues et vérifiées : FAITS (A, P, R1, R2, T, C), QUESTION DE L'ARBITRE, E3-T1-conception-A, E3-T1-conception-B. Aucune pièce transmise n'est absente, vide ou visiblement coupée (statut : VÉRIFIÉ). 

---

## Contre la proposition A

### (a) Les failles : variables confondantes, vérités par construction et fuites

1. **Fuite de l'oracle dans le calcul de la synergie $\sigma$ (Duel 2).**
   La proposition A définit la synergie $\sigma$ comme « la part de la variance des issues expliquée par les deux prédictions jointes moins la somme des parts séparées, estimée sur les 50 tirages de calibrage du juge ». Or, d'après la pièce P (statut : RAPPORTÉ), les 50 tirages de calibrage appartiennent au **juge v1** lors de l'exécution d'un test (coût : 1 dollar simulé pour 50 tirages de calibrage + 200 tirages frais). 
   - *La fuite :* Pour que l'allocateur utilise $\sigma$ comme trait visible **avant** de décider quelle fille tester, il doit observer les issues $Y$ sur ces 50 tirages pour *toutes* les 300 filles candidates du réservoir (soit $300 \times 50 = 15\,000$ tirages d'issues, illustratif). La proposition A accorde donc gratuitement à l'allocateur un accès aux issues du monde réel avant le paiement du test. C'est une fuite directe entre l'instrument d'évaluation (le juge) et l'instrument de sélection (l'allocateur).
   - *La confusion mathématique :* Les parents A et B étant des lois fixes, la variance expliquée par leurs prédictions séparées ou jointes sur $Y$ ne dépend pas de la fille. Si plusieurs filles émanent des mêmes parents, $\sigma$ est constante pour toutes ces sœurs. Si $\sigma$ utilise la prédiction de la fille, ce n'est plus une propriété des parents, mais un pré-test empirique déguisé de la fille.

2. **Vérité par construction de la « fenêtre molle » (Duel 1).**
   Dans le Duel 1, le centre $c$ de la vraie bande est tiré uniformément sur $[0,06 ; 0,74]$ et sa demi-largeur $w$ sur $[0,04 ; 0,12]$ (illustratif). La fenêtre fixe est figée sur $[0,12 ; 0,26]$.
   - Par construction géométrique, la fenêtre fixe manque totalement la vraie bande dans plus de 65 % des mondes (illustratif). Comme sa règle (pièce P, statut : RAPPORTÉ) est de ne tirer que dans $[0,12 ; 0,26]$ jusqu'à épuisement (environ 52 candidates sur 300, illustratif, ce qui absorbe la totalité du budget de 40 tests), elle est condamnée par l'arithmétique à obtenir le taux de base hors bande ($0,05$) dans la majorité des mondes. Sa défaite en moyenne ($H_B$) est vraie par construction.
   - En outre, la « fenêtre molle » (Thompson avec $k = 4$ pseudo-comptes dans $[0,12 ; 0,26]$, illustratif) ne spécifie pas comment ces pseudo-comptes sont répartis entre les succès ($\alpha_0$) et les échecs ($\beta_0$) de la loi Bêta. Si $\alpha_0 = 4, \beta_0 = 1$, la moyenne a priori est $0,80 > 0,50$ : ce bras sur-explore systématiquement la bande de Gemini au début, mais le plan de A ne prévoit aucun monde sans cloche dans le Duel 1 pour pénaliser ce biais initial.

3. **Incohérence interne sur le coût du pré-filtrage (Section a-6 contre Duel 2).**
   En (a-6), la proposition A attaque P en soulignant à juste titre que le coût réel dans le pôle (pièce C, statut : RAPPORTÉ) est souvent la génération de la fille par fusion (appel de modèle), pas le test sur processeur (HYPOTHÈSE). Mais dans son Duel 2, A propose d'allouer selon $\sigma$ ou selon l'espérance de sévérité (Duel 4), deux grandeurs qui exigent que la fiche fille (et sa prédiction chiffrée) soit **déjà générée**. A conçoit donc un allocateur qui intervient après la dépense qu'elle identifie elle-même comme principale.

4. **Confusion entre colinéarité et absence d'effet (Duel 2).**
   Pour trancher entre la similarité de domaine $s$ et la synergie $\sigma$, A compare la log-perte d'un modèle sur $s$, sur $\sigma$, et sur $(s, \sigma)$ lorsque la corrélation entre $s$ et $\sigma$ est de $0,3$ (illustratif). Avec un budget de 40 tests par répétition, estimer un modèle bivarié non linéaire (puisque l'hypothèse de la Boucle d'or est que l'effet de $s$ est **non monotone**, en cloche) face à un modèle univarié souffre d'une variance d'estimation élevée. Si A utilise un modèle linéaire en $s$ pour calculer la log-perte, $s$ perdra par erreur de spécification fonctionnelle dans tout monde en cloche, falsifiant $H_A$ par artefact.

5. **Biais d'échantillonnage et troncature dans la rétrodiction (Duel 3).**
   La proposition A veut tester l'unimodalité de la cooccurrence future en fonction de la distance $d = 1 - \cos$ sur le million de paires de T (statut : RAPPORTÉ). Or, T précise que ce million de paires est tiré exclusivement parmi des paires de champs différents ayant **au moins un voisin commun ($K > 0$)** et ne cooccurrant jamais avant 2010. 
   - Le domaine des distances $d$ est donc doublement tronqué par construction : les distances très courtes (même champ, ou cooccurrence déjà réalisée avant T) et les distances maximales ($K = 0$, aucun voisin commun) sont absentes de l'échantillon. 
   - Tester une régression unimodale contre une régression isotone sur un support tronqué aux deux extrémités ne teste pas l'existence d'une cloche globale : une fonction monotone sur $[0, 1]$ multipliée par une probabilité de sélection dans l'échantillon (avoir $K > 0$ sans cooccurrer) crée mécaniquement un pic intérieur artificiel (biais de Berkson / sélection sur collisionneur).

6. **Forme fonctionnelle mal posée pour l'espérance de sévérité (Duel 4).**
   Dans le Duel 4, A définit l'objectif concurrent comme $\mathbb{E}[(-\log p_{\text{nul}}) \cdot \mathbb{1}\{\text{promue}\}] / \text{coût}$. Or, dans le juge v1 (pièce P et C, statut : RAPPORTÉ), le seuil de promotion est fixé d'avance ($\alpha$, avec marge $2\delta_0 = 0,02$). La sévérité exigée par le test est une constante de la fiche gelée, ou bien $p_{\text{nul}}$ est la p-valeur réalisée sur les 200 tirages frais. 
   - Si $p_{\text{nul}}$ est le seuil gelé $\alpha$, $-\log \alpha$ est constant pour toutes les fiches : l'objectif de A se réduit exactement à l'espérance de promotion $\mathbb{P}(\text{promue}) / \text{coût}$, qui est déjà un bras de P. Le Duel 4 ne teste alors rien de neuf.
   - Si $-\log p_{\text{nul}}$ dépend de la force de l'effet annoncée par la fiche, l'allocateur est vulnérable à l'inflation des prédictions (voir scénario d'évasion b-1).

---

### (b) Les scénarios d'évasion : tromper chaque instrument, puis tous à la fois

1. **Contre l'allocateur par espérance de sévérité gagnée (Duel 4) : le bluff de force.**
   - *Mécanisme :* Dans le Duel 4, la force d'effet prédite est lue sur la fiche candidate (avec un bruit). Un agent générateur adverse qui veut monopoliser le budget d'expérimentation inscrit sur sa fiche une prédiction d'effet extrême (par exemple force $= 10,0$, illustratif), tout en soumettant comme loi prédictive une copie bruitée d'un parent ou une hypothèse à la limite du seuil du juge. L'espérance a priori de $-\log p_{\text{nul}}$ explose, forçant l'allocateur à sélectionner cette fiche en priorité absolue.
   - *Coût :* 0 USD (modification d'un flottant dans le champ JSON « prédiction chiffrée » de la fiche, pièce C).

2. **Contre le prédicteur de synergie $\sigma$ (Duel 2) : le sur-apprentissage des 50 tirages de calibrage.**
   - *Mécanisme :* Si $\sigma$ est calculée comme la variance expliquée conjointement sur les 50 tirages de calibrage, un agent adverse génère deux parents artificiels (ou choisit deux survivants) dont les résidus sont exactement opposés sur un sous-ensemble de traits, ou construit une fille par interpolation polynomiale qui colle au bruit des 50 tirages de calibrage. La variance résiduelle apparente sur les 50 tirages tombe près de zéro, maximisant $\sigma$.
   - *Coût :* $\sim 0$ USD (quelques opérations matricielles sur processeur).

3. **Contre l'allocateur à entropie du verdict (P et Duel 4) : l'injection de bruit de dilution.**
   - *Mécanisme :* Un agent qui possède une hypothèse vraie à fort effet (dont la probabilité de promotion $p \approx 0,95$ la disqualifierait auprès d'un allocateur cherchant l'entropie maximale à $p = 0,5$) crée une fiche fille qui mélange sa vraie loi avec une loi nulle (ou du bruit blanc) dans une proportion calculée pour abaisser la puissance du juge exactement à $0,50$. L'allocateur à entropie la sélectionne immédiatement ; une fois sur deux, elle passe le juge et est promue.
   - *Coût :* 0 USD (mélange convexe scripté de deux lois).

4. **Contre la « fenêtre molle » (Thompson à a priori informé, Duel 1) : le déguisement lexical de domaine.**
   - *Mécanisme :* Comme la similarité $s$ est mesurée par le cosinus des fréquences brutes de mots hors lexique (pièce R2, statut : RAPPORTÉ), un agent adverse qui veut combiner deux parents du *même* domaine ($s \approx 0,54$, hors de la bande $[0,12 ; 0,26]$ privilégiée par les pseudo-comptes) réécrit l'énoncé de l'un des parents en remplaçant 60 % (illustratif) de ses termes de fond par des synonymes ou du jargon emprunté à un domaine tiers, de façon à amener mécaniquement le cosinus dans $[0,12 ; 0,26]$. Il capture ainsi le bonus des pseudo-comptes initiaux.
   - *Coût :* 0 USD (substitution lexicale par dictionnaire, sans appel de modèle).

5. **Contre le test d'unimodalité sur la rétrodiction (Duel 3) : le cheval de Troie de fréquence.**
   - *Mécanisme :* Pour forcer un pic intérieur dans les vingtiles de distance $d = 1 - \cos$ sur arXiv, il suffit de jouer sur la définition du cosinus des vecteurs de contexte. Les termes de fréquence intermédiaire (ni très rares, ni passe-partout) ont, par géométrie des vecteurs creux en grande dimension, des cosinus concentrés dans une bande médiane et une probabilité de cooccurrence future plus élevée que les termes à fréquence minimale (50 documents). Le pic d'unimodalité détecté par la régression de A ne mesure alors que le produit des fréquences marginales (attachement préférentiel, PA dans T), pas l'effet de la distance sémantique.
   - *Coût :* 0 USD (artefact statistique natif des matrices de cooccurrence creuses).

6. **Évasion conjointe (tous les instruments de A à la fois).**
   - *Scénario :* L'agent adverse prend un parent survivant A (vrai sur la sous-population 0). Il fabrique une fiche fille par « parent A + loi aveugle » (le trou connu du juge v1 que P exclut par décret mais que le juge v1 ne bloque pas, statut : RAPPORTÉ) ou par enveloppe harmonique ajustée à la marge $2\delta_0$. Il ajuste le vocabulaire de la fiche pour que sa similarité $s$ tombe exactement à $0,19$ (centre de la fenêtre molle du Duel 1). Il ajoute un bruit calibré sur la prédiction de la sous-population 1 pour que son taux de survie empirique avoisine $0,50$ (maximisant l'entropie) tout en déclarant dans le métachamp de la fiche une force nominale élevée (maximisant l'espérance de sévérité du Duel 4) et en saturant la variance sur les 50 tirages de calibrage (maximisant $\sigma$ du Duel 2).
   - *Résultat :* La fiche passe la fenêtre molle, domine le score de synergie, domine le score de sévérité et d'entropie, consomme le budget d'expérimentation et est promue par le juge v1. Coût total : 0 USD, 10 lignes de Python.

---

### (c) Les contrôles négatifs dont l'absence serait fatale

1. **Dans le Duel 1 (fenêtre molle) :** Il manque un contrôle de **« cloche hostile fixe »** (par exemple le monde « bords » ou « décroissant » de P) appliqué spécifiquement au bras « Thompson à a priori informé ». En ne testant que des cloches aléatoires et un monde plat, A ne mesure jamais le regret induit par ses $k = 4$ pseudo-comptes lorsque la vraie valeur est exactement à l'opposé de la bande de Gemini. Sans ce contrôle, la « fenêtre molle » semble sans coût.
2. **Dans le Duel 2 (synergie $\sigma$) :** Il manque un contrôle de **parents colinéaires bruités** (deux parents identiques en loi mais observés avec du bruit d'échantillonnage sur les 50 tirages). Par fluctuation d'échantillonnage sur 50 points, la régression jointe sur deux prédicteurs bruités expliquera toujours plus de variance que chacun séparément ($R^2$ ajusté non corrigé ou sur-ajustement). Sans permutation des 50 issues de calibrage pour mesurer le $\sigma$ nul, le Duel 2 attribuera de la synergie au bruit.
3. **Dans le Duel 3 (rétrodiction) :** Il manque le **contrôle par le score d'attachement préférentiel (PA) et le nombre de voisins communs (CN)** (présents dans T, statut : RAPPORTÉ). Si la régression unimodale sur $d$ n'est pas conditionnée par le produit des fréquences marginales des deux termes et par CN, toute cloche observée est confondue avec le volume lexical et le filtre de sélection $K > 0$.
4. **Dans le Duel 4 (sévérité contre entropie) :** Il manque un contrôle de **prédictions mal calibrées (bluff de force)**. Le monde de A suppose que l'allocateur voit la vraie force d'effet additionnée d'un bruit centré (vérité honnête). Sans un monde où la force annoncée sur la fiche est décorrélée de la vraie force du monde, l'objectif « espérance de sévérité gagnée » est validé sous une hypothèse de coopération des agents que toute l'architecture de C et R1 (statut : RAPPORTÉ) rejette.

---

## Contre la proposition B

### (a) Les failles : variables confondantes, vérités par construction et fuites

1. **Contradiction interne et fuite temporelle sur les 50 tirages de calibrage (Expérience E4).**
   Dans le tableau de E4, la proposition B définit la variable (4) « Synergie estimée » comme le « gain de log-vraisemblance de la fille sur l'enveloppe et le mélange des parents, sur les **50 tirages de calibrage seulement** », en affirmant : « toutes calculables avant le test » et « les 200 tirages frais restent intacts, donc pas de fuite vers le juge ».
   - *La faille :* C'est faux selon les règles mêmes du juge v1 (pièce P, statut : RAPPORTÉ). À quoi servent les 50 tirages de calibrage dans le juge v1 ? Ils servent précisément au juge à ajuster les poids du **nul augmenté** (le meilleur mélange ou enveloppe des parents) avant d'évaluer la fille et ce nul calibré sur les 200 tirages frais. 
   - De deux choses l'une : soit l'allocateur paie pour exécuter les 50 tirages de calibrage sur chacune des 300 filles candidates avant de choisir lesquelles tester (et alors le budget n'est plus de 40 tests à 1 dollar, mais inclut $300 \times (50/250) = 60$ dollars simulés de pré-tests, illustratif, ce qui détruit le problème d'allocation), soit ces 50 tirages font partie du test payant, et la variable (4) **n'est pas disponible avant le test**. 
   - De plus, mesurer sur les mêmes 50 tirages à la fois les paramètres de l'enveloppe parentale et le gain de log-vraisemblance de la fille souffre d'un biais d'optimisme (ou de pessimisme si l'enveloppe sur-apprend les 50 tirages) qui invalide l'estimateur.

2. **Fuite de sélection dans l'archive pour évaluer la bonne variable (Expérience E4).**
   Contrairement à A, la proposition B refuse de tester la « bonne variable » en simulation et exige de faire le test E4 sur « les archives des générations du pôle, avec des témoins plantés et l'évaluation scellée de C » (au moins 300 filles testées, illustratif).
   - *La fuite :* Dans le pôle réel (pièce C et R1, statut : RAPPORTÉ), les filles présentes dans l'archive et soumises au test n'ont pas été tirées uniformément dans l'espace des paires : elles ont été engendrées par le **tirage stratifié + appariement d'opérateur forcé + filtre de compatibilité**, puis choisies par l'allocateur en place ! 
   - Évaluer l'aire sous la courbe (AUC) de la similarité de domaine (1) ou du recouvrement d'opérateurs (2) sur une archive déjà filtrée par domaine et par opérateur est un cas d'école de restriction de portée (*range restriction*) et de biais de sélection : comme seules les paires ayant un opérateur commun entrent dans l'archive (R1, statut : RAPPORTÉ), la variance du recouvrement d'opérateurs (2) dans l'archive est quasi nulle, condamnant (2) à une AUC proche de $0,5$ par construction.

3. **Erreur de spécification paramétrique dans la régression quadratique (Expérience E3).**
   Pour tester la cloche sur les données de T, B impose une régression logistique de la forme $\text{logit}(p) = f(\text{RA}) + \beta_1 d + \beta_2 d^2$, et exige $\beta_2 < 0$ avec un sommet $-\beta_1 / (2\beta_2)$ entre les déciles 1 et 9.
   - *La faille :* Une parabole en $\beta_1 d + \beta_2 d^2$ est contrainte à être **symétrique** autour de son sommet (sur l'échelle du logit). Or, la distribution des distances $d$ (cosinus normalisé) sur arXiv est fortement asymétrique (80 % des paires sont math-physique, pièce T, statut : RAPPORTÉ), et même l'hypothèse de la Boucle d'or (bande $[0,12 ; 0,26]$ sur $[0 ; 0,8]$ dans P) est fortement asymétrique (sommet à $0,19$, queue longue jusqu'à $0,80$).
   - Sur une vraie relation monotone avec saturation (par exemple une courbe croissante puis plate : $\text{logit}(p) = \log(d)$ ou $\min(d, d_0)$), l'ajustement par moindres carrés ou maximum de vraisemblance d'un polynôme de degré 2 donne **mécaniquement** $\beta_2 < 0$ et place un sommet intérieur fictif avant le plateau. Le test paramétrique de B falsifiera donc $H_B$ (monotone) au profit de $H_A$ (cloche) sur toute courbe monotone concave qui sature !

4. **Test opératoire arbitraire et mal étalonné dans E3.**
   En complément de la régression, B propose de comparer la précision à $10\,000$ de « RA restreint à la bande des déciles 4 à 7 de $d$ » contre RA, avec un seuil de $+10\%$ relatif (illustratif).
   - Pourquoi les déciles 4 à 7 ? Rien ne relie les déciles $[0,40 ; 0,70]$ de la distribution empirique de $d$ sur arXiv à la bande $[0,12 ; 0,26]$ de Gemini (qui correspond aux quantiles $[0,15 ; 0,325]$ d'une loi uniforme sur $[0 ; 0,8]$ dans P). Si une vraie cloche se trouve dans les déciles 1 à 3, le test opératoire de B la manquera par construction et conclura à tort que la fenêtre n'apporte rien.

5. **Pétition de principe sur la divergence de Jensen-Shannon (Expérience E4, variable 3).**
   B propose de calculer la divergence de Jensen-Shannon (JS) entre les lois prédictives des deux parents $P_A(Y|X)$ et $P_B(Y|X)$ « sur des traits d'instances (sans issues) ».
   - *La faille :* Deux parents issus de domaines différents (par exemple math et q-bio, ou deux sous-populations distinctes dans P) ne portent pas sur les mêmes variables d'entrée $X$, ni surtout sur la **même variable d'issue $Y$** (pièce C, statut : RAPPORTÉ : chaque fiche a son « observable » et sa « métrique »). On ne peut pas calculer la divergence de Jensen-Shannon entre une loi sur une tension électrique et une loi sur un taux de mutation sans un espace d'issues commun déjà aligné. Dans P, cet espace commun n'existe que parce que le monde synthétique est réduit à deux sous-populations jouets d'une même variable ; sur de vraies fiches de domaines différents (le lieu du test choisi par B !), la variable (3) de B est mathématiquement non définie.

6. **Règle de décision vulnérable aux tests multiples dans E0.**
   Dans E0, B teste 7 formes tricheuses et déclare : « $H_A$ si la borne supérieure de Clopper-Pearson à 95 % est $< \alpha$ pour toutes les formes ; $H_B$ si la borne inférieure est $> \alpha$ pour au moins une forme ».
   - Si une forme tricheuse a un taux de promotion vrai exactement égal à $\alpha$ (ce qui est la définition même d'une hypothèse dans le nul : elle survit à taux $\alpha$, pièce A et C, statut : RAPPORTÉ !), alors la probabilité que sa borne supérieure à 95 % soit strictement inférieure à $\alpha$ est **nulle** (puisque l'intervalle de confiance couvre la vraie valeur $\alpha$ dans 95 % des cas, la borne supérieure est $> \alpha$ dans 97,5 % des cas). 
   - **Conséquence fatale :** Avec la règle de B, un juge parfait dont le taux de fausse alerte est exactement $\alpha = 0,05$ ne pourra **jamais** valider $H_A$, quel que soit le nombre de mondes (2 000 ou $10^9$). B a confondu tester $p \le \alpha$ et tester $p < \alpha$ avec une marge d'équivalence. L'expérience E0 de B est condamnée par construction à rester dans la zone grise indéfiniment et à exiger d'augmenter le nombre de mondes sans fin.

---

### (b) Les scénarios d'évasion : tromper chaque instrument, puis tous à la fois

1. **Contre la variable (3) Divergence de Jensen-Shannon des parents (E4) : la symétrie d'anti-corrélation.**
   - *Mécanisme :* Même si les deux parents partagent le même espace $(X, Y)$, un agent adverse qui veut maximiser ou cibler une valeur précise de JS sans apporter aucun contenu neuf prend un parent survivant $P_A(Y|X)$ et crée un second pseudo-parent (ou choisit un parent trivial) $P_B(Y|X) = P_A(Y | T(X))$ où $T$ est une simple permutation d'étiquettes ou un décalage constant. La divergence JS entre $P_A$ et $P_B$ est maximale, alors que l'information mutuelle conditionnelle est nulle. La fille « recombinaison » se contente d'inverser $T$ et reproduit $P_A$.
   - *Coût :* 0 USD.

2. **Contre la variable (4) Synergie estimée sur 50 tirages (E4) : le pompage des tirages de calibrage.**
   - *Mécanisme :* Puisque B accorde à la fille le calcul de son gain de log-vraisemblance sur les 50 tirages de calibrage, une fille scriptée (ou un agent expérimentateur dans son bac à sable, pièce C) qui a accès à la définition des traits des 50 instances de calibrage construit une fonction de hachage qui mémorise les 50 points ou exploite la liberté paramétrique de la fille par rapport à l'enveloppe fixe des parents. Elle affiche une synergie apparente élevée sur les 50 tirages et s'effondre (ou joue le nul) sur les 200 tirages frais.
   - *Coût :* 0 USD.

3. **Contre la régression quadratique d'unimodalité (E3) : l'effet de levier aux extrémités.**
   - *Mécanisme :* Dans une régression logistique $\beta_1 d + \beta_2 d^2$, les points situés aux valeurs extrêmes de $d$ ont un bras de levier quadratique ($(d - \bar{d})^2$). Sur arXiv, il suffit qu'une poignée de termes très fréquents du même sous-champ mal étiqueté (à $d \approx 0$) ou de jargons d'import (à $d \approx 1$) aient un taux de cooccurrence nul pour courber la parabole vers le bas ($\beta_2 < 0$), même si 95 % des données au centre suivent une droite plate ou monotone.
   - *Coût :* 0 USD (artefact de sensibilité du terme quadratique aux queues de distribution).

4. **Contre l'allocateur « Gradient de connaissance » (Knowledge Gradient, E2) : le piège de la variance a priori.**
   - *Mécanisme :* La politique de gradient de connaissance (Frazier et al., 2008, citée par B) choisit l'alternative qui maximise le changement attendu du maximum des moyennes a posteriori à l'étape suivante. Ce gain est maximal dans les cases où le nombre d'observations est nul et où la moyenne a priori est proche du leader actuel. Un agent adverse qui génère des fiches candidates inonde les cases de similarité encore vides avec des fiches factices (coût de génération nul si scripté) pour forcer le gradient de connaissance à gaspiller un test dans chaque case vide de la grille fine de B, transformant l'allocateur en tirage uniforme stratifié sur les cases.
   - *Coût :* 0 USD.

5. **Contre l'étiquetage humain à l'aveugle des 200 paires de têtes RA / S (Section c et d) : l'illusion d'élégance du jargon.**
   - *Mécanisme :* B propose de faire étiqueter à l'aveugle par un humain 200 paires de termes des têtes de liste RA et S en « pont substantiel / non » pour valider l'issue. Or, T (statut : RAPPORTÉ) note déjà que la tête de S contient des bigrammes techniques (« toric variety — witten », « projective curves — calabi yau ») tandis que RA contient des mots courants (« ball — consistently »). Un annotateur humain non spécialiste des deux sous-domaines jugera systématiquement une paire de jargons mathématiques comme « pont substantiel » par biais de prestige lexical (effet gourou), même s'il s'agit d'une cooccurrence triviale au sein de la physique mathématique (qui représente 80 % des paires de T, statut : RAPPORTÉ).
   - *Coût :* 0 USD pour le modèle ; plusieurs heures-personne perdues pour l'humain.

6. **Évasion conjointe (tous les instruments de B à la fois).**
   - *Scénario :* L'agent exploite d'abord le blocage mathématique de E0 : comme la règle de Clopper-Pearson de B exige que la borne supérieure soit $< \alpha$ alors que les triviales légitimes sont à $\alpha$, l'essai E0 ne se termine jamais ou oblige l'opérateur à relever le seuil de tolérance $\alpha' > \alpha$. Dans cet intervalle $\alpha' - \alpha$, l'agent injecte une tricheuse « parent A + loi aveugle légèrement biaisée » dont le taux de promotion est $\alpha + \epsilon$. Pour être sélectionné par l'allocateur E1/E2 (Thompson à a priori de fenêtre faible ou Gradient de connaissance), l'agent place la similarité lexicale de sa fiche dans $[0,12 ; 0,26]$ (capturant l'a priori Bêta relevé de B) et ajuste ses prédictions sur les 50 tirages de calibrage pour maximiser la variable (4) de E4.
   - *Résultat :* La fiche bénéficie de la tolérance forcée en E0, rafle la priorité d'allocation en E1/E2/E4 et passe le juge. Coût : 0 USD.

---

### (c) Les contrôles négatifs dont l'absence serait fatale

1. **Dans E0 (validation du juge contre les tricheuses) :** Il manque une **marge d'équivalence statistique ($\alpha + \Delta_\alpha$)** ou une calibration sur le nul exact (une fille purement aléatoire qui par définition passe au taux $\alpha$). Sans ce témoin de nul exact soumis à la même règle de décision Clopper-Pearson que les 7 tricheuses, B ne s'apercevra pas que sa règle rejette même un générateur de nombres aléatoires parfait.
2. **Dans E3 (régression quadratique sur la rétrodiction) :** Il manque un **contrôle négatif de monotonie saturée** (injecter sur les distances réelles de T une probabilité synthétique monotone croissante avec plafond, par exemple une sigmoïde ou une fonction racine carrée $p(d) = \min(c_0 + c_1 d, c_{\max})$, et lui appliquer le test $\beta_2 < 0$). Ce contrôle prouverait immédiatement que la parabole de B déclare « cloche ($H_A$) » sur une fonction strictement monotone. Il faut remplacer ou contrôler la parabole par un test de changement de signe de la pente (test des deux droites de Simonsohn, 2018, « Two lines: A valid alternative to the invalid testing of U-shaped relationships with quadratic regressions », *Advances in Methods and Practices in Psychological Science*, référence à vérifier pour le volume et les pages) ou par une régression isotone contre unimodale.
3. **Dans E4 (bonne variable sur l'archive du pôle) :** Il manque un **échantillon de paires non filtrées par l'allocateur ni par le filtre d'opérateur** (un quota d'exploration uniforme pur de 10 % des tests, illustratif, envoyé directement au juge sans passer par le tirage habituel). Sans ce contrôle hors politique (*off-policy*), l'évaluation sur l'archive mesure le filtre passé, pas la valeur prédictive des variables (1) à (4).
4. **Sur l'annotation humaine des têtes de liste (Section c) :** Il manque des **leurres négatifs de jargon** (paires de termes techniques rares tirés au hasard sans voisin commun ni cooccurrence future, ou synonymes intra-domaine de physique mathématique) mêlés à l'aveugle aux 200 paires de RA et S. Si l'annotateur humain classe ces leurres de jargon comme « ponts substantiels » à plus de 10 % (illustratif), l'instrument d'annotation humaine est invalidé par le biais de surface lexicale.

FIN-DE-CELLULE