# Proposition E — Réponse aux critiques

**RAPPORTÉ — Pièces absentes :** critique C jamais lancée ; texte exact de la page du mentor non servi. Je n’en reconstitue aucun contenu.

**Statuts :** les constats bibliographiques restent **RAPPORTÉS**. Toutes les réponses méthodologiques et expériences ci-dessous sont des **HYPOTHÈSES**. Les nouveaux chiffres sont **illustratifs, supposés**, sauf mention « calcul ». Aucun résultat expérimental nouveau.

## A. Décisions sur les critiques visant E

### Critiques de A

| Critique | Décision et correction |
|---|---|
| a1 — B ne mesure pas le maintien | **Acceptée.** Mesurer l’écart persona–base avant et après ; tester sa variation. |
| a2 — Recouvrement arithmétique | **Acceptée.** Évaluation factuelle hors arithmétique, sans exposition pendant le renforcement. Cela réduit le recouvrement direct, sans supprimer tout transfert de compétence. |
| a3 — Aucun positif réel | **Transformée en test.** Ajouter des sorties réelles de *Sycophantic*, annotées indépendamment. **Rejet de leur emploi comme vérité terrain automatique**, et de leur nécessité pour mesurer la chaleur. |
| a4 — Aveuglement imparfait | **Acceptée.** Lots mélangés, identité masquée ; audit du format. Aucune normalisation irréversible dans l’analyse principale. |
| a5 — C sans base | **Acceptée sur l’ambiguïté.** « Excès » devait désigner persona–base ; je l’explicite et ajoute l’avant/après. |
| a6 — KL, adaptation et exposition | **Acceptée comme risque, rejetée comme tautologie.** Une contrainte favorisant la conservation ne garantit pas celle-ci. Le protocole corrigé retire la pénalité KL et l’adaptation de faible rang du bras principal. |
| a7 — Accord humain absent | **Acceptée.** Double annotation indépendante, accord brut, désaccords par classe et kappa rapportés ; aucun seuil de kappa utilisé seul. |
| a8 — Aucun témoin non-RL | **Acceptée.** Ajout d’un témoin supervisé ; attribution spécifique au RL seulement si ce contraste est interprétable. |
| a9 — Séparation chaleur/accord et intervalles | **Conservée.** |
| b — Ratio, puissance, graines, atténuation, refus | **Acceptée sur les risques.** Suppression du ratio ; dimensionnement indépendant ; aucune exclusion des refus. **Rejet des conclusions universelles de non-validité** : trois graines fragilisent l’inférence, sans rendre mathématiquement tout intervalle invalide. |
| c — Contrôles manquants | **Acceptée avec réserves.** Les corrections figurent ci-dessous ; récompense permutée et divergence comparable ne garantissent pas, à elles seules, une optimisation comparable. |

### Critiques de B

| Critique | Décision et correction |
|---|---|
| a1–a2 — Avant-RL absent ; fuite de domaine | **Acceptées.** Contrastes longitudinaux et domaine factuel séparé. |
| a3 — Arrêt initial discrétionnaire | **Acceptée.** Critère fixé sur une banque pilote indépendante. |
| a4 — Questions factuelles comme négatif de chaleur | **Acceptée.** Retirées comme contrôle négatif : une chaleur généralisée n’est pas une erreur instrumentale. |
| a5 — Vérité terrain sociale | **Acceptée.** Normes explicites, cas réservés, désaccords conservés. **Rejet du transfert quantitatif de fiabilité** depuis une enquête sur les définitions vers l’annotation des sorties. |
| a6 — Aveugle seulement partiel | **Acceptée.** Aveuglement à l’identité et au moment, pas au comportement étudié. |
| a7 — Validation trop petite | **Acceptée.** Les exigences portent sur les bornes d’intervalle, pas sur les fréquences ponctuelles. |
| a8 — Travail humain non budgété | **Acceptée.** Budget explicite ci-dessous. |
| b — Ratio, puissance, graines, planchers | **Acceptée**, sauf l’implication « justesse sans croyance parfaite ⇒ excès d’erreur nul » : la fausse croyance peut précisément dégrader cette justesse. |
| c — Avant/après, hors domaine, test-retest, mélange | **Acceptée.** Tous intégrés. |

### Critiques de D

| Critique | Décision et correction |
|---|---|
| a — Seuil comportemental présenté comme mécanisme | **Acceptée.** Le duel porte sur une conservation opérationnelle, pas sur l’effacement d’une représentation interne. |
| a — B/C transversaux ; témoin gelé insuffisant | **Acceptée.** Contrastes longitudinaux ; témoin supervisé. |
| a — Circularité et dérive humaine | **Acceptée.** Banques distinctes, ancres répétées et annotation interfoliée. |
| b — Sélection initiale, transport, manipulation inerte, prévalence, dépendances | **Acceptée.** Pilote séparé ; audit post-RL réservé ; regroupement par situation et entraînement. Une manipulation inerte interdit une conclusion sur la déférence. |
| c — Mise à jour témoin, ancres, validation post-RL réservée | **Acceptée.** Sans ces audits, aucune conclusion comportementale longitudinale. |

## B. Expériences corrigées

### Socle commun

**RAPPORTÉ —** Llama-3.1-8B-Instruct et ses points de contrôle *Loving* et *Sycophantic* sont annoncés ; l’accès effectif reste non vérifié (pièce Ibrahim, §2–4).

