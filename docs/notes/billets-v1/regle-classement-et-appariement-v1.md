# Règle de classement et d'appariement des billets — v1

Écrite et scellée **avant** tout classement (tâche 2 du mandat `mandat-corpus-et-grille-v1.md`), le 2026-11-18. Aucun texte de billet n'a été ouvert avant ce scellement ; seules les métadonnées (titre, votes, étiquettes, longueur) ont été tirées.

## Étiquettes retenues (identifiants trouvés par requête)
Contrôle de l'IA « AI Control » `F5gRQdEQHzi3tQ5Ay` ; surveillance non fiable « Untrusted Monitoring » `aahN8N35xGokCKd4g` ; interprétabilité « Interpretability (ML & AI) » `56yXXrcxRjrQs6z9R` ; tromperie « Deception » `cHoCqtfE9cF7aSs9d` ; alignement trompeur « Deceptive Alignment » `KEAWfxwjitNJFrC68` ; extraction du savoir latent « Eliciting Latent Knowledge » `mSTmKrSkFBswHaS3T` ; sous-performance délibérée « Sandbagging (AI) » `hMPBEPfDwSwoqYYAQ`. Le site n'a **aucune étiquette « sondes »** (recherche sur les 1019 étiquettes : aucune ne contient « probe ») ; les billets de sondes tombent sous l'interprétabilité ou l'extraction du savoir latent.

## Règle de fond (mot du mandat)
Est « billet de résultats empiriques » un billet qui rapporte une expérience **des auteurs** avec **au moins un chiffre ou une figure de résultat**.

## Opérationnalisation par programme (le classement est fait par programme, pour que l'agent n'ouvre pas le texte de la future moitié tenue à l'écart)
Sur le texte du billet (format markdown rendu par le site), un billet est classé « résultats » si et seulement si les trois conditions tiennent :
1. **Expérience des auteurs** : au moins deux occurrences de marqueurs d'expérience à la première personne (liste fermée dans `scripts/classer_et_apparier_v1.py`, par exemple « we train », « we find », « we found », « our results », « we evaluate », « we ran », « our experiments », « I trained », « I ran », « I found », « we measure », « we fine-tune »…).
2. **Chiffre ou figure de résultat** : au moins une image dans le corps, **ou** au moins deux nombres de résultat (pourcentage, décimal entre 0 et 1 à deux chiffres au moins, ou nombre suivi d'une métrique nommée : accuracy, AUROC, AUC, loss, F1, recall, precision, success rate, win rate, correlation).
3. **Longueur** : au moins 300 mots (en dessous, le billet est presque toujours un lien vers un article sans le texte ; exclu comme non codable).
Sont exclus d'office : questions, événements, brouillons.
Classe « autre » sinon. Le taux d'erreur du classement est mesuré **après** le partage, sur la seule moitié « développement », par lecture humaine-agent, et rapporté.

## Billets bien notés
Par année civile (2022 à 2026 ; 2026 partielle jusqu'au jour du tirage), les 15 billets classés « résultats » au plus haut score du site (`baseScore`).

## Appariement peu noté
Pour chaque billet bien noté, dans l'ordre décroissant des scores, le candidat apparié est choisi parmi les billets :
- de la même année, classés « résultats » (même classe, pour que la comparaison porte sur la rédaction et non sur le genre) ;
- dans le tiers bas des scores de l'année (tous billets de l'année portant une étiquette retenue, toutes classes) ;
- partageant au moins une étiquette retenue avec le billet bien noté ;
- de longueur comparable : rapport des nombres de mots entre 0,67 et 1,5 ;
- non déjà apparié.
Parmi eux : d'abord le plus grand recouvrement d'étiquettes retenues (indice de Jaccard), puis le plus petit écart de longueur en logarithme, puis l'identifiant (ordre lexical). Si aucun candidat : « sans apparié », consigné.

## Commentaires
Pour chaque billet bien noté : les dix commentaires au plus haut score (vue `postCommentsTop` du site), réponses comprises.

## Partage
Graine `numpy.random.SeedSequence` consignée au manifeste ; unité de partage : la **paire** (billet bien noté, son apparié et ses commentaires vont ensemble), stratifiée par année ; chaque strate année est coupée en deux moitiés (la moitié impaire va au hasard). Les billets bien notés sans apparié forment leur propre strate par année. Ainsi le partage est stratifié par année et par classe (bien noté / peu noté) à la fois.
