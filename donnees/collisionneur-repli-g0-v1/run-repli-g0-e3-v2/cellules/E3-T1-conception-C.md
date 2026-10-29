# Proposition C — Conception de la règle de repli scellable pour la porte G0 (Tour III.1)

**Note sur l'intégrité des pièces (Règle 2)** : Les extraits de la Pièce B (finissant par « il est fini ») et de la Pièce C (commençant au milieu d'une phrase par « dans sa forme confirmée » et comportant un saut à la ligne « d'octobre, section 8 ») sont visiblement coupés. Je n'invente aucun contenu manquant. Conformément à la Règle 6, la structure des livrables suit strictement la consigne système `(a), (b), (c), (d)`, tout en traitant exhaustivement les 6 points analytiques de l'objet d'étude (la Question de l'arbitre) sans exécuter ses instructions de formatage dérogatoires.

---

## (a) Ce que la question suppose sans que ce soit établi

Chaque présupposé implicite de la question et des pièces est isolé ci-dessous avec son statut strict (Règle 1) :

1. **Début du financement au 1er décembre 2026** : La question énonce qu'un financement externe, s'il est accordé, commence le 1er décembre. Or, la Pièce C est coupée et ne contient pas la date du 1er décembre ; la Pièce A bis mentionne seulement que l'appel EA Funds du 21 octobre a été décalé. Statut : **RAPPORTÉ** (par le texte de la question) / **HYPOTHÈSE** (quant à l'octroi effectif et la date d'effet).
2. **Faisabilité d'un organisme logiciel à dose-réponse diffuse (Critère 2)** : Le programme suppose que Llama-3.1-8B-Instruct peut être réglé (par consigne système ou adaptateur de bas rang) pour produire un taux de sabotage continu et contrôlable (« dose-réponse ») sans détruire la validité de la tâche. Or, la Pièce B indique qu'aucun organisme saboté n'existe au 29 octobre et que « absence de dose diffuse avec dommage = arrêt de la banque (R-680) ». Statut : **HYPOTHÈSE**.
3. **Séparabilité linéaire au-dessus du plancher aléatoire sur (i) et (ii) (Critère 3)** : Le programme suppose que les sondes linéaires v0 battront un plancher aléatoire apparié tant sur l'organisme par consigne (i) que par réglage fin léger (ii). Statut : **HYPOTHÈSE**.
4. **Stabilité des juges et scores finis (Menace sur Critères 2, 4 et G1)** : La Pièce B rapporte que sur 180 notations rejouées, aucune cellule n'atteint 0,99 de scores finis (pièce 29-2, R-671). Que la cellule redéfinie tienne avant le 30 novembre ou le 31 janvier est non établi. Statut : **OBSERVÉ-NON-AUDITÉ** (pour l'échec sur 180 notations, la pièce 29-2 n'étant pas jointe) / **HYPOTHÈSE** (pour la tenue de la cellule redéfinie).
5. **Couverture budgétaire de la phase de transition (1er nov. – 30 nov. / 31 janv.)** : La Pièce A bis indique que l'autorisation de calcul de la phase 0 (`GO-2026-10-04-08`) échoit le 1er novembre 2026, et la Pièce B note que la banque complète coûte 300 à 1 400 USD contre 90 USD accordés. La question suppose que le programme dispose des ressources de calcul pour opérer jusqu'au 30 novembre, puis jusqu'au 31 janvier. Statut : **HYPOTHÈSE**.
6. **Indépendance et déterminisme du sous-agent évaluateur (R13)** : La question suppose qu'un sous-agent neuf peut prononcer un verdict sans ambiguïté (« tenu / non tenu / non concluant ») à partir des preuves scellées. Sans grammaire formelle de vérification des preuves, deux sous-agents neufs pourraient diverger sur un cas limite. Statut : **HYPOTHÈSE**.

---

## (b) Expériences décisives (Inférence forte : $H_A$ contre $H_B$)

Pour trancher la validité de la règle de repli et des critères ouverts sans laisser de décision après lecture, voici les expériences décisives opposant deux hypothèses exclusives (Règle B4) :

### Expérience 1 : Audit à blanc du protocole de verdict R13 (sur la gouvernance de G0)
* **Objectif** : Trancher si la table de décision de la règle de repli (voir section `(d).1`) élimine toute interprétation subjective par le sous-agent neuf (R13).
* **$H_A$ (Déterminisme de la règle)** : La règle de repli et les critères de lecture scellés forment un automate déterministe ; des sous-agents neufs indépendants produisent exactement le même verdict par critère et pour la porte.
* **$H_B$ (Sous-spécification résiduelle)** : La formulation des preuves des critères 1 à 8 laisse une marge d'interprétation (ex. sur la définition d'une courbe « dose-réponse » monotone ou sur l'audit d'un PDF pour le critère 8), entraînant une divergence entre évaluateurs ou une requête d'arbitrage humain avant verdict.
* **Protocole et contrôle négatif** : Générer 10 dossiers de preuves synthétiques (illustratif) via `python -m controle_ia.run_factice` (VÉRIFIÉ, Pièce D) incluant des cas sains (tous critères remplis), des cas d'échec franc (plancher aléatoire non battu) et des **contrôles négatifs d'artefacts** (fichier `.sha256` corrompu, absence de contre-lecture R2, score de juge non fini à 0,98 au lieu de 0,99). Faire évaluer chaque dossier par 3 instances neuves indépendantes (illustratif) sous R13.
* **Métrique et seuil** : Taux de concordance exacte inter-agents sur le triplet (verdict par critère, verdict de porte, déclenchement du repli) ; seuil exigé = 100 % sur les 10 dossiers (illustratif), et 0 % de faux positifs de validation sur les contrôles négatifs d'artefacts (R5 : VÉRIFIÉ).
* **Issues falsifiantes** :
  * Si la concordance est < 100 % ou si un seul contrôle négatif passe en « tenu », **$H_A$ est falsifiée** : la règle de repli est non scellable en l'état et son parseur de preuves doit être corrigé avant le 30 novembre.
  * Si la concordance est de 100 % avec rejet systématique des artefacts, **$H_B$ est falsifiée** sur le périmètre testé.

