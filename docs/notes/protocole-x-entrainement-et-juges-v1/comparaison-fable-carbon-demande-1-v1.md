# Demande 1 (entraîner plutôt que détecter) — comparaison de la réponse de Fable et de celle de Carbon — v1

- 24 novembre 2026, vers 11:55 UTC (`date -u`). Auteur : Claude Fable 5.2, session du protocole X. Pièce de travail (classe C). Aucun chiffre de résultat de la base boîte noire.
- Pièces comparées : `reponse-fable-demande-1-v1.md` (`cc167c06…`) et `reponse-carbon-demande-1-v1.md` (`aa55515e…`), rendue sous l'accord `GO-2026-11-24-16` (30 274 jetons de réflexion, 8 853 de texte, fin normale, 1,67 USD au tarif haut). Carbon a lu la demande reformulée et le dossier de faits ; il n'a pas lu ma réponse. Sa réponse fait 5 037 mots pour 3 500 demandés.
- Les pièces de seconde main sur lesquelles les deux réponses s'appuient ont été relues sur PDF après coup (`dossier-faits-demande-1-v1-erratum-1.md`).

## En quatre lignes

1. Les deux réponses s'accordent sur le diagnostic : « sans ré-entraînement de poids » décrit un calendrier, et le papier ne montre pas qu'il faut entraîner plutôt que détecter.
2. Elles divergent sur la suite. Je recommande d'ouvrir l'entraînement dans une forme bornée (confiance 0,6). Carbon recommande de ne pas ouvrir l'entraînement de l'agent comme parade dans le premier papier (confiance 0,8), et d'entraîner autre chose : des témoins bénins, puis les sondes seules.
3. L'écart réel est plus étroit que les deux chiffres. Les deux mettent en premier la même épreuve, et renvoient au même moment la mesure la plus chère.
4. Carbon apporte trois choses que je n'avais pas : un piège dans le réglage des doses par consigne, le réapprentissage des sondes seules comme réponse principale, et une suite de trois épreuves qui ordonne les priorités.

## Ce que chacun propose

| | Fable | Carbon |
|---|---|---|
| « Sans ré-entraînement de poids » | juste ; hypothèse de calendrier, non doctrine | juste pour le saboteur à consigne cachée ; quatre angles morts |
| « Entraîner plutôt que détecter » résume-t-il le papier ? | à moitié : le papier choisit l'entraînement et mesure un juge | non : c'est un cadrage posé en page 2, non une conclusion |
| Première chose à faire | éprouver la tenue des organismes à un entraînement sans contenu (récompenses au hasard, réglage fin bénin, bruit sur les poids), après la porte de fin décembre | la même épreuve, coupée en deux : témoins bénins avant fin décembre, récompenses au hasard en janvier et février |
| Entraîner l'agent comme parade | oui, borné : lire, dans le bras d'attaque déjà prévu, ce que l'entraînement fait au dommage ; puis mesurer si une sonde dit ce qu'un entraînement a laissé, si les organismes tiennent | non dans le premier papier ; la même mesure est renvoyée à un second papier, ou ouverte si le jury la demande |
| Entraîner les moniteurs seuls | nommé comme forme déjà présente, suspendue à un heurt non tranché avec la règle de l'oracle | recommandé en premier ajout : réapprendre les sondes seules sur la part d'épisodes audités, avec deux oracles séparés |
| Organismes faits par d'autres | en parallèle, sur ton mot (changement de modèle) | second papier ; question plus précise : distinguer un frein volontaire d'un plafond honnête |
| Confiance | 0,6 | 0,8 |

## Accords

