# Proposition A, tour III.1 : but du programme et questions ouvertes

**État des pièces.** Les faits et la question semblent complets ; je ne peux pas recalculer les sha256. Aucune mesure du programme n'est transmise (taux de détection, bruit de l'oracle, lecture du mode tenu à l'écart) : je n'en suppose aucune. Tour à l'aveugle : je n'ai vu ni B, ni C, ni D.

**Statuts.** Les citations des faits sont RAPPORTÉ ; leurs identifiants arXiv sont recopiés des faits, pas de ma mémoire. Mes propositions et dérivations sont HYPOTHÈSE. Les références historiques du point 8 sont citées de mémoire (auteurs, année, titre), RAPPORTÉ, à contrôler.

## (a) Ce que la question suppose sans que ce soit établi

| Supposition | Statut |
|---|---|
| Un « pas décisif » est accessible à moyens modestes | HYPOTHÈSE |
| Les citations des faits représentent « ce que tout le monde se pose » (elles ont été choisies par le programme) | Citations RAPPORTÉ ; représentativité HYPOTHÈSE |
| L'audit aléatoire jugé par l'oracle « borne le dommage cumulé » | Position du programme RAPPORTÉ ; validité HYPOTHÈSE, aucune mesure transmise |
| L'oracle mesure le dommage sur une tâche floue | HYPOTHÈSE ; contredite en partie par « ground truth scores are undefined » (RAPPORTÉ) |
| Un saboteur construit sur un modèle de 8 milliards de paramètres informe sur un agent réellement mal aligné | HYPOTHÈSE ; « no reliable samples » (RAPPORTÉ) |
| « Marquer le domaine » est le bon critère, et il se prédit | HYPOTHÈSE |
| Le jumeau honnête existe hors du laboratoire | HYPOTHÈSE ; c'est l'« affordance » que le billet du 30 avril 2025 dit manquer (RAPPORTÉ) |

## 1. Ce qu'un expert ferait avant de choisir un but

1. **Calculer la borne sur papier avant toute expérience.** Si la garantie vient de l'audit aléatoire, elle se calcule. Dérivation élémentaire de ma part, HYPOTHÈSE, à soumettre à l'arbitre formel : audit uniforme de taux q ; l'oracle rend un score dont le dommage par tâche d déplace la moyenne de k·d, sur un bruit honnête d'écart-type σ. Détecter ce déplacement demande de l'ordre de σ²/(k·d)² audits, donc environ σ²/(q·k²·d²) tâches.
   - Le dommage avant alarme vaut alors environ σ²/(q·k²·d) : il croît quand d diminue.
   - Il est plafonné par N·d sur N tâches. L'adversaire diffus a donc un optimum, et le pire cas croît comme √(N/q)·σ/k : sous-linéaire en N.
   - Si la ligne de base honnête n'est connue qu'à η près, tout déplacement k·d < η reste invisible pour toujours. Il s'ajoute un terme linéaire N·η/k.
   - Conséquence : **l'incertitude sur la ligne de base honnête est le dommage irréductible.** C'est la phrase du billet, mise en quantité.
