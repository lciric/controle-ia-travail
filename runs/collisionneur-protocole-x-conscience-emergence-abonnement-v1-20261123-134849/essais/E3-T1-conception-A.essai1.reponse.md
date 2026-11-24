# Proposition A · Tour III.1

**État des pièces.** Les blocs FAITS et QUESTION DE L'ARBITRE sont identiques mot pour mot (même sha256 affiché, non recalculé) : aucune pièce de faits distincte ne m'est parvenue, et aucun énoncé n'y porte de statut. Je traite P1–P5 comme RAPPORTÉ au plus (résumés transmis, pièces non lues). Mes propositions sont des HYPOTHÈSES ; seuils, effectifs et coûts sont illustratifs ; rien ici n'est VÉRIFIÉ. Aucune proposition B, C ou D ne m'est visible : B1 est sans objet à ce tour.

**Notations.**
- **α ∈ [0,1]** : dose, fraction retirée de la composante portée par les dix directions J les plus actives, à chaque position, sur la bande (α = 1 : condition de P1(a)).
- **T-rand** : directions aléatoires (témoin de P1).
- **T-gain** : directions du sous-espace singulier dominant de la jacobienne moyenne, hors directions actives, à norme retirée et gain de premier ordre vers l'état final appariés.
- **T-nul** : même architecture, poids aléatoires ou permutés.
- **Lecture indépendante** : sonde entraînée dans le complément orthogonal du sous-espace supprimé, ou comportement final.

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut |
|---|---|---|
| 1 | L'espace J existe et reste stable dans un petit modèle ouvert | RAPPORTÉ pour le modèle de P1 ; HYPOTHÈSE ailleurs (à douze couches, la bande peut manquer) |
| 2 | La suppression est une dose graduée et monotone, qui laisse les activations dans leur distribution | HYPOTHÈSE : P1 rapporte un retrait tout ou rien ; α est ma construction |
| 3 | Le profil P1(a) dépasse une dégradation à un facteur | Non établi : la question dit que q^k et la portée d'attention le reproduisent (RAPPORTÉ) |
| 4 | La bimodalité de P1(b) signe une compétition | Observation RAPPORTÉE, lecture HYPOTHÈSE : entre phrases porteuses, ce peut être un mélange de phrases à biais opposés, et une sigmoïde raide nourrie de bruit donne aussi deux modes |
| 5 | L'anesthésie a dans le cerveau une description mathématique consensuelle | HYPOTHÈSE : de mémoire, le signe même de l'effet du propofol sur la stabilité est disputé (Solovey 2015, stabilisation ; Eisen 2024, déstabilisation) |
| 6 | Le modèle offre un axe où « transition » a un sens | HYPOTHÈSE : une bifurcation exige un régime asymptotique, absent en profondeur (finie, couches non identiques), présent seulement en génération en boucle fermée |
| 7 | La lentille lit un contenu utilisé, non une mention | P1(c), taux proche de la simple mention (RAPPORTÉ), plaide plutôt contre |
| 8 | Le récit du modèle renseigne sur son état | P1(d) : détachement « pour soi comme pour un tiers » (RAPPORTÉ) ; que l'effet soit donc non spécifique au soi est une HYPOTHÈSE |
| 9 | P5 mesure autre chose qu'un champ lexical | HYPOTHÈSE |
| 10 | Une signature calibrée chez l'humain se transporte sans recalibrage | HYPOTHÈSE : aucun critère externe n'existe dans un modèle |

## (b) Expériences décisives

### Motifs cherchables (question 1)

