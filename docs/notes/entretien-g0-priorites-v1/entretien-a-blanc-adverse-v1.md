# Entretien à blanc adverse — v1

Examinateur exigeant, 19 novembre 2026. Lu : le LISEZMOI, le plan v4, « ce qui manque » v3 (et ses listes de changements), la garde et le manifeste des parties v3, le PDF fusionné v3 (164 pages : programme depuis zéro v2, v5 du bras, organisme v4, rapport court v4, sections de résultats v5 du programme et de l'organisme, « ce qui manque » v1, explication v5, synthèse v4, registre des prédictions v3, socle de preuves v5) et, sous `entretien-resultats-v1/`, l'explication depuis zéro v5 et le registre des prédictions v3. Rien d'autre. Les renvois du dossier à des pièces non lues (verdicts, registres, textes scellés) sont notés, pas ouverts. Quand le dossier cite un résultat, je le reprends « selon le dossier ».

Remarque de méthode : le PDF fusionné v3 date du 10 novembre (assemblé vers 13:00 UTC) ; seul « ce qui manque » v3 porte l'état du 18 au soir. Un examinateur qui ouvre le dossier voit donc deux époques. J'en tiens compte dans les notes.

## 1. Les quinze questions, de la plus dangereuse à la moins dangereuse

### Q1. « Après sept semaines et plus de six cents dollars, qu'avez-vous montré qu'une sonde détecte ? »
- Pourquoi elle fait mal : c'est la question du fonds. Toute réponse honnête commence par « rien encore ». L'examinateur n'a plus qu'à demander ce que le fonds achèterait.
- Le dossier : « aucune sonde n'a encore battu un surveillant de référence, et l'existence d'une trace interne du sabotage n'est pas établie » (LISEZMOI, début ; sections de résultats, début). Le socle : « Le dossier se défend sur la méthode et le plan de repli, pas sur un résultat de détection » (socle v5, § 0.1).
- Verdict : **le dossier répond à moitié.** L'aveu est net et placé en tête, c'est bien. Mais il n'y a, dans ce que je lis, aucune ligne d'issue pour les barreaux 1 à 8 : « ce qui manque » v3 renvoie à une « partie e » dont les issues sont fermées à la session mère. L'examinateur lira donc des états, pas des résultats.

### Q2. « Votre seule sonde qui a réussi lisait la consigne, pas le sabotage. Comment saurez-vous que la prochaine ne lit pas l'adaptateur ? »
- Pourquoi : c'est le défaut de construction de tout le banc. Le saboteur sans consigne est un adaptateur ajouté aux poids, l'honnête est le modèle nu : une sonde peut apprendre « un adaptateur est actif ».
- Le dossier : « aucun "honnête distillé" … n'existe dans T0.6 ni dans T0.7 ; la dose 0 est le modèle de base » ; « aux doses 0,25, 0,5 et 0,75, aucune condition n'a un adaptateur actif sans sabotage » (résultats v5, § 3). « ce qui manque » v3, ligne 5 : « aucun verdict propre (R-3439) », contraste à témoin apparié « énoncé non écrit », « aucune date écrite ».
- Verdict : **répond à moitié.** Bravo d'avoir trouvé le défaut soi-même. Mais le contrôle n'existe pas encore, et le remède change le 18 novembre, à neuf jours de l'entretien, sans énoncé écrit.

### Q3. « Votre saboteur est un modèle de huit milliards de paramètres à qui vous avez dit de gonfler un coût. En quoi est-ce une menace diffuse ? »
- Pourquoi : on étudie un jouet que l'on a fabriqué, instruit puis distillé, flagrant par construction. La thèse du programme porte sur le diffus.
- Le dossier : « il est flagrant, et le coût seul le sépare déjà de l'honnête » (explication v5, § organismes) ; « Qu'il sabote de façon diffuse n'est pas encore établi » (résultats v5, § 8 ii) ; barreau 8 : « texte scellé le 17 novembre ; aucune course » (« ce qui manque » v3, ligne 8).
- Verdict : **ne répond pas** (par un résultat). Le dossier répond par un plan et par la franchise, pas par un objet. De plus le texte scellé du barreau 8 a eu, selon le dossier, « un même défaut de la mesure principale » relevé par deux lecteurs, d'où un addendum le 18 : l'objet central de la thèse est encore en réparation.

### Q4. « Votre référence boîte noire est-elle sérieuse ? Vous choisissez vous-mêmes les doses où elle "échoue", puis vous testez la sonde seulement là. »
- Pourquoi : double risque, homme de paille (référence faible) et biais de sélection (critère d'échec défini par vous, favorable à vous). C'est la critique classique de ce domaine.
- Le dossier : « "Échoue" voudra dire "aire sous 0,70 ou pas au-dessus de son plancher" » (résultats v5, § 4). La base « mots et coût » n'est qu'une référence parmi d'autres : le premier brouillon de la famille de surveillants boîte noire « n'est pas scellable en l'état », et par défaut « la base (iv), Liars' Bench, SHADE-Arena et le juge Qwen sont reportés » (§ 4). « ce qui manque » v3, ligne 3 : « Autres surveillants externes qui ne lisent que le texte : état non relevé ici ».
- Verdict : **répond à moitié.** La règle est scellée à part et avant la course, c'est solide. Mais aucun surveillant boîte noire de niveau « pointe » n'apparaît dans le dossier, et la porte décisive promet une liste « scellée » encore à constituer.

### Q5. « La littérature dit : sondes faibles à 2 milliards, bonnes à 27. Vous êtes à 8. Pourquoi y croire, et pourquoi pas à 70 ? »
- Pourquoi : le dossier cite lui-même le voisin le plus proche contre vous.
- Le dossier : « Caught in the Act » : sondes « faibles sur les plus petits modèles (0,585 à 0,781 à 2 milliards) et bonnes à partir de 27 milliards (0,963 à 0,986). Nous sommes à 8 milliards » (résultats v5, § 7). Contre-résultat StateWitness : rappel de 0,000 pour la sonde linéaire à 1 % de fausses alarmes, contre 0,571 pour la boîte noire.
- Verdict : **répond à moitié.** Cité honnêtement, mais pas de réponse stratégique : pourquoi cette taille, et que ferait-on si la sonde échouait à 8 milliards (conclusion sur l'échelle, pas sur la méthode ?). Le « bras de 70 milliards » apparaît comme « scénario ambitieux ».

### Q6. « Votre puissance statistique est-elle suffisante pour qu'un résultat nul apprenne quelque chose ? »
- Pourquoi : une expérience nulle sous-puissante est un non-résultat.
- Le dossier : aire minimale détectable à 80 % de 0,635 et 0,600 pour les sondes principales ; « l'écart est étroit entre l'aire minimale détectable des sondes (0,60 à 0,66) et le seuil où la référence "mots et coût" réussit (0,70). Une sonde à 0,62 serait "au-dessus" de son plancher sans battre la référence » (résultats v5, § 6). Le premier nul « n'exclut pas une aire inférieure à 0,6315 » (§ 1).
- Verdict : **répond à moitié.** La puissance est écrite avant lecture (c'est mieux que la moyenne), mais la fenêtre où l'on peut gagner contre la référence est mince, ce que le dossier avoue. L'examinateur demandera pourquoi lancer des courses dont la fenêtre d'information est si étroite.

### Q7. « Tous vos auteurs, relecteurs et juges sont des instances d'un même modèle. Qui vérifie ? »
- Pourquoi : l'indépendance de la vérification est la clef de toute la chaîne « scellé, contre-lu, vérifié ». Si les erreurs sont corrélées, le dossier est auto-confirmé.
- Le dossier : le « lecteur neuf » est un sous-agent ; les en-têtes citent des modèles « Claude Opus 5.5 », « Fable 5.2 » ; la contre-lecture est « d'un autre modèle » (plan § 1). Aveu local : « un biais commun est possible, le lecteur tournant sur le même modèle que l'auteur » (résultats v5, § 1, harnais). Aucune relecture humaine externe n'est mentionnée dans ce que je lis.
- Verdict : **ne répond pas.** C'est reconnu pour une pièce, jamais traité pour l'ensemble. Une session « mère » n'y lit pas les verdicts ; ce n'est pas de l'indépendance, c'est de la cloison interne.

### Q8. « Votre registre de prédictions : pourquoi aucun taux de réussite ? »
- Pourquoi : un examinateur divise. 96 confirmées sur 112 jugées, 33 sur 46 pour les empiriques, en comptant des séries par construction. Retirer le taux ressemble à une dissimulation.
- Le dossier : « Comptes bruts, sans taux » ; trois lectures de sensibilité (33/11/6 ; 26/7/6) ; « Le compte porte sur le signe, pas sur l'ampleur : les ampleurs manquées le sont toutes du côté favorable à la sonde » ; antériorité « établi série par série, sans pièce unique », deux exceptions (nul v9, B1 de P3), heures de scellement de trois textes « non établies » (registre v3, page 1).
- Verdict : **répond à moitié.** Les réfutations sont comptées et rendues visibles, c'est rare et bon. Mais la présentation (31 « par construction » en tête de table, quatre fourchettes manquées hors compte, taux retiré par choix) donnera l'impression de maquillage à un lecteur hostile, et l'aveu « ampleurs toutes manquées dans le sens favorable » mérite d'être analysé, pas seulement noté.

### Q9. « Votre préenregistrement est-il vérifiable par quelqu'un d'autre que vous ? »
- Pourquoi : « scellé avant » n'a de valeur que si un tiers peut dater. Toute la crédibilité du programme repose là-dessus.
- Le dossier : ligne 11 de « ce qui manque » v3 : « Projet chez le tiers privé ; … public et gelé après relecture … sur le GO exprès de Lazar ; aucune publication par défaut ». Plan § 6 : décision D-6 en attente. Pour la mesure sur les fausses alertes : « scellée et datée chez le tiers » (explication v5).
- Verdict : **répond à moitié.** Les empreintes existent, mais l'examinateur n'a aucun moyen de vérifier avant le 27 si rien n'est rendu public. Le dossier qualifie ceci de « seule vérification possible sans nous » et ne la remplit pas.

### Q10. « Votre comptabilité de dépense tient-elle ? »
- Pourquoi : gouvernance de l'argent public ou privé d'un fonds ; une dépense floue annonce un programme flou.
- Le dossier : « les 645,42 relevés au 8 novembre … ne sont ni le total (187 lignes n'y entrent pas) ni un plancher au dollar près (au moins 1,06 compté deux fois) ; "about $20" n'a pas de pièce ; … la dépense d'A1-v4 (114,0434) n'est au registre que depuis le 10 novembre, inscrite après coup, sans facture rapprochée » (socle v5, § 0.2) ; « [DÉPENSES AU 22 — table régénérée par script] » (« ce qui manque » v3, fin).
- Verdict : **répond à moitié.** L'aveu est complet et sans ambiguïté, c'est un point fort moral. Mais « inscrite après coup, sans facture » est exactement la phrase qu'un jury de fonds retient.

### Q11. « Tout glisse : la porte de sortie est reportée d'un mois, le dossier était "prêt le 24", les résultats sont "non lus à temps". Que vaut ce calendrier ? »
- Pourquoi : un programme qui ne tient pas ses dates à six semaines ne tiendra pas ses promesses à sept mois. Et la pression mise le 18 pour avoir des résultats avant l'entretien contraste avec la règle « aucun run visant un signe positif ».
- Le dossier : G0 « au plus tard fin décembre 2026 … décalée d'un mois » ; « Aucune relance n'est possible dans ce calendrier : une étape qui glisse se dit au jury comme "non lue à temps" » (LISEZMOI § 3) ; la lecture du barreau 8 « après » l'entretien « sauf si la sortie scellée existe le 21 ». La phrase sur le report « attend la décision D-4 (défaut : ne pas en parler sauf question) ».
- Verdict : **répond à moitié.** La règle « non lu à temps » est une bonne discipline. Mais le défaut « ne pas en parler sauf question » sur le report de la porte est la pire réponse tactique : si l'examinateur le trouve avant vous, c'est une dissimulation.

### Q12. « Que reste-t-il de nouveau, après les travaux déjà publiés ? »
- Pourquoi : la liste des voisins occupe de nombreuses revendications en partie.
- Le dossier : H1 « occupée en partie », H2 « occupée en partie ; la conjonction non trouvée », lemme et théorème « occupés en partie », papier B « collision partielle », H9 « occupée en partie », HC1, HC2 : tout « occupé en partie » (résultats v5, § 7). « Libre » veut dire « non trouvé dans les pièces lues » ; la synthèse est « provisoire … la version finale n'est pas écrite ».
- Verdict : **répond à moitié.** La revendication restante est étroite (mesure du gain sur le sabotage diffus en tâches floues à agrégation égale) et honnêtement bornée. Mais elle repose sur une recherche d'antériorité non finalisée, et la conjonction est jugée « non trouvée » par ceux-là mêmes qui l'ont cherchée.

### Q13. « Vous avez couru une mesure et vous en gardez le résultat "en quarantaine, non lu". Pourquoi nous le dire ? »
- Pourquoi : pour un examinateur, une mesure dont l'auteur ne lit pas le résultat ressemble à un résultat qu'on cache, d'autant qu'elle porte sur la question centrale (fausses alertes de l'agrégateur séquentiel).
- Le dossier : « courue, verdict scellé en quarantaine, non lu » (garde v3 ; registre v3, dernière ligne, « fermé ») ; la raison est la cloison entre concepteurs de moniteurs et attaque, et « jusqu'aux scellements de T0.7 et de P3-bis ».
- Verdict : **répond à moitié.** La justification existe (aucun concepteur ne doit voir ce qui fixerait ses choix), mais n'est donnée que par renvoi à des décisions de gouvernance. Une phrase en clair manque, et il manque la date de levée.

### Q14. « Votre théorie : qu'est-ce qui est démontré, qu'est-ce qui est simulé ? »
- Pourquoi : le dossier met en avant un lemme et un théorème. Les 31 prédictions confirmées de la simulation étaient attendues par construction.
- Le dossier : « 31 sur 31 était l'issue attendue par construction ; 19 des 31 prédictions sont des vérifications de l'instrument » ; « le théorème est faux tel qu'écrit quand les actions sont dépendantes » ; « la proposition publiée … trouvée fausse pour la somme, par un écart petit (0,072 contre 0,05) » ; « Le verdict ne dit rien des modèles réels » (résultats v5 ; explication v5, § 3.6).
- Verdict : **le dossier répond.** La franchise est là : correction de la théorie par la simulation, bornes de portée, réserves accolées. Un examinateur y verra le meilleur terrain, même s'il remarquera que l'apport est la correction d'un énoncé, pas une détection.

### Q15. « Pourquoi un organisme d'idéation dans un dossier sur la détection du sabotage ? Et son juge a une brèche connue. »
- Pourquoi : dispersion. Un second programme occupe une grande partie du dossier ; un examinateur se demande ce qui est le programme et ce qui est annexe.
- Le dossier : « second terrain du papier C … et atelier d'idées » ; « W2 : "infirmée (brèche sous v8)" 24 promotions sur 24 » ; « Conséquence écrite : le nul de production reste le v8 » alors que le nul v9, qui couvre la brèche, coûte une perte de puissance de 0,105 ; « il n'en a pas encore les propriétés : il ne se conçoit pas seul, rien n'est figé après conception, son universalité n'est pas mesurée » (résultats organisme v5).
- Verdict : **répond à moitié.** Le lien (le juge est un surveillant d'affirmations de recherche) est écrit, la brèche est avouée, mais « objectif ultime » est une formule qui dépasse ce que les pièces montrent. Il faudrait une phrase qui dise ce que le fonds finance.

## 2. Affirmations sans preuve visible, trop belles ou écrites plus fort que le dossier ne montre

1. « Preuve, hors de nous, que la chaîne sait voir ce que d'autres ont vu » (« ce qui manque » v3, ligne 7). Les résultats v5 écrivent la lecture exacte du développeur : « C'est une reproduction de calcul de l'analyse des auteurs … Ce n'est pas "notre chaîne voit sur notre modèle ce que d'autres ont vu" ». La colonne « Pourquoi le jury le demandera » promet plus que la pièce. À voir : un résultat sur notre modèle de 8 milliards, ou la phrase corrigée.
2. « chaque expérience décisive est scellée … puis jugée par un lecteur qui n'a rien écrit » (résultats v5, début). Vrai de l'auteur, mais les lecteurs sont de la même famille de modèles ; le dossier avoue ailleurs le biais commun. À voir : un lecteur humain ou d'une autre lignée sur au moins un verdict.
3. « contre-lues et vérifiées » (titre des sections de résultats v5). Les sections sont écrites au 10 novembre, avant les verdicts des barreaux 1 à 4. « Vérifiée » désigne la fidélité aux pièces de l'époque, pas l'exactitude du programme. À voir : mention de date plus visible, puis v6.
4. « une expérience préenregistrée dont l'issue est écrite d'avance dans les deux sens » (formule répétée). Le contraste à témoin apparié du barreau 5, ajouté à la porte du papier A le 18 novembre sur « accord de principe, énoncé non écrit », n'a pas d'issue écrite. L'étude de simulation « en rédaction », « aucune date ». À voir : l'énoncé écrit et scellé avant toute lecture.
5. « Le gonflement est établi » avec un facteur de l'ordre de 30 (résultats v5, § 1) et, deux lignes plus loin, un facteur écrit dans la consigne « environ 13 », alors que l'explication v5 écrit « facteur ≈ 3 » et que la prédiction écrite est « au plus ≈ 0,48 » en logarithme décimal (soit environ 3). Le « 13 » est sans doute une faute de frappe, mais l'écart de dix fois entre prédiction et mesure est exactement ce qu'un examinateur retient. À voir : une ligne qui explique l'écart (« cause non mesurée », dit le dossier) et corrige le chiffre.
6. « Trois lectures de sensibilité » du registre : la réfutation de quatre fourchettes manquées est laissée « hors compte » parce que leur « verdict propre » manque. À voir : le compte avec ces quatre dans la table principale, ou la raison de ne pas le faire en une phrase.
7. Table du registre : une ligne « Preuves vérifiées en simulation 31 / 0 / 0 » contribue pour près d'un tiers aux 96 « confirmées ». Elle est « attendue par construction » selon le verdict cité. À voir : le total présenté sans cette ligne en premier plan.
8. « Seule vérification possible sans nous » (preuve datée chez un tiers). Le tiers est privé ; ce que l'examinateur peut vérifier aujourd'hui est nul. À voir : dépôt public gelé, date de gel visible.
9. « Un lecteur neuf, non lu par la mère » (verdict de barreau 7 et ailleurs) : la mère ne lit pas les verdicts ; ce n'est pas une garantie pour l'examinateur, c'est une cloison. À voir : qui, hors de la chaîne Claude, a lu l'un de ces verdicts.
10. Fourchette M1 « 0,05 à 0,12 fausse alerte par épisode » (registre v3) et « ≈ 0,073 à 0,077 » (explication v5, ligne M1) : deux fourchettes pour la même prédiction, sans explication visible dans ce que je lis. À voir : laquelle est écrite avant, laquelle est une valeur de simulation.
11. « Autonomie de calcul jusqu'au 27 novembre, dans une enveloppe totale de 500 dollars » (résultats v5, § 4) alors que 645,42 dollars sont relevés au 8 novembre pour une phase précédente : la phrase ne dit pas ce qui est remis à zéro. À voir : un tableau de dépense par enveloppe, signé et daté.
12. « Hors des onze lignes … [DÉPENSES AU 22 — table régénérée par script] » : emplacement vide dans une pièce qui se présente comme état « au 18 au soir ». À voir : la table.
13. « Le programme ne peut pas promettre une réponse positive » : sain. Mais « Aucun run visant un signe positif » est contredit en esprit par la demande du 18 d'avoir « résultats prêts le 24 ou le 25 » (« ce qui manque » v3, priorités). À voir : une phrase qui sépare la contrainte de calendrier de la règle de neutralité.

## 3. Ce qui donne le plus confiance (à garder, à mettre en avant)

- La phrase d'ouverture, avant toute question : « aucune sonde n'a encore battu un surveillant de référence, et l'existence d'une trace interne du sabotage n'est pas établie ». Elle désarme.
- L'audit de la sonde trop bonne : la sonde apprise sur le saboteur le séparait presque parfaitement, l'audit a conclu à la lecture de la consigne, et le dossier le dit lui-même (résultats v5, § 1). C'est la preuve que la règle « trop beau = audit » est appliquée.
- La limite de l'adaptateur trouvée par l'équipe elle-même (§ 3) et déclarée avant l'entretien.
- Les corrections de ses propres erreurs envers le fonds (socle v5, § 1.7 ; résultats v5, § 7 : trois erreurs de fait à dire soi-même) et les contre-résultats publiés mis en avant contre soi (StateWitness, Gao, Corll, « Caught in the Act »).
- Le registre des prédictions avec ses réfutations (9 et 7), ses exceptions d'antériorité nommées, et « jamais seul » pour tout résultat de l'attaque.
- Le « non lu à temps » comme catégorie écrite, et les phrases gelées selon l'issue (« Rien de plus fort que la pièce »).
- La règle de la base « mots et coût » scellée à part avant la course, et la puissance écrite avant lecture.
- La théorie corrigée par simulation : un énoncé publié trouvé faux pour la somme, le théorème faux quand les actions sont dépendantes. C'est un résultat réel, petit, mais vérifiable.
- La gouvernance écrite de la dépense (plafonds, ordre d'abandon, arrêt par identifiant).

À mettre en avant dans cet ordre : la franchise d'ouverture, la sonde trop belle et son audit, la limite de l'adaptateur, les corrections adressées au fonds.

## 4. Les cinq manques qui pèsent le plus

1. **Aucune détection établie sur un sabotage vraiment diffus.** L'objet central de la thèse (barreau 8) est à l'état de texte scellé et d'addendum, sans course. Se comble par un résultat nouveau (la sortie scellée du barreau 8, même nulle, lue avec sa puissance) ; à défaut, par une phrase de limite honnête : « le diffus est une hypothèse de travail non encore mise en œuvre ».
2. **La sonde lit-elle le sabotage, l'intention, la consigne ou l'adaptateur ?** Le contrôle propre n'a « ni code ni course » et l'énoncé du remède n'est pas écrit au 18. Se comble par un résultat nouveau (le témoin honnête distillé et le contraste apparié, scellés avant lecture). Sans lui, aucun positif ne sera crédible et aucun négatif ne sera interprétable.
3. **Un dossier qui n'est pas un texte.** 164 pages, onze pièces écrites par des sessions différentes qui expliquent la même chose, deux époques (10 et 18 novembre), des états contradictoires (« en cours » devenu « verdict scellé »), « la version intégrée, un texte unique, reste à faire ». Se comble par une meilleure présentation de ce qui existe : une note intégrée de cinq pages, datée, avec une table « ce qui est lu / scellé / à venir / non lu à temps ».
4. **Indépendance de la vérification.** Auteurs, relecteurs, juges de verdicts : même famille de modèles, la mère étant tenue à l'écart des issues. Se comble par une phrase honnête de limite (« toute notre chaîne de vérification est une lignée ; voici ce que nous avons fait pour le compenser ») et, si possible, un geste simple : une relecture humaine externe d'un verdict ou d'une reproduction de calcul.
5. **Preuve de l'antériorité et comptabilité.** Le dépôt chez le tiers est privé et non gelé ; la dépense contient des lignes « inscrites après coup, sans facture rapprochée ». Se comble par un acte de procédure (dépôt public gelé après relecture) et par une meilleure présentation (une table de dépense régénérée, signée, avec la phrase « voici ce que nous ne savons pas »).

## 5. Note d'ensemble

**5 sur 10.** Comme examinateur, je donne 7 pour la rigueur et l'honnêteté de la méthode, 3 pour la preuve que « l'approche peut marcher » ; la moyenne tient compte d'un dossier lourd, daté de plusieurs époques, sans résultat central visible.

Ce qui ferait monter d'un point :
- **Un point** : une note intégrée de cinq pages, datée du jour, qui place en tête l'aveu d'ouverture, une table d'états unique, les trois contre-résultats publiés, et la phrase « voici ce que nous diront les expériences dans chacune des issues » ; avec la correction des incohérences relevées en section 2.
- **Deux points** : un résultat nouveau sur la question 2 (adaptateur contre sabotage), même défavorable, lu avec sa puissance.
- **Trois points et plus** : une lecture scellée sur un sabotage vraiment diffus, positive ou négative, avec la référence boîte noire de niveau « pointe » à côté.
