# Proposition A — Tour III.1

## État des pièces

- Les blocs FAITS et QUESTION sont identiques mot pour mot : aucun fait distinct de la question n'est transmis, et aucun énoncé ne porte d'étiquette de statut. Ce que la pièce dit « rapporté », je le traite comme RAPPORTÉ, sans le relever.
- Les « travaux de 2026 » sont cités sans auteurs ni titre : référence à vérifier. Je ne les attribue pas et n'en reconstitue pas la méthode.
- Aucune proposition B à F n'est visible à ce tour : la règle B1 est sans objet ici.
- Tous les chiffres ci-dessous sont illustratifs, sauf le nombre de tâches (six, tiré des faits) et les dénombrements qui en découlent.

## Point 0 — Une expérience peut-elle départager A et B ?

**Oui pour les prédictions, non pour leur interprétation.**

Les deux prédictions sont exclusives et chiffrables : A annonce un profil propre aux directions, B le même profil sous un témoin à dégradation globale égale. Une expérience les départage si le seuil de différence, la marge d'équivalence et les témoins sont fixés avant la mesure.

Aucune expérience de ce type ne tranche en revanche deux thèses :
- celle de B, selon laquelle un réseau sans mécanisme d'éveil n'a pas d'état à perdre ;
- la lecture de A, selon laquelle un profil propre serait un analogue de l'anesthésie au sens qui intéresse la conscience.

Ces thèses portent sur ce que le profil signifie, pas sur sa valeur. Je traite donc les points 1 à 3 pour la partie empirique.

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|---|---|
| 1 | Les directions existent et leur suppression produit la dissociation décrite. | RAPPORTÉ par la pièce, source non identifiée, non audité ici |
| 2 | La dissociation ne vient pas d'une fragilité inégale des tâches (sortie longue, marge de décision faible, calcul en série). | HYPOTHÈSE ; c'est l'enjeu du duel |
| 3 | « Dégradation globale égale » se résume à un scalaire unique. | HYPOTHÈSE ; le choix de la métrique d'appariement peut inverser la conclusion |
| 4 | Un témoin neutre existe. | HYPOTHÈSE ; la famille de témoins est un degré de liberté |
| 5 | Les directions n'ont pas été choisies sur le profil qu'elles doivent prouver. | HYPOTHÈSE ; procédure de sélection non transmise |
| 6 | L'échelle humaine est graduée et à une seule dimension. | HYPOTHÈSE ; la littérature dont je me souviens rapporte des dissociations qui s'y opposent |
| 7 | Les six tâches se projettent sur les fonctions humaines perdues ou gardées. | HYPOTHÈSE ; aucune table de correspondance n'est fournie |
| 8 | A et B épuisent les cas. | HYPOTHÈSE, que je crois fausse : un profil propre peut être fabriqué par la procédure, ou relever d'une lésion sans régime |
| 9 | L'absence d'activité autonome implique qu'il n'y a pas d'état à perdre. | Prémisse RAPPORTÉE par la pièce ; conséquence HYPOTHÈSE, non mesurable par ce plan |
| 10 | Le rapport du sujet a un équivalent chez le modèle. | HYPOTHÈSE ; aucun instrument validé à ma connaissance |

## Point 1 — Un « état analogue à l'anesthésie » a-t-il un sens ?

**Oui au sens opératoire, non au sens fort.** Pour le sens fort, il manque un pôle « éveillé » établi indépendamment de la mesure, et une variable de niveau distincte du contenu. Sans eux, le mot ne désigne qu'un profil.

Définition opératoire (HYPOTHÈSE de travail, la mienne) : un **régime de dissociation spécifique**.

- **Intervention.** Aux couches choisies du flux résiduel, la composante de l'activation dans le sous-espace U (dimension k) est remplacée par sa moyenne sur un corpus de référence. La dose α va de 0 (modèle intact) à 1, sans unité.
- **Dose commune D.** Divergence KL moyenne entre les distributions de sortie intacte et perturbée sur un corpus neutre, en nats par token. Valeur nulle : 0.
- **Performance retenue r_t.** Pour chaque tâche, (score − plancher) / (score intact − plancher), sans unité ; 1 = intact, 0 = hasard.
- **Sélectivité S.** Moyenne des r_t des trois tâches dites gardées, moins celle des trois dites perdues.
- **Écart au témoin ΔS.** S(directions) − S(témoin) à D égal. Valeur nulle : 0.

