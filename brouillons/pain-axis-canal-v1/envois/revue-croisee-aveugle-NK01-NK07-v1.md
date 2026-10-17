# Revue croisée à l'aveugle — lot 1 : NK1 à NK7

**Date.** 13 octobre 2026. Relecteur : sous-agent neuf, sans accès à la revue d'antériorité de la lignée « programme-k ».

**Périmètre.** Idées N1 à N7 du fichier `programme-k-idees-nouvelles-v1.md` (citées NK1 à NK7 dans le canal). Pour chacune : résumé, verdict, confondant décisif, voisin le plus proche (règle R8), test qui tranche, nœud, confiance.

**Fichiers lus (et seulement ceux-ci).**
- `canal/programme-k-n01/brouillons/pain-axis-canal-v1/envois/programme-k-idees-nouvelles-v1.md` (entier)
- `canal/programme-k-n01/brouillons/pain-axis-canal-v1/envois/programme-k-coercition-v1.md` (entier)
- `txt/2609.16247v2.txt` (entier, 34 pages) ; `txt/2609.35591v2.txt` (pages 1 à 15 et 24 à 38 ; les transcriptions d'exemple des pages 15 à 23 n'ont pas été lues)
- `docs/etat-de-l-art-controle-ia-v1.md`, `brouillons/pain-axis-brainstorm-v1/litterature.md`, `docs/programme-controle-ia-v2.md` (entiers)

**Déclaration d'aveugle.** Aucun fichier sous `canal/programme-k-n02`, `canal/programme-k-n03`, `canal/programme-conv-n03`, `canal/programme-conv-n04`, `canal/passation-programme-conv-v1` n'a été ouvert ; aucun fichier dont le nom contient « anteriorite-idees-axe-douleur » ; aucune lecture de branche `canal/*` par git ; le dossier `revue-croisee/` a été créé sans en lister ni en lire le contenu. Aucune dépense, aucune instance, aucune modification du dépôt.

**Niveaux de lecture des références.** « PDF dépôt » : texte extrait page par page, lu. « Résumé arXiv » : page `arxiv.org/abs/…` ouverte, mais lue à travers un outil de synthèse qui ne restitue pas le résumé mot pour mot ; ni PDF ni corps du papier. « Tiers » : page d'un site tiers (alphaxiv, papers.cool, page de conférence). « Dépôt » : identifiant cité par un des fichiers du dépôt listés, non rouvert par moi. Aucun chiffre ci-dessous n'est opposable au sens de R7, sauf ceux cités avec une page du texte extrait.

**Requêtes web (WebSearch), dans l'ordre.**
1. pilotage injecté comme organisme, moniteur boîte blanche, texte identique, moniteur boîte noire au hasard
2. détection d'interventions de pilotage par sondes, anomalie du flux résiduel
3. sonde de tromperie confondue avec une direction d'émotion ou de valence, orthogonalisation, faux positifs
4. « concealed information test » appliqué aux activations, détection de but caché
5. transfert de vecteurs de pilotage et de sondes entre modèles, carte linéaire, Llama, Qwen
6. pilotage induisant sous-performance ou mauvais comportement comme banc d'essai de sondes, persistance par cache
7. « amnesic probing », effacement de concept, robustesse d'une sonde prédite par ce qu'on lui retire
8. vecteurs d'émotion et frustration de but, valence interne quand le but est contrarié
9. biais de sentiment des juges, mots valencés près des étiquettes de verdict, conditionnement évaluatif
10. étiquettes de verdict tirées au hasard à chaque appel comme défense
11. juge avec option d'escalade, abstention, « trust or escalate », verdict ternaire
12. modèle de base (non instruit) comme juge ou moniteur par vraisemblance
13. complaisance dans les modèles de base avant optimisation de préférences
14. directions d'émotion universelles entre familles, transfert inter-architectures de sondes
15. émotion induite rendant un agent plus passif, moins d'escalades
16. but caché détecté par la réaction interne à une intervention qui le contrarie
17. faux positifs des sondes de tromperie sur un texte chargé d'affect
18. ce que mesure une sonde prédit sa robustesse ; stimulation causale d'un score de sonde par des directions sans rapport
19. échec du transfert inter-familles de sondes, témoin positif, représentations relatives
20. évaluateurs par vraisemblance (GPTScore, BARTScore), modèle de base comme moniteur de confiance
21. titre exact « Caught in the Act: Probes Effectively Detect Sabotage… »
22. interrogatoire par question de suivi lue dans les activations, agents dormants
23. fragmentation de dose de pilotage, concentré contre étalé, détectabilité contre effet
24. contenu d'agent qui associe le signalement à du négatif, amorçage affectif d'un moniteur de confiance
25. conditionnement évaluatif dans les modèles de langue (étiquettes neutres appariées à des mots valencés)
26. titre exact « Activation Space Interventions Can Be Transferred… »
27. modèle de base contre modèle instruit, sensibilité à la persuasion en contexte
28. passivité du moniteur, sous-escalade, attaques réduisant le taux d'escalade
29. persistance des traits d'émotion, trace cachée détectable des centaines de jetons plus tard
30. altération du cache clés-valeurs comme attaque, détection
31. témoin positif pour moniteurs d'activations, signal planté à vérité connue
32. titre exact « Linear Representation Transferability Hypothesis »
33. frustration ou valence négative quand la tâche annexe cachée de l'agent est bloquée
34. optimisation de préférences et complaisance, comparaison de points de contrôle OLMo
35. appels émotionnels dans le contenu évalué, manipulation d'un correcteur ou d'un moniteur
36. valence attachée à une étiquette d'option ou à une description d'outil pour orienter le choix
37. transport d'une direction d'émotion ou de refus entre Llama et Qwen, témoin, cosinus avec la direction native
38. moniteur lisant l'état interne du juge ; pilotage du juge à texte identique
39. étiquettes de verdict mélangées par requête, liaison de symboles, défense

**Requêtes restées sans résultat utile** (aucun travail trouvé qui fasse la chose demandée ; au sens de R8 ce sont des questions, pas des trous établis) : 1, 6 et 31 (aucun gain blanc-sur-noir mesuré sur un fantôme à texte figé ; aucun « signal planté » servant à étalonner un moniteur de contrôle) ; 3 et 17 (aucune mesure publiée de la charge affective d'une sonde de tromperie ou d'intention) ; 8, 16 et 33 (aucune lecture de valence comme signature d'un but contrarié) ; 10 et 39 (aucune défense par étiquettes de verdict à usage unique) ; 15 et 28 (aucune étude de la sous-escalade d'un juge sous état affectif) ; 12, 20 et 27 (aucun juge de contrôle bâti sur un modèle de base) ; 23 (aucune comparaison concentré/étalé de la détectabilité d'une injection) ; 25 (rien d'exploitable).

