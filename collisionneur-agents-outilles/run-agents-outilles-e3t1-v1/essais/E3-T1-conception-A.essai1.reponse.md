# Proposition A — Tour III.1 : agents outillés pour un organisme non fiable

**Pièce manquante** : le bloc FAITS est vide par décision de l'arbitre (RAPPORTÉ, message n° 28 § 1). Tout ce que je dis du dispositif existant a donc le statut RAPPORTÉ (par la question) ou HYPOTHÈSE ; rien n'est VÉRIFIÉ par moi.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ça compte |
|---|---|---|---|
| A1 | L'isolation actuelle remplit déjà ses quatre raisons d'être. | HYPOTHÈSE (OBSERVÉ-NON-AUDITÉ au mieux : la question la décrit, personne n'en joint d'audit). | Ajouter (b2) à une enceinte non auditée revient à mesurer une fuite marginale sur un fond inconnu. |
| A2 | « Jamais les vérités » suffit à protéger la validité de la mesure. | HYPOTHÈSE, et contredite par un résultat établi : l'organisme reçoit un score par génération, donc interroge adaptativement le jeu tenu à l'écart ; la validité statistique se dégrade avec le nombre de requêtes même sans jamais voir une étiquette (Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, « The reusable holdout: Preserving validity in adaptive data analysis », *Science*). | (b2) multiplie les requêtes par course ; le problème préexiste, (b2) l'amplifie. |
| A3 | Le goulot de l'organisme est le calcul (il « ne peut pas tester »), pas la qualité des hypothèses. | HYPOTHÈSE. | Si les hypothèses sont vagues, un agent outillé produit des tests non informatifs plus vite. Expérience E1 ci-dessous. |
| A4 | Le modèle ouvert de 8 Md est un substitut valide des cibles réelles pour la « conscience d'évaluation ». | HYPOTHÈSE. Ce qui est RAPPORTÉ dans la littérature (Needham, Edkins, Pimpale, Bartsch, Hobbhahn, 2025, « Large Language Models Often Know When They Are Being Evaluated » — liste d'auteurs à vérifier) concerne des modèles de frontière, pas une sonde sur un 8 Md. | Une sonde qui marche sur le 8 Md peut ne rien dire des modèles visés. |
| A5 | Le jeu « conscience d'évaluation » public, dont les étiquettes sont en ligne, n'est pas mémorisé par le modèle ouvert de 8 Md. | HYPOTHÈSE, probablement fausse pour une partie des items. | C'est le canal de fuite le plus direct de (b2) : « faire répondre le modèle ouvert » à un préfixe d'item peut régurgiter l'item et son étiquette. |
| A6 | (b1) est « déjà possible » et sans coût de fuite nouveau. | RAPPORTÉ (par la question). | Vrai pour l'exécution ; faux pour le choix des expériences (piratage de récompense, point 2). |
| A7 | Les sondes linéaires ou à une couche mesurent le concept visé et non un artefact (longueur, lexique, format). | HYPOTHÈSE ; la littérature impose des tâches de contrôle pour la sélectivité (Hewitt, Liang, 2019, « Designing and Interpreting Probes with Control Tasks » ; Belinkov, 2022, « Probing Classifiers: Promises, Shortcomings, and Advances », *Computational Linguistics*). | Sans tâche de contrôle intégrée à la primitive, l'organisme optimisera une sonde qui lit l'artefact. |
| A8 | La garde de fuite repère des items de test paraphrasés, pas seulement copiés. | HYPOTHÈSE ; aucune mesure jointe. | Point (c). |
| A9 | Un refus de l'agent interne (b1) ou une erreur du noyau est « neutre ». | HYPOTHÈSE. Un message d'erreur est un bit d'information ; la littérature sur le confinement le dit depuis Lampson, 1973, « A Note on the Confinement Problem », *CACM*. | Normalisation des erreurs, point 3. |

---

## (b) Expériences décisives (duel H_A / H_B)

