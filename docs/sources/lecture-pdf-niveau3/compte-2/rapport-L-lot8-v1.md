# Antériorité du lemme d'additivité « L » — lecture intégrale du lot 8 (trois pièces) — v1

- Début du travail : 2026-11-13 21:58:18 UTC (relevé par `date -u`) ; rapport écrit le 2026-11-13 22:08:59 UTC (relevé par `date -u` dans la commande qui écrit ce fichier).
- Lecteur : sous-agent neuf, modèle A. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- Mandat : verdict d'antériorité sur l'énoncé L (décision N-004), constat M4 de la contre-lecture du niveau 3.
- Pièces (empreinte sha256 vérifiée contre le compagnon `.sha256` du même dossier, égalité constatée pour les trois) :
  - `1906.08938v2.pdf` (16 pages) : `3fbaedd9705420fff23cbadb9c7d3de2240c2714c23440cbf133718534194ea9`
  - `2605.16140v1.pdf` (36 pages) : `1f70a3284a2eca0b62cded4dd43e6f88cc6930e3275349a17bee76850860a72a`
  - `math-0410072v1.pdf` (34 pages) : `cfcca06ea5e2b3852549dd896f381b2141c82fffa787787fc6fb6a5db560cbbf`
  - dossier : `…/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot8/` (extrait de `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`).
- Convention : un texte anglais entre « » suivi d'un renvoi [Cn] est une citation contrôlée par programme (annexe) ; les autres guillemets entourent des formulations du programme ou les miennes, jamais une citation d'article.
- Citations contrôlées par programme : **55 citations, 0 échec** (script `controle_citations_v1.py`, `pdftotext` avec et sans `-layout`, normalisation des espaces, ligatures, césures, apostrophes, tirets ; essai préalable : cas juste réussi, trois cas altérés tous refusés). Fichier `citations-L-v1.json` (empreinte `d424b59fc0ced791f9297b91251eb938d4175d3ce616c82a2ae94df754d110b2`) dans l'archive.

## Fichiers lus (liste exacte)

