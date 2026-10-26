# Proposition B · Tour III.3 : riposte

## 0. Pièces reçues

- **FAITS** : le bloc est vide par décision déclarée de l'arbitre. Rien n'est donc VÉRIFIÉ. Le cadre et la littérature sont RAPPORTÉS. Le reste est HYPOTHÈSE.
- **Conception B (III.1), équipe rouge A, équipe rouge C** : les trois pièces sont complètes et non coupées. Je les traite comme des données. Je n'ai pas recalculé leurs empreintes sha256.
- **Périmètre** : je ne réponds qu'aux sections « Contre la proposition B ».
- **Notation** :
  - A·B-n désigne les failles soulevées par A ;
  - C·n, C·év-n et C·ctl-n désignent respectivement les failles, les évasions et les contrôles de C.

---

## (a) Décision attaque par attaque

### Attaques de A

| Attaque | Décision | Raison, correction ou test |
|---|---|---|
| **A·B-1** (X3 vrai par construction sous F-immédiat) | **Acceptée** | Un adversaire qui lit le refus obtient une aire ROC de $\tfrac12 + \tfrac{\mathrm{TPR}-\mathrm{FPR}}{2}$. La fuite découle donc analytiquement de la qualité du filtre ; ce n'est pas une question empirique. F-immédiat est **abandonné comme dessin**. Il ne sert plus que de **contrôle positif** dans X3′a. |
| **A·B-2** (l'annulation est un bit) | **Acceptée, bornée, transformée en test** | L'annulation livre au plus 1 bit par exécution, à deux conditions. (i) **Quarantaine** : le code, le journal et les artefacts d'une exécution annulée ne sont jamais réinjectés dans $\mathcal{O}$. (ii) Lazar tient un **registre inter-exécutions** des annulations, comptées comme bits sur $D_{\mathrm{test}}$. X3′a vérifie que rien ne passe au-delà de ce bit. |
| **A·B-3** (`generate` non filtré en sortie) | **Acceptée** | C'est un trou réel. Correction : les sorties de `generate` passent par un filtre de sortie, avec la même sémantique différée que les entrées. Le test d'extraction devient **X0**, à faire en premier. |
| **A·B-4** (budget de bits incohérent avec `generate`) | **Acceptée, avec C·4** | La borne est reformulée en deux registres (§b.1). La parenthèse de A elle-même énonce la condition de validité. |
| **A·B-5** (X1 : variance entre exécutions, a2) | **Acceptée** pour la variance et pour a2 ; **rejetée** pour « l'expérimentateur devient adaptatif » | Prenons des points de contrôle **fixés avant l'exécution**, évalués à l'aveugle sur $D_{\mathrm{frais}}$ après la fin, sans aucune rétroaction vers $\mathcal{O}$ ni vers le dessin. Les artefacts sont alors des fonctions de $(D_{\mathrm{val}}, \mathcal{O})$, indépendantes de $D_{\mathrm{frais}}$. $m$ évaluations coûtent un terme en $\ln m$ dans une borne d'union, sans adaptativité. Pour a2 : $D_{\mathrm{val}}$ et $D_{\mathrm{frais}}$ sont tirés par **partition aléatoire d'un même réservoir** avant tout usage. Ils sont alors échangeables par construction. |
| **A·B-6** (placebo par permutation détectable) | **Acceptée** | Je reprends le placebo cohérent de C (C·ctl-1) et le pré-test de détectabilité de A (contrôle 3). Voir X2′. |
| **A·B-7** (fuite construction / évaluation, X4 et réservoir B) | **Acceptée** | $\mathcal{O}$ ne fournit plus de générateur de stimuli. Il fournit seulement une **description du concept en langue naturelle**, sous forme de champ du gabarit. Les stimuli sont produits par un générateur fixé par Lazar, puis répliqués sur un réservoir **B′** issu d'un générateur indépendant (C·ctl-4). |
| **A·B-8** (X5 confond critère et scellement ; nulles faciles) | **Acceptée** | Plan factoriel 2×2, avec ajout de **nulles de surface**. Voir X5′. |
| **A·B-9** (métrique de X6 manipulable ; contrôle vide) | **Acceptée** | Le contrôle vide est supprimé et le comptage libre abandonné. X6′ repose sur une banque de questions fixée par Lazar et sur des mondes nuls sentinelles. |
| **A·B-10** (tâche de contrôle de Hewitt & Liang 2019 non définie au niveau du texte) | **Acceptée** | Elle est définie au niveau du texte dans X4′. |
| **A·B-11** (la file synchrone fuit par la charge de l'hôte) | **Acceptée, transformée en test** | Le fait F2 est à déclarer : $D_{\mathrm{test}}$ est évalué sur un hôte séparé, ou hors de toute exécution active. Le volet temporel est testé dans X3′b. |

**Évasions de A (table b)**

- **Budget de bits contourné par `generate`** : traité par A·B-3 et X0.
- **Dichotomie contre F-immédiat** : sans objet, puisque F-immédiat est abandonné.
- **Sondes de cohérence contre F-différé** : **rejetée après correction**. La variante F-différé′ rend la **vraie réponse** et se contente de marquer la requête en silence. Il n'y a donc plus rien de factice à détecter.
- **Requêtes calées sur une frontière de palier** : **acceptée**. Le palier est remplacé par un ordonnancement au coût pire cas, calculé à partir de la seule requête (X3′b).
- **« Engager beaucoup d'hypothèses et rapporter les confirmées »** : **acceptée**. Le gabarit impose désormais un plafond de $m$ engagements par exécution et une correction de Holm.
- **Ladder** : A le juge tenable. Aucune action.

**Scénario « tous à la fois » : accepté.** Mon dessin est conditionnel à deux points : a6 est fausse, et $D_{\mathrm{val}}$ est chez l'hôte. Ces deux points deviennent des **préconditions**, X0 et le fait F1, qui passent **avant** toute autre expérience et non après X6.

**Contrôles fatals 1 à 7 de A : tous intégrés.**

| Contrôle de A | Où il est intégré |
|---|---|
| 1 | X0 |
| 2 | Fait F1 |
| 3 | Pré-test de X2′ |
| 4 | X5′ |
| 5 | X3′a |
| 6 | Fait F2 et X3′b |
| 7 | Registres du §b.1 |

### Attaques de C

| Attaque | Décision | Raison, correction ou test |
|---|---|---|
| **C·1** (contrôle du duel 6a vrai par construction) | **Acceptée** | Supprimé. Il est remplacé par une mesure directe du transfert du substitut vers le modèle de 8 milliards (X6′, duel 6a). |
| **C·2** (variante B-ouverte) | **Acceptée en partie** | **J'accepte** le conflit avec P4 : un calcul local sous E1 n'est pas une primitive journalisée. **Je rejette** « la borne explose ». Par l'argument même de C en C·4, les activations de textes écrits par $\mathcal{O}$ ont une information mutuelle nulle avec $D_{\mathrm{val}}$, sous l'hypothèse $H_W$ (voir §b.1, testée par X0). C·2 et C·4 se contredisent sur ce point. **Je rejette aussi** « sélection locale = fuite fatale » : choisir localement une direction avant `commit` relève de l'exploration, ce qui est permis. La protection vient de la confirmation scellée sur B et B′. **Décision** : B-ouverte n'est plus la variante par défaut. Elle n'est admissible que si les exécutions E1 sont journalisées (code et empreintes des entrées). C'est à Lazar de trancher. |
| **C·3** (métrique de `fit_probe` non arrondie) | **Acceptée en partie** | **J'accepte** que tout scalaire rendu soit quantifié sur $b$ bits et inscrit au registre $L_{\mathrm{ind}}$. **Je rejette** l'idée d'un « canal à haute capacité » comme menace. La géométrie d'un modèle **ouvert** (RAPPORTÉ par le cadre) n'est protégée ni par P1 ni par P3 : c'est l'objet même de E2. Elle ne devient une fuite que par la mémorisation, que X0 teste. |
| **C·4** (confusion de domaine dans $\sum b_i$) | **Acceptée** | Voir §b.1. |
| **C·5** (placebo détectable, plantage de $\mathcal{O}$) | **Acceptée** | Même point que A·B-6. |
| **C·6** (X5 et X6 incompatibles : pas de vérité terrain en génération ouverte) | **Acceptée, transformée en test** | Des **mondes nuls sentinelles** sont ajoutés dans X6′. |
| **C·év-1** (réponse factice détectable ; fragmentation ; faux refus) | **Rejetée** pour la détection, qui n'a plus d'objet (F-différé′). **Acceptée** pour la fragmentation et les faux refus | Le confinement se mesure sur **l'union des textes d'une exécution**, au sens du confinement de Broder (1997), et non requête par requête. Le compromis entre faux refus et quota exploitable devient X3′c. |
| **C·év-2** (débordement de lot) | **Acceptée** | (i) L'admission d'un lot se fait sur le **coût pire cas calculé à partir de la seule requête**. (ii) Aucun cache n'est utilisé pour les requêtes de $\mathcal{O}$. (iii) `generate` calcule toujours `max_jetons`, puis tronque. Le rang du lot ne dépend alors que des requêtes. Testé dans X3′b. |
| **C·év-3** (générateur du réservoir B piégé) | **Acceptée** | Même point que A·B-7, plus le réservoir B′. |
| **C·év-4** (indice positionnel qui bat le sac de mots) | **Acceptée** | On ajoute une sonde de référence sur traits de surface explicites, y compris positionnels (X4′). |
| **C·ctl-1 à 4** | **Intégrés** | Respectivement dans X2′, X3′c, X4′ et X5′/X6′. |

Je m'applique aussi une critique que C adresse à A (C·5 contre A) : un taux de conversion entre temps humain et heures de carte graphique est arbitraire. X6′ rapporte donc ses résultats sur une plage de taux.

---

## (b) Expériences corrigées

### b.0 Faits à déclarer par Lazar (ce ne sont pas des expériences ; aujourd'hui non dits)

- **F1** : où vit $D_{\mathrm{val}}$ (a3).
- **F2** : $D_{\mathrm{test}}$ est évalué sur un hôte séparé, ou sans exécution concurrente (A·B-11).
- **F3** : une seule évaluation sur $D_{\mathrm{test}}$ par programme (a4).

### b.1 Borne corrigée : deux registres (réponse à A·B-4 et C·4)

On fixe l'aléa de $\mathcal{O}$, si bien que $q_i$ est une fonction de $T_{i-1}$. Par la règle de chaîne :
$$
I(T_k;D)=\sum_{i=1}^{k} I(r_i;D\mid T_{i-1}).
$$

Considérons d'abord une réponse de la forme $r_i=f(q_i,W,\text{graine})$, où $W$ désigne les poids des modèles (le modèle ouvert et les modèles de langue appelés par $\mathcal{O}$). Si $W$ est indépendant de $D$, le terme correspondant de la somme est nul.

Cette indépendance est l'**hypothèse $H_W$** (HYPOTHÈSE, testée par X0). Sous $H_W$, seules les réponses du registre $L_{\mathrm{val}}$ (`score_val`) contribuent :
$$
I(T_k;D)\le \sum_{i\in L_{\mathrm{val}}} b_i .
$$
La borne par longueur de description du §1.2 de III.1 s'applique alors avec $k_{\mathrm{val}}\,b$ au lieu de $kb$. La raison : une fois les réponses du registre $L_{\mathrm{ind}}$ déterminées par les requêtes, il ne reste que $2^{k_{\mathrm{val}} b}$ transcriptions qui dépendent de $D$.

Le registre $L_{\mathrm{ind}}$ couvre tout le reste : `encode`, `fit_probe`, `predict` et `generate` sur des textes de $\mathcal{O}$. Il est journalisé et quantifié, mais il ne compte **pas** dans la borne, et ce **seulement si X0 ne rejette pas $H_W$**.

Si X0 rejette $H_W$, les bits de $L_{\mathrm{ind}}$ comptent eux aussi, et `generate` rend la borne vide. Il faut alors un filtre de sortie et des jeux $D_{\mathrm{val}}$ et $D_{\mathrm{test}}$ non mémorisés.

### X0 : les modèles ont-ils mémorisé $D_{\mathrm{val}}$ ou $D_{\mathrm{test}}$ ? (nouvelle ; elle conditionne tout le reste)

- **H_A** : le modèle de 8 milliards, ou un modèle de langue appelable, distingue les items de $D_{\mathrm{val}}$ ou de $D_{\mathrm{test}}$ des items témoins. On le mesure par une aire ROC qui combine la complétion exacte du suffixe à partir d'un préfixe et un score de vraisemblance.
- **H_B** : cette aire vaut environ 0,5.
- **Témoins** : des items rédigés par Lazar selon les mêmes consignes, après la date de coupure. Pas d'appariement par perplexité : c'est la critique de C contre A, que je m'applique. Le risque de dérive temporelle (même source) est déclaré.
- **Contrôle positif** : sur un modèle à corpus ouvert, de type OLMo (corpus et taille à vérifier), le détecteur doit séparer des items connus présents dans le corpus d'items connus absents, **paraphrases comprises**. Je reprends ici le contrôle 1 que C adressait à A.
- **Seuil** : la borne inférieure de l'intervalle de confiance à 95 % de l'aire dépasse 0,5. L'intervalle est obtenu par bootstrap sur les items.
- **Falsification** :
  - un rejet de H_B fait tomber $H_W$, donc le registre $L_{\mathrm{ind}}$ « gratuit » ;
  - si l'aire vaut environ 0,5 alors que le contrôle positif détecte, H_A est falsifiée à la sensibilité mesurée de ce détecteur, et à elle seule ;
  - si le contrôle positif échoue, X0 est **non concluante**. Ce n'est pas une confirmation de H_B.
- **Coût** : hors de la boucle. Des passes avant sur $|D_{\mathrm{val}}|+|D_{\mathrm{test}}|+|\text{témoins}|$, soit de quelques minutes à quelques heures de carte graphique (illustratif, d'après l'ordre de grandeur du §d de III.1).

### X1′ : surapprentissage de $D_{\mathrm{val}}$

- **Dispositif** :
  - $D_{\mathrm{val}}$ et $D_{\mathrm{frais}}$ sont obtenus par partition aléatoire d'un même réservoir ;
  - les points de contrôle $k\in\{10,50,200\}$ (illustratif) sont préenregistrés ;
  - l'évaluation est aveugle, après la fin de l'exécution, sans rétroaction ;
  - on ajoute un facteur $b\in\{1,7\}$, pour tester la thèse 1.
- **Métrique** : la pente de $\Delta(k)=S_{\mathrm{val}}-S_{\mathrm{frais}}$ en fonction de $\log k$, estimée par un modèle mixte avec un effet aléatoire par exécution. Le contraste se fait à l'intérieur d'une même exécution (A·B-5).
- **Hypothèses** :
  - **H_A** : la pente est positive ;
  - **H_B** : la pente est nulle dans l'intervalle de confiance.
- **Contrôles** :
  - **négatif** : candidats non adaptatifs ;
  - **positif** : attaque de type « boosting » sur des étiquettes aléatoires.
- **Falsification** :
  - une pente positive avec un contrôle négatif plat falsifie H_B ;
  - un intervalle de confiance qui contient 0 alors que le contrôle positif détecte falsifie H_A à ces valeurs de $k$ ;
  - une interaction $k\times b$ nulle falsifie la thèse 1.

### X2′ : le contenu des réponses de E2 cause-t-il le gain ?

- **Bras** :
  - E2 réelle ;
  - E2 **placebo cohérent** : vraies réponses d'un autre modèle ouvert, de dimension compatible ou projetée (le choix reste à vérifier), déterministes et lisses (C·ctl-1) ;
  - sans E2.
- **Pré-test de détectabilité** (contrôle 3 de A) : un discriminateur, qu'il s'agisse d'un modèle de langue ou des propres contrôles de cohérence de $\mathcal{O}$, classe des transcriptions réelles et placebo. X2′ n'est menée que si l'intervalle de confiance de son aire ROC contient 0,5. Sinon, le placebo est jugé détectable et X2′ est **annulée**, pas réinterprétée.
- **Hypothèses** :
  - **H_A** : $S_{\mathrm{frais}}(\text{réel})>S_{\mathrm{frais}}(\text{placebo})$, avec un intervalle de confiance qui exclut 0. Le gain viendrait alors de l'information **propre** au modèle de 8 milliards.
  - **H_B** : égalité. Des réponses cohérentes quelconques, ou le seul budget, suffisent.
- **Falsification** : chaque issue falsifie l'autre hypothèse. L'écart entre le placebo et le bras « sans E2 » mesure l'effet de réponses cohérentes non spécifiques.

### X3′ : fuites de l'interface vers $D_{\mathrm{test}}$

**X3′a : appartenance sous F-différé′.** Dispositif : réponse réelle, confinement mesuré sur l'union des textes d'une exécution, annulation, quarantaine.

- **H_A** : un adversaire inter-exécutions qui voit toute l'interface obtient une aire d'appartenance **supérieure** à celle d'un adversaire simulé qui ne reçoit que le bit d'annulation.
- **H_B** : les deux aires sont égales.
- **Contrôle positif** : un hôte en F-immédiat doit donner une aire supérieure à 0,5. Sinon, l'adversaire est aveugle.
- **Contrôle négatif** : un hôte leurre, dont le $D_{\mathrm{test}}$ est inconnu de l'adversaire.
- **Falsification** :
  - un écart significatif falsifie l'idée que « la seule fuite est le bit d'annulation » ;
  - l'égalité, avec un contrôle positif qui détecte, falsifie H_A pour cette surface.

**X3′b : canal temporel.** Dispositif : admission au coût pire cas calculé à partir de la requête, sans cache pour $\mathcal{O}$, `generate` à longueur maximale fixe.

- **H_A** : l'information mutuelle entre (appartenance ou état de cache) et (rang de lot, durée observée, y compris celle mesurée par un compteur local sous E1, cf. C·év-2 et C contre A) est strictement positive.
- **H_B** : elle est nulle dans l'intervalle de confiance.
- **Contrôle positif** : un hôte avec cache partagé et arrêt au jeton de fin doit fuir.
- **Falsification** : chaque issue falsifie l'autre hypothèse, sous réserve que le contrôle positif ait détecté.

**X3′c : seuil d'annulation viable.** Les valeurs $s$ et $q$ sont fixées par Lazar **avant** l'expérience (illustratif : $s=0{,}95$).

- **H_A** : il existe un seuil $\tau$ tel que (i) la survie des exécutions honnêtes rejouées est au moins $s$, et (ii) le quota d'items contaminants qu'un adversaire glisse sous $\tau$ reste au plus $q$.
- **H_B** : aucun $\tau$ ne satisfait les deux conditions.
- **Falsification** : une issue H_B rend F-différé′ non viable. Il faut alors des jeux de test remplacés, ou une interface E2 sans texte libre.

### X4′ : concept ou artefact de surface ?

- **Stimuli d'évaluation** : ils sont produits par un générateur indépendant (une autre famille de modèles, ou un humain), à partir de la seule description du concept. $\mathcal{O}$ ne fournit que la sonde.
- **Tâche de contrôle au niveau du texte** (A·B-10) :
  - les textes sont regroupés en grappes selon leur **signature de surface** : tranche de longueur, profil de ponctuation, $n$-grammes positionnels ;
  - chaque grappe reçoit une étiquette tirée au hasard ;
  - une sonde qui encode la surface réussit cette tâche, ce qui **abaisse** sa sélectivité.
- **Sondes de référence** :
  - régression linéaire sur traits de surface explicites, y compris les positions de jetons (C·ctl-3, C·év-4) ;
  - sac de mots ;
  - poids aléatoires, gardés comme plancher faible.
- **Hypothèses** :
  - **H_A** : la sélectivité dépasse 0,10 (illustratif) **et** la sonde bat la référence de surface, avec un intervalle de confiance qui exclut 0 ;
  - **H_B** : la référence de surface égale la sonde.
- **Falsification** : chaque issue falsifie l'autre hypothèse.

### X5′ : préenregistrement, plan 2×2 (A·B-8)

- **Facteurs** : critère {interne, gabarit externe} × réservoir {non scellé, scellé avec réplication sur B′}.
- **Nulles plantées** de deux types :
  - (i) étiquettes indépendantes du texte ;
  - (ii) **nulles de surface** : étiquettes corrélées à un trait de surface sans lien avec le concept déclaré.
- **Hypothèses vraies plantées** : elles mesurent la puissance (seuil de 80 %, illustratif).
- **Gabarit** : $m$ engagements au plus par exécution, avec correction de Holm.
- **Métrique** : taux de confirmation sur les nulles, avec intervalle de Clopper-Pearson comparé à $\alpha=0{,}05$.
- **Lectures exclusives** :
  - un effet réservoir significatif avec un effet critère nul falsifie l'utilité du gabarit, à réservoir scellé. C'est la prédiction de A ;
  - un effet critère significatif à réservoir scellé falsifie la thèse « le scellement suffit » ;
  - des fausses confirmations sur les nulles de surface malgré B scellé, qui disparaissent avec B′, falsifient la suffisance du seul scellement contre le piégeage.

### X6′ : départager (E1), (E2) et le bras hors boucle (A·B-9, C·1, C·6)

**Mondes nuls sentinelles.** Une fraction des exécutions (25 %, illustratif) porte sur des tâches dont la cible est, par construction, indépendante des textes, sans que $\mathcal{O}$ le sache. Leur indistinguabilité est vérifiée par un pré-test du type de celui de X2′. Toute confirmation dans un monde nul est une fausse confirmation, ce qui donne la vérité terrain qui manquait en génération ouverte.

**Métriques.**
- $S_{\mathrm{frais}}$ ;
- la fraction des questions d'une **banque fixée par Lazar** qui sont résolues, avec réplication sur B′ ;
- le taux de confirmation dans les mondes nuls.

Il n'y a pas de comptage libre. Le coût humain est rapporté sur une plage de taux de conversion.

**Duel 6a.**
- **H_A** : (E2) résout plus de questions par unité de coût que (E1) avec substitut.
- **H_B** : (E1) fait autant ou mieux.
- **Mesure annexe** : le taux de réplication sur le modèle de 8 milliards des hypothèses issues du substitut. La réplication est exécutée par l'hôte, hors de portée de $\mathcal{O}$. Cette mesure remplace le contrôle vide.
- **Falsification** : chaque issue falsifie l'autre hypothèse.

**Duel 6b.** (E2) contre le bras hors boucle. Il n'est jugé qu'après X3′ et X5′.

### Ordre

**F1–F3 → X0 → X3′ → X5′ → X4′ → X1′ → X2′ → X6′.**

### Thèses de B révisées et ce qui les réfute

1. **« Le levier, ce sont les bits qui dépendent de $D_{\mathrm{val}}$. »** Réfutée par une interaction $k\times b$ nulle dans X1′, ou par un rejet de $H_W$ dans X0.
2. **« F-immédiat fuit. »** Ce n'est plus une thèse empirique : c'est une déduction. Elle est remplacée par « F-différé′ ne fuit pas plus que le bit d'annulation », réfutée par X3′a.
3. **« (E1) ne lève pas la limite. »** Réfutée par le duel 6a.
4. **« L'arbitre est un canal. »** Tranché par F3.
5. **« Un seuil d'annulation viable existe. »** Réfutée par X3′c.

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi, au sens RAPPORTÉ par la littérature, non audité ici.**

- Un analyste adaptatif surapprend un jeu interrogé de façon répétée.
- La confidentialité différentielle des réponses implique la généralisation (Dwork et al. 2015 ; Bassily et al. 2016).
- Le Ladder protège le classement des meilleurs scores (Blum & Hardt 2015).
- Aucun mécanisme efficace ne répond correctement à beaucoup plus d'environ $n^2$ requêtes adaptatives (Hardt & Ullman 2014 ; Steinke & Ullman 2015). Tout dessin a donc un budget fini.
- Le biais est borné par l'information mutuelle entre transcription et données (Russo & Zou 2016).

**Déductions sous le cadre RAPPORTÉ (statut HYPOTHÈSE, mais sans besoin d'expérience).**

- Un filtre anti-copie qui refuse immédiatement est un oracle d'appartenance.
- Des probabilités rendues item par item sur $D_{\mathrm{val}}$ échappent à Thresholdout et au Ladder.
- Les quatre garanties P1–P4 ne protègent pas $D_{\mathrm{val}}$.

**Ce qui n'est pas établi.**

- **$H_W$** : l'absence de mémorisation de $D_{\mathrm{val}}$ et $D_{\mathrm{test}}$ par les modèles. Toute la comptabilité d'information de (E2) en dépend (§b.1).
- **Trois faits non dits** : la localisation de $D_{\mathrm{val}}$ (F1), la séparation de l'hôte de test (F2) et l'unicité de l'évaluation sur $D_{\mathrm{test}}$ (F3).
- La taille réelle du surapprentissage (X1′).
- Le fait que le contenu des réponses de E2, et non le budget, cause un gain (X2′).
- L'existence d'un seuil d'annulation qui ne tue pas les exécutions honnêtes (X3′c).
- Le fait qu'une confirmation sur réservoir scellé mesure le concept déclaré plutôt qu'un artefact du générateur (X4′, X5′).
- Le transfert d'un substitut sur processeur vers le modèle de 8 milliards, qui seul permettrait à (E1) de lever la limite (duel 6a).

**Valeur et coût, résumés.**

- (E2) seule permet les expériences sur le modèle de 8 milliards : stimuli construits, sondes, réponses à des textes de $\mathcal{O}$. Son coût en calcul est de l'ordre de quelques heures de carte graphique par expérience (illustratif, d'après le §d de III.1).
- (E1) n'apporte que du calcul local, plus un canal temporel local (X3′b). Sa valeur dépend du transfert.
- Le bras hors boucle coûte surtout du temps humain, que Lazar doit chiffrer.
- Les trois voies sont départagées par X6′ : questions résolues par unité de coût, avec réplication sur B′, et taux de fausses confirmations mesuré dans des mondes nuls. X6′ n'est interprétable qu'après X3′ et X5′.

**Ce qu'il faut faire en premier.**

1. Déclarer **F1–F3**. Cela ne coûte rien et ferme des canaux sans expérience.
2. Mener **X0**, le test de mémorisation hors de la boucle, avec un contrôle positif sur modèle à corpus ouvert.

Pourquoi X0 en premier :
- elle est **bon marché** (illustratif : quelques heures de carte graphique au plus) ;
- elle **ne requiert ni E1 ni E2** ;
- **ses deux issues changent le dessin** :
  - si $H_W$ tombe, `generate` doit être filtré en sortie, la borne doit compter tous les bits, et les jeux doivent être remplacés ;
  - si $H_W$ tient à la sensibilité mesurée, le registre $L_{\mathrm{ind}}$ est légitime, et X3′ puis X5′ peuvent commencer.

Une issue non concluante (contrôle positif aveugle) n'autorise **aucune** des deux suites.

FIN-DE-CELLULE