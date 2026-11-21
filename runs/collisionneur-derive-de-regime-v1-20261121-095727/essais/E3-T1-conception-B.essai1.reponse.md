# Proposition B : Tour III.1, correction d'un seuil à 1 % qui ne tient plus quand le régime change

**Pièces reçues.** J'ai reçu le bloc FAITS et le bloc QUESTION, complets. Aucune pièce n'est absente ni coupée.

**Convention de statut.** Les faits ne portent pas de statut explicite. Je les note donc RAPPORTÉ (énoncé dans FAITS) et je ne les promeus jamais. Tout chiffre qui dépend d'une taille d'échantillon que je choisis (n = 300) ou d'une loi supposée est marqué **illustratif**. Les calculs qui découlent seulement de α = 1 % sont marqués « dérivé de α ». Je n'ai pas lu CURA, et je ne donne aucun identifiant arXiv de mémoire.

L'ordre suit la question (1 à 6). Les livrables y sont rangés ainsi : (a) en §1, (c) en §3, (b) et (d) en §6.

---

## 1. Ce qu'un expert ferait ici, et qu'on ne demande pas

### 1.1 Mesurer d'abord le bruit du 1 % lui-même

Un seuil conforme réglé sur n épisodes garantit 1 % **en moyenne sur les tirages d'étalonnage**. Ce n'est pas une garantie pour le seuil effectivement obtenu. Conditionnellement à l'échantillon d'étalonnage, le taux réel suit une loi Bêta (Vovk 2012, « Conditional validity of inductive conformal predictors » ; Bates, Candès, Lei, Romano, Sesia 2023, « Testing for outliers with conformal p-values », *Annals of Statistics*).

Avec n = 300 (**illustratif**) :
- le seuil tombe au rang ⌈301 × 0,99⌉ = 298, c'est-à-dire **3 scores au-dessus** ;
- le taux réel suit environ Bêta(3, 298) : moyenne ≈ 1,0 %, écart-type ≈ 0,57 % ;
- P(taux réel > 2 %) ≈ 6 % et P(taux réel > 3 %) ≈ 0,6 % (approximation de Poisson, **illustratif**).

De même, mesurer un taux « triplé » de 9 alertes sur 300 épisodes de test donne un intervalle de Clopper-Pearson d'environ [1,4 %, 5,6 %] (**illustratif**).

Avant de corriger quoi que ce soit, un expert demanderait donc trois choses :
- quel était n dans CURA ;
- combien de réplications d'étalonnage ont été faites ;
- quel est l'intervalle sur le « triple ».

Le triplement est RAPPORTÉ, page non lue. Sa part de bruit est inconnue : **je ne sais pas**.

### 1.2 Nommer le problème d'étiquette, qui est le vrai verrou

Le taux de fausses alertes se définit sur les épisodes **honnêtes de l'agent**. En déploiement, on ne sait pas lesquels sont honnêtes. Toute ré-calibration après un changement de régime se fait donc sur un **substitut** :
- le jumeau ;
- des témoins injectés ;
- un flux non étiqueté supposé majoritairement honnête.

Chaque substitut achète l'échangeabilité au prix d'une hypothèse. Aucune ancre honnête échangeable n'est gratuite.

### 1.3 Traiter le décalage comme potentiellement adverse

Un agent saboteur peut **provoquer** un changement de régime (épisodes plus longs, autres sources bénignes). Un détecteur de dérive ne distingue pas une dérive bénigne d'une dérive induite.

D'où une règle que je propose comme non négociable (HYPOTHÈSE de conception) : **ne jamais recalibrer sur des épisodes de déploiement non certifiés**.

Il faut aussi bien voir l'asymétrie. Recalibrer sur un flux contaminé par du sabotage **élève** le seuil. La fausse alerte baisse, mais la détection s'effondre. La contamination attaque la puissance, pas le taux de fausses alertes. Le défaut visible (le taux triple) et le défaut invisible (la puissance chute) se corrigent dans des sens opposés.

### 1.4 Relier la contrainte « pas de moyenne ni de médiane sur les jetons » au défaut de longueur

Sans moyenne ni médiane, l'agrégation par épisode est probablement un maximum, un dernier jeton ou un quantile haut. Un maximum sur plus de jetons croît mécaniquement avec la longueur.