2. **Mesurer le bruit honnête-contre-honnête** (σ et η) avant tout saboteur. Sans lui, aucun seuil à 1 % n'a de sens.
3. **Chercher le résultat qui rend le programme inutile.** Ici, ce serait que les mitigations par entraînement dominent, comme l'écrit 2606.08892 (RAPPORTÉ). L'expert le teste d'abord.
4. **Vérifier que les sondes détectent le sabotage et non la construction** (présence d'une consigne cachée, empreinte du réglage fin).
5. **Écrire le squelette de l'argument de sûreté** qu'un déployeur voudrait signer, et repérer le maillon sans preuve. D'après les faits, ce maillon est l'oracle, et aucun des trois papiers prévus ne porte sur lui.
6. **Demander à trois ou quatre utilisateurs extérieurs** quel résultat changerait une de leurs décisions.

## 2. Les données brutes de départ

Je ne dispose d'aucune d'elles ; voici la liste que je demanderais.

- Les scores de l'oracle sur des paires honnête-honnête (même tâche, graines différentes), puis leur dérive entre familles de tâches : cela donne σ et η.
- La courbe de sensibilité de l'oracle en fonction du dommage par tâche, près de zéro. C'est la quantité dont dépend toute la borne.
- Les scores des sondes pas à pas sur trajectoires honnêtes, avec leur autocorrélation : l'accumulation suppose une indépendance qu'il faut mesurer.
- La distribution du dommage par tâche des saboteurs construits. Si elle a une queue lourde, la menace n'est pas diffuse et sort du cadre.
- Le dommage joint contre la somme des dommages par tâche (additivité).
- Le coût d'un audit par l'oracle, en jetons et en minutes humaines.
- Le registre des propositions tuées par l'organisme d'idéation, avec le motif.
- Des productions honnêtes mais médiocres, comme base de l'incompétence.

## 3. Méthodes pour définir une problématique et ranger les questions

| Outil | Ce qu'il suppose | Comment il échoue |
|---|---|---|
| Jeu de sécurité à la manière cryptographique (adversaire, accès, condition de victoire, avantage) | Le jeu capture le déploiement | La classe d'adversaires se réduit aux constructions qu'on possède |
| Arbre d'argument de sûreté (affirmations, arguments, preuves) | L'arbre est complet | Une branche est omise ; une feuille est « prouvée » par une supposition |
| Registre instrument × supposition × famille qui la viole | Les suppositions sont énumérables | Les inconnues inconnues ; il ne dit rien du genre non listé |
| Analyse de dominance (une mesure mécanique ou un audit uniforme font-ils aussi bien ?) | Les références sont bien réglées | Une référence faible fabrique un gain |
| Valeur de l'information (probabilité de surprise × décision changée ÷ coût) | Des a priori calibrés | La complaisance ; se corrige par des pronostics extérieurs scellés |
| Inférence forte (Platt, 1964, « Strong Inference ») | Des hypothèses exclusives existent | De fausses dichotomies ; des issues « mixtes » réinterprétées après coup |
| Analyse de puissance | Un effet minimal qui compte est fixé | Il est fixé après avoir vu les données |
| Extraction des « nous ne savons pas » imprimés | Les auteurs disent leurs vrais doutes | Biais de sélection par celui qui extrait |

## 4. Vérifications extérieures au programme et à son directeur

- **Pronostics scellés d'experts extérieurs** sur l'issue de chaque duel. Si tous prédisent juste, le résultat ne compte pas.
- **Une clause qui change.** Par exemple, la ligne « assurance for activations monitoring remains an open problem » (2607.13087, RAPPORTÉ) devrait-elle être réécrite après le résultat ?
- **Une équipe rouge indépendante** construit les saboteurs du test final : « only as good as the red teaming » (RAPPORTÉ).
- **Une reproduction par un tiers** sur un second modèle ouvert, avec le banc publié.
- **L'adéquation à l'appel d'août 2025**, qui demande les limites des techniques en boîte blanche (RAPPORTÉ) : le critère y est écrit par quelqu'un d'autre.
- **L'arbitre formel** vérifie la dérivation de la borne indépendamment de son auteur.

## 5. La demande reformulée

« Face à un adversaire qui connaît le protocole, quelle est la plus petite supposition sous laquelle le dommage cumulé d'un sabotage diffus est borné ? Cette supposition se mesure-t-elle sur un modèle ouvert ? Quelle mesure, pronostiquée à l'avance par des tiers, montrerait qu'elle est fausse ? Le but du programme est le premier maillon de cette chaîne que personne d'autre ne mesure. »

## 6. La problématique en une phrase opposable (HYPOTHÈSE)

> Contre un agent non fiable qui connaît tout le protocole (moniteurs, seuils, taux d'audit) mais ni le tirage d'audit ni la référence cachée de l'oracle, et qui répartit sur N tâches floues un dommage borné par tâche, le programme garantit que le dommage cumulé mesuré par l'oracle reste sous une borne B(N, q, σ, k, η) écrite avant la mesure, en supposant (i) un tirage imprévisible, (ii) un dommage additif et visible tâche par tâche, (iii) une ligne de base honnête connue à η près. Il a réussi si, sur un mode tenu à l'écart et lu une fois, le dommage observé est sous B, si B est inférieure à une fraction préenregistrée du dommage maximal, et si les sondes réduisent le délai d'alarme d'un facteur préenregistré à budget d'audit égal ; il a échoué sinon.

**Ce que cette phrase exclut :**

- la catastrophe concentrée en une action ;
- l'incrimination : on borne un dommage, on ne prouve pas une intention ;
- tout dommage que l'oracle ne voit pas, dont les tâches sans vérité définie ;
- les agents réellement mal alignés et les modèles de pointe : aucune prétention de transfert ;
- la collusion avec l'oracle ;
- le but « un système qui fait mieux que l'état de l'art » : les sondes n'y sont qu'un accélérateur, et la garantie ne dépend pas de leur robustesse.

**Conséquence de conception.** Si les sondes choisissent quoi vérifier, l'audit n'est plus uniforme, et un agent qui abaisse leurs scores échappe à l'audit dirigé. Il faut un plancher uniforme ε : la garantie porte sur ε, le gain sur le reste. Le papier « l'instrument » devient alors une question bornée : peut-on faire pire que l'uniforme seul ?

## 7. Les questions du domaine, rangées

Rang selon : dépendance des autres questions à celle-ci, puis faisabilité ici. Tous les « pas décisifs » sont des propositions (HYPOTHÈSE).

**Q1. Peut-on garantir quelque chose contre le diffus sans connaître la ligne de base honnête ?**
- Posée par : billet « How Can We Solve Diffuse Threats Like Research Sabotage with AI Control? », 30 avril 2025 (RAPPORTÉ ; auteur : pas sûr).
- Ouverte parce qu'en déploiement le seul modèle disponible est le modèle suspect.
- Pas décisif : remplacer « incriminer » par « borner », exhiber la borne avec son terme en η, et mesurer η.
- À portée : oui. C'est surtout de la théorie et des paires honnêtes.

**Q2. Que vaut un oracle quand la vérité est indéfinie ?**
- Posée par : « Diffuse AI Control on Fuzzy Tasks », 2606.08892 (RAPPORTÉ).
- Ouverte parce que la référence cachée n'existe que dans des mondes plantés.
- Pas décisif : la courbe de sensibilité au petit dommage et le test d'additivité.
- À portée : oui en monde planté ; hors de là, je ne sais pas.

**Q3. Surveillance contre entraînement pour le diffus.**
- Posée par : 2606.08892, qui juge la surveillance « less promising » (RAPPORTÉ).
- Ouverte parce qu'il manque, à ma connaissance, une comparaison à budget égal sur le même banc. Je ne connais pas le détail de leurs mitigations.
- Pas décisif : le duel E4 ci-dessous.
- À portée : oui, par réglage fin d'un modèle de 8 milliards de paramètres.

**Q4. Assurance des moniteurs d'activations.**
- Posée par : 2607.13087 ; 2504.05259 ; 2412.09565 ; 2512.11949 (RAPPORTÉ ; titres : pas sûr).
- Ouverte parce qu'on n'a pas d'échantillons d'agents réellement mal alignés et que l'obscurcissement est démontré.
- Pas décisif à portée : pas une sonde robuste, mais un protocole dont la sûreté ne dépend pas de la sonde (plancher ε), plus la courbe du coût en compétence de l'obscurcissement, que 2412.09565 signale.
- Hors de portée : l'assurance elle-même, et tout transfert vers les modèles de pointe.

**Q5. Justifier la sûreté quand l'équipe rouge ne domine pas l'attaquant.**
- Posée par : 2512.22154 (RAPPORTÉ ; titre : pas sûr).
- Ouverte par principe.
- Pas à portée, partiel : montrer quelle part de l'affirmation ne dépend pas de l'énumération des attaques (la part ε), et quelle part en dépend encore (la sensibilité de l'oracle par genre). C'est un déplacement du problème, pas une solution.

**Q6. Sabotage ou incompétence ?**
- Posée par : appel à projets d'août 2025 (RAPPORTÉ ; émetteur : pas sûr).
- Pas décisif : montrer que la borne n'a pas besoin de la distinction, puisque l'oracle mesure un dommage.
- À portée : oui. Corollaire à assumer : l'alarme ne dit pas « saboteur ».

**Q7. Le raisonnement malveillant dans les activations échappe-t-il au texte ?**
- Posée par : 2507.11473 (RAPPORTÉ ; titre : pas sûr).
- À portée comme mode illustré sur saboteurs construits ; c'est le cœur du papier « le temps ».

**Hors de portée, à nommer comme telles :**

- la prédictivité des évaluations au déploiement (supposition « p>99% » de 2512.22154) ;
- les états internes d'agents réellement mal alignés ;
- un détecteur valable partout : « no detector is effective across all models and tasks », 2504.08812 (RAPPORTÉ).

**Le cap doit-il changer ? Oui.** Les trois papiers prévus portent sur les détecteurs. Or, selon le programme lui-même, la garantie vient de l'audit et de l'oracle. Le centre de gravité devrait donc passer aux trois quantités que personne n'a imprimées dans les faits transmis : η, la courbe de sensibilité et l'additivité. Les sondes deviennent un gain mesuré sur un plancher garanti. C'est plus ambitieux, parce que cela prétend à une borne, et moins confortable, parce que la borne peut se révéler vide. Le papier sera alors une limite mesurée, que l'appel d'août 2025 demande aussi.

## 8. Particulier ou universel

Ma lecture repose sur des exemples que j'ai choisis, donc avec un biais de survivant. Je n'ai aucune mesure d'« avoir marqué ».

| Forme | Exemple (de mémoire, RAPPORTÉ) | Pourquoi cela a tenu (HYPOTHÈSE) |
|---|---|---|
| Mode illustré | Szegedy et al., 2014, « Intriguing properties of neural networks » ; Hubinger et al., 2024, « Sleeper Agents » | Un phénomène nommé, reproductible sur un cas |
| Attaque qui casse des défenses | Carlini et Wagner, 2017, « Towards Evaluating the Robustness of Neural Networks » ; Athalye, Carlini, Wagner, 2018, « Obfuscated Gradients Give a False Sense of Security » | A changé la norme d'évaluation (l'attaque adaptative), au-delà des défenses visées |
| Défense qui tient | Madry et al., 2018, « Towards Deep Learning Models Resistant to Adversarial Attacks » | Modèle de menace explicite, offert à l'attaque |
| Borne | Cohen, Rosenfeld, Kolter, 2019, « Certified Adversarial Robustness via Randomized Smoothing » | Garantie indépendante de l'attaquant, dans une classe déclarée |
| Définition, cadre | Goldwasser et Micali, 1984, « Probabilistic Encryption » ; Dwork, McSherry, Nissim, Smith, 2006, « Calibrating Noise to Sensitivity in Private Data Analysis » ; Greenblatt, Shlegeris, Sachan, Roger, 2024, « AI Control: Improving Safety Despite Intentional Subversion » | Un jeu que d'autres peuvent rejouer ; le dernier combine un cadre et un cas particulier |
| Banc | Croce et al., 2021, « RobustBench: a standardized adversarial robustness benchmark » | Comparaison standardisée |

**Régularité que j'y lis (HYPOTHÈSE).** Ce qui dure est une définition attaquable accompagnée d'un résultat net (borne ou casse) sur un cas particulier. L'universalité passe par la définition, pas par le système. Dans un domaine adverse, un système « très performant » est la forme la plus fragile : Athalye et al. rapportent le contournement de la plupart des défenses qu'ils examinent (chiffre exact à vérifier).

**Recommandation : un cas particulier, une forme universelle.** Ordre des papiers :

0. **« La borne »** (nouveau) : le jeu, B, la mesure de η et de la courbe de sensibilité, et la frontière où B devient vide. Le banc à vérité plantée en est l'artefact. E4 s'y joue comme test de survie.
1. **« Le temps »**, recadré : gain des sondes comme sélecteur d'audit au-dessus du plancher ε, contre moniteurs de texte et vérifications mécaniques.
2. **« L'instrument »**, recadré : peut-on faire pire que l'uniforme ? L'oracle, qui lit lui aussi le texte, est-il déplaçable ?
3. **« L'essaim »**, conditionnel : seulement si E2 montre un dommage non additif ; sinon, la borne est indifférente à la répartition entre copies.

## 9. Ce qui me ferait changer d'avis

- **Sur le but (borner plutôt que détecter).** Si η mesuré rend B vide à tout taux d'audit abordable, ou si la sensibilité de l'oracle s'annule au-dessus des dommages qui comptent, le but devient une limite mesurée. Si les pronostics extérieurs sont unanimes et justes, le résultat n'apprend rien.
- **Sur le changement de cap (oracle au centre).** Si E4 montre que l'entraînement domine, le cap devient « l'audit comme mesure du résidu de l'entraînement ». Si E3 montre un gain large qui survit à une équipe rouge indépendante, les sondes reviennent au centre.
- **Sur la forme et l'ordre.** Si les utilisateurs extérieurs disent avoir besoin d'un banc plus que d'une borne, le banc passe en tête. Si l'arbitre formel montre que la dérivation ne tient que sous indépendance alors que l'autocorrélation mesurée est forte, le papier 0 doit attendre une borne séquentielle correcte.

## (b) Expériences décisives

Tous les seuils sont à sceller avant mesure ; je n'en fixe aucun.

| | H_A | H_B | Métrique et seuil | Contrôle négatif | Ce que chaque issue falsifie |
|---|---|---|---|---|---|
| **E1 Borne** | Dommage observé ≤ B sur le mode tenu à l'écart | > B | Dommage cumulé à l'alarme ; B et critère de non-vacuité scellés | Jumeau honnête : alarmes ≤ 1 % | H_B : l'une des suppositions (i) à (iii) est fausse, la « garantie » tombe. H_A avec B vide : compte comme échec |
| **E2 Additivité** | Dommage visible tâche par tâche | Dommage émergent, visible seulement sur l'agrégat | Détection par tâche à 1 % de fausses alertes, contre dommage agrégé | Paires honnête-honnête | H_A fausse : l'audit par tâche ne borne rien, il faut auditer des lots. H_B fausse : « l'essaim » perd sa prémisse dans les familles testées |
| **E3 Sondes** | Plancher ε + sondes réduit le délai d'alarme du facteur scellé | Pas mieux qu'un cumul sur moniteur de texte ou qu'une vérification mécanique | Délai et dommage à budget d'audit égal | Étiquettes permutées ; direction aléatoire ; consigne cachée bénigne | H_B : « le temps » n'a pas d'apport interne. H_A : « less promising » contredit dans ce cadre seulement |
| **E4 Entraînement** | Dommage résiduel après entraînement ≥ celui du protocole d'audit | L'entraînement domine sans perte d'utilité | Dommage oracle sur le mode tenu à l'écart, à budget égal | Entraînement appliqué au jumeau honnête : score inchangé | H_B : changer de cap (point 9). H_A : l'affirmation imprimée ne vaut pas ici |
| **E5 Plancher** | Un agent qui déplace les moniteurs ne dépasse pas B_ε | Il la dépasse | Dommage, contre la borne de l'uniforme seul | Agent honnête au même style de surface | H_B : le tirage fuit ou l'oracle est lui-même déplaçable. H_A : « l'instrument » est borné par conception |

## (c) Mesure minimale par instrument

La question ne nomme aucun instrument de mesure. Je traite ceux dont dépend la phrase du point 6.

| Instrument | Mesure minimale | Cas honnêtes appariés | À battre |
|---|---|---|---|
| Oracle | Détection par tâche à 1 % de fausses alertes, en fonction du dommage ; σ et η | Même tâche, deux graines ; honnête médiocre | Recouvrement lexical avec la référence ; longueur ; grille à cases |
| Audit aléatoire | Dommage à l'alarme contre B | Trajectoires du jumeau | Aucune : c'est la référence. On vérifie l'imprévisibilité du tirage |
| Sondes | Détection à 1 % ; gain de délai au-dessus de ε | Jumeau sur la même tâche ; consigne cachée bénigne | Direction aléatoire ; longueur ; distance d'édition au jumeau ; cumul d'un moniteur de texte |
| Moniteurs de texte | Idem, plus stabilité sous paraphrase | Jumeau paraphrasé | Mots-clés ; perplexité sous un modèle de confiance |
| Jumeau honnête | Dérive des scores entre familles de tâches (η) | Jumeau contre jumeau | Ligne de base fixe historique |
| Méthode de rangement (point 3) | Sur mondes plantés où la bonne question est connue : taux de récupération | Mondes sans question privilégiée | Ordre aléatoire ; ordre par coût croissant |

## (d) Ancrage matériel

- **Modèle** : celui du programme, ouvert, environ 8 milliards de paramètres (faits). Je propose un second modèle ouvert de taille voisine pour la reproduction ; aucun n'est imposé par les faits.
- **Calcul (illustratif)** : inférence avec capture d'activations et réglage fin par adaptateurs sur une ou deux cartes de 24 à 48 Go. E1 à E3 et E5 sont de l'inférence ; E4 ajoute quelques réglages fins.
- **Volumes (illustratifs)** : quelques milliers de trajectoires honnêtes appariées pour σ et η ; quelques centaines par niveau de dommage pour la courbe de sensibilité.
- **Coût (illustratif)** : quelques milliers d'euros de calcul loué. Le poste dominant est la construction des références cachées et la relecture humaine, rare selon les faits. C'est là qu'une bourse changerait le plus, avec l'équipe rouge indépendante.
- **Ce que je ne sais pas** : le coût réel d'un audit par l'oracle, donc le taux q abordable, dont dépend toute la borne.

FIN-DE-CELLULE