# Faut-il aborder l'entraînement ? Note de fin de dossier sur ta première demande

24 novembre 2026, 12:45 UTC. Quatrième version (la troisième n'a pas été écrite) : le fond de la deuxième, trois figures tracées par programme, et une section neuve sur l'ordre et le calendrier des deux propositions, après tes mots de 12:10 UTC. Aucun chiffre neuf. La section neuve et les figures sont rédigées par la session du protocole X après le changement de modèle de 12:11 UTC (voir la passation). Pour Lazar. Rédigée par Claude Fable 5.2 (session du protocole X), à partir de sa propre réponse, de celle de Carbon et des pièces relues à la page. Note de travail, non contre-lue. Elle ne porte aucun chiffre de résultat du programme. Le collisionneur n'a pas tourné : son devis attend l'arbitrage de la session mère.

## 1. La réponse en dix lignes

**Pourquoi « sans ré-entraînement de poids » ?** Parce que la phrase parle de la courbe dose-réponse du saboteur à consigne cachée, qui manque encore au critère des saboteurs de la porte de fin décembre, et que ce saboteur ne change aucun poids : sa dose se règle dans sa consigne. La phrase décrit un calendrier. Elle n'est pas un refus de principe.

**Le papier recommande-t-il d'entraîner plutôt que de détecter ?** Il le tient pour acquis plus qu'il ne le montre. Sa lignée soupçonne que l'entraînement est le plus fort des deux contre le diffus ; le papier part de là, en une phrase de cadrage. Puis il mesure autre chose : ce que vaut le juge contre lequel on entraînerait. Ses expériences principales n'entraînent aucun modèle, et aucune ne compare l'entraînement à la détection.

**On ne va pas aborder l'entraînement ?** Si, et par trois portes de coût croissant : entraîner les sondes seules ; éprouver si nos saboteurs tiennent à un entraînement ; lire ce qu'un entraînement laisse derrière lui. Aucune n'entre dans le chemin de la porte de fin décembre.

**Cela renforcerait-il le papier ?** Oui, à une condition que personne n'a vérifiée : que nos saboteurs résistent à un entraînement quelconque. Sinon la mesure lirait leur fabrication, comme la marge asymétrique que tu as retirée le 21 novembre.

Carbon et moi sommes d'accord sur le diagnostic et sur la première épreuve. Nous divergeons sur l'ampleur : j'ouvrirais l'entraînement de l'agent sous une forme bornée ; Carbon le garderait hors du premier papier.

## 2. Cinq sens du mot « entraînement »

Le mot recouvre cinq gestes. Les confondre fait croire que le programme refuse ce que le papier recommande.

| Sens | Ce que c'est | Le plan de fin décembre en a-t-il besoin ? |
|---|---|---|
| Fabriquer le saboteur | inscrire le sabotage dans les poids | non pour le saboteur à consigne ; oui pour un témoin bénin (voir section 6) |
| Entraîner comme parade | corriger le modèle soupçonné en l'entraînant | non ; c'est la question que tu poses |
| Entraîner contre un moniteur | l'agent apprend à faire baisser un score de sonde ou de juge | non ; interdit hors d'un bras d'attaque déclaré, prévu à la phase suivante |
| Entraîner les moniteurs | apprendre ou réapprendre les sondes | oui : une sonde s'apprend, et ne s'évalue jamais sur les saboteurs qui l'ont apprise ; aucun poids de l'agent ne bouge |
| Apprendre en service | mettre le modèle à jour pendant son emploi | non ; hors du banc |

## 3. Ce que le papier dit, à la page

Le papier est « Diffuse AI Control on Fuzzy Tasks » (Terekhov, Gulcehre, Hebbar, Benton ; arXiv 2606.08892, version 3, 84 pages).

**Ce qu'il établit.**

- Un juge faible de confiance se laisse tromper par une consigne adverse : le modèle fort obtient 85,3 de note faible pour 34,7 de qualité réelle approchée ; honnête, il obtient 80,8 et 70,7 (figure 1, page 2).
- Une consigne de juge durcie résiste à leur attaque. Les auteurs la disent preuve d'existence : la trouver avec des moyens réalistes « remains an open problem » (page 2).
- En annexe, deux saboteurs à consigne entraînés contre la note faible arrivent à la même note et gardent des qualités réelles différentes : « The recovery is still not perfect » (page 84). Cette annexe entraîne un modèle de cent vingt milliards de paramètres.

**Ce qu'il suppose.**

- Que la surveillance et l'incrimination « seem theoretically […] and empirically […] less promising for mitigating diffuse threats » (page 2 ; les crochets remplacent les renvois aux sources). C'est la phrase qui a donné « entraîner plutôt que détecter ». Elle renvoie à trois sources ; elle n'est suivie d'aucune comparaison.
- Qu'un entraînement suffisant porte la note faible près de son maximum, « absent exploration hacking », c'est-à-dire si le modèle ne se retient pas d'explorer (page 3).

**Ce qu'il laisse ouvert.**

- Le cas d'un vrai modèle saboteur affiné contre la note faible, parce que la réponse dépend de la façon dont la propension est inscrite dans les poids (page 83).
- Toute lecture des états internes : aucune de ses expériences n'en fait.

**Sa leçon, dite exactement** : un entraînement vaut ce que vaut le signal contre lequel on entraîne. Ce n'est pas « ne mesurez pas, entraînez ».

## 4. Ce que dit la lignée du papier

Les travaux dont le papier descend gardent à la détection quatre emplois.

1. **Orienter l'entraînement.** Hebbar (billet du 30 avril 2025) écrit : « We suspect that training and incrimination are complementary -- training is stronger against high-action-count strategies with subtle actions, while incrimination is stronger against low-action-count strategies with egregious actions. » La phrase du papier a donc un fondement dans sa lignée : contre le diffus, l'entraînement y est tenu pour le plus fort des deux. Mais entre le sabotage concentré et le sabotage diffus, le même billet décrit un régime où l'on entraîne plus fort sur les actions les plus suspectes : il faut un détecteur pour les classer.
2. **Valider l'entraînement.** Taylor et al. (arXiv 2512.07810, page 25) écrivent qu'entraîner peut être plus praticable que détecter, et que la détection reste nécessaire pour établir qu'un sabotage a lieu et pour « validate that elicitation efforts are succeeding ».
3. **Garder les suppositions de l'entraînement.** L'entraînement doit être indiscernable du service (Ryd et al., arXiv 2604.22082, page 1). Des saboteurs publics résistent à un apprentissage par renforcement ; leurs auteurs nomment les sondes comme piste, sans les essayer (Jang et al., arXiv 2604.28182, pages 16 et 27).
4. **Tenir sous l'entraînement.** Un apprentissage en service entraîne la politique contre le moniteur, sans intention de nuire (Mallen, billet du 25 septembre 2026). Un entraînement ordinaire fait perdre leur pouvoir à des sondes apprises hors du domaine ; les sondes du domaine tiennent (Taufeeque et al., arXiv 2602.15515, pages 7 et 17).

Une cinquième pièce compte pour toi : Greenblatt (notes du 24 mars 2025) nomme un compromis, n'entraîner en ligne que les moniteurs, sondes comprises. C'est une façon d'aborder l'entraînement sans toucher à l'agent.


![**Figure 1.** Autour d'un entraînement du modèle soupçonné, la lignée du papier garde une détection à quatre endroits : orienter ce qu'on entraîne, valider ce qu'on a obtenu, garder les suppositions de l'entraînement, et tenir pendant qu'il se déroule. Sources : section 4 de cette note (Hebbar ; Taylor et al., page 25 ; Ryd et al., page 1 ; Jang et al., pages 16 et 27 ; Taufeeque et al., pages 7 et 17 ; Mallen). *Figure tracée par programme (`figures_notes_v4.py`, `aeb418f5…`), vectorielle.*](figures-v4/e3-quatre-emplois-de-la-detection.svg){width=100%}

## 5. Les formes possibles, de la moins chère à la plus lourde

Les coûts sont des ordres de grandeur, sans mesure.

| Forme | Question posée | Coût | Règle touchée | Avis de Fable | Avis de Carbon |
|---|---|---|---|---|---|
| Réapprendre les sondes seules sur la part d'épisodes audités | l'audit tiré au hasard suffit-il à garder les sondes justes quand le terrain change ? | quelques dizaines de dollars | la lettre de la règle « aucune sortie de l'oracle dans la sélection d'un moniteur » | nommée, suspendue à ton arbitrage | premier ajout, avec deux oracles séparés |
| Témoins bénins : adaptateurs entraînés sans sabotage | la sonde lit-elle le sabotage, ou le fait d'avoir été entraîné ? | quelques heures de carte | aucune | dans la fiche de validité, après la porte | avant la porte de fin décembre |
| Épreuve de tenue des saboteurs à un entraînement sans contenu | le sabotage survit-il à des récompenses tirées au hasard ? | une dizaine de dollars | aucune | premier pas, après la porte | en janvier et février |
| Lire l'attaque comme une cure, dans le bras d'attaque prévu | quand le score de sonde baisse, le dommage baisse-t-il aussi ? | marginal | aucune de plus | deuxième pas | non proposée sous cette forme |
| Lire ce qu'un entraînement contre une note faible a laissé | à note faible égale, la sonde classe-t-elle les dommages restants ? | de quelques dizaines à quelques centaines de dollars ; plusieurs semaines | « aucun score de moniteur dans l'entraînement de l'agent » : bras déclaré, donc ton mot | troisième pas, si les saboteurs tiennent | second papier |
| Sondes sur des saboteurs publics qui résistent à l'entraînement | la sonde voit-elle un frein volontaire ? | de dix à cent dollars | changement de modèle : ton mot | en parallèle | second papier |
| Entraîner l'agent selon le soupçon des sondes | corrige-t-on avec moins d'étiquettes que le hasard ? | plus de cent dollars, plusieurs mois | les deux règles | plus tard | non |
| Refaire l'annexe du papier à son échelle | — | hors de portée | — | non | non |


![**Figure 2.** Carte des formes d'un bras « entraînement » : en abscisse, le coût tel que la note le dit, par ordre croissant ; en ordonnée, la règle du programme que la forme touche. Carrés gris : les trois portes retenues et leurs préalables (sondes seules ; tenue des saboteurs et témoins bénins ; lire ce qu'un entraînement laisse). Les coûts sont des ordres de grandeur [supposé]. Source : section 5 de cette note. *Figure tracée par programme (`figures_notes_v4.py`, `aeb418f5…`), vectorielle.*](figures-v4/e1-carte-des-portes.svg){width=100%}

## 6. Ce que Carbon apporte, et ce que la relecture a changé

**Trois apports de Carbon que je n'avais pas.**

1. **Un piège dans le réglage des doses.** Si les consignes de dose du saboteur à consigne sont ajustées en regardant le dommage mesuré par l'oracle, l'agent est choisi par l'oracle, ce que ta règle interdit. Parade : fixer les consignes d'avance, ou sur un jeu banni de l'évaluation. Je ne sais pas ce que le protocole de dose prévoit ; je n'ouvre pas cette conception.
2. **Le réapprentissage des sondes seules comme première réponse**, avec un oracle d'audit distinct de l'oracle d'évaluation.
3. **Trois épreuves légères qui ordonnent les priorités** : la sonde bat-elle un classifieur de texte appris sur les mêmes étiquettes ; une personne sépare-t-elle le jumeau honnête du saboteur ; le seuil d'alerte se transporte-t-il d'un lot de sujets à un autre.

**Ce que la relecture sur PDF a changé.** Carbon et moi citions Soopal et al. (arXiv 2611.14950) pour demander « un témoin bénin ». Relu aux pages 1, 2, 6 et 8 : une sonde apprise contre le modèle de base signale 99 % des exemples d'adaptateurs bénins ; un témoin bénin apparié répare ce défaut dans une même course d'entraînement, et non d'une course à l'autre (la règle de transfert des auteurs passe dans 1 pli sur 5, 2 sur 5 avec trois recettes bénignes). **Un seul témoin ne suffit donc pas** : il faut plusieurs recettes, plusieurs courses, et une règle de transfert écrite d'avance. Le cadre de cette source est étroit (petits modèles, problèmes à réponse exacte).

**Ce qui est fragile chez Carbon.**

- Il écrit que la lignée « établit » que l'entraînement sans détection est aveugle. La lignée dit moins : la détection reste nécessaire à certains emplois.
- Il invoque l'effondrement d'un modèle de la taille du nôtre contre toute forme d'entraînement de l'agent. La source le montre pour un entraînement contre un détecteur, à pénalité extrême. L'imprécision venait de mon dossier ; elle est corrigée.
- Son « non » s'appuie en partie sur les règles en vigueur (trois chantiers, décision du 21 novembre), que ta question propose justement de rouvrir.
- Sa réponse dépasse la longueur demandée (5 037 mots pour 3 500).

**Ce qui est fragile chez moi.**

- Ma forme « lire l'attaque comme une cure » dépend d'un bras d'attaque que je ne connais pas.
- J'avais écrit « aucune carte avant la porte » sans peser que la validité des sondes entre les deux familles dépend d'un témoin bénin.

## 7. Propositions retenues, et pourquoi

1. **Trancher le réapprentissage des sondes seules.** C'est la réponse la moins chère à « aborder l'entraînement », elle a un nom dans la lignée, et elle ne touche pas à l'agent. Elle heurte la lettre d'une règle : c'est ta décision.
2. **Établir la fiche de validité des saboteurs** : tenue à un entraînement sans contenu ; témoins bénins sur plusieurs courses. Les deux réponses la mettent en premier. Sans elle, toute mesure d'entraînement est illisible.
3. **Ajouter au bras d'attaque déjà prévu une lecture du dommage**, sous réserve de sa conception par une session non exposée. Le coût est marginal.
4. **Garder fermée, pour l'instant, la mesure la plus chère** (lire ce qu'un entraînement a laissé). Elle redevient une question après la fiche de validité.
5. **Ne pas retenir** l'entraînement orienté par le soupçon ni la refonte de l'annexe du papier : les règles touchées et les moyens demandés sont hors de proportion.