Quatre critères :
1. ΔS dépasse le seuil contre tous les témoins.
2. L'ordre de perte est reproductible quand D croît, et diffère de l'ordre observé sous témoin.
3. Le profil se transfère à des tâches hors liste classées à l'avance.
4. Le profil est le même d'un domaine et d'une langue à l'autre.

Un tel régime est un fait sur le modèle. Ce n'est pas un état d'inconscience.

## (b) Expériences décisives (point 2)

### Dispositif commun

- **Sélection des tâches.** Une tâche n'est retenue que si son score intact se situe entre 70 % et 95 % (illustratif) ; la règle s'applique avant toute ablation.
- **Format.** Les six tâches des faits sont posées en choix forcé (quatre options, réponse en un token) pour égaliser la longueur de sortie. Les items sont appariés entre tâches sur la marge de décision du modèle intact. La génération libre est un format secondaire.
- **Lots disjoints.** S1 sert à identifier les directions, S2 à mesurer. S3 contient quatre familles de tâches hors liste (illustratif), classées « gardée » ou « perdue » par les tenants de A avant la mesure.
- **Témoins, tous à D égal** (tolérance 5 %, illustratif) :
  - T1 : sous-espaces aléatoires, mêmes couches, mêmes positions, même k ;
  - T2 : sous-espaces appariés en variance retirée, même site ;
  - T3 : bruit gaussien de covariance appariée, même site ;
  - T4 : dégradations non directionnelles (quantification des poids, suppression de têtes au hasard) ;
  - T5 : le témoin désigné par les tenants de B avant la mesure, ajouté tel quel.
- **Second appariement.** D′ = moyenne des r_t sur la batterie. Si les conclusions divergent selon D ou D′, l'issue est « aucune », déclarée d'avance.
- **Écart déclaré.** Les directions seront celles des travaux de 2026 si elles sont publiées, sinon réidentifiées sur S1. Dans ce second cas, un échec ne réfute que ma réidentification.

### D1 — Spécificité à dose égale (le duel central)

- **H_A :** ΔS ≥ 0,20 (illustratif) contre chacun des témoins T1 à T5.
- **H_B :** |ΔS| ≤ 0,05 (illustratif) contre au moins un témoin fixé d'avance.
- **Métrique :** ΔS sur S2 à trois doses, avec intervalle de confiance à 95 % par rééchantillonnage des items et de 50 graines par famille de témoin (illustratif).
- **Seuil pour A (illustratif) :** la borne basse de l'intervalle dépasse 0,10 à au moins deux doses, contre tous les témoins, dans au moins deux modèles sur trois.
- **Seuil pour B (illustratif) :** l'intervalle tient dans [−0,05 ; +0,05] aux trois doses (test d'équivalence).
- **Contrôle négatif :** témoin contre témoin (deux graines de T1) ; le taux de « profil distinct » doit rester ≤ 5 % (illustratif).
- **Contrôle positif :** une direction à effet connu (langue de sortie) doit être détectée.
- **Falsification :**
  - intervalle dans la marge : la prédiction de A est fausse pour ces directions et ces modèles ;
  - borne basse au-dessus du seuil : la prédiction de B est fausse pour tous les témoins inscrits ;
  - entre les deux : les deux prédictions chiffrées sont manquées, issue « aucune ».

### D2 — Profil privilégié ou fabriqué (extension de ma part, HYPOTHÈSE)

Avec six tâches, il y a 20 façons d'en désigner trois comme « gardées ».

- **H_A2 :** la partition des faits est un axe naturel. La même procédure de recherche, à budget égal, y atteint une sélectivité hors lot supérieure à celle des 19 autres partitions.
- **H_B2 :** la procédure fabrique n'importe quelle dissociation ; la partition des faits n'est pas mieux servie.
- **Métrique :** rang de la partition des faits parmi les 20, selon S mesuré sur S2.
- **Seuil (illustratif) :** rang 1 dans les trois modèles falsifie H_B2. Sous échangeabilité, la probabilité est (1/20)³ = 1,25 × 10⁻⁴ ; c'est une borne optimiste, car les modèles ne sont pas indépendants. Un rang au-delà de 5 dans au moins deux modèles falsifie H_A2.
- **Contrôle négatif :** étiquettes de tâches permutées dans S1 ; rien ne doit se transférer à S2 (S ≤ 0,05, illustratif).

