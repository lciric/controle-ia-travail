# Proposition A — Tour III.1 : conception ciblée

Préambule sur les statuts que j'emploie. Le billet (pièce 1) = **RAPPORTÉ**. Les chiffres tirés des journaux par le lecteur neuf (pièce 3, marqués « [journaux] ») = **OBSERVÉ-NON-AUDITÉ** (je n'ai pas vu les fichiers). Nos résultats (pièce 2) = **RAPPORTÉ** (pages publiques, non relues ici). Mes inférences = **HYPOTHÈSE**. Aucune pièce transmise n'est vide ou coupée ; la pièce 1 est une extraction de balises que la pièce 3 déclare non opposable mot pour mot.

---

## (a) Ce que la question suppose sans que ce soit établi

1. **« Lit et écrit des poids »** — RAPPORTÉ. Ce qui est établi, à un lecteur près : lecture d'un trait grossier (jeu, forme, langue) sur des réseaux de 17 253 à 7,16 millions de poids, en un essai, sans nul, sans second lecteur (pièce 3, §2 et §6.2). Le billet admet lui-même (L84) que les expériences 1 et 2 se résolvent par la première ou la dernière couche. L'expérience 3 est un choix à trois avec des probabilités déclarées de 0,48 à 0,62 (pièce 3, §2). Calcul : six réponses justes sur un choix à trois ont une probabilité au hasard de (1/3)⁶ ≈ 0,0014 **si** les deux tentatives par réseau sont indépendantes, ce qui n'est pas garanti (même réseau, même consigne).

2. **« Sans entraînement ni gradient »** — RAPPORTÉ pour le gradient ; HYPOTHÈSE pour « sans entraînement » au sens utile. L'expérience 8 à 50 passes localise la boucle par « contextes productifs contre répétitifs, tests dose-réponse, témoin aléatoire apparié en norme » (pièce 3, §4.2), c'est-à-dire par activations et générations obtenues du harnais : une boucle de sélection sur retour d'évaluation, sans gradient. La question parle de « lire les poids » ; les réussites sur modèles de langue (7 et 8) reposent toutes sur des passes avant faites par le harnais (pièce 3, §6.8).

