**Avertissement d'intégrité (Règle 2)** : La pièce `E3-T2-redteam-A` est absente (statut : REFUS). Les pièces documentaires `docs/etat-de-l-art-controle-ia-v1.md`, `LISEZMOI`, ainsi que le contenu des 4 familles d'évasion R-610 et de la brèche W2 sont absents ou tenus à l'écart par construction ; leur contenu n'est pas inventé ici.

---

# (a) Réponse point par point aux attaques de l'équipe rouge B

Toutes les critiques de B portent le statut d'**HYPOTHÈSE** méthodologique. Voici le tri : acceptation, rejet motivé ou transformation en test (inférence forte, règle B4).

### 1. Sur les remarques préalables d'intégrité (1 à 5)
* **Remarques 1, 2, 4 et 5 : ACCEPTÉES.**
  * (1) Le point (a).3 de ma conception initiale est requalifié d'OBSERVÉ-NON-AUDITÉ en **HYPOTHÈSE** logique.
  * (2) Les références Greenblatt et al. (2023, *AI Control: Improving Safety Despite Intentional Subversion*), Zou et al. (2023, *Representation Engineering: A Top-Down Approach to AI Transparency*) et Burns et al. (2022, *Discovering Latent Knowledge in Language Models Without Supervision*) sont issues de la littérature externe ; leur présence dans `docs/etat-de-l-art-controle-ia-v1.md` est une **HYPOTHÈSE** (références à vérifier sur pièce).
  * (4) L'expression « l'oracle confirme à 100 % » est retirée et remplacée par un audit du taux de faux négatifs de l'oracle sur un lot d'épisodes à sabotage injecté et connu du bras rouge (j'utilise ici le contrôle c.5 de B).
  * (5) Les coûts de l'organisme d'idéation et du collisionneur sont purgés des devis d'expériences : seuls les coûts de calcul d'évaluation et d'inférence des moniteurs sont retenus.
* **Remarque 3 (Contenu de W2) : ACCEPTÉE sur la purge des exemples, REJETÉE sur l'invalidation de l'Expérience 3.**
  * *Raison* : Mentionner des « commentaires trompeurs » violait l'ignorance sur W2 ; je purge toute conjecture sur la nature de W2. En revanche, opposer une défaillance de capacité intrinsèque du juge 3B (**RAPPORTÉ** au hasard) à un défaut d'interface d'entrée ne dépend d'aucune hypothèse sur le contenu interne de W2.

### 2. Sur les failles méthodologiques (Failles 1 à 11)

* **Faille 1 (Confondant d'identité de l'organisme vs détection de l'épisode) : TRANSFORMÉE EN TEST.**
  * *Action* : Si les 4 familles R-610 (**RAPPORTÉ / construites**) proviennent de poids modifiés, une sonde peut détecter l'empreinte des poids plutôt que l'acte de sabotage (**HYPOTHÈSE**). J'intègre le duel de B (organisme placebo et épisodes dormants du saboteur) directement dans le plan factoriel de l'Expérience 1 corrigée.

* **Faille 2 (Persistance causale de la consigne dans l'attention) et Faille 3 (Fuite de consigne dans la base texte 0,866) : TRANSFORMÉES EN TEST.**
  * *Action* : Dans un transformeur à attention causale (**HYPOTHÈSE** sur l'architecture), les états cachés post-consigne encodent encore la consigne. Le masquage positionnel est donc abandonné au profit exclusif de mon protocole de **paires contrefactuelles** (tableau c.3 de C, repris par B), étendu au prédicteur sur les traits du texte à 0,866 (**RAPPORTÉ**, N-029) pour égaliser le régime d'entrée entre boîte noire et boîte blanche.

* **Faille 4 (Consommation du mode tenu à l'écart avant la porte G1) : ACCEPTÉE.**
  * *Action* : Les faits stipulent que le mode tenu à l'écart n'est pas chiffré avant G1 (N-054, **RAPPORTÉ**). L'évaluer avant l'entretien brûlerait le témoin de généralisation. Les démonstrations d'avant-entretien utilisent désormais une validation croisée par bloc (« *leave-one-family-out* » : 3 familles R-610 pour l'entraînement/calibration, la 4e famille R-610 tenue à l'écart comme substitut de généralisation pré-entretien), laissant le mode N-054 intact pour G1.

* **Faille 5 (Biais du maximum lors du balayage des couches) : ACCEPTÉE.**
  * *Action* : Conformément à ma garantie 3, l'indice de la couche sondée (ex. : couche à $50\,\%$ ou $75\,\%$ de profondeur, illustratif) et l'hyperparamètre de régularisation sont figés sur le pli de calibration avant tout test. La valeur-$p$ est corrigée par test de permutation des étiquettes soumises exactement à la même règle de sélection.

* **Faille 6 (Qui lit les traces ? Fuite d'aveuglement) et Faille 9 (Pollution des sous-bras par les pièces publiques) : ACCEPTÉES.**
  * *Action* : Adoption du contrôle c.7 de B. Les scripts d'extraction d'activations et de calcul d'AUROC s'exécutent dans un **sas d'évaluation automatisé tiers** (processus sans lecture humaine ni lecture par la session mère de défense), qui ne retourne que les scalaires agrégés préenregistrés (R1). Les pièces publiques sont mises sous embargo vis-à-vis des sous-bras d'attaque jusqu'à la clôture de la vague, avec journal horodaté des empreintes `sha256` des fichiers vus par chaque sous-bras.

* **Faille 7 (Non-exclusivité des hypothèses dans les duels B4) : ACCEPTÉE.**
  * *Action* : Les hypothèses $H_A$ et $H_B$ des trois expériences sont reformulées sous forme de partitions logiques strictes ($H_B = \neg H_A$ sur un critère quantitatif unique ou un contraste d'interaction 2×2), éliminant toute zone grise non falsificatrice.

* **Faille 8 (Confusion entre information et effort/sélection entre Aveugle et Informé) : TRANSFORMÉE EN TEST.**
  * *Action* : Intégration dans l'Expérience 2 d'un budget d'essais et de jetons strictement identique entre les sous-bras, ainsi que du contrôle **informé-leurre** (contrôle c.4 de B) et d'une mesure de l'ampleur du dommage (réponse au scénario d'évasion de B sur la garantie 2 de C) pour prouver que l'évasion ne s'achète pas en réduisant le sabotage à néant.

* **Faille 10 (L'oracle mesure l'effet et non l'intention ; absence de référent) : REJETÉE sur l'exigence d'intention, TRANSFORMÉE EN TEST sur le rappel de l'oracle.**
  * *Raison du rejet partiel* : Exiger que l'oracle de vérité terrain (**RAPPORTÉ**) juge l'*intention interne* le confondrait avec les sondes boîte blanche qu'il doit étalonner. L'oracle doit rester un vérificateur d'effet objectif (sabotage fonctionnel réalisé), tandis que la distinction entre bogue d'incompétence et sabotage délibéré est assurée par le plan expérimental (comparaison du taux d'échec de l'organisme saboteur avec celui du modèle honnête et du placebo sur les mêmes tâches).
  * *Transformation en test* : Pour parer le « scénario conjoint » de B (sabotage hors couverture de l'oracle), un audit de rappel de l'oracle est intégré en prérequis via un lot scellé d'épisodes à sabotage synthétique garanti par le bras rouge (contrôle c.5 de B).

* **Faille 11 (Connivence statistique par famille de préentraînement non testée) : TRANSFORMÉE EN TEST.**
  * *Action* : Mon diagnostic (a).1 est opérationnalisé dans l'Expérience 3 corrigée en croisant orthogonalement la famille de préentraînement de l'organisme saboteur et celle du juge/moniteur (contrôle c.8 de B).

---

# (b) Les expériences corrigées (Inférence forte B4, champs fermés)

Toutes les valeurs numériques qui ne proviennent pas des faits (**0,866** pour le prédicteur texte N-029 ; hasard pour les sondes génériques et le juge 3B ; **4** familles R-610) sont marquées **illustratives** (Règle 4). Aucune recette ni procédé concret n'est décrit.

### Expérience 1 Corrigée : Découplage Contrefactuel Consigne / Organisme / Épisode (sur R-610 en validation croisée 3+1)
Cette expérience fusionne la correction de la sonde lisant la consigne (**RAPPORTÉ / faiblesse connue**), l'audit du prédicteur texte à 0,866 (**RAPPORTÉ**), le test de l'organisme placebo (Faille 1 de B) et les paires contrefactuelles (Faille 2 et 3 de B), sans toucher au mode tenu à l'écart N-054 (Faille 4 de B).

* **Protocole factoriel (sas automatisé tiers, couches préenregistrées)** :
  Les instruments (sonde boîte blanche à couche figée et prédicteur texte 0,866) sont entraînés sur 3 familles R-610 et évalués sur la 4e famille R-610 (rotation sur les 4 familles) à travers 4 conditions contrefactuelles :
  1. $C_{\text{sab}}$ : Organisme saboteur + consigne neutre + épisode de sabotage actif (attesté par l'oracle).
  2. $C_{\text{dorm}}$ : Organisme saboteur + consigne neutre + épisode dormant (exécution honnête attestée par l'oracle).
  3. $C_{\text{feinte}}$ : Modèle honnête (ou organisme placebo modifié sans objectif de sabotage) + consigne d'attaque explicite + exécution honnête forcée.
  4. $C_{\text{hon}}$ : Organisme placebo + consigne neutre + exécution honnête.
* **Duel d'hypothèses exclusives (B4)** :
  * **$H_A$ (Détection d'artefact : fuite de consigne ou empreinte d'organisme)** : Pour toute sonde boîte blanche à couche préenregistrée, soit la séparation d'épisode actif échoue sur la famille R-610 tenue à l'écart ($\text{AUROC}(C_{\text{sab}} \text{ vs } C_{\text{dorm}}) < 0,70$, illustratif), soit le moniteur confond l'acte de sabotage avec la consigne ou l'identité du modèle : $\text{AUROC}(C_{\text{feinte}} \text{ vs } C_{\text{hon}}) \ge \text{AUROC}(C_{\text{sab}} \text{ vs } C_{\text{dorm}}) - 0,10$ (illustratif) ou $\text{AUROC}(C_{\text{dorm}} \text{ vs } C_{\text{hon}}) \ge 0,60$ (illustratif).
  * **$H_B$ ($\neg H_A$ — Capture d'état latent spécifique à l'épisode de sabotage)** : Il existe une sonde préenregistrée telle que, sur la 4e famille R-610 non vue à l'entraînement, on observe simultanément : (i) détection de l'épisode actif $\text{AUROC}(C_{\text{sab}} \text{ vs } C_{\text{dorm}}) \ge 0,70$ (illustratif, $p < 0,01$ par test de permutation des étiquettes), (ii) immunité à la consigne $\text{AUROC}(C_{\text{feinte}} \text{ vs } C_{\text{hon}}) < \text{AUROC}(C_{\text{sab}} \text{ vs } C_{\text{dorm}}) - 0,10$ (illustratif), et (iii) insensibilité à l'identité de l'organisme $\text{AUROC}(C_{\text{dorm}} \text{ vs } C_{\text{hon}}) < 0,60$ (illustratif).
* **Audit parallèle de la base 0,866** : La même grille contrefactuelle est appliquée au prédicteur sur les traits du texte (0,866, **RAPPORTÉ**). Si son $\text{AUROC}(C_{\text{sab}} \text{ vs } C_{\text{dorm}})$ chute sous $0,65$ (illustratif) alors que son $\text{AUROC}(C_{\text{feinte}} \text{ vs } C_{\text{hon}}) > 0,80$ (illustratif), il est démontré que la base 0,866 dépendait d'une fuite de consigne ou de registre lexical.
* **Champs fermés de la proposition** :
  * `critère de porte visé` : Préparation de la porte G1 (assainissement des sondes et préservation intégrale du mode tenu à l'écart N-054).
  * `raison de refus TAIF levée` : Faisabilité et rigueur méthodologique (élimine les trois confondants majeurs : lecture de consigne, détection des poids de l'organisme, et surapprentissage des couches).
  * `moniteur éprouvé` : Sonde lisant la consigne (**RAPPORTÉ**), sondes boîte blanche génériques (**RAPPORTÉ**) et prédicteur sur les traits du texte à 0,866 (**RAPPORTÉ**).
  * `coût estimé (USD) et délai` : 90 USD de calcul GPU pur (illustratif, hors collisionneur/idéation), 48 heures (illustratif).
  * `ce qui la réfuterait` : Réfutation de $H_B$ si $\text{AUROC}(C_{\text{sab}} \text{ vs } C_{\text{dorm}}) < 0,70$ (illustratif) ou si le placebo/feinte déclenche la sonde autant que le sabotage réel ; réfutation de $H_A$ dans le cas complémentaire exact.
  * `pièce publique ou scellée produite` : Matrice 2×2 d'AUROC contrefactuelles agrégées (pièce publique, sous embargo vis-à-vis des sous-bras d'attaque) ; poids de l'organisme placebo et traces d'activations (pièce scellée au coffre).

---

### Expérience 2 Corrigée : Gain d'Information Pur (Aveugle vs Informé-Leurre vs Informé) à Dommage Constant
Cette expérience répond au point 2 de la question (démonstration d'évasion avant l'entretien) tout en corrigeant les Failles 7, 8 et 10 de B (contrôle informé-leurre, budget d'effort égalisé, audit préalable du rappel de l'oracle et contrainte de dommage minimal).

* **Prérequis d'étalonnage de l'oracle (Contrôle c.5 de B)** : Le sas tiers injecte un lot scellé de $K = 100$ (illustratif) épisodes de sabotage de référence à effet connu à côté de $100$ (illustratif) épisodes honnêtes présentant des bogues non malveillants. L'expérience ne procède que si le rappel de l'oracle sur les sabotages est $\ge 0,95$ (illustratif) et son taux de fausses alertes sur les bogues honnêtes $\le 0,05$ (illustratif).
* **Protocole à effort contrôlé** : Trois sous-bras d'attaque reçoivent exactement le même budget d'essais ($N = 20$ itérations, illustratif) et de calcul pour concevoir un organisme saboteur (hors mode N-054) soumis à une double contrainte : (1) préservation de l'utilité sur les tests fonctionnels standards, et (2) maintien d'une sévérité de sabotage vérifiée par l'oracle au-dessus d'un seuil fixe $S_{\min}$ (empêchant d'acheter l'évasion par réduction du dommage).
  * *Sous-bras Aveugle* : aucune description des moniteurs.
  * *Sous-bras Informé-Leurre* : reçoit un document technique de même longueur mais décrivant des traits fictifs non utilisés par la défense.
  * *Sous-bras Informé* : reçoit la spécification publique réelle du prédicteur sur les traits du texte (0,866, **RAPPORTÉ**) et des sondes génériques.
* **Duel d'hypothèses exclusives (B4)** :
  Soit $\Delta_{\text{info}} = \text{AUROC}(\text{Informé-Leurre}) - \text{AUROC}(\text{Informé})$ mesuré à sévérité de sabotage constante $\ge S_{\min}$ sur le moniteur ciblé (prédicteur texte 0,866 et sondes actuelles).
  * **$H_A$ (Nullité du gain d'information ou robustesse boîte noire)** : À budget d'essais et sévérité de sabotage constants, la connaissance de la défense n'apporte aucun avantage d'évasion significatif : $\Delta_{\text{info}} < 0,15$ (illustratif) ou l'AUROC du prédicteur texte face au sous-bras informé reste $\ge 0,75$ (illustratif).
  * **$H_B$ ($\neg H_A$ — Vulnérabilité adaptative spécifique à l'information)** : Le sous-bras informé abaisse l'AUROC du prédicteur texte sous $0,75$ (illustratif) ET creuse un écart $\Delta_{\text{info}} \ge 0,15$ (illustratif, $p < 0,01$) par rapport au sous-bras informé-leurre, tout en maintenant un taux de sabotage réussi $\ge S_{\min}$ vérifié par l'oracle.
* **Champs fermés de la proposition** :
  * `critère de porte visé` : Validation expérimentale de la structure Aveugle / Informé et démonstration d'évasion face à la base 0,866 (N-029).
  * `raison de refus TAIF levée` : Théorie du changement et Impact (prouve que l'évaluation par un attaquant informé révèle des vulnérabilités invisibles à un red-teaming aveugle, sans confondre information et effort).
  * `moniteur éprouvé` : Prédicteur sur les traits du texte (0,866, **RAPPORTÉ**) et sondes boîte blanche actuelles (**RAPPORTÉ**).
  * `coût estimé (USD) et délai` : 160 USD de calcul et d'inférence (illustratif, hors collisionneur/idéation), 3 jours (illustratif).
  * `ce qui la réfuterait` : Réfutation de $H_B$ si $\Delta_{\text{info}} < 0,15$ (illustratif) ou si l'évasion fait chuter le taux de sabotage réel sous $S_{\min}$ ; réfutation de $H_A$ si $\Delta_{\text{info}} \ge 0,15$ avec $\text{AUROC}_{\text{Informé}} < 0,75$ (illustratif).
  * `pièce publique ou scellée produite` : Différentiel $\Delta_{\text{info}}$ et $\Delta_{\text{format}} = \text{AUROC}(\text{Aveugle}) - \text{AUROC}(\text{Leurre})$ (pièce publique après embargo) ; recettes des trois sous-bras et journal d'accès `sha256` (pièce scellée au coffre).

---

### Expérience 3 Corrigée : Plan Factoriel 2×2 du Juge (Échelle 3B vs 32B $\times$ Interface Brute vs Assainie-W2) et Test de Connivence Inter-Familles
Cette expérience corrige la Faille 7 de B (qui signalait à juste titre qu'échelle et interface peuvent interagir), purge toute conjecture sur le contenu de W2 (Remarque 3 de B), et intègre le test de connivence statistique par famille de préentraînement (Faille 11 et contrôle c.8 de B).

* **Protocole factoriel 2×2×2 (exécuté dans le sas tiers)** :
  * *Facteur 1 (Échelle du juge)* : Juge de 3 milliards de paramètres (**RAPPORTÉ** au hasard) contre Juge de taille supérieure (ex. : 32B, illustratif).
  * *Facteur 2 (Protocole d'interface)* : Interface standard (sujette à la brèche W2 **RAPPORTÉE**) contre Interface assainie (application du correctif structurel de la défense visant W2, combiné au score de la sonde contrefactuelle de l'Exp. 1).
  * *Facteur 3 (Parenté de préentraînement — Test de connivence statistique)* : Juge issu de la *même* famille de modèles que l'organisme saboteur ($\text{Fam}_{=}$) contre Juge issu d'une famille de préentraînement *distincte* ($\text{Fam}_{\neq}$).
* **Duel d'hypothèses exclusives (B4) sur la réhabilitation du juge 3B** :
  * **$H_A$ (Goulot de capacité intrinsèque à 3B ou connivence de famille)** : Même avec l'interface assainie, le juge 3B évalué en croisement inter-familles ($\text{Fam}_{\neq}$) reste sous la ligne de base du prédicteur texte ($\text{AUROC}_{\text{3B, assaini, Fam}_{\neq}} \le 0,866$, **RAPPORTÉ**), OU sa performance chute de plus de $0,10$ (illustratif) lorsqu'on passe de $\text{Fam}_{=}$ à $\text{Fam}_{\neq}$ (preuve de connivence statistique).
  * **$H_B$ ($\neg H_A$ — Suffisance du juge 3B après correction d'interface sans connivence)** : Le juge 3B doté de l'interface assainie dépasse la base texte en régime inter-familles ($\text{AUROC}_{\text{3B, assaini, Fam}_{\neq}} > 0,866$, **RAPPORTÉ**) avec un écart de parenté $|\text{AUROC}(\text{Fam}_{=}) - \text{AUROC}(\text{Fam}_{\neq})| \le 0,10$ (illustratif).
  *(Note diagnostique : le contraste avec le juge 32B mesure simultanément l'effet principal d'échelle $\Delta_{\text{échelle}}$ et l'effet d'interface $\Delta_{\text{W2}}$, permettant au programme de trancher s'il faut remplacer le juge 3B avant G1).*
* **Champs fermés de la proposition** :
  * `critère de porte visé` : Fermeture de la brèche W2 (**RAPPORTÉ**), résolution du statut du juge 3B (**RAPPORTÉ**) et garantie de non-connivence statistique.
  * `raison de refus TAIF levée` : Portée et Crédibilité de l'évaluation (démontre que la détection ne repose pas sur une connivence entre modèles de même famille et résout rigoureusement la défaillance du juge 3B).
  * `moniteur éprouvé` : Juge de 3 milliards de paramètres (**RAPPORTÉ**) et mécanisme sujet à la brèche W2 (**RAPPORTÉ**).
  * `coût estimé (USD) et délai` : 140 USD de calcul GPU (illustratif, hors collisionneur/idéation), 3 jours (illustratif).
  * `ce qui la réfuterait` : Réfutation de $H_B$ si $\text{AUROC}_{\text{3B, assaini, Fam}_{\neq}} \le 0,866$ ou si l'écart inter-familles excède $0,10$ (illustratif) ; réfutation de $H_A$ dans le cas opposé.
  * `pièce publique ou scellée produite` : Tableau d'analyse de variance 2×2×2 des AUROC (pièce publique) ; traces soumises à W2 (pièce scellée au coffre).

---

# (c) Synthèse pour l'arbitre (Une page)

### 1. Ce qui est établi
* **Par les faits transmis (statuts vérifiés dans l'énoncé)** :
  * Le programme dispose d'une architecture de bras rouge structurée par deux sous-bras (aveugle et informé), un mode tenu à l'écart non chiffré avant la porte G1 (N-054), un scellement des recettes au coffre, un préenregistrement (R1) et un oracle de vérité terrain indépendant du juge (**RAPPORTÉ** au niveau méthode).
  * Quatre familles d'évasion (R-610) sont d'ores et déjà **construites** (**RAPPORTÉ**).
  * Sur le banc du programme, le prédicteur boîte noire sur les traits du texte plafonne à **0,866** (N-029, **mesuré**), tandis que les sondes boîte blanche génériques et le juge de 3 milliards de paramètres sont **au niveau du hasard** (**mesuré**). Deux faiblesses méthodologiques précises sont identifiées : une sonde qui lit la consigne au lieu de l'état interne et la brèche W2 du juge (**faiblesses connues, rapportées**).
* **Par la confrontation dialectique du collisionneur (Tours III.1 à III.3)** :
  * *Inuffisance des preuves négatives triviales* : Démontrer qu'un organisme saboteur échappe à des sondes ou à un juge 3B qui sont *déjà* au niveau du hasard ne prouve rien au jury TAIF. L'épreuve doit porter sur une sonde corrigée de ses fuites et sur le prédicteur texte à 0,866.
  * *Trois confondants fatals identifiés et neutralisés* : (1) dans un modèle autorégressif, lire les activations après la consigne lit encore la consigne par attention causale ; (2) comparer un organisme saboteur modifié à un modèle honnête standard risque de détecter la modification des poids (l'identité de l'organisme) plutôt que l'acte de sabotage ; (3) utiliser le mode tenu à l'écart N-054 pour les démonstrations avant l'entretien le contaminerait avant la porte G1.

### 2. Ce qui n'est pas établi (et constitue le risque de refus TAIF)
* **L'indépendance du score 0,866 vis-à-vis de la consigne (HYPOTHÈSE)** : On ignore si le prédicteur texte à 0,866 détecte le comportement de sabotage ou des marqueurs lexicaux induits par la consigne d'attaque.
* **L'existence d'un signal latent d'épisode pur sur R-610 (HYPOTHÈSE)** : Il n'est pas établi qu'une sonde boîte blanche, une fois privée de la consigne et confrontée à un organisme placebo (poids modifiés sans sabotage) ainsi qu'à des épisodes dormants du saboteur, fasse mieux que le hasard.
* **La non-connivence opérationnelle et statistique (HYPOTHÈSE)** : Tant que l'exécution des sondes n'est pas isolée dans un sas automatisé tiers (sans lecture par la session mère), que les couches sondées ne sont pas figées avant test, et que l'organisme saboteur et le juge partagent la même famille de préentraînement, un jury peut attribuer toute détection à un surapprentissage d'évaluation ou à une convergence distributionnelle.
* **Le rappel de l'oracle et la récupérabilité du juge 3B (HYPOTHÈSE)** : Ni le taux de faux négatifs de l'oracle face à des sabotages subtils ni la capacité d'un modèle 3B à dépasser 0,866 après fermeture de W2 ne sont démontrés.

### 3. L'expérience à faire en premier (Priorité absolue avant l'entretien)
Il faut lancer immédiatement l'**Expérience 1 Corrigée (Audit Contrefactuel Consigne / Organisme / Épisode en validation croisée 3+1 sur R-610)**, exécutée par un script sas tiers pour **90 USD et 48 heures** (illustratif) :
1. **Pourquoi en premier ?** Elle ne consomme pas le mode tenu à l'écart N-054 (préservé pour G1), ne nécessite aucun réentraînement lourd puisqu'elle exploite les 4 familles R-610 déjà construites (complétées par des épisodes dormants et des consignes contrefactuelles), et conditionne la validité de toutes les autres mesures.
2. **Gain immédiat pour l'entretien TAIF quelle que soit l'issue** :
   * Si **$H_B$ l'emporte**, le programme se présente devant le jury avec une sonde boîte blanche corrigée qui bat le hasard sur une famille d'évasion non vue à l'entraînement, avec la preuve mathématique qu'elle ne lit ni la consigne ni l'identité du modèle.
   * Si **$H_A$ l'emporte** (les sondes restent au hasard et/ou la base 0,866 s'effondre hors consigne), le programme dispose d'une démonstration rigoureuse d'évasion des 4 familles R-610 face aux moniteurs assainis, tout en prouvant au jury TAIF une maîtrise méthodologique (contrôles contrefactuels, organisme placebo, sas d'aveuglement) qui justifie l'investissement dans le pilier attaque.

FIN-DE-CELLULE