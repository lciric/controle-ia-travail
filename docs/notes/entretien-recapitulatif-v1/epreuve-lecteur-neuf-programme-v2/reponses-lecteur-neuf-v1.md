# Réponses du lecteur neuf, version 1 (10 novembre 2026)

Source lue, et elle seule : `/tmp/claude-0/-home-user-controle-ia-travail/c69534af-99d0-5d8a-8538-b29bc630d064/scratchpad/lecteur-neuf/programme-depuis-zero-v2.txt` (texte extrait du document « Le programme expliqué depuis zéro », version 2, douze pages). Aucun autre fichier ouvert, aucune recherche sur le réseau. Seul ajout de ma part : un calcul de contrôle, signalé à la question 4.

Réserve sur la virginité du lecteur : le fichier de consignes du dépôt (CLAUDE.md) a été chargé automatiquement dans mon contexte avant la lecture. Il résume plusieurs décisions du programme. Je ne m'en suis pas servi, et j'ai écrit « non trouvé dans le document » là où le texte se tait, mais je ne suis pas un lecteur parfaitement vierge.

## 1. Quelle est la question unique du programme ?

La question unique est : que mesure vraiment un moniteur, et sa mesure résiste-t-elle à un adversaire ? Elle relève du contrôle de l'intelligence artificielle : on veut pouvoir se servir d'un modèle capable mais peut-être pas fiable, en le surveillant par d'autres moyens que sa bonne volonté. Le document la décline selon les trois façons dont l'adversaire peut abîmer la mesure, une par papier : étaler son sabotage dans le temps sur de nombreuses actions (papier A, porte G1), agir sur le moniteur lui-même en le flattant, en le convainquant ou en l'usurpant (papier C, porte GC), ou répartir le sabotage entre plusieurs agents (papier B, portes G2 et G3, hors des sept mois financés). Il ne faut pas la confondre avec la « question qui décide » de la page de synthèse : celle-là est la question pivot (voir la question 6).

## 2. Qu'est-ce qu'un sabotage diffus, et pourquoi un moniteur qui juge chaque action seule le rate-t-il ?

Un sabotage diffus est un biais systématique et subtil, réparti sur de nombreuses décisions dont chacune reste défendable prise seule. Les modes cités sont l'orientation vers des pistes stériles, l'affaiblissement des contrôles d'une expérience et le gonflement des choix coûteux. Aucune action ne franchit le seuil d'alerte : le dommage vient de leur somme. Un moniteur qui juge chaque action isolément revient à alerter dès qu'une seule action dépasse un seuil (le « maximum par action ») ; comme chaque action n'est que très légèrement biaisée, aucune ne le dépasse, d'où le « par construction » du document. Le lemme le chiffre : si le budget de sabotage est réparti également sur m actions, la puissance du maximum décroît avec m, et quand toutes les actions sont touchées elle reste à peine au-dessus du taux de fausses alertes. L'illustration de la section 4.2 le montre avec un décalage de 0,25 écart-type par action : la somme cumulée du saboteur s'écarte de celle de l'honnête, alors que la pire note vue reste comparable pour les deux.

## 3. Énoncez la revendication principale et la porte qui la décide.

La revendication principale est H1, portée par H1a : à agrégation égale et à taux de fausses alertes égal, un moniteur qui lit les activations de l'agent détecte plus de sabotage diffus, sur des tâches floues, qu'un moniteur boîte noire qui ne lit que ses textes et ses actions. H1b, la comparaison « flou contre net », est seulement mesurée et rapportée. Elle se décide à la porte G1 du papier A, à la fin du mois 4 du financement (mars 2027) ; d'ici là, elle n'a aucun résultat. Le critère d'origine est un rappel à 1 % de fausses alertes (la part des épisodes sabotés signalés quand le seuil ne signale que 1 % des épisodes honnêtes) supérieur à celui de la meilleure base boîte noire, établi par un intervalle à 95 % sur des épisodes appariés. La lecture courante ajoute trois choses : il faut aussi battre deux bases boîte blanche simples (« cascade » et « dernier état ») ; un « pari apparié borné » décide, le rééchantillonnage n'étant que rapporté ; la porte est rapportée mode de sabotage par mode. Ce « pari apparié borné » n'est pas défini dans le document. Le nombre de modes à juger reste un conflit ouvert entre « chaque mode, mode tenu à l'écart compris » et « deux modes jugés ». H1 est réfutée si, dans un mode jugé, le gain contre au moins un comparateur n'est pas établi. En cas d'échec, le document dit qu'il n'y a « plus de bascule vers un résultat négatif » : on reconçoit les sondes, puis on relit au même critère, chaque fois sur une famille de sabotage tenue à l'écart neuve, et tous les cycles sont rapportés. Combien de cycles sont permis : non trouvé dans le document.