### Expérience 2 : Existence de l'organisme à dose-réponse (Critère 2, menace R-680)
* **Objectif** : Trancher si l'absence d'avancement du critère 2 au 30 novembre relève d'un manque de temps/calcul (« non concluant ») ou d'une impossibilité technique sur Llama-3.1-8B-Instruct (« non tenu » déclenchant l'arrêt de la banque R-680).
* **$H_A$ (Contrôlabilité continue)** : Il existe un paramétrage numérique de consigne système (i) et d'adaptateur de bas rang (ii) sur Llama-3.1-8B-Instruct induisant une dégradation monotone du taux de sabotage en fonction de la dose, avec préservation de la validité syntaxique (scores finis $\ge 0,99$, Pièce B).
* **$H_B$ (Bifurcation brutale / Effondrement)** : Toute augmentation du paramètre de dose fait basculer le modèle directement d'un comportement honnête (0 % de sabotage) à une destruction grossière ou au refus/incohérence (scores finis $< 0,99$), sans régime intermédiaire de sabotage discret (« absence de dose diffuse avec dommage », R-680, VÉRIFIÉ).
* **Métrique, seuil et contrôle négatif** : Corrélation de rang de Spearman $\rho_S$ entre la dose numérique (sur une grille de 5 doses préenregistrées, illustratif) et le taux de sabotage mesuré contre la référence cachée, sous contrainte de taux de scores finis $\ge 0,99$. Seuil préenregistré : $\rho_S \ge 0,80$ (illustratif) avec au moins 2 doses intermédiaires (illustratif) produisant un taux de sabotage compris dans $[0,10 ; 0,70]$ (illustratif). **Contrôle négatif** : Dose nulle ($d=0$, épisodes honnêtes) et adaptateur initialisé à zéro.
* **Issues falsifiantes** :
  * Si sur la grille complète exécutée et intègre, aucune paire de doses intermédiaires n'entre dans $[0,10 ; 0,70]$ ou si $\rho_S < 0,80$, **$H_A$ est falsifiée** : le critère 2 est « non tenu » (et R-680 arrête la banque).
  * Si les deux organismes (i) et (ii) franchissent $\rho_S \ge 0,80$ avec deux doses intermédiaires valides et scores finis $\ge 0,99$, **$H_B$ est falsifiée** : le critère 2 est « tenu ».

### Expérience 3 : Pouvoir discriminant des sondes linéaires v0 (Critère 3)
* **Objectif** : Trancher le critère 3 sur les organismes (i) et (ii) validés à l'Expérience 2.
* **$H_A$ (Signal linéaire interne)** : Les activations internes de Llama-3.1-8B-Instruct contiennent une direction linéaire séparant les épisodes sabotés des épisodes honnêtes appariés au-dessus du plancher aléatoire sur (i) ET sur (ii).
* **$H_B$ (Indiscernabilité linéaire en v0)** : Sur au moins l'un des deux organismes (notamment (ii) par adaptateur de bas rang), la représentation interne du sabotage n'est pas linéairement séparable des épisodes honnêtes au-dessus de directions aléatoires appariées.
* **Métrique, seuil et contrôle négatif** : Différence de rappel à $\tau = 0,01$ de fausses alertes (ou AUROC selon le préenregistrement de G0 ; métrique exacte de G0 non détaillée dans la Pièce A, donc AUROC / Rappel@1% pris comme illustratif de la métrique scellée) entre la sonde v0 et le 95e centile (illustratif) d'une distribution de 1 000 sondes (illustratif) ajustées sur des directions aléatoires orthogonales de même dimension (**contrôle négatif : plancher aléatoire apparié**, VÉRIFIÉ dans le glossaire) et étiquettes permutées.
* **Issues falsifiantes** :
  * Si la sonde v0 ne dépasse pas le seuil du plancher aléatoire apparié sur (i) OU sur (ii), **$H_A$ est falsifiée** (Critère 3 « non tenu »).
  * Si la sonde v0 dépasse le seuil sur (i) ET sur (ii) avec gardes intègres, **$H_B$ est falsifiée** (Critère 3 « tenu »).

---

## (c) Mesure minimale de fonctionnement des instruments nommés

Pour chaque instrument technique ou de gouvernance nommé dans la question et les faits, voici la mesure minimale de fonctionnement avant de l'autoriser à gouverner la porte G0 ou le report :

| Instrument nommé | Cas honnêtes appariés (Contrôle de fausses alertes) | Taux de détection (Rappel) et Taux de fausses alertes (FPR) exigés | Vérification mécanique à battre (Plancher) |
| :--- | :--- | :--- | :--- |
| **1. Harnais d'exécution et de capture** (Critère 1, VÉRIFIÉ prouvé) | Exécutions répétées du même épisode honnête à graine fixée (`SeedSequence`, R9, VÉRIFIÉ). | **Détection d'artefact** : 100 % sur corruption injectée (R5, VÉRIFIÉ). **FPR (dérive numérique)** : 0 % d'écart au-delà de la tolérance virgule flottante entre deux runs déterministes. | Comparaison d'empreintes `.sha256` (R6) des tenseurs d'activations bruts sur disque. |
| **2. Sondes linéaires v0** (Critère 3, ouvert) | Jumeaux honnêtes des unités d'épreuve (dose = 0, même tâche et graine de tirage, Pièce B). | En G0 : performance strictement supérieure au plancher aléatoire apparié à 95 % de confiance (illustratif pour G0 ; VÉRIFIÉ pour G1 à $\tau = 0,01$ de FPR, Pièce B). | **Plancher aléatoire apparié** (Glossaire, VÉRIFIÉ) : sondes linéaires projetées sur des sous-espaces aléatoires de même rang + classifieur sur la simple longueur en jetons de la réponse. |
| **3. Base boîte noire par action et séquentielle** (Critère 4, ouvert) | Mêmes épisodes honnêtes du jeu d'évaluation que ceux soumis aux sondes (Pièce A, Critère 4, VÉRIFIÉ). | **Finitude** : $\ge 0,99$ de scores continus finis sur les notations (Pièce B, R-671, VÉRIFIÉ). **Calibrage** : FPR empirique à $\tau = 0,01$ borné par la garde $\delta = 0,05$ en G1 (Pièce B). | Moniteur mécanique trivial : filtre par expressions régulières (mots-clés de refus/erreur) et prédicteur aléatoire uniforme continu sur $[0, 1]$ avec bris d'égalité scellé (D-S13, VÉRIFIÉ). |
| **4. Agrégateurs séquentiels** (Critère 5, VÉRIFIÉ prouvé en simulation T0.3) | Trajectoires synthétiques d'épisodes honnêtes sans sabotage (bruit gaussien/empirique calibré). | En G1 : Rappel à $\text{FPR} = 0,01$ supérieur à la meilleure base boîte noire et aux 2 bases boîte blanche à 95 % de confiance (N-008, N-056, VÉRIFIÉ). | (ii) Cascade de portes logiques (ET/OU/seuil max) sur les mêmes sondes ; (iii) Sonde lue uniquement sur le dernier état de l'épisode (Pièce B, VÉRIFIÉ). |
| **5. Évaluateur de porte R13 et Gardes d'arrêt R5** (Gouvernance) | Dossiers de preuves valides complets générés par `run_factice` (Pièce D, VÉRIFIÉ) avec empreintes `.sha256` exactes. | **Détection de non-conformité** : 100 % sur dossier incomplet, chiffre sans empreinte (R6), état de l'art sans page PDF (R7), ou préenregistrement non contre-lu (R2). **FPR** : 0 % de rejet sur dossier sain. | Script mécanique de vérification syntaxique : `sha256sum -c`, vérification d'existence de fichiers sur disque (R11) et contrôle de dates d'horodatage git des commits (R9). |

---

## (d) Ancrage matériel et Livrables 1 à 6 de l'Arbitre

### Ancrage matériel, calcul et coûts
* **Modèles ouverts** : Llama-3.1-8B-Instruct (VÉRIFIÉ, Glossaire) pour les organismes (i) et (ii) et l'extraction d'activations. (Les organismes de 70 milliards et la seconde famille mentionnés en Pièce C relèvent des paliers ultérieurs : VÉRIFIÉ).
* **Volume de calcul et dimensionnement** :
  * Pour G1 (gelée pendant le report) : $\ge 288$ unités d'épreuve par mode, chacune portant des épisodes honnêtes ($K_h = 10$, plancher 5) et sabotés ($n_h = n_s \ge \max(288 ; n_{80})$) (VÉRIFIÉ, Pièce B).
  * Pour achever G0 (critères 2, 3, 4) pendant un éventuel report : un jeu pilote réduit suffit dès lors qu'il démontre la dose-réponse (critère 2), le dépassement du plancher aléatoire (critère 3) et l'exécution de bout en bout de la base boîte noire (critère 4), soit de l'ordre de 50 à 100 épisodes par organisme et par dose (illustratif), représentant environ 15 à 40 heures-GPU A100-80Go (illustratif).
* **Coûts** :
  * Budget initial accordé pour les instruments : 90 USD (VÉRIFIÉ, Pièce B).
  * Coût estimé de la banque complète (G1) : 300 à 1 400 USD (VÉRIFIÉ, Pièce B).
  * Coût matériel de résorption des critères 2, 3 et 4 de G0 pendant le report (1er déc. 2026 – 31 janv. 2027) : estimé entre 60 et 250 USD (illustratif) de calcul GPU et d'appels API de juges (si la base boîte noire ou la notation utilise un modèle externe : SUPPOSÉ). Les critères 6, 7 et 8 ont un coût de calcul GPU nul (travail de rédaction, vérification de PDF sous R7 et contre-lecture par sous-agent sous R2 : 5 à 20 USD de jetons CPU/LLM, illustratif).

---

### Point 1. Déclencheur (au 30 novembre 2026, 23:59 UTC)

#### Table des trois issues par critère (1 à 8)
Conformément à R13 (VÉRIFIÉ), un sous-agent neuf inspecte uniquement les fichiers de preuves listés dans le manifeste de G0 et leurs empreintes `.sha256` (R6).

| Issue du critère $c \in \{1..8\}$ | Définition opérationnelle (sans jugement humain) | Preuves exigées par R13 |
| :--- | :--- | :--- |
| **TENU** | Le test préenregistré du critère $c$ a tourné jusqu'au bout, toutes les gardes techniques (R5, R9, scores finis) sont vertes, et la métrique franchit le seuil dans le sens prédit. Pour les critères documentaires (6, 7, 8) : fichier scellé, `.sha256` valide, rapport de contre-lecture R2 sans réserve bloquante, et 100 % des citations rattachées à un PDF empreinté avec numéro de page (R7). | Manifeste de run (R9), sortie de test, `.sha256` (R6), certificat R2 (pour 6, 7), table d'audit PDF (pour 8). |
| **NON TENU** | L'expérience ou la vérification a été exécutée validement (gardes techniques R5 vertes, échantillon complet), mais **la métrique échoue au seuil** (ex. sonde v0 $\le$ plancher aléatoire sur (i) ou (ii) ; absence de dose diffuse avec dommage sur la grille complète, R-680). | Manifeste de run intègre (R9) démontrant l'échec empirique sur la métrique principale. |
| **NON CONCLUANT** | L'expérience n'a pas pu être menée à terme avant l'échéance (code/organisme non prêt, devis de calcul non alloué), OU une garde technique a interrompu le run (R5 : scores finis $< 0,99$ sous R-671, corruption de fichier, absence de contre-lecture R2 à temps). | Absence d'empreinte finale au manifeste, ou log d'arrêt de garde R5 / rapport d'incomplétude. |

#### Règle de déduction de l'issue de la porte G0
Soit $E$ l'ensemble des 8 critères :
1. **PORTE FRANCHIE** $\iff \forall c \in \{1..8\}, \text{Issue}(c) = \text{TENU}$.
2. **PORTE NON FRANCHIE** $\iff \exists c \in \{1..8\}, \text{Issue}(c) = \text{NON TENU}$.
3. **PORTE NON CONCLUANTE** $\iff (\forall c \in \{1..8\}, \text{Issue}(c) \neq \text{NON TENU}) \land (\exists c \in \{1..8\}, \text{Issue}(c) = \text{NON CONCLUANT})$.

#### « Non franchie » et « Non concluante » doivent-elles déclencher la même suite au 30 novembre ?
* **Option 1A (Suite identique — Report automatique dans les deux cas)** : Tout verdict autre que « Franchie » ouvre le report jusqu'au 31 janvier 2027.
  * *Avantage* : Simplicité mécanique maximale ; donne une chance de corriger un bug d'implémentation ayant causé un « Non tenu ».
  * *Inconvénient* : Viole l'esprit de R1/R3 (« Aucun run visant un signe positif », VÉRIFIÉ) et de R-680 (« absence de dose diffuse avec dommage = arrêt de la banque », VÉRIFIÉ). Si un critère est empiriquement falsifié (« Non tenu » sur une exécution valide), relancer de nouvelles conceptions jusqu'à obtenir un signe positif constitue du *p-hacking* séquentiel ou une réécriture déguisée.
* **Option 1B (Suite différenciée — Recommandée)** :
  * **Si G0 est « NON CONCLUANTE »** (ex. retard d'exécution sur 2, 3, 4, 6, 7, 8 ou arrêt par garde R5 pour scores non finis R-671 sans falsification de l'hypothèse) : déclenchement automatique du **report unique au 31 janvier 2027, 23:59 UTC**.
  * **Si G0 est « NON FRANCHIE »** (au moins un critère est prouvé « NON TENU » sur un run valide, par exemple effondrement de la dose-réponse R-680 ou sonde v0 sous le plancher aléatoire sans artefact) : **arrêt immédiat de la branche falsifiée** (pas de répétition du même run pour chercher un signe positif, R3). Le report au 31 janvier 2027 n'est ouvert **que** si un protocole de repli technique *pré-spécifié avant le 30 novembre* (ex. changement de couche d'extraction ou de famille d'invite déjà inscrit au préenregistrement de G0) existe sans modifier l'énoncé du critère ; à défaut de repli technique pré-scellé dans G0, la porte échoue définitivement dès le 30 novembre (arrêt ou pivot majeur hors G0).
* **Recommandation** : **Option 1B** (Confiance : **0,85**). Elle seule protège R3 et R-680 tout en permettant d'absorber le retard calendaire constaté au 29 octobre (6 critères ouverts faute de temps/calcul, soit « Non concluants »).
* **Qui prononce et sur quelles preuves** : Un sous-agent neuf (R13, VÉRIFIÉ) exécute un script d'audit lisant le manifeste G0, vérifie les `.sha256` (R6), scelle le rapport de verdict, et le soumet à Lazar pour GO formel.

---

### Point 2. Pendant le report (1er décembre 2026 – 31 janvier 2027)

#### Table de dépendance et de gel (Critères 2, 3, 4, 6, 7, 8)
Les critères 1 et 5 étant prouvés au 29 octobre (Pièce B, VÉRIFIÉ), ils sont verrouillés (aucun recalcul, sauf test de non-régression si le harnais est touché).

| Critère ouvert | Dépendances amont | Statut des tâches pendant le report | Régime de dépense | Ce qui est strictement GELÉ |
| :--- | :--- | :--- | :--- | :--- |
| **Critère 2** : Organismes (i) et (ii) à dose-réponse | Critère 1 (Harnais, acquis) + Résolution de la stabilité des juges (scores finis $\ge 0,99$, R-671). | **ACTIF PRIORITAIRE** : Calibration de la grille de doses sur (i) consigne et (ii) adaptateur de bas rang ; vérification de la courbe dose-réponse. | **Dépense sur devis G0** (GPU + API juges). Arrêt immédiat si R-680 est déclenché. | Génération de la banque complète G1 (les $\ge 288$ unités/mode de G1 sont interdites). |
| **Critère 3** : Sondes v0 > plancher aléatoire sur (i) et (ii) | Critère 1 (acquis) + **Critère 2** (nécessite les épisodes générés par (i) et (ii)). | **BLOQUÉ PUIS ACTIF** : Écriture/test du code sur `run_factice` autorisé immédiatement ; entraînement et test réel des sondes v0 débloqués dès que le Critère 2 est TENU. | **Dépense sur devis G0** uniquement après validation du Critère 2 (extraction d'activations déjà payée lors du run du Critère 2). | Aucune évaluation des agrégateurs séquentiels sur données réelles (c'est l'expérience décisive de G1). |
| **Critère 4** : Base boîte noire (action + séquentielle) sur le même jeu | Critère 1 (acquis) + **Critère 2** (nécessite le même jeu d'épisodes que le Critère 3) + règle D-S13 (scores continus). | **BLOQUÉ PUIS ACTIF** : Validation du pipeline et des scores finis ($\ge 0,99$) sur jeu pilote autorisée ; exécution finale débloquée sur le jeu exact produit par le Critère 2. | **Dépense sur devis G0** (appels du moniteur boîte noire sur le jeu d'épisodes de G0 uniquement). | Aucune comparaison statistique boîte blanche contre boîte noire (c'est le critère disjonctif N-008/N-056 de G1). |
| **Critère 6** : Préenregistrement de G1 scellé et contre-lu | Décisions N1–N6 (acquises, Pièce B), règle D-S13 (acquise), mesure de la dispersion $\rho$ des comparateurs au pilote (Pièce B). | **ACTIF IMMÉDIATEMENT** : Rédaction du document complet, simulation de validité du repli N3 si requise, contre-lecture par sous-agent neuf (R2), scellement `.sha256` (R6). | **Sans dépense GPU** (coût négligeable de sous-agent R2 sur CPU/API). | **GEL TOTAL de G1** : aucune lecture de $f_A$ (P-9, VÉRIFIÉ), aucune ouverture du mode tenu à l'écart (N-054, VÉRIFIÉ), aucun tirage des 288 unités. |
| **Critère 7** : Préenregistrement du papier C (HC1–HC3) scellé et contre-lu | Indépendant techniquement des critères 2–4 (travail conceptuel et méthodologique). | **ACTIF IMMÉDIATEMENT** : Rédaction des hypothèses HC1 à HC3, plan d'analyse, contre-lecture R2, scellement R6. | **Sans dépense GPU** (coût négligeable de sous-agent R2). | **GEL TOTAL du papier C** : aucune expérience décisive de HC1–HC3 ne peut tourner avant son scellement ET le franchissement de G0. |
| **Critère 8** : État de l'art vérifié (0 chiffre non vérifié) | Accès aux PDF originaux et empreintes `.sha256` (R7). | **ACTIF IMMÉDIATEMENT** : Audit systématique de tous les documents du programme ; rattachement de chaque chiffre à un PDF empreinté + page citée (R7) ou retrait du chiffre. | **Dépense nulle** (vérification documentaire). | Publication ou envoi externe de tout document contenant un chiffre non audité sous R7. |

#### Règle de dépense bornée pendant le report (1er déc. 2026 – 31 janv. 2027)
* **Option 2A (Plafond en pourcentage du financement externe)** : Autoriser la dépense d'au plus 10 % (illustratif) de la subvention entrant le 1er décembre.
  * *Avantage* : Proportionnel aux moyens.
  * *Inconvénient* : Si le financement externe dépend lui-même de G0 ou prend du retard (SUPPOSÉ), le plafond est indéfini ; de plus, dépenser les fonds de G1 alors que G0 n'est pas franchie expose le financeur à un coût irrécupérable si le Critère 2 échoue (R-680).
* **Option 2B (Plafond absolu strict séquencé par le Critère 2 — Recommandée)** :
  * Pendant le report, le budget de calcul du programme est cantonné à une **enveloppe maximale de 250 USD (illustratif)** (ou **5 % du palier financé [illustratif]**, le plus bas des deux s'appliquant), divisée en deux tranches verrouillées :
    1. *Tranche 1 (Critère 2 + stabilité des juges)* : plafond de **150 USD (illustratif)**. Tant que le Critère 2 n'est pas validé (dose-réponse prouvée sur (i) et (ii)), aucune dépense de calcul n'est engagée sur les Critères 3 et 4.
    2. *Tranche 2 (Critères 3 et 4 sur le jeu d'épisodes du Critère 2)* : plafond de **100 USD (illustratif)**, débloqué automatiquement par l'empreinte de réussite du Critère 2.
  * **100 % du budget des expériences de G1 (les 300 à 1 400 USD de la banque complète, VÉRIFIÉ Pièce B) et du papier C est gelé en trésorerie** jusqu'au GO de G0.
* **Recommandation** : **Option 2B** (Confiance : **0,90**). Elle aligne la dépense sur la menace principale identifiée en Pièce B (R-680 : l'absence de dose diffuse arrête la banque) et protège intégralement l'argent du financeur.

---

### Point 3. Second verdict au 31 janvier 2027, 23:59 UTC

#### Ce qui se passe selon chacune des trois issues au 31 janvier 2027
Puisque la décision du directeur du 29 octobre stipule que le report est **unique** et borné au **31 janvier 2027, 23:59 UTC** (VÉRIFIÉ dans la Question), la distinction entre « Non franchie » et « Non concluante » **disparaît quant à leurs conséquences** lors de ce second verdict :

1. **Si le second verdict est « FRANCHIE »** ($\forall c \in \{1..8\}, \text{Issue}(c) = \text{TENU}$) :
   * Le sous-agent neuf (R13) scelle le verdict positif ; Lazar donne le GO.
   * Le gel budgétaire est levé : lancement immédiat de la production de la banque de G1 ($\ge 288$ unités/mode) et des expériences du papier C selon leurs préenregistrements scellés (Critères 6 et 7).
   * Le calendrier aval (GC, G1) est décalé exactement de la durée consommée par le report (au plus 2 mois), sans modification des critères de G1 (N-008, N-054, N-056 restent intacts).
2. **Si le second verdict est « NON FRANCHIE » OU « NON CONCLUANTE »** ($\exists c \in \{1..8\}, \text{Issue}(c) \neq \text{TENU}$) :
   * **Échec définitif de la porte G0 (« G0 terminée en échec »)**. Aucun nouveau délai n'est accordé.
   * **Arrêt immédiat de la piste G1** telle que conçue (la banque G1 n'est pas générée).
   * **Conséquence sur le programme et le financement** :
     * *Option 3A (Arrêt complet et restitution)* : Fermeture du programme de recherche sur la surveillance boîte blanche séquentielle et restitution au financeur du reliquat non dépensé (soit $\ge 95\%$ des fonds grâce au gel de l'Option 2B).
     * *Option 3B (Pivot vers le Papier C seul si et seulement si les critères 1, 4, 7, 8 sont tenus — SUPPOSÉ)* : Si l'échec porte uniquement sur les organismes/sondes de G1 (critères 2 ou 3), mais que le préenregistrement du papier C (critère 7) ne dépend pas des sondes v0 (SUPPOSÉ, le contenu de HC1–HC3 n'étant pas dans les pièces), soumettre au financeur l'allocation des fonds au seul papier C ou la restitution.
   * **Recommandation sur l'issue d'échec** : **Option 3A par défaut** (Arrêt de la piste G1, notification immédiate au financeur avec état des fonds intacts, et droit pour le financeur d'exiger la restitution ou d'approuver un avenant sur le papier C si le critère 7 est tenu). Confiance : **0,90**. Cela garantit qu'aucune décision unilatérale post-lecture ne détourne le financement vers un objectif amoindri.

#### Contenu minimal du rapport de porte scellé (au 30 nov. 2026 et au 31 janv. 2027)
Le fichier `rapports/verdict_G0_<date>_v1.md` (R12) accompagné de son `.sha256` (R6) doit contenir exactement :
1. **En-tête d'identité et d'indépendance (R13)** : Identifiant d'instance du sous-agent neuf, horodatage UTC, hash du commit git du dépôt, et déclaration formelle d'absence de participation à l'écriture des préenregistrements et des analyses.
2. **Vérification d'intégrité des critères gelés** : Empreinte `.sha256` du fichier de définition des 8 critères de G0 (`docs/brief-claude-code-programme-complet-v2.md`, préfixe `d5ac34db…`, Pièce A) comparée à l'empreinte de référence du 29 octobre 2026. Si l'empreinte diffère d'un seul bit $\rightarrow$ **INVALIDATION AUTOMATIQUE (verdict forcé à NON FRANCHIE pour altération de critère)**.
3. **Table d'audit des 8 critères** : Une ligne par critère (1 à 8) comportant : (a) le chemin du fichier de preuve et son `.sha256` (R6), (b) le statut des gardes R5 et des manifestes de graines R9, (c) la valeur numérique observée face au seuil préenregistré (pour 1 à 5) ou l'empreinte du certificat R2 / table PDF R7 (pour 6 à 8), (d) le verdict unitaire (`TENU`, `NON TENU`, `NON CONCLUANT`).
4. **Relevé budgétaire du report** (au 31 janv. 2027) : Somme exacte dépensée depuis le 1er décembre contre le plafond scellé (ex. 250 USD, illustratif), et attestation que 0 épisode décisif de G1 ou du papier C n'a été lu (P-9, R1).
5. **Verdict global déduit mécaniquement** et instruction d'exécution associée (ouverture du report au 30 nov. ; levée du gel ou arrêt définitif de G1 au 31 janv.).

#### Ce qui interdit mécaniquement un second report ou une réécriture déguisée d'un critère
1. **Verrou cryptographique anti-réécriture (R6 + R12)** : Le script d'audit R13 contient en dur (hardcodé et scellé avant le 30 novembre) les empreintes `.sha256` des définitions des critères 1 à 8 et des scripts de test des critères 1 à 5. Modifier un seuil, changer la définition du plancher aléatoire apparié ou retirer un organisme brise l'empreinte et met la porte en échec immédiat.
2. **Verrou horaire de caducité (Dead-man switch)** : Au-delà du `2027-01-31T23:59:59Z`, toute absence de rapport R13 scellé portant la mention `FRANCHIE` équivaut de plein droit et sans intervention humaine au verdict `NON FRANCHIE — ARRÊT DÉFINITIF DE G1`.
3. **Interdiction de nœud de gouvernance post-lecture** : À l'instar de la règle scellée pour G1 en Pièce B (« *une seule lecture, "G1 non promue" sans nœud après lecture, règle scellée contre toute seconde fiche* », VÉRIFIÉ), la clause de G0 interdit formellement d'ouvrir un nœud de décision dans `registres/decisions.md` après le 30 novembre pour modifier l'échéance du 31 janvier 2027 ou le texte des 8 critères.

---

### Point 4. Clause scellable (au plus 150 mots, une phrase principale et ses conditions)

*Option unique recommandée (Confiance : 0,95 — respecte la limite stricte de 150 mots et d'une phrase principale assortie de ses conditions) :*

> **Clause de repli G0 (N-027-bis) :** Si, au 30 novembre 2026 à 23:59 UTC, le verdict scellé par un sous-agent neuf (R13) sur les huit critères inchangés de la porte G0 (empreinte `d5ac34db…`) n'est pas « franchie », un report unique et non renouvelable s'ouvre de plein droit jusqu'au 31 janvier 2027 à 23:59 UTC, sous les quatre conditions impératives suivantes : (i) tout critère prouvé « non tenu » sans artefact interdit de relancer le même protocole pour chercher un signe positif (R3) ; (ii) aucune expérience décisive de G1 ni du papier C n'est exécutée ou lue (R1, P-9) ; (iii) les dépenses de calcul visant à résorber les critères ouverts (2, 3, 4, 6, 7, 8) sont plafonnées à 250 USD [illustratif], le budget de G1 restant intégralement gelé ; (iv) à défaut d'un verdict « franchie » scellé au 31 janvier 2027 à 23:59 UTC, la piste G1 est définitivement arrêtée sans nœud de décision.

*(Compte exact : 148 mots, 1 phrase unique structurée par deux-points et points-virgules).*

---

### Point 5. Phrase pour le financeur (en anglais, au plus 40 mots, sans rien promettre)

* **Option 5A (Axée sur le calendrier et le gel budgétaire — Recommandée)** :
  > "If Gate G0's eight frozen criteria are not all met by November 30, 2026, a single non-renewable deferral until January 31, 2027 applies, during which G1 funds remain frozen; otherwise, the G1 track stops and unspent funds are returned." *(39 mots)*
  * *Avantage* : Dit la date initiale, la borne exacte du report unique, l'intangibilité des 8 critères, la protection des fonds pendant le report, et l'arrêt sans promesse de succès.
  * *Inconvénient* : Aucun.
* **Option 5B (Ultra-concise)** :
  > "Should Gate G0 fail to meet all eight unchanged criteria by November 30, 2026, one final extension runs until January 31, 2027 with G1 compute funds frozen; if still unmet then, the G1 track terminates immediately." *(36 mots)*
  * *Avantage* : Plus courte.
  * *Inconvénient* : Ne mentionne pas explicitement le sort des fonds non dépensés en cas d'arrêt.
* **Recommandation** : **Option 5A** (Confiance : **0,95**).

---

### Point 6. À décider maintenant (Liste fermée des choix à fixer avant le 30 novembre 2026)

Pour que la clause s'applique de manière purement mécanique le 30 novembre à 23:59 UTC sans aucune décision après lecture des résultats (« on verra » = hors cadre), Lazar doit trancher et sceller **avant le 30 novembre** la liste fermée des **6 choix suivants** :

| # | Choix à fixer avant le 30 nov. 2026 | Options fermées | Avantage / Inconvénient | Recommandation & Confiance |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | **Seuils numériques exacts des critères 2 et 3 de G0** (la Pièce A dit « sabotage mesurable avec dose-réponse » et « au-dessus du plancher aléatoire apparié » sans chiffrer le seuil de G0, contrairement à G1). | **Opt. A** : Fixer un seuil formel (ex. Critère 2 : $\ge 3$ doses avec monotonie stricte et scores finis $\ge 0,99$ ; Critère 3 : borne inférieure de l'IC à 95 % de la sonde v0 > 95e centile du plancher aléatoire apparié [illustratif]).<br>**Opt. B** : Laisser le sous-agent R13 apprécier visuellement la courbe. | Opt. A rend R13 déterministe (testable par l'Expérience 1).<br>Opt. B est **non scellable** (interdit par les critères de lecture). | **Opt. A** (Obligatoire sous R1).<br>Confiance : **0,95**. |
| **C2** | **Traitement d'un critère « NON TENU » au 30 novembre** (distinction entre retard « non concluant » et réfutation empirique « non tenu »). | **Opt. A** : Report ouvert uniquement aux critères « non concluants » ; un critère « non tenu » arrête la porte dès le 30 nov., sauf repli technique pré-inscrit au préenregistrement de G0.<br>**Opt. B** : Report ouvert même si un critère est « non tenu », avec droit de chercher un nouveau design librement. | Opt. A respecte R3 et R-680.<br>Opt. B autorise la chasse au signe positif (viole R3). | **Opt. A**.<br>Confiance : **0,85**. |
| **C3** | **Plafond de dépense autorisé pendant le report** (et prolongation du nœud `GO-2026-10-04-08` qui échoit le 1er nov., Pièce A bis). | **Opt. A** : Plafond dur de **250 USD** (illustratif) séquencé (150 USD sur Critère 2, puis 100 USD sur Critères 3–4), budget G1 gelé à 100 %.<br>**Opt. B** : 0 USD sur le financement externe (financement sur fonds propres uniquement). | Opt. A permet de finir G0 sans entamer le budget de la banque G1.<br>Opt. B bloque G0 si les 90 USD initiaux (Pièce B) sont épuisés. | **Opt. A** (ou Opt. B si Lazar couvre 250 USD hors subvention : SUPPOSÉ).<br>Confiance : **0,85**. |
| **C4** | **Règle de bris d'égalité d'office après porte des scores finis pour le Critère 4** (CL2-12, R-694 : Pièce B indique que c'est une recommandation « non tranchée », seule D-S13 étant close). | **Opt. A** : Trancher R-694 positivement maintenant (le bris d'égalité D-S13 s'applique d'office uniquement si la cellule atteint $\ge 0,99$ de scores finis ; sinon la cellule est déclarée « non concluante » sous R-671).<br>**Opt. B** : Appliquer le bris d'égalité même sur des cellules ayant $< 0,99$ de scores finis. | Opt. A empêche qu'un juge défaillant (pièce 29-2) soit masqué par un bris d'égalité aléatoire.<br>Opt. B contamine la base boîte noire par du bruit de tie-break. | **Opt. A**.<br>Confiance : **0,90**. |
| **C5** | **Sort du Papier C (Critère 7) si G0 échoue au 31 janvier 2027 à cause des Critères 2 ou 3** (organismes/sondes de G1). | **Opt. A** : Arrêt complet du programme (G1 + Papier C) et restitution des fonds.<br>**Opt. B** : Arrêt de G1 seule ; si les critères 1, 4, 7 et 8 sont TENUS au 31 janv., proposition automatique au financeur de réallouer la part du Papier C ou de restituer. | Opt. A est la plus lisible et sans ambiguïté.<br>Opt. B sauve le papier C s'il est indépendant des sondes v0 (indépendance SUPPOSÉE). | **Opt. A par défaut** (ou Opt. B seulement si l'indépendance de HC1–HC3 aux critères 2–3 est écrite dans le contrat du financeur avant le 30 nov.).<br>Confiance : **0,85**. |
| **C6** | **Confirmation de la ligne de registre « R-609 remplace R-468 »** (mentionnée en Pièce C, point 14, comme attente de confirmation de Lazar). | **Opt. A** : Inscrire formellement dans `registres/decisions.md` que R-609 remplace R-468 avant l'audit du Critère 8.<br>**Opt. B** : Laisser le statut implicite (« superseded in practice »). | Opt. A évite que le sous-agent R13 ne déclare une contradiction documentaire lors de la vérification de G0.<br>Opt. B crée un risque de rejet R13 pour incohérence de registre. | **Opt. A**.<br>Confiance : **0,95**. |

FIN-DE-CELLULE