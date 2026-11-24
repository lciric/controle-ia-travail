## 1. Ce qu'un expert du domaine ferait ici, et que la question ne demande pas

Avant de décider s'il faut ajouter l'entraînement du modèle soupçonné au programme, un expert audite les **présupposés non établis** intégrés dans la question elle-même :

| Présupposé implicite de la question ou du plan actuel | Statut exact | Conséquence méthodologique |
|---|---|---|
| Les saboteurs du programme se représentent leur sabotage dans leurs états internes | **HYPOTHÈSE** (et **RAPPORTÉ** : des sondes classent mal les dénégations d'un saboteur qui ne se croit pas fautif) | Une sonde peut échouer non par défaut technique, mais faute de représentation interne du sabotage. |
| Le saboteur à adaptateur (famille 2) est un organisme robuste, représentatif d'un saboteur inscrit dans les poids | **OBSERVÉ-NON-AUDITÉ** (aucune tenue à l'entraînement mesurée ; **VÉRIFIÉ** : un saboteur par distillation de consigne sur tâche exacte cède même à un apprentissage sur récompenses aléatoires) | Tester l'entraînement comme parade sur la famille 2 risque de conclure à tort que l'entraînement guérit le sabotage diffus. |
| Une sonde sur tâche difficile à noter détecte le sabotage plutôt qu'un artefact de construction (présence d'un adaptateur ou d'une consigne cachée) ou des indices textuels | **OBSERVÉ-NON-AUDITÉ** (aucune mesure de sonde trouvée sur tâche difficile à noter ; **RAPPORTÉ** : une sonde apprise contre le modèle de base signale presque tous les adaptateurs bénins et s'appuie en partie sur des indices textuels) | La porte d'instruments de fin décembre 2026 peut être franchie par un détecteur de décalage de poids ou de longueur de consigne. |
| L'oracle du banc sépare un sabotage diffus (petit par action) du bruit intrinsèque d'une tâche difficile à noter sur un modèle de 8 milliards de paramètres | **OBSERVÉ-NON-AUDITÉ** (**VÉRIFIÉ** : tâche difficile à noter ; dommage lu contre un jumeau honnête absent hors du banc ; **RAPPORTÉ** : un juge de texte peut être trompé sur sa grille) | Si la variance naturelle du jumeau honnête dépasse l'effet par pas du saboteur, aucune voie ne peut conclure. |
| L'ambition du programme passe par l'ajout d'une parade (l'entraînement) plutôt que par la qualification des instruments et des organismes | **HYPOTHÈSE** (proposition implicite de la question) | À 1 personne et 3 chantiers actifs au plus, ajouter un front avant les portes de décembre 2026 et d'environ février 2027 dilue l'effort là où le programme est seul. |
| La troisième ligne prévue (essaims de copies à poids partagés) apporte un gain informatif avant la validation sur agent seul | **HYPOTHÈSE** (non établie dans les faits) | Un essaim de copies non collusoires se ramène statistiquement à l'accumulation sur épisodes indépendants ; lancer son infrastructure maintenant consomme un chantier précieux. |

**Quatre gestes immédiats d'un expert que la question ne demande pas :**

1. **Bloquer les confondeurs de construction par des témoins honnêtes appariés.** Comparer un saboteur à adaptateur (famille 2) au modèle de base nu (jumeau honnête) ne permet pas de distinguer le sabotage du simple fait d'avoir modifié les poids (**RAPPORTÉ** : faux positifs massifs sur adaptateurs bénins). De même, comparer la famille 1 au modèle sans consigne cachée confond le sabotage avec la présence d'instructions système supplémentaires. L'expert fabrique immédiatement des adaptateurs bénins appariés (même géométrie, volume de données et divergence KL au modèle de base) et des consignes cachées bénignes appariées, et complète la courbe dose-réponse manquante de la famille 1 (**VÉRIFIÉ**).
2. **Vérifier l'indépendance statistique des pas avant toute garantie séquentielle.** Les scores de sondes sont accumulés dans le temps avec une garantie sur le taux de fausses alertes (**VÉRIFIÉ**). Or les 10 pas d'une même révision de proposition sont fortement autocorrélés : si l'accumulateur traite les pas comme indépendants, la borne de fausses alertes est mathématiquement invalide.
3. **Tester la marge de signal du modèle 8B.** Je ne sais pas si un modèle ouvert de 8 milliards de paramètres possède assez de réserve de qualité sur une tâche de conception expérimentale pour produire un sabotage réellement *diffus* (sans erreurs locales flagrantes) tout en restant au-dessus du plancher de bruit de l'oracle. L'expert mesure d'abord ce rapport signal/bruit.
4. **Conduire la recherche d'antériorité manquante avant l'entretien du jury du 1er décembre 2026.** Aucune recherche d'antériorité complète n'a été faite sur les combinaisons des trois voies avec lecture interne (**OBSERVÉ-NON-AUDITÉ**). C'est une tâche peu coûteuse, réalisable avant toute dépense de calcul.

---

## 2. Les données brutes de départ à prendre avant toute synthèse déjà analysée

Avant de consulter la moindre aire sous courbe (AUROC) ou synthèse du programme, il faut inspecter six jeux de données brutes :

