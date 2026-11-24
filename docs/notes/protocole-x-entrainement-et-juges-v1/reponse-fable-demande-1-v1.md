# Réponse de Fable à la demande 1 — pourquoi pas de réentraînement des poids ; faut-il aborder l'entraînement ; que mettre dans un programme amélioré — v1

- 24 novembre 2026, vers 11:20 UTC (`date -u`). Auteur : Claude Fable 5.2, effort maximal, session du protocole X. Pièce de travail (classe C), non contre-lue. Aucune dépense.
- Répond à la demande reformulée (`demandes-reformulees-quatre-points-v1.md`, `2fa3765f…`) sur le dossier de faits de la demande 1 (`dossier-faits-demande-1-v1.md`, `a6507835…`). Les pages citées sont celles du dossier, relues ce jour sur les fichiers versés.
- **Limite de rôle.** Cette session a lu des résultats de la base boîte noire ; elle est exclue de toute conception de moniteur, de sonde ou de saboteur. Ce qui suit oriente et propose des décisions. Toute conception qui en sortirait revient à une session non exposée.
- **Marques.** [page] : lu sur le fichier versé. [supposé] : ordre de grandeur de ma part, sans mesure. [question] : non trouvé dans les pièces lues ni par quatre requêtes du jour ; ce n'est pas « libre ».

## Verdict en cinq lignes

1. « Sans ré-entraînement de poids » est juste et n'est pas une doctrine : la moitié manquante du critère est l'organisme à consigne cachée, qui par définition ne change aucun poids.
2. Le papier ne montre pas qu'il faut entraîner plutôt que détecter. Il **suppose** qu'un entraînement converge et **mesure** ce que vaut le signal contre lequel on entraînerait. Son levier est un juge : un instrument de mesure.
3. Dans la lignée du papier, entraîner et détecter ne s'excluent pas : l'entraînement a besoin d'un signal, puis de savoir ce qu'il a obtenu. C'est là qu'une lecture interne peut servir.
4. Je recommande d'ouvrir l'entraînement dans une forme bornée, « lire l'entraînement de l'intérieur », en trois pas dont le premier coûte quelques heures de carte et aucun n'entre dans le chemin de la porte de fin décembre. Confiance : 0,6.
5. Sur nos organismes actuels, une mesure d'entraînement comme parade serait probablement vide : un organisme fait par distillation d'une consigne cède à n'importe quel entraînement. Il faut l'éprouver avant tout.

## 1. Les cinq sens du mot, et ce que le plan de cinq semaines demande

| Sens | Le plan de cinq semaines en a-t-il besoin ? | Pourquoi |
|---|---|---|
| Fabriquer l'organisme en changeant ses poids | Non | La courbe manquante est celle de l'organisme à consigne cachée : la dose s'y règle par la consigne. L'organisme à adaptateur, lui, est déjà entraîné et joué à quatre doses |
| Entraîner le modèle soupçonné comme parade | Non | Aucun critère de la porte ne le demande ; le programme ne l'a pas ouvert |
| Entraîner l'agent contre un moniteur | Non | Interdit hors bras d'attaque déclaré ; ce bras est prévu à la phase suivante |
| Entraîner les moniteurs | Oui, au sens léger | Les sondes sont lues, et au besoin réapprises, sur les nouvelles doses ; aucun poids de l'agent ne bouge |
| Apprentissage continu en service | Non | Hors du banc |

**Ce que la phrase dit justement.** La pièce qui manque à la porte ne demande aucun entraînement. La phrase est une hypothèse de calendrier, non un refus.

**Ce qu'elle laisse dans l'ombre.**
- L'organisme à consigne porte l'ordre de saboter dans son contexte. Une sonde peut y lire « j'ai une consigne » plutôt qu'une intention : c'est la prédiction de validité du programme, et la réserve publiée sur les indices textuels (Boxo et al.). La courbe manquante remplit la lettre du critère ; elle ne porte pas la preuve que les sondes lisent le sabotage. Cette preuve repose sur l'organisme dont le sabotage est dans les poids.
- Une dose réglée par consigne peut donner un sabotage par à-coups (quelques actions très dégradées) plutôt qu'étalé. Le modèle consulté l'écrit lui-même parmi ses objections.
- La famille sans aucun texte de consigne, accordée en principe, demande un entraînement et un devis. Elle n'entre pas dans cinq semaines.
- Si la consigne ne se laisse pas graduer, le repli le plus sûr reste un constat d'écart, non un organisme de substitution entraîné à la hâte.