- La phrase que tu commentes (tirée d'une réponse antérieure de Carbon au lecteur des verdicts) décrivait un calendrier pour l'organisme à consigne cachée, dont aucun poids ne change.
- Le papier suppose qu'un entraînement converge et mesure la qualité du juge contre lequel on entraînerait. Ses expériences principales n'entraînent aucun modèle. Son annexe laisse un dommage que la note faible ne voit plus (page 84).
- La lignée du papier garde une place à la détection : orienter l'entraînement, valider ce qu'il a obtenu, établir qu'un sabotage a lieu.
- L'épreuve de tenue des organismes vient avant toute mesure d'entraînement comme parade. Un organisme fait par distillation d'une consigne peut céder à un entraînement quelconque (Ryd et al., pages 30 et 31).
- Ni l'entraînement orienté par le soupçon des sondes, ni la pénalité de sonde dans la récompense, ne s'ouvrent maintenant.
- Refaire l'annexe du papier à son échelle est hors de portée.
- Aucune absence de travaux n'est à dire comme un vide établi.

## Désaccords

1. **La mesure « une sonde dit-elle ce qu'un entraînement a laissé ? » entre-t-elle dans le premier papier ?** Je dis : oui si l'épreuve de tenue montre un organisme qui résiste. Carbon dit : second papier. Ses raisons : trois chantiers au plus, la décision du 21 novembre qui laisse la correction par l'entraînement fermée, et le risque d'un apprentissage par renforcement instable à huit milliards de paramètres. Deux de ces trois raisons sont les règles en vigueur, que ta question propose justement de rouvrir : le « non » de Carbon est en partie une déférence au dossier.
2. **Quand fabriquer les témoins bénins ?** Carbon : avant fin décembre, comme condition de validité des sondes. Moi : aucune carte pour ce bras avant la porte. Sur ce point Carbon a un argument que je n'avais pas pesé (voir « neuf », point 2), et le témoin distillé honnête est déjà une réserve connue du programme.
3. **Le réapprentissage des sondes seules.** Carbon en fait la réponse principale à « on ne va pas aborder l'entraînement ? ». Je l'avais rangé parmi les formes suspendues. Je me range à son avis sur la priorité : c'est la façon la moins chère d'aborder l'entraînement, et Greenblatt la nomme comme compromis. Elle demande que tu tranches un nœud laissé ouvert le 21 novembre.
4. **Le bras d'attaque.** Carbon propose de retirer l'optimisation avec gradient à travers la sonde, que Taufeeque et al. déconseillent (page 8). Je ne sais pas ce que le montage du bras d'attaque prévoit : je n'ouvre pas cette conception.

## Ce que Carbon apporte de neuf

1. **Le piège du réglage des doses.** Si les consignes de dose de l'organisme à consigne cachée sont ajustées en regardant le dommage mesuré par l'oracle, l'agent est choisi par l'oracle, ce que la règle interdit. Parade proposée : fixer les consignes d'avance, ou sur un jeu auxiliaire banni de l'évaluation. À faire vérifier par une session non exposée : le protocole de dose prévu le respecte-t-il ?
2. **Le transfert croisé.** Évaluer les sondes sur les nouvelles doses oblige à les apprendre sur une famille et à les lire sur l'autre. Or l'une a un adaptateur et l'autre non : une sonde peut lire l'adaptateur. D'où la demande de témoins bénins avant la porte.
3. **Deux oracles.** Pour réapprendre les sondes sur la part auditée sans heurter la règle de l'oracle : un oracle d'audit, employé sur l'échantillon tiré au hasard, et un oracle d'évaluation contre le jumeau honnête, jamais employé pour apprendre.
4. **Trois épreuves légères qui ordonnent les ajouts.** La sonde bat-elle un classifieur de texte appris sur les mêmes étiquettes, et tient-elle sur un témoin bénin ? Une personne sépare-t-elle le jumeau honnête du saboteur à huit milliards de paramètres ? Le seuil d'alerte se transporte-t-il d'un lot de sujets à un autre sans jumeau honnête ? Chaque issue décide de la priorité suivante.
5. **Une question plus précise sur les organismes publics.** Une sonde distingue-t-elle un modèle qui freine exprès son exploration d'un modèle honnête qui plafonne, à récompense observée égale ?

## Ce qui est fragile

**Chez Carbon.**
- « Toute la lignée établit que l'entraînement sans détection est aveugle » : trop fort. La lignée écrit que la détection reste nécessaire à trois usages ; Taufeeque et al. concluent aussi qu'un détecteur lu sur les états internes peut servir de signal d'entraînement sous forte régularisation (page 1).
- L'effondrement du modèle de huit milliards de paramètres est invoqué contre toute forme d'entraînement de l'agent. La source le montre pour un entraînement contre un détecteur, à pénalité extrême (α = 100). L'imprécision venait de mon dossier (« sous forte pénalité ») ; elle est corrigée à l'erratum.
- « Un ou deux adaptateurs bénins » : la source citée dit elle-même que cela ne suffit pas (voir plus bas).
- La chute attendue de la sonde à 0,50 après entraînement : Taufeeque et al. la montrent pour des sondes apprises hors du domaine ; leurs sondes du domaine tiennent (pages 7 et 17).
- « Le papier écarte la détection sur la foi d'études sans accumulation dans le temps » : non vérifié. Les deux sources empiriques portent sur des moniteurs et des auditeurs qui lisent le texte ; le reste est une inférence de Carbon.
- Une part de ses ajouts existe déjà au programme sans qu'il puisse le savoir : le prédicteur obligatoire sur les traits du texte, la déclaration de la référence honnête, l'ancre de jugement des lecteurs.
- Tous les coûts sont des ordres de grandeur, comme les miens.

**Chez moi.**
- Ma forme « lire l'attaque comme une cure » dépend d'un bras d'attaque que je ne connais pas, sur un modèle dont un voisin montre l'effondrement à pénalité extrême.
- J'ai écrit « aucune carte avant la porte » sans peser que la validité des sondes entre les deux familles dépend d'un témoin bénin.
- Ma confiance de 0,6 portait sur un ensemble de trois pas ; le troisième est le plus contesté.

## Références

**Relues sur PDF ce jour, après les deux réponses** (détail à l'erratum 1 du dossier) :
- Soopal et al. (arXiv 2611.14950 v1), pages 1, 2, 6, 8. Le chiffre de 99 % tient. **Le témoin bénin apparié ne répare le défaut que dans une même course d'entraînement** : appliquée à d'autres courses, la sonde passe la règle de transfert des auteurs dans 1 pli sur 5, 2 sur 5 avec trois recettes bénignes. L'épreuve utile est donc un transfert entre courses indépendantes, avec plusieurs recettes, et non un témoin unique.
- Boxo et al. (arXiv 2509.21344 v2), page 1 : baisse de 10 à 30 points quand les indices du texte sont retirés.
- Taufeeque et al. (arXiv 2602.15515 v2), pages 7, 8, 17.
- Gan et al. (arXiv 2604.16286 v2), pages 1, 7, 10.

**À vérifier avant tout emploi.**
- Gasteiger et al. (mars 2025) : repris d'une lecture du 20 novembre, non relu.
- L'antériorité de chaque mesure nommée « question ouverte » par l'une ou l'autre réponse : quatre requêtes seulement ont été faites.
- Ce que le protocole de dose de l'organisme à consigne et le montage du bras d'attaque prévoient : par une session non exposée.

## Ce que j'en retiens

Je garde le cœur de ma recommandation et je la corrige en trois points.

1. **J'ajoute le réapprentissage des sondes seules sur la part auditée**, comme première réponse à « aborder l'entraînement ». Il ne coûte presque rien en calcul. Il demande ta décision sur le nœud laissé ouvert le 21 novembre.
2. **Je remonte les témoins bénins**, et je les précise : plusieurs recettes, plusieurs courses, règle de transfert écrite d'avance. Leur place avant ou après la porte de fin décembre est ta décision ; elle dépend du chemin critique, que la mère connaît mieux que moi.
3. **Je baisse ma confiance sur l'entrée de la mesure la plus chère dans le premier papier.** Elle reste conditionnée à la tenue des organismes ; j'ajoute qu'elle peut devenir un second papier sans rien perdre, si l'épreuve de tenue et le bras d'attaque donnent déjà la figure qui répond au papier.

Confiance dans le plan ainsi corrigé : 0,65. Le collisionneur, s'il est accordé, donnera trois autres avis sur la même question.