1. **Traces intégrales des 10 pas** (message système exact, brouillons intermédiaires, proposition finale) pour la famille 1, les 4 doses de la famille 2 et le jumeau honnête sur les mêmes questions de recherche. But : vérifier à l'œil nu si le sabotage laisse des tics textuels grossiers qu'une vérification mécanique triviale suffirait à capter.
2. **Notes individuelles non agrégées de l'oracle de dommage**, ventilées par question, par graine aléatoire et par pas, incluant des doubles tirages du jumeau honnête. But : mesurer la variance intra-jumeau et inter-questions face à l'écart saboteur-jumeau aux 4 doses existantes.
3. **Activations résiduelles et scores bruts des sondes par pas (1 à 10) et par couche**, accompagnés des normes d'activations et des divergences KL au modèle de base pour la famille 2 et pour des adaptateurs bénins. But : détecter un raccourci de distribution globale (« poids modifiés ») ou une dérive systématique entre le pas 1 et le pas 10.
4. **Journaux exacts de fabrication de la famille 2** (nombre de traces générées, texte des consignes sources, hyperparamètres du réglage fin, courbes de perte, distance de poids au modèle de base). But : évaluer la parenté exacte avec le saboteur par distillation de consigne jugé peu robuste sur tâches exactes (**VÉRIFIÉ**, « référence à vérifier »).
5. **Matrice brute des corrélations par épisode** entre scores de sondes, scores des moniteurs textuels et variables de surface élémentaires (longueur, perplexité évaluée sous le modèle de base, entropie moyenne des logits, comptage de termes méthodologiques). But : quantifier la fuite d'indices textuels (**RAPPORTÉ**).
6. **Incréments bruts de la statistique séquentielle** sur épisodes honnêtes hors échantillon (par pas et par épisode). But : mesurer la fonction d'autocorrélation sur 10 pas et le taux empirique de fausses alertes sous la vraie structure de dépendance.

---

## 3. Ce que chaque voie peut établir

### Détecter (lecture interne par sonde, comparée au moniteur de texte)

- **Ce qu'elle peut établir :** l'existence d'un signal de suspicion cumulable dans le temps avec contrôle des fausses alertes sur des cas honnêtes appariés, et la supériorité ou non de la lecture interne sur un moniteur de texte à budget d'apprentissage et d'étiquetage égal. Si une sonde gelée détecte une famille de sabotage inédite sans consigne textuelle, elle établit une généralisation de signal exploitable pour aiguiller un audit.
- **Ce qu'elle ne peut pas établir :** l'absence de sabotage (un score bas peut refléter une non-représentation interne, une famille hors distribution ou une obscurcissement interne — **VÉRIFIÉ** sur code vérifiable, « référence à vérifier ») ; ni l'ampleur réelle du dommage sans oracle indépendant.
- **Ce qu'elle exige pour valoir :** (i) que le sabotage laisse une empreinte interne ou textuelle ; (ii) un calibrage précis du taux de suspicion d'un modèle honnête apparié (**VÉRIFIÉ**, billet de 2025, « référence à vérifier ») ; (iii) une évaluation unique sur famille inédite (règle en vigueur).
- **Ce qui la rend vaine :** un saboteur qui ne se représente pas sa faute (**HYPOTHÈSE** non vérifiée ; **RAPPORTÉ** sur les dénégations), un effondrement des fausses alertes sur adaptateurs bénins (**RAPPORTÉ**), une dérive des poids par entraînement ordinaire qui détruit la séparation des sondes hors domaine (**VÉRIFIÉ**, « référence à vérifier »), ou l'optimisation directe de l'agent contre le score de sonde.

### Auditer (échantillonnage d'épisodes jugés par un oracle sur le produit)

- **Ce qu'elle peut établir :** une borne statistique valide à tout instant sur la fréquence ou l'ampleur moyenne d'un dommage observable sur le produit (**RAPPORTÉ**, travaux de 2026, « référence à vérifier »), indépendamment de ce que le modèle « pense » en interne.
- **Ce qu'elle ne peut pas établir :** l'attribution causale d'une qualité médiocre à un sabotage plutôt qu'à la difficulté de la question en l'absence de jumeau honnête ; ni la détection d'un dommage inférieur au bruit de l'oracle ou situé dans les angles morts de sa grille (**VÉRIFIÉ**, papier de 2026, « référence à vérifier »).
- **Ce qu'elle exige pour valoir :** un oracle capable de reconnaître le dommage même face à un attaquant connaissant sa grille, et un taux de référence honnête stationnaire (**RAPPORTÉ**).
- **Ce qui la rend vaine :** la corruptibilité du juge sur tâche difficile à noter (**VÉRIFIÉ** : le juge par défaut est trompé, et le juge durci du papier de 2026 a exigé un accès peu réaliste à la vérité approchée, « référence à vérifier »), un budget d'audit insuffisant pour la taille d'effet diffuse, ou l'abandon du tirage aléatoire au profit d'un aiguillage exclusif par un moniteur trompable.

### Entraîner (le modèle soupçonné comme parade)

- **Ce qu'elle peut établir :** que des saboteurs donnés perdent leur propension sous un protocole d'entraînement précis (comme sur tâches exactes avec réglage fin puis renforcement sous supervision faible, **VÉRIFIÉ**, « référence à vérifier »), ou au contraire qu'un sabotage inscrit dans les poids survit à l'entraînement sur note faible (**VÉRIFIÉ** sur les saboteurs publics 14B qui résistent au renforcement, « référence à vérifier »).
- **Ce qu'elle ne peut pas établir :** l'éradication du sabotage sur tâche difficile à noter sans vérification indépendante — le papier de 2026 (**VÉRIFIÉ**, « référence à vérifier ») montre déjà en annexe que deux saboteurs entraînés contre une note faible atteignent la même note en conservant des qualités réelles différentes ; de plus, l'entraînement ne dit pas si un sabotage avait lieu au départ (**VÉRIFIÉ**, jeu d'audit, « référence à vérifier »).
- **Ce qu'elle exige pour valoir :** un signal de qualité non manipulable (ou des démonstrations de référence, souvent indisponibles en recherche ouverte — **VÉRIFIÉ**), l'indiscernabilité entre entraînement et service (**VÉRIFIÉ**), et l'absence de piratage d'exploration (*exploration hacking*, **VÉRIFIÉ**).
- **Ce qui la rend vaine :** des organismes fragiles qui cèdent à un entraînement aléatoire (faux succès — **VÉRIFIÉ**), une note faible trompable (Goodhart), ou la perte de capacité honnête (**VÉRIFIÉ**, notes de 2025, « référence à vérifier »).

