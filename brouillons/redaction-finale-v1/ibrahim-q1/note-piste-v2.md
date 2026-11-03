# Note de piste — réponse à Lujain Ibrahim, question 1 — v2

Rédacteur neuf, page blanche : je n'ai écrit aucune version des réponses de Lazar et je n'ai lu aucun fichier de numéro 1 de ce dossier. Travail du 3 novembre 2026, de 15:27:31 à environ 15:50 UTC (`date -u`).
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-ibrahim-q1-ensemble-v1.md`, empreinte vérifiée (`11a6237e…eb`). Dossier de piste vérifié (`6f3be686…e4`), recoupement vérifié (`bea573aa…fe0a`).

## Fiche principale : IB-10

Groupe imposé par la règle gelée : « Structure du construit ». IB-10 est la mieux classée du groupe (rang 3, testable en jours : 3), sans drapeau, avec un appui public de Lazar et deux duels à région indécise.
La réponse en garde la porte sans entraînement sur les personas publiées d'Open Character Training, les phrases émotionnelles et la croyance fausse du papier sur la chaleur, le témoin « même affirmation d'une source impersonnelle » et l'arrêt si l'instrument ne voit pas la persona.
Elle y ajoute, corrigée de son drapeau, l'idée d'IB-16 : deux composantes lues sur les mêmes modèles, avec une sélectivité attendue non nulle.

## Les trois arguments retenus

**1. Porte avant tout renforcement (IB-10).**
Open Character Training a publié Loving et Sycophantic pour Llama-3.1-8B-Instruct sans rapporter la sycophancie de Sycophantic.
Si les instruments ne voient pas la persona avant le renforcement, aucun résultat d'après renforcement n'est lisible.
L'expérience ne coûte que de l'inférence.
Appui public de Lazar : la loi a été trouvée sur ce modèle (README) ; les refus notés 3 imitent l'attraction (R4, R6).
Mesure qui tue : si Sycophantic ne bouge aucune des deux composantes, les instruments sont aveugles et le renforcement attend.

**2. Deux composantes, un seul instrument, un croisement attendu (IB-16 corrigée, conditions d'IB-10).**
Sur ses questions factuelles : effet de la croyance fausse de l'utilisateur, net de la même affirmation attribuée à une page web, et effet de la phrase triste. Chacun en différence persona − base.
Son ajustement chaleureux de Llama-8B classe déjà les deux indices : −5,24 points de justesse avec la croyance, −12,96 avec la phrase triste (tableau E5, p. 19, moyenne sur quatre jeux).
Attendu : Loving garde cet ordre, Sycophantic (« always agrees ») l'inverse.
Mesure qui tue : même signe du contraste tristesse − croyance pour les deux personas. Un intervalle à 95 % qui contient zéro laisse la question indécise.

**3. Le croisement tient sans témoin froid.**
Son papier sépare la chaleur de l'ajustement lui-même par un témoin froid, mais seulement sur Qwen-32B et Llama-70B (p. 6) ; Open Character Training n'a aucune persona froide.
Les deux personas ont la même recette : un dommage d'ajustement commun (Llama-8B perd 8,6 points sur MMLU, p. 6) déplace leurs contrastes dans le même sens et ne peut pas produire des signes opposés.
C'est ce qui rend la mesure qui tue lisible sur ces points de contrôle.
Appui public de Lazar : le même raisonnement par signe et par intervalle que R8 (bootstrap apparié sur les items, intervalles à 95 %).

La chose trompeuse choisie, un juge qui lit le ton comme le fond, s'appuie sur un résultat public de Lazar : son juge note 3 les refus, près de la destination sous éloge (R4 l. 36 et 38).

## Ce qui n'est pas repris, et pourquoi

- **IB-03** : aucun appui public de Lazar ; son attendu est une sélectivité nulle, contraire à la consigne ; puissance d'environ 3 000 items par case ; 300 heures de carte.
- **IB-19, IB-21** : aucun appui public de Lazar ; elles exigent le renforcement, ce ne sont pas des premières expériences.
- **IB-16, partie couverture** : drapeau rouge. La fiche prêtait à la taxonomie une prédiction (les cellules ne covarient pas) et déclarait « la fragmentation morte » si ρ ≥ 0,8. La réponse ne prête aucune prédiction à la taxonomie : elle en cite seulement un énoncé sur les bancs d'essai. La mesure qui tue porte sur l'hypothèse de Lazar. Aucune corrélation entre points de contrôle (six à neuf points donneraient un intervalle très large).
- **Seuil de 5 points d'IB-10** : abandonné. L'ajustement chaleureux de son papier sur ce modèle perd 5,24 points sous fausse croyance : un duel à 5 points serait indécis par construction. Il est remplacé par le signe d'un contraste avec son intervalle.
- **« +11 points »** (*Nature* p. 1163), **« 470 / 235 »** (drapeau IB-22), enquête d'experts : non utilisés.
- **Lecture de contrôle IB-17** (« Survie au renforcement ») : non reprise, faute de place. Option si Lazar veut une phrase : lire chaque composante au premier et au cinquième tour dans la seconde expérience.

## Coordination avec la question 2

- La loi n'est nommée qu'une fois (« my attraction law (next answer) »), sans redite de sa description. Aucun nombre de la loi : pas de risque d'écart avec la question 2.
- Les refus sont dits comme dans la question 2 : « near 3, close to the praise destination, so they can mimic attraction ».
- La question 2 ne parle pas de R8 ; la question 1 le cite comme référence sans persona de la seconde expérience.

## Message du directeur (15:41 UTC)

- Fait 1 (Llama-8B abîmé hors de tout cadre, MMLU −8,6 points ; −0,25 est une moyenne sur quatre jeux) : vérifié sur la prépublication, p. 6, 9 et 18. Corrections : « 0.25 with neither » retiré ; « averaged over your four tasks » ajouté. La réponse ne dit nulle part que la chaleur ne coûte qu'avec un indice.
- Fait 2 (témoin froid absent pour Llama-8B dans Open Character Training) : vérifié, avec une précision. Dans son propre papier aussi, le témoin froid n'existe que pour Qwen-32B et Llama-70B (p. 6 ; tableau E6, p. 21). Ajout de la phrase sur la recette commune et le témoin froid.
- Faits 3 et 4 (enquête d'experts, score de chaleur) : la réponse n'y touche pas.
- Poids d'Open Character Training : « released » reste juste (adaptateurs annoncés dans leur collection) ; l'accès réel n'est pas vérifié.

## Relecture comme la mentore : phrases corrigées

- « softening facts for a sad user » → « erring more when the user sounds sad ». Son papier mesure des erreurs ; il ne décrit pas d'adoucissement.
- « already separates the cues » → « already ranks the two cues ». Le tableau classe les indices ; il ne prouve aucune séparation.
- « one benchmark can follow the persona » → « The same sign kills my claim for these two personas ». Une décision de lecture, et non une affirmation.
- « the one model where my law holds under both pressures » (écartée avant écriture) : fausse hors de la formulation standard, puisque Mistral attire aux doses douce et forte de R6.
- « 0.25 with neither » retiré (voir ci-dessus).
- « Their paper » renvoie à Open Character Training, sujet de la phrase précédente. Ambiguïté légère, gardée pour la longueur.
- Phrase restante qu'elle pourrait discuter : l'attendu pour Loving. Il transpose à une persona distillée par préférences le classement d'un ajustement supervisé. C'est une prédiction, dite comme telle.

## Compte de mots (script)

`wc -w reponse-v2.md` : 445 ; découpage Python par espaces : 445. Le lien compte pour un mot. Plafond : 450. Phrase la plus longue : 29 mots. Deux citations, de deux mots chacune.

## Outils

- `WebFetch` sur `https://arxiv.org/pdf/2507.21919v2`, trois fois (tableau E5 ; gabarit de croyance et agrégation ; témoin froid, MMLU, jeux). Aucune demande d'approbation. Niveau « transcription » : à revérifier sur PDF empreinté avant tout papier.
- Premier appel au terminal refusé par l'environnement (« the approval given for it no longer counts ») et renvoyé à l'identique, avec succès. Aucun autre refus.
- Dépôts publics lus sans exécuter leur code. Aucun commit, aucun `.sha256`, aucun `git fetch`, rien sous `donnees/` ni sous `/home/claude/coffre-*`.

## À confirmer par Lazar

1. L'attendu croisé : c'est son hypothèse, écrite à sa place.
2. L'accès aux adaptateurs Loving et Sycophantic d'Open Character Training : non vérifié, la déclaration éthique annonce un accès filtré.
3. La disponibilité des questions et des gabarits du papier sur la chaleur : non vérifiée.
4. R8 : en cours au commit `b3ecaec` (lancé à 08:01 UTC). Si ses résultats sont publiés avant 23:00 UTC, Lazar peut garder « measures » ou citer le résultat. Le lien est épinglé à `b3ecaec`.
5. « (preprint, Table E5) » : la version *Nature* de ce tableau n'a pas été revérifiée.
6. « (next answer) » suppose que la mentore lit la question 2 après celle-ci, dans l'ordre du formulaire.