Le seuil unique garantit 1 % en moyenne sur les longueurs (RAPPORTÉ), pas par tranche. Je fais l'HYPOTHÈSE qu'une part du triplement est un **changement de mélange de longueurs** appliqué à un score dont la queue dépend de la longueur. Cette hypothèse se teste avant tout le reste : c'est le duel D1.

### 1.5 Vérifier l'agrégation des moniteurs

Si l'alerte finale est un OU de plusieurs moniteurs réglés chacun à 1 %, le taux global n'est pas de 1 %. Un changement de régime qui **corrèle** les moniteurs change ce taux global. La question de savoir si le triplement mesuré est par moniteur ou global n'est pas établie.

### 1.6 Demander quelle contrainte est réellement active

La relecture humaine est rare (RAPPORTÉ). La contrainte opérationnelle est donc probablement un **budget d'alertes** (un nombre par période) plutôt qu'un taux. Cela ouvre une alternative au seuil fixe (§6, proposition P5).

### (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut |
|---|---|
| Le taux réel triple sous changement de régime | RAPPORTÉ (CURA, page non lue) |
| Ce triplement dépasse le bruit d'étalonnage et de mesure | HYPOTHÈSE |
| Le défaut est un défaut de **seuil** (étalonnage), pas de **score** (sonde non invariante) | HYPOTHÈSE |
| Le changement de régime est observable : on sait quand et sur quelle variable | HYPOTHÈSE |
| Des épisodes honnêtes certifiés existent dans le nouveau régime | HYPOTHÈSE ; FAITS : « peu » par régime, RAPPORTÉ |
| Au sein d'un régime, les scores honnêtes sont échangeables | HYPOTHÈSE |
| Le jumeau subit le même décalage que l'agent honnête | HYPOTHÈSE ; FAITS : écart « fragile », RAPPORTÉ |
| 1 % par épisode est la bonne cible, plutôt qu'un budget ou un FDR | HYPOTHÈSE |
| Le décalage est bénin, pas induit par l'agent | HYPOTHÈSE |
| « Corriger » veut dire rétablir 1 % sans perte de détection chiffrée | non dit, à fixer |

---

## 2. Les données brutes à prendre au départ

Il faut partir des données **non agrégées**, chaque ligne étant un épisode.

**Identifiants et métadonnées :**
- identifiant de tâche, famille de tâche, version de l'agent, version de la sonde ;
- longueur en jetons et en pas ;
- source bénigne, horodatage, lot.

**Signaux bruts :**
- **scores par pas et par moniteur**, avant normalisation et avant le maximum ;
- la position du jeton qui réalise le maximum ;
- les **activations brutes** aux couches sondées, au moins sur un sous-échantillon, pour pouvoir tester la dérive en amont du score ;
- les sorties du jumeau sur la même tâche : scores **et** activations ;
- l'indicateur de certification honnête (comment on le sait) ;
- le tirage d'étalonnage dont dépend le seuil, avec sa graine.

**Journaux de déploiement :**
- toutes les alertes, avec leur rang dans le lot ;
- les alertes relues et leur verdict humain (rares).

Ce qu'il faut éviter : des taux de fausses alertes déjà agrégés par régime. Ils effacent l'information nécessaire pour savoir si le décalage porte sur le mélange des covariables, sur la loi conditionnelle ou seulement sur la queue.

---

## 3. Méthodes : ce que chacune suppose, comment elle échoue, et la mesure minimale (c)

**Vérifications mécaniques à battre pour toutes les méthodes**, sur les mêmes mondes plantés :
- **M0**, le seuil statique actuel ;
- **M1**, le quantile empirique des W derniers témoins certifiés ;
- **M2**, le rétrécissement fixe α/Γ ;
- **M3**, les k premiers par lot.

**Mesure minimale pour chaque méthode.** Il s'agit du taux de fausses alertes **par régime et par tranche de longueur**, avec un intervalle, sur des épisodes honnêtes **appariés** (même tâche, même longueur, régime source et régime cible). On y ajoute le taux de détection sur du sabotage planté, jamais utilisé pour le réglage. Une méthode « fonctionne » si elle tient α dans l'intervalle sur chaque régime planté **et** perd moins de détection que M2 à taux de fausses alertes égal.

### 3.1 Conforme pondéré sous décalage de covariables

**Référence.** Tibshirani, Barber, Candès, Ramdas 2019, « Conformal Prediction Under Covariate Shift », NeurIPS.