### D3 — Régime ou lésion : réponse à une perturbation

L'instrument transpose l'indice de complexité perturbationnelle. Une impulsion de norme fixe est injectée à une couche et une position ; la réponse est l'écart d'activation sur les couches et positions suivantes, binarisé, compressé (Lempel-Ziv), normalisé. L'indice est sans unité ; valeur nulle : rapport perturbé/intact = 1. Sa validité dans un transformeur, qui n'a pas de dynamique récurrente dans une passe avant, est une HYPOTHÈSE.

- **H_A3 :** à D égal, la suppression des directions abaisse l'indice plus que tout témoin (rapport ≤ 0,80 et sous le premier centile des témoins, illustratif).
- **H_B3 :** l'indice suit D, quoi qu'on retire (écart au témoin dans ± 0,05, illustratif).
- **Contrôle négatif :** impulsion d'amplitude nulle, indice attendu 0.
- **Falsification :** comme D1. Si l'indice ne bat pas les vérifications mécaniques de (c), le duel est annulé et non interprété.

### D4 — Motif dans les activations ordinaires

- **H_A4 :** sans intervention, les entrées où la projection sur U est spontanément basse échouent davantage aux tâches « perdues », à difficulté appariée.
- **H_B4 :** cette projection ne prédit pas mieux l'échec que la projection sur des sous-espaces témoins.
- **Métrique et seuil (illustratifs) :** gain d'aire sous la courbe ROC ≥ 0,05 pour A, dans ± 0,02 pour B.
- **Contrôle négatif :** étiquettes d'échec permutées.
- D4 est corrélationnel ; il ne compte que si D1 donne raison à A.

### Lecture des issues

- **Raison à A (prédiction) :** D1 pour A sur S2 et S3, sous D et D′. Si D2 donne ensuite H_B2, le profil est propre mais fabriqué : ni A ni B au sens des faits.
- **Raison à B (prédiction) :** équivalence dans D1.
- **Aucune :** zone intermédiaire, divergence entre D et D′, tâches au plancher, contrôle positif manqué.
- **Échappatoires.** A peut répondre « ce n'étaient pas les bonnes directions », B « un meilleur témoin l'aurait reproduit ». Elles ne se ferment que si chaque camp signe avant la mesure ses directions, sa batterie et son témoin. Sans cela, toute issue reste réinterprétable.
- **Limite.** La thèse conceptuelle de B ne rend pas l'issue A ininterprétable, mais la borne : elle se lit alors comme une lésion de capacité.

## (c) Mesure minimale par instrument (inclut le point 3)

Tous les seuils du tableau sont illustratifs.

