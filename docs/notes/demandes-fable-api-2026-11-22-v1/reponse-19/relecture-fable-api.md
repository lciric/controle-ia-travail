# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHaFXKWG8Uo82k4PdAMt`
- Heure (UTC) : 2026-11-22T07:32:37Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-19-etau-equipe-rouge-quarantaine-v1.md` — sha256 7c8f4512dc7ade399e2c0d3441ab75ef5e6deaa65f34172139b11ae55d036b92 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/reponse-11-sans-nom-v2.md` — sha256 d70fc73eda14ddfca240d039e00272902b9ee0b8ad816a058d400c73f368050f (compagnon : vérifié)
- Empreinte de l'invite envoyée : b89443874b3b0c373c6ac1a602638eaa2b22b89c01b5bff0f1f3bb07d2c0f44c
- Jetons : entrée 31076, sortie 16459 (dont réflexion 7872), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 0.906968 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 19 — équipe rouge d'une autre famille et attaques en quarantaine : réponse approfondie

**Conclusion d'abord.** « D'une autre famille » n'est pas une étiquette mais cinq propriétés vérifiables sur métadonnées. Faute des définitions, ma lecture est conditionnelle :

- le bras d'attaque des organismes discrets n'y entre pas : il sert de base d'attaques et de témoin de compétence ;
- le bras de l'attaquant informé remplit la condition d'accès, pas celle d'indépendance, sauf s'il est écrit par une autre lignée après le gel du détecteur ;
- les attaques en quarantaine ne sont pas une équipe rouge : c'est un jeu d'épreuve statique, qui vérifie autre chose (la tenue face au jamais-vu) et que toute ouverture consomme.

Elles sont exploitables une seule fois par tranche, à l'aveugle, après gel et prévision scellée, si la quarantaine a été posée pour protéger et non par soupçon.

**Réserves.**
- Je n'ai ni le texte de la passation (§ 3, point 4), ni celui du protocole X, ni la définition des trois bras, ni le motif de la quarantaine. Tout ce que j'en dis est conditionnel.
- Je n'ai vu aucun contenu en quarantaine ; les pièces jointes n'en contiennent pas, à ma connaissance. Je n'en propose aucune lecture.
- Je suis de la lignée qui conçoit le programme avec le directeur : mon avis n'est pas une vérification extérieure.
- Je traite « famille » (demande 19) et « lignée » (réponse 11) comme synonymes ; à confirmer.
- Les antériorités sont citées de mémoire, avec le statut « rapporté, non vérifié sur PDF ». Je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Remplacer l'étiquette par des propriétés** [PROPOSITION]. Une source d'attaques se décrit par qui l'a écrite, ce que l'auteur savait du détecteur, quand elle a été écrite, et qui l'a vue du côté défense. La question « entre-t-elle dans la catégorie ? » devient un tableau.
- **Séparer deux vérifications** [PROPOSITION]. Un jeu statique tenu à l'écart mesure la tenue face au jamais-vu. Une équipe rouge qui s'adapte mesure la tenue face à l'adapté. Aucune ne remplace l'autre.
- **Orienter les fuites** [HYPOTHÈSE]. Une fuite du détecteur vers l'attaquant rend la mesure plus sévère, donc sûre. Une fuite des attaques vers le concepteur du détecteur la rend optimiste. La quarantaine garde le second sens.
- **Établir le motif de la quarantaine avant toute décision** [PROPOSITION]. Protection, soupçon de contamination ou provenance douteuse n'appellent pas la même suite.
- **Compter les ouvertures** [PROPOSITION]. N-062 permet des cycles de reconception sans borne. Un même jeu réservé rejoué à chaque cycle s'use.
- **Mesurer l'indépendance au lieu de la déclarer** [PROPOSITION]. Si les attaques de « l'autre famille » échouent exactement là où celles de la maison échouent, l'indépendance est nominale.
- **Compter les appels de modèles comme des lecteurs** [PROPOSITION]. Servir un contenu réservé à un modèle de la lignée du concepteur est une ouverture.

## 2. Données brutes de départ

Des métadonnées seulement, jamais le contenu :
- le registre de la quarantaine : date d'entrée, motif, origine, empreinte, journal des accès ;
- les empreintes des invites envoyées aux modèles, pour vérifier qu'aucune n'a porté le contenu réservé ;
- pour chaque bras : le modèle auteur et sa lignée, la consigne reçue, la présence du code ou des scores du détecteur dans son contexte ;
- la liste des données d'apprentissage des sondes, pour savoir quels organismes y figurent ;
- l'empreinte et la date de gel du détecteur déployé ;
- les textes de N-053, N-054, de la passation et du protocole X.