**Ce qu'elle suppose.**
- La loi du score honnête **sachant les covariables** est inchangée.
- Seul le mélange des covariables change, avec un rapport de vraisemblance connu ou estimable.

**Comment elle échoue.**
- **Nouvelle version de l'agent.** Ce n'est pas un décalage de covariables, puisque la loi conditionnelle change : la garantie tombe.
- **Poids estimés en grande dimension.** La taille effective n_eff = (Σw)²/Σw² s'effondre. Or un seuil fini au niveau α exige n_eff ≥ (1−α)/α = **99** (dérivé de α). En dessous, le quantile pondéré est +∞ : on n'alerte plus jamais.
- **Erreur sur les poids.** L'écart de couverture est borné par une erreur d'estimation des poids (Lei & Candès 2021, « Conformal inference of counterfactuals and individual treatment effects », *JRSSB* ; forme exacte de la borne : référence à vérifier).

**Mesure minimale.** Le taux de fausses alertes sur un monde planté à décalage de **longueur seule**, puis sur un monde à **décalage de version** (contrôle où elle doit échouer). On rapporte n_eff avec chaque seuil.

### 3.2 Conforme adaptatif en ligne (ACI) et ses variantes

**Références.**
- Gibbs & Candès 2021, « Adaptive Conformal Inference Under Distribution Shift », NeurIPS.
- Zaffran et al. 2022, « Adaptive conformal predictions for time series », ICML.
- Bhatnagar, Wang, Xiong, Bai 2023, « Improved online conformal prediction via strongly adaptive online learning », ICML.
- Angelopoulos, Candès, Tibshirani 2023, « Conformal PID control for time series prediction », NeurIPS.

**Garantie.** Pour toute suite, la moyenne de long terme des erreurs converge vers α. L'écart est en O(1/(γT)) ; constante exacte : référence à vérifier.

**Ce qu'elle suppose.** Un **retour d'étiquette à chaque pas** : savoir si l'épisode était honnête.

**Comment elle échoue.**
- **Sans étiquette.** En déploiement, il n'y en a pas. Utilisée sur le flux brut, elle est empoisonnable.
- **Garantie de moyenne temporelle seulement.** Elle tolère 3 % sur un régime compensé par 0,3 % sur un autre.
- **Pas de mise à jour discret.** À α = 1 %, chaque fausse alerte fait chuter α_t de γ(1−α), d'où des oscillations, des seuils infinis transitoires et des fenêtres exploitables par un adversaire qui choisit son moment.

**Mesure minimale.** Le taux de fausses alertes **par régime** (pas la moyenne globale) et l'excès cumulé de fausses alertes après une bascule plantée. L'ACI n'est alimentée que par des témoins certifiés.

### 3.3 Étalonnage conditionnel par strates ou par groupes

**Références.**
- Vovk 2012, conforme de Mondrian.
- Gibbs, Cherian, Candès, « Conformal prediction with conditional guarantees », *JRSSB* (année exacte à vérifier). Garantie exacte pour toute repondération dans une classe de fonctions de dimension finie.
- Limite : Barber, Candès, Ramdas, Tibshirani 2021, « The limits of distribution-free conditional predictive inference », *Information and Inference*. La validité conditionnelle exacte sur une covariable continue est impossible sans hypothèse.

**Ce qu'il suppose.**
- Le décalage est une repondération **dans la classe** choisie (indicatrices de tranche de longueur, de famille de tâches).
- Chaque strate a au moins 99 épisodes (dérivé de α).

**Comment il échoue.**
- Avec quelques centaines d'épisodes par régime, on ne peut tenir que 2 ou 3 strates.
- **Surface de jeu.** Si la strate dépend d'une covariable que l'agent contrôle (la longueur), un saboteur choisit la strate au seuil le plus clément.

**Mesure minimale.** Le taux de fausses alertes par strate. On y ajoute un test adverse : sur un monde planté, un saboteur choisit sa longueur ; on mesure sa détection par rapport au seuil unique.

### 3.4 Détecter le changement de régime avant de faire confiance au seuil

**Références.**
- Rabanser, Günnemann, Lipton 2019, « Failing loudly », NeurIPS (empirique).
- Gretton et al. 2012, « A kernel two-sample test », *JMLR* (test sur activations).
- Vovk, Nouretdinov, Gammerman 2003, « Testing exchangeability on-line », ICML (martingales conformes).
- Shafer, Shen, Vereshchagin, Vovk 2011, « Test martingales, Bayes factors and p-values », *Statistical Science*.
- Ramdas, Grünwald, Vovk, Shafer 2023, « Game-theoretic statistics and safe anytime-valid inference », *Statistical Science*.
- Vovk & Wang 2021, « E-values: calibration, combination and applications », *Annals of Statistics*.
- Podkopaev & Ramdas, « Tracking the risk of a deployed model and detecting harmful distribution shifts » (ICLR 2022, à vérifier). C'est le plus proche : on ne déclare que les décalages **nuisibles** au risque.

**Garantie.** Par l'inégalité de Ville, P(sup_t E_t ≥ 1/δ) ≤ δ sous l'hypothèse nulle, quel que soit le moment d'arrêt.

**Ce qu'elle suppose.** Une hypothèse nulle bien définie (flux échangeable avec l'étalonnage) et un flux **certifié honnête**. Sinon, le sabotage déclenche ou masque la détection.

