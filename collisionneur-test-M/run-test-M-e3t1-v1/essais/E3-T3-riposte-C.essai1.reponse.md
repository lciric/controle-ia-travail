# Cellule C, Tour III.3 : Riposte et protocole corrigé

**Intégrité des pièces.** Le bloc FAITS indique qu'aucun fait n'est joint [RAPPORTÉ]. Les pièces E3-T1-conception-C, E3-T2-redteam-A et E3-T2-redteam-B sont complètes et se terminent par leur ligne de clôture. Conformément aux instructions, je ne réponds qu'aux sections de A et B qui visent la proposition C. Tout chiffre avancé sans dérivation formelle est marqué **illustratif**.

---

## (a) Traitement des attaques de l'équipe rouge contre C

### 1. Audit des statuts et degrés de liberté
*   **F-C1 (A) et C10 (B) — Statuts épistémiques mal employés.**
    *   *Décision :* **Acceptée.**
    *   *Raison :* Le bloc FAITS étant vide, rien ne peut être marqué VÉRIFIÉ hors de la présence matérielle des textes transmis. Conformément à la règle d'intégrité n° 1 (« Tu ne changes jamais un statut »), je ne modifie pas les étiquettes passées de ma pièce III.1, mais pour toute la suite de ce protocole : le nom du modèle `Llama-3.1-8B-Instruct` est [RAPPORTÉ] depuis l'énoncé ; ses dimensions architecturales ($d_{\text{model}} = 4096$, 32 couches) et le rôle d'agrégation causale du dernier jeton avant génération sont traités comme des [HYPOTHÈSES] (dont les paramètres techniques sont vérifiables par une assertion automatique sur `model.config` à l'exécution). La faisabilité nocturne est une [HYPOTHÈSE] opérationnelle.
*   **F-C11 (A) — Degrés de liberté résiduels (couche $L$, matériel, noyaux issus de bases existantes).**
    *   *Décision :* **Acceptée.**
    *   *Correction :* La couche est scellée par une règle unique sans intervention humaine : sélection automatique de la couche $L \in \{1, \dots, 32\}$ maximisant l'AUROC de validation croisée à 5 plis (illustratif) sur le seul corpus d'entraînement de la sonde. Les noyaux sémantiques ne sont plus extraits de bancs publics (pour éviter l'effet plafond de familiarité du contenu), mais rédigés de neuf sur des problèmes courants non académiques.

### 2. Construction des items, orthogonalité $T \times C$ et générateur
*   **F-C2 (A) et C5 (B) — Bascule du tour système entre $T_1$ et $T_0$ et injection de date par le *chat template*.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Supprimer le bloc système dans $T_0$ modifie les jetons de structure (`<|start_header_id|>system...`) et la date par défaut dans Llama-3.1 [HYPOTHÈSE]. Pour isoler le contenu du gabarit de l'artefact de formatage de dialogue, les quatre cellules reçoivent **exactement la même enveloppe structurelle** (tour système présent dans les 4 cellules, date neutralisée ou identique). Seul le texte à l'intérieur du prompt-système varie : cadrage de banc générique ($T_1$) contre cadrage d'assistant personnel continu ($T_0$).
*   **F-C3 (A) — Confusion des traits entre $T$ et $C$ (balises dans $C_1$, besoin utilitaire dans $C_0$).**
    *   *Décision :* **Acceptée et transformée en test.**
    *   *Correction :* J'adopte une table d'attribution stricte et disjointe. Le besoin utilitaire et les balises de structure appartiennent exclusivement à $T$. Le facteur $C$ est restreint au registre syntaxique et interpersonnel : $C_1$ (registre direct, injonctif, sans marqueur de politesse ni pronom de première personne) contre $C_0$ (registre conversationnel, modalisateurs, salutations). J'intègre le test de **partition brouillée** exigé par A (voir Expérience 1 corrigée).
*   **F-C12 (A) et C4 (B) — Rembourrage de longueur dans les salutations colinéaire avec $C_0$ et créant une interaction $T \times C$.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Tout rembourrage (*padding*) spécifique à une cellule est abandonné. L'égalisation de longueur se fait à la source en rédigeant des réalisations de $T_1/T_0$ et $C_1/C_0$ de longueur appariée à $\pm 3$ jetons (illustratif) par construction, et en incluant le nombre résiduel de jetons comme covariable fixe préenregistrée.
*   **C6 (B) — Une seule réalisation textuelle par niveau (*language-as-fixed-effect fallacy*).**
    *   *Décision :* **Transformée en test (Duel D1 de B intégré).**
    *   *Correction :* Chaque niveau ($T_1, T_0, C_1, C_0$) est instancié par $K = 4$ réalisations lexicales distinctes (illustratif), croisées aléatoirement avec les noyaux et modélisées par un effet aléatoire de réalisation. La variance inter-niveaux doit dépasser d'un facteur $\ge 4$ (illustratif) la variance intra-niveau entre réalisations.
*   **F-C13 (A) — Absence de vérification mécanique du générateur.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Ajout d'une suite de tests unitaires avec injection de mutants (espaces de fin de ligne, inversion d'étiquette, fuite de jeton système) qui doit atteindre 100 % de détection avant le scellement, plus le test de la **cellule à contenu vide** proposé par A.