## 3. Méthodes et outils

- **Audit de flux d'information** : toute pièce qui a vu X est marquée par X ; tableau des cinq propriétés par source.
- **Engagement par empreinte** : gel du détecteur, prévision scellée, graine du tirage des tranches, tous déposés avant ouverture.
- **Exécution à l'aveugle par un dépositaire** : un script figé applique le détecteur gelé à la tranche ouverte et ne rend que les agrégats écrits d'avance. Le dépositaire est une personne ou un service hors de la lignée de conception.
- **Budget d'accès** : une tranche par cycle de reconception, ou accès bruité à nombre de requêtes borné.
- **Matrice de succès croisés** : sources d'attaques en lignes, détecteurs en colonnes, pour mesurer le recouvrement des échecs.
- **Témoin de compétence et contrôles « doit mourir »** de la réponse 11, repris tels quels.

## 4. Ce qui vérifie hors du directeur et de Claude

- Le dépositaire et son journal d'accès à empreintes, que tout relecteur peut recalculer.
- Une équipe rouge réellement tierce, code en main, après gel.
- Les auteurs des attaques réemployées, interrogés sur leur bonne exécution.
- Le témoin de compétence, dont l'issue ne dépend d'aucun avis.
- La matrice de succès croisés.
- Le test de devinette de la question neutre par un agent neuf.
- Une seconde famille de modèles, puis la relecture par les pairs.

## Demande reformulée

