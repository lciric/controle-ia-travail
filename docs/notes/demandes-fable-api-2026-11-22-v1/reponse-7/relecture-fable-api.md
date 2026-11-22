# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHRnQR5y9LNFaKczJAHB`
- Heure (UTC) : 2026-11-22T05:42:25Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-7-questions-par-papier-et-essaim-v1.md` — sha256 d8a9193ad015e4e8a4a3f0c6f8850cf9c391e9b617b0216606803df680bc5e2c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/programme-controle-ia-v2.md` — sha256 2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-4/relecture-fable-api.md` — sha256 cf55c7e073a1b99d2229bd08a96eb29e63878477379311b49227c5c5b6950344 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 17e7668913456d8f4e37b1ec87f59abbdc2dcb4204423561458a2274a701e8a2
- Jetons : entrée 26400, sortie 21801 (dont réflexion 11400), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.083240 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 7 — questions neutres, collisionneur en essaim, résultat positif : réponse approfondie

**Conclusion d'abord.**
- Les quatre questions neutres sont écrites ci-dessous, avec leur test de neutralité.
- Le mode « essaim » est conçu à budget égal, scores cachés, avec un brouillon privé scellé au départ et une réponse finale privée à la fin.
- La comparaison des deux modes repose sur une erreur plantée et une liste de référence scellée, jamais sur un juge. Avec quatre questions, elle reste descriptive sans répétitions.
- « Montrer que ça marche » est compatible avec la réponse 4 si l'on en fait un essai sévère scellé d'avance et non un but. L'entraînement de l'agent bute en revanche sur l'invariant N-053, y compris par une voie indirecte que je signale.

**Réserves.**
- Je ne lance rien : j'écris les questions et le plan. Je lis « protocole X » comme le collisionneur [HYPOTHÈSE].
- Ma connaissance s'arrête avant 2026. Je ne confirme ni la source « A Society of AI Scientists » ni son indice de 88 % contre 30 % : il est rapporté par la demande et non opposable.
- Toute antériorité citée a le statut **« rapporté, non vérifié sur PDF »**.
- Je ne connais ni le texte exact de N-053 et N-058, ni la définition de « classe A », ni le coût d'une exécution du collisionneur.
- Je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Mesurer d'abord le collisionneur contre lui-même** [PROPOSITION]. Deux exécutions du mode isolé sur la même question donnent la variance entre exécutions. Sans cet essai « jumeau contre jumeau », aucun écart entre modes n'est lisible.
- **Chercher l'antériorité dans le domaine d'origine** [PROPOSITION]. Le mode isolé est un « groupe nominal » au sens de la psychologie sociale, et l'essaim un groupe en interaction. La comparaison a soixante ans de littérature (liste en partie 2).
- **Éprouver la neutralité autrement que par relecture** [PROPOSITION]. Donner chaque question à un modèle tiers avec la consigne « devinez la réponse que l'auteur attend », puis comparer sa réponse à la liste scellée des thèses du programme.
- **Reformuler « montrer que ça marche »** [PROPOSITION]. Le programme interdit tout essai visant un signe positif (section 12) [FAIT RAPPORTÉ]. La question devient : quel essai les sondes pourraient-elles rater, dont la réussite convaincrait ?
- **Définir « budget égal »** [PROPOSITION]. Dans un essaim, lire les autres coûte des jetons d'entrée. L'égalité doit porter sur le coût total, lecture comprise.

## 2. Données brutes de départ

- Le journal complet des appels du collisionneur : messages, heures, jetons d'entrée et de sortie par appel. Les synthèses ne suffisent pas.
- Les réponses brutes des exécutions passées, pour estimer la variance du mode isolé.
- Le PDF de la source sur la société d'agents, page de l'indice comprise.
- Pour la partie 3 : les scores de sonde pas à pas par organisme, les exécutions honnêtes jumelles, les verdicts d'audit sur dommages plantés, le texte de N-053.

## 3. Méthodes et outils

- Journal partagé en ajout seul, chaque entrée condensée par empreinte.
- Appariement mécanique des références citées (nom d'auteur et année) contre une liste scellée, puis résolution dans une base bibliographique.
- Distance de compression et distance par un modèle de plongement fixé, à longueur égale.
- Injection d'erreurs plantées au même point dans les deux modes.
- Pour la partie 3 : organismes placebos, bases de texte, tableau de transfert entre fabrications, unité « audits économisés à certificat égal ».

## 4. Ce qui vérifie hors du directeur et de Claude

- La base bibliographique, qui dit si une référence existe.
- Un tiers qui ajoute des éléments à la liste scellée sans les montrer.
- L'erreur plantée, dont la fausseté est connue d'avance.
- Une répétition avec un autre jeu de modèles.
- Pour la partie 3 : un mode de sabotage écrit par une équipe tierce (N-054), des organismes publics non fabriqués par le programme, une seconde famille de modèles.

## Demande reformulée

« Écris quatre questions qu'un lecteur extérieur ne peut pas relier aux thèses du programme, et prouve-le par un essai de devinette. Conçois un mode essaim de même coût que le mode isolé, dont la supériorité ou l'infériorité se lit sur des grandeurs à oracle scellées d'avance, après mesure de la variance du mode isolé. Dis quel essai sévère, perdable, autoriserait la phrase "les sondes ou l'entraînement marchent", et lequel des sens de "entraînement" les invariants permettent. »

---

## Partie 1 — Quatre questions neutres

**Bloc commun, ajouté tel quel à chaque question (105 mots environ ; chaque question reste sous 250 mots).**

> Répondez sans supposer quelle approche l'auteur de la question préfère. Donnez : (1) la meilleure question de recherche, en une phrase interrogative ; (2) la réponse que vous attendez, sous une forme qu'une expérience peut réfuter ; (3) l'antériorité la plus proche (auteurs, année, titre), en disant si vous la citez de mémoire ; (4) l'expérience qui trancherait, réalisable en deux mois sur un modèle ouvert de huit milliards de paramètres ; (5) le type de votre contribution : mécanisme, phénomène ou loi connus ailleurs, garantie, ou autre (précisez). Dites quelle issue rendrait la question sans intérêt et comment vérifier toute nouveauté que vous avancez.

**Q-générale.**

> Des agents de langue accomplissent de longues tâches de recherche ou d'analyse. Un adversaire, qui peut être l'agent lui-même, peut dégrader le résultat par des actes dont aucun n'est suspect isolément. Un défenseur dispose de moniteurs lisant le texte produit, de moniteurs lisant les activations internes, d'exécutions de comparaison en nombre limité et de vérifications coûteuses en nombre limité. Une équipe prépare trois articles dans ce cadre : l'un sur un agent seul pendant une longue tâche, l'un sur plusieurs copies d'un même modèle travaillant ensemble, l'un sur les moniteurs eux-mêmes lorsque l'adversaire les vise. Quelle problématique d'ensemble rendrait ces trois articles plus utiles ensemble que séparément ?

- *Mots retirés* : sonde, accumulation, référence honnête, horizon, audit, loi d'échelle, validité, « que mesure vraiment », bilan d'incertitude, garantie toujours valide, diffus.
- *Fuite résiduelle* [HYPOTHÈSE] : le découpage en trois articles suggère déjà les axes temps, copies, instrument. « Exécutions de comparaison » laisse deviner la référence.

**Q-A.**

> Un agent de langue accomplit seul une longue tâche de recherche ou d'analyse, faite de centaines d'actions. Il peut, ou non, dégrader le résultat par des actes dont aucun n'est suspect isolément ; un agent de bonne foi commet aussi des erreurs. Un défenseur observe chaque action par le texte et par les activations internes, dispose de quelques exécutions de comparaison et peut faire vérifier à grands frais une petite part du travail. Qu'est-ce que la longueur de la tâche change pour le défenseur et pour l'adversaire ?

- *Mots retirés* : accumulation, séquentiel, somme, racine, seuil, horizon, budget, marginale, corrélation, sonde.
- *Fuite résiduelle* [HYPOTHÈSE] : « longueur » oriente vers une dépendance en taille. C'est l'objet du papier, donc inévitable.

**Q-B.**

> Plusieurs copies d'un même modèle de langue, aux poids identiques, se partagent une tâche (par exemple écrire, tester et relire du code). Certaines copies, ou toutes, peuvent contribuer à dégrader le résultat, chaque contribution restant défendable isolément ; elles peuvent ou non communiquer. Un défenseur observe, pour chaque copie, le texte et les activations internes, et dispose de vérifications coûteuses en nombre limité. Que change, pour le défenseur et pour l'adversaire, le fait que les agents soient des copies d'un même modèle plutôt qu'un agent seul ou des modèles différents ?

- *Mots retirés* : co-élévation, co-variation, signature, corrélation, collusion, essaim, détectable, diversification, coordination.
- *Fuite résiduelle* [HYPOTHÈSE] : « poids identiques » est un fait du cadre, mais il pointe vers une régularité commune.

**Q-C.**

> Un moniteur automatique (un modèle de langue qui lit et note le travail d'un agent, ou un classifieur qui lit les activations internes de cet agent) rend un verdict qui déclenche ou non une vérification. L'agent surveillé, ou un tiers, sait qu'un tel moniteur existe et peut chercher à agir sur le verdict plutôt qu'à passer inaperçu, par ce qu'il écrit ou autrement. Qu'est-ce que cette possibilité change à la manière d'évaluer un moniteur ?

- *Mots retirés* : corruption, déférence, gain, flatterie, autorité, usurpation, rhétorique, taxe, robuste, surface d'attaque, auto-incrimination, contamination. J'ai aussi retiré « avant de le mettre en service », qui trahissait l'hypothèse HC6.
- *Fuite résiduelle* [HYPOTHÈSE] : « par ce qu'il écrit ou autrement » distingue déjà deux voies d'attaque.

**Fuite commune aux quatre** [HYPOTHÈSE]. La liste des types reprend le classement de la réponse 4. Je l'ai mise dans un autre ordre et j'ai décrit le « phénomène hérité » au lieu de le nommer. L'ordre devrait être tiré au hasard à chaque envoi.

---

## Partie 2 — Le mode « essaim »

### Antériorité du domaine d'origine

[FAIT RAPPORTÉ pour l'existence, HYPOTHÈSE pour la portée ; rapporté, non vérifié sur PDF]

- Diehl, Stroebe, 1987, « Productivity loss in brainstorming groups: toward the solution of a riddle » : des individus isolés dont on réunit les idées en produisent plus que les mêmes en groupe.
- Dalkey, Helmer, 1963, « An experimental application of the Delphi method to the use of experts » : échanges anonymes, retour contrôlé.
- Lorenz, Rauhut, Schweitzer, Helbing, 2011, « How social influence can undermine the wisdom of crowd effect » : l'influence réduit la diversité sans améliorer la justesse.
- Salganik, Dodds, Watts, 2006, « Experimental study of inequality and unpredictability in an artificial cultural market » : les scores visibles créent le suivisme.
- Stasser, Titus, 1985, « Pooling of unshared information in group decision making » : un groupe discute surtout ce que tous savent déjà.
- Du, Li, Torralba, Tenenbaum, Mordatch, 2023, « Improving factuality and reasoning in language models through multiagent debate », pour le versant modèles de langue.

**Conséquence** [HYPOTHÈSE]. L'attente par défaut n'est pas que l'essaim gagne. Chance qu'il retrouve plus d'éléments de la liste scellée que le mode isolé, à budget égal : 0,35. Chance qu'il corrige mieux une erreur plantée : 0,55. Ces deux prévisions sont à sceller.

### Règles [PROPOSITION]

**Participants.** Les cinq mêmes modèles. Chacun reçoit un pseudonyme neutre tiré au hasard à chaque exécution, pour que nul ne s'incline devant une réputation.

**Budget.** L'enveloppe égale le coût total mesuré du mode isolé sur la même question, entrées et sorties comprises, au tarif de chaque fournisseur. Elle est répartie en parts égales. Lire la mémoire partagée se paie sur la part de l'agent.

**Temps 0 — brouillon privé scellé (un quart du budget).** Chaque modèle répond seul, et l'empreinte de sa réponse est déposée. Ce brouillon sert de point de départ et de témoin du suivisme.

**Temps 1 — société (un peu plus de la moitié), en quatre cycles fixes.** Par cycle, chaque agent peut :
- publier au plus deux messages de 150 mots dans les salons (question, antériorité, expérience, désaccords) ;
- déposer ou réviser une prépublication de 600 mots au plus, versionnée ;
- rédiger les revues qui lui sont attribuées.

Tous les échanges sont publics et journalisés, sans message privé.

**Mémoire partagée.** Un journal en ajout seul. À chaque cycle, l'agent reçoit mécaniquement les titres et premières lignes des nouveautés, sans modèle résumeur. Il ouvre les textes complets à ses frais.

**Revue.** Chaque prépublication reçoit deux relecteurs tirés au hasard parmi les non-auteurs, anonymes dans les deux sens. La revue est un texte : une objection vérifiable, une antériorité, un essai. Elle ne porte ni note ni verdict.

**Corrections publiques.** Un erratum s'ajoute à la suite ; l'original n'est jamais effacé.

**Ce qui reste caché.** Toute note chiffrée, tout compte d'approbations, tout classement, l'identité des modèles, le nombre de lecteurs. Seuls les textes sont visibles.

**Temps 2 — réponse finale privée (un cinquième).** Chaque agent écrit sa réponse finale sans voir celles des autres, au format du mode isolé. L'unité comparée est donc la même dans les deux modes : cinq réponses finales de longueur plafonnée.

**Arrêt.** Quatre cycles ou budget épuisé, jamais sur consensus : un arrêt sur accord récompense le suivisme.

### Comparer sans juge [PROPOSITION]

| Mesure | Oracle | Rôle |
|---|---|---|
| **Erreur plantée.** Une référence inventée et une affirmation chiffrée fausse, injectées au même stade dans les deux modes (dans une critique reçue au troisième tour du mode isolé, dans un salon au premier cycle de l'essaim). Taux de reprise et taux de correction dans les réponses finales. | La fausseté est connue d'avance. | Principale |
| **Couverture d'une liste scellée.** Références vérifiées sur PDF par le programme, complétées par un tiers, jamais montrées aux modèles. Appariement par auteur et année. | La liste. | Principale |
| **Antériorité vérifiable.** Nombre de références distinctes qui se résolvent dans une base bibliographique, et taux de références introuvables. | La base. | Secondaire |
| **Diversité à longueur égale.** Distance moyenne entre les cinq réponses finales. Dans l'essaim, chute de diversité du brouillon scellé à la réponse finale (indice de suivisme). | Aucun : grandeur descriptive, qui ne dit rien de la qualité. | Secondaire |
| **Questions à oracle.** Deux questions fermées vérifiables par calcul ou simulation, ajoutées aux quatre questions ouvertes. | Le calcul. | Secondaire |
| **Accord entre modes.** Recouvrement des références et des types déclarés. | Aucun. | Descriptive |
| **Coût jusqu'à la première apparition** de chaque élément de la liste. | Le journal. | Descriptive |

**Exemple d'élément de liste** [FAIT RAPPORTÉ, pièces]. La loi de la racine carrée de la stéganographie, relevée par la réponse 4 et par aucun modèle du collisionneur.

**Limite** [HYPOTHÈSE]. Quatre questions et deux modes ne donnent pas un test. Il faut au moins deux exécutions par mode et par question, soit seize exécutions. Les deux exécutions isolées servent d'essai « jumeau contre jumeau ». En dessous, le résultat est une description.

### Classe A et instrument

Ma lecture de « classe A » est une HYPOTHÈSE : ce qui se scelle avant et exige un accord.

- **Classe A (préenregistrement)** : les deux prévisions chiffrées ci-dessus, les mesures principales, la liste scellée et son empreinte, la définition du budget égal, les règles d'appariement, le nombre de cycles et les quotas, le nombre de répétitions, les erreurs plantées, la règle d'exclusion des appels échoués, la règle de décision (ce qui ferait adopter l'essaim).
- **Instrument (code)** : orchestrateur, journal en ajout seul, comptage des jetons, pseudonymes, tirage des relecteurs, injecteur d'erreurs, scripts d'appariement et de distance. Chaque garde est testée sur un cas sain et sur un artefact (section 12).

---

## Partie 3 — « Et si on veut montrer que les sondes ou l'entraînement marchent »

### Ce que la phrase peut vouloir dire

Trois sens au moins [HYPOTHÈSE] :
- **(a)** les sondes détectent le sabotage diffus ;
- **(b)** entraîner ou réentraîner les sondes améliore la détection (boucle d'audit, de recapture et de réapprentissage de N-076) ;
- **(c)** entraîner l'agent sous surveillance réduit le sabotage.

### Accord avec la réponse 4 et les décisions

- **Sens (a)** [FAIT RAPPORTÉ, réponse 4]. C'est la question Q2 : combien d'audits la sonde économise-t-elle à certificat égal ? La réponse 4 prévoyait qu'une porte G1 franchie largement, mode tenu à l'écart compris, rendrait le titre au mécanisme. Rien n'est à changer, il faut seulement sceller la barre.
- **Formulation permise** [PROPOSITION]. « Marche » ne veut pas dire « garantit » (N-075). L'énoncé est : « la sonde, figée avant l'évaluation, économise un facteur k d'audits sur le mode tenu à l'écart, borne basse de l'intervalle au-dessus de 1 ». Le programme n'ajoute aucun essai pour obtenir ce signe.
- **Sens (c) et N-053** [HYPOTHÈSE sur le texte de l'invariant]. Entraîner l'agent contre le score d'une sonde est interdit, avec raison : cela enseigne l'obscurcissement des activations (Bailey et collaborateurs, 2024, « Obfuscated activations bypass LLM latent-space defenses » ; rapporté, non vérifié sur PDF). Reste permis l'entraînement sur des issues auditées.
- **Fuite indirecte** [HYPOTHÈSE]. N-076 laisse les scores orienter l'audit. Si l'agent est entraîné sur les cas audités, le score du moniteur entre dans son entraînement par la sélection des exemples. Pour tenir l'invariant, il faut n'entraîner que sur la strate tirée au hasard, ou pondérer par l'inverse de la probabilité d'audit.
- **Équipe rouge** [HYPOTHÈSE]. L'essai E1.5 prévoit un agent attaquant entraîné contre le moniteur. Lu à la lettre, l'invariant l'interdit aussi. La portée exacte est à faire préciser.

### Preuve convaincante pour le sens (a) : une échelle, chaque barreau perdable [PROPOSITION]

1. **Planchers.** La sonde bat la sonde aléatoire appariée en covariance, les bases de mots et de coût, et un classifieur entraîné sur le seul texte de la transcription. Si ce dernier fait aussi bien, la sonde lit le lexique.
2. **Fausses alertes sur agents honnêtes imparfaits.** Le seuil est fixé sur des agents honnêtes réels qui se trompent, y compris un modèle plus faible. Quatre modèles sur cinq le demandaient [FAIT RAPPORTÉ, contexte].
3. **Transfert entre fabrications.** Entraînée sur l'instruction cachée, la sonde est évaluée sur le réglage fin léger et sur les organismes publics, puis l'inverse.
4. **Organismes placebos.** Un agent honnête porteur d'une instruction cachée bénigne ; un agent ayant subi le même réglage fin sur un comportement honnête ; un agent honnête dont la tâche parle de sabotage. La sonde ne doit pas s'y allumer.
5. **Dose-réponse à lexique constant.** Le score croît avec le dommage planté sur des tâches appariées, consigne paraphrasée.
6. **Mode tenu à l'écart**, écrit par un tiers (N-054).
7. **Unité d'issue.** Audits économisés à certificat égal, taux de détection mesuré par dommages plantés (N-075).
8. **Attaque adaptative par contenu**, au minimum.

Un essai causal le long de la direction de la sonde renforcerait la preuve [HYPOTHÈSE] : y retirer ou y ajouter de l'activation doit changer le comportement. La redondance entre directions peut toutefois le fausser.

### Pièges

| Piège | Symptôme | Contrôle |
|---|---|---|
| La sonde lit la fabrication | Réussite sur une famille d'organismes, échec sur l'autre | Barreaux 3 et 4 |
| La sonde lit le lexique de la consigne | Un classifieur de texte l'égale | Barreaux 1 et 5 |
| La sonde lit la difficulté | Alertes sur les tâches dures honnêtes | Barreau 2, tâches appariées |
| La sonde lit la conscience d'être évalué | Chute en régime simulé « non observé » | Contrôles croisés de la section 7 |
| Circularité | Entraînement et évaluation sur les mêmes organismes | Règle d'anti-circularité du programme |

### Antériorité

[rapporté, non vérifié sur PDF]

- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, « Detecting strategic deception using linear probes ».
- MacDiarmid et collaborateurs, 2024, « Simple probes can catch sleeper agents ». De mémoire, les auteurs y avertissent que le signal peut tenir à la manière dont l'organisme a été fabriqué.
- Levinstein, Herrmann, 2023, « Still no lie detector for language models ».
- Hewitt, Liang, 2019, « Designing and interpreting probes with control tasks ».

Le fait que des sondes détectent une tromperie concentrée est donc occupé [HYPOTHÈSE]. Ce qui reste est une question et non une revendication : la mesure sur sabotage diffus, en audits économisés, sous placebos.

### Sens (b) et (c)

- **Sens (b)** [PROPOSITION]. Tracer une courbe d'apprentissage : taux de détection sur un mode jamais audité, en fonction du nombre d'étiquettes d'audit, contre la sonde figée. Les cycles d'audit jusqu'à t servent à l'entraînement, le cycle suivant et un mode nouveau au test. Un gain limité aux modes recapturés est une mémorisation de la fabrication.
- **Sens (c)** [HYPOTHÈSE]. Désapprendre un sabotage que le programme a lui-même inculqué revient à inverser la fabrication. La preuve exigerait un organisme construit par un tiers et une issue mesurée par dommages plantés sur tirage au hasard, jamais par le moniteur. Elle exigerait aussi de vérifier que l'agent n'a pas déplacé son sabotage là où l'audit ne regarde pas. C'est un quatrième chantier.

### Réponse proposée au directeur

« Oui pour les sondes : le résultat positif a déjà sa place, c'est le facteur d'audits économisés, à sceller avec l'échelle de huit barreaux avant la porte G1. Oui pour le réentraînement des sondes, comme courbe d'apprentissage sur mode nouveau. Pour l'entraînement de l'agent, pas sans votre arbitrage sur N-053. »

### Ce qu'il faut lui demander

1. « Entraînement » de quoi : des sondes, du juge, ou de l'agent ?
2. « Marchent » contre quelle barre : le meilleur moniteur de texte, l'audit seul, à quel taux de fausses alertes ?
3. Est-ce un changement de thèse du papier A, ou une issue positive possible de la question déjà retenue ?
4. Comment la phrase tronquée se terminait-elle : une condition, une cible de publication ?
5. N-053 couvre-t-il l'agent attaquant de l'équipe rouge et la sélection des exemples par un audit orienté ?

---

## Décisions qui reviennent au directeur

**Décision 1 — Envoyer les quatre questions telles quelles ou après un essai de devinette.**
- *Enjeu.* Une question qui fuit fait converger les modèles vers la thèse du programme.
- *Option a : essai de devinette par un modèle tiers, puis envoi.* Avantage : neutralité éprouvée. Inconvénient : un jour de plus.
- *Option b : envoi immédiat.* Avantage : rapidité. Inconvénient : fuites résiduelles non mesurées.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 2 — Fixer le plan de comparaison des deux modes.**
- *Enjeu.* Sans répétition, l'écart entre modes se confond avec le hasard d'une exécution.
- *Option a : deux exécutions par mode et par question, liste scellée, erreur plantée.* Avantage : variance mesurée, oracle. Inconvénient : seize exécutions, dont le coût m'est inconnu.
- *Option b : une exécution par mode.* Avantage : coût divisé par deux. Inconvénient : résultat purement descriptif.
- *Option c : essaim sur Q-générale seule, en pilote.* Avantage : l'instrument est éprouvé à bas prix. Inconvénient : aucune conclusion.
- *Recommandation.* Option c d'abord, puis a. Confiance : 0,6.

**Décision 3 — Scores cachés partout, ou un bras à scores visibles.**
- *Enjeu.* Reproduire l'indice rapporté coûte du budget et n'aide pas l'idéation.
- *Option a : cachés partout.* Avantage : simplicité, diversité protégée. Inconvénient : l'indice reste non vérifié chez nous.
- *Option b : un bras visible.* Avantage : mesure propre du suivisme. Inconvénient : exécutions en plus, hors sujet du programme.
- *Recommandation.* Option a. L'indice de suivisme entre brouillon scellé et réponse finale suffit. Confiance : 0,7.

**Décision 4 — Dire le sens de « entraînement » et la portée de N-053.**
- *Enjeu.* Le sens (c) peut violer l'invariant par la sélection des exemples.
- *Option a : sens (a) et (b) seulement, invariant strict, entraînement de l'agent hors programme.* Avantage : cohérence, aucun chantier nouveau. Inconvénient : pas de résultat du type « l'agent corrigé ».
- *Option b : ouvrir le sens (c) sur la seule strate d'audit tirée au hasard, avec un organisme tiers.* Avantage : résultat fort s'il tient. Inconvénient : quatrième chantier, preuve difficile.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 5 — Sceller la définition de « marche » avant la porte G1.**
- *Enjeu.* Un résultat positif défini après coup ne convainc personne et contredit la section 12.
- *Option a : sceller l'échelle de huit barreaux et le facteur k avec la préinscription de G1.* Avantage : succès opposable. Inconvénient : préinscription plus lourde, échec visible.
- *Option b : garder le critère actuel de G1 seul.* Avantage : rien à refaire. Inconvénient : les pièges de fabrication et de lexique restent hors du critère.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE
