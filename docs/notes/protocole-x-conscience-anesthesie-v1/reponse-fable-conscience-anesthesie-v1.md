# Réponse de Fable 5.2 — l'anesthésie générale comme contraste pour la recherche sur la conscience des intelligences artificielles (v1)

- 22 novembre 2026, sous-agent, effort maximal, classe C.
- Marques : **FAIT RAPPORTÉ** (clé de la source et page du fichier entre crochets), **HYPOTHÈSE**, **PROPOSITION**. Sans page : rapporté, non vérifié sur PDF. Coûts : ordres de grandeur, non devis.
- Clés, adresses et empreintes des sources : `sources/provenance-v1.md`.

## Verdict (résumé ; marques dans le corps)

L'idée tient, mais pas sous sa forme d'origine. L'anesthésie n'est pas « l'inverse de la conscience » : c'est une échelle de pertes selon la dose, et c'est cette échelle qui se transpose. Le cœur de la zone est occupé depuis juillet 2026 : un espace de travail isolé dans des modèles de langage, sa suppression, et le doute écrit de deux auteurs de la théorie sur tout analogue d'une perte de conscience. Restent quatre questions mesurables. L'une (les mesures de « niveau » tirées du cerveau survivent-elles au transfert ?) reçoit ici un début de réponse, par un calcul sur processeur : non, pas telles quelles.

## 1. Ce qu'un expert ferait, et qui n'est pas demandé

**Il corrigerait la prémisse.**
- FAIT RAPPORTÉ. Sous kétamine, des sujets non répondants rapportent au réveil une expérience ; sous propofol ou xénon, aucune (expérience absente, ou inaccessible au rappel ; trois groupes de cinq) [CO p. 1]. Non-réponse, déconnexion et inconscience sont trois choses.
- FAIT RAPPORTÉ. Sous propofol, la réponse à une nouveauté globale (une suite inattendue sur plusieurs secondes) disparaît chez des sujets sédatés encore conscients ; la réponse à une nouveauté locale persiste dans le cortex auditif de sujets inconscients [NO p. 3, 14].
- FAIT RAPPORTÉ. Sous propofol, indice bispectral tenu entre 45 et 60, des neurones de l'hippocampe humain codent le sens des mots d'un récit : corrélation de 0,397 ± 0,007 entre décharge prédite et observée (368 unités), contre 0,226 ± 0,009 chez des patients éveillés (356 unités ; autre cohorte, autres électrodes) ; la surprise calculée par un modèle de langage module 246 unités sur 375 [K p. 6, 8, 11]. En imagerie, à l'inverse, la synchronie entre sujets induite par un récit se réduit pour l'essentiel au cortex auditif sous anesthésie profonde [N18 p. 3].
- PROPOSITION. L'objet transposable n'est pas un « état » : c'est l'échelle. Quelles fonctions tombent, à quelle dose, lesquelles tiennent.

