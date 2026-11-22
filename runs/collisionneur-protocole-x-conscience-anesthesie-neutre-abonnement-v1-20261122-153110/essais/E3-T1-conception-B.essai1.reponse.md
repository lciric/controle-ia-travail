# Proposition B — Tour III.1

**État des pièces.** Le bloc FAITS est présent et complet, mais il reprend mot pour mot la question de l'arbitre (même empreinte annoncée, que je n'ai pas recalculée). Il ne transmet donc aucun fait muni d'un statut, et je n'en invente pas.
**Statuts.** RAPPORTÉ désigne un résultat publié que je cite de mémoire ; les références sont en fin de cellule. HYPOTHÈSE désigne une proposition de ma part. Rien n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ, car aucune donnée n'a été examinée ici. Chaque chiffre est marqué « illustratif ». Les noms de modèles (comme Pythia-160M) et les années servent d'identifiants.
**B1.** Le tour est à l'aveugle : je ne vois pas A, C, D, E et F. Je ne les critique pas et je ne m'en sers pas.

**Thèse de travail (HYPOTHÈSE).** La transposition sert surtout de *modèle nul*. Elle peut dire si un marqueur humain de l'anesthésie est spécifique, ou s'il découle de toute dégradation d'un traitement hiérarchique. Elle peut aussi dire si une mesure cérébrale reste valable dans un autre substrat. Elle ne peut pas désigner un état d'un réseau comme conscient, faute d'ancre (point a6).

## (a) Ce que la question suppose sans que ce soit établi

1. **Que l'anesthésie oppose « conscient » et « non conscient ».** Elle dissocie au moins trois choses : la conscience, la connexion à l'environnement et la capacité de réagir. Ne pas réagir n'implique pas l'absence d'expérience : des patients rapportent des rêves, et certains répondent par la technique de l'avant-bras isolé. — RAPPORTÉ [R1]. Le contraste humain n'est lui-même établi qu'après coup, par le récit du sujet.
2. **Qu'il existe un axe unique de « niveau » de conscience.** C'est contesté. — RAPPORTÉ [R2].
3. **Que « l'anesthésie » forme un seul contraste.** Sous kétamine, l'indice de complexité perturbationnelle (PCI) reste élevé et les sujets rapportent des rêves ; sous propofol et sous xénon, ce n'est pas le cas. — RAPPORTÉ [R3]. Ce que l'anesthésie épargne dépend donc de l'agent ; je prends le propofol comme référence.
4. **Que les mesures cérébrales mesurent la conscience plutôt qu'une physiologie.** Le PCI a été calibré chez l'humain contre ce que les sujets pouvaient rapporter [R4, R5]. La propagation des réponses à une stimulation s'effondre en sommeil lent [R6]. — RAPPORTÉ. On relie cet effondrement à la bistabilité des neurones (alternance de périodes actives et silencieuses) — référence à vérifier. Une unité de transformeur n'a pas d'équivalent évident de ce mécanisme. — HYPOTHÈSE.
5. **Que le réseau a une dynamique à perturber.** En inférence, un transformeur n'a pas d'activité spontanée : une passe est déterministe et ne contient pas de boucle. Seul le contexte (le cache clés-valeurs) porte un état. — RAPPORTÉ (architecture documentée). Pour la théorie de l'information intégrée 3.0, un système sans boucle a une intégration Φ nulle [R7]. — RAPPORTÉ. Reste ouverte la question de savoir si la boucle formée par la génération jeton après jeton change ce verdict. — HYPOTHÈSE.
6. **Que le pôle « conscient » se repère côté réseau.** Chez l'humain, l'éveil sert de référence parce que le sujet peut en rendre compte. Dans un modèle de langage, ce compte rendu est une sortie entraînée sur du texte humain ; il n'est donc pas une source indépendante. — HYPOTHÈSE (argument). Les grilles d'indicateurs tirées des théories [R8] ne fournissent pas non plus d'ancre empirique. — RAPPORTÉ.
7. **Que la réversibilité et la gradation apportent une information côté réseau.** Toute intervention sur des poids ou des activations se défait exactement, donc la réversibilité n'apprend rien. — HYPOTHÈSE (argument). Chez l'animal, la perte et le retour de conscience ne surviennent pas à la même concentration d'anesthésique (« inertie neuronale ») [R9]. — RAPPORTÉ. Dans un transformeur, une telle hystérésis apparaîtrait trivialement, parce que le cache garde des représentations calculées sous forte dose ; elle ne teste donc pas l'analogie. — HYPOTHÈSE.
8. **Que ce que l'anesthésie ou le sommeil supprime est propre à la conscience.**
   - Dans le paradigme local-global, l'effet global disparaît chez les sujets non conscients, alors que l'effet local persiste en grande partie [R10, R11].
   - En sommeil, le cerveau ne suit plus le rythme des phrases (mesuré par marquage fréquentiel), alors qu'il suit encore celui des syllabes [R12, R13].
   - Sous propofol, la réponse du cortex temporal à la parole persiste, mais la réponse à l'ambiguïté sémantique baisse [R14].
   - Ces trois résultats sont RAPPORTÉS. La composante globale (P3b) dépend aussi de la tâche et du compte rendu demandé [R15]. — RAPPORTÉ.
   - Il n'est pas établi que ces dissociations ne viennent pas simplement d'un rapport signal/bruit qui baisse à mesure que le traitement monte dans la hiérarchie. — HYPOTHÈSE, testée en E2.