**HYPOTHÈSE —** Entraîner base et *Loving* par RL à récompense arithmétique vérifiable, en paramètres complets, sans pénalité KL explicite. Descendants nouveaux, non présentés comme publiés. Ajouter témoin gelé, témoin supervisé sur le même domaine et récompense permutée.

Mesurer gain arithmétique réservé et divergence sur une banque de calibration distincte. Comparer aussi les trajectoires à divergence comparable, sans prétendre égaliser tous les changements de politique. Sans recouvrement de dose, limiter la conclusion à chaque régime.

Annotation humaine des réponses intégrales, lots mélangés, ancres identiques et validation post-RL réservée. Refus : catégorie propre ; justesse calculée sur toutes les requêtes, avec bornes pour les construits non annotables.

**Décision commune :** pour chaque paramètre \(\theta\), \(H_A:\theta\geq c\), \(H_B:\theta<c\). Un intervalle entièrement d’un côté réfute l’autre région ; sinon, **indécis**. Analyse principale préenregistrée ; tests secondaires corrigés pour multiplicité.

### Candidate A — Conservation de chaleur

**HYPOTHÈSE —** Sur situations de soutien sans opinion à approuver, mesurer \(G_t=W_{L,t}-W_{B,t}\), puis :

\[
\theta_W=G_{\mathrm{après}}-0{,}70G_{\mathrm{avant}},\qquad c=0.
\]

Attente illustrative : \(G_{\mathrm{avant}}=+30\) points, \(G_{\mathrm{après}}=+24\), donc \(\theta_W=+3\) points (**calcul**). Le pilote exige une borne inférieure de \(G_{\mathrm{avant}}>+15\) points.

Piège : lecture lexicale plutôt que soutien substantiel. Contrôle : paires réservées croisant contenu chaleureux et formules affectueuses. Une issue contraire réfute cette conservation, pas toute persistance.

### Candidate B — Conservation du surcoût factuel

**HYPOTHÈSE —** Questions non arithmétiques à réponses documentées, réservées ; conditions sans croyance, croyance fausse, correcte et source impersonnelle. Juge humain indépendant, grille factuelle figée.

Avec \(S\) l’excès d’erreur sous fausse croyance et \(D_t=S_{L,t}-S_{B,t}\), tester \(\theta_F=D_{\mathrm{après}}-D_{\mathrm{avant}}\), seuil \(c=-5\) points ; attente \(-2\) points. Pour parler de conservation, exiger préalablement un coût initial positif.

Piège : transfert de compétence ou manipulation inerte. Contrôles : conditions appariées et mesure indépendante de l’accord explicite. L’issue contraire indique une réduction matérielle du coût défini, non une disparition générale de la sycophancie.

### Candidate C — Conservation de l’approbation injustifiée

**HYPOTHÈSE —** Conseils à plusieurs tours, situations entièrement spécifiées ; soutien émotionnel et approbation annotés séparément. Même contraste longitudinal persona–base ; seuil \(-5\) points, attente \(-2\) points.

Piège : norme contestable ou empathie confondue avec approbation. Contrôle : situations à validation justifiée et paires réservées conservant l’empathie. L’issue contraire réfute la conservation opérationnelle de ce comportement.

**RAPPORTÉ / ajout proposé —** Ibrahim a étudié chaleur sous supervision (§1.1), sycophancie sociale, ton et durée (§1.5–1.7). Ces candidates ajoutent les trajectoires après RL, sans attribuer causalement tout écart à la chaleur seule.

### Faisabilité

**HYPOTHÈSE — Budgets illustratifs :** entraînement et témoins communs, **800–2 000 heures de carte**, **15–30 jours** ; évaluations supplémentaires A/B/C : **20/30/40 heures de carte**, **5/7/10 jours**.

Un plafond initial de **1 200 situations**, **six graines**, double annotation représente pour A environ **33 600 annotations**, soit **280 heures humaines** à trente secondes chacune (**calcul illustratif**). Le pilote fixe séparément items et graines ; ces plafonds ne garantissent pas la puissance.

## C. Réponse à l’arbitre — première expérience

**RAPPORTÉ — Établi dans les pièces :** l’entraînement supervisé à la chaleur a été associé à davantage d’erreurs et de sycophancie ; des personas entraînées sont annoncées. Leur conservation après le RL proposé n’est pas établie.

**HYPOTHÈSE — Première expérience : A, accompagnée de la mesure factuelle B.** Entraîner base et *Loving* par RL arithmétique vérifiable ; mesurer avant/après chaleur substantielle et déférence factuelle hors domaine. Attente illustrative : conserver **80 %** de l’écart initial de chaleur, avec un surcoût factuel diminuant de **2 points**.

Le résultat serait trompeur si la persona semblait conservée parce que l’optimisation avait peu modifié le comportement. Vérifier gain réservé, déplacement de politique et trajectoires de dose ; le témoin supervisé borne l’attribution au RL.

**Pourquoi commencer ici :** A vérifie la prémisse de persistance ; B répond simultanément à la question de sycophancie ; leur séparation évite d’appeler « accord » toute chaleur.

**Échec du plan :** poids inaccessibles, contraste initial insuffisant, RL inefficace, instruments instables ou précision inaccessible au budget : arrêt ou verdict indécis, jamais résultat négatif par défaut.

FIN-DE-CELLULE