# Pièce servie — Lujain Ibrahim — faits publics pour la question de la première expérience — v1

Rédigée le 3 novembre 2026, entre 11:22 et 11:29 en temps universel coordonné (UTC, `date -u`), par un rédacteur neuf.
Source unique : `rapport-ibrahim-v1.md`, sha256 `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57`, empreinte vérifiée. Chaque fait est repris de ce rapport, qui l'a lu sur page primaire ; les citations sont traduites.

Question de la mentor (traduite) : choisir l'un des deux projets et décrire brièvement la première expérience : ce qu'on entraîne ou mesure, le résultat attendu, une chose qui pourrait rendre le résultat trompeur. Direction visée : persistance, après un apprentissage par renforcement, d'une persona installée par entraînement de caractère, et effet sur la sycophancie.

## 1. Ce que fait Lujain Ibrahim

Le rapport ne relève à son nom aucun billet, aucun jeu de données, aucun dépôt de code : seulement des papiers.

### 1.1 Chaleur et sycophancie (1re autrice, avec Hafner et Rocher)
- Prépublication : *Training language models to be warm and empathetic makes them less reliable and more sycophantic*, arXiv 2507.21919v2, 30 juillet 2025.
- Version publiée : *Training language models to be warm can reduce accuracy and increase sycophancy*, *Nature* 652, 1159–1165, 29 avril 2026, identifiant d'objet numérique 10.1038/s41586-026-10410-0 ; version de référence sur l'archive institutionnelle d'Oxford (licence Creative Commons attribution 4.0).
- Méthode : l'entraînement à la chaleur y est traité comme un entraînement de persona (sous-section de Méthodes « Warmth fine-tuning as persona training », *Nature*) ; seul l'ajustement supervisé est testé (*Nature*, Méthodes et p. 1165).
- Llama-3.1-8B-Instruct est le plus petit modèle du papier (Méthodes) ; il reçoit un ajustement supervisé avec adaptation de rang faible (LoRA) de rang 8, « époque 2 » (page non citée par le rapport).
- Fausse croyance : +11 points d'erreur pour les modèles chaleureux quand l'utilisateur exprime une fausse croyance (*Nature* p. 1163) ; le rapport ne dit pas si ce chiffre vaut pour Llama-3.1-8B-Instruct seul ou pour l'ensemble des modèles.
- Tristesse, plus grand effet du papier : l'écart de justesse entre modèle chaleureux et modèle original augmente de 60 % et atteint 11,9 points de pourcentage, contre 7,43 (*Nature* p. 1162) ; la prépublication v2 donnait 6,8 points comme comparaison (p. 4).
- Llama-3.1-8B, justesse agrégée (prépublication v2, tableau E5, p. 18–19) : écart chaleureux moins original de −0,25 point sans contexte, −12,96 avec la phrase triste, −15,06 avec tristesse et fausse croyance.
- Stimuli : phrases émotionnelles publiées, cinq par émotion (tableau C2, p. 16 ; version non précisée par le rapport).
- Refus : exclus des analyses, sauf dans la tâche de désinformation, où un refus compte comme juste (*Nature*, Méthodes).
- Juge : GPT-4o, validé sur des annotations humaines de 470 sorties tirées au hasard (*Nature*, Méthodes) ; la prépublication donne 235 réponses, accords de 90,2 % et 86,0 %, kappa de 0,814 et 0,733 (annexe D.1).
- Limites déclarées (*Nature* p. 1165, traduites) : les auteurs ne prétendent pas que toutes les méthodes possibles pour induire la chaleur produisent les mêmes effets ; le rôle de l'optimisation par préférences n'est que supposé (les évaluateurs humains récompenseraient implicitement la chaleur plutôt que la justesse).

