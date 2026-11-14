# Antériorité du lemme d'additivité « L » — la lettre de Ker (2007) — v2

- Version 1 écrite le 2026-11-14 vers 07:00 UTC. Reprise pour la v2 commencée le 2026-11-14 à 07:08:56 UTC. Ce fichier est écrit le 2026-11-14 07:11:10 UTC. Toutes ces heures ont été relevées par `date -u`, la dernière dans la commande qui écrit ce fichier.
- **Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.**
- **Rapport remplacé** : `rapport-L-ker2007-v1.md`, sha256 `81b965d5c9d239feedf570880dd2eb5e5f26d6b5848b4c4a5ff7afcf57e94d6a`, archivé sans modification. Son archive : `fichiers-de-travail-L-ker2007-v1.tar` (`ccab65a20c8c1abd3e65b545325ad5fed549f438847325e265e41adc2088502e`).
- **Contre-lecture intégrée** : `contre-lecture-rapport-L-ker2007-v1.md` (`8805d9cf5be364115c9f68a12e58986c03367d2668e9518b0690dd32fcb5686a`), et son archive `fichiers-de-travail-contre-lecture-L-ker2007-v1.tar` (`a06f14a518deff94092397214d036acd7b549e16ee8d10688f10ad60b94dce41`).
  - Les deux empreintes ont été vérifiées et sont égales aux valeurs attendues ; l'archive a été extraite dans un sous-dossier neuf.
  - Verdict du contre-lecteur : « tient avec corrections ». Quatre constats majeurs (A à D), six mineurs (E à J), aucun bloquant, aucune case changée.
- Autres rapports sur L, non modifiés : `rapport-L-voisins-v2.md` (`649f471e…`), `rapport-L-lot8-v2.md` (`8d9f2654…`).
- Consigne : `cb0623c4…`. Avant d'écrire, un `ls` du seul dossier `compte-2/` a montré qu'il n'existait ni `rapport-L-ker2007-v2.md` ni `fichiers-de-travail-L-ker2007-v2.tar`.
- Pièce : `ker-2007-capacity-result-batch-steganography.pdf`, 4 pages, sha256 `73113e2de45bf7b9dd93350238b07a2c45f00d29f62b2be1457d042ce2dd98e9`, égal au compagnon `.sha256`.
- Citations contrôlées par programme : **51 citations, 0 échec**. Elles sont dans `citations-L-ker2007-v2.json`, présent dans l'archive seulement (sha256 `106df9fe72016a6de76b6e46203115e608a4dce4bf2599bc9d517191e617d786`). J1 à J40 sont les citations de la v1 ; J41 à J51 sont nouvelles.
- Conventions :
  - Tout extrait anglais entre « », titres compris, est une citation contrôlée.
  - Les formules sont « lues sur le PDF, non contrôlées par programme ».
  - Nature des chiffres : « auteurs » (imprimé dans la pièce) ou « calcul » (refait par moi).

## Fichiers lus et étendue

1. La pièce : relue en entier pour la v2, 4 pages en texte, puis 4 pages en image (pages 1 à 4 vues en v1 ; pages 2 et 3 revues pour les formules).
2. La contre-lecture, en entier. Dans son archive, j'ai seulement listé les fichiers ; je n'ai exécuté aucun script.
3. Calcul indépendant : `verifs_ker2007_v2.py`, en formes fermées, lancé par le Python du dépôt sur processeur, sans tirage.

Aucune ouverture fautive. Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucune suppression. Aucun refus.

## 0. En tête

1. **La lettre n'occupe pas le cœur de L1.**
   - Le mot qui désignerait la moyenne n'y figure pas.
   - La seule somme de la lettre est celle des indicatrices de signe : « we have a sum of not-identically distributed random variables so we cannot use the central limit theorem as in [1]. » [J21] (p. 2).
   - La loi de ce compte dépend de la répartition. Exemple calculé (erreur gaussienne réduite, N = 100, total des proportions 2) : espérance du compte 50,80 si la charge est répartie également, 50,68 si elle est concentrée sur deux objets. C'est aussi le chiffre du contre-lecteur.
   - Le cœur de L1 reste occupé en partie, **par Ker 2006 seul**.