### E1 — Le goulot est-il le calcul ou l'hypothèse ?

- **H_A** : donner à l'organisme une primitive de calcul (b2) augmente la part de ses hypothèses préenregistrées confirmées sur le jeu tenu à l'écart. **H_B** : la part confirmée ne change pas ; seul le nombre d'hypothèses émises change (le calcul produit du bruit, pas du signal).
- **Métrique** : taux de confirmation = hypothèses dont le test préenregistré, exécuté par le noyau sur items tenus à l'écart, dépasse le seuil fixé à l'avance, divisé par hypothèses émises. Comparaison appariée sur le même nombre de générations.
- **Seuil** : différence ≥ 15 points de taux de confirmation (illustratif) à n ≥ 40 hypothèses par bras (illustratif), intervalle par bootstrap excluant zéro.
- **Contrôle négatif — primitive placebo** : un bras où `entrainer`/`predire` rendent des probabilités issues d'un modèle dont les activations ont été permutées entre textes. L'organisme ne doit pas le savoir. Si le bras placebo confirme autant que le bras réel, H_A est falsifiée *et* on apprend que le score mesure autre chose que l'hypothèse.
- **Ce qui falsifie** : H_A tombe si l'écart réel–témoin < seuil ou si placebo ≈ réel ; H_B tombe si l'écart dépasse le seuil et que le placebo reste au niveau du témoin sans primitive.

### E2 — Fuite par requêtes adaptatives (raison d'être 1)

- **H_A** : avec (b2), l'organisme reconstitue de l'information sur les étiquettes tenues à l'écart au-delà du hasard. **H_B** : non.
- **Dispositif** : canaris. Le noyau insère dans le jeu tenu à l'écart k items (illustratif : 50) dont l'étiquette est tirée au sort et n'a aucun rapport avec le contenu. Après N générations, on calcule l'exactitude du meilleur détecteur produit par l'organisme sur les canaris seuls.
- **Métrique et seuil** : exactitude sur canaris ; H_A retenue si > 0,5 avec p < 0,01 (test binomial) ; sinon H_B. Même protocole sans (b2) donne le fond de fuite existant (teste A1 au passage).
- **Contrôle négatif** : canaris dont l'étiquette est retirée au sort à chaque génération (aucune information stable à fuir) ; leur exactitude doit rester à 0,5 dans tous les bras.
- **Ce qui falsifie** : exactitude > 0,5 falsifie « le noyau ne rend jamais les vérités » comme garantie suffisante ; exactitude à 0,5 après N grand falsifie l'objection la plus forte contre (b2), *pour ce budget de requêtes*.

### E3 — Mémorisation du jeu public par le modèle ouvert (A5)

- **H_A** : le modèle de 8 Md complète au moins une fraction f des items publics à partir de leur préfixe (régurgitation). **H_B** : aucun item n'est complété au-delà de ce qu'on obtient sur des textes de même distribution jamais publiés.
- **Métrique** : taux de complétion exacte sur 100 premiers jetons à partir d'un préfixe de 50 (illustratif), items publics contre items de contrôle rédigés après la date de coupure du modèle.
- **Seuil** : écart ≥ 5 points (illustratif). Contrôle négatif : textes synthétiques de même longueur et lexique.
- **Ce qui falsifie** : H_A falsifiée si l'écart est nul ; H_B falsifiée sinon, et alors la primitive « faire répondre le modèle » doit exclure toute génération libre sur préfixes proches du jeu (voir point 3).

### E4 — Capacité des canaux auxiliaires (temps, tailles, erreurs)