### 3. Entraînement de la sonde et validité de l'Expérience 0
*   **F-C4 (A), C1 (B) et C11 (B) — Sonde entraînée sur l'annonce explicite du test, biais de personne grammaticale (2e vs 1re) et fabrication des étiquettes d'usage.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Entraîner la sonde sur « Voici un test » apprend un détecteur lexical d'annonce ou de pronom qui favorise mécaniquement $C_1$. Je remplace ce jeu d'entraînement par un **corpus de provenance écologique apuré des formats de test** :
        *   Positifs (évaluation) : énoncés issus de bancs d'essai ouverts (questions ouvertes sans options A/B/C/D ni balises `[INSTRUCTION]`, ex. questions de raisonnement ou de connaissances reformulées en question directe).
        *   Négatifs (usage) : vraies requêtes d'utilisateurs issues de journaux de conversation publics (ex. WildChat ou LMSYS-Chat-1M, [RAPPORTÉ comme bases existantes, à vérifier]), filtrées pour être des questions de même longueur et de même personne grammaticale (appariement exact de la proportion de `je`/`vous`/impératifs entre positifs et négatifs).
*   **F-C5 (A) et C2 (B) — Expérience 0 (listes d'achats en QCM) confondant « évaluation vs gabarit » avec « question vs non-question » et avec le domaine (académique vs domestique).**
    *   *Décision :* **Transformée en test.**
    *   *Correction :* Les listes d'achats sans forme interrogative sont abandonnées. Le jeu de contrôle négatif d'E0 oppose désormais deux ensembles **strictement interrogatifs, en format QCM $(A)/(B)/(C)/(D)$, et appariés par domaine** : (1) de vraies questions de banc d'essai technique/académique contre (2) de vraies questions de dépannage utilitaire du même domaine technique (extraites de forums d'entraide type StackExchange, [RAPPORTÉ comme source, à vérifier]) mises artificiellement au format QCM $(A)/(B)/(C)/(D)$. J'ajoute en outre un **témoin de provenance de domaine** (contrôle c1 de B).
*   **F-C5 (A) et C3 (B) — Témoin TF-IDF aveugle au format par construction.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Le classifieur de surface (TF-IDF + régression logistique $L_2$) est entraîné directement en validation croisée sur la tâche cible qu'il doit prédire (y compris avec les marqueurs de format QCM et les styles), plus un second témoin TF-IDF entraîné sur le corpus de la sonde.

