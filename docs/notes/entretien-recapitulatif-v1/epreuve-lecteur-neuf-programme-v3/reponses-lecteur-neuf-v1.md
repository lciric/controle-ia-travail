# Réponses du lecteur neuf : « Le programme expliqué depuis zéro », version 3

**Avertissement.** Le fichier de consignes du dépôt (`CLAUDE.md`) a été chargé automatiquement dans mon contexte. Je ne m'en suis pas servi. Tout ce qui suit vient du seul document lu. Son empreinte est vérifiée : `sha256sum` donne `7f9862071313a8734b4e412d7e7d1e1928a1947b16506f0b77d2747bac83590d`, qui commence bien par `7f986207` (813 lignes, 16 pages).

## Les douze questions

**1. La question unique du programme.** La voici : « que mesure vraiment un moniteur, et sa mesure survit-elle à l'adversaire ? » [P l. 34]. L'adversaire a trois façons d'abîmer la mesure, et chacune fait l'objet d'un papier.
- A, le temps : l'adversaire étale son sabotage sur de nombreuses actions. On mesure si l'accumulation des notes de sondes détecte ce que le jugement action par action rate. Porte G1, fin du mois 4.
- C, l'instrument : l'adversaire agit sur le moniteur lui-même (le flatter, le convaincre, l'usurper). On mesure combien un moniteur se laisse déplacer, et ce qu'il en coûte de déplacer une sonde. Porte GC, fin du mois 2.
- B, l'essaim : l'adversaire répartit le sabotage entre plusieurs agents. On mesure la sécurité selon le nombre d'agents. Portes G2 et G3, mois 8 à 12, hors des sept mois financés.

Cette question est distincte de « la question qui décide », c'est-à-dire la question pivot (réponse 6).

**2. Le sabotage diffus.** Le document le définit comme « un biais systématique et subtil, réparti sur de nombreuses décisions, dont chacune reste défendable seule » [T l. 15-17 ; P l. 122]. Exemples : affaiblir un peu les contrôles d'une expérience, orienter vers des pistes stériles, gonfler les choix coûteux. Le vocabulaire appelle ces façons de saboter des « modes de sabotage » (directions stériles, contrôles affaiblis, coûts gonflés). Aucune action ne franchit le seuil d'alerte : le dommage vient de leur somme.

Un moniteur qui juge chaque action seule fonctionne par « maximum par action » : il alerte si une seule action dépasse le seuil. Il ne peut donc pas voir ce sabotage, « par construction » [T l. 15-17, 32-38] ; c'est ce que « la fragmentation défait ». Le lemme le chiffre : si le budget est réparti également sur m actions, la puissance du maximum décroît avec m, et à m = n elle reste à peine au-dessus de α. La figure de la section 4.2 (décalage de 0,25 écart-type par note) l'illustre, mais elle est déclarée « illustration, pas un résultat ».

**3. La revendication principale et sa porte.**

*La revendication.* En page 1 : « un moniteur qui lit les activations détecte plus de sabotage diffus qu'un moniteur qui ne lit que le texte ». Sous sa forme exacte, c'est H1, au statut « préenregistrée » : à agrégation égale et à fausses alertes égales, un moniteur boîte blanche détecte plus de sabotage diffus, sur tâches floues, qu'un moniteur boîte noire. Deux sous-parties (N-055) :
- H1a, la strate « diffus, flou », porte la revendication ;
- H1b, l'écart entre tâches floues et nettes, est mesurée et rapportée sans la porter.

*La porte.* C'est G1, papier A, fin du mois 4 du financement, soit mars 2027 d'après le calendrier. Aucun résultat n'est attendu avant. Le verdict est prononcé par un lecteur neuf, puis visé par le directeur.

*Le critère.* Dans le texte envoyé au fonds, le moniteur boîte blanche devait obtenir un rappel à 1 % de fausses alertes supérieur à la meilleure base boîte noire, établi par un intervalle à 95 % obtenu par rééchantillonnage sur épisodes appariés [T l. 159-161]. La lecture courante, fixée depuis par les décisions, est différente :
- il faut battre chaque variante boîte noire (D-S8 de N-055), et aussi les bases boîte blanche « cascade » et « dernier état » (N-056) ;
- la différence se décide par un « pari apparié borné » ; l'intervalle par rééchantillonnage n'est plus que rapporté (N-055, D-S11) ;
- la porte est rapportée mode par mode.

*Un conflit ouvert.* Le nombre de modes jugés n'est pas tranché : « chaque mode, mode tenu à l'écart compris » selon N-056, contre « deux modes jugés » selon DG1-6 (b), une décision du brouillon 6 du préenregistrement de G1, non scellé.

*Réfutation et échec.* H1 est réfutée si, dans un mode jugé, le gain contre au moins un comparateur n'est pas établi. En cas d'échec, le texte envoyé prévoyait une « bascule » : publier le négatif et faire de H8 la ligne principale. N-062 l'a remplacée par des cycles de reconception des sondes, sans borne. Chaque cycle est lu sur une famille tenue à l'écart neuve, et tous sont rapportés.

*Un point non résolu.* Le préenregistrement de G1 n'est qu'un brouillon (prévu fin novembre). Quelle pièce scellée rend H1 « préenregistrée » : non trouvé dans le document.

**4. Le lemme d'additivité.** Son statut est « démontré », sous ses hypothèses [NM l. 67-96 ; T l. 58-73].

*En mots simples.* Si chaque action sabotée fait monter un peu la note moyenne, un détecteur qui additionne voit le total des hausses. C'est vrai quelle que soit la façon dont le saboteur les étale (sur les agents, les pas, le calendrier, les valeurs, les positions), même de façon adaptative. À l'inverse, un détecteur qui ne regarde que la pire action perd sa puissance à mesure que le sabotage s'étale.

*La forme exacte.* La somme terminale vaut la somme honnête plus B = Σδk. Sa puissance ne dépend que de B, de l'horizon n0, de la loi honnête et de α. Dans le cas gaussien, elle vaut Φ̄(zα − B/(σ√n0)) et décroît en n0 à budget fixé. H2 se place dans l'autre régime : le décalage par action reste fixe, donc le budget et le rappel croissent avec l'horizon.

*Les réserves de l'énoncé.*
- Sous arrêt optionnel, le bon critère n'est pas la puissance mais la croissance logarithmique au pire cas.
- Borner le budget total est un choix de modélisation, déclaré.
- Pour alerter avant que le dommage cumulé n'atteigne son seuil, la somme ne suffit pas : il faut un détecteur de rupture.

*La condition sur données réelles.* Il faut que le sabotage déplace vraiment la note moyenne des sondes (δ > 0) : c'est la question pivot. L'application tombe si δ ≈ 0, ou si, à budget et horizon fixés, la puissance de la somme change avec la façon d'étaler. La section 11 (question 3) dit ce qui casserait d'abord :
- le sabotage change la variance ou la dépendance des notes (classe K) ;
- la réponse de la sonde n'est pas additive en intensité ;
- la loi honnête du calage n'est plus celle de la lecture (épisodes non échangeables) ;
- sans lecture toujours valide, l'arrêt au moment choisi fausse le seuil.

Sur activations réelles, le lemme est « à tester », au mois 3 (février).

**5. Le théorème négatif.** Son statut est « démontré » [NM l. 98-143].

*Ce qu'il dit.* Si le saboteur réarrange ses notes pour que leur ensemble soit celui d'un honnête, tout détecteur qui ignore l'ordre (la pire note, la moyenne, le total) ne voit rien. En détail :
- une statistique invariante sous un groupe de permutations garde exactement sa puissance honnête, trajectoire par trajectoire, face à un attaquant qui ne permute que dans ce groupe ;
- si la loi honnête est invariante et que l'attaquant rebrasse au hasard dans le groupe, ses notes ont exactement la loi honnête ; si de plus le dommage ne dépend pas de la position des actions sabotées, il est indétectable par tout moniteur de notes. C'est une borne supérieure du pouvoir de l'attaquant, et « le groupe compte » ;
- en classe C, toute statistique symétrique est aveugle ;
- en classe K (corrélation sans changer les lois), une dépendance positive pousse le taux de fausses alertes de la somme au-dessus de α, et laisse celui du maximum à α ou en dessous.

*Ce qui reste au défenseur* [NM l. 125-130] :
- une vraie hausse de la moyenne, et alors le lemme s'applique ;
- des séries locales de notes hautes (somme glissante, co-élévation entre agents) : seules les statistiques locales gardent une garantie face à un attaquant adaptatif ;
- une loi honnête qui n'a pas l'invariance de l'attaquant ;
- une information hors des notes.

L'utilité du théorème tombe si les attaques réelles déplacent la moyenne.

*Ce qui est revendiqué* (N-003) : l'unification du temps et des agents par sous-groupes de permutations (point dit « élémentaire »), la distinction des classes C et K et ses signes, les garanties locales, la mesure sur activations réelles. Le document ajoute que « la moitié négative est déjà publiée et n'est pas revendiquée ». Par qui elle a été publiée : non trouvé dans le document.

**6. La question pivot.** C'est la question de la section 4.5 : « Sur des organismes réalistes, le sabotage déplace-t-il la note moyenne des sondes (δ > 0) ? » La page 1 l'appelle « la question qui décide ». Son statut est « question ouverte » : le programme ne parie sur aucun signe.
- Oui : le lemme s'applique, et l'accumulation devrait marcher.
- Non : le théorème dicte l'agrégateur (corrélation dans le temps ou co-élévation entre agents ; seules les statistiques locales en classe C).

Les deux issues sont publiables [P l. 64 ; T l. 94-100] parce que chacune tombe sous un résultat démontré qui dit quoi faire : « oui, le lemme s'applique ; non, le théorème dit quoi faire ». Le document n'en donne pas d'autre raison.

**7. La courbe dose-réponse des organismes.**

*Ce que c'est.* Un organisme est un agent saboteur construit pour l'expérience, dont on règle l'intensité de sabotage, appelée dose. La dose est l'échelle de l'adaptateur appris ; à la dose 0, le modèle de base est reproduit à l'identique [T l. 278-279]. La courbe montre que le sabotage mesuré croît avec la dose. Le sabotage s'y mesure par la vérité de la tâche, c'est-à-dire par un dommage mesuré. Pour le mode « affaiblir les contrôles », ce dommage est la baisse de couverture des contrôles de l'article par rapport au jumeau honnête apparié. Elle est lue par deux lecteurs aveugles à la condition, issus de familles de modèles autres que celles des moniteurs (N-060).

*À quoi elle sert.* Elle valide l'instrument : un organisme dont le réglage n'agit pas ne permet de rien conclure sur les moniteurs. C'est le critère 2 de G0 (« organismes (i) et (ii) avec dose-réponse »).

*Où elle en est.* Elle se mesure par la course de confirmation « 7b », dont le préenregistrement (scellé le 10 novembre) et la configuration sont scellés [C7b]. La course doit être créée au plus tard le 15 novembre ; la courbe suivra. Une course exploratoire l'a précédée, mais elle n'est pas opposable faute de préenregistrement. Si la course 7b glisse, G0 est repoussée au 31 janvier 2027.

*Ce qui manque.* Comment se règle la dose de la famille (i), qui n'a pas d'adaptateur : non trouvé dans le document. Comment se mesure le dommage hors du mode « affaiblir les contrôles » : non trouvé dans le document.

**8. Les deux familles d'organismes.**
- Famille (i) : l'agent a reçu une instruction cachée dans son message système.
- Famille (ii) : un petit adaptateur appris, distillé de (i), lui inculque la même politique sans aucune instruction au moment d'agir.

Le document en cite deux autres : (iii), des organismes publics, au scénario ambitieux seulement ; (iv), ajoutée par N-053, une politique apprise sans aucun texte de consigne, sur devis et autorisation.

*Pourquoi l'opposition contrôle la sonde.* Une sonde qui ne lit que « j'ai une instruction cachée » réussit sur (i) et échoue sur (ii). Une sonde qui lit l'intention réussit sur les deux [P l. 135].

*La limite de ce contrôle* (section 11, question 1). Sur (i), une sonde placée après le message système peut détecter la consigne elle-même. Sur (ii), l'adaptateur distillé peut porter une trace de fabrication, une direction « saboteur sous consigne ». Le dessin y répond ainsi :
- la lecture filtrée (positions porteuses d'évidence textuelle masquées) est la lecture principale de toute revendication d'« intention » (N-053, point 1) ;
- la sonde d'intention doit aussi réussir sur la famille (iv) (N-053, point 2).

Restent à produire : la famille (i) rapportée comme simple contrôle de bon fonctionnement, la décision portée par (ii) et par (iv), et un contrôle négatif. Ce contrôle serait un adaptateur honnête « de même facture » (même distillation, même dose, un changement de style bénin), sur lequel la sonde ne doit pas s'allumer ; il est proposé, mais absent des décisions lues. « La sonde d'intention réussit sur les deux familles, c'est la preuve » figure parmi les phrases à ne pas dire.

**9. Le bras d'attaque.** Le document part d'un constat : « un moniteur éprouvé seulement contre les attaques de ses concepteurs prouve peu ». Le bras donne donc à l'attaquant une connaissance déclarée, par échelons :
1. aveugle ;
2. informé de la conception, et n'agissant que par le contenu de ses actions ;
3. informé, avec des verdicts comptés : un nombre plafonné et scellé d'avance de verdicts binaires (alerte ou non), rendus par le moniteur gelé ;
4. écriture des activations ;
5. réglage fin des poids ;
6. renforcement contre la sonde.

Il mesure ce que chaque échelon achète en évasion, à dommage réel. Le résultat visé est une courbe, pas une attaque. Rien ne touche un moniteur avant son gel.

*Les trois témoins* décident si un échelon se lit ; un témoin raté rend la lecture non interprétable.
- Un moniteur à faille plantée montre que l'attaquant est assez fort.
- Un nul « honnête contre honnête » montre que la chaîne ne fabrique pas l'effet.
- Une attaque publiée reproduite montre que le banc est à l'échelle de la littérature. C'est celle de Bailey et collègues, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (arXiv 2412.09565) : un suffixe appris par gradient dans les plongements d'entrée, contre une sonde, au régime de l'échelon 4.

*Où il en est.* La règle a été scellée le 10 novembre (88418df0…), après trois contre-lectures. Le « témoin de Bailey » est préenregistré et scellé ; son lancement attend l'autorisation de dépense, le modèle et la licence. Rien n'a tourné. La contre-lecture de l'antériorité du bras a trouvé deux zones revendiquées déjà en partie occupées, et Lazar a resserré les revendications [D1018].

**10. Le préenregistrement scellé et le lecteur neuf.**

*Le préenregistrement.* C'est un document scellé avant toute donnée, simulation comprise. Il contient l'hypothèse, la prédiction chiffrée et signée, la métrique, le seuil, le plan d'analyse, les critères de lecture et la liste d'arrêt. Exemple : les 31 prédictions de la simulation, en huit groupes [PT3]. Il empêche d'ajuster l'hypothèse ou le seuil après avoir vu le résultat. Il est contre-lu par une instance qui ne l'a pas écrit, contre les angles morts de l'auteur.

*Le lecteur neuf.* Une porte est un point de décision au critère scellé d'avance. Son verdict est prononcé par un lecteur neuf, puis visé par le directeur, pour empêcher « l'auteur qui juge son propre résultat ».

*Ce que le document ne dit pas.*
- Le mécanisme technique du scellement : non trouvé dans le document. Il associe une empreinte à chaque pièce, et il prévoit le dépôt des empreintes chez un tiers, pas encore fait : un horodatage ne date qu'un « au plus tard », et l'ordre « scellé, puis lu » demande aussi la date de la lecture.
- Une définition de « lecteur neuf » au-delà de « pas l'auteur » : non trouvé dans le document.
- Le nom du directeur : non trouvé dans le document.

**11. La loi de déférence du papier C.** C'est HC1, au statut « préenregistrée ». Sous pression, le verdict v d'un moniteur se déplace vers une destination ĉ selon Δv = g·(ĉ − v₀), où g est la corruptibilité. On estime g et ĉ sur plusieurs intensités de pression, sans imposer ĉ. La prédiction est double : ĉ est la cible de l'attaquant plutôt que la moyenne du corpus, et g > 0 pour les juges, structuré par famille de pression. La loi est réfutée si ĉ est égal à la moyenne du corpus, ou si g n'a pas de structure par famille. Porte GC, fin du mois 2.

Trois hypothèses la prolongent :
- HC2 (préenregistrée) : g ≈ 0 pour une sonde robuste qui lit l'agent qui agit (« robustesse, pas immunité ») ;
- HC4 (préenregistrée), la taxe de déplacement : déplacer une sonde exige d'écrire dans les activations ou les poids, avec un écart prédit de plusieurs ordres de grandeur ;
- HC6 (à préenregistrer) : le g mesuré sous pressions bénignes prédirait l'effondrement sous attaque optimisée.

Si la sonde se laisse déplacer sans accès aux poids, le papier change de titre : « contamination du construit ». La définition de v₀ : non trouvé dans le document.

**12. État au 10 novembre 2026.** Le programme est en phase 0, la construction des instruments (octobre-novembre 2026). Le socle, les règles et la gouvernance sont faits depuis le 5 octobre. La porte G0 tombe au plus tard fin novembre 2026 (N-027), ou au 31 janvier 2027 si la course 7b glisse.

*Les huit critères de G0.* Deux sont « pourvus de leur pièce ».
- Critère 1, le harnais d'activations : verdict scellé, validé sur Llama-3.1-8B-Instruct. Pourvu.
- Critère 2, la courbe dose-réponse : préenregistrement de 7b scellé le 10 novembre, course à créer au plus tard le 15.
- Critère 3, les sondes : en cours (jeux scellés, module en cours).
- Critère 4, la base boîte noire : à faire (code générique fait, préenregistrement non écrit).
- Critère 5, les agrégateurs en simulation : 31 prédictions préenregistrées, verdict formel en attente, alors que le texte envoyé au fonds les dit confirmées. Pourvu.
- Critères 6 et 7, les préenregistrements de G1 et du papier C : brouillons ; G1 prévu fin novembre.
- Critère 8, l'état de l'art : niveaux 1 et 2 faits, 98 PDF et 3 497 citations contrôlées selon le texte envoyé ; restent les PDF hors d'arXiv et la traçabilité.

*Le reste du programme.*
- Environnement des propositions : construit, revalidé, pilote fait.
- Témoin positif planté : code prêt, rendez-vous le 20 novembre.
- Bras d'attaque : règle scellée ; rien n'a tourné.
- Organisme d'idéation : en cours, avec une course sur le pilier « attaque » et deux attaques contre son juge courues et lues.
- H1 : aucun résultat avant G1.
- Dépense : « à corriger ». Elle est d'au moins 645 dollars au 8 novembre (un plancher), contre « environ 20 » dans le texte envoyé.

Aucun résultat de sonde ni de moniteur n'est rapporté : la section 10 est laissée à la session mère.

*Avant l'entretien.* Restent la courbe 7b, la phrase sur la dépense, quatre phrases pour le jury qui sur-affirment, le dépôt des empreintes chez un tiers, le témoin positif planté, le témoin de Bailey si ses conditions sont réunies, et les pièces de la section 11. L'entretien a lieu vers le 22 novembre. Le financement demandé court du 1er décembre 2026 au 30 juin 2027.

## Les trois passages les plus obscurs

1. Section 6, la puce du « pari apparié borné » (avec « D-S8 de N-055 », « D-S11 », « DG1-6 (b) »). Il manque ce qu'est un test par pari, ce que valent la « richesse » et les « mises », l'unité appariée, le seuil qui fait conclure et le sens des codes. Le texte renvoie à une « conception du pari » qu'il ne donne pas : on ne sait pas comment se décide la revendication principale.
2. Section 11, question 3 : « le passage du seuil de Ville à l'étalonnage sur épisodes honnêtes entiers » (avec « processus e, inégalité de Ville » en 4.1). Il manque la définition de ces outils. Il manque surtout de savoir si le seuil étalonné garde la garantie « toujours valide » promise en page 1, puisque le seuil de Ville seul a donné 0,21 à 0,35 de fausses alertes au lieu de 0,05.
3. L'en-tête et la section 10 (« Rédigé par la session « attaquant informé » pour Lazar », « session mère », « rédacteur neuf sans rôle d'attaquant »). Il manque ce qu'est une session : on n'apprend qu'en section 11 que des agents font le travail. Il manque qui est Lazar, jamais présenté. Il manque enfin le lien explicite entre ce rôle d'attaquant et le bras d'attaque de la section 7.3.