9. **Que l'alignement entre modèle et cerveau reflète le traitement du langage.** Des modèles non entraînés prédisent déjà une part non nulle des réponses cérébrales au langage [R16]. — RAPPORTÉ. Testé en E4.

## (b) Expériences en duel

**Ordre.** E1 et E4 sont indépendantes. E3 cherche la signature trouvée en E2. Si E1 donne H_A, le PCI transposé s'ajoute à cette signature.

### E1 — Une mesure cérébrale distingue-t-elle un réseau qui fonctionne d'un réseau sans fonction ? (direction 4)

**Grandeur : PCI_art.**
- On ajoute une perturbation δ au flux résiduel d'un contexte neutre, à la couche l₀ et à la position t₀.
- La réponse est la différence entre activations perturbées et non perturbées, sur les couches au-delà de l₀ et les positions à partir de t₀, plus k jetons suivants en forçage.
- Une cellule (composante principale × couche × position) est dite significative si l'écart dépasse le quantile 99 % [illustratif] des écarts entre deux contextes neutres appariés. Dans un système déterministe, c'est le seul substitut à une activité de fond.
- La matrice binaire obtenue est compressée par Lempel-Ziv [R17] et normalisée par l'entropie de source, comme en [R4].
- **Unité** : sans dimension. **Valeur nulle** : 0 (rien ne se propage) ; une matrice aléatoire de même densité donne environ 1.

**Témoins sans fonction, appariés honnêtement.**
- T1 : poids permutés à l'intérieur de chaque matrice ; leur distribution est conservée, la fonction est détruite.
- T2 : poids d'initialisation (point de contrôle 0), remis à l'échelle pour égaler la norme de réponse du modèle entraîné.
- T3 : sortie de chaque bloc remplacée par un bruit de mêmes moments statistiques.

**Lésions.** L1, ciblée : ablation des têtes d'induction [R18]. L2, aléatoire : même nombre de têtes tirées au hasard, appariée sur la hausse de perte (Δperte).

- **H_A (la mesure suit la fonction).** Une fois le gain de perturbation apparié (norme du jacobien), PCI_art sépare le modèle entraîné de T1–T3 sur l'ensemble des sites, avec une AUC ≥ 0,9 [illustratif]. Il sépare aussi L1 de L2 à Δperte égale.
- **H_B (la mesure suit le gain).** Une régression de PCI_art sur le gain, la densité de cellules significatives et la norme d'activation atteint R² ≥ 0,8 [illustratif], et l'AUC résiduelle reste ≤ 0,6 [illustratif].
- **Ce qui falsifie H_A.** Un témoin apparié en gain tombe dans la distribution du modèle entraîné, ou L1 ne se distingue pas de L2. Prédiction risquée (HYPOTHÈSE) : T2, proche du régime chaotique, obtiendra un PCI_art au moins égal à celui du modèle entraîné.
- **Ce qui falsifie H_B.** L'AUC résiduelle reste ≥ 0,9 [illustratif] après la régression.
- **Contrôles négatifs.** Avec δ = 0, PCI_art vaut 0. Entre deux contextes neutres non perturbés, environ 1 % [illustratif] des cellules sont significatives, par construction.
- **Contrôle positif du code.** Le même calcul de Lempel-Ziv, appliqué à l'EEG de sédation au propofol [R19 ; accès à vérifier], doit retrouver la baisse de complexité rapportée [R20]. Sinon, E1 est suspendue.
- **Première expérience.** Pythia-160M, au point de contrôle 0 et au point final ; 100 sites × 20 directions [illustratif].
- **Pour qui cherche si une IA peut être consciente.** H_B retire l'indice le plus cité, sauf à le recalibrer pour ce substrat, ce qui est impossible sans ancre (a6). H_A donne un indice qui suit l'intégration fonctionnelle : c'est une condition pour s'en servir, pas une preuve.
- **Pour qui juge la question mal posée.** H_B fournit un argument chiffré : l'indice mesure le gain d'un milieu excitable. H_A l'oblige à expliquer pourquoi un indice sensible au même type de dommage dans deux substrats ne compterait pas.