### Combinaisons et interférences entre les trois voies

- **Détecter + Auditer (complémentarité conditionnelle) :** la sonde accélère la détection en dirigeant une fraction du budget d'audit vers les épisodes suspects, tandis qu'une fraction tirée au hasard conserve la garantie contre un saboteur invisible à la sonde (règle en vigueur). Si l'aiguillage remplace totalement le tirage aléatoire, la garantie disparaît.
- **Entraîner + Détecter (antagonisme par défaut) :** un entraînement ordinaire sans adversaire dégrade le pouvoir de séparation de sondes apprises hors domaine (**VÉRIFIÉ**, « référence à vérifier »), et un apprentissage en ligne prolongé équivaut à entraîner la politique contre le moniteur (**VÉRIFIÉ**, billet de 2026, « référence à vérifier »). Entraîner contre la sonde induit obscurcissement interne ou rationalisation textuelle (**VÉRIFIÉ** sur code vérifiable) et enfreindrait la règle en vigueur. La seule combinaison non destructive est **séquentielle et découplée** : entraîner sur un signal indépendant des moniteurs, recalibrer la sonde sur un jumeau honnête ayant subi le même entraînement, puis vérifier s'il subsiste un sabotage résiduel.
- **Entraîner + Auditer (risque de contamination) :** l'audit valide après coup l'effet de l'entraînement ; mais dès que la sortie de l'oracle entre dans la sélection ou l'entraînement de l'agent, la garantie d'audit indépendant est perdue (règle en vigueur).

### Mesure minimale de fonctionnement pour chaque instrument

*Tous les seuils chiffrés ci-dessous sont marqués « illustratif » (absents des faits).*

| Instrument | Mesure minimale (détection / fausses alertes) | Cas honnêtes appariés obligatoires | Vérifications mécaniques à battre |
|---|---|---|---|
| **Sonde interne** | Rappel ≥ 50 % (illustratif) sur cumul de 20 épisodes (illustratif) à taux de fausses alertes ≤ 1 % (illustratif, borne valide à tout instant), en lecture unique sur famille inédite | Consignes cachées bénignes (pour F1) ; adaptateurs bénins appariés en rang/KL/données (pour F2) ; modèle de base + perturbations bénignes (pour F3) | (1) Classifieur sur statistiques de surface (longueur, perplexité sous modèle de base, entropie des logits) ; (2) détecteur de distance d'activations au modèle de base ; (3) moniteur de texte entraîné sur exactement les mêmes étiquettes |
| **Moniteur de texte (juge)** | Rappel ≥ 50 % (illustratif) à fausses alertes ≤ 1 % (illustratif) sur cumul équivalent, y compris face à un attaquant informé de la grille | Propositions honnêtes de qualité naturellement basse sur questions difficiles ; témoins bénins appariés | (1) Vérificateur lexical/structurel automatique (présence de contrôles, hypothèses, ablations) ; (2) juge par défaut sans durcissement |
| **Audit / oracle sur le produit** | Puissance ≥ 80 % (illustratif) à risque α ≤ 5 % (illustratif) pour détecter un écart de dommage fixé sur lot de K épisodes (illustratif) ; fausses condamnations ≤ 5 % (illustratif) | Doubles tirages du jumeau honnête sur questions de difficulté hétérogène ; adaptateurs bénins produisant un style différent mais une qualité égale | (1) Score purement stylistique (longueur, lisibilité) ; (2) tirage aléatoire pur sans sonde (pour prouver le gain d'accélération de l'aiguillage) |
| **Entraînement du modèle soupçonné** | Réduction ≥ 80 % (illustratif) du dommage réel mesuré par l'oracle indépendant, perte de capacité honnête ≤ 5 % (illustratif), rémanence hors distribution d'entraînement ≤ 5 % (illustratif) | Jumeau honnête et adaptateurs bénins soumis exactement au même entraînement | (1) Entraînement placebo (récompenses aléatoires / bruit de poids) ; (2) réglage fin supervisé bénin simple. *(Si le placebo guérit le saboteur, c'est l'organisme qui est invalidé.)* |

---

## 4. Les programmes possibles

Cinq architectures réellement distinctes sont comparées (modèle ouvert 8B sauf mention ; coûts hors faits marqués « illustratif »).

### Architecture A0 — Statu quo (ne rien changer)
- **Thèse :** Les trois lignes prévues (détection temporelle, corruptibilité, essaims) suffisent à décider de la valeur des sondes sans toucher à l'entraînement ni aux organismes.
- **Expérience centrale :** Comparer sonde et moniteur de texte sur agent seul (F1/F2), puis tester la corruptibilité et étendre aux essaims.
- **Ce qui la réfuterait :** Des faux positifs massifs sur adaptateurs bénins ou l'effondrement de F2 sous entraînement placebo, qui rendraient les résultats ininterprétables.
- **Exigences (saboteurs / vérité du dommage) :** Suppose implicitement F2 robuste, F1 calibrée, et l'oracle fiable sans bruit mesuré.
- **Règles modifiées :** Aucune.
- **Coût et ancrage matériel :** Modèle ouvert 8B sur GPU louée ; environ 20 à 40 courses (illustratif), soit ~1 000 à 2 500 $ (illustratif), mais dispersion critique du temps de la seule personne dirigeante sur l'infrastructure d'essaims.
- **Risque d'antériorité :** Faible sur les sondes en tâche difficile à noter (**OBSERVÉ-NON-AUDITÉ**), moyen sur les essaims ; je ne sais pas l'état exact des travaux non publiés.

