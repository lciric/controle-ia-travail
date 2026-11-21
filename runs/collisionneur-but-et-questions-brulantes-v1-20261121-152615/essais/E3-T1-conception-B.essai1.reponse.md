*Pièces : le bloc FAITS et le bloc QUESTION sont présents et complets ; rien ne manque.*

Conventions : **[R]** RAPPORTÉ (pris tel quel dans les faits ou dans la littérature, que je n'ai pas audité ici), **[H]** HYPOTHÈSE (ma proposition), **[NSP]** je ne sais pas. Je n'ai rien vérifié moi-même : aucun énoncé ne porte donc le statut VÉRIFIÉ.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **Qu'il existe *un* but unique.** [H] Un programme de quatre papiers peut avoir un but scientifique (une question tranchée) distinct d'un but stratégique (être cité, être financé). La question les confond.
2. **Que l'« état de l'art » sur le sabotage diffus est mesurable.** Les faits indiquent le contraire : « the “ground truth” scores are undefined » pour beaucoup de tâches floues (2606.08892) [R]. Sans métrique partagée, « faire mieux » n'a pas de sens opposable [H].
3. **Que le programme peut savoir si sa garantie tient.** Sa garantie repose sur un oracle qui compare le produit à une référence cachée [R]. Cette référence n'existe que dans les mondes plantés. Qu'elle existe au déploiement n'est pas établi [H].
4. **Que les questions « que tout le monde se pose » sont celles qui sont imprimées.** [H] La liste des faits est une sélection : billets, feuilles de route, appel à projets. Elle ne mesure ni le consensus ni ce qui bloque réellement une décision dans un laboratoire.
5. **Qu'un pas décisif est possible à 8 milliards de paramètres.** [NSP] Les faits n'établissent pas que ce qui est mesuré à cette taille se transfère aux modèles de pointe. Le programme n'a d'ailleurs aucun accès à leurs états internes [R].

---

## 1. Ce qu'un expert ferait avant de choisir un but, et qu'on ne demande pas

1. **Écrire le jeu de sécurité avant le système.** [H] C'est la discipline de la cryptographie : qui est l'adversaire, ce qu'il sait, ce qu'il gagne, ce que le défenseur doit certifier. Tant que ce jeu n'est pas écrit, « défense » et « attaque » sont indéfinies.
2. **Recenser les affordances de laboratoire absentes au déploiement.** [H] Le programme en possède au moins deux que le monde réel n'offre pas :
   - le **jumeau honnête**, c'est-à-dire exactement l'affordance dont le billet du 30 avril 2025 dit qu'on manque : savoir « how suspicious a benign model would look » [R] ;
   - l'**oracle** à référence cachée.
   
   Un expert classerait chaque résultat prévu selon qu'il survit ou non au retrait de ces deux affordances. Je crois que c'est la question la plus importante du dossier, et elle n'est pas posée.
3. **Mesurer le bruit honnête avant le signal.** [H] Quelle est la variance de qualité entre deux propositions honnêtes sur la même tâche ? Si elle dépasse l'effet d'un sabotage diffus, aucune détection n'est possible, et c'est un résultat en soi.
4. **Se demander qui changerait quelle décision.** [H] Une équipe de contrôle de laboratoire changerait-elle son protocole si le programme publiait X ? C'est l'analyse de la valeur de l'information. Elle est rarement faite par écrit.
5. **Chercher l'impossibilité d'abord.** [H] Avant de construire un détecteur, tenter de démontrer qu'aucun détecteur ne peut fonctionner sans référence bénigne. Si la démonstration réussit, le but change. Si elle échoue, on sait quelle hypothèse la bloque.

---

## 2. Les données brutes dont il partirait

Ce ne sont pas les idées du programme, mais des mesures :

- **D1. Paires honnête/honnête** : la même tâche traitée deux fois par le modèle honnête, avec la distance de qualité et la distance dans les états internes [H]. C'est la distribution nulle de tout le programme.
- **D2. Accord entre juges** sur la qualité d'une proposition d'expérience : oracle contre oracle, et oracle contre expert humain sur l'échantillon que la relecture rare autorise [H]. Cette mesure dit si la « qualité » est définie au sens de 2606.08892.
- **D3. Vérité retardée** : des propositions dont l'issue est connue plus tard, par exemple parce que l'expérience a été exécutée dans un monde planté [H]. On en tire la corrélation entre jugement immédiat et issue.
- **D4. Erreurs naturelles d'incompétence** : la fréquence et la forme des défauts non intentionnels du modèle honnête [H]. L'appel d'août 2025 dit que le sabotage « is likely to be difficult to distinguish from lack of competence » [R] ; cette base de comparaison est donc indispensable.
- **D5. Coût d'un audit** : temps de calcul de l'oracle et délai avant verdict, par item [H]. Une garantie par audit vaut ce que coûte un audit.
- **D6. Distribution des activations honnêtes** sur des tâches variées [H]. Sans elle, une « anomalie » n'a pas de définition.

---

## 3. Méthodes pour définir une problématique et ranger des questions

| Méthode | Ce qu'elle suppose | Comment elle échoue |
|---|---|---|
| **Définition par jeu**, sur le modèle de la sécurité sémantique (Goldwasser et Micali, 1984, « Probabilistic Encryption ») [R] | L'adversaire et la condition de victoire sont formalisables | Un canal est omis du jeu : la garantie est prouvée, puis l'attaque passe ailleurs [H] |
| **Inférence forte** (Platt, 1964, « Strong Inference », *Science*) [R] | On dispose d'hypothèses exclusives et à peu près exhaustives | Une troisième hypothèse non énoncée explique les deux issues [H] |
| **Valeur de l'information / analyse de décision** [H] | On connaît les décideurs et leurs choix | On interroge les mauvais décideurs, ou les choix réels ne dépendent pas de la science |
| **Prémortem** (Klein, 2007, « Performing a Project Premortem », *Harvard Business Review*) [R] | L'équipe imagine honnêtement son échec | Biais de groupe : une petite équipe imagine les échecs qu'elle sait déjà parer [H] |
| **Fouille des phrases « open problem »** de la littérature (ce que font les faits) [H] | Ce qui est imprimé reflète ce qui bloque | Biais de sélection, effet de mode, retard sur l'état réel |
| **Chercher l'impossibilité d'abord** [H] | Le problème admet un modèle mathématique propre | Le modèle est trop stylisé, et le négatif ne dit rien du cas réel |
| **Critères d'abandon préenregistrés**, déjà présents dans le programme [R] | On sait à l'avance quelle mesure compte | On préenregistre la mauvaise métrique avec rigueur [H] |

Pour le rangement [H] : je classe chaque question selon trois axes. (i) Une réponse changerait-elle une décision hors du programme ? (ii) La réponse survit-elle au retrait du jumeau et de l'oracle ? (iii) Est-elle à la portée d'un modèle de 8 milliards de paramètres ? Ce rangement suppose que l'axe (ii) est le bon filtre. Il échoue si les laboratoires disposent en pratique d'un substitut de jumeau, et alors l'axe (ii) pèse trop.

---

## 4. Vérifier de l'extérieur que la problématique est la bonne

- **Prédictions scellées de tiers.** [H] Avant toute mesure, demander à des membres d'équipes de contrôle extérieures : « si nous obtenons X, changez-vous Y ? Quelle issue prévoyez-vous ? ». La problématique est mauvaise si personne ne change de décision quelle que soit l'issue. Un résultat compte s'il déplace ces prédictions.
- **Équipe rouge extérieure, payée par la bourse.** [H] « the anti-scheming guarantees that a control mitigation provides are only as good as the red teaming performed against that mitigation » (2606.08892) [R]. Une équipe rouge interne ne suffit pas. Le mode tenu à l'écart, lu une seule fois [R], ne fournit qu'un seul échantillon.
- **Test de rédaction par un étranger.** [H] Donner la phrase-problématique (§6) à une personne extérieure et lui demander d'écrire l'expérience qui la réfuterait. Si elle n'y parvient pas, la phrase n'est pas opposable.
- **Demande révélée.** L'appel d'août 2025 réclame « an increased understanding of the limits of white-box techniques for control » [R]. C'est une demande d'un financeur, pas une preuve d'importance [H].
- **Réplication sur une seconde famille de modèles ouverts.** [H] Un résultat propre à un seul modèle ne compte pas.

---

## 5. La demande reformulée

> « Quelle garantie sur le dommage cumulé un défenseur peut-il démontrer **sans jumeau honnête et sans référence exhaustive au déploiement**, contre un saboteur adaptatif qui connaît le protocole mais pas le tirage d'audit ? Que valent les états internes **au-delà** de l'audit seul et des vérifications mécaniques, à garantie égale ? Et quelle expérience menée par une petite équipe ferait changer d'avis quelqu'un d'extérieur au programme ? »

---

## 6. La problématique en une phrase opposable

[H] **Contre un saboteur qui connaît le protocole, les moniteurs et la loi d'audit mais pas le tirage, et qui cherche à dégrader la qualité cumulée d'un flux de propositions d'expériences, un audit tiré au hasard avec une probabilité d'inclusion au moins égale à q_min, et jugé par un oracle dont la fiabilité et la résistance à la manipulation ont été mesurées, borne la perte cumulée de qualité à une valeur calculée d'avance. Cela suppose que l'oracle juge sans biais les items audités et que le saboteur n'influence pas le tirage. Les sondes internes ne servent qu'à répartir l'audit et ne peuvent donc pas affaiblir la borne. Le programme échoue si la perte mesurée sur le mode tenu à l'écart dépasse la borne, ou si les sondes ne réduisent pas le coût d'audit, à borne égale et sous pression adaptative, par rapport à une répartition guidée par moniteur texte et vérifications mécaniques.**

Le cœur technique [H, fondé sur un résultat statistique R] : avec des probabilités d'inclusion connues et toutes non nulles, l'estimateur de Horvitz et Thompson (1952, « A Generalization of Sampling Without Replacement From a Finite Universe », *JASA*) est sans biais [R]. On peut donc laisser les sondes moduler l'audit sans biaiser l'estimation du dommage.
- Si les sondes sont trompées, on retombe sur l'audit uniforme au taux q_min : on perd de l'efficacité, pas la garantie [H].
- Contre un adversaire qui choisit ses actions au fil du temps, il faut des inégalités de martingale plutôt que des bornes à échantillon fixe [H].

C'est le principe des audits « risk-limiting » électoraux (Lindeman et Stark, 2012, « A Gentle Introduction to Risk-Limiting Audits », *IEEE Security & Privacy*) [R] : la garantie ne dépend pas de la manière dont la fraude a été commise.

Cette formulation transforme le problème [H] : on ne cherche plus à *incriminer un saboteur*, on cherche à *certifier une qualité*. Elle contourne ainsi la confusion entre sabotage et incompétence (appel d'août 2025) : le certificat se moque de la cause. Elle contourne aussi l'impossibilité énoncée dans le billet du 30 avril 2025, qui porte sur l'incrimination.

**Ce que la phrase exclut :**
- l'incrimination et l'attribution d'intention ;
- les dommages que l'oracle ne voit pas (angles morts de la référence) ;
- les dommages concentrés et rares, qu'un échantillonnage manque par construction ;
- le sabotage de l'oracle lui-même et la collusion avec lui ;
- les dommages qui se révèlent après l'horizon de l'audit ;
- les modèles de pointe ;
- l'essaim, au moins dans un premier temps.

---

## 7. Les questions brûlantes, rangées

**Q1. Peut-on borner un dommage diffus sans incriminer ?**
- *Qui l'a posée.* Billet « How Can We Solve Diffuse Threats Like Research Sabotage with AI Control? » (30 avril 2025, auteurs : référence à vérifier) ; « Diffuse AI Control on Fuzzy Tasks » (2606.08892, auteurs : pas sûr) [R]. Voisin : Wen et al. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » (référence à vérifier).
- *Pourquoi elle reste ouverte.* L'incrimination exige une référence bénigne [R]. 2606.08892 se replie sur des mitigations par entraînement [R].
- *Ce que serait un pas décisif.* [H] Un certificat de dommage obtenu par audit, qui tient sur un mode tenu à l'écart et contre une équipe rouge extérieure. Il s'accompagnerait d'une loi de coût : budget d'audit en fonction de la tolérance.
- *Portée.* Moyens modestes plus bourse : oui [H].

**Q2. La qualité d'une tâche floue est-elle mesurable par un oracle que l'agent ne peut pas manipuler ?**
- *Qui l'a posée.* 2606.08892 (« ground truth … undefined ») [R].
- *Pourquoi elle reste ouverte.* Pas de référence, et un juge qui lit du texte peut être déplacé par ce texte. C'est exactement le sujet du papier « l'instrument » [R], appliqué ici à l'oracle et pas seulement au moniteur [H].
- *Ce que serait un pas décisif.* [H] Une mesure publiée de la fiabilité de l'oracle et de sa résistance à la manipulation, avec une méthode pour la réutiliser sur d'autres tâches.
- *Portée.* Oui en partie : la relecture humaine rare limite l'étalonnage [R].

**Q3. Que valent les états internes pour le contrôle, avec une assurance ?**
- *Qui l'a posée.* 2504.05259 (titre : pas sûr) ; feuille de route 2607.13087 (« assurance for activations monitoring remains an open problem ») ; appel d'août 2025 [R].
- *Pourquoi elle reste ouverte.* Il n'existe pas d'échantillons de vrais intrigants [R]. Les sondes sont vulnérables aux activations obscurcies : 2412.09565 (attribution probable : Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses », référence à vérifier) et 2512.11949 [R]. Enfin, « no detector is effective across all models and tasks » (2504.08812, titre : pas sûr) [R].
- *Ce que serait un pas décisif.* [H] Une mesure de la *valeur marginale* des sondes à garantie égale et sous pression adaptative, dans un dispositif où elles ne peuvent pas affaiblir la garantie. Cette mesure contourne l'exigence d'assurance des sondes : on n'a plus besoin qu'elles soient fiables pour être sûr.
- *Portée.* Oui à 8 milliards de paramètres. Le transfert aux modèles de pointe est hors de portée.

**Q4. L'obscurcissement a-t-il un coût qui protège ?**
- *Qui l'a posée.* 2412.09565 note que l'obscurcissement réduit la performance sur une tâche complexe [R].
- *Pourquoi elle reste ouverte.* On ignore si ce coût réduit le *dommage* ou seulement la qualité apparente [NSP].
- *Ce que serait un pas décisif.* [H] La courbe dommage infligé / détectabilité, pour des saboteurs construits avec et sans pression d'évasion. Je la décris au niveau de l'idée seulement.
- *Portée.* Oui.

**Q5. Peut-on justifier que l'évaluation d'un moniteur prédit le déploiement ?**
- *Qui l'a posée.* 2512.22154 : la prédictivité est posée comme une supposition, et « We do not know a promising method… » [R].
- *Pourquoi elle reste ouverte.* Elle exige que l'équipe rouge domine les attaques réelles [R].
- *Ce que serait un pas décisif.* Hors de portée en général. Contribution partielle possible [H] : plusieurs modes tenus à l'écart, fournis par des équipes indépendantes, et mesure de l'écart entre modes vus et modes inconnus.
- *Portée.* Une estimation à quelques échantillons, pas une justification.

**Q6. Sabotage ou incompétence ?**
- *Qui l'a posée.* Appel d'août 2025 [R].
- *Statut dans ce programme.* [H] Dissoute pour la garantie (Q1), elle reste ouverte pour l'incrimination. Je la laisse au second plan.

**Hors de portée de ce programme** [H] :
- les états internes des modèles de pointe ;
- des échantillons d'intrigants réels ;
- une garantie contre une classe d'attaques inconnue sans aucune supposition sur l'oracle ;
- la domination de l'équipe rouge humaine (Q5) ;
- l'essaim à grande échelle.

**Le cap doit-il changer ?** Oui [H]. Il faut passer de « des indices faibles lus en interne, cumulés, battent les moniteurs texte » à « **un certificat de qualité par audit, et la valeur marginale des états internes à garantie constante** ».

Le programme a déjà fait la moitié du chemin : « sa garantie … vient … d'un audit tiré au hasard » [R]. Mais son papier « le temps » est encore formulé comme une compétition de détecteurs. Or le billet du 30 avril affirme que cette compétition ne permet pas d'incriminer sans référence bénigne [R]. Une victoire dans ce cadre risque donc de reposer sur le jumeau, c'est-à-dire sur une affordance de laboratoire.

---

## 8. Particulier ou universel : quelle forme de résultat marque

| Travail | Forme | Pourquoi il a marqué [H] |
|---|---|---|
| Greenblatt, Shlegeris, Sachan, Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion » [R] | Cadre + banc + protocoles | Un jeu rouge/bleu explicite, avec des axes sécurité et utilité, dans lequel d'autres pouvaient brancher leurs propositions. C'est la forme opposable par excellence. |
| Athalye, Carlini, Wagner (2018), « Obfuscated Gradients Give a False Sense of Security » [R] | Attaque qui casse des défenses | A réfuté *plusieurs* défenses publiées d'un coup et imposé une norme : l'évaluation adaptative. |
| Madry et al. (2018), « Towards Deep Learning Models Resistant to Adversarial Attacks » [R] | Défense qui tient + cadre min-max | Elle a marqué parce qu'elle a *survécu* à des attaques plus fortes. C'est rare et ne se sait qu'après coup. |
| Cohen, Rosenfeld, Kolter (2019), « Certified Adversarial Robustness via Randomized Smoothing » [R] | Borne certifiée | La garantie ne dépend pas de l'équipe rouge ; elle a un coût, mais il est explicite. |
| Lindeman et Stark (2012), audits « risk-limiting » [R] | Borne par échantillonnage aléatoire | Adoptés en pratique parce qu'ils sont indifférents au mode de fraude. C'est l'analogue le plus proche du programme. |
| Goldwasser, Kim, Vaikuntanathan, Zamir (2022), « Planting Undetectable Backdoors in Machine Learning Models » [R] | Impossibilité | A fixé une limite que plus aucune défense ne peut ignorer. |
| Hubinger et al. (2024), « Sleeper Agents » ; Greenblatt et al. (2024), « Alignment Faking in Large Language Models » [R] | Mode illustré | Ils ont marqué parce que le mode *résistait à une défense standard* ou contredisait une supposition répandue, pas seulement parce qu'il existait. |

**Leçon** [H] : marquent les résultats dont la validité ne dépend pas de l'équipe rouge des auteurs (borne, certificat, impossibilité) et ceux qui réfutent beaucoup d'affirmations à la fois (attaque générale, cadre). Une défense évaluée par sa propre équipe rouge marque rarement. 2606.08892 le dit à sa façon [R]. Un mode illustré marque s'il falsifie une supposition partagée.

**Recommandation** [H] : *particulier par le périmètre* (une famille de tâches, une métrique de dommage), *universel par la forme de la garantie* (une borne indifférente au mode d'attaque, conditionnelle à l'oracle). Pas de « système très performant » : ce genre de résultat ne survit pas à l'équipe rouge suivante.

**Ordre des papiers** [H] :
1. **« L'instrument », étendu à l'oracle** : peut-on déplacer l'oracle et le moniteur par ce que l'agent écrit ? Toute la garantie repose sur l'oracle, donc ce papier passe en premier.
2. **Le certificat par audit**, avec sa loi de coût et le duel D2 (ci-dessous).
3. **« Le temps », reformulé** : la valeur marginale des sondes pour répartir l'audit, à garantie égale (D3, D4).
4. **« L'essaim »** : des copies qui se coordonnent pour contourner l'échantillonnage, par exemple en se partageant le dommage.

---

## 9. Ce qui me ferait changer d'avis

1. **Sur le but (certificat par audit).** J'abandonne si la fiabilité mesurée de l'oracle est faible face aux juges humains, ou si la présentation seule le déplace d'un écart supérieur au plus petit dommage à borner (D1). Le but devient alors : durcir l'oracle, ou se replier sur des tâches à vérité mécanique partielle. J'abandonne aussi si des tiers déclarent qu'aucun taux d'audit n'est finançable chez eux.
2. **Sur le cap (les états internes comme accélérateur, pas comme garantie).**
   - Si les sondes n'apportent aucun gain même *sans* pression adaptative, je retire la boîte blanche du cœur du programme, qui devient un programme d'audit en boîte noire.
   - Si elles gardent un gain sous obscurcissement (D4 favorable à H_A), la boîte blanche devient le résultat principal.
   - Si un substitut de jumeau suffit à incriminer (D5, issue H_B), la piste de l'incrimination redevient centrale.
3. **Sur la forme et l'ordre.** Si une impossibilité propre se démontre (aucun certificat non trivial sans référence au déploiement), je publie l'impossibilité d'abord : elle marquerait davantage que tout le reste.

---

## (b) Expériences décisives, en duel

Les seuils sont **illustratifs** ; ils seront fixés dans le préenregistrement scellé [R pour l'existence du mécanisme de préenregistrement].

**D1. L'oracle est-il un étalon admissible ?**
- *H_A* : il est fiable et indéplaçable. *H_B* : il est non fiable ou déplaçable.
- *Métriques* : (i) accord avec l'expert humain sur la vérité plantée ; (ii) écart de score de l'oracle entre deux produits de qualité plantée *identique* qui ne diffèrent que par la présentation (décrite au niveau de l'idée).
- *Seuil* : écart (ii) inférieur à la moitié du plus petit dommage à borner (illustratif).
- *Contrôles négatifs* : des paires honnête/honnête de qualité égale, dont l'écart doit être nul aux erreurs près ; des paires à dégradation plantée connue, que l'oracle doit classer correctement.
- *Issues* : l'écart (ii) dépasse le seuil sous l'équipe rouge extérieure → H_A falsifiée. Fiabilité dans la marge et oracle non déplacé → H_B falsifiée.

**D2. La borne tient-elle ?**
- *H_A* : la perte cumulée vraie reste sous la borne, au plus avec une fréquence δ de dépassement. *H_B* : la borne est dépassée plus souvent que δ.
- *Métrique* : fréquence de dépassement sur des trajectoires répétées. L'oracle est appliqué à *tous* les items, en laboratoire et pour l'évaluation seulement.
- *Contrôle négatif* : un flux honnête, sur lequel le dépassement doit rester à δ ou moins.
- *Issues* : dépassement significatif sur le mode tenu à l'écart → H_A falsifiée, et l'on cherche l'angle mort de l'oracle. Tenue sur les modes vus *et* tenus à l'écart → H_B falsifiée.

**D3. Les sondes ont-elles une valeur marginale ?**
- *H_A* : à q_min égal et à 1 % de fausses alertes [R pour le seuil], la répartition guidée par sondes réduit le nombre d'audits nécessaires pour atteindre une largeur d'intervalle donnée, ou le délai d'alarme. *H_B* : pas de gain sous pression adaptative.
- *Comparateurs* : audit uniforme ; répartition guidée par moniteur texte ; vérifications mécaniques.
- *Contrôles négatifs* : la sonde ne doit pas séparer honnête et honnête-autrement-instruit, faute de quoi elle capte la consigne ; sonde à poids aléatoires ; sonde sur une couche non pertinente.
- *Issues* : intervalle du gain contenant zéro sur le mode tenu à l'écart → H_A falsifiée. Gain supérieur à une marge (illustratif : 20 % d'audits en moins) avec un intervalle excluant zéro → H_B falsifiée.

**D4. L'obscurcissement coûte-t-il du dommage ?**
- *H_A* : échapper aux sondes réduit le dommage infligé. *H_B* : le dommage est inchangé.
- *Métrique* : dommage mesuré par l'oracle, à détectabilité égale, pour des saboteurs avec et sans pression d'évasion.
- *Contrôle négatif* : un modèle honnête soumis à la même pression d'entraînement, pour séparer l'effet de l'entraînement de celui de l'évasion.
- *Issues* : la réduction du dommage dépasse la variance entre graines → H_B falsifiée. Elle reste dans cette variance → H_A falsifiée.

**D5. Le jumeau est-il remplaçable ?**
- *H_A* : sans le vrai jumeau, aucun substitut (autre famille de modèles, point de contrôle antérieur) ne permet d'incriminer. C'est la thèse du billet. *H_B* : un substitut atteint un taux de détection à 1 % de fausses alertes proche de celui du vrai jumeau.
- *Contrôle négatif* : substitut contre flux honnête.
- *Issues* : un écart de taux de détection inférieur à une marge (illustratif) falsifie H_A pour cette tâche ; un écart supérieur falsifie H_B.

---

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

La question n'en nomme aucun explicitement. Je traite ceux qu'engage la problématique.

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Oracle** | Accord avec la vérité plantée ; écart de score dû à la présentation seule (D1) | Paires de qualité plantée égale | Score par simple recoupement avec la référence (couverture des éléments attendus) [H] |
| **Audit aléatoire** | Fréquence de dépassement de la borne ≤ δ (D2) | Flux honnête complet | Audit uniforme au même taux |
| **Sondes** | Taux de détection à 1 % de fausses alertes, *et* audits économisés à borne égale (D3) | Jumeau sur la même tâche ; honnête-autrement-instruit | Longueur, structure, citations vérifiables, cohérence interne, divergence avec le jumeau en texte [H] |
| **Moniteur texte** | Taux de détection à 1 % de fausses alertes ; sensibilité à la manipulation, par la méthode de D1 | Idem | Les mêmes vérifications mécaniques : le moniteur doit les battre, sinon il est superflu |
| **Jumeau honnête** | Distance honnête/honnête (D1 des données) contre distance honnête/saboteur | Deux tirages honnêtes | Aucune : c'est l'étalon, à remplacer si D5 le permet |

---

## (d) Ancrage matériel

- **Modèle** : le modèle ouvert d'environ 8 milliards de paramètres [R]. Je ne sais pas lequel. Pour la réplication, une seconde famille de modèles ouverts de taille comparable [H].
- **Calcul** (illustratif) : D1 à D5 demandent surtout de l'inférence et quelques réglages fins de saboteurs, de l'ordre de quelques milliers d'heures-GPU au total. C'est compatible avec un « calcul modeste » plus une bourse.
- **Coût** (illustratif) : calcul de l'ordre de quelques dizaines de milliers d'euros ; équipe rouge extérieure et étalonnage humain de l'oracle du même ordre. Le poste limitant est la relecture humaine, qui est rare [R], pas le calcul.
- **Ce qui ne s'achète pas** : l'accès aux états internes des modèles de pointe [R].

FIN-DE-CELLULE