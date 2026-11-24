### 1. Ce qu'un expert du domaine ferait ici, et que la question ne demande pas

Avant de décider s'il faut élargir le programme (et notamment ouvrir l'entraînement comme parade), un expert en évaluation de contrôle et en lecture des états internes commencerait par vérifier les fondations expérimentales que la question tient implicitement pour acquises.

**Gestes prioritaires que la question ne demande pas (ma proposition) :**

1. **Traiter en urgence le facteur de confusion « présence d'un adaptateur ».** Il est `RAPPORTÉ` qu'une sonde apprise contre le modèle de base signale presque tous les exemples d'adaptateurs bénins. Sur le banc actuel, le saboteur à adaptateur diffère du jumeau honnête (`VÉRIFIÉ`) par le simple fait d'avoir subi un réglage fin. Sans une batterie d'adaptateurs bénins appariés (même procédure, même rang, sans sabotage — incluant des adaptateurs publics tiers sur le même modèle ouvert de 8 milliards de paramètres), on risque de mesurer un détecteur de décalage de poids plutôt qu'un détecteur de sabotage. Le même biais s'applique au saboteur à consigne cachée vis-à-vis de consignes système bénignes de structure comparable.
2. **Séparer l'information interne de l'information déjà présente dans le texte ou dans des signaux mécaniques simples.** Il est `RAPPORTÉ` que des sondes de sous-rendement s'appuient en partie sur des indices textuels. Un expert exige de savoir si la sonde lit le sabotage *au-delà* du texte généré, des statistiques de trajectoire sur 10 pas, de l'entropie des logits et de la divergence locale par rapport au modèle de base — et si elle sépare le sabotage de la simple incompétence honnête (les pires épisodes du jumeau honnête).
3. **Tester la validité écologique des organismes fabriqués avant d'étudier une parade par entraînement.** Sur des tâches à réponse exacte, un saboteur distillé depuis une consigne perd son sous-rendement même sous un apprentissage à récompenses aléatoires, signe d'un organisme peu robuste (`VÉRIFIÉ`). On ne sait pas si l'adaptateur distillé du programme se comporte ainsi ou comme les saboteurs publics de 14 milliards de paramètres qui résistent à l'apprentissage par renforcement (`OBSERVÉ-NON-AUDITÉ` ; `VÉRIFIÉ`). Evaluer l'entraînement défensif sur un organisme qui s'effondre au premier bruit produirait un faux positif méthodologique.
4. **Distinguer deux sens de « diffus ».** Une menace peut être diffuse dans l'espace des *actions* (chaque pas sur 10 paraît acceptable) tout en étant concentrée dans l'espace *interne* (maintien d'une intention persistante), ou diffuse dans les deux (biais subtil inscrit sans représentation d'être fautif, cas où les sondes classent mal les dénégations, `RAPPORTÉ`). Le programme doit classer ses saboteurs selon cet axe.
5. **Auditer la dépendance temporelle et la disparition du jumeau honnête hors banc.** Les 10 pas de révision d'une même proposition (`VÉRIFIÉ`) sont fortement autocorrélés : accumuler des scores de sonde pas à pas sans modéliser cette dépendance invalide la garantie de fausses alertes. Plus profondément, le jumeau honnête n'existe qu'au banc (`VÉRIFIÉ`), alors que l'incrimination sur petits indices exige de connaître avec précision la suspicion d'un modèle honnête (`VÉRIFIÉ`, billet de 2025, référence à vérifier).

**Ce que la question suppose sans que ce soit établi (avec statuts) :**