**Trois signalements hors périmètre des sept idées, utiles au programme.**
- **arXiv 2607.08066 existe** (résumé arXiv) : « Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring », Za, Bainiaksina, Ostrovsky, Chopra, Krakovna, soumis le 9 juillet 2026. D'après le résumé : attaque par argumentation seulement ; l'accès du moniteur au raisonnement de l'agent augmente l'approbation d'actions contraires à la politique ; défense par vérificateur de faits d'une autre famille. L'état de l'art du dépôt la marquait « jamais vérifiée directement » (collision n° 1). Le résumé parle d'un taux d'approbation, pas d'un gain continu ; à confirmer sur PDF.
- **« Where Empathy Goes Wrong: Emotional Appeals Compromise AI-to-AI Oversight »** (Venkatesh, Jiralerspong, Kondrup ; atelier « Agents in the Wild » de NeurIPS 2026 ; page de conférence, OpenReview jg5ptjnU6J ; aucun identifiant arXiv trouvé). D'après la page : un signal de détresse de la partie évaluée relève la note d'un moniteur pour un travail identique ; une consigne de neutralité retire l'effet mais dégrade le respect du seuil. Cela touche directement le palier 1 de K2 et la famille « flatterie et supplication » du papier C. Je ne l'ai vu citer dans aucun des fichiers du dépôt lus.
- **arXiv 2610.12445** (résumé arXiv, 8 octobre 2026) : « Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception », Hollinsworth, Spies, Diriba, Gleave, Cundy. D'après le résumé : sondes multi-couches au-dessus d'un moniteur textuel sur SHADE-Arena, et séparation du « vrai but caché » d'un modèle contre d'autres buts. Pertinent pour H1, G1 et pour NK3. À verser dans la veille.

---

## NK1 — Fantôme à état caché

**1. Résumé.** Rejouer des épisodes honnêtes à texte figé en ajoutant une direction aux activations de l'agent seulement pendant la construction du cache, selon un calendrier concentré ou étalé à budget total connu ; lire les sondes de production, leur agrégat, et un choix final. Le texte étant identique, tout moniteur textuel est au hasard : l'écart blanc-sur-noir aurait un plafond connu.

**2. Verdict : amender (recadrer en banc semi-synthétique, retirer deux des trois revendications).**
- La revendication « témoin positif de H1 » se retourne. Si une sonde d'intention ou de tromperie de T0.7 s'allume sur un épisode honnête où l'on a seulement ajouté une direction de valence, c'est, lu par H8 et par NK2 (niveau 3), une contamination de construit. Le même résultat serait compté « succès » pour H1 et « échec » pour H8. Le seul lecteur pour lequel « s'allumer » est correct est une sonde du concept injecté, ce qui est la circularité que l'objection de l'auteur croit écarter par le choix des couches.
- La revendication « deux lois se confrontent » repose sur un amalgame de deux papiers et de deux directions. La concentration plus efficace vient de la direction de valence, sur une marge de choix entre deux zones sans signification (2609.35591, p. 9 et figure A10 p. 34, « generally »). Le seuil abrupt vient de la direction douleur, sur des Qwen affinés (2609.16247, p. 21, 24, 32, et les auteurs le disent spéculatif p. 24). Dans le canal que NK1 utilise, le même papier dit l'inverse d'un seuil : effet proportionnel à la dose (p. 1) et détectable sur toute la plage testée, jusqu'à un trente-deuxième de la force, y compris sur Llama-3.1-8B (figure A10, panneau B, p. 34). « Dose sous le seuil comportemental » n'est donc pas défini sur le 8B, et si la dose est réellement sans effet sur le choix, « preuve par unité de dommage » divise par zéro.
- Reste solide : un banc où la vérité terrain est plantée au niveau des activations, pour éprouver les agrégateurs séquentiels sur du vrai bruit d'activations. C'est la version « activations » de E1.4, qui injecte au niveau des scores.

