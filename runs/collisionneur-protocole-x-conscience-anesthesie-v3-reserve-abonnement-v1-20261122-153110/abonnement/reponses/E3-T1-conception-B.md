# Proposition B, tour III.1

**État des pièces**
- J'ai lu `texte-servi.md` seul, en entier, sans autre outil ni recherche.
- Les blocs FAITS et QUESTION ont un contenu identique et annoncent la même empreinte sha256. Je n'ai pas pu la recalculer, donc elle n'est pas vérifiée.
- Le bloc FAITS n'attribue aucun statut. Les « travaux de 2026 » n'ont ni auteur, ni modèle, ni taille d'effet : je les traite comme RAPPORTÉ, non attribuable. Rien n'est VÉRIFIÉ dans ce texte.
- Je suis la *proposition* B. Elle n'a aucun lien avec la *position* B. Le tour se fait à l'aveugle, donc la règle B1 est sans objet ici.
- **Tous les chiffres ci-dessous sont illustratifs.**

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition (conséquence si elle est fausse) | Statut |
|---|---|---|
| S1 | Un petit ensemble U de directions produit le profil décrit (sinon, il n'y a rien à tester avant une réplication). | RAPPORTÉ, non attribuable |
| S2 | U a été trouvé sans utiliser les tâches ni les items où l'on mesure le profil (sinon, le profil est circulaire). | HYPOTHÈSE |
| S3 | Le partage entre fonctions gardées et perdues suit une fonction, pas un format. Or les tâches « gardées » ont d'ordinaire une réponse courte et les « perdues » une génération longue (sinon, c'est un effet de longueur). | HYPOTHÈSE ; la pièce ne précise pas les formats |
| S4 | L'anesthésie fournit une échelle graduée unique (sinon, « la rejouer » n'a pas de cible). | HYPOTHÈSE. Contre elle, RAPPORTÉ de mémoire : les profils dépendent de l'agent (Sarasso et al. 2015), et ne pas répondre n'est pas la même chose que ne rien vivre (Sanders et al. 2012) |
| S5 | Les six tâches ont des équivalents sous anesthésie. Or un sujet anesthésié ne traduit ni ne résume (sinon, la correspondance est arbitraire). | HYPOTHÈSE |
| S6 | « Dégradation globale égale » désigne une grandeur unique (sinon, le choix de la métrique fabrique l'issue). | HYPOTHÈSE |
| S7 | Le modèle n'a « ni activité autonome ni état ». En génération libre pourtant, la boucle autorégressive et le cache clé-valeur forment un état entretenu par la sortie. La prémisse de B devient alors testable (E3). | HYPOTHÈSE, en partie fausse au sens étroit (RAPPORTÉ de mémoire ; vérifiable dans le code) |
| S8 | A et B épuisent les cas. Il existe une troisième voie : un profil propre à U mais dû à une fonction banale (composition en plusieurs étapes, identité de langue). Dans ce cas, une victoire empirique de A ne validerait pas son interprétation. | HYPOTHÈSE |
| S9 | Le rapport du sujet a un équivalent dans le modèle. Or l'auto-rapport d'un modèle ablaté est produit par le réseau ablaté lui-même, sans canal indépendant après coup. | HYPOTHÈSE |

## 0. Une expérience peut-elle départager A et B ?

**Oui pour la question empirique. Non pour la question de la transposition.**

- **Question empirique.** Quand on supprime U, le profil diffère-t-il de celui d'un témoin à dégradation globale égale, fixée avant la mesure ? « Profil propre » et « même profil » s'excluent dès que la métrique d'appariement et les marges sont fixées. Je traite les points 1 à 3 pour cette question.
- **Question de la transposition.** Ce régime est-il l'analogue d'une perte de conscience ? On ne peut pas trancher, pour une raison logique. Chez l'humain, le statut de l'éveil est connu par le rapport du sujet, et le rapport au réveil calibre en partie l'autre pôle. Dans un modèle, le statut des deux pôles est inconnu : comparer deux inconnues ne calibre aucune des deux. Je traite aussi les points 4 à 6 pour cette raison.

**Asymétrie, annoncée d'avance.**
- Un profil propre falsifie la prédiction de B, mais pas sa thèse : faute de pôle connu, la ressemblance reste non diagnostique.
- Un même profil falsifie la prédiction de A et lui retire sa principale pièce empirique.
- L'expérience peut donc réfuter l'argument de A, mais seulement la prédiction de B.

## 1. Un « état analogue à l'anesthésie » a-t-il un sens ?

**Au sens fort, non.** Trois critères manquent :
1. Un pôle dont le statut conscient est établi en dehors de la manipulation.
2. Un canal de rapport indépendant du réseau manipulé.
3. Un système d'éveil sur lequel l'intervention agirait comme antagoniste. Chez l'humain, l'anesthésie agit sur les systèmes d'éveil. Chez le macaque, une stimulation thalamique centrale renverse l'état (RAPPORTÉ de mémoire : Brown, Lydic & Schiff 2010 ; Redinbaugh et al. 2020).

**Au sens dégonflé, oui**, sous un nom neutre : *régime à profil sélectif* (RPS). Ce nom ne prétend rien sur la conscience.

- **Intervention.** Aux couches ℓ ∈ L et à toutes les positions : h ← h − α·UUᵀ(h − μ_ℓ).
  - U est une matrice orthonormée à k colonnes.
  - μ_ℓ est la moyenne sur un corpus de référence.
  - α ∈ [0 ; 1].
  - On remplace par la moyenne plutôt que par zéro, pour limiter la sortie de distribution.
- **Grandeurs mesurées.**
  - **G** : divergence KL moyenne par jeton entre le modèle intact et le modèle modifié. Elle est mesurée en forçage par l'enseignant, sur un corpus neutre tenu à part. Unité : nats par jeton. Valeur nulle : 0.
  - **d_t** = (s_t intact − s_t modifié) / (s_t intact − s_t plancher). Le plancher est le hasard, ou une sortie dégénérée déclarée d'avance pour les tâches génératives. Sans unité : 0 = intact, 1 = plancher.
  - **S** = moyenne des d_t des tâches « perdues » − moyenne des d_t des tâches « gardées ». S est compris dans [−1 ; 1]. Valeur nulle : 0.
  - **Σ** = S_U − S_témoin, à G égal. Valeur nulle : 0, c'est-à-dire aucune spécificité au-delà d'une dégradation générique.
  - **T½** : demi-vie de la persistance après relâchement (E3), en jetons. Valeur nulle : 0.
- **Critère.** Il y a RPS si Σ ≥ 0,15 et S_U > 0, sur des tâches et des formats tenus à part, dans deux familles de modèles.
- **Ce que j'exclus.** La réversibilité est automatique ici : α → 0 restaure tout. Elle est centrale chez l'humain mais ne discrimine rien dans un modèle, donc je l'exclus des critères.

## 2. Expériences (livrable b ; seuils illustratifs)

**Fixé avant toute mesure**
- Modèles M1 et M2 : deux familles à poids ouverts, de 1 à 3 milliards de paramètres, en version instruite.
- U est soit fourni par les auteurs de 2026, soit retrouvé par une procédure déclarée d'avance, sur des tâches distinctes des six tâches de test.
- Conditions de validité :
  - chaque tâche, sur le modèle intact, est au moins 20 points au-dessus du plancher et sous 95 % ;
  - G est apparié à ± 5 % ;
  - les items de test n'ont pas servi à choisir U ;
  - l'analyste ne sait pas quelle famille est laquelle jusqu'au verrouillage.
- L'appariement principal se fait sur G. Appariements secondaires : entropie croisée, fraction de variance retirée. Si le verdict change selon la métrique, l'issue est « aucune ».

**Témoins, tous appariés en G**
- T-hasard : 200 sous-espaces aléatoires de dimension k, dans les mêmes couches. Ils donnent la distribution nulle de S.
- T-variance : sous-espaces tirés parmi les premières composantes principales.
- T-bruit : bruit gaussien.
- T-poids : quantification ou élagage des poids, soit un dommage sans direction.
- T-sortie : hausse de la température d'échantillonnage.
- Témoin positif : la direction de refus d'Arditi et al. (2024), dont l'effet est documenté.

### E1 : spécificité à dégradation égale, croisée avec le format

On croise les six familles de tâches avec deux formats :
- **Format discriminatif** : choix par vraisemblance parmi quatre options aux leurres appariés, y compris pour le raisonnement à plusieurs sauts, la traduction et le résumé.
- **Format génératif** : réponse libre, y compris pour la classification (étiquette justifiée), l'extraction et la grammaticalité (réécriture corrigée).

Σ est calculé contre chaque famille de témoins.

| | H_A : profil propre | H_B : même profil |
|---|---|---|
| Prédiction | Contre toutes les familles de témoins et dans les deux formats : Σ ≥ 0,15, avec une borne basse de l'IC à 95 % au-dessus de 0,05. S_U dépasse le 99ᵉ centile de T-hasard. | Contre au moins une famille de témoins et dans les deux formats : l'IC à 90 % de Σ tombe dans [−0,05 ; 0,05] (double test unilatéral). |
| Falsifiée par | l'équivalence avec une famille | Σ ≥ 0,15 hors marge contre toutes les familles |

Cas hors duel, déclarés d'avance :
- Σ > 0 en génératif seulement : le profil suit le format. A est falsifié au sens fonctionnel, sans que B soit confirmé.
- Σ ≤ −0,15 : les deux positions sont falsifiées.
- Tout autre résultat : « aucune ».

Les effectifs sont fixés par un pilote sur des items séparés, pour une puissance de 0,9, soit 400 à 600 items par cellule.

### E2 : ordre de perte selon la dose (« l'échelle graduée »)

- α varie en huit paliers. Pour chacune des douze cellules tâche × format, on relève α₅₀, la dose à laquelle d_t = 0,5.
- On construit un prédicteur mécanique de fragilité, F : l'ordre des marges du modèle intact (log-vraisemblance de la bonne réponse moins celle de la meilleure concurrente).
- Condition préalable : sous les témoins, la corrélation de rangs de Kendall entre l'ordre de perte et F doit valoir au moins 0,8. Sinon, E2 ne conclut pas.

| | H_A | H_B |
|---|---|---|
| Prédiction | r_K(U, F) ≤ 0,4, hors de la distribution des témoins, et reproduit dans M2 | r_K(U, F) dans la distribution des témoins |
| Falsifiée par | r_K dans cette distribution | r_K ≤ 0,4 hors de cette distribution |

La pente de la courbe dose-réponse est rapportée, sans valeur de verdict. Un seuil abrupt propre à U serait une condition pour une lecture « par ignition », pas une preuve.

### E3 : lésion ou régime ? (test de la prémisse de B)

- On prend un texte de 1 024 jetons. L'intervention ne s'applique qu'aux positions 256 à 511, puis elle est relâchée. On mesure ensuite la KL jeton par jeton.
- Deux modes :
  - **forçage par l'enseignant** : l'effet résiduel ne passe que par les clés et valeurs calculées pendant l'intervention ;
  - **génération libre** : le modèle consomme sa propre sortie.
- T½ est le nombre de jetons nécessaires pour que la KL retombe sous la moitié de sa valeur dans la fenêtre d'intervention.

| | H_A : régime auto-entretenu propre à U | H_B : lésion sans état |
|---|---|---|
| Prédiction | T½(U) / T½(témoin) ≥ 3 en forçage, à G égal dans la fenêtre | rapport dans [0,67 ; 1,5] |
| Falsifiée par | rapport dans [0,67 ; 1,5] | rapport ≥ 3 |

Même positive, E3 ne montrerait qu'une propagation par la mémoire de contexte, ni éveil ni conscience.

**Une position rend-elle certaines issues ininterprétables ?**
- La thèse de B rend toute issue ininterprétable pour la conscience, mais pas pour le profil.
- La seconde branche de A, « chercher le motif dans les activations ordinaires », aussi, si la recherche se fait après coup : elle trouvera toujours un motif.
- Version admissible, déclarée d'avance : sur des entrées ordinaires, la norme de la projection sur U prédit-elle les erreurs item par item des tâches « perdues » mieux que la même norme sur T-hasard et mieux que F ?
  - H_A : gain d'AUC ≥ 0,05.
  - H_B : équivalence à ± 0,02 près.

## 3. Données humaines brutes

**Oui, comme référence ordinale et pour tester la spécificité du côté humain. Non comme étalon de la conscience.**

Candidats, tous cités de mémoire, disponibilité publique à vérifier :
- **Chennu et al. (2016)** : EEG sous sédation graduée au propofol, avec une tâche auditive et une mesure de la réponse. Données déposées publiquement, à mon souvenir.
- **Davis et al. (2007)** : IRMf sous sédation. La réponse à la parole est conservée, le traitement de l'ambiguïté sémantique est aboli. C'est un équivalent langagier, parmi ceux que je connais, du partage entre fonctions gardées et perdues.
- **Paradigme local-global (Bekinschtein et al. 2009)** : l'effet local est conservé, l'effet global disparaît sans conscience de la règle. Études sous sédation : référence à vérifier.
- **Jeu d'IRMf d'anesthésie de l'université du Michigan** : référence à vérifier.

Usage :
1. Pour chaque sujet, extraire l'ordre de perte des niveaux de traitement en fonction de la concentration au site effecteur.
2. Déclarer d'avance la correspondance entre niveaux humains et tâches du modèle, avant toute mesure sur le modèle. Ce choix est un degré de liberté et doit être annoncé comme tel.
3. Tester la spécificité du côté humain, en duel :
   - H_A : l'ordre sous anesthésie est propre (r_K < 0,5 avec chacune des autres dégradations : privation de sommeil, inattention, alcool) ;
   - H_B : r_K ≥ 0,8 avec au moins une de ces dégradations.

   De mémoire, l'effet global disparaît aussi sous inattention (Bekinschtein et al. 2009). Si B l'emporte ici, ressembler à l'anesthésie ne signifie rien pour un modèle, et le diagnostic de B serait établi du côté humain.
4. Exiger que l'ordre sous U ressemble plus à l'ordre sous anesthésie que ne le font les témoins et les dégradations humaines non anesthésiques.

Limite : aucune donnée humaine ne porte sur le raisonnement à plusieurs sauts, la traduction ou le résumé sous anesthésie. La comparaison reste ordinale et passe par une correspondance choisie.

## 4. Ce que chaque issue permet d'affirmer selon les théories

Notations : **IA** = profil propre ; **IB** = même profil ; **E3+** = persistance propre à U.

| Théorie | IA | IB | E3+ |
|---|---|---|---|
| Espace de travail global (Mashour et al. 2020) | U est compatible avec un goulot de l'intégration en plusieurs étapes. Ni ignition, ni diffusion, ni rapport ne sont montrés. | U n'est pas ce goulot ; rien sur le reste du modèle. | Maintien par le contexte ; la diffusion globale manque. |
| Information intégrée (Oizumi et al. 2014) | Rien : Φ porte sur la structure causale physique et s'annule pour un système à propagation avant (de mémoire). | Rien | Rien |
| Traitement récurrent (Lamme 2006) | Rien : une passe avant n'est pas récurrente. | Rien | Récurrence par la boucle de sortie ; il reste contesté qu'elle compte. |
| Ordre supérieur (Brown, Lau & LeDoux 2019) | Rien, sauf si U représente des états du modèle. À tester en duel comme E1, sur la calibration entre confiance et exactitude. | Idem | Rien |
| Approches biologiques | Rien : l'anesthésie se définit par son action sur l'éveil d'un organisme. | Rien ; rejoint la thèse de B. | Rien |

Valable pour toutes les théories :
- Aucune issue ne permet d'écrire qu'un modèle « était conscient et a perdu cet état », ni qu'il ne l'est pas.
- IA permet une affirmation d'interprétabilité : U a une spécificité fonctionnelle que n'expliquent ni la dégradation générique, ni le format, ni la fragilité.
- IB permet une affirmation de méthode : dans ce modèle, la ressemblance avec l'anesthésie n'est pas diagnostique.
- Pour une grille d'indicateurs (Butlin et al. 2023), IA ajouterait au plus un indicateur fonctionnel.

## 5. Vérification hors de l'équipe

- **Pré-enregistrement public horodaté** : code avec empreinte, métriques, règle d'appariement, seuils, items et partitions.
- **Publication** de U, des graines des témoins, des sorties brutes et des scripts. Un script unique recalcule Σ, T½ et α₅₀ en quelques heures sur un GPU.
- **Réplication indépendante** : une équipe reçoit la procédure mais pas U, retrouve U sur M2 et rejoue E1 à E3.
- **Collaboration adversariale** : des tenants de A et de B signent les critères avant la mesure. Modèle : l'essai « espace de travail global contre information intégrée » du Cogitate Consortium (Nature, 2025 ; titre exact : référence à vérifier).
- **Équipe rouge** chargée de reproduire Σ par une intervention triviale : format, longueur, température, quantification, identité de langue. Un succès annule tout résultat favorable à A.
- **Côté humain** : réanalyse des données publiques par un laboratoire extérieur, avec la correspondance déclarée d'avance.

## 6. L'explication triviale la plus dangereuse

**Le format et la longueur de sortie.**
- Les tâches « gardées » donnent d'ordinaire une réponse courte. Les « perdues » demandent une génération longue, où les erreurs par jeton s'accumulent.
- Toute perturbation qui touche la cohérence sur la durée, la fin de réponse ou l'identité de langue produit donc ce profil.
- L'appariement sur G ne neutralise pas ce biais : G se mesure par jeton, alors que l'accumulation se fait sur toute la réponse.

**Témoin.** Le croisement des formats d'E1, avec notation par vraisemblance en forçage, plus T-sortie. Si la température seule reproduit le profil à G égal, le profil est un effet d'accumulation.

**En second : la circularité de la sélection** (Kriegeskorte et al. 2009). Témoins :
- tâches et items tenus à part ;
- la procédure de sélection rejouée sur des étiquettes de tâches permutées, ce qui mesure la spécificité qu'elle fabrique à elle seule.

## (c) Instruments : la mesure minimale qui dit s'ils fonctionnent

| Instrument | Détection | Fausses alertes (cas honnêtes appariés) | Vérification mécanique à battre |
|---|---|---|---|
| Suppression de U | Une sonde linéaire du contenu de U retombe au plancher (± 5 points) à la couche ℓ et en aval, malgré l'auto-réparation (McGrath et al. 2023). Le témoin positif est reproduit. | Sous-espaces aléatoires de même norme : les sondes sans rapport restent inchangées. | Effacement LEACE (Belrose et al. 2023) |
| Appariement sur G | Deux témoins aléatoires à G égal donnent la même dégradation moyenne (écart ≤ 0,03). | Test-retest du modèle intact | Appariement sur la seule perplexité |
| Indice S et distribution nulle | Une lésion plantée (direction d'identité de langue, spécifique de la traduction) est détectée au moins 18 fois sur 20. | Le seuil est dépassé au plus 5 % du temps sur 200 sous-espaces aléatoires (taux mesuré, pas supposé). | Prédicteur de fragilité F |
| Batterie de tâches | Dégradation monotone sous quantification croissante | Paraphrases des consignes : effet minimal détectable ≤ 0,05 | Contrôle de contamination |
| Persistance T½ | Une séquence insérée dans la fenêtre laisse une persistance mesurable. | Sans intervention, T½ = 0. | T½ sous T-bruit |
| Auto-rapport, s'il est utilisé | Il détecte la présence de l'intervention. | Exécutions intactes, même consigne | Classifieur externe sur la sortie (perplexité, longueur). À égalité, le rapport n'apporte rien. |
| Correspondance humaine | Similarité entre l'ordre sous U et l'ordre sous anesthésie | Fréquence à laquelle les témoins « ressemblent à l'anesthésie » | Similarité avec les dégradations humaines non anesthésiques |

## (d) Ancrage matériel (illustratif)

- **Modèles** : deux familles à poids ouverts, de 1 à 3 milliards de paramètres. Candidats, à vérifier : Qwen2.5, Llama 3.2, OLMo 2. Les plus petits échoueront sans doute aux conditions de validité en traduction et en raisonnement à plusieurs sauts.
- **Calcul** :
  - environ 300 conditions × environ 10⁶ jetons, soit environ 3 × 10⁸ jetons par modèle ;
  - à environ 5 000 jetons/s sur un GPU de classe A100 ou H100, avec les crochets d'intervention, cela fait environ 17 h par modèle ;
  - avec M2, E3 et les pilotes : 50 à 100 heures-GPU, soit 150 à 400 € en location ;
  - un modèle de 3 milliards de paramètres en bf16 tient sur 24 Go.
- **Données humaines** : réanalyse sur processeur, quelques jours d'analyste.
- **Coût principal, humain** : douze jeux tâche × format, pré-enregistrement et équipe rouge, soit 2 à 4 mois-personne.

## Antériorité

**Lu dans cette session** : aucun article, seulement `texte-servi.md`.

**De mémoire, non relu ici**
- Brown, Lydic & Schiff (2010), *General anesthesia, sleep, and coma*, NEJM.
- Sanders, Tononi, Laureys & Sleigh (2012), *Unresponsiveness ≠ unconsciousness*, Anesthesiology.
- Sarasso et al. (2015), *Consciousness and complexity during unresponsiveness induced by propofol, xenon, and ketamine*, Curr. Biol.
- Davis et al. (2007), *Dissociating speech perception and comprehension at reduced levels of awareness*, PNAS.
- Bekinschtein et al. (2009), *Neural signature of the conscious processing of auditory regularities*, PNAS.
- Chennu et al. (2016), *Brain connectivity dissociates responsiveness from drug exposure during propofol-induced transitions of consciousness*, PLoS Comput. Biol.
- Redinbaugh et al. (2020), *Thalamus modulates consciousness via layer-specific control of cortex*, Neuron.
- Oizumi, Albantakis & Tononi (2014), *From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0*, PLoS Comput. Biol.
- Mashour, Roelfsema, Changeux & Dehaene (2020), *Conscious processing and the global neuronal workspace hypothesis*, Neuron.
- Lamme (2006), *Towards a true neural stance on consciousness*, Trends Cogn. Sci.
- Brown, Lau & LeDoux (2019), *Understanding the higher-order approach to consciousness*, Trends Cogn. Sci.
- Butlin, Long et al. (2023), *Consciousness in Artificial Intelligence: Insights from the Science of Consciousness*, prépublication.
- Kriegeskorte, Simmons, Bellgowan & Baker (2009), *Circular analysis in systems neuroscience: the dangers of double dipping*, Nat. Neurosci.
- Arditi et al. (2024), *Refusal in language models is mediated by a single direction*.
- Belrose et al. (2023), *LEACE: Perfect linear concept erasure in closed form*.
- McGrath et al. (2023), *The Hydra effect: emergent self-repair in language model computations*.

**Non attribuables** : les « travaux de 2026 » ; le jeu d'IRMf du Michigan ; les études local-global sous sédation ; le titre exact de l'article du Cogitate Consortium.

## Ce qui peut être réfuté

Sept énoncés, aucun ne portant sur la conscience d'un modèle :
1. Σ ≥ 0,15 contre tous les témoins, dans les deux formats.
2. Σ est équivalent à 0 contre au moins un témoin.
3. Le profil suit le format.
4. L'ordre de perte sous U s'écarte de la fragilité.
5. T½(U) / T½(témoin) ≥ 3.
6. L'ordre de perte sous anesthésie est propre chez l'humain.
7. La projection naturelle sur U prédit les erreurs au-delà de F.

FIN-DE-CELLULE