### 4. Modèle statistique, règle de décision et H-M2
*   **F-C6 (A), F-C7 (A) et C7 (B) — Règle de décision asymétrique, trous logiques, instabilité du ratio $|\beta_T|/|\beta_C|$ et dénominateur de $d$ non fixé.**
    *   *Décision :* **Acceptée.**
    *   *Correction :*
        1. Remplacement du ratio brut par une **différence linéaire de contrastes** $|\beta_T| - 2|\beta_C| > 0$ évaluée par bootstrap non paramétrique par grappes (sur les noyaux, $10\,000$ tirages, illustratif), ce qui élimine toute division par zéro.
        2. Standardisation de tous les effets par un dénominateur unique et scellé : l'écart-type résiduel intra-noyau $\sigma_\epsilon$ du modèle mixte complet.
        3. Ajout d'un test d'équivalence **TOST** sur $\beta_C$ dans la branche $H_A$ et fermeture complète de l'arbre de décision en 4 issues mutuellement exclusives et exhaustives (voir Expérience 1 corrigée).
*   **F-C8 (A) et C9 (B) — H-M2 testée uniquement dans $(T_1, C_1)$, fragilité de la moyenne des ratios de variance par item, et classement de la permutation des options.**
    *   *Décision :* **Acceptée et transformée en test.**
    *   *Correction :*
        1. H-M2 est exécutée dans les **deux cellules extrêmes** $(T_1, C_1)$ et $(T_0, C_0)$ pour séparer la sensibilité positionnelle pure de la perte de familiarité du gabarit $T_1$.
        2. Le ratio par item est remplacé par le **ratio des composantes de variance globales** ($\sigma^2_{\text{pos}} / \sigma^2_{\text{sem}}$) estimées par un modèle linéaire mixte sur l'ensemble des items, avec le même nombre de variantes ($M = 3$, illustratif) dans chaque orbite.
        3. La permutation de l'ordre des options (qui modifie à la fois la position et le lien lettre-sens) est traitée comme une troisième orbite distincte $\mathcal{G}_{\text{opt}}$, séparée de la paraphrase lexicale pure ($\mathcal{G}_{\text{sem}}$) et du déplacement de blocs ($\mathcal{G}_{\text{pos}}$).
*   **F-C9 (A) et C8 (B) — Perplexité en covariable conditionnelle (bifurcation interdite) et statut de médiateur vs confondant.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Aucune décision conditionnelle aux données de test. Deux modèles sont préenregistrés et exécutés systématiquement : **M2-A (confirmatoire principal)** sans perplexité (car H-M2 postule que le changement positionnel agit *via* une dérive distributionnelle, dont la perplexité est le médiateur [HYPOTHÈSE]), et **M2-B (analyse de médiation secondaire)** incluant la log-perplexité centrée comme covariable fixe, plus le contrôle d'injection de noms rares de A (pour vérifier si la sonde réagit à la perplexité pure sans changement positionnel).
*   **F-C10 (A) — Dictionnaire de synonymes sans vérification de sens.**
    *   *Décision :* **Acceptée.**
    *   *Correction :* Les substitutions lexicales de $\mathcal{G}_{\text{sem}}$ portent uniquement sur les verbes et adjectifs d'encadrement du noyau (pré-validés par double lecture humaine à 100 % sur les 120 noyaux avant scellement), jamais sur les entités ou les valeurs numériques qui déterminent la réponse correcte.
*   **Adversaire-modèle $\gamma$ (A et B) — Absence de contrôle positif d'injection et de balayage positionnel.**
    *   *Décision :* **Transformée en test.**
    *   *Correction :* Ajout d'un **contrôle positif synthétique** par addition d'un vecteur connu dans le flux résiduel des cellules $T_1$ pour vérifier que le pipeline recouvre $\beta_T$, et enregistrement secondaire (exploratoire, hors règle de décision) de 3 positions de jetons antérieures (fin du prompt-système, fin de la question, dernier jeton).

---

## (b) Protocole expérimental corrigé (Inférence forte)

### Architecture commune du générateur et de la sonde