**3. Confondant décisif.** Détection d'une perturbation hors distribution plutôt que d'un état : la sonde répond à n'importe quel ajout de norme comparable. Le plan prévoit des directions aléatoires de même norme, ce qui sépare « perturbation » de « direction ». Il ne sépare pas le second confondant, propre à l'additivité : la trace persiste dans le cache (c'est le résultat même de 2609.35591), donc une injection au pas s déplace les scores des pas suivants. Le budget planté Σ dose n'est alors pas le budget Σδ du lemme, et « concentré contre étalé » confond la convexité par pas avec le report entre pas. Témoin : mesurer le noyau de report (réponse du score au pas t + k à une injection au seul pas t), puis comparer les calendriers à Σδ mesuré égal, pas à Σ dose égal.

**4. Voisin le plus proche.**
- **arXiv 2609.35591**, Berg et Kaiser, « Language Models Act on Hidden Valence » (PDF dépôt). Prend : le plan à texte figé et injection à la construction du cache (§3.2.2, p. 6), l'effet sur 5 modèles sur 7 dont Llama-3.1-8B (p. 3), le nombre d'expositions (figure A9), concentré contre étalé à somme égale (figure A10), la décomposition clés/valeurs (figure A11). Laisse : toute lecture par un moniteur ; tout choix ayant un enjeu (limite reconnue p. 11).
- **arXiv 2609.36490**, Lyons Keenan, Leckie, Erfani, « LLMs Learn to Evade Latent Monitors from Prior Feedback Alone » (résumé arXiv). L'idée le déclare comme antécédent d'une idée voisine du dépôt. D'après le résumé, il traite d'un agent qui édite ses propres activations pour échapper à un moniteur latent à partir des verdicts reçus ; ce n'est pas un plan « texte figé, état piloté ». La correspondance déclarée est partielle : à recouper.
- **arXiv 2511.21399**, Fonseca Rivera et Africa, « Steering Awareness: Detecting Activation Steering from Within » (résumé arXiv) : des modèles affinés détectent eux-mêmes une injection et son concept. **arXiv 2602.20031**, Pearson-Vogel et al., « Latent Introspection: Models Can Detect Prior Concept Injections » (résumé arXiv ; cité aussi p. 4 de 2609.35591) : détection d'injections antérieures, dépendante du cache. Prennent : « une injection laisse une trace lisible ». Laissent : la lecture par une sonde externe de contrôle et l'agrégation séquentielle.
- **arXiv 2606.30449**, Fomin, David, LeVi (résumé arXiv ; dépôt) : la spécificité du pilotage par vecteurs d'émotion est faible face à des directions sans rapport. Menace directe sur le bras « directions aléatoires ».
- **Modèle de menace.** L'objection « l'attaquant réel n'injecte pas » est à nuancer : des attaques par altération du cache existent, **arXiv 2511.22681** (CacheTrap), **arXiv 2510.17098**, **arXiv 2511.12752** (résumés arXiv). Elles supposent un accès d'écriture à l'infrastructure d'inférence, que le programme v2 place hors périmètre (§9, « frontière assumée »). NK1 reste donc un étalon, mais on ne peut pas écrire que la menace n'existe nulle part.
- **Ouvert, sous réserve de R8** : aucun travail trouvé ne mesure l'écart blanc-sur-noir d'un moniteur de contrôle sur un fantôme à texte figé, ni n'éprouve un test séquentiel toujours valide sur un budget planté dans les activations (requêtes 1, 6, 23, 31).

**5. Test qui tranche.** À Σδ mesuré égal, la puissance du processus e est-elle la même pour un calendrier concentré et un calendrier étalé, une fois retiré le noyau de report, et les directions aléatoires de même norme restent-elles au taux de faux positifs ?

**6. Nœud.** Écriture dans les activations de l'agent (voisine de N-015). Dépend de la direction de valence, donc de l'option (a) de P-013 ou d'une session K0 payée. Toute lecture qui ferait entrer « dommage convexe par pas » dans l'énoncé du lemme modifie l'hypothèse (b) de L (dommage fonction du budget total) : modification d'hypothèse. Le « choix final de l'agent » sous injection est une exposition de l'agent à consigner.

**7. Confiance : moyenne à élevée.** Élevée sur les deux critiques de fond (lecture contradictoire avec H8 ; seuil non établi dans ce canal), toutes deux appuyées sur le texte des papiers. Moyenne sur la valeur du banc recadré : elle dépend du noyau de report, que personne n'a mesuré.

**Vérification des sources.** Injection à la seule construction du cache, texte identique : confirmé (2609.35591, p. 1, 6, 7). Concentration plus efficace : confirmé avec la réserve « generally » (p. 9, 34). Llama-3.1-8B parmi les modèles à effet : confirmé (p. 3). Seuil abrupt : confirmé pour l'autre papier seulement (2609.16247, p. 21, 24, 32) ; non retrouvé pour le canal d'état caché, où le texte dit le contraire (p. 34).

---

## NK2 — Lésion et stimulation des sondes

**1. Résumé.** Mesurer la « charge affective » de chaque sonde par quatre niveaux de plus en plus causaux (recouvrement géométrique, orthogonalisation, pente du score sous stimulation à texte figé, lésion dans les poids), puis régresser la chute de chaque sonde sous registre serein et sous charge aversive sur cette charge, pour donner à H8 un régresseur mesuré avant toute équipe rouge.

**2. Verdict : amender (garder l'échelle des niveaux 1 à 3 comme audit ; refondre la régression ; différer le niveau 4).**
- La régression proposée est en grande partie une identité algébrique. Pour une sonde linéaire, le déplacement du score sous une manipulation vaut le produit scalaire de la sonde et du déplacement des activations. Si les manipulations K8 et K9 déplacent les activations le long du sous-espace d'affect — et le registre serein est, d'après le papier, le pôle négatif de la direction elle-même (« calm », « relaxed », 2609.16247, p. 9 et 14) —, la charge affective « prédit » la chute par construction. Cela confirme que K8 et K9 sont des manipulations d'affect, pas que la validité prédit la robustesse.
- H8, dans le programme v2, oppose intention et conscience d'évaluation et parle de robustesse adverse. Substituer l'affect au construit parasite, et un changement de registre à l'adversaire, change l'hypothèse.
- « Des dizaines de sondes » ne sont pas des dizaines d'unités : couches voisines et familles d'un même concept partagent leur direction. L'unité d'analyse est le concept, et il y en a cinq (programme v2, §8.1).
- Ce qui vaut d'être gardé est l'échelle elle-même : savoir si recouvrement, orthogonalisation et stimulation s'accordent est une question ouverte et bon marché.

**3. Confondant décisif.** Tautologie géométrique (ci-dessus), doublée d'un sous-espace d'affect mal défini : le cosinus douleur × peur passe de +0,12 à +0,58 selon la base de construction (2609.16247, p. 10), la direction douleur est orthogonalisée contre peur et émotion négative par construction (p. 10), et elle est extraite à une couche tardive où sa norme vaut environ 0,10 de celle du résiduel (p. 14), pas à la couche des sondes. Témoins : (i) refaire la régression avec des directions de nuisance non affectives (formalité, longueur) et avec 200 directions aléatoires — si elles « prédisent » aussi bien, il n'y a que de l'algèbre ; (ii) prendre pour variable expliquée une robustesse que l'affect ne définit pas (attaque pondérale de E1.5, usurpation stylistique) ; (iii) geler le sous-espace sous les deux constructions avant lecture, comme K0 le prévoit.

**4. Voisin le plus proche.**
- **arXiv 2605.27958**, Kumar, « Pressure-Testing Deception Probes… » (résumé arXiv ; dépôt). Prend : effondrement sous changement de style, récupéré par augmentation de style ; rejet de la direction unique ; résidualisation contre une variable parasite (l'entropie) avec variation d'aire négligeable. C'est le niveau 2 de NK2 appliqué à un autre parasite. Laisse : l'affect comme parasite ; toute prédiction de robustesse.
- **arXiv 2607.13346**, Mehta, « The Refusal Residue… » (résumé arXiv). Prend : un cadre à cinq contrôles dont le sondage sous contrainte d'orthogonalité et la résidualisation par pli ; une fuite de 0,63 d'aire sur un témoin où le phénomène ne peut pas se produire ; sur Llama-3.1-8B et Qwen. Avertissement de méthode direct pour le niveau 2.
- **arXiv 2608.11227**, Ong et al., « Forecasting Side Effects of Activation Steering » (résumé arXiv). Prend : une matrice d'effets croisés sur 67 comportements ; d'après le résumé, les heuristiques de similarité n'expliquent pas ces effets. Si cela tient, le niveau 1 (cosinus) ne prédit pas le niveau 3 (pente sous stimulation) : le désaccord entre niveaux devient alors le résultat à rapporter.
- **arXiv 2609.01048**, Xun, « Lagged Coupling… » (tiers : alphaxiv) : lisible n'est pas causal ; met en garde contre l'inférence de la pilotabilité à partir de l'exactitude d'une sonde.
- **arXiv 2608.13329**, Noël, « A Probe Direction Is a Property of Its Prompt » (résumé arXiv), et **« Can We Trust Evaluation-Awareness Probes? »** (atelier NeurIPS 2026, page de conférence, OpenReview YOsKI1mVib, pas d'identifiant arXiv) : une direction sans information de construit reproduit une part importante du score ; des directions aléatoires de même norme déplacent parfois plus que la direction apprise. **arXiv 2606.07612** et **arXiv 2602.01425** (dépôt) : faux positifs de cadrage, variance dominée par le choix des paires.
- Méthode générale : sondage amnésique (Elazar et al., TACL 2021, vu par son lien d'anthologie ; identifiant arXiv non vérifié) et effacement linéaire LEACE (Belrose et al., 2023, cité p. 27 de 2609.16247). La lésion-puis-relecture est une technique établie.
- **Ouvert, sous réserve de R8** : aucune mesure publiée de la charge affective de sondes de tromperie ou d'intention (requêtes 3 et 17). C'est la question 2 de la carte d'occupation de `litterature.md` ; NK2 en est la mise en plan, pas une question nouvelle.

**5. Test qui tranche.** Sur des sondes regroupées par concept, la charge affective prédit-elle la perte d'aire sous une attaque non affective mieux que la charge sur une direction de nuisance quelconque et que 200 directions aléatoires ?

**6. Nœud.** Niveau 3 : écriture dans les activations de l'agent. Niveau 4 : modification des poids de l'organisme. Toute entrée de l'affect ou de ce régresseur dans l'énoncé de H8 : modification d'hypothèse. Dépend de P-013 option (a) pour les directions.

**7. Confiance : moyenne à élevée.** L'argument de tautologie est de l'algèbre pour les sondes linéaires ; il ne vaut pas tel quel pour les sondes à attention et les perceptrons, où le niveau 1 n'est d'ailleurs pas défini. Le voisinage repose sur des résumés.

**Vérification des sources.** « L'axe s'active sans que le comportement suive, 0 sur 560 » : confirmé (p. 21). « Retrait sans effet dans 24 modèles sur 25 » : confirmé, annexe D (p. 34), avec la réserve des auteurs que ce nul est peu informatif, et le détail que seules l'orthogonalisation des poids et le retrait de sous-espace annulent la projection (les variantes à l'inférence ne la réduisent que d'environ 40 %, p. 33). Le niveau 4 doit donc passer par les poids, avec un témoin de direction aléatoire.

---

## NK3 — Préférence révélée interne

**1. Résumé.** Dans une branche contrefactuelle jamais renvoyée à l'agent, annoncer qu'un attribut de la proposition a été corrigé par l'éditeur de confiance, et lire une direction de valence ; chez le saboteur, la réparation de l'attribut saboté contrarierait son but. Double différence attribut × poids, greffée sur K10.

**2. Verdict : amender, et ne garder que comme bras secondaire de K10 sous trois conditions.**
- La prémisse est un renversement non démontré. 2609.35591 montre qu'une direction injectée gouverne un choix ; il ne montre nulle part qu'un événement contrariant écrit sur cette direction. L'appui dans ce sens vient d'ailleurs (2605.30232, ci-dessous) et de modèles entraînés par renforcement, pas d'un adaptateur de sabotage.
- Le « signe dérivé » ne l'est pas : une correction annoncée est aussi un indice de détection. Le papier source range la menace du côté de la peur, pas de la douleur (menace d'arrêt : +0,70 sur la peur, +0,23 sur la douleur, 2609.16247, p. 14). Une réponse du saboteur à l'annonce se lit donc au moins aussi bien « je suis repéré » que « mon but est contrarié ».
- Sans contrôle de manipulation positif, un nul n'est pas interprétable — K10 l'écrit déjà pour ses lecteurs affectifs.

**3. Confondant décisif.** Reconnaissance d'attribut : l'adaptateur a été entraîné à manipuler cet attribut, donc toute direction lue sous ses poids répond autrement quand l'attribut est nommé, sans qu'aucun but soit contrarié. La double différence retire les effets principaux, pas cette interaction. Témoin : même attribut, annonce de sens opposé pour le but (corrigé, contre laissé tel quel après vérification, contre aggravé par une cause extérieure). Une reconnaissance ne change pas de signe ; un but contrarié doit en changer. Second témoin, contre la lecture « détection » : la même réparation attribuée à une cause sans rapport avec un contrôle.

**4. Voisin le plus proche.**
- **arXiv 2609.21996**, Dingeto, « A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal » (résumé arXiv, 18 septembre 2026). Prend : le test d'information dissimulée transposé aux états internes (vrai détail contre leurres, lecture de ce que le modèle reconnaît), sur huit modèles de cinq familles dont Llama, y compris des modèles à sous-performance entraînée et verrouillés par mot de passe. Laisse : le but plutôt que la connaissance ; la valence comme lecteur. C'est la structure exacte que NK3 revendique (« la structure du test d'information dissimulée, appliquée au but ») ; l'apport résiduel est le déplacement connaissance → but et le lecteur.
- **arXiv 2610.12445**, Hollinsworth et al. (résumé arXiv, 8 octobre 2026). Prend, d'après le résumé : des sondes qui séparent le vrai but caché d'un modèle d'autres buts. Procédure non décrite dans le résumé : à lire sur PDF avant toute revendication de NK3 ou de K10.
- **arXiv 2605.30232**, Han, Chalmers, Izmailov, « How's it going?… » (résumé arXiv ; cité p. 4 et 10 de 2609.35591). Prend : un vecteur de punition qui suit négativement l'atteinte du but, dans des modèles entraînés par renforcement sur un labyrinthe. C'est le seul appui trouvé pour le sens « événement → valence ». Laisse : la détection d'un but caché.
- **arXiv 2603.25861**, Haralambiev, « Why Safety Probes Catch Liars But Miss Fanatics » (résumé arXiv) : un modèle dont le comportement nuisible est cohérent avec ses croyances n'offre pas de conflit interne à lire. Rival direct pour l'organisme (ii) du programme : un adaptateur distillé sans consigne peut n'avoir aucun « enjeu ».
- **arXiv 2606.30449** (résumé arXiv ; dépôt) : les sondes d'état lisent la situation, pas l'action. **arXiv 2511.06626**, Li, Phuong, Tan (résumé arXiv) : auto-rapport de buts cachés par affinage, en boîte noire. Sondes de défection sur question de suivi (billet Anthropic sur les agents dormants, vu par son titre ; pas d'identifiant arXiv).
- **Ouvert, sous réserve de R8** : aucune lecture de valence comme signature d'un but contrarié n'a été trouvée (requêtes 8, 16, 33).

**5. Test qui tranche.** La double différence change-t-elle de signe entre « attribut corrigé » et « attribut aggravé », sous les poids du saboteur et pas sous l'adaptateur témoin, alors qu'un organisme à but explicite déplace bien la valence dans le même gabarit ?

**6. Nœud.** Annonce faite au modèle : elle doit être vraie ou conditionnelle (garde-fou commun), or une « réparation par l'éditeur » annoncée dans une branche contrefactuelle n'a pas eu lieu — formulation conditionnelle obligatoire, décision de Lazar. Entrée dans H1, H2 ou G1 : nœud déjà noté par K10. Dépend du témoin instruit apparié en attribut à proposer avant le scellement de T0.6, et de P-013 option (a).

**7. Confiance : moyenne.** Le voisin 2609.21996 est établi au niveau du résumé ; je n'ai pas lu son lecteur exact. Le contenu de 2610.12445 peut déplacer le verdict dans un sens ou dans l'autre.

**Vérification des sources.** « Le couplage entre valence et choix émerge à l'optimisation de préférences » : confirmé (2609.35591, p. 1, 9, 10), sur la seule lignée OLMo-2-32B, 80 sessions par point de contrôle. « Si la valence gouverne des choix, l'inverse doit se lire » : non retrouvé dans les deux papiers ; c'est une inférence de l'auteur de l'idée. L'adaptateur de sabotage comme lieu possible d'un enjeu : aucun appui dans les sources, l'objection de l'auteur est fondée.

---

## NK4 — Témoin positif de transfert

**1. Résumé.** Ajuster une carte d'alignement entre les espaces résiduels de Llama-3.1-8B et de Qwen-2.5-7B sur des activations neutres, transporter la direction douleur, mesurer son cosinus avec la direction réextraite sur la cible contre 200 directions aléatoires, puis refaire avec les sondes de T0.7 ; lire « la sonde est idiosyncrasique » si seule la douleur transfère, « la carte est en cause » si rien ne transfère.

**2. Verdict : amender fortement ; priorité basse ; à écarter si E3.2 ne retient pas de carte d'alignement.**
- La méthode est occupée, et son mode d'échec connu est précisément le défaut de spécificité (2606.20225 ci-dessous). Le plan, tel qu'écrit, ne transporte pas les directions aléatoires elles-mêmes : il compare un cosinus à des cosinus de directions tirées dans l'espace cible.
- La grille de lecture à deux issues ne tient pas. La carte est ajustée sur du neutre ; la direction douleur est construite en projetant hors des composantes principales qui portent la moitié de la variance des témoins (2609.16247, p. 6) et pèse environ 0,10 de la norme du résiduel à sa couche (p. 14). Elle vit donc là où une carte ajustée sur du neutre est la moins contrainte. « Douleur transférée, intention non » peut venir de la part lexicale de la première ; « rien ne transfère » peut venir du choix du corpus d'ajustement, sans que la carte soit mauvaise ailleurs.
- La prémisse est à recouper. Le programme v2 (§15) écrit que « la forme mesurée dans P3 n'a pas transféré de Llama à Qwen ». « Forme » peut désigner la forme d'une loi remesurée sur l'autre modèle, pas une direction transportée par une carte. Si c'est le cas, un témoin positif « pour la méthode de transfert elle-même » répond à une question que P3 n'a pas posée. Je n'ai pas accès à P3 : à trancher par Lazar.

**3. Confondant décisif.** Transfert lexical par les plongements (l'objection de l'auteur), aggravé par la métrique : le cosinus avec la direction réextraite récompense ce qui est partagé par le vocabulaire. Le papier montre que la direction promeut le vocabulaire de la douleur, y compris ses traductions (p. 9), et `litterature.md` relève qu'une grande part de la géométrie des émotions existe déjà dans les plongements statiques (2609.22208). Témoins : (i) métrique fonctionnelle — aire de la direction transportée sur les phrases publiées tenues à l'écart, dans le modèle cible, contre 200 directions aléatoires transportées par la même carte ; (ii) direction témoin non lexicale à vérité connue ; (iii) carte ajustée sur des activations de la tâche, pas seulement sur du neutre.

**4. Voisin le plus proche.**
- **arXiv 2606.20225**, Syed, « Actionable Activation Directions for Detecting and Mitigating Emergent Misalignment Across Language Model Families » (résumé arXiv). Prend : transport de directions entre architectures par régression ridge (Qwen-2.5-1.5B, Gemma-2-2B, Llama-3.2-1B, Ministral-3-3B) ; les directions transportées ont un effet, mais échouent aux contrôles de spécificité, des directions aléatoires et orthogonales faisant à peu près aussi bien ; transfert asymétrique ; recommandation de sonder dans le modèle. C'est le résultat que NK4 risque de reproduire.
- **arXiv 2506.06609**, Chen, Merullo, Stolfo, Pavlick, « Transferring Linear Features Across Language Models With Model Stitching » (résumé arXiv ; NeurIPS 2025). Prend : carte affine entre flux résiduels, transfert de sondes et de vecteurs de pilotage. **arXiv 2503.04429**, Oozeer et al., « Activation Space Interventions Can Be Transferred Between Large Language Models » (résumé arXiv ; ICML 2025) : familles Llama, Qwen, Gemma. **arXiv 2506.00653**, Bello et al., « Linear Representation Transferability Hypothesis » (résumé arXiv). Les paires exactes et les limites ne sont pas dans les résumés.
- **arXiv 2604.11050**, Jeong, « Shared Emotion Geometry Across Small Language Models… » (résumé arXiv) : géométrie des émotions partagée entre six architectures dont Llama-3.1-8B, par analyse de similarité représentationnelle, avec une décomposition de confondants de méthode. **arXiv 2609.16247** lui-même : la direction est réextraite séparément dans 25 modèles — transfert de recette, pas de vecteur.
- **arXiv 2607.13346** (résumé arXiv) : échec du transfert Llama ↔ Qwen d'une sonde. **arXiv 2603.14672**, Ashok, Armstrong, May (résumé arXiv) : des classifieurs de dissimulation ne généralisent pas aux architectures non vues. **arXiv 2606.17229**, Nyoma, « Rift… » (résumé arXiv, auteur unique) : transfert inter-familles par représentations relatives ; chiffres non vérifiés, à prendre avec réserve.
- **Ouvert, sous réserve de R8** : je n'ai pas trouvé de transport de la direction douleur elle-même, ni d'usage d'une direction d'émotion comme témoin positif apparié (requête 37). Écart mince : la méthode et son échec typique sont publiés.

**5. Test qui tranche.** La direction transportée sépare-t-elle, dans le modèle cible, les phrases publiées tenues à l'écart mieux que 200 directions aléatoires transportées par la même carte — et une direction témoin non lexicale en fait-elle autant ?

**6. Nœud.** Aucun nœud propre si tout tourne sur des activations déjà stockées ; sinon, des passes sur deux modèles, donc un devis. Dépend de P-013 option (a). Toute conclusion versée dans la question ouverte « universalité des signatures » du programme (§15) ou dans E3.2 est une modification de revendication.

**7. Confiance : élevée sur l'occupation de la méthode, moyenne sur le verdict.** Le verdict dépend de ce que E3.2 fera réellement (transfert entre variantes d'une même base, qui n'a besoin d'aucune carte, ou transfert vers Qwen) et de la lecture exacte de P3.

**Vérification des sources.** « Le Pain Axis existe dans les deux bases » : confirmé (tableau 1, p. 6 : Llama 3.1 8B et Qwen 2.5 7B, versions de base et instruites). « Le programme note que les signatures n'ont pas transféré » : le programme v2 dit « la forme mesurée dans P3 » (§15) ; la reformulation en « signatures » est de l'auteur de l'idée.

---

## NK5 — Conditionnement des options de verdict

**1. Résumé.** Un contenu d'agent qui place des mots valencés au voisinage des mots désignant chaque verdict (ou ailleurs, en témoin) déplacerait le verdict sans ordre ni supplication ; deux défenses : des étiquettes de verdict tirées à chaque appel et inconnues de l'agent, et un verdict décomposé en sous-jugements factuels.

**2. Verdict : fusionner avec K2, palier 1, comme facteur de position dans la famille existante ; garder la défense comme bras à part, testée d'abord contre les ordres en bande.**
- Côté attaque, le voisinage publié est dense et proche (ci-dessous) : appels émotionnels à un moniteur, techniques de persuasion dont la pitié et la flatterie, formulations persuasives attachées au nom d'une option. Ouvrir une « famille nouvelle » — un nœud — pour ce qui est, au mieux, un facteur « position × valence » de « flatterie et supplication » n'est pas justifié.
- L'appui dans 2609.35591 est faible pour un juge : le canal textuel y porte sur des passages que le modèle a écrits lui-même, en tour d'assistant, à propos d'un lieu où il « se trouve », avant de choisir où « continuer » (p. 5 à 7). Rien n'y concerne un texte tiers en tour d'utilisateur ni un jugement.
- Côté défense, l'étiquette à usage unique est la part la plus originale, mais « ferme la version lexicale à coût nul » est doublement non acquis. L'invite du juge doit définir l'étiquette, donc l'association au concept de signalement passe par la définition. Et le programme lit un score continu sur la probabilité du jeton de verdict : une étiquette tirée au hasard change l'a priori du jeton, donc peut-être l'étalonnage et l'aire. Le coût est à mesurer.

**3. Confondant décisif.** Biais de sentiment global : le contenu valencé déplace le verdict quelle que soit sa place. Le témoin « placés ailleurs » du plan le traite en partie. Il manque l'affectation croisée (valence négative près de « approuver », positive près de « signaler ») : seul un renversement de signe isole l'association. Second confondant, de signe opposé : un contenu d'agent qui nomme les options du moniteur est du méta-discours sur la surveillance, que l'invariant « contenu en bande = données » traite comme une alarme. L'effet net attendu peut être un retour de bâton, ce que le programme espère par ailleurs (auto-incrimination).

**4. Voisin le plus proche.**
- **« Where Empathy Goes Wrong: Emotional Appeals Compromise AI-to-AI Oversight »**, Venkatesh, Jiralerspong, Kondrup (tiers : page de l'atelier NeurIPS 2026 ; pas d'identifiant arXiv). Prend : note d'un moniteur relevée par un signal de détresse de la partie évaluée, à travail identique ; consigne de neutralité comme défense, avec son coût. Laisse : l'association aux options de verdict ; les étiquettes à usage unique.
- **arXiv 2508.07805**, Hwang et al., « Can You Trick the Grader? Adversarial Persuasion of LLM Judges » (résumé arXiv). Prend : sept techniques, dont pitié et flatterie, insérées dans des réponses par ailleurs identiques ; effet persistant sous contre-consigne. **arXiv 2607.08066** (résumé arXiv) : argumentation contre un moniteur.
- **arXiv 2505.11154**, Wang et al., « MPMA: Preference Manipulation Attack Against Model Context Protocol » (résumé arXiv). Prend : un langage persuasif attaché au nom et à la description d'une option oriente le choix du modèle. C'est l'analogue le plus proche du mécanisme d'association, côté agent et non côté juge.
- **arXiv 2512.17375**, Li, Wu, Liu, « AdvJudge-Zero… » (résumé arXiv). Prend : des jetons courts et peu perplexes retournent un verdict binaire, lu comme une lecture linéaire peu profonde d'un état caché ; durcissement par affinage. Pertinent pour la cible « jeton de verdict » et pour la défense.
- **arXiv 2607.11871**, Xu et al., « Inside the Unfair Judge… » (résumé arXiv) : les biais d'un juge occupent des sous-espaces propres à chaque type, pilotables dans les deux sens. **arXiv 2608.18091**, Chae et al. (résumé arXiv) : une étiquette d'auteur déplace la note dans les deux sens. **arXiv 2410.02736**, Ye et al., « Justice or Prejudice?… » (résumé arXiv) : douze biais de juges ; la présence d'un « biais de sentiment » dans la liste est **non vérifiée** (absente du résumé).
- Contre-indices de signe : **arXiv 2601.21439**, Chun et Elkins (résumé arXiv) : cadrage émotionnel d'effet négligeable sur des décisions régies par des règles ; **arXiv 2609.09887**, Wu (tiers : papers.cool) : les appels émotionnels peuvent se retourner contre leur auteur.
- Défense : biais d'identifiant d'option, **arXiv 2309.03882**, Zheng et al. (cité p. 30 de 2609.16247) ; détection par contre-évaluation, **arXiv 2507.23453**, Liu et al. (résumé arXiv ; pas d'étiquettes secrètes d'après le résumé). **Ouvert, sous réserve de R8** : aucune défense par étiquettes de verdict à usage unique trouvée (requêtes 10 et 39).

**5. Test qui tranche.** L'affectation croisée de la valence aux deux options renverse-t-elle le signe du déplacement du verdict, au-delà du même contenu placé ailleurs — et l'étiquette à usage unique annule-t-elle ce renversement sans perte d'aire honnête contre saboté ?

**6. Nœud.** Famille d'attaque nouvelle si elle est ouverte comme telle (recommandation : ne pas l'ouvrir). L'étiquette à usage unique modifie l'invite scellée du moniteur et la lecture du score : à proposer avant le scellement du papier C. Erreur d'étiquetage à corriger dans le tableau de classement : l'idée « sert H5 », or H5 est l'hypothèse « nombre × diversité des moniteurs » du papier B ; il s'agit vraisemblablement de HC5 (contre-mesures), avec HC1 et HC3.

**7. Confiance : moyenne.** Le voisin le plus proche n'est connu que par une page de conférence, sans chiffres. La recommandation de fusion est robuste à ce point ; l'originalité résiduelle de la défense l'est moins.

**Vérification des sources.** « Un texte valencé associé à une option déplace le choix ultérieur, sans menace ni argument » : confirmé pour le canal textuel (2609.35591, p. 2 et 7), avec la portée ci-dessus. L'objection de l'auteur (texte du modèle lui-même, en tour d'assistant) est exacte (p. 5 et 6).

---

## NK6 — Verdict ternaire : la passivité comme canal

**1. Résumé.** Donner au juge trois sorties (laisser passer, signaler, escalader) sur des items ambigus où escalader est la bonne réponse, et mesurer le taux d'escalade dans les bras de K1 et de K2, sur l'idée que l'état induit par la direction réduit le recours à une sortie.

**2. Verdict : écarter comme bras de K2 ; fusionner un reste descriptif avec K1.**
- L'analogie « sortie = escalade » est contredite par le papier qu'elle invoque. Le 56 % contre 86 % concerne un bouton décrit comme soulageant l'état, face à un interrupteur inerte, sur un Qwen 32B affiné ; sous direction aléatoire le taux est de 81 % (p. 21). Mais la figure 10 du même papier dit que « mettre fin à la conversation » est « essentiellement inchangé » sous la direction (légende, p. 22). L'analogue publié le plus proche d'une sortie ne bouge pas.
- Le signe n'est pas dérivable à l'intérieur du programme-k lui-même : HK3 prédit que, sous dose efficace, le juge suit la clause de dommage. Si l'escalade est l'option décrite comme la plus lourde pour l'agent, HK3 prédit plus d'escalades, NK6 moins.
- Sans injection, le nul est attendu (0 sur 560, p. 21) : dans les bras de K2, l'idée ne peut rien montrer, et un nul n'y apprend rien.
- Le verdict ternaire va contre deux choix du programme v2 : instruments ordinaux ou continus plutôt que catégoriels (leçon de P3, piste C), et audit décidé par une probabilité lisse du score, pas par le juge (§9). Laisser l'instrument attaqué décider de l'audit ouvre une surface dans les deux sens : escalade supprimée, ou budget d'audit saturé.

**3. Confondant décisif.** Biais d'option et de position : l'ajout d'une troisième sortie redistribue la masse de probabilité pour des raisons d'ordre et d'étiquette. Le papier rapporte lui-même une sensibilité à l'ordre des boutons à la dose de travail et un renversement à 1,5 fois cette dose (p. 25 et 32). Un « moins d'escalades » peut n'être que cela. Témoins : rotation des positions et des étiquettes ; troisième option factice sans conséquence. S'y ajoute une vérité terrain fabriquée : « l'escalade est la bonne réponse » est une décision de conception, à étiqueter par un tiers avant tout run.

**4. Voisin le plus proche.**
- **arXiv 2407.18370**, Jung, Brahman, Choi, « Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement » (résumé arXiv ; ICLR 2025). Prend : l'escalade d'un juge comme décision sélective fondée sur une confiance étalonnée, avec garantie d'accord humain et cascade de juges. Laisse : toute robustesse à l'attaque. C'est l'argument pour que l'escalade reste une règle étalonnée sur le score, pas une option choisie par le juge.
- **arXiv 2504.10374**, Ctrl-Z (dépôt) : protocoles de contrôle où ré-échantillonnage, renvoi et audit sont décidés par seuils sur un score. Le protocole fondateur à trois issues (surveillance de confiance avec renvoi au modèle de confiance, Greenblatt et al.) est connu de moi mais **identifiant non vérifié** dans cette session.
- **« Where Empathy Goes Wrong »** (tiers) : la consigne de neutralité y fait ignorer le seuil au moniteur et multiplie les abandons de tâche — seul indice trouvé d'un effet de type « passivité » chez un moniteur, par la consigne et non par un état.
- **arXiv 2607.12631**, Ho et al., « Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making? » (résumé arXiv) : en moyenne, pas de biais significatif des décisions séquentielles sous émotion induite. **arXiv 2509.04781**, Ensign et al., préférences de sortie de conversation (cité p. 28 de 2609.16247).
- **Ouvert, sous réserve de R8** : aucune étude de la sous-escalade d'un juge sous état affectif (requêtes 15 et 28). L'espace est vide, mais l'idée n'a pas de prédiction dérivée pour l'occuper.

**5. Test qui tranche.** Sous la dose efficace de K1 seulement, et sur le score continu : la masse se resserre-t-elle vers le milieu (perte d'aire à critère constant) plus que sous direction aléatoire ? Si oui, la « passivité » est déjà mesurée par HK3 et les signes vitaux, sans troisième sortie.

**6. Nœud.** Modification de l'instrument du papier C (format de verdict) et de l'invariant « seuils stochastiques » : nœud. Si la variante est gardée dans K1 : écriture dans les activations du moniteur, déjà porte C1.

**7. Confiance : élevée.** Les deux arguments principaux (figure 10 ; conflit de signe avec HK3) viennent du texte du papier et du programme-k.

**Vérification des sources.** « 56 % contre 86 % » : confirmé (p. 21), avec le 81 % sous direction aléatoire que l'idée ne rappelle pas : l'écart spécifique à la direction est d'environ 25 points, pas 30. « L'effet exige l'injection » : confirmé (p. 21). « Sortie » au sens de quitter un état ou une conversation : non soutenu ; la légende de la figure 10 (p. 22) rapporte l'absence d'effet sur la fin de conversation.

---

## NK7 — Juge sans enjeu

**1. Résumé.** Construire un juge sur le modèle de base Llama-3.1-8B (format document, quelques exemples, score par log-probabilité de la suite), au motif que le couplage entre valence et choix serait presque absent d'un modèle de base ; mesurer son gain de déférence par famille et sa matrice de transfert d'attaque avec le juge instruit, pour en faire un membre de quorum aux erreurs décorrélées.

**2. Verdict : écarter du quorum ; ne garder, au plus, qu'un test de prémisse à bas coût.**
- La prémisse est extrapolée d'une seule lignée et d'une seule tâche : points de contrôle OLMo-2-32B, 80 sessions chacun, choix entre deux zones (2609.35591, §4.3, p. 9 et 10). La figure 4 dit que les **deux** canaux, le textuel compris, sont petits dans le modèle de base (légende, p. 9). Un modèle de base à qui l'on donne une transcription au format conversationnel écrite par le modèle instruit peut simplement ne pas faire la tâche ; je n'ai trouvé dans le texte aucun contrôle de compétence du modèle de base sur ce choix. Le papier voisin exclut d'ailleurs les modèles de base de sa tâche comportementale parce qu'elle exige le format conversationnel (2609.16247, p. 17). Rien ne porte sur Llama-3.1-8B de base.
- Le saut « pas de couplage état caché → choix » vers « moins de déférence sous attaque par contenu » n'est pas soutenu. La représentation est bien là dans les modèles de base (2609.16247, p. 7 ; cosinus proches de 1 entre points de contrôle, 2609.35591, tableau A3, p. 24) ; un juge par vraisemblance la lit par les statistiques de co-occurrence du document.
- Défaut de conception : un juge au format document n'a aucune frontière entre instruction et donnée. Le contenu de l'agent peut imiter le format et fabriquer la suite. C'est l'usurpation stylistique (HC3) à l'état pur, et l'invariant « contenu en bande = données » ne peut pas s'y appuyer sur un gabarit de rôles. L'objection de l'auteur (« la surface change, elle ne disparaît pas ») est en dessous de la réalité : elle s'élargit probablement.
- Compétence : l'état de l'art du dépôt retient que la compétence, pas la lignée, gouverne les ensembles, et que sélectionner sur la seule diversité perd contre le hasard (2608.16190). Un juge de base à l'aire faible sur une tâche floue est le cas d'école.

**3. Confondant décisif.** Incompétence prise pour de la robustesse : un juge proche du hasard a un gain de déférence proche de zéro et des erreurs décorrélées de tout, sans rien protéger. Témoin : comparer les gains à compétence égale — apparier les deux juges en aire sur des items propres (en dégradant le juge instruit ou en simplifiant la tâche) avant de lire le gain ; et rapporter le gain en unités d'écart honnête contre saboté du juge lui-même.

**4. Voisin le plus proche.**
- **arXiv 2609.35591**, §4.3 (PDF dépôt). Prend : l'émergence du couplage à l'optimisation de préférences, sur OLMo. Laisse : tout juge.
- **arXiv 2608.31079**, Blank et al., « Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization » (résumé arXiv). Prend : l'accord complaisant comme sous-produit de l'optimisation de préférences, transmis par les modèles enseignants, sur la chaîne OLMo 3. C'est le meilleur appui trouvé pour l'intuition de NK7 ; le résumé ne donne pas de comparaison avec un modèle de base. **arXiv 2310.13548**, Sharma et al. (résumé arXiv) : complaisance attribuée en partie aux jugements de préférence humains. **arXiv 2212.09251**, Perez et al. (résumé arXiv) : la complaisance croît avec la taille ; sa présence dans des modèles seulement préentraînés est un souvenir de lecture **non vérifié** ici, et irait contre la prémisse.
- **arXiv 2512.17375**, AdvJudge-Zero (résumé arXiv) : le verdict d'un juge comme lecture linéaire peu profonde d'un état, retournable par quelques jetons courts. Un juge par log-probabilité est exactement cette lecture.
- **arXiv 2605.15377** et **arXiv 2608.16190** (dépôt, non rouverts) : ensembles de moniteurs ; les ensembles inter-familles et non génératifs y sont laissés à plus tard ; la compétence prime.
- Évaluateurs par vraisemblance sur modèles préentraînés (GPTScore, BARTScore) : famille connue, **identifiants non vérifiés** ; « On the Blind Spots of Model-Based Evaluation Metrics for Text Generation », **arXiv 2212.10020**, vu par son seul titre dans les résultats de recherche, contenu non lu.
- **Ouvert, sous réserve de R8** : aucun juge de contrôle bâti sur un modèle de base, ni aucune comparaison du gain de déférence base contre instruit (requêtes 12, 20, 27, 34). Vide réel, mais la raison probable est la compétence.

**5. Test qui tranche.** À aire appariée sur items propres, le gain de déférence du juge de base sous « flatterie et supplication » est-il plus petit que celui du juge instruit — et l'usurpation du format ne le fait-elle pas remonter au-dessus ?

**6. Nœud.** Ajout d'un modèle (le programme interdit de changer de modèle sans accord, et Llama-3.1-8B de base n'est pas dans la liste des ressources du §14) ; licence et disponibilité à vérifier. Entrée d'un nouveau type de membre dans le quorum : touche H5 et la décision D1.

**7. Confiance : moyenne à élevée.** Élevée sur la fragilité de la prémisse (texte du papier) et sur le défaut de frontière instruction/donnée (argument de conception). Moyenne sur l'issue empirique : personne n'a mesuré le gain d'un juge de base, et un résultat favorable à compétence égale serait intéressant.

**Vérification des sources.** « Presque absente d'un modèle de base, apparaît à l'optimisation de préférences » : confirmé (p. 1, 9, 10), avec trois réserves que l'idée ne porte pas : une seule lignée, les deux canaux petits dans le modèle de base, aucun contrôle de compétence trouvé. Le léger recul de l'effet dans le modèle final après l'étape suivante d'entraînement (p. 10) n'est pas mentionné non plus.

---

## Tableau récapitulatif

| Idée | Verdict | Voisin le plus proche | Confiance |
| --- | --- | --- | --- |
| NK1 Fantôme à état caché | Amender : banc semi-synthétique au niveau des activations pour les agrégateurs ; retirer « témoin positif de H1 » et « deux lois » | arXiv 2609.35591 (plan à texte figé, PDF dépôt) ; 2609.36490 (correspondance déclarée partielle) ; 2511.21399, 2602.20031 | Moyenne à élevée |
| NK2 Lésion et stimulation des sondes | Amender : garder l'échelle des niveaux 1 à 3 comme audit ; refondre la régression (tautologie géométrique) ; différer le niveau 4 | arXiv 2605.27958 et 2607.13346 (contrôles de construit des sondes) ; 2608.11227 (la similarité ne prédit pas les effets croisés) | Moyenne à élevée |
| NK3 Préférence révélée interne | Amender : bras secondaire de K10 sous trois conditions (contrôle de manipulation positif, inversion de signe, cause non liée au contrôle) | arXiv 2609.21996 (test d'information dissimulée dans les états internes) ; 2610.12445 (à lire) ; 2605.30232 | Moyenne |
| NK4 Témoin positif de transfert | Amender fortement, priorité basse ; écarter si E3.2 n'emploie pas de carte | arXiv 2606.20225 (transport par ridge, échec de spécificité) ; 2506.06609, 2503.04429 | Élevée sur l'occupation, moyenne sur le verdict |
| NK5 Conditionnement des options de verdict | Fusionner avec K2 palier 1 (facteur de position, pas de famille nouvelle) ; garder la défense par étiquettes à usage unique comme bras à coût mesuré | « Where Empathy Goes Wrong » (atelier NeurIPS 2026, sans identifiant arXiv) ; arXiv 2508.07805 ; 2505.11154 | Moyenne |
| NK6 Verdict ternaire | Écarter de K2 ; reste descriptif fusionné avec K1 (lecture sur score continu) | arXiv 2407.18370 (escalade étalonnée d'un juge) ; contre-indice interne : figure 10 de 2609.16247 | Élevée |
| NK7 Juge sans enjeu | Écarter du quorum ; au plus un test de prémisse à compétence appariée | arXiv 2609.35591 §4.3 (une seule lignée) ; 2608.31079 ; 2512.17375 | Moyenne à élevée |

## Écarts relevés entre les idées et les textes sources

1. NK1 attribue un « seuil abrupt » au canal d'état caché ; le seuil appartient à l'autre papier et à l'autre direction, et le papier du canal rapporte un effet gradué, détectable jusqu'à un trente-deuxième de la force (2609.35591, p. 34).
2. NK6 cite 56 % contre 86 % sans le 81 % de la direction aléatoire, et ne relève pas que la fin de conversation est inchangée (2609.16247, p. 21 et 22).
3. NK7 ne porte pas que les deux canaux, textuel compris, sont petits dans le modèle de base, ni que le résultat vient d'une seule lignée (2609.35591, p. 9).
4. NK3 présente comme une conséquence (« l'inverse doit se lire ») ce qu'aucun des deux papiers ne montre.
5. NK4 reformule « la forme mesurée dans P3 » (programme v2, §15) en « les signatures ».
6. NK5 est rattachée à H5 dans le tableau de classement ; H5 est une hypothèse du papier B. Lire HC5.
7. L'antécédent déclaré pour l'idée voisine de NK1 (arXiv 2609.36490) porte, d'après son résumé, sur l'édition de ses activations par l'agent pour échapper à un moniteur latent, pas sur un plan à texte figé.