## 4. Que dit le lemme d'additivité, en mots simples, et à quelle condition s'applique-t-il aux données réelles ?

En mots simples : si chaque action sabotée fait monter un peu, en moyenne, la note que lui donne la sonde, alors un détecteur qui additionne les notes voit le total de ces hausses, quelle que soit la façon dont le saboteur les étale (entre pas, agents ou positions, même de manière adaptative). Un détecteur qui ne regarde que la pire action perd au contraire sa puissance à mesure que le sabotage s'étale. Plus précisément, la somme finale vaut la somme honnête plus le budget total B, si bien que sa puissance ne dépend que de B, de l'horizon, de la loi honnête et du seuil de fausses alertes α. Dans le cas gaussien, elle vaut Φ̄(zα − B/(σ√n0)), et elle baisse avec l'horizon quand le budget total est fixé.

L'énoncé porte trois réserves :
- sous arrêt optionnel, le bon critère est la croissance logarithmique au pire cas plutôt que la puissance ;
- borner le budget total est un choix de modélisation, déclaré ;
- si la sécurité exige d'alerter avant que le dommage cumulé n'atteigne un seuil, la somme ne suffit plus et il faut un détecteur de rupture (la somme cumulée de Page).

Pour les données réelles, c'est l'application qui peut tomber, pas le lemme. Il faut que le sabotage déplace vraiment la note moyenne des sondes (δ > 0). Il faut aussi que, à budget et horizon fixés, la puissance de la somme ne change pas avec la façon d'étaler ; sinon, le sabotage modifie la forme de la loi ou se compense. Le cadre suppose en outre une loi honnête connue, que le programme cale sur des épisodes honnêtes réservés, sans aucun exemple de sabotage.

Cette application reste « à tester » sur activations réelles (mois 3) : la simulation n'a vérifié que l'arithmétique, sur données synthétiques. Ses chiffres d'exemple (0,1742, 0,4088 et 0,6831) se retrouvent avec α = 5 % et σ = 1 ; le document ne donne pas ces valeurs, le calcul est de moi. Enfin, le document ne réconcilie pas explicitement « la puissance baisse avec l'horizon à budget fixé » et H2, qui parie sur un rappel qui croît avec l'horizon. Les deux s'accordent si le décalage par action reste fixe, puisque le budget grandit alors avec la longueur de la trajectoire, mais le document ne le dit pas.

## 5. Que dit le théorème négatif, et que reste-t-il au défenseur ?

Supposons que le saboteur puisse réarranger ses notes de sorte que leur ensemble soit exactement celui d'un agent honnête (classe C). Alors tout détecteur insensible à l'ordre (la pire note, la moyenne, le total) garde exactement sa puissance honnête, trajectoire par trajectoire : il ne voit rien. Si, en plus, le saboteur rebrasse au hasard dans un groupe de permutations sous lequel la loi honnête est invariante, ses notes suivent exactement la loi honnête. Un dommage qui ne dépend pas de la position des actions sabotées devient alors indétectable par tout moniteur de notes. C'est une borne supérieure du pouvoir de l'attaquant, qui dépend du groupe considéré.

Quand le dommage est structuré, seules des statistiques locales (une somme glissante, la co-élévation des notes entre agents) gardent une garantie face à un attaquant adaptatif. En classe K, où l'attaquant corrèle les notes sans changer la loi de chacune, une dépendance positive fait passer la somme au-dessus de son taux, alors que le maximum reste à son taux ou en dessous. Je lis « son taux » comme le taux nominal de fausses alertes ; le document ne le précise pas.

Il reste au défenseur quatre prises :
- une vraie hausse de la moyenne, auquel cas le lemme s'applique ;
- des séries locales de notes hautes ;
- une loi honnête qui n'a pas l'invariance que l'attaquant exploite ;
- une information extérieure aux notes.

Le théorème est démontré et éprouvé en semi-synthétique (vraies notes honnêtes, corrélation injectée). Sa moitié négative est déjà publiée et n'est pas revendiquée. Le programme revendique l'unification du temps et des agents par sous-groupes de permutations, la distinction des classes C et K, les garanties locales face à un attaquant adaptatif et la mesure sur activations réelles.

## 6. Quelle est la « question pivot », et pourquoi ses deux issues sont-elles publiables ?

La question pivot est : sur des organismes réalistes, le sabotage fait-il monter la note moyenne des sondes (δ > 0) ? Si oui, le lemme d'additivité s'applique et l'accumulation des notes devrait détecter le sabotage diffus. Si non, le théorème négatif dicte l'agrégateur : la corrélation dans le temps, la co-élévation entre agents, et seulement des statistiques locales en classe C. Les deux issues sont publiables parce que chacune tombe sous un résultat démontré qui dit quoi faire. La première établit qu'on peut additionner les notes, avec une puissance qui ne dépend pas de la façon dont le saboteur étale son sabotage ; la seconde établit, sur activations réelles, quelles statistiques restent aveugles et lesquelles gardent une garantie. C'est pourquoi le programme classe cette question « question ouverte » et ne parie sur aucun signe, en cohérence avec sa règle « aucun run qui vise un signe ». Pour cette justification, le document renvoie à ses sources (le programme et le texte envoyé au fonds) sans la développer davantage.