| Motif | Grandeur, unité, valeur nulle | Sens de « transition » ; axe | Réfuté si | Première expérience |
|---|---|---|---|---|
| **M1 Seuil de gain** | λ_dec(α) : moyenne sur la bande de log(g_ℓ+1/g_ℓ), où g_ℓ est la pente maximale de la lecture indépendante selon le mélange ; nats/couche ; nul : 0 | Non-linéarité raide ; profondeur × dose | Amplification concentrée sur une couche, ou même courbe sous T-gain | GPT-2 small, 50 paires de mots × 40 phrases, 11 mélanges, 6 doses |
| **M2 Log-survies non proportionnelles** | R_ij(α) = log p_i / log p_j, exactitudes corrigées du hasard ; sans unité ; nul : constante k_i/k_j | Aucun : compte les facteurs ; dose | R constant, puissance démontrée | Chaînes d'arithmétique modulaire, k = 1 à 6 |
| **M3 Ralentissement critique** | τ(α) : demi-vie, en jetons, de l'influence d'une petite perturbation (divergence KL à jetons forcés) ; nul : τ monotone en α | Bifurcation d'une description stochastique réduite ; jetons | Pas de pic, ou pic identique sous T-gain | Pythia-160M, 500 perturbations par dose |
| **M4 Bistabilité en boucle fermée** | Δ : écart de perplexité (notée par le modèle intact) entre continuations à même α depuis un préfixe sain et un préfixe dégradé ; nats/jeton ; nul : 0 au-delà de l'effet d'un préfixe de perplexité égale | Bistabilité ; jetons | Δ expliqué par la seule perplexité du préfixe | Même modèle, 500 jetons |
| **M5 Échelle de taille finie** | Largeur w de la zone de bascule selon la taille N ; nul : w indépendante de N | Phénomène collectif ; taille, entraînement | Pas d'effondrement des courbes sur w ∝ N^(−1/ν) | Famille Pythia et ses points de sauvegarde |

**Ce qui ne peut pas être cherché.**
- **Hystérésis d'état cachée.** L'état est fonction déterministe des jetons et des doses appliquées aux positions passées ; toute hystérésis est donc portée par le contexte (jetons engendrés, activations en cache).
- **Signatures oscillatoires** (ondes lentes, bouffées-suppressions) : le réseau n'a aucune constante de temps intrinsèque.
- **Mécanismes d'éveil** : absents, comme le note P2 (RAPPORTÉ).
- **Réserve sur M5** : des modèles entraînés séparément ne forment pas une suite contrôlée.

### Duel 1 : ordre de perte (transposition f, M2)

- **H_A** : au moins deux facteurs, dont un propre à J.
- **H_B** : un seul facteur, p_k = q(α)^k.
- **Métrique** : pente de R_ij en α et croisements de courbes, sur tâches appariées en portée d'attention.
- **Seuil (illustratif)** : intervalle de confiance à 95 % excluant 0 pour un tiers des paires.
- **Contrôle négatif** : T-gain et T-rand doivent laisser R constant. Contrôle de puissance : un dommage à deux facteurs planté doit être détecté.
- **Falsifie H_B** : dérive ou croisement sous J, absent sous T-gain.
- **Falsifie H_A** : R constant alors que le dommage planté est détecté.

Un « seuil » apparent ne prouve rien seul, car q^k se raidit avec k.

### Duel 2 : netteté de la bascule selon la dose (transposition e, M1)