### E2 — Une intervention épargne-t-elle le local et supprime-t-elle le global sans tout dégrader ? (direction 1)

**Grandeurs.**
- **Paradigme local-global sous forme de texte.** On répète des blocs « x x x x y » (longueurs illustratives). Le déviant local est y ; le déviant global est « x x x x x » après habituation.
- E_loc et E_glob : surprise supplémentaire sur le dernier symbole. **Unité** : nats ; **nulle** : 0. Variante : AUC d'un décodeur standard/déviant, couche par couche ; nulle : 0,5.
- **Second couple d'index, qui transpose [R12].** On présente des flux isochrones de phrases de quatre mots [illustratif]. Le pic spectral des activations au rythme du mot donne l'index local, celui au rythme de la phrase donne l'index global. Unité : rapport du pic aux fréquences voisines ; nul : 1.

**Interventions sans a priori sur la structure du réseau.**
- I1 : gain α < 1 sur les contributions des blocs supérieurs.
- I2 : bruit gaussien σ ajouté au flux résiduel.
- I3 : température d'attention τ, uniforme.

**Témoin mécanique M.** On tronque la fenêtre d'attention à un essai (plusieurs largeurs). M supprime le global par construction : il sert de contrôle positif et ne compte pas pour H_A.

**Appariement indispensable.** Les stimuli sont choisis pour que E_loc et E_glob aient le même rapport signal/bruit de départ (AUC égales à ±0,02 près [illustratif]). Sans cela, n'importe quelle dégradation éteint d'abord l'effet le plus faible.

**Métrique : sélectivité S.** S est l'aire entre les courbes de rétention normalisées du local et du global. Ces courbes sont tracées en fonction de la hausse de perplexité sur un corpus tenu à part, pour comparer les interventions à dégradation égale. S est sans dimension ; sa valeur nulle est 0. La distribution nulle vient de 200 [illustratif] directions de bruit et sous-ensembles de couches tirés au hasard, à hausse de perplexité égale.

- **H_A (spécificité).** Au moins une famille parmi I1–I3 donne un S au-delà du quantile 99 % [illustratif] de la distribution nulle, à rapport signal/bruit apparié, sur les deux couples d'index.
- **H_B (hiérarchie générique).** Après appariement, S reste dans la distribution nulle pour I1–I3 ; la dissociation visible sans appariement disparaît avec lui.
- **Ce qui falsifie H_A** : aucune famille ne sort de la distribution nulle. **Ce qui falsifie H_B** : une famille en sort sur les deux couples d'index.
- **Contrôles.** À dose nulle, S vaut 0. M doit donner un S élevé ; sinon, la métrique est aveugle.
- **Première expérience.** GPT-2 small et Pythia-160M ; 2 000 séquences ; 3 familles × 20 doses [illustratif].
- **Si H_B gagne.** Les dissociations humaines (local/global, syllabe/phrase) sont prédites par n'importe quel traitement hiérarchique bruité. Elles perdent du poids comme marqueurs *spécifiques* de la conscience, et d'abord chez l'humain. Pour qui cherche une conscience artificielle, ce sont deux marqueurs de moins à transférer. Pour qui juge la question mal posée, c'est un appui mesuré à l'idée que ces marqueurs suivent la profondeur du traitement.
- **Si H_A gagne.** On obtient un modèle manipulable d'une composante d'intégration séparable. Pour qui cherche une conscience artificielle, c'est un outil expérimental, pas un verdict. Pour qui juge la question mal posée, cela montre qu'un réseau sans ancre de conscience reproduit le profil, donc que le profil ne suffit pas. On ne pourrait l'éviter qu'en soutenant que le réseau est conscient, ce qu'aucune mesure ici ne tranche.