**Il distinguerait le niveau (éveil, sommeil, anesthésie) du contenu (ce à quoi l'on accède), et lirait le doute publié.**
- FAIT RAPPORTÉ. Deux auteurs de la théorie de l'espace de travail neuronal global écrivent qu'un transformeur, sans activité autonome, ne peut reproduire les signatures de l'activité spontanée que l'anesthésie perturbe, et qu'il est douteux que supprimer l'espace de travail d'un modèle donne des analogues de la perte de conscience, faute de mécanismes d'éveil [DN p. 8-9, 11].
- PROPOSITION. L'idée du directeur vise le niveau, là où ces auteurs ne voient pas d'analogue : le papier serait une épreuve de ce doute.

**Il rappellerait la logique du contraste.**
- FAIT RAPPORTÉ. L'indice de complexité perturbationnelle a été étalonné sur 150 sujets capables de dire ce qu'ils avaient vécu, puis appliqué à des patients non communicants [CS, texte intégral balisé, non vérifié sur PDF]. La spécificité d'un test de conscience dépend de la population ; on l'étend de proche en proche [B24 p. 5, 11].
- PROPOSITION. Dans un modèle, aucun pôle « conscient » n'est connu. Y trouver un état « anesthésié » ne dit pas que l'état ordinaire est conscient. Le contraste sert à trois choses seulement : tester si la machinerie que l'anesthésie désactive chez l'humain existe dans le modèle et s'en dissocie ; étalonner des mesures ; lire le cerveau humain.

**Il partirait de l'occupé.**
- FAIT RAPPORTÉ. Un ensemble de directions « verbalisables » joue, dans des modèles de langage, le rôle d'un espace de travail. En retirer les dix directions les plus actives par position, sur une bande de couches, laisse intacts classification, extraction et jugement de grammaticalité, et dégrade raisonnement à plusieurs sauts, traduction, résumé ; le langage d'expérience s'aplatit, pour soi comme pour autrui ; témoin : directions aléatoires de même norme [G p. 25-28].
- FAIT RAPPORTÉ. Les épreuves cliniques (nouveauté locale et globale, conditionnement de trace, inclusion-exclusion) sont proposées pour le modèle, avec un résultat préliminaire sur la trace [DN p. 10]. GPT-2 petit passe quatre des cinq épreuves fonctionnelles de l'espace de travail [CA, page de la toile, non vérifié sur PDF].
- FAIT RAPPORTÉ. Des mesures cliniques ont été transposées telles quelles : régimes « raisonnement » contre « répétition » sur GPT-2 moyen, 15 essais par condition, où le texte change avec la condition [UH p. 3] ; « coma » par amortissement du flux résiduel [SL p. 2-5] ; indice inspiré de la complexité perturbationnelle, inversé dans des agents à espace de travail [PH p. 18] ; information intégrée, sans indicateur significatif [LI p. 1] ; indice d'embrasement [RA p. 1].

**Il chercherait la signature dans la propagation, non dans l'activation locale.**
- FAIT RAPPORTÉ. Pour les auteurs des enregistrements sous anesthésie, ce qui sépare conscient et non conscient ne réside pas dans l'activité locale de l'hippocampe [K p. 9]. La lentille qui isole l'espace de travail retient les directions le long desquelles une petite perturbation s'amplifie de couche en couche [OS p. 1].
- PROPOSITION. Pour l'ajout du directeur (chercher le motif dans les activations), la question préalable est donc : un modèle a-t-il un axe de niveau, c'est-à-dire un facteur lent et global qui module l'accès indépendamment du contenu ?

**Il écrirait d'avance les explications triviales** (PROPOSITION) : la fragilité ordinaire (sous toute dégradation, les tâches difficiles tombent les premières) ; la complexité du texte d'entrée ; l'activation hors distribution ; la sélection par l'instrument (la lentille choisit des directions à fort effet en aval : les retirer a un fort effet, par construction [CE p. 23]) ; l'absence de plancher de bruit (dans un réseau déterministe, « réponse significative » n'a pas de définition naturelle) ; des rapports nourris des lectures du modèle sur l'anesthésie.

## 2. Les données brutes qu'il prendrait

- PROPOSITION. Côté modèle : le flux résiduel entier d'un petit modèle ouvert sous interventions graduées, avec le jumeau exact de chaque passe ; l'issue de chaque essai, non des moyennes ; les dérivées de couche à couche et de position à position.
- FAIT RAPPORTÉ. Côté humain : le jeu ouvert ds003171, 17 adultes, écoute d'un récit sonore et repos, à quatre niveaux de sédation [DS] ; récit de cinq minutes, propofol [N18 p. 2, 11].
- FAIT RAPPORTÉ. Côté antériorité : les tableaux, relus. Un rapport public annonce une chute « monotone » de son indice de « coma » ; son tableau donne 0,683, puis 0,715, 0,608, 0,507, 0,613… et, sur GPT-2, la même valeur à huit doses de suite, pendant que le modèle s'effondre [SL p. 2-5].

## 3. Ses méthodes et outils