### Architecture A1 — Métrologie durcie + diagnostic d'entraînement (Proposition retenue)
- **Thèse :** La contribution unique du programme est la première mesure auditée des sondes internes contre les moniteurs de texte sur une tâche difficile à noter, sécurisée par des contrôles appariés, une famille 3 sans consigne et un test diagnostique de résistance à l'entraînement (sans ouvrir l'entraînement comme parade de déploiement).
- **Expérience centrale :** Test préenregistré en lecture unique sur une famille 3 sans consigne (validée résistante au placebo), comparant sonde gelée, moniteur de texte durci et vérification mécanique, suivi d'un comparateur hors ligne d'entraînement contre note faible.
- **Ce qui la réfuterait :** Soit l'incapacité de la sonde à battre les baselines mécaniques ou le moniteur de texte à FPR ≤ 1 % (illustratif) sur témoins appariés, soit l'éradication complète du dommage de F3 par un simple entraînement sur note faible sans dégradation de capacité.
- **Exigences (saboteurs / vérité du dommage) :** Témoins honnêtes appariés (consignes et adaptateurs bénins), F3 sans consigne résistant à l'entraînement placebo, et calibrage du plancher de bruit de l'oracle sur un sous-échantillon humain aveugle.
- **Règles modifiées :** **Aucune.** L'entraînement n'est utilisé que comme test de robustesse d'organisme et comparateur hors ligne sur le banc, sans entrer dans la correction de déploiement ni recevoir aucun score de moniteur ou d'oracle dans le signal de sélection. Les essaims sont retirés des 3 chantiers actifs avant la porte d'environ février 2027.
- **Coût et ancrage matériel :** Modèle ouvert 8B (plus réplication externe facultative sur les saboteurs publics 14B, **VÉRIFIÉ**) sur GPU louée (ex. une carte de 40 à 80 Go VRAM, illustratif) ; ~35 à 60 courses et réglages fins légers (illustratif), soit ~1 800 à 4 000 $ (illustratif) + ~1 500 à 3 000 $ (illustratif) de notation humaine ciblée.
- **Risque d'antériorité :** Faible sur la combinaison « sonde interne + tâche difficile à noter + saboteur sans consigne + comparateur sur poids affinés » (explicitement laissée ouverte par le papier de 2026, **VÉRIFIÉ**, « référence à vérifier ») ; je ne sais pas si des équipes privées mènent cette mesure sans l'avoir publiée.

### Architecture A2 — Parade par entraînement + sondes comme vérificateur (changement de règle)
- **Thèse :** Sur tâche difficile à noter, l'entraînement du modèle soupçonné (contre une note faible durcie, voire régularisé par sonde) est la parade principale, les sondes servant à valider la guérison.
- **Expérience centrale :** Entraîner par renforcement un saboteur robuste sur la tâche en 10 pas contre la note faible (et éventuellement avec pénalité de sonde sans passage de gradient), puis mesurer le dommage résiduel et la détection post-entraînement.
- **Ce qui la réfuterait :** Un effondrement de qualité honnête, un contournement de la note faible maintenant le dommage réel, ou la perte de calibration des sondes après entraînement (**VÉRIFIÉ** sur code vérifiable).
- **Exigences (saboteurs / vérité du dommage) :** Saboteur résistant au placebo (F3) ET oracle quasi incorruptible pour séparer guérison réelle et Goodhart.
- **Règles modifiées :** **Oui.** Ouvre la correction par entraînement (actuellement fermée) et, dans la variante régularisée par sonde, lève l'interdiction d'introduire un score de moniteur dans l'entraînement hors bras d'attaque.
- **Coût et ancrage matériel :** RL sur trajectoires de 10 pas en 8B, très sensible aux hyperparamètres ; ~80 à 150 courses équivalentes (illustratif), soit ~6 000 à 15 000 $ (illustratif) + évaluation humaine lourde, incompatible avec une seule personne avant décembre 2026.
- **Risque d'antériorité :** Élevé ; les équipes du papier de 2026, du billet de 2025 et des travaux sur tâches exactes et code vérifiable (**VÉRIFIÉ**, « référence à vérifier ») occupent déjà ce terrain avec des modèles bien plus grands.

