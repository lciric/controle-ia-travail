# Proposition C — Tour III.3 : réponse aux critiques et synthèse

*Note d'intégrité liminaire (Règles 1, 2, 3, 4) : Aucune pièce transmise n'est absente ou coupée. Les textes des pièces servies ont le statut **RAPPORTÉ**, leurs chiffres d'exécution non rejoués ici ont le statut **OBSERVÉ-NON-AUDITÉ**, et toute analyse ou conception a le statut **HYPOTHÈSE**. Tout chiffre de dimensionnement introduit hors des faits est marqué **illustratif**.*

---

## (a) Traitement des critiques reçues sur la proposition C

### 1. Intégrité des statuts, attributions et formules théoriques
- **Attribution de `llama-3.1-8b` au modèle de la banque T0.5 (Critiques A, E)** : **Acceptée.** La pièce 10 (§ 3, RAPPORTÉ) mentionne `llama-3.1-8b` dans le résumé de l'article externe `2609.36490` (`lot3-Cc`), tandis que les pièces 1 (§ 9.4.A.3) et 3 (§ 0) parlent uniquement d'un « modèle de 8 milliards de paramètres » (RAPPORTÉ) sans le nommer. Je retire cette identification : le modèle cible reste strictement désigné comme « le modèle de 8 milliards de paramètres à poids ouverts de la banque T0.5 ».
- **Statut « VÉRIFIÉ » attribué aux lectures d'exécution des pièces 4, 5, 6, 7 (Critique A)** : **Acceptée.** N'ayant pas rejoué les scripts ni recalculé les empreintes des sorties d'exécution moi-même, je requalifie tous les résultats chiffrés des lancements (pièces 4, 5, 6) en **OBSERVÉ-NON-AUDITÉ** et les affirmations textuelles des dossiers en **RAPPORTÉ**.
- **Produit des puissances $\beta_{\text{total}} = \beta_{\text{TM}} \times \beta_{\text{pôle}}$ et borne de fuite $\mathcal{O}(k \log M / N_{\text{épreuve}})$ (Critiques A, D, E)** : **Acceptée.** Le produit des puissances suppose l'indépendance conditionnelle des deux filtres sachant $H_1$, qui est fausse si la difficulté de la fiche affecte les deux étages ; la vraie borne générale est $\max(0, \beta_{\text{TM}} + \beta_{\text{pôle}} - 1) \le \beta_{\text{total}} \le \min(\beta_{\text{TM}}, \beta_{\text{pôle}})$ (HYPOTHÈSE, reprise de E). De même, la vitesse de fuite dépend de la capacité d'exploitation de l'opérateur de recombinaison : je la requalifie en **HYPOTHÈSE** paramétrique testée par l'expérience E2 corrigée.
- **Contradiction de vérité terrain sur la porte de sortie R13 au tableau c.6 (Critique E)** : **Acceptée.** Des hypothèses existantes du programme (H1–H9, HC1–HC6) masquées et reformulées sont par définition des *redites internes* : elles constituent le **contrôle négatif** (qui doit être rejeté par la porte de nouveauté avec un taux de fausses sorties $\le 0,10$, illustratif), et non des témoins positifs. Les témoins positifs de sortie doivent être des hypothèses tenues à part (par exemple, H9 retirée temporairement du prompt du lecteur neuf pour vérifier qu'il la reconnaît comme neuve et décisive par rapport à H1–H8).

### 2. Sur l'Expérience E1 (Architecture de survie et multiplicité)
- **Tautologie des 5 témoins de couche 3 dans le bras strict et mélange de deux variables (conjonction vs 3 voies ET e-BH plat vs pondéré) (Critiques A, B, D, E)** : **Acceptée et transformée en test.** Compter une fiche « gelée en attente » comme un succès équivalent à une promotion sur épreuve compare une décision administrative à une preuve empirique, et condamne le bras 1 par construction sur la couche 3.
  - *Correction* : La distinction entre « promue Couche 1 » et « différée Couche 3 » est fixée comme **règle architecturale déterministe** (on ne jette pas une fiche parce que la banque de couche 2/3 n'est pas encore construite). L'expérience E1 est recentrée exclusivement sur une **même cohorte de fiches immédiatement testables (Couche 1)** et teste en plan factoriel $2 \times 2$ l'effet du filtre préalable des tests de mort (Actif vs Inactif) croisé avec la pondération e-BH (Pondérée par le score de développement/test de mort vs Plate), évalués sur la **même définition de confirmation terminale** sur épreuve fraîche.
- **Condition de validité de la pondération e-BH et sous-dimensionnement à 10 témoins (Critiques A, B, D, E)** : **Acceptée.** La garantie $\text{FDR} \le \alpha$ de e-BH pondéré exige que les poids $w_i \ge 0$ satisfassent $\sum_{i=1}^m w_i = m$ et soient $\mathcal{F}_0$-mesurables (gelés strictement *avant* toute lecture de l'épreuve, sur des données de développement ou de test de mort disjointes en tâches de l'épreuve), garantissant $\mathbb{E}[w_i E_i \mid \mathcal{F}_0] \le w_i$ sous le nul. L'effectif est porté à $n = 40$ témoins vrais et $40$ témoins faux en simulation sur banque pour éliminer la zone d'indécision binomiale.

### 3. Sur l'Expérience E2 (Fuite d'information inter-générationnelle)
- **Extinction sous nul homogène, faiblesse possible de l'opérateur de recombinaison, et inversion du test d'équivalence (Critiques A, B, D, E)** : **Acceptée et transformée en test.**
  1. Comme le montre E, si seules les survivantes engendrent $g+1$, alors sous nullité globale $\Pr(R_1 > 0) \le \alpha$ éteint 95 % des campagnes dès $g=1$, masquant la fuite conditionnelle $\Pr(R_{g+1} > 0 \mid \text{sélection sur } E_{\text{fixe}})$. Il faut donc sélectionner à chaque génération les $K$ fiches ayant **la plus haute richesse observée $\log W$ sur l'épreuve** (même sous le seuil de promotion) pour ensemencer $g+1$, sous un **nul hétérogène** (lois nulles variant par leurs traits et sous-populations de nuisance, critique B).
  2. Pour séparer « la réutilisation est sûre » de « le proposeur LLM exploite mal le bit de survie » (critique A), E2 inclut désormais un **opérateur de recombinaison adversarial (oracle sur les scores de sélection)** à côté du proposeur normal.
  3. Le critère d'équivalence $p > 0,10$ (fautif, critiques D et E) est remplacé par un duel d'inférence forte sur un paramètre unique $\theta = \text{FWER}_{\text{Fixe}} - \text{FWER}_{\text{Renouvelé}}$ avec marge $\delta = 0,03$ (illustratif) sur $R = 800$ campagnes simulées (illustratif, dimensionnement repris de A).

### 4. Sur l'Expérience E3 (Héritage négatif en contexte vs filtre mécanique)
- **Asymétrie du nombre d'appels (« rejette et redemande ») et longueur de contexte (Critiques A, D, E)** : **Acceptée.** Permettre au bras « filtre mécanique » de redemander des fiches après rejet lui octroie plus de tirages. Dans E3 corrigée, le nombre d'appels au proposeur est **strictement fixé à $M$ propositions brutes sans relance** dans tous les bras, et la longueur de prompt est appariée par l'ajout d'une archive neutre hors-sujet de même longueur en jetons (reprise de A, D, E) et d'un bras à raisons permutées.
- **Impuissance et biais de cible de la divergence $D_{\text{JS}}$ sur la sonde (Critiques A, B, D, E)** : **Acceptée.** Comme le démontre B, sur un moniteur binaire proche du nul ($\Delta p \approx 0,1$), $D_{\text{JS}} \approx (\Delta p)^2/8 \approx 0,001$, et du bruit aléatoire maximise $D_{\text{JS}}$ sans valeur scientifique (critique D). Je remplace $D_{\text{JS}}$ par le **rendement en propositions admissibles, distinctes (selon un canoniseur tiers gelé) et confirmées sur épreuve fraîche** à budget d'appels strictement fixe.

### 5. Sur l'Expérience E4 (Ablation de la boucle de sélection à la génération 2)
- **Confondant de testabilité du Bassin J, biais d'alignement d'instrument, et dégénérescence de $\text{Nats}/\$$ (Critiques A, B, D, E)** : **Acceptée.**
  1. Si le Bassin J est choisi parmi toutes les fiches des juges-modèles, il contient des fiches non traduisibles et perd par défaut de traduction (critique A). Les trois bassins parentaux — **Bassin P (Pôle)**, **Bassin J (Juges-modèles)** et **Bassin R (Aléatoire, contrôle négatif)** — sont désormais tous trois **conditionnés sur l'admissibilité au pont en génération 1** (reprise de A et E).
  2. La somme des excès $\log W - \log(m/\alpha)$ mesure le dépassement d'arrêt (overshoot) et favorise circulairement l'instrument du pôle (critiques A, B, D, E). Je l'abandonne au profit du **nombre de familles d'hypothèses distinctes confirmées sur une épreuve d'audit finale $T_{\text{audit}}$ évaluée à horizon fixe** (log-score prédictif hors échantillon et test de permutation à taille fixe, sans arrêt optionnel).
- **Critique de la baseline « extracteur régulier » sur le format texte libre de la course 1 (Critique B)** : **Rejetée pour la course 2, acceptée pour la course 1.** En course 1, le champ `loi_predictive` est en texte libre (RAPPORTÉ, pièce 7 § a.1), ce qui désavantage un extracteur régulier. En revanche, en course 2, la fiche comporte une prédiction chiffrée et signée utilisant une métrique de la **liste fermée M** et des données de la **liste fermée D** (RAPPORTÉ, pièce 7 § a.1). Sur les fiches de course 2, la table déterministe `métrique M × donnée D → spécification` (option D-P2.c de la pièce 7 § h) est donc un contrôle mécanique équitable et obligatoire.

---

## (b) Les expériences corrigées (Inférence forte, sans zone d'indécision muette)

*Convention commune (reprise de A et E) : Chaque expérience teste un paramètre $\theta$ contre une marge préenregistrée $\delta$ via le duel exclusif $\mathcal{H}_A : \theta > \delta$ contre $\mathcal{H}_B : \theta \le \delta$. Soit $[L_{95}, U_{95}]$ l'intervalle de confiance bilatéral à 95 % de $\hat{\theta}$ : si $L_{95} > \delta$, $\mathcal{H}_B$ est réfutée ; si $U_{95} \le \delta$, $\mathcal{H}_A$ est réfutée ; si $\delta \in [L_{95}, U_{95}]$, le verdict est explicitement déclaré **NON CONCLUANT (sous-dimensionné)** et déclenche la règle de repli associée.*

---

### Expérience E1 corrigée — Fidélité du pont et gain de puissance de la pondération e-BH (Couche 1)

Cette expérience scinde l'ancien E1 en deux volets orthogonaux : **E1a** (étalonnage du pont sur banc d'altérations) et **E1b** (plan factoriel $2 \times 2$ de la règle de sélection sur fiches admissibles).

- **Volet E1a (Fidélité et couverture du pont)** :
  - *Protocole* : Sur un banc de $N_{\text{banc}} = 60$ fiches (illustratif, dimensionné d'après A et B pour que 0 erreur donne une borne supérieure Clopper-Pearson $< 0,05$) composé de : 20 fiches réelles (10 de course 1 + 10 au format course 2), 20 témoins « aller-retour » écrits depuis une loi connue (dont 10 contenant **deux nombres cités** où un seul est l'effet cible, contrôle de A), et 20 témoins négatifs (5 à effet nul $\Delta w = 0$, 5 à sens inversé subtil, 5 à mauvaise sous-population, 5 hors-gabarit/théorème).
  - *Paramètre co-primaire* : Taux de traductions acceptées et matériellement fidèles $u_{\text{fidèle}} = \Pr(\text{Acceptée} \wedge \text{Fidèle})$ sur les 20 témoins aller-retour, et taux d'erreurs silencieuses $p_{\text{err}} = \Pr(\text{Acceptée avec loi erronée})$ sur les 40 témoins à vérité connue.
  - *Duel ($\delta_{\text{fid}} = 0,70$, $\delta_{\text{err}} = 0,05$, illustratifs)* :
    - $\mathcal{H}_A$ (Pont opérationnel) : $u_{\text{fidèle}} > 0,70$ ET $p_{\text{err}} \le 0,05$, avec un gain de couverture $\ge 0,20$ (illustratif) sur l'extracteur régulier sans LLM sur le sous-ensemble au format course 2.
    - $\mathcal{H}_B$ (Pont infidèle ou stérile) : $u_{\text{fidèle}} \le 0,70$ OU $p_{\text{err}} > 0,05$.

- **Volet E1b (Plan factoriel $2 \times 2$ : Filtre Test de Mort $\times$ Pondération e-BH)** :
  - *Protocole (en simulation sur banque fraîche de $N = 300$ épisodes, illustratif)* : Générer $m = 40$ propositions admissibles en Couche 1 + $40$ témoins vrais (log-cotes $\theta \in [0,5 ; 0,7]$, illustratif) + $40$ témoins faux sous nul informé (dont 20 à effet exactement nul « connu + 0 » sur le même moniteur, contrôle de A et B). Comparer 4 bras sur la **même épreuve fraîche** : (B1) Sans TM + e-BH plat ; (B2) Avec TM sur tranche de développement disjointe + e-BH plat sur survivantes ; (B3) Sans TM + e-BH pondéré par richesse de développement ($w_i \ge 0, \sum w_i = m$, gelés avant épreuve) ; (B4) Avec TM + e-BH pondéré. Contrôle négatif de pondération (D) : bras à poids aléatoires permutés.
  - *Paramètre* : Gain de rappel net $\Delta R = R_V(\text{B4}) - R_V(\text{B1})$ à $\widehat{\text{FDR}} \le 0,05$.
  - *Duel ($\delta_R = 0,10$, illustratif)* : $\mathcal{H}_A : \Delta R > 0,10$ (le pré-filtrage et la pondération augmentent la puissance en concentrant le budget $\alpha$) contre $\mathcal{H}_B : \Delta R \le 0,10$ (le pré-filtrage détruit autant de vraies qu'il économise de multiplicité ; on garde e-BH plat sans double filtre).

---

### Expérience E2 corrigée — Fuite adaptative sous nul hétérogène et opérateur cas-pire

- **Question** : La réutilisation d'une même épreuve de $N = 150$ épisodes sur $G = 3$ générations viole-t-elle le contrôle du FWER/FDR sous sélection des meilleures richesses ?
- **Protocole et contrôles négatifs (Simulation CPU pure, 0 USD d'API)** :
  - *Monde nul hétérogène (correction B)* : Toutes les lois proposées ont un effet vrai nul ($\Delta w = 0$ par rapport au vrai processus générateur dans la population infinie), mais portent sur 13 moniteurs et des traits de variances et fréquences marginales distinctes.
  - *Règle de reproduction sans extinction (correction E)* : À chaque génération ($m = 20$ lois), les $K = 5$ lois ayant obtenu la plus grande richesse $\log W$ sur l'épreuve (même si $\log W < \log(m/\alpha)$) sont sélectionnées comme parents de $g+1$.
  - *Quatre bras croisés sur $R = 800$ campagnes indépendantes (illustratif, correction A)* :
    1. **Fixe-Oracle (Cas pire, contrôle A)** : Épreuve fixe ($E_1 = E_2 = E_3$), recombinaison par un optimiseur local qui combine linéairement les traits des $K$ parents ayant maximisé $\log W$.
    2. **Fixe-Standard** : Épreuve fixe, opérateur de recombinaison bisociative standard du noyau.
    3. **Renouvelé-Oracle** : Épreuve fraîche tirée à chaque génération ($E_1 \perp E_2 \perp E_3$), même optimiseur local.
    4. **Fixe-Sans-Sélection (Contrôle de base B, D, E)** : Épreuve fixe, mais parents tirés au hasard parmi les $m$ lois (vérifie l'étalonnage nominal du juge).
- **Paramètre et duel** : Soit $\theta = \widehat{\text{FWER}}_{g=3}(\text{Fixe}) - \widehat{\text{FWER}}_{g=3}(\text{Renouvelé})$ (sous le nul global, $\text{FDR} = \text{FWER}$, remarque D et E), avec marge $\delta = 0,03$ (illustratif).
  - $\mathcal{H}_A$ (Fuite adaptative réelle) : $\theta > 0,03$ dans le bras Fixe-Standard ou Fixe-Oracle (borne inférieure $L_{95} > 0,03$). *Conséquence : interdiction absolue de réutiliser l'épreuve entre générations (D-P4 option a obligatoire).*
  - $\mathcal{H}_B$ (Robustesse du pare-feu) : $\theta \le 0,03$ y compris sous l'opérateur Fixe-Oracle ($U_{95} \le 0,03$).

---

### Expérience E3 corrigée — Archive négative en contexte contre filtrage mécanique à budget d'appels fixe

- **Question** : Exposer les proposeurs LLM aux fiches éliminées et à leurs motifs améliore-t-il ou dégrade-t-il le nombre de propositions distinctes et valides à $g=2$, à nombre d'appels strictement constant ?
- **Protocole et contrôles négatifs (appariés en longueur et en tirages, corrections A, B, D, E)** :
  - À partir d'un même état de génération 1 (5 survivantes, 15 éliminées), demander exactement $M = 30$ fiches brutes (illustratif, **sans aucune relance en cas de rejet**) réparties sur $P = 6$ populations parentales indépendantes de 5 fiches chacune, dans 4 bras :
    1. **Bras Complet (S + M-Vrai)** : Prompt = 5 survivantes + 15 mortes avec leurs vraies raisons d'échec + longueur totale $L_0$ jetons.
    2. **Bras Permuté (S + M-Perm, contrôle D)** : Prompt = 5 survivantes + 15 mortes avec raisons d'échec permutées aléatoirement ($L_0$ jetons ; sépare l'information causale de la raison et l'exposition au lexique des mortes).
    3. **Bras Neutre + Filtre Noyau (S + Texte-Neutre, contrôle A, B, D, E)** : Prompt = 5 survivantes + texte méthodologique hors-sujet complétant exactement à $L_0$ jetons ; la mémoire mécanique du noyau filtre post-hoc les redites.
    4. **Bras Sans-Héritage** : Prompt de génération 1 sans survivantes ni mortes, complété à $L_0$ jetons.
- **Métrique (sans $D_{\text{JS}}$ sur sonde interne)** : Nombre moyen par population de fiches de $g=2$ qui sont simultanément : (i) acceptées par le pont, (ii) non redondantes avec $g=1$ et entre elles selon un **canoniseur tiers gelé** (évaluation d'équivalence fonctionnelle sur une grille externe de 1 000 points d'entrée couvrant tout l'espace des traits, indépendante de la sonde du noyau, correction A, D, E), et (iii) survivantes au test de mort.
- **Paramètre et duel** : $\theta = \mu_{\text{Complet}} - \mu_{\text{Neutre+Filtre}}$, marge $\delta = 0$ (ou $\delta = 0,5$ fiche par population de 5, illustratif).
  - $\mathcal{H}_A$ (Gain de l'archive négative en prompt) : $\theta > 0,5$ ET $\mu_{\text{Complet}} > \mu_{\text{Permuté}}$.
  - $\mathcal{H}_B$ (Ancrage négatif ou inutilité du prompt négatif) : $\theta \le 0,5$ (le filtrage mécanique post-hoc par le noyau sur prompt épuré des mortes suffit ou domine).

---

### Expérience E4 corrigée — Ablation de la sélection du pôle à la génération 2 sur audit indépendant

- **Question** : À admissibilité initiale égale et budget d'appels égal, ensemencer la génération 2 par les survivantes du pôle produit-il plus de découvertes confirmées hors-pôle qu'un ensemencement par les juges-modèles ou par tirage aléatoire ?
- **Protocole et contrôles négatifs (corrections A, B, D, E)** :
  - *Conditionnement sur l'admissibilité (correction A et E)* : En génération 1, ne retenir que le vivier $\mathcal{V}_{\text{adm}}$ des fiches qui passent la garde de forme et sont traduites avec accord par le pont en Couche 1.
  - *Quatre bassins parentaux (taille $K = 4$ parents par réplication, $R = 5$ réplications par sous-banques/tâches, illustratif)* :
    1. **Bras P (Pôle)** : Les $K$ meilleures fiches de $\mathcal{V}_{\text{adm}}$ selon la sévérité du pôle + test de mort sur l'épreuve $T_1$.
    2. **Bras J (Juges-modèles)** : Les $K$ meilleures fiches de $\mathcal{V}_{\text{adm}}$ selon le classement des 3 juges-modèles (Kimi, Argon, Opus), sans regarder $T_1$.
    3. **Bras A (Aléatoire admissible, contrôle A, D, E)** : $K$ fiches tirées uniformément sans remise dans $\mathcal{V}_{\text{adm}}$.
    4. **Bras P-Inversé (Éliminées du pôle, contrôle B)** : Les $K$ fiches de $\mathcal{V}_{\text{adm}}$ les plus sévèrement réfutées sur $T_1$.
  - *Génération 2 à volume fixe* : Chaque bras génère exactement $m_2 = 15$ fiches filles (illustratif) à coût d'idéation identique.
  - *Audit terminal indépendant $T_{\text{audit}}$ (correction A, B, D, E)* : Toutes les filles traduisibles des 4 bras sont gelées et évaluées sur une même tranche d'audit $T_{\text{audit}}$ jamais vue ($N = 300$ épisodes, munie de 10 témoins vrais et 10 témoins faux d'étalonnage, contrôle A), selon **deux critères co-primaires** : (1) le juge figé avec seuil e-BH calculé **séparément par bras** à $m_2 = 15$ (évite la multiplicité asymétrique signalée par A et E) ; (2) un **audit statistique externe à horizon fixe** (différence de log-score prédictif moyen par épisode sur l'ensemble des $N = 300$ épisodes contre le prédicteur connu, testée par permutation stratifiée par tâche avec correction de Holm-Bonferroni à $\alpha = 0,05$, sans arrêt séquentiel). Les découvertes sont dédupliquées par le canoniseur tiers de E3.
- **Paramètre et duel** : Soit $\theta = Y_P - \max(Y_J, Y_A)$ le gain moyen de familles distinctes confirmées sur $T_{\text{audit}}$ (par l'audit à horizon fixe), avec marge $\delta = 0,5$ découverte par réplication (illustratif).
  - $\mathcal{H}_A$ (Fécondité héréditaire du pôle) : $\theta > 0,5$ ET $Y_P > Y_{\text{P-Inversé}}$.
  - $\mathcal{H}_B$ (Monde plat / absence d'héritage utile) : $\theta \le 0,5$ (alors que l'audit promeut $\ge 8/10$ témoins vrais et $0/10$ faux) $\implies$ **arrêt de la reproduction multi-générationnelle** au profit d'une génération 1 élargie (reprise du critère d'arrêt réclamé par B à E).

---

## (c) Réponse à la question de l'arbitre (en une page)

### 1. Ce qui est établi par les pièces servies
1. **L'architecture mécanique du pôle et du pont fonctionne à blanc** : En simulation (cycle v5, pièce 6, OBSERVÉ-NON-AUDITÉ), le juge figé par pari séquentiel (Ville + e-BH), le nul des filles v2 et la mémoire anti-redite tiennent leurs garanties de fausses promotions (0 fausse promue) et exploitent des lignées fécondes *quand le monde simulé en contient*. En lancement réel avec agents (« (a) bis », pièce 4, OBSERVÉ-NON-AUDITÉ), la plomberie complète (Opus 5.5 expérimentateur en bac `bwrap`, Fable 5.1 vérificateur, juge figé) tourne sans erreur pour 5,89 USD sur 11 fiches, mais dans un monde tautologique. Le pont `pont_v1.py` (pièces 7 et 8, RAPPORTÉ) est codé selon le principe « prédicteur connu + effet cité » avec double traduction aveugle inter-familles et passe 82 essais unitaires et 25/25 mutations sur banques synthétiques.
2. **Trois verrous empiriques bloquent aujourd'hui toute boucle générationnelle réelle** :
   - *Absence de puissance (« pas de dents ») sur données réelles* : Sur la banque réelle T0.5 (120 puis 288 épisodes d'un modèle 8B notés par deux juges), le pôle sous multiplicité e-BH promeut 0 fiche et 0 témoin vrai sur 5 (pièce 5, OBSERVÉ-NON-AUDITÉ ; en couche 1 bis, meilleure richesse 2,28 pour un seuil de 3,0, RAPPORTÉ, pièce 7 § a.4).
   - *Épuisement et absence des banques d'épreuve* : L'épreuve de la seule banque existante (T0.5) est entièrement lue ; les banques de couche 2 (avec sabotage) et de couche 3 n'existent pas (RAPPORTÉ, pièce 7 § Verdict.2). Or un effet réaliste (log-cotes 0,6) exige $\approx 150$ à $300$ épisodes d'épreuve frais par génération sous multiplicité (RAPPORTÉ, pièce 7 § a.4).
   - *Chaîne jamais reliée de bout en bout* : Les tests de mort sont codés mais jamais activés en course ; le pont n'a jamais traduit une vraie fiche ; aucune fiche de la course 1 n'est devenue une expérience du programme (RAPPORTÉ, pièce 1 § 9.2 et § 10).

### 2. Ce qui n'est pas établi (et qu'il ne faut pas présupposer dans la règle gelée)
1. **La viabilité de la conjonction stricte (Q1)** : Exiger « survit au test de mort ET promue par le pôle » pour survivre à la génération 1 éliminerait par construction les 45 à 60 % (SUPPOSÉ, pièce 7 § b.3) de fiches légitimes qui relèvent de la couche 3 (nouveaux épisodes/sondes requis) ou de preuves formelles (N3). **Règle retenue** : Séparer la population en quatre états — *Promue Couche 1* (entre dans le bassin reproducteur immédiat), *Gelée en attente Couche 3 / Théorie* (spécification scellée après accord du pont et survie au test de mort local, mise en file d'attente de devis GPU sans être éliminée ni comptée comme confirmée), *Indécise / Non traduisible N8* (retirée, ne passe pas à $g+1$), et *Réfutée* (archivée dans la mémoire du noyau).
2. **L'innocuité de la réutilisation d'épreuve (Q2) et de l'archive négative en prompt (Q3)** : Rien n'établit que la sélection darwinienne sur une épreuve fixe préserve la garantie de 5 % au-delà d'une génération, ni que montrer les fiches mortes aux LLM proposeurs les aide au lieu de les ancrer lexicalement. **Règle retenue par défaut** : Une tranche d'épreuve fraîche ($\ge 300$ épisodes) par génération ; seules les survivantes sont servies dans le prompt des proposeurs, tandis que les éliminées sont tenues par la mémoire mécanique du noyau pour filtrer les redites en aval.
3. **L'existence de lignées fécondes réelles (Q5, Q6)** : En monde plat (pièce 6) comme dans la rétrodiction de Swanson (pièce 1), la marche générationnelle ne bat pas l'allocation directe. Tant que l'ablation E4 n'a pas réfuté $\mathcal{H}_B$, il ne faut pas dépasser 2 générations. Pour éviter l'effondrement sur une lignée et le biais de testabilité, la reproduction est plafonnée par niche $(\text{Axe} \times \text{Opérateur canonisé})$ et la sortie vers le programme (Q4) est filtrée par un lecteur neuf (R13) sur distance prédictive non nulle à H1–H9 / HC1–HC6 et rattachement à une porte.

### 3. L'expérience à faire en premier (Ordre d'exécution séquentiel et portes d'arrêt)
Il est inutile de lancer une course 2 complète à 160 USD tant que le pont et la banque d'épreuve n'ont pas prouvé leurs dents. L'expérience prioritaire absolue combine **le premier essai étalonné du pont (D-P5 / E1a) et la simulation de non-fuite (E2)**, suivis de la génération d'une épreuve fraîche :

1. **Immédiatement (Coût : 2 à 5 USD d'API + 0 USD CPU, nœud D-P5 chez `session-depot`)** :
   - Jouer **E2 corrigée** en simulation CPU pure (800 campagnes sous nul hétérogène, Fixe vs Renouvelé avec opérateur oracle) pour trancher définitivement D-P4 (besoin d'épreuve fraîche par génération).
   - Jouer **E1a (D-P5 élargi)** : Tirer les 10 idées distinctes de la course 1 + 10 fiches synthétiques au format course 2 + 20 témoins aller-retour (dont 10 à deux nombres) et 20 témoins négatifs (dont « connu + 0 »), traduits en affectation croisée (Opus 5.5 / Kimi / Argon) contre l'extracteur régulier mécanique (D-P2 option c).
   - *Porte d'arrêt 1* : Si le pont échoue à $u_{\text{fidèle}} > 0,70$ ou $p_{\text{err}} \le 0,05$, on corrige la consigne du pont ou on impose un champ « loi » natif au proposeur (D-P1 option b) *avant* toute course 2.
2. **Juste après (Devis GPU dédié : ~25 à 45 USD illustratifs)** : Construire sur le modèle 8B à poids ouverts deux tranches d'épreuve fraîches disjointes $T_1$ et $T_2$ ($\ge 300$ épisodes chacune) et vérifier que le juge figé y promeut $\ge 80\%$ des témoins vrais de log-cotes $0,6$ et $0\%$ des témoins faux (« dents confirmées »). Alors seulement, lancer la génération 1 et l'ablation préenregistrée E4 en génération 2.

FIN-DE-CELLULE