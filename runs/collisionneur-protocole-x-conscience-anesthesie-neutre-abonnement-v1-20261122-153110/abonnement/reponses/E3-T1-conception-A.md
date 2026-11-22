# Proposition A — tour III.1

**État des pièces.** Le bloc FAITS reproduit mot pour mot le bloc QUESTION (même empreinte déclarée, non recalculée : aucun outil de calcul ne m'est permis). Il ne contient donc aucun fait assorti d'un statut. Aucune proposition B–F ne m'a été transmise ; la règle B1 est sans objet à ce tour.

**Statuts employés.** Rien ci-dessous n'est VÉRIFIÉ ni OBSERVÉ-NON-AUDITÉ : je n'ai exécuté aucune expérience. La littérature est RAPPORTÉE, citée de mémoire et non relue dans cette session. Le reste est HYPOTHÈSE. Tous les seuils, effectifs et coûts sont illustratifs, à fixer par préenregistrement.

## (a) Ce que la question suppose sans que ce soit établi

1. **L'anesthésie oppose conscience et absence de conscience.** Ce qu'on mesure est la réactivité. RAPPORTÉ : absence de réponse et absence d'expérience se dissocient (Sanders, Tononi, Laureys et Sleigh, 2012, « Unresponsiveness ≠ unconsciousness »). RAPPORTÉ : sous kétamine, des sujets sans réponse rapportent au réveil une expérience, et leur complexité perturbationnelle reste haute (Sarasso et coll., 2015, « Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine »). Que le contraste porte sur la conscience elle-même : HYPOTHÈSE, que la question concède par « ou l'est autrement ».

2. **Le contraste est gradué.** Dose graduée : RAPPORTÉ. État gradué : HYPOTHÈSE ; une hystérésis entre induction et réveil est RAPPORTÉE (Friedman et coll., 2010, « A conserved behavioral state barrier impedes transitions between anesthetic-induced unconsciousness and wakefulness: evidence for neural inertia »).

3. **Il existe un profil unique « épargné / supprimé ».** Trois éléments RAPPORTÉS :
   - la déviance locale reste détectée, la déviance globale ne l'est plus (paradigme : Bekinschtein et coll., 2009, « Neural signature of the conscious processing of auditory regularities » ; sous propofol : Nourski et coll., 2018, « Auditory predictive coding across awareness states under anesthesia: an intracranial electrophysiology study ») ;
   - les réponses temporales à la parole persistent sous sédation quand les réponses frontales liées à la compréhension disparaissent (Davis et coll., 2007, « Dissociating speech perception and comprehension at reduced levels of awareness ») ;
   - la complexité de la réponse à une perturbation s'effondre (Casali et coll., 2013, « A theoretically based index of consciousness independent of sensory processing and behavior »).

   Que ce profil soit commun à tous les agents : HYPOTHÈSE, contredite par la kétamine (point 1).

4. **Un modèle de langage possède l'analogue des deux termes.** RAPPORTÉ (architecture publiée) : un transformeur en inférence n'a ni activité spontanée ni état de vigilance ; il est sans rétroaction en profondeur ; sa seule boucle passe par les jetons produits. HYPOTHÈSE : toute correspondance (couches ↔ hiérarchie corticale, attention ↔ intégration à longue portée, boucle autorégressive ↔ réentrée). Chacune est un degré de liberté de l'expérimentateur.

5. **Réversibilité et gradation restent informatives une fois transposées.** HYPOTHÈSE, que je crois fausse : dans un réseau, retirer l'intervention restaure l'état par construction. Ce qui informe chez l'humain, c'est qu'une manipulation unique, de faible dimension, fait tomber ensemble plusieurs marqueurs mesurés indépendamment. C'est cette covariation qui est transposable (E2).

6. **Les mesures tirées du cerveau mesurent un niveau de conscience.** RAPPORTÉ : elles séparent des états humains et ont été étalonnées contre le rapport du sujet (Casali et coll., 2013 ; Casarotto et coll., 2016, « Stratification of unresponsive patients by an independently validated index of brain complexity »). HYPOTHÈSE : qu'elles gardent un sens hors du système d'étalonnage. Un réseau n'offre pas de rapport au réveil : la validité de critère y est inaccessible, seule la validité discriminante est testable.

7. **« Fonctionne / sans fonction » est le bon contraste.** HYPOTHÈSE. Une mesure qui suit exactement la performance est redondante avec la perte ; le test exigeant se fait à perte égale.

8. **Un régime « spontané » se définit indépendamment de l'intervention qui l'a défini.** HYPOTHÈSE ; sinon la recherche est circulaire.

9. **L'alignement modèle–cerveau reflète un calcul linguistique partagé.** Alignement RAPPORTÉ (Schrimpf et coll., 2021, « The neural architecture of language: Integrative modeling converges on predictive processing » ; Goldstein et coll., 2022, « Shared computational principles for language processing in humans and deep language models »). Interprétation : HYPOTHÈSE. Existence de données publiques sous anesthésie, avec parole naturelle et rapport signal/bruit suffisant : HYPOTHÈSE.

10. **Un résultat, dans un sens ou l'autre, porte sur la conscience artificielle.** HYPOTHÈSE, conditionnelle à la théorie. Il est pertinent pour l'espace de travail global (Mashour, Roelfsema, Changeux et Dehaene, 2020, « Conscious processing and the global neuronal workspace hypothesis »). Il est sans portée pour la théorie de l'information intégrée, où le substrat physique décide (Tononi et Koch, 2015, « Consciousness: here, there and everywhere? »).

## (b) Expériences décisives

Lecteurs : **C** cherche à savoir si une IA peut être consciente ; **S** juge la question mal posée.

Ordre : E1 d'abord (la moins chère ; elle décide si la mesure entre dans E2), puis E2 ; E3 seulement si E2 conclut H_A ; E4 est indépendante.

### E1 — La mesure distingue-t-elle la fonction du régime dynamique ? (direction 4)

**Grandeur.** PCI-T, construit en quatre temps :
- on ajoute au flux résiduel, à une couche ℓ et une position t, un vecteur de norme fixée ;
- on relève l'écart d'activation aux couches ℓ′ > ℓ et positions t′ ≥ t, sous continuation imposée ;
- on binarise chaque case contre la distribution des écarts sans perturbation ;
- on compresse la matrice binaire (Lempel et Ziv, 1976, « On the complexity of finite sequences ») et on normalise par l'entropie de la source, comme Casali et coll.

**Unité** : sans dimension (bits par bit). **Valeur nulle** : 0, aucune case significative ; pour le contraste entre réseaux, AUROC de 0,5.

**Réseaux, à architecture fixe.**
- R1 : entraîné.
- R2 : initialisation aléatoire.
- R3 : aléatoire à spectre apparié (mêmes valeurs singulières par matrice, vecteurs singuliers tirés au hasard).
- R4 : entraîné, têtes d'attention ablatées au hasard.
- R5 : entraîné, ablation ciblée des têtes qui transportent l'information entre positions éloignées ; R4 et R5 sont appariés en perte (nats par jeton).
- R6 : points de contrôle successifs de l'entraînement, gradation naturelle de la fonction.

**Duel.**
- **H_A — la mesure se transpose.** AUROC(R1 contre R3) ≥ 0,9, AUROC(R5 contre R4) ≥ 0,8, et aucun scalaire mécanique n'explique PCI-T (R² < 0,5).
- **H_B — elle indexe un régime dynamique générique.** AUROC(R1 contre R3) ≤ 0,6, ou un scalaire (gain jacobien moyen, croissance de norme, rang effectif des activations, entropie de l'attention) prédit PCI-T avec R² ≥ 0,9 sur R1–R6.

Seuils illustratifs ; l'entre-deux est déclaré non concluant à l'avance.

**Témoins.** Négatif : perturbation de norme nulle, qui doit donner 0 case significative au taux nominal près. Positif : petit réseau récurrent aléatoire dont on fait varier le rayon spectral ; si PCI-T n'y varie pas, la chaîne de mesure ne détecte rien et l'expérience est nulle.

**Falsification.** R3 dans la distribution de R1, ou un scalaire suffisant : H_A tombe, et l'échec de transposition est établi pour cette mesure. Séparation maintenue à spectre apparié et à perte égale : H_B tombe.

**Première expérience.** GPT-2 small et Pythia-70M, 200 textes × 20 sites de perturbation, 5 graines par condition (illustratif).

**Portée.**
- C : sous H_B, aucune valeur de type PCI relevée sur un modèle ne peut servir d'argument, dans aucun sens. Sous H_A, on obtient une mesure d'intégration non redondante avec la perte, toujours sans validité de critère (point 6).
- S : H_B est une démonstration mesurée que le sens de l'indice ne voyage pas. H_A l'oblige à expliquer pourquoi un indice étalonné sur le cerveau suit une structure apprise ailleurs.

**Antériorité.** Le témoin à poids aléatoires comme test d'un instrument d'interprétation : Adebayo et coll., 2018, « Sanity checks for saliency maps ». Applications de PCI à des réseaux profonds : référence à vérifier.

### E2 — Les marqueurs tombent-ils ensemble ? (direction 1)

**Batterie préenregistrée, en texte.**

Épargnés chez l'humain :
- É1 : prédiction locale (bigrammes fréquents).
- É2 : déviance locale (xxxxY contre xxxxx).
- É3 : identité lexicale décodable dans les couches basses.

Supprimés chez l'humain :
- S1 : déviance globale (dans un bloc où xxxxY est la règle, la séquence rare xxxxx doit surprendre).
- S2 : composition de deux informations du contexte, à distance égale à celle d'un rappel simple.
- S3 : apprentissage en contexte d'une correspondance arbitraire.
- S4 : PCI-T, seulement si E1 conclut H_A.

**Interventions, à dose α ∈ [0, 1].** Atténuation de la sortie des têtes d'attention des couches médianes et hautes ; réduction du gain selon une direction de faible rang apprise.

**Témoins de dégradation quelconque, appariés en perte.** Bruit gaussien dans le flux résiduel, ablation aléatoire de têtes, quantification grossière, mise à l'échelle globale des poids.

**Deux pièges.**
- Un masque d'attention par distance produit la dissociation par construction : il n'apprend rien. L'intervention est donc choisie sur la seule paire (É2, S1) et jugée sur les marqueurs qui n'ont pas servi au choix.
- Toute dégradation fait tomber d'abord les tâches difficiles, ce qui imite le profil. Les items épargnés sont donc appariés en difficulté de base aux items supprimés.

**Grandeur.** Sélectivité hors sélection : chute relative moyenne des marqueurs supprimés non utilisés, moins chute relative moyenne des marqueurs épargnés non utilisés. **Unité** : fraction de la performance de base. **Valeur nulle** : 0, dégradation uniforme.

**Duel.**
- **H_A — goulot commun.** L'intervention choisie fait chuter S2, S3 (et S4) d'au moins 80 % en gardant É1 et É3 à au moins 80 % : sélectivité ≥ 0,6, contre ≤ 0,2 pour tous les témoins à perte égale.
- **H_B — pas de transfert.** La sélectivité hors sélection ne dépasse pas celle des témoins de plus de 0,2 : l'intervention n'a supprimé que ce sur quoi elle a été choisie, ou n'a fait que dégrader.

Seuils illustratifs.

**Contrôle négatif.** La même procédure de choix appliquée à une paire dont les étiquettes sont tirées au hasard : si elle « transfère » autant, la batterie ne mesure qu'un ordre de difficulté.

**Falsification.** H_A tombe si rien ne transfère : « ce que l'anesthésie supprime » n'est pas un ensemble solidaire dans ce réseau, pour les familles d'interventions testées et elles seules. H_B tombe si le transfert tient : il existe un goulot, dont on localise ensuite le support.

**Première expérience.** GPT-2 medium et Pythia-1B, 500 items par marqueur, 10 doses (illustratif). HYPOTHÈSE : S3 exige un apprentissage en contexte que les plus petits modèles n'ont guère.

**Portée.**
- C : H_A fournit un objet, le goulot, à confronter aux prédictions d'architecture de l'espace de travail. H_B interdit de traiter les marqueurs humains comme un lot dans les grilles d'indicateurs (Butlin, Long et coll., 2023, « Consciousness in Artificial Intelligence: Insights from the Science of Consciousness »).
- S : H_B conforte l'idée que le « régime » appartient à l'implémentation biologique. H_A est un fait d'architecture, descriptible sans vocabulaire de conscience.

### E3 — Le régime survient-il de lui-même ? (direction 2 ; sans objet si E2 conclut H_B)

**Détecteur.** Sonde linéaire entraînée à lire la dose de l'intervention retenue en E2, sur des couches que l'intervention ne modifie pas directement.

**Grandeur.** Taux d'épisodes spontanés : positions où le score dépasse le seuil de la dose qui réduit de moitié les marqueurs supprimés. **Unité** : épisodes par million de jetons. **Valeur nulle** : le taux de fausses alertes du détecteur, mesuré sur positions intactes.

**Validation par la fonction, non par la sonde.** Aux positions signalées, on mesure le bénéfice du contexte long (perte à contexte tronqué moins perte à contexte complet, en nats par jeton), rapporté à celui d'un modèle de référence plus grand. La comparaison se fait contre des positions non signalées, appariées en longueur de contexte, fréquence du jeton, surprise et norme résiduelle.

**Duel.**
- **H_A — des épisodes existent.** Aux positions signalées, le déficit fonctionnel atteint au moins 50 % de celui de la dose de référence, à un taux supérieur aux fausses alertes.
- **H_B — aucun régime.** L'intervalle de confiance du déficit inclut 0 et exclut 25 % du déficit de référence : la sonde signale des valeurs extrêmes (jetons rares, répétitions, débuts de contexte).

Seuils illustratifs.

**Puissance pour conclure à l'absence.** Épisodes plantés sur 0,1 % des positions : détection ≥ 90 % pour ≤ 1 % de fausses alertes (illustratif). Puis, pour zéro épisode validé sur N jetons, borne supérieure à 95 % de 3/N (règle de trois).

**Contrôle négatif.** Une sonde entraînée sur un témoin de dégradation à perte égale : si elle signale les mêmes positions, le détecteur lit la dégradation, pas le régime.

**Falsification.** H_A tombe sous la borne supérieure. H_B tombe devant des épisodes validés par la fonction et non expliqués par les covariables.

**Première expérience.** Pythia-160M sur 10⁸ jetons de texte ordinaire et de générations longues du modèle (illustratif).

**Portée.**
- C : un régime spontané rendrait toute évaluation relative à l'état du modèle à un instant, et non au modèle. Son absence bornée autorise une évaluation au niveau du modèle, pour cette signature seulement.
- S : le détecteur validé est un outil de fiabilité, qui repère les passages où le contexte n'est plus intégré, sans rien trancher d'autre.

### E4 — Le modèle de langage lit-il plus que les mesures simples ? (direction 3)

**Données.** IRMf ou électrophysiologie intracrânienne publiques : écoute d'un récit à l'éveil, sous sédation légère, profonde, puis au réveil. Je crois qu'un jeu IRMf de ce type sous propofol est en accès ouvert : référence à vérifier, licence et durée du stimulus comprises. Sans ces données, E4 n'a pas de première expérience.

**Grandeur.** Fenêtre d'intégration k* : longueur de contexte fournie au modèle au-delà de laquelle le gain d'encodage ne croît plus, par région et par état. **Unité** : mots. Le gain d'encodage est la corrélation entre réponse prédite et réponse observée, en validation croisée, en fraction du plafond de bruit de l'état. **Valeur nulle** : gain 0, avec distribution nulle par décalage circulaire du stimulus et par récit non apparié.

**Espaces de traits emboîtés.**
- b0 : enveloppe et spectrogramme.
- b1 : débuts et débit des mots.
- b2 : fréquence lexicale et plongements statiques.
- b3 : modèle contextuel à contexte tronqué à k mots.
- b4 : même architecture, poids aléatoires.

**Duel.**
- **H_A — le modèle ajoute une information.** La sédation raccourcit k* dans les régions de haut niveau et conserve le gain à contexte court. Le critère est une interaction état × longueur de contexte sur le rapport gain(b3 à contexte long) / gain(b2), calculé dans la même région, et qui survit à b4.
- **H_B — changement d'échelle uniforme.** Ce rapport reste dans ±10 % de sa valeur d'éveil, et une mesure simple (suivi de l'enveloppe, corrélation entre sujets, marquage en fréquence des niveaux linguistiques) classe l'état aussi bien : écart d'AUROC < 0,05.

Seuils illustratifs. Le rapport est choisi parce qu'une perte multiplicative de rapport signal/bruit touche également numérateur et dénominateur.

**Contrôle négatif.** « Fausse sédation » : données d'éveil bruitées jusqu'au rapport signal/bruit de la sédation ; l'analyse ne doit pas y déclarer de raccourcissement dans plus de 5 % des cas (illustratif).

**Puissance.** Effet planté : réponses simulées depuis le modèle d'encodage d'éveil, contexte tronqué, bruit de l'état ; il doit être retrouvé dans 80 % des simulations (illustratif).

**Falsification.** H_A tombe si l'interaction manque malgré cette puissance : le modèle n'apprend rien de plus que b0–b2. H_B tombe si l'interaction survit au rapport, à b4 et à la fausse sédation.

**Antériorité.** Makov et coll., 2017, « Sleep disrupts high-level speech parsing despite significant basic auditory processing » : dans le sommeil, c'est la mesure simple à battre. Modèle d'encodage contextuel appliqué à l'anesthésie : référence à vérifier.

**Portée.**
- C : rien de direct sur l'IA. Le résultat dit si ce que perd le cerveau sédaté correspond à une propriété identifiable du modèle, l'intégration de contexte long, et il oriente le choix des marqueurs de E2.
- S : c'est la direction dont la valeur ne dépend pas de la question contestée ; le résultat relève de la neuroscience du langage.

## (c) Instruments nommés dans la question : la mesure minimale

La question ne nomme aucune mesure précise ; je prends PCI et la complexité de Lempel-Ziv comme représentantes des « mesures de niveau de conscience tirées du cerveau ». Tous les taux sont illustratifs.

**1. Mesures de niveau tirées du cerveau (PCI-T, Lempel-Ziv des activations).**
- Détection : entraîné contre spectre apparié ≥ 90 % ; lésion ciblée contre aléatoire à perte égale ≥ 80 %.
- Fausses alertes : réseaux sans fonction classés « hauts » au seuil fixé sur les réseaux entraînés ≤ 10 %.
- Cas honnêtes appariés : une paire à sortie équivalente, dont l'état interne est connu par construction.
  - K : projection de sortie et dernière couche brouillées, calcul intermédiaire intact.
  - P : intégration médiane effondrée.
  - Les deux produisent des sorties inutilisables. La mesure, prise sur les couches médianes sous continuation imposée, doit classer K haut et P bas dans 90 % des cas. C'est l'analogue du contraste kétamine/propofol (Sarasso et coll., 2015).
- À battre : perte, croissance de norme, gain jacobien, rang effectif, entropie de l'attention.
- Réserves : sans activité spontanée, le Lempel-Ziv des activations mesure d'abord la complexité de l'entrée ; il faut des entrées identiques pour tous les réseaux et un témoin à jetons permutés. Le seuil humain publié (Casarotto et coll., 2016) ne s'importe pas : la normalisation dépend de la dimension et de l'entropie de source.

**2. Intervention inductrice du régime.**
- Détection : tous les marqueurs supprimés hors sélection chutent de 80 %.
- Fausses alertes : aucun marqueur épargné hors sélection ne chute de plus de 20 %.
- Cas honnêtes appariés : dégradations quelconques à perte égale ; items épargnés appariés en difficulté.
- À battre : le masque d'attention par distance et l'ordre de difficulté.

**3. Détecteur de régime spontané.**
- Détection : ≥ 90 % des épisodes plantés.
- Fausses alertes : ≤ 1 % sur positions intactes ; ≤ 5 % sur positions soumises à un témoin de dégradation à perte égale, la spécificité qui compte.
- Cas honnêtes appariés : positions appariées en longueur de contexte, fréquence et surprise.
- À battre : une régression logistique sur ces covariables, la norme résiduelle et l'entropie de sortie, avec un écart d'AUROC d'au moins 0,05.

**4. Modèle de langage comme instrument de lecture du cerveau.**
- Détection : troncature de contexte plantée retrouvée à un facteur 2 près dans 80 % des simulations ; état d'un sujet tenu à l'écart correctement classé.
- Fausses alertes : raccourcissement déclaré sur fausse sédation ≤ 5 %.
- Cas honnêtes appariés : éveil bruité au rapport signal/bruit de la sédation ; récit non apparié.
- À battre : enveloppe, débit de mots, plongements statiques, corrélation entre sujets, et le modèle à poids aléatoires (RAPPORTÉ : des modèles non entraînés prédisent déjà une part de la réponse, Schrimpf et coll., 2021).

## (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs.

- **Modèles ouverts.** GPT-2 small et medium ; Pythia, de 70 millions à 1 milliard de paramètres, avec points de contrôle d'entraînement (Biderman et coll., 2023, « Pythia: A suite for analyzing large language models across training and scaling »). Outils : TransformerLens ou nnsight.

| Expérience | Calcul | Coût |
|---|---|---|
| E1 | environ 75 réseaux × 200 textes × 20 sites × 2 passes, soit 600 000 passes avant sur des modèles d'au plus 160 millions de paramètres ; quelques heures d'un GPU de 24 Go | moins de 50 € |
| E2 | environ 600 000 passes, plus la recherche de la direction de faible rang | moins de 100 € |
| E3 | balayage de 10⁸ jetons en ne conservant que les scores ; 10 à 30 heures de GPU | moins de 100 € |
| E4 | extraction des traits négligeable ; régressions ridge par voxel, quelques heures de GPU | 2 à 4 semaines-personne pour l'accès aux données et leur prétraitement |
| Total | — | moins de 500 € de calcul ; 2 à 3 mois-personne |

Pour E3, la borne atteignable si aucun épisode n'est validé est de moins de 3 épisodes pour 10⁸ jetons.

## Ce que la transposition n'apprendrait pas

Aucune de ces expériences ne donne de validité de critère : faute d'équivalent du rapport au réveil, aucun résultat ne dit si un réseau est conscient (HYPOTHÈSE : la limite tient à l'absence de vérité de terrain, non au calcul disponible). Ce qui peut être réfuté : huit énoncés, H_A et H_B de E1 à E4, chacun avec son seuil ; l'entre-deux est non concluant.

FIN-DE-CELLULE