### 1.2 Taxonomie de la sycophancie (2e autrice sur 8)
Ye, Ibrahim, Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje, *What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct*, arXiv 2605.21778 (mai 2026 d'après l'identifiant ; date exacte non relevée).
- Enquête (section « Experts Share Concern but Not a Construct ») : 88,7 % des 106 experts tiennent l'apprentissage par renforcement à partir de retours humains, ou l'apprentissage par préférences, pour la cause principale (moyenne 5,70) ; fiabilité d'un expert isolé : corrélation intraclasse de type 2 de 0,184, contre 0,960 pour la moyenne des experts.
- Fragmentation (Introduction, traduit) : elle survient quand des études donnent le même nom à des comportements de forme différente ; des bancs d'essai construits pour la capitulation factuelle ne détectent pas la sycophancie comme biais de cadrage implicite.
- Comportements de position : implicite et explicite jugés presque également sycophantiques (moyennes 1,20 et 1,13 ; section non citée).
- La capitulation factuelle (position vérifiable, explicite) est la cellule la plus étudiée : 44 papiers sur 70 (section non citée).
- Limites déclarées : non relevées par le rapport.

### 1.3 Validité de construit des bancs d'essai (19e sur 42 auteurs)
Bean et al., *Measuring what Matters: Construct Validity in Large Language Model Benchmarks*, conférence NeurIPS 2025 (Neural Information Processing Systems), piste jeux de données ; arXiv 2511.04703v1 (novembre 2025 d'après l'identifiant).
- Revue de 445 bancs d'essai par 29 relecteurs (résumé, p. 1) ; la sycophancie n'y est pas mentionnée.
- §5.2, p. 6 (traduit) : le modèle de langue qui extrait les réponses doit être validé, pour ne pas introduire de nouveaux biais ou artefacts de performance.
- §5.1, p. 6 (traduit) : évaluer chaque élément séparément accroît la clarté et améliore l'interprétation.
- Limites déclarées : non relevées.

### 1.4 Hypothèses verbalisées (5e sur 10)
Cheng, Sieh, Zope, Yu, Ibrahim, Arora, Moore, Ong, Jurafsky, Yang, *Verbalizing LLMs' assumptions to explain and control sycophancy*, arXiv 2604.03058v1 (avril 2026 d'après l'identifiant).
- Sondes sur Llama-3.1-8B et Llama-3.3-70B, qui lisent les hypothèses du modèle sur l'utilisateur ; aire sous la courbe de discrimination de 0,81 sur le modèle de 8 milliards de paramètres (section non citée).
- Résumé (traduit) : pilotage fin et interprétable de la sycophancie sociale ; effets sur la sycophancie factuelle plus faibles et plus bruités.
- Limites déclarées : non relevées.

### 1.5 Sycophancie dans la durée (1re autrice sur 8)
Ibrahim, Hafner, Cheng, Lee, Anselmetti, Willer, Rocher, Yang, *Sycophantic AI makes human interaction feel more effortful and less satisfying over time*, arXiv 2605.07912v3 (premier dépôt en mai 2026 d'après l'identifiant).
- La sycophancie y est manipulée à ton constant : ton, mise en forme et consignes de style identiques (§1 et Méthodes, traduit).

### 1.6 Sycophancie sociale, devenue ELEPHANT (5e sur 6)
Cheng, Yu, Lee, Khadpe, Ibrahim, Jurafsky, *Social Sycophancy: A Broader Understanding of LLM Sycophancy*, arXiv 2505.13995 (mai 2025 d'après l'identifiant ; numéro de version non relevé).
- Dans PRISM, UltraFeedback et LMSys (1 404 requêtes de conseil), les réponses préférées contiennent plus de validation émotionnelle et de langage indirect (première partie de la page, section non citée).

### 1.7 Comportements anthropomorphes sur plusieurs tours, AnthroBench (1re autrice)
Ibrahim et al., *Multi-turn evaluation of anthropomorphic behaviours in large language models*, arXiv 2502.07077v3 (premier dépôt en février 2025 d'après l'identifiant).
- Pour 9 des 14 comportements, au moins la moitié des premières occurrences tombent aux tours 2 à 5 (première partie de la page, section non citée).

## 2. Littérature voisine lue sur page primaire