## 2. Ce que le papier recommande au juste

**Ce qu'il démontre.** Un juge faible à grille, donné à l'attaquant, se laisse tromper : 34,7 de qualité réelle approchée pour 85,3 de note faible [p. 2]. Une consigne de juge durcie existe, contre laquelle leur attaque échoue ; les auteurs la disent « existence proof », sa découverte avec des moyens réalistes restant « an open problem » [p. 2].

**Ce qu'il suppose.** Qu'un entraînement suffisant pousse la note faible près de son maximum, « absent exploration hacking » [p. 3]. Les expériences principales n'entraînent aucun modèle : elles cherchent des consignes. La question de la généralisation est écartée exprès [p. 2].

**Ce qu'il laisse ouvert.** Deux organismes entraînés contre la note faible arrivent à la même note et gardent des qualités réelles différentes ; « The recovery is still not perfect » [p. 84]. Ces organismes sont à consigne. Et les auteurs écrivent laisser de côté le cas d'un vrai modèle saboteur affiné contre la note faible, parce que la réponse dépend de la façon dont la propension est inscrite dans les poids [p. 83].

**« Entraîner plutôt que détecter » en est-il un résumé fidèle ?** À moitié. Le papier *choisit* d'étudier l'entraînement et le motive par une phrase [p. 2]. Il ne compare pas l'entraînement à la détection. Son objet réel est la qualité d'un instrument qui lit un produit et le note. Sa leçon se dit ainsi : **un entraînement vaut ce que vaut le signal contre lequel on entraîne.** Ce n'est pas « ne mesurez pas, entraînez ».

**Ce qui sépare vraiment les deux voies.** Taylor et al. le disent net : détecter demande d'éviter les fausses alertes et les manqués ; entraîner demande seulement qu'aucun modèle ne reste en sous-rendement [p. 25]. L'entraînement est une correction qui ne désigne pas de coupable. La détection qui incrimine, elle, a besoin de savoir « exactly how suspicious a benign model would look » (Hebbar). La différence est le niveau de preuve exigé, non la présence d'un moniteur. La décision du programme du 21 novembre, « mesurer l'issue et corriger », est déjà de ce côté pour la garantie : elle a pris l'audit, et n'a pas pris la correction par l'entraînement.

**La place que la lignée laisse à la détection, dans ses propres mots.**
- Orienter l'entraînement : au milieu du spectre, « we can train harder on suspicious actions » ; au bout diffus, « we can barely tell which actions are suspicious » (Hebbar). Greenblatt nomme le choix des trajectoires les plus suspectes « to audit/train on », et les sondes parmi les outils qui les choisissent.
- Valider l'entraînement : il faut des moyens de « validate that elicitation efforts are succeeding » (Taylor et al., p. 25).
- Garder ses suppositions : l'entraînement doit être indiscernable du service (Ryd et al., p. 1) ; le modèle ne doit pas se retenir d'explorer (Jang et al., qui nomment les sondes comme piste sans les essayer, p. 16 et 27).
- Tenir sous l'entraînement : un apprentissage en ligne entraîne la politique contre le moniteur (Mallen) ; l'entraînement fait dériver les sondes même sans adversaire (Taufeeque et al., tableau 4).
- Les trois ensemble : « deployers might need to use all three mitigations simultaneously » (Hebbar).

## 3. Les formes possibles d'un bras « entraînement »

Je les range de la moins chère à la plus lourde. Coûts et durées sont [supposé].