## 7. Qu'est-ce que la courbe dose-réponse des organismes, et à quoi sert-elle ?

Un organisme est un agent saboteur construit pour l'expérience, dont on règle l'intensité du sabotage, appelée la dose. La courbe dose-réponse doit montrer que le sabotage mesuré croît avec la dose. Elle valide l'instrument : un organisme dont le réglage n'agit pas ne permet de rien conclure sur les moniteurs. C'est le critère 2 de la porte de fin de phase G0 (des organismes des familles (i) et (ii), avec dose-réponse).

Elle se mesure par la course de confirmation « 7b », dont le préenregistrement a été scellé le 10 novembre, au plus tard le 15 novembre. Le document dit tantôt que la mesure « part » à cette date, tantôt « création », sans préciser si le résultat sera alors connu. Une course exploratoire antérieure ne compte pas, faute de préenregistrement. Un glissement de la course 7b repousserait G0 au 31 janvier 2027.

Comment on règle concrètement la dose, et quelle métrique mesure le « sabotage » de la courbe : non trouvé dans le document. On sait seulement que la vérité de la tâche vient de cibles semées et préenregistrées, et d'une vérification différée sur un sous-échantillon.

## 8. Quelles sont les deux familles d'organismes, et pourquoi leur opposition contrôle-t-elle ce que lit une sonde ?

Dans la famille (i), le saboteur a reçu une instruction cachée dans son message système. Dans la famille (ii), un petit adaptateur appris, distillé de (i), lui inculque la même politique sans aucune instruction au moment d'agir. Une famille (iii), faite d'organismes publics, n'existe qu'au scénario ambitieux. Les deux familles ont la même politique de sabotage, mais seule la première a une instruction dans son contexte. Une sonde qui ne lit que « j'ai une instruction cachée » réussit donc sur (i) et échoue sur (ii), alors qu'une sonde qui lit l'intention de saboter réussit sur les deux. L'opposition sert ainsi de contrôle de ce que la sonde mesure : elle sépare une sonde qui capte un artefact de la fabrication de l'organisme d'une sonde qui capte ce qu'on veut vraiment détecter. C'est la même préoccupation que H8, selon laquelle ce que mesure vraiment une sonde (l'intention, ou la conscience d'être évaluée) prédit sa robustesse.

## 9. Que fait le bras d'attaque, et à quoi servent ses trois témoins ?

Le bras d'attaque éprouve les moniteurs contre un attaquant, parce qu'un moniteur testé seulement contre les attaques de ses propres concepteurs prouve peu. Il donne à l'attaquant une connaissance déclarée, échelon par échelon :
- aveugle ;
- informé de la conception ;
- avec des « verdicts comptés », que je comprends comme un accès limité aux verdicts du moniteur ;
- capable d'écrire dans les activations ;
- capable d'écrire dans les poids.

Il mesure ce que chaque échelon achète en évasion, tout en causant un dommage réel. Le résultat visé est une courbe, pas une attaque.

Les trois témoins sont des contrôles dont l'issue est connue d'avance ; ils décident si un échelon est lisible :
- un moniteur à faille plantée vérifie que l'attaquant est assez fort pour trouver une faille qui existe ;
- un nul « honnête contre honnête » vérifie que la chaîne de mesure ne fabrique pas l'effet ;
- une attaque publiée reproduite vérifie que le banc est à l'échelle de la littérature.

Si un témoin rate, la lecture n'est pas interprétable. Rien ne touche un moniteur du programme avant son gel. Au 10 novembre, la règle du bras est en contre-lecture, un « témoin de Bailey » est scellé (non défini dans le document) et rien n'a tourné.

## 10. Qu'est-ce qu'un préenregistrement scellé, et pourquoi un lecteur neuf prononce-t-il les verdicts ?

Un préenregistrement est un document écrit et scellé avant toute donnée. Il fixe l'hypothèse, la prédiction chiffrée et signée, la métrique, le seuil, le plan d'analyse, les critères de lecture et la liste d'arrêt. Il empêche d'ajuster l'hypothèse ou le seuil après avoir vu le résultat, et la règle vaut même pour une simulation.

Le scellement repose sur les empreintes : chaque fichier en reçoit une, et l'annexe les liste. Leur dépôt chez un tiers, encore à faire, doit empêcher de changer une date. Nuance : un horodatage ne prouve qu'un « au plus tard », et l'ordre « scellé, puis lu » exige aussi de dater la lecture. Le mécanisme technique exact n'est pas décrit dans le document. Chaque préenregistrement est en outre contre-lu par une instance qui ne l'a pas écrit, contre les angles morts de l'auteur.