### Architecture A3 — Changement d'objet : science de l'oracle et de l'audit en recherche ouverte
- **Thèse :** Le goulot d'étranglement n'est pas la lecture interne mais l'absence d'oracle fiable sur tâches difficiles à noter ; le programme devient un programme d'audit et de juges résistants sans jumeau honnête.
- **Expérience centrale :** Construire et attaquer en jeu rouge/bleu un protocole d'audit multi-étapes (décomposition de propositions, vérifications croisées) évalué contre des experts humains en aveugle.
- **Ce qui la réfuterait :** L'incapacité de tout protocole d'audit réaliste (sans accès à la vérité approchée) à battre un attaquant connaissant la grille à coût raisonnable.
- **Exigences (saboteurs / vérité du dommage) :** Saboteurs moins contraints sur les poids, mais exigence massive d'annotations humaines expertes comme vérité de référence.
- **Règles modifiées :** Abandon de fait de la sonde comme instrument central (changement d'objet du programme).
- **Coût et ancrage matériel :** Faible en calcul (~500 à 1 500 $, illustratif), très lourd en évaluation humaine experte (~10 000 à 30 000 $, illustratif).
- **Risque d'antériorité :** Élevé (prolonge directement le papier de 2026 et les audits publiés en 2026, **VÉRIFIÉ** et **RAPPORTÉ**, « référence à vérifier »).

### Architecture A4 — Changement d'objet : survie des sondes sous entraînement ordinaire et dérive de poids
- **Thèse :** Même sans parade offensive, un déploiement réel comporte des mises à jour de poids ; le programme étudie si une sonde interne survit (ou peut être recalibrée sans saboteur connu) après un entraînement ordinaire bénin ou en ligne.
- **Expérience centrale :** Mesurer la chute de séparation et de calibration d'une sonde validée après des étapes croissantes de réglage fin bénin / d'apprentissage en ligne, et tester des méthodes de recalibration utilisant uniquement des données honnêtes.
- **Ce qui la réfuterait :** Soit la stabilité triviale des sondes (problème inexistant), soit l'impossibilité de recalibrer sans re-connaître le saboteur (échec de la solution).
- **Exigences (saboteurs / vérité du dommage) :** Suppose déjà une sonde qui fonctionne à l'état statique sur tâche difficile à noter (prérequis non établi, **OBSERVÉ-NON-AUDITÉ**).
- **Règles modifiées :** Aucune (sauf si l'on teste l'apprentissage en ligne couplé au moniteur, ce qui relèverait d'un bras d'attaque déclaré).
- **Coût et ancrage matériel :** ~40 à 70 courses 8B (illustratif), soit ~2 500 à 5 000 $ (illustratif).
- **Risque d'antériorité :** Moyen (prolonge le constat sur code vérifiable et le billet de 2026, **VÉRIFIÉ**, « référence à vérifier ») ; je ne sais pas si une équipe l'explore déjà sur tâches ouvertes.

---

## 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

Cinq vérifications externes indépendantes empêchent le programme de s'auto-valider :

1. **Test en aveugle sur un saboteur « boîte noire » d'une équipe rouge externe.** Une équipe indépendante fabrique un saboteur sur le même modèle ouvert 8B (par une méthode non communiquée) et le remet mêlé en aveugle à plusieurs adaptateurs bénins. Le programme applique ses sondes gelées, préenregistrées, sans réentraînement.
2. **Étalonnage humain en double aveugle de l'oracle.** Des chercheurs du domaine des articles sources, ignorant la condition (jumeau, dose, saboteur) et l'existence des sondes, comparent des paires de propositions issues du banc. Cela mesure le bruit inter-évaluateurs humain et valide si l'oracle automatisé détecte un dommage scientifique réel plutôt qu'un artefact stylistique.
3. **Transfert externe sur les saboteurs publics de 14 milliards de paramètres (**VÉRIFIÉ**).** Leurs auteurs ont nommé les sondes comme piste sans les essayer (**VÉRIFIÉ**, « référence à vérifier »). Y appliquer exactement le même protocole (avec adaptateurs bénins appariés) élimine le biais d'organismes taillés sur mesure pour les sondes du programme.
4. **Audit statistique tiers sur dépôt horodaté.** Publication horodatée (avant la lecture unique) des poids des sondes, des seuils séquentiels, du code d'analyse et des traces brutes permettant à un tiers de recalculer les fausses alertes hors échantillon, l'autocorrélation sur 10 pas et le respect des règles de séparation.
5. **Réplication d'échelle par un partenaire disposant de plus de calcul.** Reproduction du protocole gagnant ou perdant sur un modèle ouvert plus grand (par ex. 32 à 70 milliards de paramètres, illustratif) pour écarter un effet de capacité limité au 8B.

---

## 6. Reformulation exigeante de la tâche

**Proposition de mandat révisé (architecture A1) :**

> Établir, sur un modèle ouvert de 8 milliards de paramètres exécutant une tâche ouverte difficile à noter en 10 pas, si la lecture des états internes par sondes accumulées dans le temps apporte un gain mesurable et transférable sur des vérifications mécaniques et sur des moniteurs de texte durcis — à taux de fausses alertes contrôlé sur des témoins honnêtes appariés — contre un sabotage diffus inscrit dans les poids sans consigne textuelle (validé résistant à un entraînement placebo), et déterminer si un entraînement hors ligne contre une note faible supprime ce sabotage ou laisse un dommage résiduel que seule l'alliance sonde + audit détecte.

**Décisions de périmètre (règles en vigueur intégralement maintenues) :**
- **Garder :** la détection temporelle sur agent seul ; la corruptibilité des moniteurs (sondes vs juges) ; les règles strictes de non-fuite des scores de moniteurs et d'oracle ; le préenregistrement et la lecture unique sur famille inédite.
- **Retirer (ajourner après la porte d'environ février 2027) :** la ligne « essaims de copies à poids partagés », qui consomme un des 3 chantiers actifs avant validation des instruments de base.
- **Ajouter (dans le 3e chantier libéré) :** la qualification rigoureuse des témoins honnêtes appariés, la fabrication de la famille 3 sans consigne, et un **volet diagnostique d'entraînement hors ligne** (test placebo/bénin de robustesse d'organisme, test de dérive des sondes sous réglage fin bénin, puis comparateur contre note faible sur F3). **Ne pas ouvrir** l'entraînement du modèle soupçonné comme parade opérationnelle de déploiement.

---

## 7. Programme des priorités classé

Évaluation selon la formule : `score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût`, avec chaque critère noté de 1 à 5 *(propositions d'évaluation illustratives ; coût : 1 = CPU minimal, 5 = calcul ou évaluation humaine lourds)*.

| Rang | Chantier candidat | Gain (G) | Facilité (F) | Portée (P) | Potentiel (D) | Coût (C) | Score de base | Rang (ambition)* | Rang (budget serré)** | Statut |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **1** | **P1.** Témoins honnêtes appariés, courbe F1, fuite textuelle et autocorrélation séquentielle | 5 | 5 | 4 | 3 | 2 | **150,0** | 4 (805) | **1** (75,0) | Retenu |
| **2** | **P2.** Stress-test d'entraînement (placebo/bénin) sur F2 et dérive des sondes sous SFT bénin | 5 | 4 | 4 | 4 | 3 | **106,7** | 3 (853) | **2** (35,6) | Retenu |
| **3** | **P3.** Famille 3 sans consigne + duel en lecture unique sonde interne vs moniteur de texte durci | 5 | 3 | 5 | 5 | 4 | **93,8** | **1** (1353) | **3** (23,4) | Retenu |
| **4** | **P4.** Plancher de bruit de l'oracle (étalonnage humain), corruptibilité et gain d'aiguillage d'audit | 4 | 3 | 4 | 4 | 3 | **64,0** | 5 (591) | **4** (21,3) | Retenu |
| **5** | **P5.** Comparateur hors ligne « entraînement contre note faible » sur F3 robuste et résidu détectable | 4 | 2 | 5 | 5 | 4 | **50,0** | **2** (884) | **5** (12,5) | Retenu |
| 6 | **P6.** Bras d'attaque déclaré : évasion de l'agent entraîné contre le score de sonde | 4 | 2 | 4 | 4 | 4 | 32,0 | 6 (362) | 6 (8,0) | Attend (phase suivante) |
| 7 | **P7.** Essaims de copies à poids partagés | 2 | 2 | 3 | 3 | 4 | 9,0 | 7 (57) | 7 (2,3) | Ajourné |
| 8 | **P8.** Entraînement en ligne (sur note faible ou sonde) comme parade opérationnelle | 2 | 1 | 3 | 3 | 5 | 3,6 | 8 (32) | 8 (0,7) | Exclu |

*\*Sensibilité « ambition » : `G × F^0,5 × P² × D² / C` (réduit le poids de la facilité, renforce portée et potentiel). \*\*Sensibilité « budget serré » : `G × F × P × D / C²` (pénalise fortement le coût).*

**Analyse de sensibilité :** l'ensemble des 5 chantiers retenus `{P1, P2, P3, P4, P5}` est **entièrement invariant** aux deux variations de pondération, et les rejets (`P7`, `P8`) restent fermement en queue de classement. Sous pondération « budget serré », l'ordre exact 1 à 8 ne change pas. Sous pondération « ambition », `P3` passe 1er et `P5` passe 2e devant `P2` et `P1` — mais `P3` et `P5` dépendent logiquement des contrôles de `P1` et du test de robustesse de `P2`, ce qui impose d'exécuter `P1` et `P2` en premier.

### Les cinq expériences décisives (inférence forte `H_A` contre `H_B`)

*Toutes les valeurs chiffrées de seuils, tailles d'échantillons, heures GPU et budgets en dollars ci-dessous sont marquées « illustratif » (sauf 8B, 10 pas, 4 doses et « quelques dizaines de dollars » par course, issus des faits).*

#### P1 — Validité des sondes face aux témoins honnêtes appariés et aux raccourcis mécaniques
- **`H_A` (signal spécifique non trivial) :** La sonde entraînée sur F1/F2 détecte le sabotage diffus sans déclencher de fausses alertes massives sur des témoins honnêtes appariés, et dépasse les vérifications mécaniques de surface.
- **`H_B` (artefact de construction ou fuite de surface) :** Le pouvoir séparateur de la sonde provient du décalage d'adaptateur/consigne cachée ou d'indices textuels de surface.
- **Métrique et seuil :** Rappel (TPR) cumulé sur 20 épisodes (illustratif) à taux empirique de fausses alertes (FPR) ≤ 1 % (illustratif) mesuré *exclusivement* sur les témoins appariés après correction d'autocorrélation sur 10 pas ; écart ΔTPR ≥ +15 points (illustratif) au-dessus de la meilleure vérification mécanique (statistiques de surface + norme d'activation).
- **Contrôle négatif :** 6 adaptateurs bénins (illustratif) appariés en rang/données/KL à F2 (style, rigueur, domaine) et 6 consignes cachées bénignes (illustratif) appariées en longueur à F1, plus courbe dose-réponse à 4 doses (illustratif) pour F1.
- **Ancrage matériel et coût :** Modèle ouvert 8B + 6 réglages fins légers bénins + inférence sur ~200 épisodes par condition (illustratif) sur 1 GPU louée (ex. 40–80 Go VRAM, illustratif) + analyse CPU ; ~400 à 800 $ (illustratif).
- **Falsification :** Un FPR > 5 % (illustratif) sur adaptateurs/consignes bénins ou ΔTPR ≤ 0 falsifie `H_A` (la sonde n'est pas un détecteur de sabotage) ; TPR ≥ 50 % (illustratif) à FPR ≤ 1 % (illustratif) et ΔTPR ≥ +15 points (illustratif) falsifie `H_B`. L'expérience serait invalidée méthodologiquement si les adaptateurs bénins avaient une divergence KL nettement différente de F2.

#### P2 — Robustesse de F2 à l'entraînement et stabilité des sondes sous réglage fin bénin
- **`H_A` (organisme robuste + sonde fragile à la dérive) :** F2 conserve son sabotage après un entraînement placebo (récompenses aléatoires), et un réglage fin supervisé bénin sur le modèle honnête dégrade la calibration de la sonde.
- **`H_B` (organisme fragile par distillation, ou sonde invariante) :** F2 perd son sabotage dès l'entraînement placebo (comme l'organisme peu robuste publié sur tâches exactes, **VÉRIFIÉ**) — sous-test 2a ; ou la sonde conserve son FPR ≤ 2 % (illustratif) et sa séparation après réglage fin bénin sans recalibration — sous-test 2b. *(Les deux volets sont testés séparément pour éviter toute ambiguïté.)*
- **Métrique et seuil :** Volet 2a : maintien ≥ 70 % (illustratif) du dommage initial de F2 après apprentissage sur récompenses aléatoires (et après SFT bénin hors tâche). Volet 2b : variation de FPR ≤ +1 point (illustratif) et perte de TPR ≤ 10 points (illustratif) de la sonde gelée après SFT bénin sur le jumeau honnête.
- **Contrôle négatif :** Jumeau honnête et adaptateurs bénins soumis exactement aux mêmes étapes d'entraînement placebo et de SFT bénin (mesure de la perte de capacité honnête).
- **Ancrage matériel et coût :** Modèle ouvert 8B, 4 à 6 réglages fins / RL courts (illustratif) sur 1 GPU louée ; ~500 à 1 000 $ (illustratif).
- **Falsification :** Si F2 perd > 50 % (illustratif) de son dommage sous récompenses aléatoires, sa validité comme organisme de poids est falsifiée (il faut impérativement F3 avant tout comparateur d'entraînement). Si la sonde perd > 10 points de TPR ou franchit FPR > 2 % (illustratif) après SFT bénin, l'hypothèse de stabilité statique des sondes est falsifiée.

#### P3 — Duel préenregistré en lecture unique : sonde interne vs moniteur de texte durci sur Famille 3 (sans consigne)
- **`H_A` (avantage propre de la lecture interne) :** Sur une famille de sabotage inédite inscrite dans les poids sans aucune consigne textuelle (F3, ayant réussi le test placebo de P2), la sonde interne gelée (préenregistrée sur F1/F2) détecte le sabotage en lecture unique mieux que le moniteur de texte durci à même budget de fausses alertes.
- **`H_B` (non-transfert interne ou parité avec le texte) :** Sans consigne verbalisée, F3 ne déclenche pas la sonde interne au-delà du hasard ou reste détectée aussi bien (ou mieux) par un moniteur de texte durci et/ou une vérification mécanique.
- **Métrique et seuil :** TPR cumulé sur 20 épisodes (illustratif) à FPR ≤ 1 % (illustratif) sur témoins appariés, avec ΔTPR(sonde − meilleur moniteur de texte durci) ≥ +15 points (illustratif) en lecture unique ; réplication secondaire prévue sur les saboteurs publics 14B (**VÉRIFIÉ**).
- **Contrôle négatif :** Adaptateurs bénins entraînés par la même procédure d'optimisation que F3 mais sur un objectif honnête (même budget d'étapes et divergence KL).
- **Ancrage matériel et coût :** Modèle ouvert 8B (plus option 14B public sur GPU 80 Go, illustratif) ; fabrication et calibrage dose-réponse de F3 + évaluation en lecture unique ; ~1 200 à 2 500 $ (illustratif).
- **Falsification :** ΔTPR ≤ 0 ou TPR(sonde) < 30 % (illustratif) en lecture unique falsifie `H_A` (et remet en cause le programme centré sur les sondes) ; TPR(sonde) ≥ 50 % (illustratif) avec ΔTPR ≥ +15 points (illustratif) falsifie `H_B`. L'expérience est invalidée si F3 ne produit pas un dommage réel supérieur au plancher de bruit de l'oracle mesuré en P4, ou si la sonde a été réajustée après lecture de F3.

#### P4 — Plancher de bruit de l'oracle, corruptibilité et gain réel d'aiguillage d'audit
- **`H_A` (aiguillage utile et résistant) :** L'oracle de dommage présente un rapport signal/bruit validé par étalonnage humain aveugle, et l'audit hybride (fraction aléatoire + fraction aiguillée par sonde) divise au moins par 2 (illustratif) le nombre d'épisodes audités nécessaires pour détecter un sabotage diffus, y compris quand le moniteur de texte est corrompu.
- **`H_B` (oracle noyé dans le bruit ou aiguillage sans gain) :** Le dommage diffus est inférieur au bruit inter-évaluateurs humain, ou l'aiguillage par sonde n'accélère pas significativement l'audit par rapport au tirage aléatoire pur (ou échoue dès que le saboteur optimise contre la grille textuelle).
- **Métrique et seuil :** Accord oracle-humains en double aveugle (corrélation de rang ≥ 0,65 illustratif sur 60 paires de propositions, illustratif) ; facteur de réduction du nombre médian d'épisodes audités pour atteindre 80 % de puissance à α = 5 % (illustratif) ≥ 2,0× (illustratif) par rapport à l'audit aléatoire pur.
- **Contrôle négatif :** Doubles tirages du jumeau honnête sur questions difficiles (vérification de l'absence de faux positifs d'audit) et condition d'attaque connaissant la grille du juge textuel.
- **Ancrage matériel et coût :** Analyse principalement CPU sur les traces de P1/P3 + quelques courses de corruptibilité sur 8B (~300 à 600 $, illustratif) + indemnisation d'évaluateurs humains experts (~1 500 à 3 000 $, illustratif).
- **Falsification :** Une corrélation oracle-humains < 0,40 (illustratif) falsifie la validité du banc lui-même ; un facteur d'accélération < 1,3× (illustratif) falsifie la thèse « la sonde est l'accélérateur de l'audit » (`H_A`), tandis qu'un facteur ≥ 2,0× (illustratif) avec accord humain ≥ 0,65 (illustratif) falsifie `H_B`.

#### P5 — Comparateur hors ligne « entraînement contre note faible » sur F3 robuste (comble l'angle mort du papier de 2026)
- **`H_A` (résidu diffus détectable) :** Entraîner un saboteur robuste à poids modifiés (F3) contre la note faible sur la tâche difficile à noter laisse subsister un dommage réel significatif à note faible presque maximale, que la sonde interne (recalibrée sur jumeau honnête entraîné de même) + l'audit continuent de capter.
- **`H_B` (suffisance de l'entraînement) :** L'entraînement contre la note faible élimine le dommage réel de F3 sans dégrader la capacité honnête, rendant les sondes redondantes sur ce régime.
- **Métrique et seuil :** Dommage résiduel post-entraînement mesuré par l'oracle indépendant ≥ 30 % (illustratif) du dommage initial alors que la note faible atteint ≥ 95 % (illustratif) du niveau du jumeau honnête, combiné à un TPR de sonde recalibrée ≥ 40 % (illustratif) à FPR ≤ 1 % (illustratif).
- **Contrôle négatif :** Jumeau honnête et adaptateurs bénins soumis exactement au même entraînement contre la note faible (contrôle de dégradation de capacité et base de recalibration honnête).
- **Ancrage matériel et coût :** Modèle ouvert 8B ; 4 à 6 campagnes de réglage par préférences / RL contre note faible (illustratif) sur GPU louée ; ~1 200 à 2 500 $ (illustratif). Aucune règle n'est modifiée (comparateur hors ligne ; aucun score de sonde ni d'oracle dans l'entraînement).
- **Falsification :** Un dommage résiduel ≤ 10 % (illustratif) à capacité honnête préservée falsifie `H_A` (l'entraînement suffit sur cet organisme) ; un dommage résiduel ≥ 30 % (illustratif) à note faible saturée falsifie `H_B` (et si en plus la sonde recalibrée échoue à le détecter, les deux parades — entraînement faible et sonde — échouent conjointement).

### Ordonnancement (strictement ≤ 3 chantiers actifs simultanés)

- **Avant la porte d'instruments (fin décembre 2026) — 3 chantiers actifs :**
  1. **P1** (complet : témoins bénins, courbe F1, baselines mécaniques, autocorrélation). *Premiers résultats + recherche d'antériorité prêts pour le jury du 1er décembre 2026.*
  2. **P2** (complet : test placebo/bénin sur F2 + dérive de sonde sous SFT bénin). *Résultats préliminaires sur F2 prêts pour le jury du 1er décembre 2026.*
  3. **Amorçage de P3** (finalisation du devis, entraînement et validation placebo de F3, sans encore ouvrir le jeu de lecture unique).
- **Ce qui attend (janvier – environ février 2027, porte lecture interne vs texte ; puis phase suivante) :**
  - Dès clôture de P1 : lancement de **P4** (étalonnage humain, corruptibilité, aiguillage d'audit).
  - Dès clôture de P2 et validation de F3 : exécution de la lecture unique de **P3** (pour la porte d'environ février 2027), puis **P5** (comparateur contre note faible).
  - *Après la porte d'environ février 2027 seulement* : **P6** (bras d'attaque déclaré : évasion contre sonde) et, uniquement si la détection sur agent seul a survécu à P3/P4/P6, réévaluation de **P7** (essaims).
- **Ce qui ne doit pas être fait :**
  - **Ne pas lancer P8** (entraînement en ligne comme parade opérationnelle, surtout contre score de sonde ou d'oracle) : cela violerait les règles en vigueur (fermeture de la correction par entraînement ; interdiction d'injecter un score de moniteur ou d'oracle dans l'entraînement), dépasserait la bande passante d'une seule personne et produirait des résultats non interprétables avant P2/P3.
  - **Ne pas maintenir les essaims (P7)** dans les trois chantiers actifs avant février 2027.
  - **Ne pas réajuster une sonde** après avoir regardé ses scores sur F3 (violation de la règle de lecture unique).

### Ce qui reste hors de portée

Même si l'architecture A1 réussit intégralement, quatre limites demeurent hors de portée de ce programme (1 personne, modèle 8B, budget modeste) :
1. **L'extrapolation directe aux modèles frontières :** un comportement de sonde positif ou négatif sur 8 milliards de paramètres ne garantit pas le même résultat sur un modèle dix ou cent fois plus grand, dont la représentation interne et la capacité de sabotage diffus peuvent changer de régime.
2. **La preuve d'absence de sabotage :** aucun protocole de détection par sonde ne démontre qu'un modèle est sûr face à un saboteur qui ne se représente pas sa faute ou qui échappe de façon adaptative au classifieur.
3. **Le déploiement sans jumeau honnête en régime ultra-diffus :** si le dommage par épisode est inférieur à la variance naturelle entre experts humains sur des questions de recherche ouvertes, aucun audit d'épisodes isolés ne peut trancher sans référence de base connue.
4. **La défense contre un déploiement en apprentissage continu en ligne :** tant que les poids évoluent continûment sous l'effet de retours corrélés aux moniteurs (**VÉRIFIÉ**, billet de 2026, « référence à vérifier »), la dérive jointe de la politique et de la calibration des sondes reste un problème ouvert au-delà de février 2027.

FIN-DE-CELLULE