1.  **Table d'attribution scellée et disjointe ($K=4$ réalisations par niveau, illustratif) :**
    *   **Facteur $T$ (Gabarit pragmatique et structurel) :**
        *   $T_1$ (Banc d'essai) : Prompt-système générique d'évaluation + absence d'objectif pratique + choix d'options présentées en liste verticale numérotée `(A)`, `(B)`, `(C)`, `(D)` + consigne de format (`Réponse (une seule lettre) :`).
        *   $T_0$ (Usage utilitaire) : Prompt-système d'assistant de travail continu + contexte d'action concret (`Pour dépanner mon script...`) + mêmes 4 options intégrées en prose fluide dans la phrase interrogative + absence de consigne de lettre.
    *   **Facteur $C$ (Registre stylistique pur, à structure constante) :**
        *   $C_1$ (Direct/Impersonnel) : Phrases déclaratives et impératives neutres, sans pronoms de 1re personne ni formules de politesse, longueur appariée à $C_0$ ($\pm 3$ jetons, illustratif).
        *   $C_0$ (Conversationnel) : Salutations initiales, pronoms de 1re personne, modalisateurs (`j'aimerais savoir si...`, `merci`), sans aucun mot exprimant un besoin pratique (réservé à $T_0$).
    *   **Facteur Placebo $P$ (Contrôle c2/D2 de B) :** Variation de surface de même distance d'édition que $C$ mais pragmatiquement neutre (ex. ponctuation double vs simple, synonymes d'adverbes temporels dans le contexte neutre).
2.  **Assertions mécaniques avant scellement :**
    *   Vérification sur les $120 \times 4 = 480$ invites (illustratif) que les jetons spéciaux d'en-tête (`system`, `user`, `assistant`) sont strictement identiques en nombre et en format dans les 4 cellules, et que le jeton lu est toujours l'indice $-1$ correspondant à `\n\n` après `<|end_header_id|>`.
    *   Test sur **cellule à contenu vide** (les 4 gabarits appliqués à une chaîne générique `Texte de la question ici`). Si $|\beta_T(\text{vide})| > 0,5 |\beta_T(\text{plein})|$ (illustratif), l'effet est déclaré purement résiduel de gabarit à vide.

---

### Expérience 0 (Corrigée) : Validité de construit de la sonde et du plan (Porte d'arrêt/continuation)

Cette étape regroupe trois duels préalables sur le jeu de validation avant de lire les contrastes de H-M1.