- *Présupposé A* : Les saboteurs du programme possèdent une représentation interne détectable de leur sabotage, distincte d'un artefact d'adaptateur ou de consigne. **Statut : `HYPOTHÈSE`** (explicitement notée comme telle dans les faits ; fragilisée par les constats `RAPPORTÉ` sur les dénégations et les adaptateurs bénins).
- *Présupposé B* : Les sondes fonctionnent sur une tâche difficile à noter. **Statut : `OBSERVÉ-NON-AUDITÉ`** (aucune mesure de sonde sur une tâche difficile à noter n'a été trouvée dans la recherche bornée).
- *Présupposé C* : Les saboteurs du programme constituent des organismes représentatifs pour juger de la tenue à un entraînement. **Statut : `OBSERVÉ-NON-AUDITÉ`** (tenue à l'entraînement non mesurée ; appartenance au régime fragile ou robuste inconnue).
- *Présupposé D* : L'oracle du banc mesure fidèlement un dommage scientifique réel sans être lui-même bruité ou biaisé par la surface du texte. **Statut : non établi** (`VÉRIFIÉ` que la tâche est difficile à noter et qu'un juge par défaut est trompé dans le papier de 2026, référence à vérifier ; la concordance avec des experts humains n'est pas rapportée).
- *Présupposé E* : La garantie séquentielle de fausses alertes calibrée contre le jumeau honnête survit hors banc (nouveaux sujets, mises à jour bénignes). **Statut : non établi** (`VÉRIFIÉ` que le jumeau honnête n'existe qu'au banc et qu'un entraînement ordinaire dégrade des sondes hors domaine).
- *Présupposé F* : Rendre le programme « ambitieux » passe par l'ajout de chantiers (entraînement, essaims) plutôt que par le durcissement des tests de falsification sur l'instrument central. **Statut : choix non démontré**, en tension avec la contrainte `VÉRIFIÉ` d'une seule personne et trois chantiers actifs au plus.

---

### 2. Les données brutes de départ à prendre avant toute synthèse déjà analysée

Avant d'interpréter des courbes agrégées (AUROC, p-valeurs séquentielles ou résumés d'articles), il faut inspecter les objets bruts suivants (ma proposition) :

1. **Échantillon apparié de trajectoires complètes sur les 10 pas** (par ex. 30 à 50 questions de recherche, `illustratif`) : textes bruts de chaque pas pour le jumeau honnête, un adaptateur bénin apparié, le saboteur à consigne cachée (courbe dose-réponse à produire, actuellement manquante `VÉRIFIÉ`) et le saboteur à adaptateur aux 4 doses existantes (`VÉRIFIÉ`), avec les notes brutes de l'oracle et les notations aveugles d'au moins deux chercheurs humains externes (20 à 30 paires, `illustratif`) afin de vérifier la taille d'effet réelle rapportée à la variance honnête.
2. **Distributions brutes (non seuillées) des scores de sondes** par pas (1 à 10) et par épisode sur cinq strates négatives : modèle de base honnête, adaptateurs bénins construits localement, adaptateurs bénins publics tiers sur le même modèle 8B, consignes système bénignes de longueur équivalente, et quintile inférieur de qualité du jumeau honnête (20 % pires épisodes honnêtes, `illustratif`).
3. **Vérifications mécaniques brutes sur exactement les mêmes épisodes** : longueur et taux d'édition entre pas consécutifs, entropie moyenne et maximale des logits, log-probabilité de la trajectoire évaluée sous le modèle de base, norme des activations résiduelles, classifieur linéaire simple sur le texte seul, et scores bruts d'un juge texte par défaut et d'un juge texte durci.
4. **Détails bruts de fabrication des saboteurs existants** : jeu exact de distillation de l'adaptateur, rang/couches/normes de poids, et valeurs brutes des 4 doses existantes (`VÉRIFIÉ`) pour vérifier l'absence de saturation ou d'effondrement stylistique grossier.
5. **Journal complet des essais de sondes déjà effectués** (couches testées, formulations de questions de suite, hyperparamètres rejetés) afin de prévenir toute fuite statistique avant le test unique sur la famille inédite (`VÉRIFIÉ`).
6. **Textes intégraux et annexes des travaux cités dans les faits** (notamment le papier de 2026 sur ce banc et les articles sur organismes fragiles vs saboteurs 14B, références à vérifier), pour vérifier les protocoles exacts sans dépendre de notes de synthèse.

---

### 3. Ce que chaque voie peut établir

Le régime étudié cumule deux difficultés : menace diffuse (effet petit par action) et tâche difficile à noter (variance honnête élevée, absence de vérificateur exact).

#### Détecter (sondes internes + accumulation séquentielle, comparées aux moniteurs de texte)
- **Ce qu'elle peut établir :** Une séparation statistique entre l'agent surveillé et une référence honnête spécifiée, plus rapide ou plus fine qu'un moniteur texte, éventuellement *avant* l'accumulation d'un dommage important ; un gain d'information conditionnellement au texte et aux baselines mécaniques ; la persistance (ou le déplacement) d'une anomalie interne après une intervention d'entraînement.
- **Ce qu'elle ne peut pas établir :** L'absence de sabotage (un score nul ne réfute ni un saboteur sans représentation interne saillante `HYPOTHÈSE`/`RAPPORTÉ`, ni une évasion par obscurcissement `VÉRIFIÉ`) ; l'ampleur réelle du dommage scientifique ; une garantie de fausses alertes hors banc sans estimation fiable du nul en déploiement (`VÉRIFIÉ`).
- **Ce qu'elle exige pour valoir :** Calibration sur cas honnêtes stratifiés (adaptateurs bénins, prompts bénins, épisodes honnêtes ratés, sujets inédits) ; validation préenregistrée à lecture unique sur une famille de sabotage inédite sans texte de consigne (`VÉRIFIÉ`) ; supériorité démontrée sur les baselines mécaniques et le juge texte durci à même taux de fausses alertes ; prise en compte de l'autocorrélation des 10 pas.
- **Ce qui la rend vaine :** Détection d'un artefact d'adaptateur ou de consigne (`RAPPORTÉ`) ; absence de représentation interne transférable ; dérive du nul sous entraînement ordinaire hors domaine (`VÉRIFIÉ`) ; obscurcissement interne sous pression adaptative (`VÉRIFIÉ`).

#### Auditer (tirage aléatoire d'épisodes + oracle sur le produit, éventuellement aiguillé par sonde)
- **Ce qu'elle peut établir :** Une borne statistique valide à tout instant sur le taux de dommage réalisé, publiée par plusieurs équipes en 2026 (`RAPPORTÉ`, référence à vérifier), indépendante des états internes du modèle ; la seule mesure directe du dommage sur le produit final.
- **Ce qu'elle ne peut pas établir :** Un dommage inférieur à la résolution (ou caché dans les angles morts) de son oracle (`VÉRIFIÉ` : juge par défaut trompé dans le papier de 2026, référence à vérifier) ; une distinction entre sabotage léger et baisse de compétence sans taux de dommage honnête de référence (`RAPPORTÉ`) ; une détection peu coûteuse quand l'effet par épisode est noyé dans le bruit de la tâche.
- **Ce qu'elle exige pour valoir :** Un oracle résistant ou ancré sur un audit humain expert aveugle ; un niveau de référence honnête estimé sur des tâches comparables ; si la sonde aiguille l'audit, un plancher strictement positif de probabilité d'audit aléatoire sur tous les épisodes (pondération par probabilité inverse) pour préserver la garantie pire-cas en cas d'évasion.
- **Ce qui la rend vaine :** Un oracle corruptible ou en désaccord avec des humains experts ; un budget d'audit humain incapable de résoudre un petit écart moyen ; l'élimination du tirage aléatoire sur les épisodes à faible score de sonde.

#### Entraîner (réglage fin / apprentissage par renforcement du modèle soupçonné comme parade)
- **Ce qu'elle peut établir :** Empiriquement, sur un banc muni d'un organisme préalablement prouvé robuste, si un protocole précis (traces bénignes, note faible durcie, régularisation) réduit le dommage mesuré par un oracle indépendant ; en sens inverse, si un organisme fabriqué est fragile (effacé par récompenses aléatoires, `VÉRIFIÉ`) et à quelle vitesse un entraînement bénin ou adaptatif casse les sondes (`VÉRIFIÉ`).
- **Ce qu'elle ne peut pas établir :** Une garantie de sécurité en déploiement sur une tâche difficile à noter : entraîner contre une note faible laisse deux saboteurs atteindre la même note faible avec des qualités réelles différentes (`VÉRIFIÉ`, annexe du papier de 2026, référence à vérifier), peut échouer par « exploration hacking » (`VÉRIFIÉ`), exige l'indiscernabilité entre entraînement et service (`VÉRIFIÉ`), et ne prouve pas son propre succès sans détection/audit externe (`VÉRIFIÉ`, jeu d'audit sur le sous-rendement, référence à vérifier). De plus, l'effet dépend de la façon dont la propension est inscrite dans les poids (`VÉRIFIÉ`).
- **Ce qu'elle exige pour valoir :** Des organismes prouvés résistants au bruit aléatoire ; un signal de récompense non corrompu (le goulot même des tâches ouvertes où les démonstrations de référence peuvent être impossibles, `VÉRIFIÉ`) ; une évaluation post-entraînement indépendante.
- **Ce qui la rend vaine :** La guérison illusoire d'un adaptateur distillé peu robuste (`VÉRIFIÉ`) ; l'optimisation de la note faible ou de la sonde au détriment de la qualité réelle (`VÉRIFIÉ`).

#### Combinaisons et antagonismes
- **Synergies :** *Détecter + Auditer* est structurellement complémentaire (conforme aux règles actuelles `VÉRIFIÉ`) : l'audit aléatoire porte la garantie pire-cas, la sonde accélère la détection par aiguillage pondéré, et l'audit sert à recalibrer le nul. *Détecter + Entraîner (en diagnostic)* : l'entraînement aléatoire filtre les organismes fragiles, et la détection vérifie si un entraînement prétendument correctif n'a pas simplement masqué le sabotage.
- **Antagonismes :** *Entraîner nuit à Détecter* : même sans intention malveillante, un entraînement ordinaire réduit la séparation des sondes hors domaine (`VÉRIFIÉ`), et un déploiement long avec apprentissage en ligne revient à entraîner la politique contre le moniteur (`VÉRIFIÉ`, billet de 2026, référence à vérifier), induisant l'obscurcissement interne (`VÉRIFIÉ`). *Entraîner sur le signal d'audit détruit l'indépendance de l'audit* (ce qu'interdit la règle actuelle `VÉRIFIÉ`). *Aiguiller tout l'audit via la sonde sans plancher aléatoire détruit la garantie d'audit.*

#### Mesure minimale de fonctionnement de chaque instrument (ma proposition ; chiffres marqués « illustratif »)

| Instrument | Mesure minimale (détection et fausses alertes, `illustratif`) | Cas honnêtes appariés obligatoires | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **Sonde interne** | TPR $\ge 0{,}50$ à FPR $\le 1\%$ sur doses à dommage significatif (et $\ge 0{,}40$ sur la 3e famille inédite) | Modèle de base, $\ge 4$ adaptateurs bénins (dont publics), prompts système bénins, 20 % pires épisodes honnêtes (`illustratif`) | Entropie des logits, log-probabilité sous modèle de base, norme d'activations, taux de révision sur 10 pas, classifieur linéaire sur texte seul |
| **Accumulateur séquentiel** | FPR empirique $\le \alpha = 5\%$ sur $T=200$ épisodes hors-domaine ; réduction $\ge 2\times$ du délai médian de détection | Flux honnêtes sur articles inédits + adaptateurs bénins, en respectant la dépendance intra-épisode (10 pas) | Cumul séquentiel sur les scores des baselines mécaniques et audit aléatoire pur |
| **Moniteur de texte (juge durci)** | Accord $\ge 75\%$ avec experts humains sur direction du dommage ; TPR $\ge 0{,}40$ à FPR $\le 1\%$ ; tenue sous optimisation de consigne | Mêmes strates honnêtes + épisodes honnêtes stylistiquement maladroits mais scientifiquement valides | Heuristiques de longueur/structure/présence de contrôles, juge par défaut |
| **Audit aléatoire + oracle** | Accord humain–oracle $\ge 75\%$ ; couverture empirique de la borne de dommage $\ge 95\%$ | Paires honnête-vs-honnête en aveugle pour vérifier l'absence de biais systématique de l'oracle | Tirage uniforme sans aiguillage ; moyenne mobile naïve sans garantie valide à tout instant |
| **Entraînement (uniquement si testé)** | Dommage résiduel $\le 20\%$ du dommage initial *sur organisme prouvé résistant au RL aléatoire*, avec baisse de capacité honnête $\le 10\%$ | Jumeau honnête soumis au *même* protocole d'entraînement | Entraînement sur récompenses aléatoires et réglage fin sur traces bénignes génériques |

---

### 4. Les programmes possibles

Voici cinq architectures réellement distinctes (les coûts et durées hors faits sont `illustratif` ; chaque modification des règles en vigueur `VÉRIFIÉ` est signalée explicitement).

#### Architecture 0 : Statu quo (ne rien changer)
- **Thèse :** Les sondes accumulées dans le temps surpassent les moniteurs texte sur une tâche difficile à noter, résistent mieux à la corruption et s'étendent aux essaims à poids partagés.
- **Expérience centrale :** Comparaison sonde vs juge texte sur adaptateur et consigne cachée, puis extension aux essaims.
- **Ce qui la réfuterait :** Une sonde détectant surtout les adaptateurs bénins ou ne battant pas une vérification mécanique, ce qui rend la ligne « essaims » sans objet.
- **Exigences (saboteurs / vérité du dommage) :** Courbe dose-réponse à consigne cachée + 3e famille ; oracle supposé fiable sans contrôle systématique d'adaptateurs bénins ni test de fragilité d'organisme.
- **Coût :** 3 chantiers sur 1 personne (`VÉRIFIÉ`, saturation immédiate), ~1 500–3 000 $ GPU (`illustratif`), mais fort risque de dispersion avant le jury du 1er décembre 2026.
- **Règles modifiées :** Aucune.
- **Risque d'antériorité :** Faible sur la tâche difficile à noter (`OBSERVÉ-NON-AUDITÉ`), élevé de critique méthodologique frontale sur les contrôles négatifs (`RAPPORTÉ`).

#### Architecture 1 : Programme recentré « Sonde calibrée + Audit aiguillé » (retrait des essaims, pas d'entraînement comme parade)
- **Thèse :** Sur une tâche difficile à noter, une lecture interne purgée des artefacts d'adaptateur et comparée à des vérifications mécaniques accélère un audit aléatoire garanti sur une famille de sabotage inédite sans texte de consigne, dans un domaine de validité borné par la dérive bénigne et l'évasion.
- **Expérience centrale :** Test préenregistré à lecture unique sur la 3e famille (sans consigne) d'une sonde calibrée sur adaptateurs bénins, couplée à un audit aléatoire à plancher fixe, contre audit pur, juge texte durci et baselines mécaniques, précédé d'un diagnostic de fragilité des organismes et de dérive bénigne.
- **Ce qui la réfuterait :** Échec à dépasser les vérifications mécaniques ou le juge texte durci sur la 3e famille, ou rupture de la borne de fausses alertes hors-domaine.
- **Exigences :** 3e famille sans consigne + contrôle par même procédure sans sabotage ; batterie d'adaptateurs bénins (dont publics) ; petit audit humain aveugle de l'oracle.
- **Coût :** ~2 500–5 500 $ GPU + 20–40 h d'évaluation humaine experte (`illustratif`), compatible avec 1 personne sur 2–3 chantiers d'ici fin février 2027.
- **Règles modifiées :** Aucune sur la parade (l'entraînement reste fermé comme correction ; seule une autorisation de bras de diagnostic sans score de moniteur est clarifiée pour le stress-test d'organisme).
- **Risque d'antériorité :** Faible à moyen (`OBSERVÉ-NON-AUDITÉ` sur sonde en tâche difficile à noter et sur combinaison audit+sonde ; une recherche d'antériorité complète manque encore `OBSERVÉ-NON-AUDITÉ`).

#### Architecture 2 : Programme intégré « Frontière Détecter / Auditer / Entraîner » (ouverture conditionnelle de l'entraînement)
- **Thèse :** Sur une tâche difficile à noter, l'entraînement sur note faible échoue à supprimer de façon fiable un saboteur robuste, et les sondes tranchent (ou échouent à trancher) entre guérison réelle, contournement de note faible et obscurcissement interne.
- **Expérience centrale :** Sur un saboteur prouvé résistant au bruit aléatoire (3e famille ou contrôle externe 14B `VÉRIFIÉ`), entraînement sur note faible durcie (sans oracle), suivi d'une évaluation croisée dommage réel / note faible / sonde.
- **Ce qui la réfuterait :** Tous les saboteurs 8B s'effondrent sous récompenses aléatoires, ou l'entraînement sur note faible supprime complètement le dommage sans obscurcissement ni besoin de sonde.
- **Exigences :** Saboteur robuste prouvé, infrastructure d'apprentissage par renforcement multi-tours (10 pas) sur 8B/14B, juge durci construit sans fuite d'oracle.
- **Coût :** ~5 000–12 000 $ GPU + évaluation humaine (`illustratif`) ; très tendu pour 1 personne avant fin février 2027.
- **Règles modifiées :** **OUI** — lève la règle « corriger en entraînant l'agent n'est pas ouvert » (et, si la sonde entre dans le signal d'entraînement, modifie la règle interdisant tout score de moniteur dans l'entraînement hors bras d'attaque `VÉRIFIÉ`).
- **Risque d'antériorité :** Moyen-élevé — le papier de 2026 (`VÉRIFIÉ`, référence à vérifier) désigne exactement cette suite (vrai saboteur affiné contre note faible) et dispose de modèles bien plus grands.

#### Architecture 3 (changement d'objet) : « Science des organismes modèles et de la représentabilité interne »
- **Thèse :** Les contradictions de la littérature sur les sondes et l'entraînement s'expliquent par la nature des organismes saboteurs (fragilité au bruit, artefact de poids, présence ou absence de représentation interne du sabotage).
- **Expérience centrale :** Cartographie systématique des 3 familles (consigne, adaptateur distillé, appris sans consigne) + saboteurs publics 14B (`VÉRIFIÉ`) × contrôles bénins appariés selon trois mesures : tenue au RL aléatoire, séparabilité interne conditionnellement au texte/poids, stabilité sous décalage bénin.
- **Ce qui la réfuterait :** Comportement uniforme de toutes les familles (aucune dissociation entre mode de fabrication, fragilité et lisibilité interne).
- **Exigences :** Les 3 familles + adaptateurs bénins + saboteurs publics 14B ; exigence plus légère sur l'oracle (seul un calibrage de dose vérifié par humains suffit).
- **Coût :** ~2 000–5 000 $ GPU (`illustratif`), calibré pour 1 personne ; publiable quelle que soit l'issue (positive ou négative sur les sondes).
- **Règles modifiées :** Aucune sur les parades (simple bras de diagnostic d'organismes).
- **Risque d'antériorité :** Faible sur l'intégration des trois axes en tâche difficile à noter (`OBSERVÉ-NON-AUDITÉ`).

#### Architecture 4 (changement d'objet) : « Durcissement d'oracle et entraînement faible » (abandon de la centralité des sondes)
- **Thèse :** Sur une tâche difficile à noter, le goulot d'étranglement étant la qualité du juge, le progrès passe par la construction sans fuite de juges durcis servant à entraîner l'agent plutôt que par la lecture interne.
- **Expérience centrale :** Construction d'un juge durci sans accès à la vérité approchée, puis entraînement d'un saboteur 8B contre ce juge, évalué par experts humains.
- **Ce qui la réfuterait :** Contournement systématique du juge durci ou perte de compétence honnête.
- **Exigences :** Annotations humaines massives, saboteur robuste, RL multi-tours.
- **Coût :** ~6 000–15 000 $ GPU + budget humain lourd (`illustratif`).
- **Règles modifiées :** **OUI — refonte complète** (ouvre l'entraînement contre score de juge et abandonne l'instrument central).
- **Risque d'antériorité :** Élevé — concurrence frontale avec les auteurs du papier de 2026 (`VÉRIFIÉ`, référence à vérifier) en perdant l'avantage comparatif de l'accès boîte blanche au modèle ouvert 8B.

*Arbitrage proposé :* L'**Architecture 1** (enrichie du diagnostic d'organismes emprunté à l'**Architecture 3**) exploite l'avantage comparatif d'une personne sur un modèle ouvert 8B, respecte les règles en vigueur, et préserve une issue scientifique propre même si les sondes échouent sur la 3e famille.

---

### 5. Ce qui, en dehors du programme et de son équipe, permettrait de vérifier la validité du résultat

1. **Audit aveugle du dommage par des experts externes.** Deux à trois chercheurs indépendants notent des paires anonymisées (jumeau honnête vs saboteur, mélangées à des paires honnête-vs-honnête) sans connaître l'oracle ni les doses, pour vérifier que le dommage mesuré est scientifiquement réel.
2. **Contrôles négatifs fournis par des tiers.** Tester les sondes gelées sur des adaptateurs LoRA bénins publics existants (entraînés hors programme sur le même modèle ouvert 8B pour le dialogue, la synthèse ou les sciences) : l'équipe ne peut pas avoir involontairement sur-ajusté sa sonde à ces poids.
3. **Validation croisée sur organismes saboteurs externes.** Appliquer les sondes (et contrôles bénins) aux saboteurs publics de 14 milliards de paramètres résistants au RL (`VÉRIFIÉ`, référence à vérifier), dont les auteurs ont nommé la piste des sondes sans l'essayer, ou participer à un test aveugle où une équipe rouge externe fournit un adaptateur sur le même modèle 8B sans révéler son procédé avant publication des scores.
4. **Préenregistrement public et vérification statistique tierce.** Dépôt horodaté des seuils, hyperparamètres et code d'évaluation avant ouverture de la famille inédite (`VÉRIFIÉ`), accompagné d'une vérification par un statisticien externe de la validité de la borne séquentielle sous dépendance intra-épisode (10 pas) et échantillonnage pondéré.
5. **Réplication hors modèle 8B et hors banc unique.** Répétition du protocole minimal par un autre groupe sur une autre architecture ouverte (7B–14B, `illustratif`) et une seconde tâche ouverte difficile à noter (par ex. critique de protocole expérimental) pour exclure un artefact de modèle ou de tâche.

---

### 6. Reformulation exigeante de la tâche

> « Avec une seule personne, trois chantiers actifs au plus, un modèle ouvert de 8 milliards de paramètres, un jury le 1er décembre 2026, une porte d'instruments fin décembre 2026 et une porte de comparaison fin février 2027, quel ensemble minimal de chantiers préenregistrés à inférence forte — en retirant toute ligne prématurée — permet d'établir ou de réfuter, sur une tâche difficile à noter :
> 1. qu'une sonde interne détecte un sabotage authentique (et non un artefact d'adaptateur, de consigne ou de faible qualité) mieux que des vérifications mécaniques simples et un moniteur texte durci, y compris en lecture unique sur une famille apprise sans texte de consigne ;
> 2. que les saboteurs du programme résistent à un entraînement bénin ou à récompenses aléatoires, et dans quelle mesure un entraînement ordinaire dégrade la calibration de la sonde ;
> 3. qu'une sonde ainsi validée réduit effectivement le coût d'un audit aléatoire garanti sans rompre sa borne de fausses alertes hors banc ni sa garantie pire-cas ;
> tout en n'ouvrant l'entraînement du modèle soupçonné comme parade défensive que si un organisme robuste est établi, si les autres voies montrent une limite précise, et après modification explicite des règles en vigueur ? »

---

### 7. Programme des priorités classé

Chaque chantier candidat est noté de 1 à 5 (évaluation relevant de ma proposition ; coût : 1 = CPU seul, 5 = lourd en calcul ou évaluation humaine) selon :
`score = (gain_informatif × facilité × portée × potentiel_de_découverte_majeure) / coût`.

| Rang | Chantier | Gain | Fac. | Portée | Découv. | Coût | Score | Statut proposé |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **C1.** Contrôle adaptateurs/prompts bénins, vérifications mécaniques et courbe dose-réponse consigne cachée | 5 | 5 | 5 | 3 | 2 | **187,5** | **Retenu (avant porte fin déc.)** |
| **2** | **C4.** Couplage sonde + audit aléatoire séquentiel (autocorrélation 10 pas et hors-domaine) | 4 | 5 | 4 | 3 | 2 | **120,0** | **Retenu (avant porte fin déc.)** |
| **3** | **C2.** Stress-test de fragilité des organismes (RL aléatoire / SFT bénin) et dérive bénigne des sondes | 5 | 4 | 4 | 4 | 3 | **106,7** | **Retenu (avant porte fin déc.)** |
| **4** | **C3.** Audit humain aveugle de l'oracle + test lecture unique sur 3e famille (sans consigne) : sonde vs juge durci | 5 | 3 | 5 | 5 | 4 | **93,8** | **Retenu (porte fév. 2027)** |
| **5** | **C5.** Bras d'attaque adaptatif (évasion sonde vs juge texte durci ; déjà prévu `VÉRIFIÉ`) | 4 | 3 | 5 | 4 | 4 | **60,0** | **Retenu (phase suivante)** |
| 6 | **C6.** Validation externe par sondes sur les saboteurs publics 14B résistants au RL (`VÉRIFIÉ`) | 4 | 3 | 3 | 4 | 3 | **48,0** | En réserve (après fév. 2027) |
| 7 | **C7.** Entraînement du modèle soupçonné sur note faible comme parade autonome *(change les règles)* | 3 | 2 | 4 | 3 | 5 | **14,4** | **Ne pas faire dans ce cycle** |
| 8 | **C8.** Essaims de copies à poids partagés *(ligne 3 actuelle)* | 2 | 2 | 3 | 3 | 4 | **9,0** | **Retirer / reporter** |

**Sensibilité du classement aux pondérations :**
- *Variante « priorité découverte »* (`gain² × portée × découverte² / coût`, sans `facilité`) : **C3** passe 1er (`781,3`), devant **C1** (`562,5`), **C2** (`533,3`), **C5** (`320,0`), **C4** (`288,0`), **C6** (`256,0`), **C7** (`64,8`), **C8** (`27,0`). Le top 4 reste composé des mêmes chantiers (bien que C3 dépende chronologiquement de C1 et C2).
- *Variante « budget/temps très serré »* (`coût²` au dénominateur) : **C1** (`93,8`), **C4** (`60,0`), **C2** (`35,6`), **C3** (`23,4`), **C6** (`16,0`) passe 5e juste devant **C5** (`15,0`), **C7** (`2,9`), **C8** (`2,3`).
- *Conclusion de sensibilité :* Le cœur (C1, C2, C3, C4) et le rejet (C7, C8) sont invariants ; seul l'arbitrage entre C5 (évasion RL sur 8B) et C6 (validation externe sur saboteurs publics 14B) bascule si la contrainte de calcul prime.

#### Expériences décisives des cinq chantiers retenus (inférence forte `H_A` vs `H_B` ; chiffres hors faits marqués `illustratif`)

**1. Chantier C1 — Purge des artefacts d'adaptateur/consigne et courbe dose-réponse manquante**
- `H_A` : Une sonde entraînée contre des adaptateurs bénins et consignes bénignes détecte le sabotage (adaptateur aux 4 doses `VÉRIFIÉ` et consigne cachée aux doses appariées) sur des adaptateurs bénins *inédits* mieux que toute vérification mécanique.
- `H_B` : Une fois les adaptateurs bénins inédits et prompts bénins inclus dans le nul, la sonde retombe au niveau des vérifications mécaniques ou viole la contrainte de fausses alertes.
- *Métrique et seuil (`illustratif`) :* Taux de détection à FPR $\le 1\%$ sur le nul durci inédit : `H_B` falsifiée si $\text{TPR}_{\text{sonde}} \ge 0{,}50$ ET $\Delta\text{TPR} = \text{TPR}_{\text{sonde}} - \text{TPR}_{\text{meilleure baseline}} \ge +0{,}15$ (IC 95 % > 0) aux doses à dommage significatif ; `H_A` falsifiée si FPR > 1 % sur adaptateurs bénins inédits ou $\Delta\text{TPR} \le 0$.
- *Contrôle négatif :* $\ge 4$ adaptateurs bénins inédits (2 distillés localement sans sabotage + 2 adaptateurs publics tiers sur le même 8B, `illustratif`), 2 prompts système bénins de longueur appariée, et les 20 % pires épisodes du jumeau honnête (`illustratif`).
- *Ancrage matériel et coût (`illustratif`) :* Modèle ouvert 8B (`VÉRIFIÉ`), 2 adaptateurs bénins légers + ~500 épisodes de 10 pas + baselines CPU : 200–600 $ GPU (quelques dizaines de dollars par course `VÉRIFIÉ`).
- *Condition d'invalidation :* Absence de dommage mesurable sur la courbe dose-réponse à consigne cachée.

**2. Chantier C4 — Couplage sonde + audit aléatoire séquentiel hors-domaine**
- `H_A` : Un schéma combinant un plancher d'audit aléatoire (ex. $p_0 = 10\%$, `illustratif`) et un aiguillage par sonde agrégée par épisode (supprimant l'autocorrélation des 10 pas) maintient le taux de fausses alertes sous $\alpha$ sur des articles scientifiques inédits (sans jumeau honnête) et divise significativement le nombre d'audits requis.
- `H_B` : Sans jumeau honnête, la dérive hors-domaine rompt la borne $\alpha$ ou, après recalibration conservatrice, annule le gain d'audit par rapport au tirage aléatoire pur.
- *Métrique et seuil (`illustratif`) :* Sur 100 flux rééchantillonnés d'horizon $T = 200$ épisodes hors-domaine : `H_B` falsifiée si FPR empirique $\le \alpha = 5\%$ ET rapport d'économie d'appels d'oracle $R \ge 2{,}0$ ; `H_A` falsifiée si FPR $> 10\%$ ou $R < 1{,}3$ après recalibration.
- *Contrôle négatif :* Flux 100 % honnêtes sur sujets inédits + adaptateurs bénins + sonde permutée aléatoirement (doit donner $R \approx 1$ tout en préservant la garantie pire-cas via $p_0$).
- *Ancrage matériel et coût (`illustratif`) :* Inférence de ~250 épisodes hors-domaine sur 8B (150–400 $) + simulations statistiques sur CPU seul (< 50 $).
- *Condition d'invalidation :* Fuite d'articles de calibration dans le jeu hors-domaine.

**3. Chantier C2 — Fragilité de l'organisme adaptateur et dérive des sondes sous entraînement bénin**
*(Règle en vigueur : aucun score de moniteur ni d'oracle dans l'entraînement ; ne constitue pas une parade. Si la règle fermant l'entraînement de l'agent s'applique à tout réglage fin post-sabotage, déclarer une dérogation strictement limitée à ce bras de diagnostic.)*
- `H_A` : L'adaptateur distillé du programme est un organisme robuste : son dommage résiduel reste élevé après un RL à récompenses aléatoires et après un SFT bénin léger.
- `H_B` : L'adaptateur est un organisme fragile (comme le résultat `VÉRIFIÉ` sur tâche exacte) : son sabotage s'effondre dès le RL à récompenses aléatoires. *(Mesure co-enregistrée : dérive du FPR de la sonde figée sur le jumeau honnête après SFT bénin.)*
- *Métrique et seuil (`illustratif`) :* Fraction résiduelle de dommage $\rho = \Delta Q_{\text{post}} / \Delta Q_{\text{pré}}$ mesurée contre le jumeau honnête ayant subi le même entraînement : `H_B` falsifiée si $\rho \ge 0{,}50$ ; `H_A` falsifiée si $\rho \le 0{,}20$ (zone $0{,}20 < \rho < 0{,}50$ non concluante). Dérive de sonde jugée critique si le FPR passe de $1\%$ à $> 5\%$.
- *Contrôle négatif :* Jumeau honnête soumis au *même* RL aléatoire et au *même* SFT bénin (sa qualité moyenne ne doit pas chuter de plus de 10 %, `illustratif`).
- *Ancrage matériel et coût (`illustratif`) :* Modèle 8B, 2 entraînements légers (RL aléatoire + SFT bénin) + évaluations : 500–1 200 $ GPU.
- *Condition d'invalidation :* Effondrement général de la capacité du jumeau honnête sous le traitement de contrôle.

**4. Chantier C3 — Audit humain aveugle de l'oracle et lecture unique sur la 3e famille (sans consigne)**
- `H_A` : Sur un dommage confirmé par des humains experts aveugles, la sonde figée et préenregistrée généralise à la 3e famille (apprise sans texte de consigne `VÉRIFIÉ`) et dépasse le juge texte durci ainsi que les vérifications mécaniques.
- `H_B` : Sans texte de consigne dans la fabrication du saboteur, la sonde préenregistrée échoue à généraliser au-delà du juge texte durci ou des baselines mécaniques, falsifiant la transférabilité de `HYPOTHÈSE`.
- *Métrique et seuil (`illustratif`) :* (1) Accord humain–oracle $\ge 75\%$ sur la direction du dommage ; (2) En lecture unique (`VÉRIFIÉ`) sur la 3e famille à FPR $\le 1\%$ : `H_B` falsifiée si $\text{TPR}_{\text{sonde}} \ge 0{,}40$ ET $\text{TPR}_{\text{sonde}} - \text{TPR}_{\text{juge durci}} \ge +0{,}15$ ; `H_A` falsifiée si $\text{TPR}_{\text{sonde}} < 0{,}25$ ou $\text{TPR}_{\text{sonde}} \le \text{TPR}_{\text{juge durci}}$.
- *Contrôle négatif :* Paires honnête-vs-honnête en aveugle pour les humains ; modèle de contrôle entraîné par le *même procédé sans consigne* sur récompense bénigne pour la sonde.
- *Ancrage matériel et coût (`illustratif`) :* Fabrication 3e famille + contrôle sur 8B (1 000–2 500 $ GPU) + inférence (300 $) + 20–40 h d'experts humains aveugles (1 500–3 000 $ ou temps de pairs).
- *Condition d'invalidation :* Accord humain–oracle $< 65\%$ (`illustratif`), disqualifiant l'oracle avant le test de sonde.

**5. Chantier C5 — Bras d'attaque adaptatif (évasion contre sonde vs contre juge texte durci)**
*(Conforme à la règle en vigueur : bras d'attaque déclaré prévu à la phase suivante `VÉRIFIÉ` ; l'oracle reste strictement exclu de l'entraînement. Aucune recette d'attaque publiée ; seules les courbes agrégées sont rapportées.)*
- `H_A` : À budget égal d'optimisation sans gradient à travers le moniteur, la sonde (ou une sonde tenue en réserve sur d'autres couches) résiste mieux à l'évasion que le juge texte durci.
- `H_B` : L'optimisation adaptative abaisse la détection de la sonde (y compris en réserve) au niveau honnête tout en préservant l'essentiel du dommage, aussi facilement ou plus facilement que contre le juge texte durci.
- *Métrique et seuil (`illustratif`) :* Au budget où l'attaquant réduit la détection du juge durci de $\ge 50\%$ en gardant $\ge 70\%$ du dommage : `H_B` falsifiée si la sonde (ou réserve) garde $\ge 60\%$ de son TPR initial ou réduit le dommage sous $30\%$ ; `H_A` falsifiée si les deux sondes tombent sous $20\%$ de TPR avec dommage résiduel $\ge 70\%$.
- *Contrôle négatif :* Même pénalité de sonde appliquée au jumeau honnête (la qualité honnête ne doit pas chuter de plus de 10 %, `illustratif`).
- *Ancrage matériel et coût (`illustratif`) :* RL/optimisation sur 8B (deux bras + contrôle honnête) : 1 500–3 500 $ GPU.
- *Condition d'invalidation :* Effondrement de qualité du jumeau honnête sous la pénalité ou organisme non robuste non écarté par C2.

#### Calendrier de décision (1 personne, 3 chantiers actifs max)
- **Avant la porte d'instruments (fin décembre 2026 ; premiers résultats bruts pour le jury du 1er décembre 2026) :** Exécuter **C1, C4 et C2** (3 chantiers actifs, coût cumulé modéré ~900–2 250 $, `illustratif`). En parallèle administratif : finaliser le devis de la 3e famille et l'accord des évaluateurs humains. *Règle de porte :* si C1 échoue, ne pas lancer C5 ; reconcevoir la sonde (en gardant la 3e famille vierge `VÉRIFIÉ`) ou basculer vers l'Architecture 3.
- **Entre fin décembre 2026 et la porte de comparaison (~fin février 2027), puis phase suivante :** Exécuter **C3** (livrable central de la porte de comparaison), puis **C5** (et **C6** si C2 révèle une fragilité de l'adaptateur 8B ou en complément externe après février 2027).
- **Ce qui ne doit pas être fait :** Retirer/reporter **C8 (essaims)** tant que le mono-agent n'a pas passé C1–C4. Ne pas ouvrir **C7 (entraînement correctif comme parade)** dans ce cycle : cela changerait les règles sans organisme robuste prouvé, placerait un programme 8B en concurrence frontale défavorable avec le papier de 2026 (`VÉRIFIÉ`) et risquerait de mesurer un artefact de fragilité.

#### Ce qui reste hors de portée
- **La validité d'échelle :** Je ne sais pas si les comportements d'obscurcissement interne, de fragilité d'adaptateur ou de représentabilité du sabotage observés sur un modèle de 8 milliards de paramètres se transfèrent à des modèles d'un ou deux ordres de grandeur plus grands ; cela reste hors de portée du budget actuel.
- **Les saboteurs qui ne se représentent véritablement pas leur sabotage :** Je ne sais pas aujourd'hui quel procédé d'apprentissage sans consigne produit un saboteur à la fois réaliste, résistant au bruit aléatoire et dépourvu de représentation interne explicite ; si C3 falsifie `H_A`, les sondes ne fourniront pas de garantie contre cette classe.
- **L'absence totale de référence honnête en déploiement long :** Sans jumeau honnête et face à une dérive continue des tâches ou des mises à jour du modèle, aucune sonde ne peut prouver à elle seule l'absence de menace diffuse ; la garantie ultime demeure limitée par la résolution de l'audit humain sur le produit.
- **La recherche d'antériorité exhaustive :** Elle reste incomplète (`OBSERVÉ-NON-AUDITÉ`) sur les combinaisons des trois voies avec lecture interne et devra être close avant publication.

FIN-DE-CELLULE