2. **Théorème 1 (p. 2) : deux moitiés, sur deux périmètres différents** (constat A).
   - **Partie 1** : « There is a pooling strategy for the Warden such that, no matter what the Steganographer’s embedding strategy, » [J15]. Si M/√N → ∞, le compte des signes (« The Warden will count the number of positive estimates » [J19]) met le stéganographe à risque, **pour toute répartition**, valeurs inégales comprises (« work a little harder than in [1], for rigour and because we allow non-uniform embedding by the Steganographer. » [J20]). C'est une **garantie de détection**, donnée par **un seul** détecteur.
   - **Partie 2** : « There is an embedding strategy for the Steganographer such that, no matter what the Warden’s pooling strategy, » [J16]. Si M/√N → 0, la répartition **égale** (« The Steganographer’s embedding strategy is simply to split the payload equally between all covers. » [J23], p. 3) n'est à risque pour **aucun** test : « This will suffice to bound the Warden’s ability to perform (2), no matter what pooling strategy they use. » [J24] (p. 3) ; « Any such test is called a pooling strategy. » [J42] (p. 1). C'est une **borne supérieure** de toute détection, pour une seule répartition.
   - **Décroissance en n₀ à budget fixé** : c'est la partie 2. Elle est démontrée **pour la répartition égale, contre tout test**.
   - Pour la somme et pour toute répartition, la décroissance s'obtient en ajoutant l'invariance de Ker 2006. Cet assemblage tient en une ligne de calcul ; il n'est imprimé dans aucune des deux pièces.
3. **La lettre donne des inégalités à N fini, avec constantes explicites** (constat B).
   - L'énoncé du théorème est asymptotique, sans constante : « we are only able to determine capacity a) asymptotically and b) without regard to the multiplicative constant of » [J22] (p. 2).
   - La preuve, elle, travaille à N fini (lu sur le PDF, p. 3) : d(α, β) ≤ D_KL(X₀‖X₁) < N·B·p²/2 = B·M²/(2N·C²), **pour tout test** et sous répartition égale. B est explicite : c'est l'opposé du minorant de (log ψ)''. L'exemple de la p. 4 donne B = 15000 (auteurs).
   - La formule (4) (p. 3) donne β < Φ(C₂ − C₃·M/√N) + C₁/√N. C₂ et C₃ sont explicites (ligne qui précède (4), et formule (6)). Seule C₁, le reste de Berry-Esséen, n'est pas donnée : « Then there is some constant » [J45] (p. 2).
   - **Conséquence.** La décroissance de la détection à charge fixée est imprimée à N fini, avec constante, pour tout détecteur, sous répartition égale. L'occupation est **plus ferme** que ne le disait la v1.
4. **Valeurs inégales** (constat C). Elles sont admises : « In [1] we also imposed the constraint that all cover objects used for embedding had to contain the same amount of payload: the “uniform embedding” assumption. We relax this latter condition in this paper. » [J12] (p. 1, note 1). Mais elles ne servent qu'à la partie 1 ; la partie 2 revient à la répartition égale (« The Steganographer’s embedding strategy is simply to split the payload equally between all covers. » [J23] ; « embedding strategy, identically distributed » [J48], p. 3). L'invariance de la somme sous valeurs inégales n'est imprimée ni ici ni chez Ker 2006. **Le résidu de L1 est inchangé** : valeurs inégales, adaptatif, écriture trajectoriel. Il tient en une ligne et relève d'une remarque citée. La v1 se contredisait sur ce point (section 0 contre section 5) ; c'est corrigé.
5. **Formule (4) et L3 (b) : voisin, à lire durement** (constats D et E).
   - Ce n'est **pas** une invariance. C'est une inégalité de pire cas sur une autre statistique (le compte des signes), dont la loi dépend de la répartition. La lettre le dit : « so there is no UMP test; the results in [1] illustrate vividly how the performance of a pooling strategy can be heavily dependent on the embedding strategy. » [J34] (p. 4). L'auteur juge ses inégalités lâches : « we note that it is the extravagant inequalities in Section II-A which are primarily responsible for the gap. » [J47] (p. 4).
   - Le niveau du test n'est borné qu'asymptotiquement : α < α*/2 + C₁/√N (lu sur le PDF, p. 2), puis « which, for sufficiently large » [J46] N. C₁ est inconnue : à N fini, ni le niveau ni la borne ne sont chiffrables.
   - Elle suppose un décalage plafonné par objet (p_i ≤ 1) : A est le minimum de ψ sur [−1, 0]. Valeur calculée dans l'exemple de la p. 4 : 0,99970 × 10⁻⁴, comme l'imprime l'auteur.
   - **Le contenu de L3 (b) à horizon fixe est L1 lui-même**, dont le précédent le plus proche reste Ker 2006. Le passage à la lecture toujours valide n'est que l'inclusion « franchissement terminal ⊂ alarme d'ici n₀ », jointe à L1 : mathématiquement, une ligne.
   - Ce que (4) ajoute : une garantie de détection, fonction du seul total, pour des valeurs inégales, avec le compte des signes.
6. **Séquentiel** (constat H).
   - La lettre ne le traite pas : « In practice a Steganographer probably has an increasing number of covers and wants to know how much they can safely embed at each point. » [J35] ; « This sequential setting is a little different from the batch setting considered here, and further work will be needed to study it. » [J36] (p. 4). Le nombre d'objets est fixé d'avance : « is known to both parties, before any embedding takes place. » [J43] (p. 4).
   - Déduction du contre-lecteur, que j'adopte : la borne de la partie 2 vaut pour tout test du lot ([J42]). Elle s'applique donc aussi à l'événement « alarme d'ici N » d'une règle lue en séquence dans un lot de taille connue. Sous répartition égale, elle majore en M²/N toute détection séquentielle. Cette déduction n'est pas imprimée.
   - La lettre ne dit rien du calendrier, du coût du report ni du prix de la garantie toujours valide.

## 1. Suite donnée à la contre-lecture

J'ai relu les p. 1-4 en texte et les p. 2-3 en image, et refait les chiffres de la p. 4 et l'exemple du compte des signes (`verifs_ker2007_v2.py`).

| constat | gravité | décision | où dans la v2 | motif |
|---|---|---|---|---|
| A — la décroissance en n₀ est portée par la partie 2 (répartition égale, tout test) | majeur | corrigé | sections 0 (point 2), 3, 4, 5, 6 | [J16], [J23], [J24] (p. 2-3) : à M fixé, on est dans le cas M/√N → 0, que seule la répartition égale traite ; la partie 1 ne donne qu'une garantie de détection, pas une décroissance. |
| B — inégalités à N fini, avec constantes explicites | majeur | corrigé | sections 0 (point 3), 2, 3 | La preuve donne d(α, β) < B·M²/(2N·C²) à N fini, avec B explicite (p. 3, lu sur le PDF) ; C₂ et C₃ sont explicites ; seule C₁ ne l'est pas ([J45]). |
| C — valeurs inégales admises pour la partie 1 seulement ; résidu de L1 inchangé | majeur | corrigé | sections 0 (point 4), 2, 5 | [J12] (p. 1) contre [J23], [J48] (p. 3) : la partie 2 revient à la répartition égale ; la contradiction de la v1 entre ses sections 0 et 5 est levée. |
| D — formule (4) : inégalité de pire cas sur une autre statistique ; L3 (b) | majeur | corrigé | sections 0 (point 5), 3, 5, 6 | « voisin » est maintenu ; « le plus proche à ce jour » est retiré pour L3 (b), dont le contenu à horizon fixe est L1 (Ker 2006) ; [J34], [J47] (p. 4) ; exemple du compte des signes recalculé (50,80 contre 50,68). |
| E — niveau asymptotique, C₁ inconnue, décalage plafonné | mineur | corrigé | section 0 (point 5) | Le niveau est α*/2 + C₁/√N puis [J46] (p. 2) ; A est le minimum de ψ sur [−1, 0] (p. 3). La v1 disait « à N fini » sans ces réserves. |
| F — l'adaptativité au sens de L n'est pas nommée | mineur | corrigé | sections 2, 6 | [J10] (p. 1) vise le choix selon le contenu des objets. L'adaptativité de L (valeurs dépendant des scores observés) est hors du modèle : choix fixé d'avance (« We say that a Steganographer’s embedding strategy is a choice of » [J41], p. 1), N connu d'avance ([J43], p. 4). Elle est « non traitée », pas « exclue en toutes lettres ». |
| G — la section 7 de la v1 resserrait trop | mineur | corrigé | sections 5, 7 | Restent aussi non trouvés, hors de la couche séquentielle : L2 au seuil exact, la dépendance, la non-compensation, les sondes. |
| H — la partie 2 borne toute règle lue en séquence dans le lot | mineur | corrigé | sections 0 (point 6), 3, 5, 6 | Déduction juste de [J42] et [J24] (tout test de (2)) ; elle est marquée comme déduction, non imprimée. |
| I — (log ψ)'' ne sert qu'à la partie 2 ; queues lourdes | mineur | corrigé | sections 2, 5 | La partie 1 n'emploie que le support infini et la positivité de ψ sur [−1, 0] (p. 2-3). À queues lourdes, le compte des signes atteint l'ordre √N, alors que la moyenne de Ker 2006 n'admet qu'une charge en N^{1/ν}, plus grande : la somme n'y est pas le détecteur d'ordre optimal. |
| J — profondeur de lecture et recalcul | mineur | corrigé | sections « Fichiers lus », 2 | Recalcul fait (mon calcul) : bornes de la p. 4, 1,1635 × 10⁶ et 0,0081210, soit un rapport de 1,43 × 10⁸ ; A = 0,99970 × 10⁻⁴. L'enchaînement de (4) a été relu ligne à ligne sur l'image, sans le refaire au-delà. |