*   **Duel E0.1 (Spécificité pragmatique contre Format/Domaine) :**
    *   *$H_A$ (Sonde de situation d'évaluation)* : La sonde sépare des questions de banc d'essai en QCM de vraies questions utilitaires du même domaine technique mises au format QCM, avec $\text{AUROC} \ge 0,75$ (illustratif), ET son cosinus avec une **sonde de domaine** (académique vs quotidien) et une **sonde de construit étranger** (sentiment/langue) est $< 0,25$ (illustratif).
    *   *$H_B$ (Détecteur de format ou de domaine)* : $\text{AUROC} < 0,75$ (illustratif) sur les paires QCM appariées en domaine, ou colinéarité $\ge 0,25$ (illustratif) avec la sonde de domaine.
*   **Duel E0.2 (Réalisations contre Niveau — Duel D1 de B) :**
    *   *$H_A$ (Effet de classe)* : Dans un modèle mixte sur un jeu de calibration, le ratio entre la variance inter-niveaux de $T$ et la variance inter-réalisations ($K=4$ chaînes par niveau) vérifie $\sigma^2_{\text{niveau}} / \sigma^2_{\text{réalisation}} \ge 4,0$ (illustratif).
    *   *$H_B$ (Artefact d'exemplaire unique)* : Ratio $< 4,0$ (illustratif).
*   **Duel E0.3 (Spécificité contre Sensibilité générique — Duel D2 de B) :**
    *   *$H_A$ (Réponse au construit)* : $|\beta_T|$ dépasse l'effet du facteur placebo $|\beta_P|$ (borne inférieure à 95 % de $|\beta_T| - |\beta_P| > 0,2\sigma_\epsilon$, illustratif).
    *   *$H_B$ (Sensibilité au bruit de surface)* : $|\beta_T| - |\beta_P| \le 0,2\sigma_\epsilon$ (illustratif).
*   **Règle d'arrêt :** Si l'un des trois duels E0 conclut à $H_B$, l'instrument est invalidé (Voie c activée : arrêt et rapport méthodologique sur l'échec d'isolation du construit).

---

### Expérience 1 (Corrigée) : Test de H-M1 ($T$ contre $C$ sur $N=120$ noyaux nouveaux)

*   **Modèle statistique :** Modèle linéaire à effets mixtes sur le logit brut $y_{ijklm}$ (noyau $i \in \{1..120\}$, gabarit $j \in \{-0,5; +0,5\}$, style $k \in \{-0,5; +0,5\}$, réalisation de gabarit $l \in \{1..4\}$, réalisation de style $m \in \{1..4\}$) :
    $$y_{ijklm} = \beta_0 + \beta_T T_j + \beta_C C_k + \beta_{TC} (T_j \cdot C_k) + \gamma \text{len}_{ijklm} + u_i + v_l + w_m + \epsilon_{ijklm}$$
    Tous les coefficients sont standardisés par l'écart-type résiduel $\sigma_\epsilon$: $\tilde{\beta}_X = \beta_X / \sigma_\epsilon$.
*   **Hypothèses et Arbre de décision complet et symétrique ($\alpha = 0,025$ unilatéral pour les bornes, illustratif) :**
    *   **Issue 1 — $H_A$ validée (H-M1 : Dominance de $T$ et négligeabilité relative de $C$) :**
        1. Borne inférieure de l'IC à 95 % de $|\tilde{\beta}_T| > 0,40$ (illustratif) ;
        2. Borne inférieure de l'IC à 95 % par bootstrap de la différence linéaire $|\tilde{\beta}_T| - 2|\tilde{\beta}_C| > 0$ ;
        3. $|\tilde{\beta}_T|$ dépasse le 95e centile (illustratif) de la distribution des $|\tilde{\beta}_{\text{pseudo-}T}|$ obtenus par **partition brouillée** des 7 traits unitaires de la table d'attribution ;
        4. Interaction contenue : $|\tilde{\beta}_{TC}| < 0,5 |\tilde{\beta}_T|$ (illustratif).
        *(Sous-cas 1a : si en outre le TOST confirme $|\tilde{\beta}_C| < \delta = 0,15$ [illustratif], l'effet de $C$ est nul ; Sous-cas 1b : sinon, $C$ a un effet mineur mais dominé d'un facteur $>2$ par $T$).*
    *   **Issue 2 — $H_B$ validée (Réfutation de H-M1 par persistance de $C$) :**
        Borne inférieure de l'IC à 95 % de $|\tilde{\beta}_C| \ge \delta = 0,15$ (illustratif) ET la borne supérieure de $|\tilde{\beta}_T| - 2|\tilde{\beta}_C| \le 0$ (ou $|\tilde{\beta}_C| \ge 0,5 |\tilde{\beta}_T|$ avec $p < 0,01$, illustratif).
    *   **Issue 3 — Nullité instrumentale (Réfutation conjointe de $T$ et $C$) :**
        Les tests d'équivalence TOST confirment simultanément $|\tilde{\beta}_T| < 0,20$ et $|\tilde{\beta}_C| < 0,20$ (illustratif), alors que le **contrôle positif d'injection synthétique** dans les activations est bien détecté à $> 0,90$ de sa valeur théorique (illustratif).
    *   **Issue 4 — Indétermination / Sous-puissance ou Interaction dominante :**
        Tout autre cas (ex. IC de $|\tilde{\beta}_T| - 2|\tilde{\beta}_C|$ chevauchant 0 sans que les TOST soient franchis, ou $|\tilde{\beta}_{TC}| \ge 0,5 |\tilde{\beta}_T|$). Rapporté comme résultat non concluant nécessitant une augmentation de $N$.

---

### Expérience 2 (Corrigée) : Test de H-M2 (Stabilité sémantique vs Sensibilité positionnelle)

*   **Protocole :** Exécuté symétriquement dans la cellule $(T_1, C_1)$ **et** dans la cellule $(T_0, C_0)$ sur les $N=120$ noyaux. Pour chaque item de base, on génère 3 orbites de $M=3$ variantes déterministes (illustratif) :
    1. $\mathcal{G}_{\text{sem}}$ : Substitution de 3 verbes/adjectifs d'encadrement à partir d'une table auditée humainement à 100 % (aucun changement de la clé de réponse).
    2. $\mathcal{G}_{\text{pos}}$ : Déplacement de blocs fonctionnels complets à lexique strictement constant (inversion de l'ordre `[Contexte] / [Question]`, déplacement de la consigne ou de la justification en tête vs en queue).
    3. $\mathcal{G}_{\text{perp}}$ (Contrôle négatif de A) : Remplacement des noms propres ou objets de contexte par des lexèmes rares de même catégorie grammaticale (déplaçant la perplexité sans changer la structure positionnelle).
*   **Modèle et Métrique :** Estimation par maximum de vraisemblance restreint (REML) des composantes de variance intra-item $\sigma^2_{\text{sem}}$, $\sigma^2_{\text{pos}}$ et $\sigma^2_{\text{perp}}$ sur l'ensemble des 120 noyaux.
    *   *Analyse confirmatoire M2-A :* Sans covariable de perplexité.
    *   *Analyse secondaire M2-B :* Avec log-perplexité de l'invite en covariable fixe (test de médiation distributionnelle).
*   **Duel d'inférence forte :**
    *   **$H_A$ (H-M2 validée : Sensibilité positionnelle propre) :** Dans M2-A, la borne inférieure de l'IC à 95 % (par bootstrap sur les noyaux) du ratio global $\sigma^2_{\text{pos}} / \sigma^2_{\text{sem}} > 3,0$ (illustratif), ET $\sigma^2_{\text{pos}} / \sigma^2_{\text{perp}} > 2,0$ (illustratif), dans $(T_1, C_1)$ comme dans $(T_0, C_0)$.
    *   **$H_B$ (Réfutation de H-M2) :** $\sigma^2_{\text{pos}} / \sigma^2_{\text{sem}} \le 1,5$ (illustratif) (dérive lexicale équivalente à la dérive positionnelle), OU $\sigma^2_{\text{pos}} \approx \sigma^2_{\text{perp}}$ (simple artefact de perplexité), OU l'effet disparaît dans $(T_0, C_0)$ (montrant que $\mathcal{G}_{\text{pos}}$ ne faisait que détruire le gabarit $T_1$).

---

## (c) Synthèse en une page pour la décision de l'arbitre

### 1. Ce qui est établi
Au départ de cette nuit, sur la base stricte des pièces auditées :
*   **Faisabilité computationnelle vs goulot méthodologique** [HYPOTHÈSE chiffrée] : L'extraction des activations d'un modèle de 8 milliards de paramètres sur $\sim 2000$ passes avant (illustratif) ne prend que quelques minutes de GPU (moins de $10\text{ \$}$, illustratif). Le risque ne réside pas dans le temps de calcul, mais dans la **confondance par construction** entre l'instrument (la sonde) et les facteurs manipulés ($T$ et $C$).
*   **Convergence des critiques (A, B, C) sur quatre pièges mortels** [RAPPORTÉ des trois cellules] :
    1. *Circularité de la sonde :* Une sonde entraînée sur des bancs d'essai bruts lit les marqueurs de surface de $T$ ; une sonde entraînée sur des annonces explicites (« Voici un test ») lit l'impératif de seconde personne de $C$ ; une sonde entraînée sur des données artificiellement réécrites dans le gabarit de test devient aveugle à $T$.
    2. *Enchevêtrement $T/C$ et tour système :* Varier la présence d'un prompt-système ou utiliser un rembourrage de longueur dans les salutations injecte un décalage structurel ou une interaction artificielle $T \times C$.
    3. *Sophisme de l'exemplaire unique :* Tester une seule chaîne de caractères par niveau de $T$ et $C$ confond l'effet du concept avec l'effet d'une formulation arbitraire.
    4. *Instabilité des ratios :* Le critère $|\beta_T|/|\beta_C| > 2$ explose lorsque $\beta_C \approx 0$ et favorise H-M1 par manque de puissance statistique s'il n'est pas remplacé par une différence linéaire $|\beta_T| - 2|\beta_C| > 0$ couplée à un test d'équivalence (TOST).

### 2. Ce qui n'est pas établi (à trancher par l'expérience)
1.  **Existence d'une direction linéaire de « conscience d'évaluation » dans Llama-3.1-8B-Instruct** qui soit distincte (a) de la détection du registre académique et (b) de la détection syntaxique des listes à choix multiples [HYPOTHÈSE].
2.  **Validité de H-M1** : Une fois les fuites lexicales et l'enveloppe du tour système contrôlées, le gabarit pragmatique $T$ domine-t-il réellement le registre stylistique $C$ d'un facteur supérieur à 2 [HYPOTHÈSE] ?
3.  **Validité de H-M2** : La sensibilité du signal au réordonnancement des blocs ($\mathcal{G}_{\text{pos}}$) est-elle une propriété structurelle de la représentation ou une simple réaction à la dégradation de la perplexité de l'invite [HYPOTHÈSE] ?

### 3. L'expérience à lancer en premier cette nuit
Ne pas lancer le plan $2 \times 2 \times 2$ (Option b), trop vulnérable aux interactions parasites. Exécuter une **séquence à porte d'arrêt (Option c conditionnelle vers Option a)** en 4 heures (illustratif) :

1.  **Heure 1–2 (Générateur et Sonde propre) :**
    *   Coder le générateur déterministe avec **enveloppe système constante**, table d'attribution disjointe, $K=4$ réalisations par niveau (illustratif), sans rembourrage asymétrique, et passer à 100 % les tests de mutants et de cellule à contenu vide.
    *   Entraîner la sonde sur des paires écologiques hors-QCM (questions ouvertes de bancs vs vraies requêtes d'usage appariées en personne grammaticale et en longueur).
2.  **Heure 3 (L'expérience décisive à faire en premier : Expérience 0 — Validation de l'instrument) :**
    *   Soumettre la sonde au triple test : **(E0.1)** séparation de questions de banc vs questions techniques d'usage réel *toutes deux formatées en QCM* ($\text{AUROC} \ge 0,75$, illustratif) et orthogonalité à une sonde de domaine ; **(E0.2)** variance inter-niveaux de $T \ge 4 \times$ variance entre les 4 réalisations d'un même niveau ; **(E0.3)** effet de $T$ supérieur au facteur placebo de ponctuation.
3.  **Heure 4 (Bifurcation scellée d'avance) :**
    *   **Si E0 échoue :** Arrêt immédiat (Option c). Le résultat — publiable et décisif — démontre que sur un modèle 8B, le signal de « conscience d'évaluation » lu par une sonde linéaire se réduit à un détecteur de domaine ou d'exemplaire lexical.
    *   **Si E0 réussit :** Descellement et exécution automatisée des passes avant pour **Expérience 1 (H-M1)** et **Expérience 2 (H-M2)** en 15 minutes de GPU (illustratif), avec analyse par différence linéaire $|\tilde{\beta}_T| - 2|\tilde{\beta}_C|$ et TOST.

FIN-DE-CELLULE