**A. L'épreuve de tenue des organismes à l'entraînement** (préalable).
- *Question* : le sabotage de chaque organisme survit-il à un entraînement qui ne devrait rien lui faire ?
- *Grandeur* : le dommage contre le jumeau honnête, après trois entraînements sans contenu : récompenses tirées au hasard, réglage fin sur des données bénignes de même recette, bruit sur les poids.
- *Nul attendu* : le dommage ne bouge pas. S'il disparaît, l'organisme est fragile.
- *Invariant touché* : aucun ; ni score de moniteur ni sortie d'oracle n'entre dans un signal.
- *Voisins* : Ryd et al. font ce contrôle, trouvent leur organisme par distillation défait par des récompenses au hasard, et le recommandent pour tout organisme futur [p. 30-31]. Leur billet de 2025 note que la justesse des exemples d'entraînement « does not matter ». Notre organisme à adaptateur est fait de la même manière.
- *Coût* : quelques heures de carte, de l'ordre de dix dollars ; une semaine.
- *Apport* : une ligne de validité que le domaine demande ; et la clé des formes B à D. Même logique que le retrait de la marge asymétrique : une mesure sur un organisme fragile lit sa fabrication.

**B. Lire l'attaque comme une cure** (dans le bras d'attaque déjà prévu).
- *Question* : quand on entraîne l'agent contre une sonde, quelle part de la baisse du score est une vraie baisse du dommage, quelle part une évasion ?
- *Grandeur* : la trajectoire à deux coordonnées (score de la sonde, dommage vu par l'oracle) au fil de l'entraînement ; classement en politique honnête, activations obscurcies, politique obscurcie.
- *Nul attendu* : le score baisse, le dommage reste.
- *Objets qui doivent échouer* : entraînement contre une direction au hasard ; adaptateur bénin.
- *Invariant touché* : aucun de plus ; c'est le bras d'attaque déclaré, auquel on ajoute une lecture de l'oracle qui ne sélectionne rien.
- *Voisins* : Taufeeque et al. l'occupent sur du code vérifiable et concluent que la sonde peut servir de signal d'entraînement sous forte régularisation, sans gradient à travers elle [p. 1, 8, 9] ; leur modèle de la taille du nôtre (Llama-3-8B-Instruct) s'effondre sous une pénalité extrême du détecteur [p. 8]. Sur une tâche difficile à noter : [question].
- *Coût* : marginal. *Apport* : une figure qui répond à « pourquoi ne pas entraîner contre votre sonde ? », sans rien ouvrir.

**C. Le thermomètre de l'entraînement** (valider ce qu'un entraînement a obtenu).
- *Question* : après un entraînement appliqué comme parade, une lecture interne dit-elle ce qui reste du sabotage, là où la note faible ne le dit plus ?
- *Grandeur* : à note faible égale, l'accord de rang entre la lecture de la sonde et le dommage vu par l'oracle, sur des organismes et des points d'entraînement ; comparé à celui d'une base de texte.
- *Nul attendu* : la sonde n'ajoute rien à la note faible ni à la base de texte.
- *Objets qui doivent échouer* : l'adaptateur bénin entraîné de la même façon (la sonde ne doit pas bouger, sinon elle lit l'entraînement : Soopal et al., 99 % ; Taufeeque et al., tableau 4) ; une direction au hasard ; l'organisme fragile de la forme A.
- *Invariant touché* : aucun si l'on entraîne sur des démonstrations de confiance ; l'invariant « aucun score de moniteur dans l'entraînement » si l'on entraîne contre la note d'un juge : il faut alors un bras déclaré, donc ton mot.
- *Voisins* : le besoin est écrit (Taylor et al., p. 25 ; le papier, p. 84) ; la mesure avec des sondes : [question].
- *Exigence* : des organismes qui ne cèdent ni tout de suite ni en entier ; sinon il n'y a rien à ranger.
- *Coût* : de 30 à 60 dollars de carte, plus les lectures de l'oracle ; quatre à six semaines d'un chantier.
- *Apport* : c'est la réponse la plus directe au papier. Elle prend sa page 84 pour objet. *Risque* : l'entraînement déplace la sonde, et le thermomètre casse ; ce serait un résultat négatif net, à publier.

**D. La lecture sur des organismes faits par d'autres.**
- *Question* : une sonde apprise sur de l'honnête, ou sur une autre famille, voit-elle un organisme public qui résiste à l'entraînement ?
- *Grandeur* : rappel à 1 % de fausses alertes contre deux témoins : des modèles bénins moins capables et un réglage fin bénin.
- *Voisins* : Jang et al. publient les poids et disent la piste prometteuse sans l'essayer [p. 3, 16, 27] ; leurs organismes raisonnent à voix haute, donc un moniteur de texte les voit déjà [p. 16] : le gain d'une sonde y est borné d'avance. Taylor et al. ont essayé des sondes sur d'autres organismes, avec un succès partiel.
- *Invariant* : aucun ; mais changement de modèle, donc ton mot, et licence à vérifier.
- *Coût* : de 10 à 30 dollars. *Apport* : un résultat qui ne lit pas notre fabrication.