Aucune réserve n'est maintenue. Après relecture, chaque constat se vérifie sur la page indiquée. Pour H et pour la remarque de D sur L3 (b), j'ai vérifié le raisonnement lui-même : une fonction de X₁, …, X_N reste un test de (2), et l'événement « alarme d'ici n₀ » contient bien le franchissement terminal. Ce sont des déductions élémentaires, et elles sont marquées comme telles.

## 2. Fiche — « A Capacity Result for Batch Steganography » [J1], « Andrew D. Ker, Member, IEEE » [J2]

- **Venue** : « IEEE SIGNAL PROCESSING LETTERS, VOL. 14, NO. 8, AUGUST 2007 » [J3] ; « Manuscript received August 11, 2006; revised September 20, 2006. » [J4] ; « Digital Object Identifier 10.1109/LSP.2006.891319 » [J5]. Référence [1] : « Batch steganography and pooled steganalysis » [J37] (Ker 2006). Référence [2] : « An information-theoretic model for steganography » [J38] (Cachin 2004, non lu).
- **Cadre** (lu sur le PDF, p. 1) :
  - N objets de capacité C ; charge totale M ; répartition « We say that a Steganographer’s embedding strategy is a choice of » [J41] p_1, …, p_N, avec 0 ≤ p_i ≤ 1 et C·Σp_i = M ; « Possibly some are zero, so that the transmitted objects may be a mixture of covers and stego objects. » [J9].
  - Pur décalage : « We further assume that the estimation error distribution does not depend on the true value being estimated. » [J8].
  - Erreurs indépendantes : « are assumed independent. » [J11].
  - « Note that the covers are considered uniform, not only in their capacity but also to prevent the Steganographer embedding adaptively. » [J10] (choix selon le contenu).