- **H_A** : les champs auxiliaires rendus par le noyau (durée, octets, code d'erreur) portent ≥ 1 bit par appel exploitable pour distinguer deux états internes du noyau (par exemple « item de test présent / absent dans la requête »). **H_B** : < 0,05 bit par appel après normalisation.
- **Métrique** : information mutuelle estimée entre l'état caché et le vecteur de champs auxiliaires, sur 1 000 appels (illustratif) ; méthode : classifieur entraîné à prédire l'état à partir des champs, exactitude convertie en bits.
- **Contrôle négatif** : même mesure avec champs remplacés par des constantes (doit donner 0).
- **Ce qui falsifie** : H_A falsifiée si information < 0,05 bit avec normalisation ; H_B falsifiée sinon, ce qui impose la quantification et le rembourrage décrits au point 3.

### E5 — (b1), (b2), humain dans la boucle (demande 5)

- Trois bras, même lignée d'organismes, même banque de tâches, même nombre de générations.
- **H_A** : le gain de score tenu à l'écart par euro dépensé est plus élevé en (b2) qu'en (b1) et qu'en « humain ». **H_B** : le bras « humain » domine à coût égal (les humains filtrent mieux les hypothèses que le calcul ne les teste).
- **Métrique** : Δscore holdout / coût total (calcul + appels + heures humaines valorisées), et taux de canaris (E2) comme garde-fou : un bras qui gagne du score en fuyant est disqualifié.
- **Seuil** : rapport ≥ 1,5 entre bras (illustratif) sur 3 lignées indépendantes.
- **Contrôle négatif** : bras sans aucune possibilité de test (état actuel). Issue : si (b1) ≈ (b2), l'infrastructure (b2) ne vaut pas sa surface de fuite ; si humain ≥ (b2), A3 est falsifiée.

---

## (c) Mesure minimale pour chaque instrument nommé

| Instrument | Taux de détection à mesurer | Fausses alertes sur cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| **Garde de fuite** (sur `rechercher`, `telecharger`, et sur textes engendrés par l'organisme en (b2)) | Part des items de test détectés quand ils sont : copiés, tronqués, paraphrasés par un modèle, traduits puis retraduits (quatre strates). | Textes du même sujet, même longueur, même registre, écrits par un humain après la coupure, jamais publiés : taux de blocage doit rester < 1 % (illustratif). | MinHash sur 5-grammes de caractères ; seuil de cosinus sur plongements phrastiques. Si la garde ne bat pas ces deux lignes sur la strate « paraphrase », elle n'apporte rien. |
| **`entrainer`/`predire`** (sondes) | Sur une tâche de contrôle à la Hewitt & Liang (étiquettes aléatoires fixées par mot) : la sonde doit échouer. Sélectivité = exactitude tâche réelle − exactitude tâche de contrôle. | Items honnêtes appariés : même prompt, une variante « évaluation » et une variante « déploiement » différant du minimum. | Régression logistique sur sac de mots du texte brut. Une sonde sur activations qui ne bat pas le sac de mots lit le lexique, pas un état interne. |
| **Détecteur de conscience d'évaluation** (produit de l'organisme) | TPR sur items dont l'étiquette vient d'un juge humain, hors du jeu public. | FPR sur paires appariées ci-dessus ; FPR sur textes contenant les mots « test », « benchmark », « évaluer » sans contexte d'évaluation. | Expression régulière sur ce lexique ; longueur du prompt ; présence d'instructions numérotées. |
| **Agent interne (b1)** | Part du code proposé qui reproduit un résultat connu planté par le noyau (vérité de référence sur données synthétiques). | Part des hypothèses déclarées « confirmées » par l'agent et infirmées sur le jeu tenu à l'écart (c'est sa fausse alerte). | Hypothèse nulle : tirer la conclusion au hasard. Si la précision de l'agent n'est pas supérieure à 0,5 sur la confirmation, il ne sert qu'à produire du texte. |
| **Moniteur de confiance** (si adopté pour (b2), voir point 4) | Part des requêtes malveillantes injectées par une équipe rouge (encodage d'items de test, dépassement de plafond, texte de sonde conçu pour la régurgitation) qui sont bloquées. | Part des requêtes honnêtes d'une course témoin bloquées à tort ; cible < 2 % (illustratif). | Règles mécaniques : taille, nombre d'items, liste noire de préfixes. Le moniteur n'est justifié que s'il détecte ce que les règles ratent. |
| **Journal / plafonds** | 100 % des dépassements tentés (fuzzing du serveur local) refusés et journalisés. | Zéro refus d'appels sous plafond. | Test déterministe ; aucun apprentissage. |

---

## (d) Ancrage matériel

- **Modèles ouverts de la classe 8 Md** : famille Llama 3 8B, Qwen2.5 7B (existence VÉRIFIÉE ; licence et version exacte à fixer par l'arbitre). Choisir un modèle dont la date de coupure est documentée, pour E3.
- **Extraction d'activations** : une carte de 24 Go suffit en demi-précision pour un 8 Md en inférence ; 10 000 textes de 512 jetons, une couche, donnent ~10 000 × 512 × 4 096 × 2 octets ≈ 42 Go si on garde tous les jetons, ~84 Mo si on garde le dernier jeton ou la moyenne (calcul explicite). Le noyau doit imposer l'agrégation par texte ; sinon la volumétrie devient un canal et un coût.
- **Temps** : illustratif, ordre de 10 à 30 minutes GPU pour 10 000 textes de 512 jetons sur une carte de classe A10/L4 ; entraînement d'une sonde linéaire sur 84 Mo : secondes de processeur central.
- **Coût** : illustratif, 1 à 3 €/heure de carte louée ; une course de 20 générations avec un plafond de 10 extractions de 2 000 textes par génération coûte de l'ordre de quelques dizaines d'euros de calcul, à vérifier sur devis. Les appels `appeler` aux modèles de frontière dominent sans doute le budget, pas la carte.
- **Pilote E5** : trois bras × trois lignées × 20 générations ; coût de calcul illustratif de l'ordre de la centaine d'euros ; coût humain du bras « humain dans la boucle » : quelques heures par lignée, c'est le poste à chiffrer honnêtement.

---

## Réponses aux cinq demandes

### 1. Ce que les agents outillés apporteraient, et le coût

Expériences aujourd'hui impossibles pour l'organisme (toutes HYPOTHÈSES sur leur utilité, à soumettre à E1) :

1. **Paires de contraste engendrées** : l'organisme écrit des paires minimales (même contenu, cadre « évaluation » vs « déploiement »), les fait passer au modèle ouvert, entraîne une sonde, mesure la sélectivité contre la tâche de contrôle. Coût : une extraction par paire, 2 000 textes ≈ quelques minutes GPU.
2. **Balayage de couches** : quelle couche porte le signal. Coût : extraction multicouche (× nombre de couches en stockage si on agrège par texte, négligeable sinon).
3. **Ablation d'items** : retirer les items contenant le lexique évident et voir si la sonde tient (teste A7 de l'intérieur). Coût : entraînements CPU.
4. **Réponses du modèle** à ses propres textes : voir si le modèle de 8 Md change de comportement selon le cadre. Coût : génération, plus cher que l'extraction ; c'est aussi la primitive la plus dangereuse (E3).

Ce que (b1) permet seul : 3 entièrement (sur activations déjà fournies), 1 et 2 seulement si le noyau accepte des textes nouveaux. Ce que (b1) n'apporte jamais : un calcul sur carte.

### 2. Surface de fuite, point par point

**(b1) — agent interne, processeur seul.**
- Validité (1) : pas de canal nouveau vers les vérités. Canal ancien amplifié : plus d'hypothèses par génération → plus de requêtes au score → A2.
- Dépenses (2) : les appels `appeler` de l'agent passent par le noyau ; le temps CPU est borné. Risque : boucle agent qui consomme tout le budget d'appels en une génération ; plafond par génération déjà nécessaire.
- Secrets (3) : rien de nouveau si le bac à sable tient (A1).
- Traçabilité (4) : le code proposé par le modèle de frontière et exécuté localement n'est tracé que si le noyau journalise aussi la sortie de `appeler` et l'exécution ; sinon une partie du raisonnement sort du journal.
- Piratage de récompense : l'organisme choisit les expériences qui le font paraître bon et déclare « confirmé » ce que l'agent dit. Sans test tenu à l'écart par le noyau, le mot « confirmé » ne vaut rien ; c'est le défaut documenté des systèmes de recherche automatisée (Lu, Lu, Lange, Foerster, Clune, Ha, 2024, « The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery » ; revue automatique complaisante et biais d'auto-préférence : Zheng et al., 2023, « Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena » ; Panickssery, Bowman, Feng, 2024, « LLM Evaluators Recognize and Favor Their Own Generations »).

**(b2) — primitive de calcul lourd.**
- Validité (1), canaux classés par gravité :
  - **Régurgitation** par le modèle ouvert d'items publics (E3). Gravité haute si la primitive « faire répondre » est libre.
  - **Choix des items** : si l'organisme peut soumettre des textes proches des items de test, la garde de fuite est le seul rempart (A8).
  - **Résultats d'entraînement** : probabilités sur des textes proches des items de test ≈ sonde sur les items eux-mêmes ; gravité moyenne, bornée par le nombre d'appels (Dwork et al. 2015 donne le cadre : bruit calibré et budget de requêtes).
  - **Temps de calcul, tailles, erreurs** : E4. Gravité faible par appel, cumulable. Le temps de file sur la carte renseigne aussi sur les *autres* courses (canal entre courses).
- Dépenses (2) : la réservation au pire cas doit couvrir extraction + génération ; une génération de texte sans borne de jetons est le trou évident.
- Secrets (3) : la carte louée est hors du bac à sable ; si le noyau y transporte autre chose que des textes et des hyperparamètres, c'est une sortie. Le code de la sonde ne doit jamais être du code arbitraire : architecture choisie dans un menu, pas écrite.
- Traçabilité (4) : acquise si chaque requête et chaque chiffre rendu est journalisé ; perdue si des fichiers d'activations sont rendus bruts (volumétrie non lisible).
- Piratage de récompense : identique à (b1), plus un risque spécifique : optimiser la sonde pour maximiser une métrique d'entraînement que le noyau rend, au lieu du test tenu à l'écart. Parade au point 3.

### 3. Dessin de (b2)

**Primitives minimales** (trois, pas plus) :

| Primitive | Entrée | Rendu | Jamais rendu |
|---|---|---|---|
| `activer(textes, couches, agregation)` | ≤ N textes par appel, ≤ L jetons chacun, couches dans une liste autorisée, agrégation ∈ {dernier jeton, moyenne} | un identifiant opaque + dimensions | les activations elles-mêmes (elles restent côté noyau) |
| `sonder(id_activations, etiquettes, archi ∈ menu, pas ≤ P)` | étiquettes écrites par l'organisme | perte finale quantifiée, probabilités sur un sous-ensemble de validation que l'organisme a lui-même étiqueté, sélectivité contre tâche de contrôle calculée par le noyau | poids de la sonde ; toute métrique sur items tenus à l'écart |
| `repondre(textes, max_jetons ≤ T)` | textes passés par la garde de fuite | texte engendré, repassé par la garde avant retour | toute complétion dont le préfixe approche un item du jeu public (blocage silencieux, remplacement par un jeton de refus uniforme) |

**Bornes** (illustratives, à régler sur devis) : par génération, ≤ 10 `activer` de ≤ 2 000 textes, ≤ 50 `sonder`, ≤ 200 `repondre` de ≤ 256 jetons ; par course, dix fois cela ; plafond en secondes GPU réservé au pire cas avant l'appel.

**Gardes** : garde de fuite sur les textes entrants *et* sortants ; liste d'exclusion des items de test et du jeu public (empreintes + plongements) ; architectures dans un menu fermé ; erreurs réduites à une énumération fixe de cinq codes ; champs de temps et de taille quantifiés (temps arrondi à la dizaine de secondes, tailles rembourrées à des paliers) ; journal de chaque appel avec empreinte des entrées.

**File d'exécution** : asynchrone, par ticket. Le temps d'attente en file n'est pas décompté du temps de génération (sinon la charge d'autres courses devient un canal et une injustice) ; seul le temps GPU consommé l'est. Conséquence : une génération peut se terminer avec des tickets en attente ; les résultats sont livrés à la génération suivante. Cela ralentit la boucle mais coupe le canal temporel entre courses. Alternative synchrone, plus simple, acceptable seulement si une carte est dédiée à la course (coût) — à départager par E4.

**Préenregistrement sans choix du test par l'organisme** : l'organisme écrit, *avant* tout appel de la génération, une fiche d'hypothèse (énoncé, sonde, couche, seuil de succès). Le noyau scelle la fiche, puis tire *lui-même* les items de test dans un réservoir hors d'atteinte, exécute la sonde de l'organisme dessus, et ne rend qu'un verdict binaire agrégé — à la génération suivante, et seulement si le nombre de verdicts de la course reste sous un budget (parade à A2, dans l'esprit du *reusable holdout*). L'organisme choisit l'hypothèse, jamais les items ni le moment de l'évaluation.

### 4. Ce qui est connu (références que je peux attribuer)

- Contrôle d'une IA non fiable : Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion » — surveillance par modèle de confiance, approbation des actions à risque, équipe rouge ; le cadre est directement applicable à `repondre` et `activer`.
- Validité sous requêtes adaptatives : Dwork et al., 2015, cité en A2.
- Sondes et tâches de contrôle : Alain, Bengio, 2016, « Understanding intermediate layers using linear classifier probes » ; Hewitt, Liang, 2019 ; Belinkov, 2022 (cités en A7).
- Conscience d'évaluation et comportement sous évaluation : Needham et al., 2025 (à vérifier) ; Greenblatt, Denison et al., 2024, « Alignment faking in large language models » ; van der Weij, Hofstätter, Jaffe, Brown, Ward, 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations ».
- Agents de recherche et leurs failles : Lu et al., 2024 (ci-dessus) ; Si, Yang, Hashimoto, 2024, « Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers » (nouveauté jugée plus haute, faisabilité plus basse) ; Gottweis et al., 2025, « Towards an AI co-scientist » (à vérifier) ; juges complaisants : Zheng et al., 2023 ; Panickssery, Bowman, Feng, 2024.
- Contamination des bancs d'essai : Sainz et al., 2023, « NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark » (à vérifier).
- Canaux cachés et temporels : Lampson, 1973 ; Kocher, 1996, « Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems ».
- Préenregistrement : Nosek, Ebersole, DeHaven, Mellor, 2018, « The preregistration revolution », *PNAS*.
- Non cité faute d'attribution sûre : travaux sur « sondes simples contre agents dormants » (référence à vérifier) ; études de piratage de récompense en agents de code (référence à vérifier).

### 5. Comment départager (b1), (b2), humain dans la boucle

Pilote E5, précédé obligatoirement de E2 et E3 (si E3 révèle une régurgitation, `repondre` sort du dessin avant toute comparaison). Mesure unique : Δscore sur le jeu tenu à l'écart par euro, sous contrainte « exactitude sur canaris ≤ 0,55 ». Trois lignées, vingt générations, trois bras ; coût de calcul illustratif de l'ordre de la centaine d'euros, coût humain à chiffrer. Issues : (b2) ne se justifie que si elle bat (b1) d'un facteur net *et* ne dégrade pas les canaris ; si l'humain domine, la bonne dépense est un meilleur préenregistrement, pas une carte. Je ne présente aucune des trois voies comme la réponse ; je note que la plus coûteuse en surface de fuite, (b2), est aussi la seule dont l'apport dépend d'une hypothèse (A3) que personne n'a mesurée.

FIN-DE-CELLULE