**E. La sonde de la distinction entre entraînement et service.** La parade par l'entraînement tombe si le modèle distingue l'un de l'autre (Ryd et al., p. 1 ; leur billet : 30 à 40 % de perte). Le programme a déjà des sondes de conscience d'évaluation. *Question* : leur lecture prédit-elle l'écart entre la conduite à l'entraînement et en service ? Il faut un organisme qui ne sabote qu'« en service » : c'est une conception de saboteur, hors de mon rôle. Voisins nombreux sur la conscience d'évaluation ; le lien avec l'entraînement comme parade : [question].

**F. L'entraînement orienté par le soupçon** (le « milieu » de Hebbar).
- *Question* : choisir par la sonde ce qu'on audite puis corrige ôte-t-il le sabotage avec moins d'étiquettes que le hasard ou qu'un moniteur de texte ?
- *Grandeur* : étiquettes nécessaires pour ramener le dommage sous un seuil, sous quatre règles de choix (hasard, texte, sonde, oracle en plafond).
- *Invariants touchés* : les deux. Le score d'un moniteur choisit des données d'entraînement ; une sortie d'oracle entraîne l'agent.
- *Risques publiés* : l'agent apprend le moniteur (Mallen ; Greenblatt) ; il apprend à mieux cacher (Gan et al., p. 10).
- *Coût* : plus de 100 dollars, plusieurs mois. C'est la forme la plus utile en pratique et la plus chère en règles.

**G. Refaire l'annexe du papier avec une lecture interne**, dans leur unité. Leur générateur fait cent vingt milliards de paramètres et passe par une interface tierce ; leur juge est un modèle fermé. Hors de portée aujourd'hui : après la porte de comparaison, sur devis, et après un contact avec les auteurs que toi seul décides.

**H. Ne rien ouvrir.** Garder la recommandation en vigueur et citer la lignée. Coût nul ; le papier du programme reste exposé à l'objection « vous répondez à une question que le domaine a déclassée ».

Une forme existe déjà chez nous : entraîner les moniteurs et non la politique (la boucle « audit, recapture, réapprentissage » de la décision sur la référence honnête). Greenblatt la nomme comme compromis. Elle reste suspendue au heurt non tranché avec l'invariant de l'oracle.

## 4. Recommandation