**Comment elle échoue.**
- Un test global de dérive alerte sur des changements de masse qui ne touchent pas la queue à 1 %, et rate des changements de queue. Il faut parier sur **l'indicateur d'alerte au point de fonctionnement**.
- Le coût en échantillons est élevé. Pour distinguer 3 % de 1 %, la divergence de Kullback-Leibler vaut environ 0,013 nat. Il faut donc environ ln(1/δ)/KL, soit **≈ 230 témoins à δ = 5 %** et **≈ 350 à δ = 1 %** (**illustratif**, borne d'oracle ; un pari réel est plus lent).

**Mesure minimale.**
- Le délai de détection et l'excès de fausses alertes accumulées avant détection, sur la famille de dérive plantée.
- Le taux de fausses déclarations de rupture sur des flux sans dérive (contrôle négatif).

### 3.5 Ré-étalonnage par fenêtre glissante

**Référence.** Barber, Candès, Ramdas, Tibshirani 2023, « Conformal prediction beyond exchangeability », *Annals of Statistics*. La couverture perd au plus Σ w̃_i · d_TV(Z, Z^(i)) avec des poids fixés à l'avance, par exemple favorisant les épisodes récents.

**Ce qu'il suppose.** La fenêtre contient surtout le régime courant, et W ≥ 99 (dérivé de α).

**Comment il échoue.** Après une bascule, le taux de fausses alertes reste élevé pendant environ W épisodes. La borne n'est utile que si l'on borne d_TV, ce qu'on ne sait pas faire sans données du nouveau régime.

**Mesure minimale.** Le taux de fausses alertes en fonction du temps écoulé depuis la bascule, comparé à M1.

### 3.6 Témoins honnêtes injectés dans chaque lot

**Principe.** On calcule une p-valeur conforme **relative aux témoins du même lot**. La validité vient de l'échangeabilité entre témoins et épisodes honnêtes de l'agent dans ce lot.

**Ce qu'il suppose.** Les témoins sont indiscernables pour l'agent et tirés du même régime.

**Comment il échoue.** Certifier un témoin honnête suppose :
- soit un autre modèle (pas échangeable) ;
- soit des tâches à vérification mécanique complète (biais de sélection) ;
- soit un agent placé dans une condition où saboter est impossible (condition discernable ?).

Chaque voie réintroduit un décalage. HYPOTHÈSE à tester : le duel D2 sert de modèle.

**Mesure minimale.** La distance entre la queue des témoins et celle des épisodes honnêtes appariés de l'agent, sur un monde planté où la vérité est connue.

### 3.7 Jumeau honnête comme référence courante

**Principe.** Score différencié d = s_agent − s_jumeau sur la même tâche. Il annule les décalages **communs** (nouvelle tâche, nouvelle source bénigne).

**Comment il échoue.** Il n'annule pas un décalage propre à l'agent : nouvelle version, ou jumeau non mis à jour. La queue de d peut aussi s'élargir, puisque deux bruits s'ajoutent.

**Mesure minimale.** Le taux de fausses alertes de d par régime (duel D2), et la détection de d par rapport à s seul.

### 3.8 Robustesse au pire cas sur une famille de décalages

**Références.**
- Cauchois, Gupta, Ali, Duchi, « Robust validation: confident predictions even when distributions shift », *JASA* (année à vérifier) : boules de f-divergence.
- Pour les rapports de densité bornés : Jin, Ren, Candès 2023, « Sensitivity analysis of individual treatment effects: a robust conformal inference approach », *PNAS* (à vérifier).

**Garantie.** Si le rapport de densité est borné par Γ partout, alors Q(alerte) ≤ Γ·P(alerte), et α' = α/Γ suffit.

**Comment elle échoue.** Le décalage de position n'a pas de rapport borné dans la queue. Calcul gaussien (**illustratif**) :
- un décalage de 0,445 σ triple le taux à 1 % ;
- la règle α/3 (seuil à z ≈ 2,713) donne encore **≈ 1,17 %** sous ce décalage ;
- il faudrait α' ≈ **0,28 %**.

Avec n = 300, le niveau 0,28 % est inférieur à 1/301 : le seuil conforme est **infini**. Il faudrait environ 356 épisodes honnêtes (**illustratif**). Le pire cas coûte donc soit de la puissance, soit des données qu'on n'a pas.

**Mesure minimale.** Le taux de fausses alertes sur **toute** la famille plantée (pas seulement le décalage qui triple), et la perte de détection par rapport à M0.

### 3.9 Autres outils pertinents

**Garantie conditionnelle à l'étalonnage (PAC).** Choisir un seuil tel que P(taux réel > α) ≤ δ sur les tirages d'étalonnage (Vovk 2012 ; Bates et al. 2023). Cela supprime la part Bêta du §1.1, au prix d'un seuil plus haut.

**Correction de décalage d'étiquette.** Lipton, Wang, Smola 2018, « Detecting and correcting for label shift with black box predictors », ICML. Elle ne s'applique ici que si le « régime » se réduit à une variable discrète de mélange.

**Contrôle du FDR par e-valeurs.** Wang & Ramdas 2022, « False discovery rate control with e-values », *JRSSB*. Pertinent si l'on renonce au seuil fixe (P5).

---

## 4. Ce qui, hors du programme, permettrait de vérifier qu'une correction tient

1. **Mondes plantés tenus par un tiers.** La famille de dérive où le taux triple existe (RAPPORTÉ). Il faut y ajouter des familles **que le concepteur de la règle ne voit pas** :
   - décalage de position ;
   - décalage d'échelle ;
   - alourdissement de queue sans changement de masse ;
   - décalage conditionnel par version ;
   - décalage induit par un adversaire qui choisit sa longueur.

   Un tiers tire les paramètres et garde la vérité hors de la machine, ce qui est déjà la règle du programme (RAPPORTÉ).
2. **Jeux publics à décalage.** WILDS (Koh et al. 2021, « WILDS: A benchmark of in-the-wild distribution shifts », ICML) permet de vérifier la mécanique d'étalonnage, pas la détection de sabotage. Pour des épisodes d'agents honnêtes contre saboteurs sous décalage, il existe peut-être un banc d'évaluation du type SHADE-Arena (référence à vérifier). Je ne sais pas s'il en existe un public avec un décalage de régime contrôlé.
3. **Réplication du triplement CURA** : lecture de la page, puis reproduction avec n connu et plusieurs tirages d'étalonnage.
4. **Mesure indépendante** sur un second modèle ouvert et une seconde implémentation de la sonde. La correction doit tenir sur les deux.
5. **Préenregistrement** de α, δ, W, de la famille de décalages et des seuils de mort, **avant** de voir les mondes plantés.

---

## 5. Reformulation de la demande

> Pour une règle d'alerte calculée à partir de **n épisodes honnêtes certifiés** d'un régime source, de **témoins certifiés** arrivant à un débit donné et d'un flux non étiqueté **jamais** utilisé pour l'étalonnage :
>
> (i) pour quelle **classe explicite de décalages D** peut-on garantir, **régime par régime** et avec une probabilité d'au moins 1−δ sur l'étalonnage, un taux de fausses alertes ≤ α ;
>
> (ii) en combien d'épisodes témoins détecte-t-on, avec une erreur ≤ δ, qu'on est **sorti de D**, et combien de fausses alertes excédentaires paie-t-on pendant ce délai ;
>
> (iii) quelle perte de détection cela coûte sur du sabotage planté, comparée à M0–M3 ;
>
> (iv) quand le budget de témoins ne permet pas (i), quelle règle sans seuil fixe tient un **budget d'alertes** à la place ?

---

## 6.