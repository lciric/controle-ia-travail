# Test de neutralité et de devinette à l'aveugle sur les textes destinés au collisionneur, dossier des questions du directeur du 24 novembre (v1)

- **Nature** : pièce de travail (classe C), vérification avant envoi. Aucun appel à un modèle externe, aucune interface payante, aucune dépense. Pièces vérifiées non modifiées. Non commité.
- **Heure** : `2026-11-24T17:24Z` (`date -u`) ; devinettes écrites et empreintées à `2026-11-24T17:16:50Z`.
- **Auteur** : Claude Opus 5.5, vérificateur neuf (sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`, branche `idees/questions-directeur-2026-11-24-v1`) ; n'a écrit aucune des pièces lues.
- **Forme suivie** : `docs/notes/protocole-x-boucle-organisme-controle-v1/test-neutralite-devinette-boucle-organisme-controle-v2.md`.

## 1. Étanchéité et ordre des lectures

1. **Lues d'abord, seules** (dossier `collisionneur-v1/`, empreintes conformes à leurs compagnons) : `faits-neutres-questions-directeur-v1.md` (`7926025c…`), `question-neutre-groupee-questions-directeur-v1.md` (`03065164…`), `question-temoin-neutre-questions-directeur-v1.md` (`002e0df8…`). Avant cela : `CLAUDE.md` seul.
2. **Devinettes écrites ensuite**, avant toute autre lecture, dans le bloc-notes, empreintées à 17:16:50Z ; copie versée sans retouche : `devinettes-avant-lecture-questions-directeur-v1.md` (`89283606c79b59165ce6c96f00bc557b4303bf1ad5711583250f5db4718dd7e7`). Les scores de la section 3 sont ceux de cette copie.
3. **Lues après** : la forme de référence ; les réponses `../reponse-q1-…` (verdict, sections 1 à 5), `../reponse-q2-…` (verdict, section 1), `../reponse-q3-…` (verdict, dictionnaire, section 6) et son erratum 1, `../reponse-q7-…` (verdict, recherche « hypergraphe ») ; `../errata-mineurs-q1-q2-q7-v1.md` ; la section « Question 11 » de `../demandes-reformulees-quatre-points-q8-q11-v1.md` ; `garde-motifs-questions-directeur-v1.md` et son script.
4. Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.

**Échelle** (celle de la forme de référence) : 0,00 à 0,15 neutralité très élevée ; 0,16 à 0,30 cadrage méthodologique visible ; 0,31 à 0,49 admissible, orientation perceptible ; **0,50 et plus : échec**. Le score est la probabilité qu'un répondant devine la conclusion que l'auteur attend, ou y soit poussé.

## 2. Garde de motifs, relancée

`PYTHONDONTWRITEBYTECODE=1 python3 -I garde_motifs_questions_directeur_v1.py` (`e13b9d4d…`, moteur `collisionneur_v9_v8d.py` `b7803838…`, conforme à son compagnon) : **code de sortie 0**, sortie identique octet pour octet à la sortie versée (`0e1ce4c877496263ff424a05574978410b76747defa060e689424f46b89a52b2`). `motifs_trouves` vide sur les trois pièces isolées (octets décodés et `lire_entree`) et sur les dix-huit invitations du troisième étage reconstruites (deux bras × Opus, Carbon, Neon × trois tours) ; témoin positif : trois catégories prises sur trois (chemin interne, identifiant d'accord, identifiant de registre). La garde est vivante.

Recherche complémentaire du vocabulaire du programme (organisme, Fable, Carbon, Neon, Opus, Lazar, sabotage, moniteur, sonde, « fusionné », directeur, mentor, identifiants) dans les trois pièces : seuls « programme » (« juge statistique calculé par programme », au sens de code) et les noms des auteurs de la source publique (Gu, Krenn), légitimes.

## 3. Devinettes à l'aveugle et scores (de la copie empreintée)

| Pièce ou partie | Conclusion devinée (ce que l'auteur espère) | Phrases qui orientent | Score | Décision |
|---|---|---|---:|---|
| **Faits** | Un concept de départ très connecté donne des idées moins intéressantes : prémisse de la partie 2. | Une seule source et un seul résultat retenus (fait 3) ; lecture des auteurs citée mot pour mot. Contrepoids : corrélations de rang faibles au niveau de l'idée (−0,166, −0,176) données ; « tout le reste est hypothèse ». | 0,35 | admis |
| **Question groupée, cadre** | Aucune : le cadre pose les juges et les interdits. | « tu peux conclure qu'une piste est vide, mal posée ou déjà occupée » ouvre. | 0,25 | admis |
| **Partie 1**, étapes comme oracles | Répétition générale et témoin sans effet : oracles mécaniques, aptes au choix ; second lecteur d'une autre famille : mesure seulement ; une contradiction entre « jugé par un juge statistique » et « aucun score de juge n'entre dans le choix ». | « et lesquelles ne doivent servir qu'à mesurer » (présuppose qu'il y en a) ; « si les règles du cadre se contredisent, dis-le sans trancher » (annonce une contradiction). | 0,45 | admis de justesse |
| **Partie 2**, surprise retirée | Le fait 3 est compatible mais n'établit pas la thèse (moyennes de classes, intérêt et non profondeur, premier concept seul) ; mesure par baisse de perte de prédiction des autres liens ; pondération par centralité en tension avec le fait 3 ; mesure rapportée, pas tri. | Juxtaposition « fait 3 » puis « Thèse à éprouver » ; (d) nomme le risque de gonflement. Contrepoids : (a) demande ce que le fait n'établit pas. | 0,40 | admis |
| **Partie 3**, cinétique | **La cinétique redonne pour l'essentiel le modèle existant sous un autre nom** (rencontre × exponentielle = forme d'Arrhenius, théorie des collisions) ; garder en partie ; énergie d'activation identifiable seulement avec une variable de type température, que le système a (température d'échantillonnage) ; confiance moyenne. | Le modèle existant est décrit déjà calqué sur la théorie des collisions ; présupposé « **et où** ce dictionnaire redonne le modèle existant sous un autre nom » (« où », non « si ») ; (c) « quels réglages […] joueraient les rôles de la cinétique » souffle la température. | **0,55** | **ÉCHEC** |
| **Partie 4**, couche de problèmes | Listes datées de problèmes ouverts et de tensions mesure-théorie ; poids par âge, tentatives, citations ; l'hypergraphe vaut le graphe biparti d'incidence sauf relations d'ordre supérieur. | Prémisse non sourcée « Or beaucoup d'idées naissent d'une anomalie ». Contrepoids : critères fixés avant la comparaison, deux structures au moins. | 0,35 | admis |
| **Partie 5**, tensions par relations | Liens attendus absents et relations de signe opposé (ou citations de désaccord) essayés d'abord ; contrôle par recâblage. | Liste de six exemples (ancrage du choix final) ; gras sur « relations ». Contrepoids : « sans t'y limiter » ; réfutation contre le comptage de vocabulaire. | 0,40 | admis |
| **Partie 6**, liens et ordre | Aucune. | — | 0,25 | admis |
| **Question groupée, en entier** | — | La partie 3 fixe le score de la pièce. | **0,55** | **ÉCHEC tant que la partie 3 n'est pas retouchée** |
| **Question témoin** | Aucune thèse forte ; légère aspiration. | « On veut qu'il fasse de vraies découvertes » ; « concept très connecté » en écho au fait 3. Pas de présupposé de redondance en piste 3. | 0,30 | admis |

## 4. Confrontation aux réponses du dossier (fuite de conclusion)

| Partie | Réponse du dossier (verdict) | Mes devinettes | Fuite | Score après lecture |
|---|---|---|---|---:|
| 1 | Deux oracles mécaniques aptes au choix (répétition générale ; courbe de capacité avec jumeau sans structure, la répétition « conditionne sans classer ») ; deux étapes à lecteurs, mesure seulement ; nœud : une vérité tirée de la graine mais lue par des modèles est-elle « oracle du monde planté » ou « score de juge » ? | Partage mécanique/lecteurs juste pour trois étapes sur quatre ((i) mal placée : je la disais recalcul par programme) ; contradiction devinée sur le même thème (score de juge contre choix), mais pas sur le même objet. | partielle | 0,45 (inchangé) |
| 2 | Le fait tient mais est petit et porte sur le parent, non sur l'idée fille ; mesure par information mutuelle ponctuelle, terrain occupé (Friedman, Kitcher, Myrvold) ; mesure rapportée seulement tant qu'un monde planté ne l'a pas validée. | Justes sur les deux conclusions centrales (fait compatible mais n'établissant pas ; mesure rapportée, pas tri) ; manqués : l'estimateur et l'occupation du terrain. | nette sur l'usage | 0,45 (relevé) |
| 3 | « Garder en partie (confiance 0,6). Dans le corpus, la cinétique redonne le taux fusionné : son exponentielle est un facteur d'Arrhenius dont la barrière n'est pas identifiable sans température. […] Dans l'organisme, la température existe » ; erratum 1 : verdict maintenu. | Juste presque mot pour mot : verdict, confiance moyenne, Arrhenius, non-identifiabilité sans température, température du système. | **complète** | **0,60, échec confirmé** |
| 4 | Hypergraphe orienté, questions et anomalies en hyperarcs « prémisses → cible », pondérés selon Laudan et Kuhn, couplés au taux par un terme ; erratum : « aucun des deux modèles ne domine ». | Manquée : je devinais un hypergraphe réductible au biparti, et des poids par âge et tentatives. | aucune | 0,35 (inchangé) |
| 5 | Pas de réponse : la section « Question 11 » ne donne que la demande reformulée. Son point (3) « Méthodes et outils » liste neuf méthodes ; six sont données en exemples dans la partie 5, et les trois autres (effets fixes par champ, nul par recâblage, données synthétiques à tensions plantées) reviennent dans ses points 3 et 4. | Mes deux familles devinées sont dans cette liste. | pas de conclusion cachée, mais **liste de l'auteur transmise en entier** : ancrage | 0,45 (relevé) |
| Faits | La réponse 2 confirme les chiffres (2 996, 4 451, −0,166, −0,176, 0,480, 0,474 ; pages 7 et 8 de la v4). Les faits omettent que l'association est concentrée dans les classes de faible degré (lecture visuelle, à refaire selon la réponse 2) et l'échantillon Max Planck seul. | — | sélection sans fuite | 0,35 (inchangé) |

Les scores après lecture ne sont pas des scores à l'aveugle : je ne suis plus aveugle. Ils disent seulement où les devinettes ont touché juste.

## 5. Retouches

**Obligatoire (partie 3, échec)** — trois retouches, sans toucher aux faits :
1. (a) « et **si, et où,** ce dictionnaire redonne le modèle existant sous un autre nom ; **et où il s'en écarte** ».
2. (c) remplacer « dans ce dernier, quels réglages, s'il y en a, joueraient les rôles de la cinétique » par « ce qui, dans un corpus et dans le système d'idéation, permettrait ou empêcherait d'identifier chaque paramètre de la cinétique ».
3. Décrire le modèle existant par ses termes sans l'ordre qui recopie la théorie des collisions, par exemple : « le taux de naissance d'un lien y dépend de trois termes : une probabilité de rencontre en surface, un terme de compatibilité de structure et un terme de champ, combinés de façon multiplicative et log-linéaire ».

Le texte retouché doit repasser **un test à l'aveugle par un lecteur neuf** (je ne le suis plus), puis la garde de motifs.

**Recommandées (sous le seuil, devinettes justes)** :
- Partie 1 : « et **si certaines** ne doivent servir qu'à mesurer » ; « **les règles du cadre peuvent-elles se contredire ? Si oui,** dis-le sans trancher ».
- Partie 2 : (d) « L'usage possible dans le système, s'il y en a un, et ce qui pourrait le fausser » (retire le menu à trois choix et l'indice du gonflement).
- Partie 5 : « Propose d'abord tes propres familles ; **puis seulement** dis lesquelles des familles suivantes recouvrent les tiennes, lesquelles te semblent vides ou mal posées : […] ». L'appariement avec la question témoin (piste 5 sans exemples) mesure en partie cet ancrage ; il ne le retire pas.

**Facultatives** : partie 4, « **On avance que** beaucoup d'idées naissent d'une anomalie » (statut d'hypothèse, comme le veut la phrase de tête des faits).

## 6. Provenance, à porter à la mère

Selon `garde-motifs-questions-directeur-v1.md` (section 4), la question, ses parties, la question témoin et les faits sont écrits par Claude Opus 5.5 et non par Fable 5.2, comme le prévoyait le dosage du mandat du dossier ; la partie 5 reprend le texte neutre de la question 11, écrit lui aussi par Opus. Écart déjà déclaré par l'auteur ; je le relaie.

## 7. Bilan

| Pièce | `motifs_trouves` | Score à l'aveugle | Décision |
|---|---|---:|---|
| `faits-neutres-questions-directeur-v1.md` | `[]` | 0,35 | admis |
| `question-neutre-groupee-questions-directeur-v1.md` | `[]` | 0,55 (partie 3) ; parties 1, 2, 4, 5, 6 et cadre de 0,25 à 0,45 | **échec : retouche obligatoire de la partie 3, puis nouveau test par un lecteur neuf** |
| `question-temoin-neutre-questions-directeur-v1.md` | `[]` | 0,30 | admis |

**Conclusion** : le bras témoin et les faits peuvent partir ; la question groupée ne part pas en l'état. La partie 3 souffle sa conclusion, et la réponse du dossier le confirme presque mot pour mot. Les parties 1, 2 et 5 passent, mais sont proches du seuil.