- **Hypothèses du théorème 1** : « Theorem 1 (Batch Steganographic Capacity): Suppose the shift hypothesis (1) and that the error density » [J40] ; support infini, « at least twice continuously differentiable » [J49], (log ψ)'' minoré (p. 2).
  - La partie 1 n'utilise que le support infini et la positivité de ψ sur [−1, 0].
  - La partie 2 utilise le minorant de (log ψ)''.
  - Aucune moyenne nulle n'est exigée : « Note that we do not require that the error has zero mean » [J30] (p. 3).
  - Lois admises : « such a bound exists for many common distributions with infinite support including Gaussian, Cauchy, Logistic, and the Student » [J28] (p. 3).
- **Preuves.**
  - Partie 1 : Berry-Esséen, « which not only gives asymptotic behaviour but also bounds the difference from the asymptotic distribution function. » [J44] (p. 2), avec la constante [J45]. Elle donne Σ(q − q_i) < −A·M/C (lu sur le PDF, p. 3), puis la formule (4).
  - Partie 2 : borne d'entropie relative (p. 3, lu sur le PDF).
  - Passage à la limite (p. 4) : « If we pass to the limit we can tighten (4) to » [J50]. Il donne (6) et (7).
- **Chiffres** :
  - imprimés par l'auteur (p. 4) : γ ≤ 1,163 × 10⁶ par (6) et γ ≥ 0,008121 par (7), pour une loi de Student à 2 degrés de liberté, d'échelle 0,01, et (α*, β*) = (0,05 ; 0,5) ;
  - recalculés par moi : 1,16349 × 10⁶ et 0,0081210 (rapport 1,43 × 10⁸) ; A = 0,99970 × 10⁻⁴ ; q̄ = 0,99995 ;
  - « It turns out that these two bounds on detection reliability are a long way apart. » [J32] ; « but not very helpful to the Steganographer in practice because the bounds on » [J33].