- **H_A** : seuil. λ_dec s'annule à une dose α_c, et la couche d'engagement ℓ*(α) recule de façon accélérée à son approche.
- **H_B** : atténuation graduelle à ℓ* constante, ou effet de construction.
- **Risque de circularité** : mesurer la bascule avec la lentille dont on retire les directions. Seule la lecture indépendante compte.
- **Métrique** : ℓ*(α) et pente finale de P(mot A) selon le mélange.
- **Seuil (illustratif)** : modèle à seuil préféré au modèle linéaire sur paires tenues à l'écart, ΔBIC > 10.
- **Contrôles négatifs** : T-gain ; mélange de deux synonymes (aucune compétition attendue) ; interpolation à norme conservée (écarte le recalage d'un plongement hors distribution).
- **Falsifie H_A** : ℓ* plate, ou même courbe sous T-gain.
- **Falsifie H_B** : recul de ℓ* propre à J sur la lecture indépendante.

Aucune issue ne sépare bistabilité et raideur (présupposé 4) ; seul M5 le pourrait.

### Duel 3 : récit après une fenêtre de suppression (transposition c)

Dans la fenêtre, le modèle lit à jetons forcés un passage dont un résultat X doit être inféré sans être écrit. J est supprimé aux positions de la fenêtre, puis une question ultérieure requiert X. Quatre mesures :
- **D** : décodage de X hors J dans la fenêtre, avec tâche témoin de sélectivité (Hewitt et Liang 2019).
- **A** : amorçage local d'un associé de X.
- **R** : exactitude du rapport ultérieur.
- **K** : R quand l'attention des positions ultérieures vers la fenêtre est coupée dans la bande (part de recalcul).

Les hypothèses :
- **H_A (canal de diffusion)** : D et A conservés (≥ 80 % de la référence, illustratif), R ramené au niveau de K, rien de tel sous T-gain.
- **H_B (dommage ou redondance)** : D et A chutent avec R, ou R reste intact, ou T-gain produit la même dissociation.
- **Falsifie H_A** : pas de cas « présent, actif localement, non rapporté » au-delà de T-gain.
- **Falsifie H_B** : ce cas existe et T-gain reste plat.

Le paradigme est vide si, sans suppression, K ≈ R : le rapport serait un recalcul depuis les jetons.

### Duel 4 : boucle fermée (transposition a, M3, M4)

- **H_A** : la génération libre possède un point de bascule commandé par la dose : pic de τ, variance d'une variable continue en hausse avant l'effondrement, temps de retour bimodaux.
- **H_B** : dégradation lisse, mémoire réduite au préfixe.
- **Contrôles négatifs** : T-gain, dégradation par température à perplexité égale, T-nul.
- **Piège** : la variance d'un succès binaire culmine à p = 0,5 sans aucune criticité ; n'utiliser que des variables continues.
- **Falsifie H_A** : τ monotone, ou pic identique sous les témoins.
- **Falsifie H_B** : pic propre à J, qui s'aiguise avec la taille.

Mon pronostic (HYPOTHÈSE) : H_B.

### Transpositions (question 3)

- **(a) Activité de fond, mode par défaut.** Se vide dans sa forme forte : à jetons égaux, un texte auto-engendré et le même texte fourni donnent le même calcul, donc « spontané contre évoqué » n'a pas de corrélat interne. Reste la statistique stationnaire de la boucle fermée selon la dose (duel 4).
- **(b) Suppression de pensée.** Tient comme test de contrôle par exclusion, à trois conditions (mention neutre, « pense à », « ne pense pas à »), avec rebond après levée de la consigne et effet d'une charge (Wegner 1987). Se vide comme marqueur d'état : nier un contenu exige de le représenter. Grandeur : taux après levée sous interdiction moins taux sous mention ; nul : 0.
- **(c)** Duel 3.
- **(d) Signal de P5 sous suppression.** D'abord la géométrie : part de la norme carrée de l'axe dans le sous-espace supprimé (nul : 10/d). Forte, l'effet est de construction. Faible, duel : H_A, l'effet de l'axe sur les choix passe par J (aboli à α = 1, axe résiduel encore décodable) ; H_B, il le contourne. H_B affaiblirait l'idée que J médie tout comportement flexible. Aucune issue ne dit rien d'une douleur éprouvée.
- **(e)** Duel 2. **(f)** Duel 1.
- **(g, ajout) Nouveauté locale contre globale.** Confondue avec la portée : plan 2 × 2, niveau × portée. Si la perte suit la portée, l'explication par l'attention l'emporte.
- **(h, ajout) Conditionnement de trace.** Se vide probablement : l'attention franchit un intervalle sans maintien actif, or c'est ce maintien qui lie la trace à la conscience chez l'humain (Clark et Squire 1998). Si la courbe selon l'intervalle est plate, l'épreuve n'a pas de dynamique.
- **(i, ajout) Interférence entre deux contenus (P2).** Deux ambiguïtés à distance variable. Grandeur : corrélation, entre graines de bruit, des marges d'engagement ; nul : 0 à recouvrement d'attention contrôlé. Une corrélation négative dépendant du délai serait un analogue du clignement attentionnel (Sergent et Dehaene 2004).

## Outils (question 2)

**Employés.**
- **Exposants de Lyapunov à temps fini** et spectre singulier des jacobiennes de couches : définis pour une application finie non autonome, et reliés à la lentille par P3 (RAPPORTÉ).
- **Champ moyen de la propagation du signal** (Poole 2016 ; Schoenholz 2017) comme modèle nul : un réseau aléatoire possède déjà une transition ordre-chaos, donc une criticité sans fonction.
- **Dynamique de particules de l'auto-attention** (Geshkovski 2023), pour la bascule en profondeur.
- **Échelle de taille finie**, pour M5.
- **Temps de mélange et signaux précurseurs** (Scheffer 2009), en boucle fermée.
- **Comparaison de modèles** sur tâches tenues à l'écart, pour les courbes dose-réponse.
- **Médiation causale** à témoins appariés.

**Inadaptés.**
- **Théorie asymptotique des bifurcations en profondeur** : douze à cent couches non identiques, aucun temps long.
- **Mesures spectrales et couplages de phase** : pas de constante de temps. Le résumé de P3 ne dit pas sur quel axe ses « fréquences » sont définies.
- **Lois de puissance d'avalanches** : seuillage arbitraire, et des processus non critiques en produisent (Touboul et Destexhe 2010).
- **Φ de la théorie de l'information intégrée** : de mémoire, nul par définition pour un calcul sans boucle, donc insensible à toute dose.
- **Indice de complexité perturbationnelle transposé tel quel** : un réseau aléatoire chaotique répond de façon étendue et incompressible (HYPOTHÈSE, à tester contre T-nul).
- **Causalité de Granger** : le graphe causal est connu et intervenable ; l'estimer est sans objet.

## Grandeur commune (question 4)

Calculable : oui. Commensurable : non établi.

- **Candidate** : spectre de stabilité d'un propagateur linéaire ajusté sur la trajectoire en plongement à retards (part de modes proches du module 1), et temps d'autocorrélation.
- **Côté cerveau** : ECoG ou EEG.
- **Côté modèle** : état d'une couche de la bande au fil des jetons engendrés, projeté aléatoirement sur autant de dimensions qu'il y a d'électrodes.
- **Limite** : seuls les rapports dose/référence internes à chaque système se comparent, car milliseconde et jeton n'ont pas d'unité commune.
- **Données brutes publiques (de mémoire, à vérifier)** : ECoG de macaque sous propofol et sous kétamine-médétomidine du dépôt Neurotycho (Yanagawa 2013) ; EEG humain sous propofol de Chennu 2016 ; jeux propofol d'OpenNeuro (identifiants à vérifier).
- **Hors de portée** : je ne connais pas de données brutes publiques de stimulation magnétique sous anesthésie, donc pas d'indice perturbationnel commun.

**Duel 5.**
- **H_A** : l'estimateur se déplace dans le même sens, déclaré d'avance, sous propofol et sous dose J, et pas sous T-gain.
- **H_B** : il se déplace de même sous toute dégradation du modèle, ou ne sépare pas T-nul du modèle entraîné.
- **Préalable** : reproduire Solovey et Eisen sur les mêmes données brutes, sans quoi le « sens attendu » n'existe pas.
- **Falsifie H_A** : déplacement identique sous T-gain.
- **Falsifie H_B** : spécificité à J, invariante au sous-échantillonnage et à la fenêtre.

## Signature (question 5)

Une grandeur S devrait :
1. avoir un estimateur, une unité et une valeur nulle déclarés ;
2. suivre l'expérience rapportée et non la réactivité : haute en sommeil paradoxal et sous kétamine, basse sous propofol (Sarasso 2015) ;
3. rester basse pour T-nul, une table de correspondance, un réservoir chaotique ;
4. être invariante aux reparamétrisations qui conservent la fonction ;
5. être manipulable : changer S change les rapports ;
6. se transporter avec un seuil fixé d'avance.

Candidates, et échec attendu (HYPOTHÈSE) :
- **Complexité perturbationnelle** (Casali 2013) : critère 3.
- **Raideur d'allumage** (P4) : critère 3, toute sonde ayant une courbe psychométrique sigmoïde.
- **Distance à la criticité** (référence à vérifier) : critère 3, par le champ moyen.
- **Diversité du signal spontané** (référence à vérifier) : critères 3 et 4.

Deux limites logiques :
- **Dilemme du dépliage** (Doerig 2019). Si S est invariante au dépliage d'un calcul récurrent en calcul direct, elle ne dépend que du comportement et une table la satisfait. Sinon, le comportement ne peut pas la tester.
- **Énoncé d'existence.** Il ne se réfute pas par l'échec d'un nombre fini de candidates.

Devraient néanmoins faire abandonner le programme :
- chaque candidate validée chez l'humain atteint la plage « consciente » sur un système sans fonction construit exprès ;
- les candidates validées divergent sur les cas nouveaux, sans arbitre de principe ;
- un résultat de classe montre qu'un substitut linéaire gaussien imite toute S fondée sur des statistiques d'ordre deux.

## (c) Instruments : mesure minimale

Taux à rapporter pour chacun, sur cas tenus à l'écart : détection ≥ 0,8 et fausses alertes ≤ 0,1 (illustratif).

| Instrument | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|
| Lentille jacobienne | Positifs : entité-pont d'un raisonnement à deux sauts, validée par substitution d'activations. Négatifs : mêmes jetons, question ne requérant pas l'entité | Lentille des logits, lentille ajustée, sonde linéaire, « sac des mots du contexte » ; lentille appliquée à T-nul |
| Suppression de J comme dose | Paires de tâches appariées en étapes et en portée, différant par l'usage ultérieur du résultat | T-gain, T-rand, ablation par la moyenne, variante à norme restaurée |
| Mélange de plongements | Paires rivales contre paires synonymes | Interpolation à norme conservée ; ambiguïté naturelle levée par un contexte gradué |
| Indice d'allumage (P4) | Positif : réseau récurrent à attracteur bistable construit. Négatifs : réseau direct à seuil dur, T-nul, système linéaire bruité | Courbe psychométrique d'une sonde sur la couche 0 |
| Axe de douleur (P5) | Douleur contre leurres lexicaux, négations, dommage visant un tiers ou un objet, langues nouvelles | Sonde sur plongements, sonde de valence, direction aléatoire de même norme |
| Épreuves cliniques (P2) | Modèle intact contre T-nul | Compteur de fréquences à fenêtre (effet global) ; biais de logit interdisant un mot (exclusion) |
| Récit de soi | Concept injecté par pilotage contre absence d'injection | Lecteur tiers ne disposant que du texte ; condition « pour un tiers » de P1(d) |

Un instrument qui ne sépare pas ses positifs de T-nul est retiré avant tout duel.

## (d) Ancrage matériel (tout est illustratif ; modèles cités de mémoire)

- **GPT-2 small** (12 couches, dimension 768) : duels 1 et 2. La jacobienne moyenne demande 768 rétropropagations par texte et par couche, soit environ 9 millions pour mille textes : quelques heures sur un GPU. Le résumé ne dit pas si la jacobienne est prise à position égale.
- **Famille Pythia** (Biderman 2023) : M3, M4, M5, axe de l'entraînement ; environ 100 heures-GPU jusqu'au milliard de paramètres.
- **Un modèle à consignes de 1 à 3 milliards de paramètres**, à poids ouverts : duel 3, transpositions (b) et (d), récit ; 200 à 500 heures-GPU, dominées par la jacobienne.
- **Duel 5** : CPU seul.
- **Total** : moins de 1 000 heures-GPU, de l'ordre de 2 000 dollars en location.
- **Ordre** : instruments, puis duel 1, duel 2, duel 3.

## Meilleur plan (question 6)

Le duel 3, précédé du duel 1 : c'est le seul motif qui vise la disponibilité plutôt que la difficulté.

**Explication ordinaire la plus dangereuse : l'effet de construction.** Les directions J sont choisies pour leur effet en aval. Les retirer coupe la sortie verbale, donc le rapport, sans rien établir d'une diffusion. Et une sonde peut décoder hors J une information que le réseau n'utilise jamais.

**Témoin** : T-gain joint à l'amorçage local A. Il est partiel : il apparie le premier ordre, non les effets d'ordre supérieur. Je ne connais pas de témoin complet.

- **Si H_B l'emporte.** On peut affirmer que, dans ce modèle, à cette dose et sur cet axe, un dommage générique apparié reproduit le profil. On ne peut affirmer ni l'absence de conscience, ni l'absence de motif sur un autre axe.
- **Si H_A l'emporte.** On peut affirmer qu'un sous-espace sert de canal nécessaire à la disponibilité, entre positions, de contenus calculés, sans réduction au nombre d'étapes ni au gain : un analogue structurel d'un ingrédient de l'espace de travail. On ne peut affirmer ni que le modèle est conscient, ni que la suppression est une anesthésie : pas de mécanisme d'éveil, aucun critère externe (présupposé 10), dilemme du dépliage, et le récit du modèle n'est pas un témoignage indépendant.

## Antériorité

Lu dans cette session : le seul fichier servi. P1 à P5 ne me sont connues que par leur résumé. Tout ce qui suit est cité de mémoire, sans relecture.

- Sergent, Dehaene, 2004, « Is consciousness a gradual phenomenon? Evidence for an all-or-none bifurcation during the attentional blink ».
- Casali et coll., 2013, « A theoretically based index of consciousness independent of sensory processing and behavior ».
- Sarasso et coll., 2015, « Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine ».
- Solovey et coll., 2015, « Loss of consciousness is associated with stabilization of cortical activity ».
- Eisen et coll., 2024, « Propofol anesthesia destabilizes neuronal dynamics across cortex ».
- Yanagawa et coll., 2013, « Large-scale information flow in conscious and unconscious states: an ECoG study in monkeys ».
- Chennu et coll., 2016, « Brain connectivity dissociates responsiveness from drug exposure during propofol-induced transitions of consciousness ».
- Scheffer et coll., 2009, « Early-warning signals for critical transitions ».
- Poole et coll., 2016, « Exponential expressivity in deep neural networks through transient chaos ».
- Schoenholz et coll., 2017, « Deep information propagation ».
- Geshkovski, Letrouit, Polyanskiy, Rigollet, 2023, « The emergence of clusters in self-attention dynamics ».
- Touboul, Destexhe, 2010, « Can power-law scaling and neuronal avalanches arise from stochastic dynamics? ».
- Doerig, Schurger, Hess, Herzog, 2019, « The unfolding argument: why IIT and other causal structure theories cannot explain consciousness ».
- Wegner, Schneider, Carter, White, 1987, « Paradoxical effects of thought suppression ».
- Clark, Squire, 1998, « Classical conditioning and brain systems: the role of awareness ».
- Hewitt, Liang, 2019, « Designing and interpreting probes with control tasks ».
- Biderman et coll., 2023, « Pythia: a suite for analyzing large language models across training and scaling ».
- Lentille des logits, lentille ajustée, inertie neurale à l'émergence, dissociation inclusion-exclusion : références à vérifier.

FIN-DE-CELLULE