Ma confiance dans cet ensemble : 0,65. J'avais 0,6 avant de lire Carbon ; lui donne 0,8 à une version qui garde l'entraînement de l'agent hors du premier papier.

## 7 bis. Ordre et calendrier des deux propositions

**Proposition, à revoir par Fable si Lazar le veut.** Tes mots de 12:10 UTC (`GO-2026-11-24-21`) : faire les deux propositions, celle de Fable et celle de Carbon, dans un ordre à déterminer ; et inscrire au programme : **« la première épreuve est de vérifier que nos organismes tiennent face à un entraînement sans contenu »** (inscription faite par la session du dossier de l'entretien).

| Pas | Quoi | Vient de | Dépend de | Quand [proposé] | Coût [supposé, repris des notes] |
|---|---|---|---|---|---|
| 1 | **Tenue des saboteurs à un entraînement sans contenu** : récompenses tirées au hasard, réglage fin bénin de même recette, bruit sur les poids ; dommage mesuré contre le jumeau honnête | Fable (forme A) ; Carbon ; collisionneur ; **mot de Lazar : la première épreuve** | un devis ; une conception d'épreuve par une session non exposée | décembre, avant la porte si le chemin critique le permet | une dizaine de dollars ; une semaine |
| 2 | **Témoins bénins** : plusieurs recettes, plusieurs courses d'entraînement, règle de transfert écrite d'avance | Carbon ; collisionneur ; relecture de Soopal et al. | un devis ; même outillage que le pas 1 | décembre, dans la même location que le pas 1, lu après lui | quelques heures de carte |
| 3 | **Instruction du nœud de la règle de l'oracle** (réapprendre un moniteur sur la part auditée) par une session non exposée, puis décision de Lazar | Carbon (deux oracles séparés) | rien | en parallèle, décembre, écriture seule | aucune dépense |
| 4 | **Sondes seules réapprises sur la part auditée** | Carbon (premier ajout) ; Greenblatt | pas 2 réussi ; pas 3 tranché | janvier | quelques dizaines de dollars |
| 5 | **Lire l'attaque comme une cure** : au bras d'attaque déjà prévu, suivre ensemble le score de sonde et le dommage | Fable (forme B) | pas 1 ; calendrier du bras d'attaque ; écrit dans son préenregistrement | avec le bras d'attaque, phase suivante | marginal |
| 6 | **Lire ce qu'un entraînement laisse** : à note faible égale, la sonde classe-t-elle les dommages restants ? | Fable (forme C) ; Carbon la renvoyait à un second papier | pas 1 montre un saboteur qui tient ; pas 2 montre une sonde qui lit le sabotage ; bras déclaré accordé | février et mars au plus tôt, ou second papier | de quelques dizaines à quelques centaines de dollars ; plusieurs semaines |

**Pourquoi cet ordre.**

1. **La tenue d'abord**, parce que toute mesure d'entraînement sur un saboteur fragile lit sa fabrication : un organisme fait par distillation d'une consigne a été remis d'aplomb par de simples récompenses tirées au hasard (Ryd et al., pages 30 et 31). C'est aussi le mot de Lazar.
2. **Les témoins bénins ensuite, dans la même location**, parce qu'ils emploient le même outillage d'adaptateurs ; on les lit après la tenue pour que la première épreuve reste la première. Sans eux, une sonde peut lire l'adaptateur et non le sabotage, et un témoin d'une seule course ne suffit pas (Soopal et al., pages 6 et 8).
3. **Le nœud de l'oracle en parallèle**, parce qu'il ne coûte qu'une écriture et bloque le pas 4.
4. **Les sondes seules avant toute lecture d'entraînement de l'agent**, parce que c'est la porte la moins chère, qu'elle ne touche pas à l'agent, et qu'elle a un nom dans la lignée (Greenblatt).
5. **La lecture de l'attaque avec le bras d'attaque**, parce qu'elle n'ajoute qu'une lecture à une course prévue.
6. **La mesure la plus chère en dernier**, parce qu'elle a besoin des trois réponses précédentes : un saboteur qui tient, une sonde qui lit le sabotage, et un bras déclaré.

**Ce qui ferait changer l'ordre.**

- Le pas 1 montre que rien ne tient à notre échelle : on garde les pas 2 à 5 et on retire le pas 6 ; la famille sans texte de consigne passe en priorité de devis.
- Le pas 2 montre que la sonde lit l'adaptateur : le pas 4 attend une sonde corrigée ; le pas 6 est suspendu.
- Le chemin critique de la porte de fin décembre ne laisse pas de place : les pas 1 et 2 glissent en janvier, sans changer d'ordre.
- Le collisionneur, s'il finit, rend un ordre différent : on compare, on note l'écart, Lazar tranche.

![**Figure 3.** Ordre et calendrier proposés pour les deux propositions. Barres : période de chaque pas ; flèches : « précède ». Lignes tiretées : l'entretien du 1er décembre, la porte des instruments de fin décembre, et la porte de comparaison, environ deux mois après. Les pas 1 et 2 ne sont pas sur le chemin critique de la porte ; s'il ne leur laisse pas de place, ils glissent en janvier sans changer d'ordre. Proposition, à revoir par Fable si Lazar le veut. Source : `ordre-et-calendrier-deux-propositions-entrainement-v1.md`. *Figure tracée par programme (`figures_notes_v4.py`, `aeb418f5…`), vectorielle.*](figures-v4/e2-ordre-et-calendrier.svg){width=100%}


## 8. Décisions

**A. Le réapprentissage des sondes seules sur la part d'épisodes audités** (nœud : il touche la lecture d'une règle ; aucun défaut ne s'applique). *Depuis tes mots de 12:10 UTC : il entre au plan (pas 4 de la section 7 bis) ; reste à trancher la règle de l'oracle (pas 3).*

- Enjeu : c'est la porte la moins chère vers l'entraînement, et le point laissé ouvert le 21 novembre.
- Option 1 : l'ouvrir, avec deux oracles séparés. Avantage : répond à ta question sans toucher à l'agent. Inconvénient : une règle se lit autrement.
- Option 2 : le laisser fermé. Avantage : rien ne bouge. Inconvénient : l'objection « vous n'entraînez rien » reste entière.
- Option 3 : le faire instruire d'abord par une session non exposée, puis trancher. Avantage : tu décides sur une conception contre-lue. Inconvénient : une à deux semaines.
- Recommandation : option 3. Confiance : 0,6.

**B. Les témoins bénins, avant ou après la porte de fin décembre** (dépense : sur devis).

- Enjeu : sans eux, une sonde apprise sur le saboteur à adaptateur peut lire l'adaptateur. Le banc compte déjà un adaptateur témoin ; le témoin distillé honnête manque (ta réserve). Ce que la relecture ajoute : un témoin d'une seule course ne suffit pas.
- Option 1 : devis maintenant, fabrication avant la porte. Option 2 : après la porte. Option 3 : pas de témoins.
- Recommandation : demander le devis maintenant et décider sur pièces ; la mère connaît le chemin critique mieux que moi. Confiance : 0,6.

**C. L'épreuve de tenue des saboteurs à un entraînement sans contenu** (dépense : sur devis). *Depuis tes mots de 12:10 UTC : c'est la première épreuve, inscrite au programme.*

- Recommandation : oui, comme premier pas de tout ce qui touche à l'entraînement. Confiance : 0,75.

**D. Ouvrir un bras déclaré « lire ce qu'un entraînement a laissé »** (nœud).

- Recommandation : pas maintenant ; décider après l'épreuve de tenue. Confiance : 0,65.

**E. Une recherche d'antériorité par un lecteur non exposé**, sur les travaux qui citent Hebbar, Ryd et al., Jang et al. et le papier (proposition avec recommandation ; sans dépense d'interface).

- Recommandation : oui. Défaut sous 48 heures : la mère la lance.

**F. Deux vérifications à confier à une session non exposée** : le protocole de dose du saboteur à consigne respecte-t-il la règle de l'oracle ; le bras d'attaque passe-t-il un gradient à travers la sonde, ce que Taufeeque et al. déconseillent (page 8).

**G. Une citation à instruire pour ta décision sur le plancher d'audit** : les notes de Greenblatt du 24 mars 2025 décrivent un entraînement en ligne sur une part d'actions tirées au hasard après exécution. Je ne les ai pas trouvées parmi les citations de cette décision.

**H. Le collisionneur sur « ce qui entre dans un programme amélioré et ambitieux »** : devis contre-lu, envoyé à la mère qui arbitre la clé partagée (15,90 USD au pire sans relance, de 6,0 à 7,3 attendus, ligne de 18 USD). Rien n'est lancé.

## 9. Pour l'entretien du 1er décembre

**À dire.** « Ce papier étudie ce vers quoi un entraînement convergerait, étant donné un juge. Il n'entraîne pas dans ses expériences principales, et son levier est un instrument de mesure. Sa lignée écrit quatre endroits où il faut encore détecter. Ma garantie vient d'un audit de l'issue. Je n'ai pas ouvert la correction par l'entraînement ; avant de l'ouvrir, je vérifie que mes saboteurs résistent à un entraînement. »

**À ne pas dire.** « Le papier montre que l'entraînement marche », ou « que la détection échoue ». « Personne n'a essayé de sondes sur ce point » : quatre requêtes ne font pas une recherche. « Sans réentraînement » comme un choix de principe. « La lignée du papier préfère la détection » : elle tient l'entraînement pour le plus fort contre le diffus, et garde à la détection les quatre emplois de la section 4.

## 10. Références

**Relues à la page ce jour.** Terekhov et al., pages 1 à 4, 10 et 80 à 84. Hebbar, billet du 30 avril 2025. Greenblatt, notes du 24 mars 2025. Ryd, Benton et Hebbar, billet du 13 novembre 2025. Ryd et al., pages 1, 4, 30 et 31. Taylor et al., page 25. Jang et al., pages 3, 10 à 12, 16 et 27. Taufeeque et al., pages 1, 7, 8, 9 et 17. Mallen, billet du 25 septembre 2026. Soopal et al., pages 1, 2, 6 et 8. Boxo et al., page 1. Gan et al., pages 1, 7 et 10.

**À vérifier avant tout emploi.** Gasteiger et al. (mars 2025), repris d'une lecture antérieure. L'affirmation de Carbon que les sources du papier ignorent l'accumulation dans le temps. L'antériorité de chaque mesure dite « question ouverte ».

## 11. Ce qui n'a pas été fait

- Aucune lecture en entier des voisins : pages citées seulement.
- Aucune recherche d'antériorité au-delà de quatre requêtes.
- Aucun chiffrage sur mesure.
- Aucune conception de saboteur, de sonde ni de moniteur : cette session a lu des résultats et en est exclue.
- Le collisionneur n'a pas tourné. La sous-question pour l'organisme d'idéation est écrite, non servie.

## Ce qui change depuis la deuxième version

1. Trois figures tracées par programme, chacune avec une légende qui se lit seule et ses sources.
2. Section 7 bis : l'ordre et le calendrier des deux propositions, après tes mots de 12:10 UTC ; décisions A et C annotées en conséquence.

## Ce qui changeait depuis la première version

1. Section 1 : la courbe du saboteur à consigne est dite manquer « au critère des saboteurs », non à la porte entière ; la réponse sur le papier passe de « non » à « il le tient pour acquis plus qu'il ne le montre », pour rendre justice à sa lignée.
2. Section 2 : la ligne « entraîner les moniteurs » reprend la règle telle qu'elle est écrite.
3. Section 3 : la citation de la page 2 marque ses coupes.
4. Section 4 : la phrase de Hebbar est citée en entier ; elle donne à l'entraînement l'avantage contre le diffus, ce que la première version ne disait pas.
5. Décision B : le banc compte déjà un adaptateur témoin.
6. Décision G : « à instruire », non « à ajouter ».
7. Section 9 : une phrase de plus à ne pas dire, sur ce que la lignée préfère.

## Pièces

Dans `docs/notes/protocole-x-entrainement-et-juges-v1/`, branche `protocole-x/entrainement-et-juges-v1` : la demande reformulée en quatre points (`demandes-reformulees-quatre-points-v1.md`), le dossier de faits et son erratum 1, `reponse-fable-demande-1-v1.md`, `reponse-carbon-demande-1-v1.md` (1,67 USD sous l'accord `GO-2026-11-24-16`), `comparaison-fable-carbon-demande-1-v1.md`, `devis-collisionneur-entrainement-et-juges-v3.md`, `ordre-et-calendrier-deux-propositions-entrainement-v1.md`, `figures_notes_v4.py` et `figures-v4/`.