1. `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (en entier).
2. `…/scratchpad/pieces-10016a61/docs/sources/lecture-pdf-niveau3/consignes-v1/consigne-commune-lecture-v1.md` (en entier).
3. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 53 à 77.
4. `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 85.
5. `docs/programme-controle-ia-v2.md`, lignes 85 à 125.
6. `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 95 à 112.
7. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 137 à 152.
8. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 368 à 407.
9. Les trois PDF ci-dessus, en entier (annexes, preuves et bibliographies comprises), par `pdftotext` (mode brut, page par page) ; vues en image : page 11 de `1906.08938v2.pdf` (figure 4), pages 8 et 19 de `2605.16140v1.pdf`.
10. Dans le dossier du lot 8, `ls` du dossier et les trois compagnons `.sha256` ; aucun autre PDF du lot ouvert.

Aucune ouverture fautive. Aucune recherche récursive dans le dépôt, aucune commande git, aucun appel réseau ni de modèle, aucune dépense. Aucun refus de permission rencontré.

## 0. En tête : occupations, même partielles

1. **Occupation partielle, de nature outil classique — `2605.16140v1` (Lo et Bloch), composante de L1 : *une grandeur de détection ne dépend que du budget cumulé, pour toute répartition, même adaptative*.** L'article établit, pour toute politique causale (donc adaptative), (a) une borne supérieure de la détectabilité par le guetteur qui ne dépend que d'un budget cumulé additif dans le temps, « We introduce the expected covertness budget (ECB) as an analytically tractable covertness metric that bounds from above the relative entropy between the observation sequences induced by active and passive sensing. » [C20] ; « this metric takes the form of an expected accumulated cost up to a stopping time, where the instantaneous cost depends only on the current probing probability » [C28] ; et (b) une identité exacte en espérance, « we claim that the relative entropy between P and Q is exactly the product of the expected post-change unmodulated LLR, D, and the expected post-change sensing effort » [C31] (p. 18), d'où une borne sur le délai qui ne dépend que de l'effort total, « the ECB constraint fundamentally limits the total probing effort that can be expended covertly. » [C29]. **Fait** : dépendance au seul budget cumulé, quelle que soit l'allocation causale, en borne (côté discrétion) et en espérance (côté information). **Non fait** : égalité **en loi, trajectorielle**, de la statistique terminale ; puissance exacte fonction de (B, n₀, F₀, α) ; budget **linéaire** de décalage face à une statistique **somme** (ici le budget de discrétion est **quadratique** en les intensités) ; rôles de L (dans l'article, l'acteur discret est le sondeur légitime, et le guetteur fait un test binaire hors ligne sur toute la suite, « Then Eve’s detector is a binary hypothesis test between the null hypothesis » [C26], p. 7). C'est la même nature d'occupation que celle déjà portée par 2608.02698 au niveau 3 (borne par la divergence totale), avec en plus l'identité de Wald : le verdict d'ensemble ne change pas de case.
2. **Le passage « à B fixé, la puissance décroît avec n₀ » (L1) est, dans sa forme d'échelle, la loi de la racine carrée de la communication discrète.** Les deux premières pièces la citent comme classique : « the square root law (SRL), i.e., Alice » [C5] (1906.08938, p. 1, rappel de Bash, Goeckel et Towsley 2013, non lu ici) et « reflecting a square-root-law phenomenon analogous to that in covert communication. » [C25] (2605.16140, p. 2). La puissance du test z de L1 dépend de B/(σ√n₀) (formule de la note v2, section 3) : le budget indétectable croît comme √n₀, ce qui est exactement l'échelle de cette loi. Ce n'est pas une occupation de l'énoncé exact de L1 (la loi de la racine carrée porte sur le détecteur optimal et la divergence, L1 sur la statistique somme), mais **l'échelle en √n₀ ne peut pas être présentée comme un apport**.
3. **Aucune occupation, même partielle, de L4, L2, L3 (borne invariante, coût du report, prix de la garantie toujours valide), de la comparaison processus e cumulé contre détecteur de rupture, de la non-compensation, de la validité sous dépendance, ni de l'application aux sondes**, dans les trois pièces lues.
4. **Identité de la pièce « Huang, Wang et Poor » non vérifiée — et probablement fausse.** `1906.08938v2` a **quatre** auteurs imprimés : « Ke-Wen Huang, Hui-Ming Wang, Senior Member, IEEE, » [C2] et « Don Towsley, Life Fellow, IEEE, and H. Vincent Poor, Fellow, IEEE » [C3] (p. 1), titre « LPD Communication: A Sequential Change-Point Detection Perspective » [C53] (première ligne seule : [C1]). La bibliographie de 2605.16140 (p. 35) range cette pièce sous « LPD communication: A sequential change-point detection perspective » [C35], « IEEE Transactions on Communications, vol. 68, no. 4, pp. 2474–2490, Apr. 2020. » [C36], et cite à côté une **autre** pièce, à trois auteurs exactement : « K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” IEEE Transactions on Information Theory, vol. 67, no. 11, pp. 7285–7303, Nov. 2021. » [C37]. Si le rapport C2 visait « Huang, Wang et Poor », la pièce à trois auteurs (revue de théorie de l'information, 2021) en est le candidat le plus probable ; **elle n'est pas dans le lot et n'a pas été lue**. Je n'ai pas lu le rapport C2 lui-même (hors de mes fichiers nommés) : je ne peux pas trancher, je signale le doute. Le constat M4 n'est donc **pas clos** pour cette pièce ; il l'est pour 1906.08938 et 2605.16140.

## 1. Fiches par article

### 1.1 `1906.08938v2.pdf` — Huang, Wang, Towsley, Poor, « LPD Communication: A Sequential Change-Point Detection Perspective » [C53]

- **Venue** : aucune imprimée dans le PDF (prépublication, version 2 du 3 février 2020, catégorie théorie de l'information) ; 2605.16140 la cite comme parue dans la revue de communications de l'association des ingénieurs électriciens, 2020 ([C36], p. 35).
- **Cadre** : un émetteur (Alice) veut rester discret face à un guetteur (Willie) qui lance un détecteur séquentiel de rupture ; *faible probabilité de détection* (sigle anglais LPD dans le titre) = communication discrète. L'émission commence à un instant ν inconnu de Willie, dure L pas à puissance constante q ; le signal reçu change de **variance** (loi exponentielle de moyenne 1 contre 1+q pour l'énergie reçue), pas de moyenne seule. Trois détecteurs : Shewhart (instantané), somme cumulée de Page (CUSUM), Shiryaev-Roberts, réglés à durée moyenne avant fausse alarme γ. Discrétion : « Communication is said to be covert if it ceases before being detected by Willie with high probability. » [C4] (p. 1), mesurée par « as the probability that Willie is not alerted during the transmission, i.e., the probability of a missed detection » [C9] (p. 6). Le levier de l'émetteur : « if the time duration of communication is less than the detection delay, then Willie will not be alerted with a high probability. » [C6] (p. 3).
- **Résultats** : forme close de la probabilité de discrétion sous Shewhart (théorème 1, p. 6-7) ; récurrences exactes sous somme cumulée (théorèmes 2-3, p. 7-9) ; calcul numérique sous Shiryaev-Roberts (p. 8-9, annexe C) ; conditions nécessaires de faisabilité (théorème 4, corollaires 1-3, p. 10) ; optimisation numérique de (q, L) sous contrainte de discrétion θ (p. 10-14). Chiffres de réglage (auteurs) : γ = 500, θ = 0,95 (p. 12).
- **Calendrier (le point le plus proche de L3)** : « a larger value of ν results in a smaller covert probability. This is because the detector accumulates more noise samples before Alice starts to transmit to Bob as ν increases. » [C13] (p. 13 ; figure 4, p. 11 : somme cumulée à ν = 40 et 300, Shiryaev-Roberts à ν = 100 et 300, lu sur la figure) ; « the covert probability in the Shewhart test does not depend on ν due to the fact that the Shewhart test statistic only depends on the instantaneous signal received at each moment. » [C14] (p. 13) ; « Fig. 8 suggests that having a sufficiently large value of ν produces a lower bound on the actual performance. » [C16] (p. 14) ; « the performance of LPD communication is significantly influenced by the time difference between when Willie starts its detection procedure and when Alice starts to transmit » [C17] (p. 15). Donc, face à un détecteur de rupture, **commencer tard nuit à l'émetteur discret** (ou ne change rien sous Shewhart) — sens opposé à L3 (a) pour le processus e cumulé, et **cohérent avec L3 (d)** (le détecteur de rupture ne se dilue pas dans le préfixe honnête). L'article ne compare jamais un processus e cumulé à un détecteur de rupture.
- **Répartition dans le temps à budget fixé** : non étudiée. La discrétion dépend de q et de L séparément ; « simply increasing the transmission duration does not always improve the performance of LPD communication. » [C15] (p. 13). Calcul (mien, `calcul_shewhart_v1.py`, sur la formule de la p. 7 lue sur le PDF) : à énergie totale qL = 3 fixée et γ = 500, la probabilité de discrétion sous Shewhart vaut 0,79 (L = 1), 0,92 (L = 10), 0,79 (L = 100) — **non invariante à la répartition**, non monotone (calcul).
- **Ce qu'il ne fait pas / limites reconnues** : pas de budget total, pas de statistique somme, pas de garantie toujours valide, pas de dépendance entre observations, un seul émetteur. Willie restreint aux trois tests ; le problème minimax est ouvert : « is still an open problem. » [C11] (p. 12) ; les résultats sont « they can be viewed as theoretical upper bounds on the achievable LPD communication performance under sequential detection » [C12] (p. 12). Hypothèses fortes : Willie connaît la puissance pour la somme cumulée et Shiryaev-Roberts, « To enable the CUSUM or SR test, Willie needs to know the transmit power of Alice » [C7] (p. 5) ; Alice connaît γ et perçoit les alarmes, « Alice and Bob can effectively avoid the occurrence of Case 1 if they can sense Willie’s response to the alarms. » [C8] (p. 5) ; le jeu entre les deux est laissé ouvert, « the problem of LPD communication can be modeled as a game played by Alice and Willie » [C10] (p. 6).
- **Incohérences, résultats trop beaux** : rien de suspect de propreté ; l'effet du calendrier ne repose que sur deux valeurs de ν par test (figure 4) — réserve de portée.
- **Verdicts par composante** : voir la table, section 2. Verdict d'ensemble pour L : **voisin**.

### 1.2 `2605.16140v1.pdf` — « Yun-Feng Lo and Matthieu R. Bloch » [C19], « Covert Bayesian Quickest Change Detection » [C18]

- **Venue** : aucune imprimée (prépublication du 15 mai 2026). Les auteurs signalent : « Parts of this document have received assistance from generative AI tools to aid in the composition » [C34] (p. 34).
- **Cadre** : **rôles inversés par rapport à L**. Le sondeur légitime (Alice) détecte au plus vite une rupture (cadre bayésien, loi a priori géométrique) en sondant activement un canal, et doit rester discret face à un guetteur (Eve) qui fait un test binaire hors ligne sur toute la suite ([C26], p. 7). Budget de discrétion attendu (sigle anglais ECB) : « We introduce the expected covertness budget (ECB) as an analytically tractable covertness metric that bounds from above the relative entropy between the observation sequences induced by active and passive sensing. » [C20] (p. 1) ; « this metric takes the form of an expected accumulated cost up to a stopping time, where the instantaneous cost depends only on the current probing probability » [C28] (p. 14). La dépendance créée par une politique en boucle fermée est traitée par majoration : « a closed-loop probing policy generally induces statistical dependence across the probing sequence » [C27] (p. 9).
- **Résultats** (formules lues sur le PDF, non contrôlées par programme) : erreur totale minimale d'Eve ≥ 1 − √(½ D) (inégalité de Pinsker, p. 9, (11)-(15)) ; budget ECB = E[Σ_{i≤τ} χ²(Q¹‖Q⁰)·β_i²] (p. 15, (57)) ; lemme VI.1 : d·ADD + D·B ≥ |ln α| − d/ρ (p. 17) ; identité D(P‖Q) = D·B(Π) (p. 18, (79)) ; lemme VI.2 : B ≤ √(δ·ADD/χ²₁) par Cauchy-Schwarz (p. 21) ; théorème VI.5 et remarque VII.7 : ADD* = |ln α|/d − D√δ/(d^{3/2}√χ²₁)·√|ln α| + O(1) (p. 22, 32). Lectures en mots : « the ECB constraint fundamentally limits the total probing effort that can be expended covertly. » [C29] (p. 16) ; « which measures the total expected probing activity accumulated after the changepoint and before stopping » [C30] (p. 16) ; « explicitly quantifying the maximum square-root-order covert sensing gain possible » [C21] (p. 1).
- **Répartition dans le temps** : sous un budget **quadratique**, la répartition compte et l'allocation plate est optimale : « The equality condition above provides a hint for how to allocate the probing probabilities » [C32] (p. 21) ; « allocate a flat sequence between » [C33] (p. 22). C'est un **contre-indice** à toute lecture de L1 qui dirait « la détectabilité ne dépend que du budget total, pour tout détecteur » : face à un détecteur dont la puissance dépend d'une somme de carrés (rapport de vraisemblance, divergence), l'attaquant a intérêt à étaler ; l'invariance de L1 est propre aux statistiques fonctions de la somme (ce que la note v2 dit déjà).
- **Calendrier** : politique à probabilité constante dans le temps ; la littérature voisine propose au contraire « propose the use of a power sequence that strictly decays over time » [C24] (p. 2, pièce [30], non lue) — voisin non lu sur le calendrier.
- **Voisins nommés, non lus** : « In [23], [24], the authors study a covert communication problem in which an adversary attempts to detect the transmission by running a quickest change detection algorithm. » [C22] (p. 2 ; [23] = 1906.08938, [24] = la pièce à trois auteurs) ; « In [25], [26], the authors introduce the problem of quickest change detection in the presence of a covert adversary that attempts to do maximum damage by controlling the changepoint and post-change distribution » [C23] (p. 2 ; Ramtin et collègues, 2024 et 2025).
- **Chiffres** (auteurs, p. 33-34) : ρ = 1/20, δ = 1/24, D ≈ 0,8318 ; réduction du délai moyen d'environ 10 à 50 pas, soit de 63 % à 16 % en relatif, par rapport à l'absence de sondage.
- **Incohérence interne** (lu sur le PDF, pages 8 et 19 vues en image) : D est défini p. 8 comme D(P₁¹‖P₀¹) (indice : état du canal ; exposant : action), mais l'équation (91), p. 19, écrit D(P₁¹‖P₁⁰) ; coquille probable (P₁⁰ = P₀⁰ par l'hypothèse « pas de détection passive gratuite »), sans effet sur l'énoncé.
- **Ce qu'il ne fait pas** : pas de budget linéaire de décalage, pas de statistique somme, pas de détection « avant le dommage » (le délai moyen est celui du sondeur), pas de garantie toujours valide au sens de Ville (probabilité de fausse alarme bayésienne), pas de plusieurs agents, pas de dépendance dans les observations honnêtes.
- **Verdict d'ensemble pour L** : **occupée en partie** (L1, au niveau de l'outil, voir section 0, point 1) ; voisin ou ne touche pas pour le reste.

### 1.3 `math-0410072v1.pdf` — « By David Donoho and Jiashun Jin » [C55], « HIGHER CRITICISM FOR DETECTING SPARSE HETEROGENEOUS MIXTURES » [C54]

- **Venue** : imprimée, Annales de statistique, « 2004, Vol. 32, No. 3, 962–994 » [C38] (p. 1) ; tiré à part électronique.
- **Cadre** : « testing whether n normal means are all zero versus the alternative that a small fraction is nonzero. » [C39] (p. 1) ; n moyennes normales, une fraction ε_n = n^{−β} non nulle (½ < β < 1), d'amplitude μ_n = √(2r log n) (p. 4, formules lues sur le PDF).
- **Ce qu'ils établissent exactement sur somme, maximum et « critique d'ordre supérieur »** (higher criticism, statistique de second niveau qui maximise un score z de la fraction de p-valeurs significatives) :
  - la somme ne voit rien dans ce régime : « In this range the number of nonzero means is too small to be noticeable in any sum which is, in expectation, of order n, so it cannot noticeably affect the behavior of the bulk distribution of the p-values. » [C43] (p. 4) ; la combinaison de Fisher échoue : « In our setting of extreme heterogeneity, Fisher’s method is unable to function well asymptotically » [C49] (p. 11, théorème 1.5) ;
  - le maximum (équivalent à la plus petite p-valeur, « another equivalent term for this is Bonferroni-based inference. » [C46], p. 9) a la frontière ρ_Max(β) = (1 − √(1−β))² (théorème 1.3, p. 10, formule lue sur le PDF), égale à la frontière optimale pour β ≥ ¾ : « so that Mn is effective in the range of very sparse alternatives » [C47] (p. 10) ; strictement moins bonne pour ½ ≤ β < ¾ : « can be dramatically outperformed when there may be about » [C48] (p. 10 ; ρ*(½) = 0 contre ρ_Max(½) ≈ 0,0858, auteurs) ; la procédure à taux de fausses découvertes a la même frontière que le maximum (théorème 1.4, p. 11) ;
  - la critique d'ordre supérieur atteint la frontière optimale partout (théorème 1.2, p. 6), sans connaître (r, β) ; « Of course, in the cases where the amplitude/sparsity relation falls below the detection boundary, all methods fail. » [C45] (p. 6) ; extensions non gaussiennes (p. 19-25), où « the best that either the maximum or the FDR-controlling methods can obtain is » [C52] (p. 25).
  - Tous ces énoncés sont **asymptotiques** (n → ∞, niveau tendant vers 0 assez lentement) : « While our theoretical work is largely asymptotic, we provide simulations in finite samples » [C40] (p. 2) ; « whether our theory adequately describes practice in small samples » [C51] (p. 19).
- **Porte-t-il déjà L2 ?** Non. L2 est un énoncé **à n fini, au seuil exact, à budget total B fixé** : la puissance du maximum décroît quand la fragmentation m croît, vers un plancher strictement au-dessus de α. Donoho et Jin ne fixent jamais le budget total (l'amplitude par composante est calibrée en √(2r log n), pas en B/m) et travaillent dans le régime **épars**, où c'est la somme qui échoue et le maximum qui garde une puissance — l'autre face de la même dichotomie. Calcul (mien) : dans leur calibration, B = n^{1−β}·√(2r log n), et le rapport signal sur bruit de la somme vaut B/√n = n^{½−β}·√(2r log n) → 0 pour β > ½, ce qui est la lecture de L1 de leur phrase [C43] (calcul). Verdict L2 : **voisin** (dichotomie classique, versant épars) et **contre-indice** pour toute phrase qui ferait du maximum la statistique faible en général ou de la somme la bonne statistique en général : dans le régime épars la somme échoue, et la critique d'ordre supérieur domine les deux.
- **Lien avec la discrétion** : exemple d'application « Detection of covert communications. » [C41] (p. 3), où « the specific frequencies being used might change randomly from one epoch to another » [C42] (p. 3) — un émetteur qui répartit son signal, analogue conceptuel de la répartition de L ; aucun énoncé sur un budget.
- **Incohérences** (lu sur le PDF) : p. 5, la région est écrite 0 < β < ½ (lu sur le PDF) alors que tout l'article travaille sur ½ < β < 1 (coquille probable) ; p. 20, « we view this as modeling the covert communications problem of Section 1.5. » [C50] alors que ce problème est posé à la section 1.7 (p. 12-13), la section 1.5 traitant de la combinaison classique des p-valeurs.
- **Verdict d'ensemble pour L** : **voisin** (L2 et L1 au niveau de la dichotomie classique), contre-indice de formulation pour L2.

## 2. Table composante × article

| composante de L | 1906.08938 (Huang, Wang, Towsley, Poor) | 2605.16140 (Lo, Bloch) | math/0410072 (Donoho, Jin) |
|---|---|---|---|
| L1 — invariance terminale exacte, trajectorielle ; puissance fonction de (B, n₀, F₀, α) seulement | ne touche pas (discrétion fonction de q et L séparément ; non invariante à énergie fixée, calcul) ; échelle √n cité comme classique, p. 1 [C5] | **occupée en partie** (outil) : borne de détectabilité par budget cumulé additif et identité « information = D × effort total », pour toute allocation causale, p. 1, 14, 16, 18 [C20, C28, C29, C31] ; non fait : égalité en loi, statistique somme, budget linéaire | voisin : la somme ne voit pas quelques moyennes non nulles, p. 4 [C43] |
| L1 — décroissance en n₀ à B fixé | voisin (loi de la racine carrée citée, p. 1 [C5]) | voisin (loi de la racine carrée, p. 2 [C25] ; lemme VI.2, p. 21) | ne touche pas |
| L4 — invariance de la répartition entre agents au même pas, y compris toujours valide | ne touche pas | ne touche pas | ne touche pas |
| L2 — séparation avec le max, effondrement sous fragmentation, plancher > α à n fixé | ne touche pas | ne touche pas | voisin + contre-indice de formulation (régime épars : max > somme ; critique d'ordre supérieur optimale), p. 4, 10, 11 |
| L3 — effet du calendrier | voisin (sens opposé pour les détecteurs de rupture : commencer tard nuit à l'émetteur), p. 11, 13, 14, 15 [C13, C14, C16, C17] | ne touche pas (allocation constante) ; voisin non lu cité, p. 2 [C24] | ne touche pas |
| L3 — borne inférieure invariante fonction de (B, n₀) | ne touche pas | ne touche pas | ne touche pas |
| L3 — coût du report et prix de la garantie toujours valide chiffrés | ne touche pas | ne touche pas | ne touche pas |
| Sécurité « avant le dommage » (détecteur de rupture contre processus e cumulé) | voisin (critère « aucune alarme pendant l'émission » sous Shewhart, somme cumulée, Shiryaev-Roberts, p. 1, 6 [C4, C9] ; aucune comparaison avec un processus e cumulé) | ne touche pas | ne touche pas |
| Non-compensation comme condition empirique | ne touche pas | ne touche pas | ne touche pas |
| Validité sous dépendance | ne touche pas | ne touche pas (dépendance des sondages, pas des observations honnêtes), p. 9 [C27] | ne touche pas |
| Application aux scores de sondes internes d'un agent | ne touche pas | ne touche pas | ne touche pas |

## 3. Verdict d'ensemble sur L

**Occupé en partie** (case inchangée par rapport au niveau 3). Les trois pièces du lot 8 n'occupent ni l'énoncé adverse exact ni ses composantes chiffrées ; elles resserrent le cœur classique sur deux points (loi de la racine carrée pour l'échelle en √n₀ ; dépendance au seul budget cumulé pour toute allocation causale, en borne et en espérance, dans 2605.16140) et ajoutent deux contre-indices de formulation (calendrier opposé face aux détecteurs de rupture ; maximum supérieur à la somme dans le régime épars). La pièce « Huang, Wang et Poor » à trois auteurs reste **non lue** (section 0, point 4).

## 4. Ce qui reste revendicable (formulation)

« L'égalité exacte, en loi et trajectoire par trajectoire, de la statistique terminale somme sous un budget **linéaire** de décalage réparti de façon éventuellement adaptative entre agents, pas, positions et valeurs (L1, L4, y compris en lecture toujours valide aux frontières de pas) ; ses conséquences chiffrées en lecture toujours valide (borne inférieure invariante fonction de (B, n₀), coût du report, prix de la garantie, L3) ; la séparation au seuil exact et à n fini avec le maximum (L2) ; la comparaison, pour l'alarme avant le dommage, entre processus e cumulé et détecteurs de rupture ; la validité sous dépendance ; et la mesure sur scores de sondes internes. L'échelle en √n₀ est la loi de la racine carrée de la communication discrète, citée comme classique ; la dépendance d'une grandeur de détection au seul budget cumulé, pour toute allocation causale, existe comme outil (identité de Wald, budget de discrétion attendu de Lo et Bloch) ; la dichotomie somme, maximum et critique d'ordre supérieur est classique (Donoho et Jin, versant épars). »

## 5. Ce qu'une phrase publique déclarant L ne doit pas affirmer

(Je ne rédige pas cette phrase ; rôle exclu.)
- que l'échelle « à B fixé, la puissance décroît comme B/√n₀ » est nouvelle (loi de la racine carrée, [C5], [C25]) ;
- que « la détectabilité ne dépend que du budget total » pour tout détecteur : faux face à un détecteur fondé sur la divergence ou le rapport de vraisemblance, où l'allocation plate est optimale pour l'acteur discret ([C32], [C33]) ;
- que « reporter le sabotage aide l'attaquant » sans nommer la règle (processus e cumulé) : face aux détecteurs de rupture, commencer tard nuit à l'émetteur discret ([C13], [C16]) ;
- que le maximum est en général la statistique faible ou la somme en général la bonne : dans le régime épars, c'est l'inverse, et la critique d'ordre supérieur domine ([C43], [C47], [C49]) ;
- que la littérature de la communication discrète face à un détecteur séquentiel de rupture a été lue en entier : seules 1906.08938 et 2605.16140 l'ont été ; Huang, Wang et Poor (2021), Ramtin et collègues (2024, 2025), Bash et collègues (2013 et suivants) et la pièce [30] de Lo et Bloch ne l'ont pas été ;
- que 1906.08938 est la pièce « Huang, Wang et Poor » du rapport C2.

## 6. Ce que je n'ai pas fait

- Je n'ai pas lu le rapport C2 (hors de mes fichiers nommés) : l'identification de sa pièce « Huang, Wang et Poor » repose sur la seule bibliographie de 2605.16140.
- Je n'ai pas lu les autres pièces du lot 8 (2102.00630, 1906.09256, 2310.01153, 2501.03982, etc.) ni les pièces citées non versées ([24], [25], [26], [30] de 2605.16140 ; Bash et collègues).
- Les formules sont recopiées « lu sur le PDF, non contrôlé par programme » ; seules des phrases en mots sont contrôlées. Figures : seule la figure 4 de 1906.08938 (p. 11) a été vue en image (avec les pages 8 et 19 de 2605.16140, pour une notation) ; les autres figures sont lues par leurs légendes et le texte.
- Aucun nouveau calcul de L lui-même ; un seul calcul sur une formule d'article (Shewhart, `calcul_shewhart_v1.py`, sortie dans l'archive).

## 7. Refus

Aucun refus de permission, de crochet ni de classifieur.

## Annexe — citations contrôlées (numérotation de `citations-L-v1.json`)

| n° | pièce | page | citation exacte |
|---|---|---|---|
| C1 | `1906.08938v2.pdf` | 1 | LPD Communication: A Sequential Change-Point |
| C2 | `1906.08938v2.pdf` | 1 | Ke-Wen Huang, Hui-Ming Wang, Senior Member, IEEE, |
| C3 | `1906.08938v2.pdf` | 1 | Don Towsley, Life Fellow, IEEE, and H. Vincent Poor, Fellow, IEEE |
| C4 | `1906.08938v2.pdf` | 1 | Communication is said to be covert if it ceases before being detected by Willie with high probability. |
| C5 | `1906.08938v2.pdf` | 1 | the square root law (SRL), i.e., Alice |
| C6 | `1906.08938v2.pdf` | 3 | if the time duration of communication is less than the detection delay, then Willie will not be alerted with a high probability. |
| C7 | `1906.08938v2.pdf` | 5 | To enable the CUSUM or SR test, Willie needs to know the transmit power of Alice |
| C8 | `1906.08938v2.pdf` | 5 | Alice and Bob can effectively avoid the occurrence of Case 1 if they can sense Willie’s response to the alarms. |
| C9 | `1906.08938v2.pdf` | 6 | as the probability that Willie is not alerted during the transmission, i.e., the probability of a missed detection |
| C10 | `1906.08938v2.pdf` | 6 | the problem of LPD communication can be modeled as a game played by Alice and Willie |
| C11 | `1906.08938v2.pdf` | 12 | is still an open problem. |
| C12 | `1906.08938v2.pdf` | 12 | they can be viewed as theoretical upper bounds on the achievable LPD communication performance under sequential detection |
| C13 | `1906.08938v2.pdf` | 13 | a larger value of ν results in a smaller covert probability. This is because the detector accumulates more noise samples before Alice starts to transmit to Bob as ν increases. |
| C14 | `1906.08938v2.pdf` | 13 | the covert probability in the Shewhart test does not depend on ν due to the fact that the Shewhart test statistic only depends on the instantaneous signal received at each moment. |
| C15 | `1906.08938v2.pdf` | 13 | simply increasing the transmission duration does not always improve the performance of LPD communication. |
| C16 | `1906.08938v2.pdf` | 14 | Fig. 8 suggests that having a sufficiently large value of ν produces a lower bound on the actual performance. |
| C17 | `1906.08938v2.pdf` | 15 | the performance of LPD communication is significantly influenced by the time difference between when Willie starts its detection procedure and when Alice starts to transmit |
| C18 | `2605.16140v1.pdf` | 1 | Covert Bayesian Quickest Change Detection |
| C19 | `2605.16140v1.pdf` | 1 | Yun-Feng Lo and Matthieu R. Bloch |
| C20 | `2605.16140v1.pdf` | 1 | We introduce the expected covertness budget (ECB) as an analytically tractable covertness metric that bounds from above the relative entropy between the observation sequences induced by active and passive sensing. |
| C21 | `2605.16140v1.pdf` | 1 | explicitly quantifying the maximum square-root-order covert sensing gain possible |
| C22 | `2605.16140v1.pdf` | 2 | In [23], [24], the authors study a covert communication problem in which an adversary attempts to detect the transmission by running a quickest change detection algorithm. |
| C23 | `2605.16140v1.pdf` | 2 | In [25], [26], the authors introduce the problem of quickest change detection in the presence of a covert adversary that attempts to do maximum damage by controlling the changepoint and post-change distribution |
| C24 | `2605.16140v1.pdf` | 2 | propose the use of a power sequence that strictly decays over time |
| C25 | `2605.16140v1.pdf` | 2 | reflecting a square-root-law phenomenon analogous to that in covert communication. |
| C26 | `2605.16140v1.pdf` | 7 | Then Eve’s detector is a binary hypothesis test between the null hypothesis |
| C27 | `2605.16140v1.pdf` | 9 | a closed-loop probing policy generally induces statistical dependence across the probing sequence |
| C28 | `2605.16140v1.pdf` | 14 | this metric takes the form of an expected accumulated cost up to a stopping time, where the instantaneous cost depends only on the current probing probability |
| C29 | `2605.16140v1.pdf` | 16 | the ECB constraint fundamentally limits the total probing effort that can be expended covertly. |
| C30 | `2605.16140v1.pdf` | 16 | which measures the total expected probing activity accumulated after the changepoint and before stopping |
| C31 | `2605.16140v1.pdf` | 18 | we claim that the relative entropy between P and Q is exactly the product of the expected post-change unmodulated LLR, D, and the expected post-change sensing effort |
| C32 | `2605.16140v1.pdf` | 21 | The equality condition above provides a hint for how to allocate the probing probabilities |
| C33 | `2605.16140v1.pdf` | 22 | allocate a flat sequence between |
| C34 | `2605.16140v1.pdf` | 34 | Parts of this document have received assistance from generative AI tools to aid in the composition |
| C35 | `2605.16140v1.pdf` | 35 | LPD communication: A sequential change-point detection perspective |
| C36 | `2605.16140v1.pdf` | 35 | IEEE Transactions on Communications, vol. 68, no. 4, pp. 2474–2490, Apr. 2020. |
| C37 | `2605.16140v1.pdf` | 35 | K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” IEEE Transactions on Information Theory, vol. 67, no. 11, pp. 7285–7303, Nov. 2021. |
| C38 | `math-0410072v1.pdf` | 1 | 2004, Vol. 32, No. 3, 962–994 |
| C39 | `math-0410072v1.pdf` | 1 | testing whether n normal means are all zero versus the alternative that a small fraction is nonzero. |
| C40 | `math-0410072v1.pdf` | 2 | While our theoretical work is largely asymptotic, we provide simulations in finite samples |
| C41 | `math-0410072v1.pdf` | 3 | Detection of covert communications. |
| C42 | `math-0410072v1.pdf` | 3 | the specific frequencies being used might change randomly from one epoch to another |
| C43 | `math-0410072v1.pdf` | 4 | In this range the number of nonzero means is too small to be noticeable in any sum which is, in expectation, of order n, so it cannot noticeably affect the behavior of the bulk distribution of the p-values. |
| C44 | `math-0410072v1.pdf` | 4 | so the nonzero means cannot have a visible effect on the upper extremes. |
| C45 | `math-0410072v1.pdf` | 6 | Of course, in the cases where the amplitude/sparsity relation falls below the detection boundary, all methods fail. |
| C46 | `math-0410072v1.pdf` | 9 | another equivalent term for this is Bonferroni-based inference. |
| C47 | `math-0410072v1.pdf` | 10 | so that Mn is effective in the range of very sparse alternatives |
| C48 | `math-0410072v1.pdf` | 10 | can be dramatically outperformed when there may be about |
| C49 | `math-0410072v1.pdf` | 11 | In our setting of extreme heterogeneity, Fisher’s method is unable to function well asymptotically |
| C50 | `math-0410072v1.pdf` | 20 | we view this as modeling the covert communications problem of Section 1.5. |
| C51 | `math-0410072v1.pdf` | 19 | whether our theory adequately describes practice in small samples |
| C52 | `math-0410072v1.pdf` | 25 | the best that either the maximum or the FDR-controlling methods can obtain is |
| C53 | `1906.08938v2.pdf` | 1 | LPD Communication: A Sequential Change-Point Detection Perspective |
| C54 | `math-0410072v1.pdf` | 1 | HIGHER CRITICISM FOR DETECTING SPARSE HETEROGENEOUS MIXTURES |
| C55 | `math-0410072v1.pdf` | 1 | By David Donoho and Jiashun Jin |