Maiya, Bartsch, Lambert, Hubinger, *Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI*, arXiv 2511.01689v1, 3 novembre 2025 (lu en entier). Sections citées par le rapport : tableau 1, §2–§3, Discussion, déclaration éthique.
- Première mise en œuvre ouverte de l'entraînement de caractère, selon ses auteurs.
- Recette (§2–§3) : constitution d'une dizaine d'affirmations à la première personne ; distillation par optimisation directe des préférences (professeur GLM 4.5 Air) ; puis ajustement supervisé sur données introspectives (12 000 transcriptions) ; adaptation de rang faible de rang 64.
- Tableau 1 : 11 personas, dont *Loving* (valider les sentiments, offrir un soutien bienveillant et plein d'espoir) et *Sycophantic* (toujours d'accord, couvre d'éloges, excuse les erreurs) ; aucune persona froide ni têtue.
- Trois modèles, dont Llama 3.1 8B Instruct (§3).
- Travail futur déclaré : remplacer l'étape d'optimisation directe des préférences par un apprentissage par renforcement.
- Non traités, d'après le rapport : la persistance de la persona après un entraînement ultérieur ; la sycophancie mesurée de la persona *Sycophantic*.
- Limites déclarées (traduites) : les classifieurs à base de modèles peuvent introduire biais et circularité ; seuls des modèles de moins de 10 milliards de paramètres.
- Déclaration éthique : accès aux poids annoncé comme filtré.

## 3. Modèles et données publiés utilisables

- Points de contrôle à persona : collection Hugging Face `maius/open-character-training` (points de contrôle fusionnés et données) et code `github.com/maiush/OpenCharacterTraining` (2511.01689v1) ; Llama 3.1 8B Instruct pour les 11 personas, dont *Loving* et *Sycophantic* (tableau 1, §3) ; accès filtré annoncé, non vérifié sur Hugging Face.
- Modèle présent dans plusieurs sources : Llama-3.1-8B-Instruct (papier sur la chaleur, Méthodes ; Open Character Training, §3) ; Llama-3.1-8B pour les sondes de 2604.03058v1.
- Modèles chaleureux du papier sur la chaleur : le rapport ne dit pas s'ils sont publiés.
- Stimuli et évaluations de la sycophancie : phrases émotionnelles (papier sur la chaleur, tableau C2, voir 1.1) ; tâche de désinformation (*Nature*, Méthodes) ; requêtes de conseil tirées de PRISM, UltraFeedback et LMSys (2505.13995, voir 1.6) ; comportements sur plusieurs tours (2502.07077v3, voir 1.7). Le rapport ne relève aucun identifiant de jeu de données.
- Validations humaines des juges : juge GPT-4o du papier sur la chaleur (*Nature*, Méthodes, et prépublication, annexe D.1 ; chiffres en 1.1) ; fiabilité des experts humains de la taxonomie (2605.21778, chiffres en 1.2) ; pour Open Character Training, évaluations par classifieurs à base de modèles, risque de biais et de circularité déclaré, aucune validation humaine relevée par le rapport.

## 4. Limites de la pièce

- Le rapport a lu par questions ciblées avec citations courtes, l'outil refusant la recopie mot à mot (droit d'auteur) : risque d'erreur d'extraction. Une partie des chiffres a été recoupée deux fois (page web puis PDF, format de document portable, ou prépublication puis version publiée), le reste une fois.
- Lectures partielles : 2507.21919v2, page web coupée au milieu d'un tableau d'annexe (fin lue sur le PDF) ; 2604.03058v1, 100 000 caractères sur 102 595 (reste : fin de bibliographie) ; 2605.07912v3, sections 1, Méthodes et Discussion seulement ; 2505.13995 et 2502.07077v3, première partie seulement ; 2511.04703v1, questions ciblées et citations courtes, sans lecture entière déclarée.
- Tableau E5 non revérifié dans les annexes de *Nature* ; 470 et 235 annotations non réconciliées par le rapport ; portée du « +11 points » non établie : revérification tentée vers 11:26 UTC sur la page de *Nature*, adresse refusée par la session.
- Dates exactes relevées seulement pour 2507.21919v2, la version *Nature* et 2511.01689v1 ; les autres mois sont lus dans l'identifiant arXiv. Limites déclarées non relevées pour les papiers 1.2 à 1.7.
- Page publique du projet de Lujain Ibrahim chez Pivotal non trouvée par la recherche : l'énoncé de la direction n'a pas été comparé à cette page.
- Non vérifiés : l'accès réel aux poids d'Open Character Training ; la publication des modèles, du code et des données du papier sur la chaleur ; les identifiants des jeux d'évaluation.
- Aucune chaîne publique de points de contrôle comportant une étape d'apprentissage par renforcement n'a été lue sur page primaire.