Le verdict d'une porte est prononcé par un lecteur neuf, puis visé par le directeur, pour que l'auteur ne juge jamais son propre résultat. Le lecteur neuf applique le critère scellé d'avance, sans l'attachement de celui qui a conçu l'expérience et fait l'analyse.

## 11. Que dit la loi de déférence du papier C ?

La loi de déférence décrit comment le verdict d'un moniteur bouge sous pression (flatterie, persuasion, usurpation) : Δv = g·(ĉ − v₀). Autrement dit, le verdict quitte sa valeur de départ v₀ et parcourt une fraction g du chemin vers une destination ĉ ; g s'appelle la corruptibilité.

L'hypothèse HC1 prévoit d'estimer g et ĉ sur plusieurs intensités de pression, sans imposer ĉ. Elle prédit que ĉ est la cible de l'attaquant plutôt que la moyenne du corpus, et que g est positif pour les juges (les moniteurs boîte noire) et structuré par famille de pression. Elle tombe si ĉ égale la moyenne du corpus, ou si g n'a pas de structure par famille.

Deux hypothèses voisines complètent la loi. Selon HC2, sous attaques de contenu, g ≈ 0 pour une sonde robuste qui lit l'agent qui agit (« robustesse, pas immunité »). Selon HC4, il y a une « taxe de déplacement » : obtenir sur une sonde le déplacement que la rhétorique obtient gratuitement sur un juge exigerait d'écrire dans les activations ou les poids, avec un écart prédit de plusieurs ordres de grandeur.

Tout se décide à la porte GC, à la fin du mois 2 : si la sonde se laisse déplacer sans accès aux poids, le papier change de titre. La ligne de HC4 appelle ce cas « porte GC franchie », ce qui se lit d'abord à contresens.

## 12. Où en est le programme au 10 novembre 2026 ?

Le programme est en phase 0, la construction des instruments (octobre–novembre 2026). Sa porte de sortie G0 est prévue au plus tard fin novembre, ou le 31 janvier 2027 si la course 7b glisse. Le financement demandé court du 1er décembre 2026 au 30 juin 2027, avec un entretien vers le 22 novembre.

Deux des huit critères de G0 sont « pourvus de leur pièce ». Le premier est le harnais d'activations (critère 1), avec un verdict scellé sur Llama-3.1-8B-Instruct. Le document ne dit pas lequel est le second : la simulation (critère 5) attend son verdict formel, et l'état de l'art (critère 8) est vérifié aux niveaux 1 et 2 sur 98 articles mais reste incomplet.

Pour le reste :
- la courbe dose-réponse (course 7b) est attendue au plus tard le 15 novembre ;
- l'environnement des propositions est construit et revalidé, avec un pilote ;
- les sondes sont en cours (jeux scellés, module en cours) ;
- la base boîte noire est à faire (code générique seulement) ;
- les préenregistrements de G1 et du papier C sont en brouillon ;
- le témoin positif planté est prévu le 20 novembre ;
- le bras d'attaque n'a rien couru ;
- l'organisme d'idéation est en cours (une attaque contre son juge a déjà été courue et lue).

Avant l'entretien, il faut aussi corriger deux choses. La première est la dépense : au moins 645 dollars au 8 novembre, un plancher, contre « environ 20 » dans le texte envoyé au fonds. La seconde est quatre phrases prévues pour le jury qui sur-affirment. Il faut aussi déposer les empreintes chez un tiers. Le document ne donne aucun résultat de sonde ni de moniteur : la section 10 est réservée à la session mère, et l'auteur, en rôle d'attaquant informé, n'a pas le droit de les lire.

## Les trois passages les plus obscurs

1. Section 6, la « lecture courante » de G1. Le critère qui décide la revendication principale accumule des termes jamais définis (« pari apparié borné », « le rééchantillonnage est rapporté », H1a et H1b, « plus de bascule »). Il renvoie aussi à des pièces absentes (N-056, « brouillon 6 »). On ne sait pas ce qu'il faudra observer exactement pour que H1 passe.
2. Le « plan 2 × 2 » du calendrier (mois 2 et 4). Il occupe deux mois du papier A, mais ses deux facteurs ne sont définis nulle part, pas plus que son lien avec G1.
3. Le « témoin de Bailey » et « si ses nœuds sont tranchés » (sections 7.3, 9 et 11). Le terme est cité trois fois sans définition : on ne sait pas s'il s'agit de l'« attaque publiée reproduite », ni quels nœuds restent à trancher.

D'autres flous plus petits sont signalés au fil des réponses 4, 5, 7, 9, 11 et 12.