### E3 — Le régime apparaît-il de lui-même ? (direction 2)

**Grandeur.** Taux de déclenchement, pour 1 000 jetons [illustratif], d'un détecteur de la signature trouvée en E2, dans des activations ordinaires. **Valeur nulle** : le taux de fausses alertes du détecteur sur des contextes intacts appariés en longueur, position et entropie de l'entrée.
- Le détecteur est une sonde linéaire entraînée à séparer les activations sous intervention E2 des activations intactes, et évaluée sur des données tenues à part.
- Deux index se lisent à chaque position : la rétention d'un référent introduit loin en arrière (AUC d'une sonde, nulle 0,5) et l'identité du jeton précédent (AUC, nulle 0,5).

**Données.**
- La partie validation de The Pile [R21].
- Des générations libres du même modèle, où apparaissent des boucles de répétition [R22].
- Des contextes plus longs que la longueur d'entraînement.

Candidats (HYPOTHÈSE) : les boucles de répétition, où la fluidité locale est conservée, le fil du document est perdu, et la boucle s'entretient elle-même ; les puits d'attention [R23].

- **H_A (régime interne).** Le taux de déclenchement dépasse celui des fausses alertes. De plus, les déclenchements prédisent la perte du référent sur les jetons suivants mieux qu'un modèle fondé sur des caractéristiques de l'entrée (longueur, position, taux de répétition, entropie n-gramme) : gain d'AUC ≥ 0,05 [illustratif], avec un intervalle de confiance qui exclut 0.
- **H_B (fonction de l'entrée).** Le taux ne se distingue pas des fausses alertes, ou bien les caractéristiques de l'entrée prédisent aussi bien (l'intervalle du gain contient 0).
- **Ce qui falsifie H_A** : H_B observée sur les trois sources. **Ce qui falsifie H_B** : un gain significatif sur au moins une source, reproduit sur un second modèle.
- **Contrôle négatif.** Des textes mélangés phrase à phrase, où la perte du global est imposée par l'entrée. Un détecteur valide doit attribuer ces cas aux caractéristiques de l'entrée.
- **Limite.** Si E2 donne H_B, la seule signature disponible est celle de M. E3 cherche alors des épisodes « comme si la fenêtre était tronquée », et le lien avec l'anesthésie s'affaiblit d'autant.
- **Si H_A gagne.** Une variable d'état interne existe et peut être suivie. Le sceptique notera qu'elle se confond peut-être avec des pannes banales, comme la répétition.
- **Si H_B gagne.** Dans cette architecture, « l'état » se réduit au contexte : parler d'un niveau du modèle indépendamment de son entrée n'a pas de prise mesurable. C'est un appui à la thèse « question mal posée », pour cette architecture seulement. Qui cherche une conscience artificielle devra se tourner vers des architectures dotées d'une dynamique propre.

### E4 — Un modèle de langage lit-il mieux que des mesures simples ce que le cerveau sous sédation traite encore ? (direction 3)

**Grandeur.** On mesure ΔR², la variance expliquée par les traits contextuels d'un modèle (couche l) au-delà d'un ensemble de traits de base. Elle est normalisée par le plafond de bruit, calculée par région et par niveau de sédation ; sa valeur nulle est 0. Le contraste étudié est C = ΔR²(éveil) − ΔR²(sédation profonde).

**Traits de base (les vérifications mécaniques à battre).** Enveloppe et spectrogramme acoustiques, début et débit des mots, fréquence des mots, plongements statiques, surprise selon un modèle n-gramme.

**Témoins.**
- La même architecture non entraînée [R16].
- Le même modèle sur des mots permutés à l'intérieur de chaque phrase, ce qui détruit le contexte.
- Contrôle négatif : un décalage circulaire des traits par rapport au signal cérébral ; ΔR² doit alors être proche de 0.
- Contrôle positif : l'enveloppe acoustique doit rester prédictive dans le cortex auditif sous sédation (HYPOTHÈSE fondée sur [R14]).

**Données.** Il faut des enregistrements publics de sédation au propofol pendant l'écoute d'un récit. Je connais une étude en IRMf avec un extrait sonore de film (Naci et al., 2018 — référence à vérifier ; je ne donne pas d'identifiant de dépôt de mémoire). L'EEG ou la MEG conviendraient mieux pour la résolution temporelle ; leur disponibilité publique est à vérifier.

- **H_A (l'instrument apporte quelque chose).** C_LLM > 0, avec un intervalle de confiance qui exclut 0, dans des régions temporales ou frontales. De plus, C_LLM dépasse à la fois C du modèle non entraîné et C du modèle n-gramme, avec des intervalles des différences qui excluent 0.
- **H_B (rien de plus que des mesures simples).** C_LLM ne dépasse pas C du modèle n-gramme ou du modèle non entraîné (l'intervalle d'une différence contient 0).
- **Ce qui falsifie H_A** : H_B observée alors que l'effet attendu dépasse le seuil de détection. **Ce qui falsifie H_B** : les deux différences excluent 0.
- **Puissance d'abord.** On simule des données où l'on plante une composante contextuelle atténuée d'un facteur connu, avec un bruit et une autocorrélation copiés des vraies données. On fixe ainsi, avant toute analyse, le plus petit C détectable. Les études de sédation sont petites (environ vingt sujets [illustratif]) ; on n'interprète H_B qu'au-dessus de ce seuil.
- **Si H_A gagne.** On dispose d'un instrument pour quantifier le traitement contextuel résiduel chez des patients qui ne répondent pas (la question de la conscience « déconnectée », a1). Côté IA, on sera tenté de conclure que les représentations du modèle correspondent à la « composante consciente ». Cette inférence n'est pas valide, car des représentations qui se correspondent ne font pas un état partagé : le résultat porte sur le cerveau.
- **Si H_B gagne.** Des mesures simples suffisent. Le sceptique y voit que l'alignement entre modèle et cerveau ne dit rien de l'état de conscience.

## (c) Instruments nommés dans la question : la mesure minimale qui dit s'ils fonctionnent

Tous les taux de ce tableau sont illustratifs.

| Instrument | Cas positifs | Cas négatifs honnêtes appariés | Taux visés | Vérifications mécaniques à battre |
|---|---|---|---|---|
| Mesure cérébrale transposée (PCI_art, Lempel-Ziv) | Modèles entraînés intacts, 3 tailles ou plus | T1–T3 appariés en gain et en norme ; L2 appariée à L1 en Δperte | Détection ≥ 0,9 ; fausses alertes ≤ 0,1 | Gain du jacobien, densité de cellules significatives, norme de la réponse, Δperte seule |
| Intervention « régime » (indice S) | M à plusieurs largeurs de fenêtre (sélectivité construite) | Directions et couches tirées au hasard, à hausse de perplexité égale | Détection de M ≥ 0,95 ; fausses alertes ≤ 0,01 | Hausse de perplexité seule ; écart de rapport signal/bruit au départ |
| Détecteur de régime spontané | Activations sous intervention E2, tenues à part | Contextes naturels intacts appariés en longueur, position et entropie | Détection ≥ 0,9 ; fausses alertes ≤ 0,05 | Classifieur sur les seules caractéristiques de l'entrée |
| Modèle de langage comme instrument sur le cerveau | Données synthétiques avec composante plantée | Mêmes données sans composante ; décalage circulaire | Puissance ≥ 0,8 au C visé ; fausses alertes ≤ 0,05 | Modèle n-gramme, plongements statiques, enveloppe acoustique, modèle non entraîné |

Règle : un instrument qui ne bat pas les vérifications de la dernière colonne n'est pas utilisé dans l'expérience suivante.

## (d) Ancrage matériel

- **Modèles ouverts.** GPT-2 small ; la suite Pythia (de 70M à 410M), qui fournit des points de contrôle intermédiaires dont l'initialisation [R24]. Outils : bibliothèques ouvertes d'interprétabilité, par exemple TransformerLens.
- **Calcul (toutes valeurs illustratives).**
  - E1 : environ 10⁵ passes de 256 jetons sur 160 M paramètres, soit environ 10¹⁶ FLOP ; moins d'une heure sur un GPU de 24 Go.
  - E2 : environ 4·10⁶ passes courtes, soit environ 10¹⁷ FLOP ; quelques heures.
  - E3 : activations sur environ 10⁷ jetons ; moins d'une heure, plus quelques dizaines de Go de stockage.
  - E4 : extraction des traits négligeable ; régressions ridge sur CPU en quelques heures.
- **Coût (illustratif).** Quelques dizaines d'euros de GPU en nuage. Les vraies contraintes sont le temps humain, surtout pour préparer les données de sédation (quelques semaines-personne, illustratif), et l'accès à ces données.

## Ce que l'ensemble n'apprendrait pas

- Aucune issue n'établit ni n'exclut qu'un réseau ait une expérience vécue (a6).
- La réversibilité et l'hystérésis ne testent rien côté réseau (a7).
- **Ce qui est réfutable : quatre duels, soit huit issues qui falsifient chacune une hypothèse.** Ils portent sur :
  - la spécificité des marqueurs humains (E2) ;
  - la validité du transfert d'une mesure cérébrale (E1) ;
  - l'existence d'états qui ne se réduisent pas à l'entrée (E3) ;
  - l'apport d'un modèle de langage comme instrument (E4).

## Références (citées de mémoire ; statut RAPPORTÉ)

- R1 Sanders, Tononi, Laureys & Sleigh (2012). Unresponsiveness ≠ unconsciousness. *Anesthesiology*.
- R2 Bayne, Hohwy & Owen (2016). Are there levels of consciousness? *Trends in Cognitive Sciences*.
- R3 Sarasso et al. (2015). Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine. *Current Biology*.
- R4 Casali et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. *Science Translational Medicine*.
- R5 Casarotto et al. (2016). Stratification of unresponsive patients by an independently validated index of brain complexity. *Annals of Neurology*.
- R6 Massimini et al. (2005). Breakdown of cortical effective connectivity during sleep. *Science*.
- R7 Oizumi, Albantakis & Tononi (2014). From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0. *PLoS Computational Biology*.
- R8 Butlin, Long et al. (2023). Consciousness in Artificial Intelligence: Insights from the Science of Consciousness. Prépublication.
- R9 Friedman et al. (2010). A conserved behavioral state barrier impedes transitions between anesthetic-induced unconsciousness and wakefulness: evidence for neural inertia. *PLoS ONE*.
- R10 Bekinschtein et al. (2009). Neural signature of the conscious processing of auditory regularities. *PNAS*.
- R11 Strauss et al. (2015). Disruption of hierarchical predictive coding during sleep. *PNAS*.
- R12 Ding, Melloni, Zhang, Tian & Poeppel (2016). Cortical tracking of hierarchical linguistic structures in connected speech. *Nature Neuroscience*.
- R13 Makov et al. (2017). Sleep disrupts high-level speech parsing despite significant basic auditory processing. *Journal of Neuroscience*.
- R14 Davis et al. (2007). Dissociating speech perception and comprehension at reduced levels of awareness. *PNAS*.
- R15 Pitts, Metzler & Hillyard (2014). Isolating neural correlates of conscious perception from neural correlates of reporting one's perception. *Frontiers in Psychology*.
- R16 Schrimpf et al. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*.
- R17 Lempel & Ziv (1976). On the complexity of finite sequences. *IEEE Transactions on Information Theory*.
- R18 Olsson et al. (2022). In-context learning and induction heads. *Transformer Circuits Thread*.
- R19 Chennu et al. (2016). Brain connectivity dissociates responsiveness from drug exposure during propofol-induced transitions of consciousness. *PLoS Computational Biology*.
- R20 Schartner et al. (2015). Complexity of multi-dimensional spontaneous EEG decreases during propofol induced general anaesthesia. *PLoS ONE*.
- R21 Gao et al. (2020). The Pile: An 800GB dataset of diverse text for language modeling. Prépublication.
- R22 Holtzman, Buys, Du, Forbes & Choi (2020). The curious case of neural text degeneration. *ICLR*.
- R23 Xiao, Tian, Chen, Han & Lewis (2024). Efficient streaming language models with attention sinks. *ICLR*.
- R24 Biderman et al. (2023). Pythia: A suite for analyzing large language models across training and scaling. *ICML*.

FIN-DE-CELLULE