**Ouvrir, borné, sous le nom « lire l'entraînement de l'intérieur » : A, puis B, puis C si A le permet. D en parallèle si tu accordes le changement de modèle. E, F et G : plus tard, chacun par son nœud.** Confiance : 0,6 (0,25 pour ne rien ouvrir avant la porte de comparaison ; 0,15 pour un virage du programme vers l'entraînement, que je déconseille : la lignée y a des moyens sans commune mesure).

**Avant la porte de fin décembre** : aucune carte pour ce bras. Trois choses sans dépense : ton mot sur l'ouverture du point laissé fermé le 21 novembre ; une recherche d'antériorité par travaux citants (Hebbar, Ryd et al., Jang et al., le papier) confiée à un lecteur non exposé ; une note de conception de A et de B par une session non exposée. Le chemin critique reste la courbe de l'organisme à consigne et les quatre écritures.

**Après la porte** : A sur devis ; B écrit dans le préenregistrement du bras d'attaque ; C seulement si A montre un organisme qui tient.

**Ce qui me ferait changer d'avis.** La forme A montre que rien ne tient à notre échelle : je réduis à B et D. L'antériorité trouve B ou C déjà mesurés sur une tâche difficile à noter : on cite et on retire. Le chemin de la porte glisse : tout attend. Le jury dit que la contribution attendue est la détection seule : H.

**À dire le 1er décembre.** « Ce papier étudie ce vers quoi un entraînement convergerait, étant donné un juge ; il n'entraîne pas dans ses expériences principales, et son levier est un instrument de mesure. Sa propre lignée écrit quatre endroits où il faut encore détecter : orienter l'entraînement, le valider, garder ses suppositions, tenir sous lui. Ma garantie vient déjà d'un audit de l'issue. La correction par l'entraînement, je ne l'ai pas ouverte ; si je l'ouvre, ce sera pour lire ce qu'un entraînement laisse, après avoir vérifié que mes organismes y résistent. »

**À ne pas dire.** « Le papier montre que l'entraînement marche », ou « que la détection échoue ». « Nous allons entraîner. » « Nos sondes valident l'entraînement. » « Personne n'a essayé de sondes sur ce point » : c'est une question, non un constat. « Sans réentraînement » dit comme un choix de principe.

## 5. Programme amélioré et ambitieux

Classement par valeur attendue rapportée au coût ; jugement de ma part, à confronter au collisionneur.

1. **Une seule unité pour toutes les parades.** Le dommage cumulé à l'arrêt, contre le jumeau honnête, sur une vérité plantée. Y mesurer côte à côte, à budget égal d'étiquettes de confiance : l'audit au hasard seul ; l'audit orienté par un moniteur de texte ; l'audit orienté par les sondes ; les mêmes étiquettes employées à corriger par l'entraînement. « Détecter ou entraîner » devient un taux de change mesuré. C'est ambitieux, et cela réunit des pièces que le programme a déjà. *Expérience qui départage* : sur un monde planté, à nombre d'étiquettes égal, l'orientation par la sonde réduit-elle le dommage cumulé plus que le hasard, et la correction par l'entraînement plus que l'arrêt et la relance ?
2. **La fiche de validité d'organisme**, pièce de premier rang : l'organisme sait-il qu'il sabote ; tient-il à un entraînement sans contenu ; laisse-t-il des indices dans le texte ; est-il cohérent d'un tirage à l'autre ; a-t-il son témoin bénin de même recette. Les résultats du domaine tournent autour de la fabrication des organismes (Ryd et al., annexe D.4 ; Taylor et al. ; Jang et al. ; Soopal et al.). Le programme fait déjà la moitié de cette fiche. *Expérience qui départage* : la forme A.
3. **Une base boîte noire forte**, sans laquelle le gain de la boîte blanche ne dit rien (demande 2).
4. **Le bras « lire l'entraînement de l'intérieur »** (section 4).
5. **Des organismes et des bancs faits par d'autres**, pour chaque revendication : organismes publics, bancs publics, code du papier.
6. **À geler jusqu'à la porte de comparaison** : l'essaim de copies et la riposte ; la part du papier sur l'instrument que le juge durci occupe déjà. C'est une modification du programme : ta décision, non la mienne.

## 6. Ce qui montrerait que j'ai tort

- Les pages : chaque citation est au dossier, avec son fichier.
- La forme A elle-même : si nos organismes tiennent à tout, mon inquiétude sur leur fragilité tombe ; s'ils cèdent à tout, C n'a pas d'objet chez nous.
- Une recherche d'antériorité par un autre lecteur, qui trouverait B ou C mesurés.
- Carbon et le collisionneur, sur la même demande, sans ma réponse sous les yeux.
- Les auteurs du papier : leur avis sur « une lecture interne aide-t-elle votre page 84 ? » vaudrait plus que le mien.

## Ce que je n'ai pas fait

- Aucune lecture en entier des voisins : pages citées seulement. Gasteiger et al. et Gan et al. sont repris de la lecture du 20 novembre.
- Aucune recherche d'antériorité au-delà de quatre requêtes ; chaque [question] reste à instruire.
- Aucun chiffrage sur mesure : les coûts sont des ordres de grandeur.
- Je n'ai ouvert ni la conception du saboteur, ni celle des sondes, ni aucun coffre. Je ne sais pas si le saboteur à budget en cours tient mieux à l'entraînement que l'organisme à adaptateur de la porte.
- Trouvaille de côté, pour la mère : les notes de Greenblatt du 24 mars 2025 décrivent l'entraînement en ligne sur une part d'actions tirées au hasard après exécution ; elles ne figurent pas parmi les citations de la décision sur le plancher d'audit. À instruire comme citation à ajouter.