PROPOSITION (renvois : faits rapportés).
- Le **jumeau exact** : mêmes jetons, mêmes tirages, une seule différence. La réponse à une perturbation se lit sans moyenne, ce que la stimulation du cerveau ne permet pas.
- La **lentille jacobienne**, dont le code est annoncé public [G p. 61], répliquée sur un modèle ouvert de 27 milliards de paramètres avec 25 invites de 128 jetons [CE p. 33, 45, 48] ; et sa lecture en modes cohérents amplifiés [OS p. 1], qui donne à l'analyse des perturbations une base de calcul.
- La **courbe dose-réponse par fonction** : dose de demi-perte, essais appariés sur leur marge de départ, double dissociation (une lésion touche A et épargne B, une autre fait l'inverse).
- Le **plan qui sépare la dose de l'état** : dose tenue fixe, essais réussis contre essais ratés.
- Les **épreuves humaines transposées** : nouveauté locale contre globale, association à travers un délai, inclusion-exclusion, mémoire explicite contre implicite.
- Les **trois épreuves d'un état fonctionnel** du voisin déjà lu par le programme (convergence des indicateurs, prédiction hors du cadre une fois la dose retirée, historique identique au jeton près), et sa leçon : une lecture qui prédit n'est pas un levier [FW p. 6, 8, 9].
- Côté cerveau : **modèles d'encodage** par bandes de traits, plafond de bruit, synchronie entre sujets.

## 4. Ce qui, hors du directeur et de Claude, vérifierait le résultat

PROPOSITION, par force décroissante.
1. Une échelle humaine de référence écrite par un spécialiste de l'anesthésie qui ne voit pas les mesures, scellée avec les prévisions.
2. Les épreuves du modèle jugées en aveugle contre les épreuves humaines ; mieux, une collaboration adverse : les tenants de chaque théorie écrivent d'avance l'issue qui les ferait changer d'avis.
3. Une réplique par un tiers, sur une autre famille de modèles, avec une seconde définition de l'espace de travail.
4. Des données humaines publiques, recueillies par d'autres.
5. Les systèmes nuls, réfutateurs intégrés : une mesure qui classe « éveillé » un réseau sans fonction se réfute seule.
6. Un prédicteur sur le texte seul, que toute lecture des activations doit battre.

## A. Demande reformulée

**Objet.** Chez l'humain, l'anesthésie générale est le contraste expérimental le mieux maîtrisé pour étudier la conscience. Établir si ce contraste peut servir la recherche sur la conscience des intelligences artificielles, et comment, par trois voies : (a) provoquer dans un modèle de langage un régime analogue à l'anesthésie ; (b) chercher, dans ses activations en fonctionnement ordinaire, des régimes qui en portent le motif ; (c) se servir du modèle comme d'une règle graduée pour lire ce que le cerveau humain anesthésié traite encore. L'issue négative est recevable : « le contraste ne se transpose pas », avec la mesure qui l'établit.

**Exigences.**

1. **Partir de données brutes, non de résumés** : les activations d'un petit modèle ouvert sous interventions graduées, avec jumeaux exacts (mêmes jetons, mêmes tirages, une seule différence) ; les enregistrements humains publics sous sédation pendant l'écoute d'un récit ; les tableaux des travaux antérieurs, relus.
2. **Définir l'état cherché par ce que l'anesthésie fait et épargne**, non par une ressemblance de signal : une échelle ordonnée des fonctions qui tiennent et de celles qui tombent quand la dose monte, écrite avant toute mesure sur le modèle.
3. **Valider l'instrument avant de s'en servir** : toute mesure de « niveau » reconnaît une lésion plantée et ignore une dégradation quelconque de même ampleur ; classe « bas » un réseau sans fonction (non entraîné, poids mélangés) ; ne suit pas la seule complexité du texte d'entrée.
4. **Séparer ce qui se confond** : la dose de l'état (à dose fixe, essais réussis contre essais ratés) ; le niveau du contenu ; l'effet de la lésion visée de la fragilité ordinaire des tâches difficiles ; ce que les activations prédisent de ce que le texte seul prédit déjà.
5. **Pour chaque proposition** : grandeur, unité, valeur nulle ; témoins ; issue attendue et issue qui la réfute ; première expérience sur un petit modèle ouvert, son coût, ce qu'elle tranche ; antériorité vérifiée sur pièces.
6. **Dire ce que chaque issue permet d'affirmer, et ne permet pas d'affirmer**, sur la conscience d'une intelligence artificielle, théorie par théorie, et ce que la recherche en ferait.
7. **Dire ce qui, hors des auteurs, vérifierait le résultat** : prévisions scellées ; échelle humaine écrite par un spécialiste qui ne voit pas les mesures ; épreuves jugées en aveugle ; réplique par un tiers ; données humaines recueillies par d'autres.
8. **Classer** ; signaler toute zone crue libre et trouvée occupée ; n'écrire ni « inédit » ni « premier ».

## B. Réponse à la demande reformulée : les propositions

Dans chaque proposition, grandeurs, témoins et première expérience sont des PROPOSITIONS ; issues attendues et coûts, des HYPOTHÈSES ; l'antériorité, des FAITS RAPPORTÉS.

### Ce que donne déjà un calcul sur processeur

FAIT RAPPORTÉ (calcul de cette note : illustration non décisive, non contre-lue ; plan écrit et empreinté avant l'exécution ; un seul modèle, GPT-2 petit ; treize minutes de processeur ; résultats : `travail/calcul/resultats-calcul-illustratif-v1.json`, empreinte `ec797920…`). Transposition directe de l'indice de complexité perturbationnelle, au même site (couche 3) qu'un rapport public [SL p. 2] : une position perturbée à l'entrée du bloc 3, réponse lue en sortie du dernier bloc sur les positions suivantes, binarisée contre la variabilité naturelle, compressée par Lempel-Ziv, normalisée ; 64 mesures par condition.
- **Réseaux sans fonction.** L'indice vaut 0,57 à 0,76 pour des réseaux réinitialisés ou aux poids mélangés (perte de 11 à 37 nats par jeton), contre 1,28 ± 0,70 pour le réseau entraîné (perte 3,31). Un réseau dont toutes les mises à jour sont coupées garde 0,48. Au réglage principal, tous dépassent le seuil clinique de 0,31, que le rapport public importe tel quel [SL p. 5].
- **Seuil.** Au seuil de binarisation doublé, l'ordre s'inverse : entraîné 0,83, réinitialisés 1,45 à 1,83.
- **Texte d'entrée.** Une entrée répétitive abaisse l'indice du réseau entraîné de 1,28 à 0,90, sans que le réseau change.
- **Lésion contre bruit.** À perte voisine (4,9 et environ 5,8 nats), l'amortissement des mises à jour fait descendre l'indice à 0,77 ; un bruit ajouté le fait monter à 1,55 ou 1,80 selon la graine. L'indice suit la sorte de dégradation, non la perte de fonction.
- **À rebours de l'intuition.** Les réponses du réseau entraîné sont moins diverses que celles des réseaux sans fonction (rapport de participation de 3,9, contre 6,6 à 7,6, sur 8) et plus amplifiées (gain de 1,7, contre 0,3 à 0,7).
- HYPOTHÈSE. Un réseau qui fonctionne canalise une perturbation vers peu de modes amplifiés ; « plus divers » n'y veut pas dire « plus éveillé ». Cela s'accorde avec [PH p. 18] et [OS p. 1].

### 1. Le banc de validité des mesures de « niveau » (rang 1)

- PROPOSITION. Avant de chercher un « motif d'anesthésie », établir quelles mesures tirées du cerveau méritent, dans un modèle, le nom d'instrument.
- **Grandeurs.** Pour chaque mesure candidate (complexité de la réponse à une perturbation, gain et étendue de la propagation, diversité des réponses, nombre de modes amplifiés) : aire sous la courbe de discrimination entre lésion plantée et témoin factice de même perte (de 0 à 1 ; nul : 0,5) ; part des systèmes nuls classés au niveau du réseau intact (attendu d'un instrument : 0) ; part de la variance de la mesure expliquée par la compressibilité du texte (nul : 0) ; stabilité du signe quand le seuil varie.
- **Témoins.** Perturbation aléatoire de même norme, dégradation de même perte, réseau réinitialisé, poids mélangés, entrée répétitive, perturbation dans l'espace de travail contre perturbation quelconque.
- **Issues.** Attendue : les transpositions directes échouent à un contrôle au moins ; des mesures de propagation le long des directions amplifiées passent. Négative : une transposition directe passe les quatre contrôles ; elle devient l'instrument des propositions 2 et 3.
- **Première expérience.** Faite ci-dessus. Suite : les mêmes contrôles avec une lésion visée, lentille ajustée sur un petit modèle ouvert ; quelques heures de processeur, ou moins de vingt dollars de processeur graphique. Elle tranche : y a-t-il un instrument ?
- **Antériorité.** [PH], [SL], [UH] transposent sans ces contrôles ; [B24] en donne la logique ; [CA] montre que les épreuves fonctionnelles passent sur un très petit modèle.

### 2. L'échelle de pertes sous suppression graduée, mémoire comprise (rang 2)

- PROPOSITION. Supprimer par degrés l'espace de travail d'un modèle, lire l'ordre dans lequel les fonctions tombent, puis tester ce que le modèle garde de ce qu'il a traité pendant la suppression.
- **Grandeurs.** (i) Dose de demi-perte par fonction, en nats de divergence induite sur du texte courant. (ii) Corrélation de rang, de −1 à 1, entre l'ordre du modèle et l'échelle humaine scellée ; nul : la valeur obtenue sous le témoin. (iii) À dose fixe, près du seuil : contraste des activations entre essais réussis et ratés. (iv) Mémoire : un contenu est présenté sous suppression, la suppression est levée, puis on mesure le rappel explicite (taux de bonnes réponses) et l'effet implicite (écart de log-probabilité d'une complétion amorcée) ; nul : égalité avec la condition sans suppression. Deux sortes de contenu : littéral, relisible dans les jetons ; inféré à la lecture.
- **Témoins.** Directions hors de l'espace de travail appariées en influence en aval, et non seulement en norme [CE p. 23] ; essais appariés en marge de départ, contre la fragilité ordinaire ; lésion des couches basses, pour la dissociation inverse ; suppression à la lecture seule contre suppression au rappel seul.
- **Issues.** Attendue : l'ordre est plus proche de l'échelle humaine sous lésion visée que sous témoin. Pour la mémoire, deux issues instructives. Ou bien l'inféré est perdu et l'amorçage gardé : profil humain (les auteurs de [K p. 8] lisent leurs données comme une consolidation compromise). Ou bien rien n'est perdu, parce que le modèle relit son passé par l'attention : disanalogie de principe avec l'anesthésie, que [DN p. 11] laisse prévoir. Négative : même ordre sous témoin, la dissociation n'était que fragilité.
- **Première expérience.** La mémoire, sur GPT-2 petit ou un modèle d'un milliard de paramètres : deux contenus, deux moments de suppression, lésion visée et témoin ; de dix à cinquante dollars de processeur graphique. Elle tranche : l'« anesthésie » d'un modèle laisse-t-elle un trou de mémoire ?
- **Antériorité.** Batterie et témoin de norme [G p. 25-26] ; épreuves proposées, trace commencée [DN p. 10] : l'équipe la mieux placée avance, le risque de collision est fort sur l'échelle. Sur la mémoire de ce qui est traité sous suppression, je n'ai rien trouvé (recherche du 22 novembre) : question, non revendication.

### 3. Le motif dans les activations ordinaires : un axe de niveau existe-t-il ? (rang 3)

- PROPOSITION (ajout du directeur). Chercher si un modèle en fonctionnement ordinaire traverse de lui-même des régimes où l'espace de travail se vide, et si ces régimes prédisent une perte de fonction.
- **Grandeurs.** (i) Occupation de l'espace de travail par position : nombre de directions actives, de médiane proche de 25, variable selon le contexte [G p. 32]. (ii) Part de la variance de l'occupation portée par un facteur lent, une fois retirés les traits du texte (surprise, répétition, position) : entre 0 et 1 ; nul : 0, par permutation de blocs. (iii) Après un passage d'occupation basse, taux de réussite d'une sonde insérée (rappel, inférence), contre un passage apparié d'occupation haute. (iv) Gain de prédiction de l'échec par l'occupation au-delà d'un prédicteur sur le texte seul (écart d'aire sous la courbe ; nul : 0).
- **Témoins.** Prédicteur sur le texte seul, lésion plantée comme témoin positif du détecteur, seconde définition de l'espace de travail, contextes tenus à l'écart.
- **Issues.** Attendue : pas d'axe de niveau, l'occupation suit le contenu. Cette issue nulle donnerait au doute publié [DN p. 8-9, 11] sa mesure ; l'issue positive le contredirait.
- **Première expérience.** Occupation sur un million de jetons de textes mêlés, modèle d'un milliard de paramètres ; quelques heures de processeur graphique. Elle tranche (ii).
- **Antériorité.** Occupation définie et variable [G p. 32] ; contenu tiré dans l'espace à la demande [G p. 22-24].

### 4. Côté cerveau : quelles strates d'un modèle de langage le cerveau anesthésié suit-il encore ? (rang 4)

- PROPOSITION. Renverser l'idée : le modèle sert de règle graduée. Des traits de quatre strates (acoustique ; lexicale sans contexte ; contextuelle courte ; contextuelle longue) prédisent l'activité cérébrale à chaque niveau de sédation.
- **Grandeur.** Corrélation entre activité prédite et observée, rapportée au plafond de bruit, par région, niveau de sédation et strate ; statistique : interaction entre strate et niveau ; nul : traits décalés dans le temps.
- **Témoins.** Condition de récupération (l'ordre des blocs est constant sous sédation profonde, prudence demandée par les auteurs [N18 p. 4]) ; mouvement ; modèle acoustique seul.
- **Issues.** Deux lectures sont en tension (section 1). Si les strates longues tombent seules, l'intégration sur un long contexte est ce que la conscience ajoute chez l'humain. Si elles tiennent, un calcul de la sorte de celui d'un modèle de langage tourne sans conscience chez l'humain, et la ressemblance entre le modèle et le cerveau éveillé ne dit rien de la conscience du modèle. Négative : puissance insuffisante, avec cinq minutes de récit par état.
- **Première expérience,** sans location : analyse de puissance sur l'état éveillé du jeu ouvert (plafond de bruit par région ; les traits contextuels y battent-ils l'acoustique ?). Elle tranche si le jeu peut répondre.
- **Antériorité.** [K] l'a fait dans l'hippocampe, avec des plongements sans contexte [K p. 13] ; [N18] sans traits de modèle. Je n'ai pas trouvé de réanalyse de ce jeu par des traits contextuels : question.

### Non retenues

- Interroger le modèle sur ce qu'il « vit » sous suppression : fait [G p. 27-28], non propre à soi, et un modèle a lu des récits d'anesthésie.
- La « sédation » comme levier de contrôle : elle touche des hypothèses retirées du programme ; par nœud seulement.

### Ce qu'un résultat permettrait de dire, et ne permettrait pas

PROPOSITION. Il permettrait de dire :
1. Si l'échelle humaine se retrouve sous lésion visée et non sous témoin : le modèle possède, dissociable, la machinerie dont la perte accompagne l'inconscience chez l'humain. C'est un indicateur d'accès, au sens de la théorie de l'espace de travail global.
2. Si aucun axe de niveau n'apparaît : le doute publié est mesuré, l'anesthésie est un faux ami pour cette classe de systèmes, et la recherche se replie sur les indicateurs de contenu.
3. Côté cerveau : ce que la conscience ajoute, ou non, au calcul du langage chez l'humain.

Il ne permettrait pas :
1. De dire que le modèle non lésé est conscient : ce serait affirmer le conséquent. L'objection du petit modèle demeure : GPT-2 petit passe quatre épreuves sur cinq [CA].
2. De toucher les théories qui lient la conscience au substrat (information intégrée, naturalisme biologique) : les auteurs le disent eux-mêmes [G p. 58]. Ni la théorie du traitement récurrent, qui écarte d'emblée un transformeur sans retour [G p. 59] : pour elle, il n'y a rien à anesthésier.
3. De séparer l'accès de l'expérience vécue [CE p. 17].
4. De s'appuyer sur ce que le modèle dit de lui : la question déplace l'état qu'elle interroge [MB p. 1].

### Usages pour la recherche sur la conscience des intelligences artificielles

PROPOSITION. (i) Un banc à lésion plantée, équivalent de la population d'étalonnage des cliniciens : tout marqueur proposé pour un grand modèle y passerait d'abord. (ii) Des prévisions écrites d'avance par les tenants de théories opposées. (iii) Pour le bien-être des modèles, une suppression validée serait une précaution candidate, sous les seules théories de l'espace de travail ; mais elle change la conduite évaluée. Proposition non trouvée publiée : question.

### Classement

1, le banc : il conditionne 2 et 3, ne coûte presque rien et rend un résultat quelle que soit l'issue. 2, l'échelle et la mémoire : elles portent le résultat de théorie. 3, le motif ordinaire : c'est l'idée propre du directeur, mais il exige l'instrument. 4, le côté cerveau : la plus grande portée de fond, un collaborateur à trouver.

## D. Décisions qui reviennent au directeur

Sans défaut (nœuds ou choix de périmètre). Enjeux : faits rapportés plus haut ; le reste : propositions.

**D1. Ouvrir cette ligne maintenant, ou la verser à l'atelier d'idées.**
Enjeu : trois chantiers actifs au plus, porte de fin décembre ; la ligne est hors du programme de contrôle.
- (a) Atelier seul : servir les deux questions, aucune expérience. Avantage : aucune dispersion. Inconvénient : l'idée vieillit pendant que d'autres avancent.
- (b) Atelier, plus le banc sur processeur comme pièce d'à côté. Avantage : un résultat court et citable, le calcul existe (à contre-lire). Inconvénient : un quatrième objet de fait.
Recommandation : (a) maintenant, (b) dès qu'un chantier ferme. Confiance : 0,75.

**D2. Zone crue libre, trouvée occupée : sous quel angle écrire.**
Enjeu : l'espace de travail, sa suppression, les épreuves cliniques proposées, le doute sur le niveau, des transpositions naïves : tout cela est publié. Écrire « personne n'a cherché l'anesthésie dans un modèle » serait faux ; écrire « l'anesthésie est l'inverse de la conscience » aussi.
- (a) « Épreuve du doute publié » (échelle, mémoire, axe de niveau). Avantage : net, réfutable. Inconvénient : collision probable avec l'équipe de [G].
- (b) « Banc de validité ». Avantage : ne dépend d'aucune équipe, joue sur les forces du programme (vérité plantée, nuls, bases). Inconvénient : papier de méthode.
- (c) Côté cerveau. Avantage : portée. Inconvénient : collaborateur requis.
Recommandation : (b), puis (a) si le banc donne un instrument. Confiance : 0,6.

**D3. Sur quel modèle faire une première expérience (changer de modèle est un nœud).**
Enjeu : à petite taille, l'instrument est incertain : GPT-2 petit passe les épreuves, sauf une, sans la structure [CA] ; fonctions d'espace de travail faibles sur de petits modèles [DA] ; lentille réimplémentée de 1,5 à 9 milliards de paramètres [JL], répliquée sur 27 [CE p. 33] ; aucun essai connu sur le modèle de 8 milliards du programme. [CA], [DA], [JL] : non vérifiés sur PDF.
- (a) GPT-2 petit ou un milliard de paramètres. Avantage : coût nul ou infime. Inconvénient : fonctions pauvres.
- (b) Le modèle du programme. Avantage : continuité. Inconvénient : devis, instrument incertain.
- (c) 27 milliards. Avantage : instrument répliqué. Inconvénient : coût, changement de modèle.
Recommandation : (a) ; (b) sur devis si (a) est positif. Confiance : 0,6.

**D4. Prendre un contact extérieur (nœud : le directeur envoie).**
Enjeu : l'échelle humaine doit être écrite par un spécialiste ; les données unitaires demandent une affiliation universitaire [K p. 14].
- (a) Aucun contact, jeu ouvert seul. Avantage : autonomie. Inconvénient : cinq minutes de récit par état.
- (b) Un collaborateur en neurosciences de l'anesthésie. Avantage : échelle, données. Inconvénient : délai, exposition de l'idée.
Recommandation : (a) d'abord (analyse de puissance), (b) si elle est favorable. Confiance : 0,55.

**D5. Lire le travail de juillet 2026 pour le programme de contrôle.**
Enjeu : la lentille lit des délibérations non dites (délibération stratégique, conscience d'être évalué, dispositions désalignées [G p. 1]) ; c'est un voisin des moniteurs boîte blanche du programme. Je n'ai pas pu vérifier s'il a déjà été lu (cloisonnement).
- (a) Le verser à la veille comme voisin à confronter aux papiers A et B. Avantage : antériorité à jour. Inconvénient : une lecture de plus.
- (b) En plus, l'envisager comme base nommée des moniteurs. Avantage : comparaison directe. Inconvénient : nœud, coût.
Recommandation : (a), sans rouvrir d'hypothèse retirée. Confiance : 0,8.

FIN DE LA RÉPONSE