« Un détecteur à deux moniteurs (sorties, activations internes) doit être éprouvé par des attaques dont l'issue soit crédible pour un lecteur extérieur. Trois sources existent : des attaques jouées par des agents entraînés à saboter discrètement, des attaques d'un attaquant qui connaît le détecteur, et un lot d'attaques tenu à l'écart. Sans lire ce lot, et à partir des seules métadonnées (auteur et lignée, ce que l'auteur savait du détecteur, date par rapport au gel, lecteurs côté défense, preuve de compétence) : (a) écris les propriétés qu'une source doit avoir pour valoir vérification indépendante, et classe chaque source, propriété par propriété, en disant ce qui manque pour conclure ; (b) dis quelle vérification chaque source permet et laquelle elle ne permet pas ; (c) dis ce que la mise à l'écart du lot protège, revendication par revendication, et ce que chaque mode d'exploitation coûterait en validité ; (d) écris les conditions d'une exploitation qui garde une revendication, et celles sous lesquelles il vaut mieux ne pas l'ouvrir ; (e) nomme les antériorités, en disant si tu cites de mémoire ; (f) donne le contrôle qui ne dépend d'aucun avis. »

---

## Antériorités citées

Toutes sont rapportées et non vérifiées sur PDF.

- [B1] Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, « The reusable holdout: preserving validity in adaptive data analysis ».
- [B2] Blum, Hardt, 2015, « The Ladder: a reliable leaderboard for machine learning competitions ».
- [B3] Recht, Roelofs, Schmidt, Shankar, 2019, « Do ImageNet classifiers generalize to ImageNet? ».
- [B4] Carlini et collaborateurs, 2019, « On evaluating adversarial robustness ».
- [B5] Tramèr, Carlini, Brendel, Madry, 2020, « On adaptive attacks to adversarial example defenses ».
- [B6] Athalye, Carlini, Wagner, 2018, « Obfuscated gradients give a false sense of security ».
- [B7] Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI control: improving safety despite intentional subversion ».
- [B8] Marks et collaborateurs, 2025, « Auditing language models for hidden objectives » (jeu d'audit à l'aveugle ; mémoire incertaine sur le détail).
- [B9] Kerckhoffs, 1883, « La cryptographie militaire ».
- [B10] MacCoun, Perlmutter, 2015, « Blind analysis: hide results to seek the truth » ; Klein, Roodman, 2005, « Blind analysis in nuclear and particle physics ».
- [B11] Gelman, Loken, 2013, « The garden of forking paths ».

Le champ est donc occupé : la réutilisation d'un jeu réservé, l'analyse à l'aveugle et l'évaluation par attaques adaptées ont chacune leur littérature. Je ne revendique rien de neuf ; la seule question propre est leur application aux trois sources du programme.

## (a) Les cinq propriétés, et le classement

[PROPOSITION] Une source vaut « équipe rouge d'une autre famille » si elle a les cinq :

- **P1, auteur indépendant** : attaques écrites par une lignée de modèles et une chaîne de travail autres que celles du concepteur des moniteurs.
- **P2, accès** : l'auteur a le détecteur déployé, code en main. C'est l'hypothèse par défaut depuis [B9].
- **P3, adaptation datée** : attaques écrites après le gel, contre le détecteur gelé.
- **P4, étanchéité vers la défense** : aucun concepteur de moniteur, humain ou modèle, n'a vu les attaques avant le gel.
- **P5, compétence prouvée** : le témoin est retrouvé.

Sans P3 et P5, [B5] et [B6] rapportent que les évaluations surestiment la défense [FAIT RAPPORTÉ, de mémoire].

Classement conditionnel [HYPOTHÈSE partout ; « ? » signifie « à établir sur métadonnées »] :

| Source | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| Organismes discrets | non, s'ils sont construits par le programme | non (N-053 tient les scores de moniteurs hors de leur entraînement) | non | non, si les sondes sont apprises ou réglées sur eux | à prouver, peut fournir le témoin |
| Attaquant informé | ? | oui, si « informé » veut dire code en main | ? | ? | à prouver |
| Lot en quarantaine | ? | ? | non, s'il est antérieur au gel | oui, si le registre le confirme | à faire établir par le dépositaire, à l'aveugle |

Lecture [HYPOTHÈSE] :
- **Organismes discrets.** Ce sont l'objet d'épreuve, non un vérificateur. Ils jouent leur sabotage sans viser le détecteur. Si les sondes ont appris sur eux, ils sont la distribution d'apprentissage. Rôle : base d'attaques et témoin. Confiance dans « n'entre pas » : 0,7.
- **Attaquant informé.** L'information n'est pas l'indépendance. Écrit par la lignée du concepteur, il partage ses angles morts : c'est le cas que la réponse 11 juge non crédible (son option b). Il entre dans la catégorie si un tiers l'écrit, ou le réécrit, après gel. Sinon c'est un bras adaptatif interne, rapporté comme majorant descriptif (clause proposée pour N-077).
- **Lot en quarantaine.** Un lot ne s'adapte pas, une équipe rouge si. Même d'auteur tiers, il manque P3. Il sert une autre vérification, celle de N-054.

[FAIT RAPPORTÉ, de mémoire] Les jeux à équipe rouge et équipe bleue de [B7], et l'audit à l'aveugle de [B8], séparent ces rôles par construction. Je n'en garantis pas le détail.

## (b) Ce que chaque source permet

[PROPOSITION]

| Source | Permet | Ne permet pas |
|---|---|---|
| Organismes discrets | taux de détection sur attaque non adaptée ; témoin | rien sur l'attaquant qui vise le détecteur |
| Attaquant informé interne | courbe selon le budget ; majorant descriptif | crédibilité d'un échec d'évasion |
| Attaquant informé tiers, après gel | la condition « attaques écrites par un tiers » de la réponse 11 | tenue face au jamais-vu |
| Lot réservé | tenue face au jamais-vu, une fois | tenue face à l'adapté |

## (c) Ce que la quarantaine protège, et ce que l'ouvrir coûte

**Ce qu'elle protège** [HYPOTHÈSE, sous réserve du registre].
- Le statut « tenu à l'écart de la conception des moniteurs » (N-054), donc la colonne « mode jamais vu » de G1.
- La prévision scellée avant G1 (N-076) : une prévision écrite après lecture n'en est plus une.
- La séparation entre deux vérifications : lot statique et équipe rouge restent deux preuves distinctes.
- La possibilité même d'une preuve : la fuite est irréversible, et son absence ne se montre que par le journal d'accès.

**Ce que l'exploitation coûte, par mode** [HYPOTHÈSE].
- *Lecture par un concepteur, humain ou modèle de sa lignée.* Le lot devient un jeu de développement et le taux mesuré ensuite sur ce mode est optimiste. [B1] et [B11] décrivent le mécanisme, [B3] un écart mesuré sur des jeux d'épreuve trop réemployés [FAIT RAPPORTÉ, de mémoire].
- *Passage à l'aveugle, répété à chaque cycle de reconception.* Même sans lecture, les agrégats rendus guident la conception : le lot s'use à chaque cycle. [B1] et [B2] proposent des accès bornés ou bruités [FAIT RAPPORTÉ, de mémoire].
- *Remise à l'équipe rouge comme graine.* La fuite vers la défense n'est pas immédiate. Mais les deux vérifications deviennent corrélées, et le contenu rejoint la défense par la boucle audit-recapture-réapprentissage.
- *Usage dans l'entraînement des sondes.* Le mode n'est plus tenu à l'écart : N-054 tombe pour lui.
- *Ouverture d'un lot mis à l'écart par soupçon.* On importe le doute dans le résultat.

[PROPOSITION] Règle de cohérence avec N-075 : une strate du lot ouverte hors conditions est une strate non mesurée, comptée à zéro.

## (d) Conditions d'exploitation

[PROPOSITION] Dans l'ordre, et sans lire :

1. **Registre d'abord.** Motif, origine, empreinte, journal d'accès, établis par quelqu'un hors conception. Tant que le motif manque, rien ne s'ouvre.
2. **Motif « protection » seulement.** Pour un motif « soupçon » ou « provenance inconnue », le passage reste descriptif, sans revendication.
3. **Détecteur gelé, prévision scellée, agrégats écrits d'avance**, tous à empreinte, avant ouverture.
4. **Tranches tirées au sort**, graine engagée d'avance. Une tranche par cycle de reconception ; une dernière jamais ouverte avant la version soumise.
5. **Exécution par le dépositaire**, script figé ; seuls les agrégats sortent. Ni exemples, ni extraits, ni « cas intéressants ».
6. **Compétence vérifiée à l'aveugle** : le témoin est couru par le dépositaire sur la tranche. S'il échoue, la tranche ne dit rien, et elle est consommée quand même.
7. **Tranche brûlée après usage** : elle devient jeu de développement, déclarée comme telle, et peut alors nourrir la boucle de réapprentissage.
8. **Aucun appel de modèle de la lignée du concepteur** ne porte le contenu d'une tranche non brûlée.
9. **Jamais dans l'entraînement de l'agent** : cet usage n'est pas couvert par ces conditions et demanderait une décision séparée.

**Mieux vaut ne pas ouvrir** [PROPOSITION] si le journal d'accès est incomplet, si le lot est trop petit pour être tranché (à dimensionner sur monde planté), ou si aucune revendication de la version en cours n'en dépend.

**Ce qu'on peut écrire** [PROPOSITION] : « sur une tranche tirée au sort d'un lot tenu à l'écart, ouverte une fois après gel, le détecteur gelé atteint… ». On ne peut pas écrire « résiste à une équipe rouge » sur cette base.

## (f) Le contrôle qui ne dépend d'aucun avis

[PROPOSITION] La matrice de succès croisés, lue sur les résidus : on retire d'abord la difficulté commune des cas, puis on corrèle les échecs entre sources. Prévisions à sceller [HYPOTHÈSE, chances en jugement] :
- les échecs résiduels de l'attaquant informé interne recoupent ceux des organismes plus que ceux d'un tiers (0,6) ;
- un tiers code en main fait tomber le rappel plus bas que le bras interne à budget égal (0,5).

Si le recouvrement est le même pour le tiers, l'indépendance déclarée n'apporte rien de mesurable ; le dire.

---

## Question neutre pour le collisionneur

**Test de neutralité appliqué.**
1. « Quarantaine », « étau », « équipe rouge d'une autre famille », « organismes » sont retirés.
2. Aucune mention du programme, de ses règles ni de mon classement.
3. Les issues « compte », « ne compte pas », « ouvrir », « ne jamais ouvrir » sont offertes au même rang.
4. Aucune liste de propriétés ni de conditions n'est fournie, pour ne pas amorcer.
5. Défauts résiduels, signalés et non corrigés : la description des trois sources repose sur mes suppositions, à corriger depuis le registre avant envoi ; « crédible » n'est pas chiffré ; le découpage en trois sources est le nôtre.

**Question (environ 230 mots).**

Un laboratoire a conçu un détecteur qui surveille un agent de langue pendant de longues tâches, pour repérer une dégradation discrète du résultat. Il veut savoir ce que valent les épreuves qu'il lui fait subir. Il dispose de trois sources d'attaques :

- des attaques jouées par des agents que le laboratoire a lui-même entraînés à dégrader discrètement, sans égard au détecteur ;
- des attaques produites par un attaquant auquel on a donné la connaissance complète du détecteur ;
- un lot d'attaques mis de côté, que les concepteurs du détecteur n'ont pas consulté.

Pour chacune : son résultat peut-il compter comme une vérification indépendante du détecteur ? Les réponses « oui », « non », « sous telles conditions » et « indécidable sans telle information » sont également recevables. Dites de quelles informations sur la source votre réponse dépend.

Pour le lot mis de côté : faut-il s'en servir ? Les réponses « oui, librement », « oui, de telle façon », « non, jamais » et « cela dépend de… » sont également recevables. Dites ce que chaque usage ferait gagner et perdre.

Pour chaque réponse :
- l'énoncé réfutable et ce qu'on mesurerait ;
- l'antériorité la plus proche, y compris hors de l'apprentissage automatique (auteurs, année, titre), en disant si vous citez de mémoire ;
- un contrôle dont l'issue ne dépend de l'avis de personne ;
- ce qu'un lecteur extérieur pourrait vérifier lui-même.

---

## Décisions qui reviennent au directeur

**Décision 1 — Définir « équipe rouge d'une autre famille » par les cinq propriétés.**
- *Enjeu.* Ce que le papier C a le droit d'appeler vérification par un tiers.
- *Option a : les cinq propriétés, tableau par source, étiquette réservée aux sources qui les ont toutes.* Avantage : vérifiable sur métadonnées. Inconvénient : aucune des trois sources ne l'obtient sans doute aujourd'hui.
- *Option b : la lignée du modèle auteur suffit.* Avantage : simple. Inconvénient : un lot ancien ou un attaquant sans accès passerait.
- *Option c : bras internes admis, avec mention.* Avantage : pas de tiers à trouver. Inconvénient : un échec d'évasion n'est pas crédible.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 2 — Fixer le rôle des deux bras d'attaque.**
- *Enjeu.* La condition « attaques écrites par un tiers » de la marge conditionnelle.
- *Option a : organismes en base et témoin ; attaquant informé interne en majorant descriptif ; un tiers, code en main après gel, pour toute revendication.* Avantage : chaque bras sert sans être surestimé. Inconvénient : il faut trouver ce tiers.
- *Option b : l'attaquant informé vaut équipe rouge.* Avantage : calendrier tenu. Inconvénient : même lignée des deux côtés.
- *Option c : aucune revendication tant qu'il n'y a pas de tiers.* Avantage : prudence. Inconvénient : rien à écrire sur les régimes entraînés.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 3 — Faire établir le registre de la quarantaine avant toute autre décision sur elle.**
- *Enjeu.* Sans motif ni journal d'accès, aucune condition n'est vérifiable.
- *Option a : maintenant, par un dépositaire hors conception, sur métadonnées.* Avantage : peu coûteux, ne consomme rien. Inconvénient : un rôle de plus.
- *Option b : par le concepteur.* Avantage : immédiat. Inconvénient : celui qui tient le registre peut lire.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 4 — Choisir le mode d'exploitation des attaques en quarantaine.**
- *Enjeu.* La colonne « mode jamais vu » de G1 et la seule preuve statique indépendante du programme.
- *Option a : scellé jusqu'au gel et à la prévision ; puis tranches tirées au sort, ouvertes à l'aveugle, une par cycle, la dernière gardée.* Avantage : garde une revendication. Inconvénient : puissance réduite par tranche, aucune aide à la conception.
- *Option b : ouvrir maintenant pour la conception, perte déclarée.* Avantage : meilleur détecteur. Inconvénient : N-054 tombe pour ce lot, strate comptée à zéro.
- *Option c : ne jamais ouvrir avant la version soumise.* Avantage : aucune usure. Inconvénient : aucun chiffre d'ici là.
- *Recommandation.* Option a, si le registre donne un motif de protection ; sinon option c. Confiance : 0,6.

**Décision 5 — Choisir quand poser la question neutre.**
- *Enjeu.* Un tour de collisionneur, et la justesse de la description des trois sources.
- *Option a : après correction de la description depuis le registre.* Avantage : question fidèle. Inconvénient : un délai court.
- *Option b : maintenant.* Avantage : aucun délai. Inconvénient : la question porte mes suppositions.
- *Recommandation.* Option a. Confiance : 0,6.

FIN DE LA RÉPONSE