- **Ce que la lettre reconnaît de Ker 2006** : « risk of detection increases. But the investigation was limited » [J51] ; « But the investigation was limited to a particular metric for risk, considered a restricted form of batch steganography, and did not prove a general result. » [J13] ; « We will prove that this is correct in a fairly general sense. » [J14] (p. 2).
- **Hypothèse clé d'indépendance** : « A key assumption is that the steganalysis errors for the » [J29] … ; « The setting of batch steganography allows this independence assumption, and it is a key reason why it is possible to develop capacity results » [J31] (p. 3-4).
- **Hypothèse forte de décalage** : « The strongest hypothesis is the shift hypothesis. » [J25] ; « Fundamentally we need that, in the limit as the payload per cover tends to zero, the steganalysis response is linear in the number of embedding changes » [J26] ; « We do not attempt a formal proof at this stage » [J27] (p. 3).
- **Adaptativité** : hors du modèle (choix fixé, N connu d'avance). Elle n'est pas nommée au sens de L (constat F).
- **Réserve de propreté** : aucune. Les bornes sont lâches de huit ordres de grandeur, et l'auteur le dit ([J32], [J47]).

## 3. Table composante × pièce (lettre de Ker 2007)

| composante de L | verdict | appui |
|---|---|---|
| L1, cœur — égalité en loi de la somme, toute répartition | ne touche pas (aucune moyenne ; pas d'invariance pour le compte des signes) ; reste occupé en partie par Ker 2006 seul | p. 2 [J19, J21], p. 4 [J34] |
| L1 — décroissance en n₀ à budget fixé | **occupée** : démontrée pour la répartition égale, contre tout test, à N fini, avec constante explicite (partie 2) ; pour la somme sous toute répartition, assemblage d'une ligne avec Ker 2006, non imprimé | p. 2-3 [J16, J23, J24, J48] |
| L4 — plusieurs pas, frontières de pas, toujours valide | ne touche pas | — |
| L2 — maximum au seuil exact, n fini | ne touche pas ; contre-indice général : la performance dépend de la répartition | p. 4 [J34] |
| L3 (b) — borne inférieure invariante, lecture toujours valide | voisin : formule (4), garantie fonction du seul total, valeurs inégales, autre statistique, inégalité de pire cas, niveau asymptotique | p. 2-3 [J15, J19, J44, J46] |
| L3 — calendrier, coût du report, prix du toujours valide | ne touche pas ; séquentiel réservé ; la partie 2 majore toute règle lue dans un lot de taille connue (déduction) | p. 3 [J24], p. 4 [J35, J36, J43] |
| processus e cumulé contre détecteur de rupture | ne touche pas | — |
| non-compensation | ne touche pas | — |
| validité sous dépendance | ne touche pas ; indépendance posée | p. 1 [J11], p. 3-4 [J29, J31] |
| scores de sondes internes | ne touche pas | — |

## 4. Verdict sur L (table fermée)

**Occupé en partie.** La case ne change pas. Par composante, en cumulant le lot 8, Ker 2006, Bash et collègues et Ker 2007 :
- **cœur de L1** : occupé en partie (Ker 2006) ;
- **décroissance en n₀** : occupée (Ker 2006 sous forme de capacité ; Ker 2007 à N fini, contre tout test, sous répartition égale) ;
- **L4** : voisin ;
- **L3 (b)** : non trouvé en lecture toujours valide (voisins : Ker 2006 par L1 ; formule (4) de Ker 2007) ;
- **L2 au seuil exact, L3 séquentiel, processus e cumulé contre détecteur de rupture, non-compensation, dépendance, sondes** : non trouvés dans les pièces lues.

## 5. Ce qui reste distinctif (L ; Ker 2006, Bash et collègues, Ker 2007 ensemble ; lignes sèches, non tranché)

- L1, cœur — imprimé : Ker 2006, p. 7, 14 (moyenne, pur décalage, deux valeurs, choix aléatoire, énoncé comme immédiat) ; non démontré par Ker 2007 ; résidu : valeurs inégales, adaptatif (non traité), écriture trajectorielle ; une ligne ; remarque citée.
- L1, décroissance en n₀ à budget fixé — imprimée : Ker 2006 (capacité de la moyenne, exposant selon la queue) ; Ker 2007, partie 2 (répartition égale, tout test, N fini, constante) ; transfert à toute répartition pour la somme : une ligne non imprimée ; résidu : aucun.
- Échelle et queues — capacité en √N démontrée à queues lourdes (Ker 2007) ; à queues lourdes la moyenne n'atteint pas cet ordre (Ker 2006, charge en N^{1/ν}) ; la somme n'est pas le détecteur d'ordre optimal ; à dire.
- Garantie de détection fonction du seul total, valeurs inégales — imprimée pour le compte des signes (Ker 2007, formule (4)) ; inégalité de pire cas ; niveau asymptotique ; C₁ inconnue.
- Bash et collègues — voisin : loi de la racine carrée ; détecteur de puissance gouverné par l'énergie (moments, bruit gaussien).
- L4 — contenu propre (plusieurs pas, frontières de pas, toujours valide) non trouvé ; L1 pas par pas ; élémentaire.
- L3 (b) en lecture toujours valide — non trouvé ; contenu : inclusion d'événements jointe à L1 ; une ligne.
- L3, calendrier, coût du report, prix du toujours valide chiffrés — non trouvés ; séquentiel réservé (Ker 2006, p. 5 ; Ker 2007, p. 4) ; la borne de Ker 2007 (partie 2) majore toute règle lue dans un lot de taille connue (déduction).
- Alarme avant le dommage, processus e cumulé contre détecteurs de rupture — comparaison non trouvée ; critère publié (Huang et collègues, lot 8).
- L2, maximum au seuil exact, n fini, plancher — non trouvé ; sens qualitatif chez Ker 2006 ; forme close du test de Shewhart (lot 8).
- Validité sous dépendance — non trouvée ; indépendance posée (Ker 2007) ; pistes (même clé : Ker 2006 ; Markov : Bash et collègues).
- Biais honnête et étalonnage — publié (Ker 2006).
- Non-compensation — non trouvée.
- Application aux scores de sondes internes — non trouvée.
- Lectures préalables à toute phrase — Huang, Wang et Poor 2021 ; Bash et collègues 2014, 2016 ; Arumugam et Bloch 2016 ; Trivedi et Chandramouli 2003 ; Filler, Ker et Fridrich 2009 ; Cachin 2004.
- Repli prévu — N-004, option (c) : L présenté comme corollaire cité, effort porté sur la mesure ; toute bascule effective est un nœud.

## 6. Ce qu'une phrase publique ne doit pas affirmer (ajouts)

Je ne rédige pas cette phrase. Elle ne doit pas affirmer :
1. que la lettre démontre la décroissance de la détection à budget fixé pour toute répartition : elle la démontre pour la répartition égale, contre tout test ;
2. que cette décroissance n'est connue qu'en ordre asymptotique : la borne en M²/N vaut à N fini, avec constante ;
3. que la lettre couvre les valeurs inégales pour l'invariance de la somme ;
4. que la formule (4) est une invariance, ou un test de niveau garanti à N fini ;
5. que la borne invariante de L3 (b) est un résultat substantiel au-delà de L1 : c'est une inclusion d'événements jointe à L1 ;
6. que la lettre exclut en toutes lettres l'adaptativité au sens de L : elle ne la traite pas ;
7. qu'aucune borne de détection fonction du budget total n'atteint les règles séquentielles : la partie 2 majore toute règle lue dans un lot de taille connue ;
8. que la statistique somme est le détecteur d'ordre optimal : à queues lourdes, le compte des signes atteint l'ordre √N et la moyenne non ;
9. que la loi en √n₀ exige une variance finie ;
10. que Ker démontre l'invariance de la moyenne.

## 7. Colonne « déclarable » de L

**Elle reste à « non » (R-2649).** La lettre resserre encore la zone revendicable : la décroissance est démontrée à N fini, et L3 (b) se réduit à une ligne au-delà de L1. Ce qui n'est pas trouvé ne se limite pas à la couche séquentielle et toujours valide (L4 sur plusieurs pas, L3, processus e cumulé contre détecteur de rupture). Restent aussi non trouvés L2 au seuil exact, la validité sous dépendance, la non-compensation et l'application aux sondes (constat G).

La réserve M4 demeure : les pièces de la section 5 (« lectures préalables ») ne sont ni versées ni lues.

Le resserrement de la revendication est une décision du directeur ; je ne la prends pas.

## 8. Ce que je n'ai pas fait

- Aucune autre pièce lue.
- La preuve de la formule (4) a été relue ligne à ligne sur l'image, sans être refaite symboliquement. Le contre-lecteur dit l'avoir refaite.
- Mes calculs sont en formes fermées, sans tirage, donc sans graine.

## 9. Refus

Aucun refus de permission, de crochet ni de classifieur. Aucune ouverture fautive.

## Annexe — citations contrôlées (`citations-L-ker2007-v2.json`, dans l'archive)

| id | n° JSON | pièce | page | citation exacte |
|---|---|---|---|---|
| J1 | 1 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | A Capacity Result for Batch Steganography |
| J2 | 2 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Andrew D. Ker, Member, IEEE |
| J3 | 3 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | IEEE SIGNAL PROCESSING LETTERS, VOL. 14, NO. 8, AUGUST 2007 |
| J4 | 4 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Manuscript received August 11, 2006; revised September 20, 2006. |
| J5 | 5 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Digital Object Identifier 10.1109/LSP.2006.891319 |
| J6 | 6 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | It was conjectured that, given covers of uniform capacity and a quantitative steganalysis method satisfying certain assumptions, |
| J7 | 7 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | capacity is proportional only to the square root of the number of covers. We now prove that, with respect to a natural definition of secure capacity, and in a suitably asymptotic sense, this conjecture is true. |
| J8 | 8 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | We further assume that the estimation error distribution does not depend on the true value being estimated. |
| J9 | 9 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Possibly some are zero, so that the transmitted objects may be a mixture of covers and stego objects. |
| J10 | 10 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Note that the covers are considered uniform, not only in their capacity but also to prevent the Steganographer embedding adaptively. |
| J11 | 11 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | are assumed independent. |
| J12 | 12 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | In [1] we also imposed the constraint that all cover objects used for embedding had to contain the same amount of payload: the “uniform embedding” assumption. We relax this latter condition in this paper. |
| J13 | 13 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | But the investigation was limited to a particular metric for risk, considered a restricted form of batch steganography, and did not prove a general result. |
| J14 | 14 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | We will prove that this is correct in a fairly general sense. |
| J15 | 15 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | There is a pooling strategy for the Warden such that, no matter what the Steganographer’s embedding strategy, |
| J16 | 16 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | There is an embedding strategy for the Steganographer such that, no matter what the Warden’s pooling strategy, |
| J17 | 17 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | a result in sharp contrast to those of coding and noisy channels where information transmitted is always proportional to the number of symbols sent. |
| J18 | 18 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | It is a modification of the simplest pooling strategy investigated in [1] and certainly is not an “optimal” strategy in practice. |
| J19 | 19 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | The Warden will count the number of positive estimates |
| J20 | 20 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | work a little harder than in [1], for rigour and because we allow non-uniform embedding by the Steganographer. |
| J21 | 21 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | we have a sum of not-identically distributed random variables so we cannot use the central limit theorem as in [1]. |
| J22 | 22 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | we are only able to determine capacity a) asymptotically and b) without regard to the multiplicative constant of |
| J23 | 23 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | The Steganographer’s embedding strategy is simply to split the payload equally between all covers. |
| J24 | 24 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | This will suffice to bound the Warden’s ability to perform (2), no matter what pooling strategy they use. |
| J25 | 25 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | The strongest hypothesis is the shift hypothesis. |
| J26 | 26 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | Fundamentally we need that, in the limit as the payload per cover tends to zero, the steganalysis response is linear in the number of embedding changes |
| J27 | 27 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | We do not attempt a formal proof at this stage |
| J28 | 28 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | such a bound exists for many common distributions with infinite support including Gaussian, Cauchy, Logistic, and the Student |
| J29 | 29 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | A key assumption is that the steganalysis errors for the |
| J30 | 30 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | Note that we do not require that the error has zero mean |
| J31 | 31 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | The setting of batch steganography allows this independence assumption, and it is a key reason why it is possible to develop capacity results |
| J32 | 32 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | It turns out that these two bounds on detection reliability are a long way apart. |
| J33 | 33 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | but not very helpful to the Steganographer in practice because the bounds on |
| J34 | 34 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | so there is no UMP test; the results in [1] illustrate vividly how the performance of a pooling strategy can be heavily dependent on the embedding strategy. |
| J35 | 35 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | In practice a Steganographer probably has an increasing number of covers and wants to know how much they can safely embed at each point. |
| J36 | 36 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | This sequential setting is a little different from the batch setting considered here, and further work will be needed to study it. |
| J37 | 37 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | Batch steganography and pooled steganalysis |
| J38 | 38 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | An information-theoretic model for steganography |
| J39 | 39 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | It is easy to check that the capacity theorem remains valid. |
| J40 | 40 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | Theorem 1 (Batch Steganographic Capacity): Suppose the shift hypothesis (1) and that the error density |
| J41 | 41 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | We say that a Steganographer’s embedding strategy is a choice of |
| J42 | 42 | `ker-2007-capacity-result-batch-steganography.pdf` | 1 | Any such test is called a pooling strategy. |
| J43 | 43 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | is known to both parties, before any embedding takes place. |
| J44 | 44 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | which not only gives asymptotic behaviour but also bounds the difference from the asymptotic distribution function. |
| J45 | 45 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | Then there is some constant |
| J46 | 46 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | which, for sufficiently large |
| J47 | 47 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | we note that it is the extravagant inequalities in Section II-A which are primarily responsible for the gap. |
| J48 | 48 | `ker-2007-capacity-result-batch-steganography.pdf` | 3 | embedding strategy, identically distributed |
| J49 | 49 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | at least twice continuously differentiable |
| J50 | 50 | `ker-2007-capacity-result-batch-steganography.pdf` | 4 | If we pass to the limit we can tighten (4) to |
| J51 | 51 | `ker-2007-capacity-result-batch-steganography.pdf` | 2 | risk of detection increases. But the investigation was limited |