| Instrument | Détection attendue | Fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|---|
| Suppression de directions | Effet connu retrouvé sur ≥ 95 % des items avec une direction de référence ; projection résiduelle ≤ 1 %, non reconstituée en aval | Intervention neutre (retirer puis remettre) : 0 % de sorties modifiées | Même item, intervention neutre contre active | Tenir sous remplacement par la moyenne et par rééchantillonnage, pas seulement sous mise à zéro |
| Témoin à dégradation égale | Effet planté (direction propre à une tâche) détecté ≥ 90 % | Témoin contre témoin ≤ 5 % sur 200 paires | Mêmes items, même site, même D, deux graines | Profil prédit par les seules courbes dose-réponse des témoins |
| Échelle graduée | Coefficient de reproductibilité de Guttman ≥ 0,90 (seuil d'usage, de mémoire) | Accord d'ordre avec le témoin (τ de Kendall) ≥ 0,8 : l'échelle n'est que la fragilité | Mêmes items à doses croissantes | Ordre des tâches selon la marge de décision du modèle intact |
| Motif dans les activations ordinaires | Gain d'aire ROC ≥ 0,05 pour prédire l'échec | Part des entrées signalées dont le comportement est intact, à rapporter | Paires appariées en longueur et perplexité, ou paraphrases | Longueur, rareté des tokens, marge de décision, projection sur sous-espaces témoins |
| Rapport du sujet, côté modèle (hors critère principal) | Le modèle signale l'intervention plus souvent quand elle est active | Signalements sous intervention neutre | Même invite, intervention neutre contre active | Classifieur ne lisant que le texte produit ; sonde linéaire |
| Données humaines et indices de complexité | Éveil contre propofol sans réponse : aire ROC ≥ 0,90 par sujet | Éveil contre éveil (test-retest) ≤ 5 % | Même sujet ; à exposition comparable, réactif contre non réactif | Puissance spectrale et variance du signal ; côté modèle : norme d'activation, rang effectif, D |

**Point 3.** Les données humaines brutes servent, mais pour deux usages seulement :
- étalonner la chaîne de calcul des indices de complexité sur un contraste dont le sens est connu ;
- fixer une prédiction d'ordre : l'indice baisse-t-il quand la réponse disparaît ?

Elles ne servent pas de profil cible : aucune correspondance entre les six tâches et les fonctions humaines n'est établie, et les valeurs absolues ne se comparent pas d'un substrat à l'autre.

Candidats, de mémoire, disponibilité publique à vérifier :
- EEG haute densité sous propofol avec réactivité et taux plasmatiques (Chennu et al., 2016) ;
- IRM fonctionnelle sous propofol déposée sur OpenNeuro (jeux à identifier : référence à vérifier) ;
- enregistrements peropératoires de VitalDB (Lee et al., 2022), sans rapport subjectif.

Je ne sais pas si les données de stimulation magnétique avec EEG de Casali et al. (2013) et de Sarasso et al. (2015) sont publiques.

Ces données portent les limites du rapport dites dans les faits. De mémoire, la kétamine conserve la complexité et s'accompagne de récits de rêve (Sarasso et al., 2015), et l'absence de réponse n'est pas l'inconscience (Sanders et al., 2012) : l'échelle humaine n'est pas à une dimension.

## (d) Ancrage matériel

- **Modèles.** Modèles instruits à poids ouverts de 1 à 3 milliards de paramètres (illustratif), par exemple Gemma 2 2B, Qwen2.5 3B, Llama 3.2 3B (noms de mémoire, à vérifier). Un modèle de la taille de GPT-2 small est écarté : traduction et raisonnement à plusieurs sauts y seraient au plancher (HYPOTHÈSE, contrôlée par la règle 70–95 %).
- **Outils.** Bibliothèques d'intervention sur les activations (TransformerLens, nnsight ; de mémoire).
- **Calcul par modèle (illustratif), hors T5 :**
  - mesure : 603 conditions (3 doses × [1 cible + 4 familles × 50 graines]) × 6 tâches × 300 items ≈ 1,09 million de passes ; à 50 passes par seconde sur un GPU de 24 Go, environ 6 heures ;
  - calibrage des doses par dichotomie : ≈ 0,96 million de passes, environ 5,4 heures ;
  - D2 : 20 recherches de directions, environ 10 heures ;
  - génération libre sur sous-échantillon : environ 10 heures.
- **Total (illustratif).** Environ 32 heures-GPU par modèle, 96 pour trois, 190 avec reprises. À 0,5–1 $ l'heure, de l'ordre de 100 à 200 $.
- Le coût dominant est humain : construction des items appariés et préenregistrement.

## Point 4 — Ce que chaque issue permet d'affirmer, par théorie

| Théorie | Issue A | Issue B |
|---|---|---|
| Espace de travail global (Mashour et al., 2020) | Compatible avec un rôle de diffusion large porté par ces directions : un indice fonctionnel au sens de Butlin et al. (2023), pas une preuve. L'embrasement n'est pas testé. | Ces directions ne marquent pas un tel rôle. Rien sur l'architecture en général. |
| Information intégrée (Tononi et al., 2016) | Sans effet : la théorie fait dépendre la conscience de la structure causale du support, pas du calcul. L'indice de D3 s'en inspire, mais ne mesure pas Φ. | Sans effet, pour la même raison. |
| Ordre supérieur (Lau et Rosenthal, 2011) | Muette : le plan ne mesure aucune représentation d'ordre supérieur, sauf ajout d'une tâche de métacognition à la batterie. | Muette. |
| Traitement récurrent (Lamme, 2006) | Verdict fixé par l'architecture (passe avant), pas par l'issue. | Idem. |
| Approches biologiques et de l'éveil (Aru et al., 2023 ; Brown et al., 2010) | Lue comme lésion de capacité, non comme perte d'état. | Attendue, mais non probante. |

**L'issue A permet d'affirmer** qu'il existe une intervention dont le profil fonctionnel est propre et ne se réduit pas à une dégradation globale ; le contraste devient un outil utilisable. **Elle ne permet pas d'affirmer** que le modèle était conscient avant, ni inconscient après.

**L'issue B permet d'affirmer** que, pour ces directions et ces modèles, l'analogie n'ajoute rien au mot « dégradation ». **Elle ne permet pas d'affirmer** qu'aucun régime de ce type n'existe, ni que ces systèmes ne sont pas conscients, ni que la thèse conceptuelle de B est vraie.

Dans les deux cas, l'absence de pôle indépendant demeure.

## Point 5 — Vérification hors de l'équipe

- **Préenregistrement** horodaté avec empreinte : plan, seuils, graines des témoins, listes d'items, classement de S3, avant toute mesure.
- **Collaboration contradictoire :** les tenants de A fixent directions et tâches hors liste, ceux de B fixent leur témoin, un tiers exécute.
- **Publication** des vecteurs, du code, des graines et des sorties brutes ; les poids étant ouverts, chacun peut réexécuter.
- **Réplication** par une équipe qui n'a pas choisi les directions, sur un modèle d'une autre famille et avec une autre méthode d'identification.
- **Défi ouvert :** tout témoin à D égal qui reproduit le profil réfute l'issue A.
- **Notation à l'aveugle** des sorties en génération libre.

## Point 6 — L'explication triviale la plus dangereuse

**La circularité de la sélection.** Si les directions ont été retenues parce que leur suppression produit la dissociation, alors « profil distinct du témoin aléatoire » est vrai par construction. On aurait trouvé de la même façon des directions pour n'importe quelle autre dissociation (Kriegeskorte et al., 2009, pour le problème général). Le danger est qu'elle donne à l'issue A l'apparence d'un résultat.

**Témoin :** D2 (même procédure, même budget, sur les 19 autres partitions), joint à la mesure sur les lots disjoints S2 et S3. Il existe, mais il est partiel : si la procédure des travaux de 2026 ne m'est pas accessible, je ne contrôle que la mienne.

Du côté opposé, une issue B peut venir d'un manque de sensibilité. Le témoin est le contrôle positif de D1 : sans détection de l'effet planté, l'issue B n'est pas interprétée.

## Antériorité

**Lu dans cette session :** uniquement la pièce transmise. **Tout ce qui suit est cité de mémoire**, sans relecture ni vérification ici. Je n'attribue pas les « travaux de 2026 ».

Anesthésie et complexité :
- Casali et al., 2013, « A theoretically based index of consciousness independent of sensory processing and behavior ».
- Sarasso et al., 2015, « Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine ».
- Schartner et al., 2015, « Complexity of multi-dimensional spontaneous EEG decreases during propofol induced general anaesthesia ».
- Chennu et al., 2016, « Brain connectivity dissociates responsiveness from drug exposure during propofol-induced transitions of consciousness ».
- Sanders, Tononi, Laureys et Sleigh, 2012, « Unresponsiveness ≠ unconsciousness ».
- Brown, Lydic et Schiff, 2010, « General anesthesia, sleep, and coma ».
- Lee et al., 2022, « VitalDB, a high-fidelity multi-parameter vital signs database in surgical patients ».

Théories :
- Mashour, Roelfsema, Changeux et Dehaene, 2020, « Conscious processing and the global neuronal workspace hypothesis ».
- Tononi, Boly, Massimini et Koch, 2016, « Integrated information theory: from consciousness to its physical substrate ».
- Lau et Rosenthal, 2011, « Empirical support for higher-order theories of conscious awareness ».
- Lamme, 2006, « Towards a true neural stance on consciousness ».
- Butlin, Long et al., 2023, « Consciousness in Artificial Intelligence: Insights from the Science of Consciousness ».
- Aru, Larkum et Shine, 2023, « The feasibility of artificial consciousness through the lens of neuroscience ».

Ablation, témoins, circularité :
- Elazar, Ravfogel, Jacovi et Goldberg, 2021, « Amnesic Probing: Behavioral Explanation with Amnesic Counterfactuals » (témoin par directions aléatoires en nombre égal).
- Hewitt et Liang, 2019, « Designing and Interpreting Probes with Control Tasks ».
- Arditi et al., 2024, « Refusal in Language Models Is Mediated by a Single Direction ».
- McGrath et al., 2023, « The Hydra Effect: Emergent Self-repair in Language Model Computations ».
- Kriegeskorte, Simmons, Bellgowan et Baker, 2009, « Circular analysis in systems neuroscience: the dangers of double dipping ».

FIN-DE-CELLULE