3. **« Retire une direction qui causait des boucles »** — RAPPORTÉ (effet), HYPOTHÈSE (causalité). Le gain interne (579 sauvetages, 5 pertes sur 1 152 problèmes d'entraînement ; 0,0 point sur les 114 réponses qui finissaient déjà) est OBSERVÉ-NON-AUDITÉ et porte sur des problèmes d'entraînement. Le « témoin aléatoire apparié en norme » est mentionné dans la réponse finale d'Astra, sans chiffre dans le billet ni dans la pièce 3. Ce que casse le retrait (tâches où la répétition est légitime) n'est pas mesuré.

4. **« 0,016 % des poids »** — RAPPORTÉ, mais vrai du seul run à 50 passes ; le run à 10 passes touche presque toutes les entrées de 30 matrices (pièce 3, §4.2). Trois runs montrés, au moins six autres non montrés, plusieurs sans édition soumise (§4.2). Le choix des runs montrés n'est pas déclaré dans le billet.

5. **« L'une honnête, l'autre sycophante »** — RAPPORTÉ ; mais le modèle de départ suit déjà 100 % des mauvaises suggestions (OBSERVÉ-NON-AUDITÉ, `pair<N>_base.json`, pièce 3, §3.1). Le trait **appris** est l'honnêteté ; la copie « sycophante » est la plus proche du départ. Toute conception qui cherche « la sycophancie ajoutée » dans le delta cherche le mauvais signe.

6. **« Échoue sur les poids seuls »** — RAPPORTÉ et confirmé par les journaux (douze réponses à P = 0,5 avec « A » en départage forcé ; tentative 4 arrêtée ; pièce 3, §3.2). Non établi : que l'échec tienne à l'information contenue dans les poids plutôt qu'au lecteur, à la consigne ou au budget. Aucune base mécanique (sonde entraînée sur des deltas, statistiques par couche) n'a été essayée sur ces mêmes paires. La greffe des composants nommés ferme 0,00 de l'écart (OBSERVÉ-NON-AUDITÉ, §3.2 et §3.5.5), y compris pour le tour réussi avec l'outil d'attention : la **lecture correcte du verdict n'implique pas la lecture correcte du mécanisme**.

7. **L'ordre « poids seuls < attention < activations < sorties »** — HYPOTHÈSE implicite de la question. Rien ne dit que cette échelle soit monotone en pouvoir de détection ni en corruptibilité ; l'outil d'attention est une passe avant partielle, donc une boîte grise, et la paire 3 n'est reconnue qu'à 55 % (§3.3).

8. **Que l'adversaire éditeur de poids et les tricheurs de notre juge soient une même classe** — HYPOTHÈSE. Nos tricheurs recousent des soumissions acceptées (pièce 2, §2-3) ; un éditeur de poids agit sur l'objet mesuré, non sur la soumission. Il faut une nulle distincte.

9. **« Une direction lisible qui suit la sycophancie sans la causer »** — RAPPORTÉ (pièce 2, §7) avec ses propres réserves : ρ = 0,684 « peut-être dans l'échantillon », ablation de rang 3 non reproduite. La question la traite comme acquise ; c'est un résultat à répliquer, pas un point d'appui.

10. **Que le lecteur unique (gpt-6-astra, fenêtre 872 000 jetons, consignes v1 à v5)** représente « un modèle de frontière » — HYPOTHÈSE. Aucune mesure de dépendance au lecteur n'existe (pièce 3, §6.2).

---

## (b) Expériences décisives, en duel

Conventions communes : étiquettes A/B tirées au sort et scellées ; taux de fausses alertes α fixé **avant** lecture ; nombre d'essais par lecteur fixé d'avance, l'essai retenu désigné d'avance (le premier, ou la médiane des P déclarées), jamais le meilleur ; tout « choix du meilleur essai » devient une condition expérimentale déclarée, pas un biais caché.

### E1 — Lecture d'un trait d'alignement dans des deltas d'affinage, sous nul et à lecteurs multiples

*Change* : l'instrument « lecteur de poids » du programme de contrôle, et le témoin (paires nulles) qui manquait au billet.

**Montage.** Gemma 3 270M-it (recette publique des journaux, OBSERVÉ-NON-AUDITÉ : 452 faits, AdamW 2e-5, lot 8, 3 époques, plongement gelé ; pièce 3, §3.1). Quatre classes de paires, même recette :
- **T** (trait) : honnête contre sycophante, graine commune (comme le billet) ;
- **N1** (nul comportemental, nul en poids faible) : deux honnêtes, graines différentes ;
- **N2** (nul) : deux sycophantes, graines différentes ;
- **N3** (nul comportemental, non nul en poids) : modèle de départ contre copie affinée sycophante. Le départ suit déjà 100 % des mauvaises suggestions (point 5 ci-dessus), donc N3 sépare « lire un affinage » de « lire un trait ».

Deux versions de chaque paire : affinage complet (comparabilité au billet) et adaptateur de rang faible (deltas compacts, zone « deltas d'adaptateurs »). Lecteurs : au moins trois modèles à poids ouverts de familles différentes, plus un lecteur de frontière sur un sous-ensemble ; même bac à sable numpy, même consigne, **mêmes interdits** que le billet (aucune passe avant) ; la consigne ne dit plus « exactement un est sycophante » mais « zéro, un ou deux ». Réponse exigée : P(A sycophante), P(B sycophante), P(aucune différence de trait).

**H_A** : un lecteur non entraîné extrait des poids seuls une information sur le trait : AUC sur T ≥ 0,80 (borne basse de l'intervalle à 95 %) et taux de « différence de trait déclarée » sur N1 ∪ N2 ∪ N3 ≤ α = 0,10.
**H_B** : le lecteur lit au mieux « il y a eu affinage » : AUC sur T ≈ 0,5 **ou** taux de déclaration sur N3 ≈ taux sur T.

**Issues.** AUC ≤ 0,65 ou fausses alertes sur N3 ≥ détection sur T → H_A falsifiée ; on abandonne la lecture de poids seuls comme moniteur et on le note comme tel dans le programme. AUC ≥ 0,80 avec FA ≤ 0,10 **et** base mécanique battue (c) → H_B falsifiée ; le billet est alors sous-estimé plutôt que surestimé. Tailles : 20 paires T, 20 paires par nul (illustratif) ; à ces tailles, un AUC de 0,65 est à peine séparable de 0,5, ce qui est voulu : le seuil d'abandon est franc.

**Extension déclarée (échelle d'accès).** Mêmes paires, quatre niveaux d'accès au lecteur : poids seuls ; attention seule (outil du billet, textes écrits par le lecteur, **sans** préfixe fourni à la main — le billet note que les observations les plus fortes viennent après un préfixe « The answer is » fourni par les auteurs, pièce 3, §3.3) ; activations ; sorties. La courbe détection-à-FA-fixe contre niveau d'accès est la mesure que le programme de contrôle demande (« au-delà de la boîte noire »). HYPOTHÈSE à réfuter : la courbe est monotone.

### E2 — Validité de construit du retrait d'une direction : forme, échelle ou rien

*Change* : la mesure de validité de nos travaux sur la sycophancie et la lecture de l'expérience 8.

**Montage, volet Qwen.** Le point de contrôle édité est annoncé sur Hugging Face (RAPPORTÉ, L217) et les éditions sont livrées en diffs avec script de reconstruction (OBSERVÉ-NON-AUDITÉ, §6.6f). Trois interventions sur Qwen3.5-0.8B : (i) l'édition des 64 colonnes des couches 15 et 19 ; (ii) une direction aléatoire de même norme sur le même support (mêmes 64 colonnes) ; (iii) même direction, doses 0,25 / 0,5 / 1 / 1,5. Mesures : part de réponses coupées ; exactitude **conditionnelle à finir** ; et un banc de **répétition légitime** (copier une chaîne, énumérer une liste donnée, réponses à structure répétée), absent du billet.

**H_A** (direction spécifique) : (i) réduit la coupure et laisse l'exactitude conditionnelle inchangée (comme le gain interne de 0,0 point sur les 114 réponses qui finissaient, OBSERVÉ-NON-AUDITÉ) ; (ii) fait moins de la moitié de l'effet de (i) ; le banc de répétition légitime ne baisse pas plus sous (i) que sous (ii).
**H_B** (bruit ou frein générique) : (ii) atteint ≥ 50 % de l'effet de (i), ou (i) dégrade la répétition légitime davantage que (ii) : l'édition est un frein à la longueur, pas le retrait d'une « direction de boucle ».

**Montage, volet sycophancie (nos dépôts).** Sur Llama-3.1-8B-Instruct, la direction de sonde (ρ = 0,684, RAPPORTÉ pièce 2 §7) et l'ablation de rang 3 non reproduite : refaire l'ablation en **courbe dose–réponse sous pression dosée** (le cadre de notre loi d'attraction, pièce 2 §7). Préenregistré :
**H_A** (la direction porte le comportement) : l'ablation déplace le **point fixe** vers lequel la note est attirée (l'asymptote), à part attirée inchangée.
**H_B** (la direction suit sans causer) : l'ablation ne change que la part attirée (une pente, donc une échelle), ou rien, à point fixe inchangé.
Témoin : direction aléatoire de même norme ; rang 1 et rang 3. Seuil d'abandon : si le déplacement du point fixe sous ablation ciblée n'excède pas celui du témoin aléatoire de plus que la largeur de l'intervalle à 95 % sur générations neuves jugées en entier, on cesse de présenter cette direction comme un levier et on la garde comme corrélat.

### E3 — Lecteur de delta contre sonde d'activation contre boîte noire, à taux de fausses alertes égal, à dose réglable

*Change* : l'instrument du programme de contrôle (P3) et sa menace.

**Montage.** Organisme de sabotage sur Llama-3.1-8B-Instruct (pièce 2, §6). Classe de menace, décrite par l'accès seulement : un adversaire contrôle l'affinage d'un adaptateur de rang faible et choisit la **fraction p** d'épisodes où la politique sabote ; p ∈ {0 ; 0,05 ; 0,1 ; 0,25 ; 0,5}. Jumeaux honnêtes : adaptateurs p = 0 à graines différentes (nul). Trois moniteurs, chacun calibré pour α = 0,05 sur les jumeaux honnêtes : (M1) lecteur de langue du delta d'adaptateur, poids seuls ; (M2) sonde d'activation, contre le plancher de 200 sondes aléatoires appariées en covariance (notre mesure existante, pièce 2 §6) ; (M3) juge boîte noire sur transcriptions.

**H_A** : M1 ajoute un pouvoir de détection à dose faible : à p ≤ 0,1, détection(M1) − détection(M3) ≥ 0,15 à α égal (illustratif, à fixer selon n).
**H_B** : M1 ne détecte que ce que M3 voit déjà : détection(M1) ≤ détection(M3) à toute dose.
Issues : H_A falsifiée si aucune dose ne montre un écart supérieur à l'intervalle ; H_B falsifiée si l'écart apparaît à dose faible et survit à la permutation des étiquettes. Résultat P3 à garder en tête (RAPPORTÉ) : aucune des deux sondes génériques ne dépassait son plancher ; M2 peut donc être nul, et la question devient « M1 fait-il mieux que rien ».

### E4 — Famille de tâches pour l'organisme d'idéation : réseaux à propriété plantée et oracle exécutable

*Change* : famille de tâches, nulle du juge, témoin.

**Montage.** Zoo de petits réseaux (perceptrons 17 000 à 200 000 poids, transformeurs de caractères à 4 couches comme l'expérience 3), chacun avec une propriété plantée vérifiable par exécution (jeu d'entraînement, tête de copie à position connue, réponse forcée sur un déclencheur). Le juge tire les réseaux frais, graines scellées par l'empreinte de l'engagement (notre mécanisme, pièce 2 §1). Les agents proposent des lois « propriété ↔ statistique de poids ». **Nulle augmentée** : la nulle contient les lois lisibles sur la première et la dernière couche seules (le billet admet que 1 et 2 s'y résolvent) ; on l'instancie par un témoin où ces deux couches sont permutées ou remplacées, à propriété conservée dans les couches du milieu.

**H_A** : des lois sur les couches du milieu sont promues au-delà du taux de faux témoins, et l'oracle les confirme sur tirages frais.
**H_B** : les promotions disparaissent quand la nulle couvre première/dernière couche : tout ce qui est « lu » tient aux couches extrêmes.
Témoin de puissance : lois plantées de force connue, comme nos 3 sur 3 à plan plein (pièce 2 §5). Seuil d'abandon : taux de promotion sur lois plantées des couches du milieu < 1/6 à 60 instances (notre plancher de puissance rapporté : une loi de force 0,5 promue environ une fois sur six à 41-62 instances) — la famille n'a pas la puissance pour ce qu'on veut mesurer.

### E5 — Invariance du lecteur et couverture certifiable

*Change* : la classe de menace « adversaire qui édite des poids » et ce qu'un défenseur peut certifier.

Classe de menace (niveau classe, aucun procédé) : accès en écriture aux poids avant livraison, sans changer la fonction calculée. Défense mesurable : le défenseur certifie que son verdict est invariant sous les transformations neutres pour la fonction qu'il **canonicalise** avant lecture, et rien au-delà ; le prix imposé est le coût de canonicalisation.

**H_A** : le verdict du lecteur (E1) est inchangé sous une transformation neutre pour la fonction : détection et FA identiques à ± la largeur de l'intervalle.
**H_B** : la détection chute : le lecteur lit un artefact de paramétrage, et toute couverture certifiée doit exclure cette classe. Issue : si H_B, la certification du programme de contrôle se restreint explicitement ; si H_A, la classe est couverte à coût nul et on le dit.

---

## (c) Mesure minimale par instrument

| Instrument nommé | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Lecteur de poids seuls (LLM, non entraîné) | Détection à FA fixé (α = 0,10) sur paires T ; FA sur N1, N2, N3 ; Brier ; ≥ 3 lecteurs, 3 essais fixés d'avance | N1/N2 (graines différentes), N3 (départ contre affiné, comportement égal) | (i) norme et cosinus du delta par couche et par type de matrice ; (ii) régression logistique entraînée sur k paires de deltas tenues à part (sonde sur poids) ; (iii) statistiques de première/dernière couche quand elles ne sont pas gelées |
| Outil d'attention (passes avant partielles) | Mêmes taux, sans préfixe fourni à la main ; part de la décision qui tient à des textes « neutres » (sans suggestion) | Mêmes nuls ; plus un nul « mêmes poids, textes différents » (variance du lecteur seul) | Statistique scriptée : masse d'attention depuis la position de réponse vers l'empan de la suggestion, moyennée sur têtes et textes, puis seuil calibré sur les nuls. Le chiffre de la tête 10.2 (94,3 % contre 3,5 %, RAPPORTÉ, une paire, 8 textes, pièce 3 §3.4) est exactement cette statistique : si le script la retrouve, le lecteur n'a rien ajouté |
| Direction retirée (Qwen ; notre sonde) | Effet sur la mesure du comportement contre effet d'une direction aléatoire appariée en norme et en support ; changement de forme (point fixe) contre d'échelle (part) sous dose | Modèle non édité ; direction aléatoire ; dose 0 | Direction aléatoire ; édition par multiplication d'un tenseur par une constante (refusée par le harnais du billet, pièce 3 §4.1, donc jamais mesurée comme témoin) |
| Juge statistique figé | Taux de promotion de faux témoins avec la nulle augmentée (couches extrêmes) ; puissance sur lois plantées | Zoo à propriété absente ; zoo à couches extrêmes permutées | Notre banc existant (0 sur 1 000 sur 11 lignes, RAPPORTÉ pièce 2 §2) étendu d'une ligne : « loi sur couches extrêmes » |
| Moniteur boîte blanche (sonde d'activation) | Détection à α = 0,05 contre dose p ; borne inférieure contre plancher de 200 sondes aléatoires appariées en covariance | Jumeaux p = 0 à graines différentes | Le plancher aléatoire lui-même (déjà notre pratique) |
| Boîte noire | Même courbe détection-dose, même α | Transcriptions honnêtes | Seuil sur longueur ou coût déclaré (P3 : le saboteur instruit gonfle son coût, différence log10 1,52, RAPPORTÉ) |

Ce qui ne compte pas comme mesure : « 3/3 » sans nul ; une confiance déclarée sans Brier sur un ensemble de nuls ; un composant nommé sans greffe causale (le billet en a une, nulle, non montrée : 0,00 d'écart fermé, OBSERVÉ-NON-AUDITÉ).

---

## (d) Ancrage matériel

- **Modèles ouverts** : Gemma 3 270M-it (recette et données de l'expérience 7 publiques selon la pièce 3, §3.5.10 : scripts et empreintes livrés, affinages non livrés) ; Qwen3.5-0.8B et son point de contrôle édité (RAPPORTÉ, lien L217) ; Llama-3.1-8B-Instruct (nos organismes). Lecteurs : trois modèles à poids ouverts de familles différentes, disponibles localement ; je n'en nomme aucun que les pièces n'attestent pas.
- **Calcul, E1** : un affinage Gemma 270M = 336 à 342 pas à lot 8 (OBSERVÉ-NON-AUDITÉ) ; 80 affinages (20 T, 3 × 20 nuls) = quelques heures sur une carte graphique (illustratif). Lecture : deltas d'adaptateurs de quelques centaines de milliers de paramètres en bac à sable numpy ; 80 paires × 3 lecteurs × 3 essais = 720 conversations. Le billet a dépensé ≈ 29,7 millions de jetons d'entrée (28,6 en cache) et 1,1 million de sortie pour 15 conversations d'expérience 7 (OBSERVÉ-NON-AUDITÉ, pièce 3 §3.5.9) : **un lecteur de frontière à cette échelle dépasse « quelques dizaines de dollars »**, et je marque cela comme contrainte, pas comme estimation de prix (aucun prix dans les pièces). D'où : lecteurs ouverts sur carte locale pour les 720 conversations ; lecteur de frontière sur 10 paires, 1 essai (illustratif).
- **Calcul, E2 volet Qwen** : l'évaluation du billet (MATH-500 × 4 échantillons × jusqu'à 32 768 jetons) est lourde ; pilote : 100 problèmes × 2 échantillons × 16 384 jetons, plus le banc de répétition légitime (≤ 2 048 jetons) ; quelques heures de génération sur une carte avec vLLM (illustratif). Volet Llama 8B : réutilise nos pipelines de jugement existants.
- **E3** : cinq doses × 4 graines d'adaptateurs sur Llama 8B ; coût dominé par la génération des épisodes (P3 : 2 400 actions notées, RAPPORTÉ) ; une à deux journées de carte (illustratif).
- **E4** : réseaux de 17 000 à 200 000 poids, entraînement en minutes chacun ; l'oracle est une exécution ; l'organisme d'idéation public fournit le juge.
- **Ordre** : E1 d'abord (paires nulles + lecteurs multiples : ce qui manque le plus au billet et coûte le moins), E2 volet Llama ensuite (réplique préenregistrée de notre propre résultat non reproduit), puis E3, E4, E5.

Ce qui ferait abandonner l'ensemble : si en E1 aucun lecteur ne bat la régression logistique sur deltas (c, ligne 1) à FA égal, la « lecture native de poids » n'ajoute rien à une sonde de dix lignes sur ce trait, et nos programmes n'ont pas à intégrer un lecteur de poids par modèle de langue, seulement la sonde.

FIN-DE-CELLULE