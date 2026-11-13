# Antériorité du lemme d'additivité « L » — lecture intégrale du lot 8 (trois pièces) — v2

- Version 1 écrite le 2026-11-13 à 22:08:59 UTC ; reprise pour la version 2 commencée le 2026-11-13 à 22:22:21 UTC ; ce fichier écrit le 2026-11-13 22:28:23 UTC. Toutes ces heures ont été relevées par `date -u`, la dernière dans la commande qui écrit ce fichier.
- Lecteur : modèle A ; contre-lecteur : modèle B ; A ≠ B.
- **Rapport remplacé** : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-L-lot8-v1.md`, sha256 `130283adeceff8ee8a3bae0487e5ac17a69b80c24884e3e5b4aec41c5d64e6ab`, archivé sans modification. Son archive : `fichiers-de-travail-L-lot8-v1.tar`, sha256 `e643d527c4056def09ee227d89dd572a8c0b3cba429b8c6f9d6aa96e24b87c69`.
- **Contre-lecture intégrée** : `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-L-lot8-v1.md`, sha256 `4083822e6cb35bf9051975e64a87dfd5e1ca1ceab8d74c0d81b3994a9beb6a83`. Son archive : `fichiers-de-travail-contre-lecture-L-lot8-v1.tar`, sha256 `ce947fe73acc5208ef673f2114a26fbba6f02bb235a0112ad07ae72190669e48`. Les deux empreintes ont été vérifiées avant lecture et sont égales aux valeurs attendues. Verdict de la contre-lecture : « tient avec corrections ». Aucun constat bloquant ; quatre constats majeurs (A, B, G, H) et quatre mineurs (C, D, E, F).
- Mandat : verdict d'antériorité sur l'énoncé L (décision N-004), constat M4 de la contre-lecture du niveau 3. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur à ma version 1.
- Pièces (sha256 vérifié contre le compagnon `.sha256` du même dossier, égalité constatée pour les trois) :
  - `1906.08938v2.pdf` (16 pages) : `3fbaedd9705420fff23cbadb9c7d3de2240c2714c23440cbf133718534194ea9`
  - `2605.16140v1.pdf` (36 pages) : `1f70a3284a2eca0b62cded4dd43e6f88cc6930e3275349a17bee76850860a72a`
  - `math-0410072v1.pdf` (34 pages) : `cfcca06ea5e2b3852549dd896f381b2141c82fffa787787fc6fb6a5db560cbbf`
  - dossier : `…/scratchpad/pieces-10016a61/docs/sources/pdf/niveau3-v1/lot8/`, extrait de la branche `prep/etat-de-l-art-niveau3-pieces-v1`, tête `10016a61`.
- Convention de citation :
  - un texte anglais entre « » suivi d'un renvoi [Cn] est une citation contrôlée par programme (liste en annexe) ;
  - les autres guillemets entourent des formulations du programme ou les miennes, jamais une citation d'article ;
  - les numéros C1 à C55 sont ceux de la version 1 ; C56 à C98 sont nouveaux ;
  - « (mon calcul) » marque un chiffre que j'ai calculé moi-même ; « (auteurs) » un chiffre imprimé dans l'article ; « (lu sur la figure) » un chiffre lu sur une figure ; « (contre-lecteur) » un chiffre du contre-lecteur que j'ai recalculé.
- Citations contrôlées par programme : **98 citations, 0 échec**. Contrôle fait par `controle_citations_v1.py`, inchangé depuis la version 1 : `pdftotext` avec et sans `-layout`, normalisation des espaces, ligatures, césures, apostrophes et tirets. Les citations sont dans `citations-L-v2.json` (sha256 `bcef36f2a00991609619eb9894675fb354e8ff170e6d3d9716625e8eeff75271`), inclus dans l'archive v2.

## Fichiers lus (liste exacte)

1. `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, en entier.
2. `…/scratchpad/pieces-10016a61/docs/sources/lecture-pdf-niveau3/consignes-v1/consigne-commune-lecture-v1.md`, en entier.
3. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 53 à 77.
4. `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 85.
5. `docs/programme-controle-ia-v2.md`, lignes 85 à 125.
6. `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, lignes 95 à 112.
7. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 137 à 152.
8. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 368 à 407.
9. Les trois PDF, en entier, annexes, preuves et bibliographies comprises, par `pdftotext` page par page en mode brut. Pages vues en image :
   - `1906.08938v2.pdf` : page 11 (figure 4) ;
   - `2605.16140v1.pdf` : pages 7, 8 et 19 ;
   - `math-0410072v1.pdf` : page 9 (figure 1).
10. Pour la version 2 :
    - `docs/sources/lecture-pdf-niveau3/compte-2/contre-lecture-rapport-L-lot8-v1.md`, en entier ;
    - son archive, extraite dans un sous-dossier neuf de mon dossier de travail. J'en ai lu la liste ; je n'ai ouvert aucun de ses fichiers, et j'ai refait par mes propres moyens le seul calcul qu'elle contient.
11. Dans le dossier du lot 8 : `ls` et les trois compagnons `.sha256`. Aucun autre PDF du lot n'a été ouvert.

Aucune ouverture fautive. Aucune recherche récursive dans le dépôt, aucune commande git, aucun appel réseau ni de modèle, aucune dépense. Aucun refus de permission.

## 0. En tête : occupations, même partielles

1. **Dans les trois pièces lues, aucune composante revendiquée de L n'est occupée, même en partie.** C'est un changement par rapport à la version 1 (constat A, corrigé), qui rangeait la composante « dépendance au seul budget » de L1 en « occupée en partie » par `2605.16140`. Ce libellé était trop fort, pour trois raisons :
   - **Côté guetteur, la borne n'est pas linéaire.** Elle porte sur un coût cumulé **quadratique** en les probabilités de sondage, pondéré par l'état du canal : « where the instantaneous cost depends only on the current probing probability βi and channel state » [C56] (p. 14). Ma citation C28 de la version 1 s'arrêtait avant la mention de l'état du canal.
   - **À total linéaire fixé, cette borne dépend de la répartition.** C'est l'objet du lemme VI.2 : « On the other hand, from Cauchy-Schwarz inequality, » [C59] (p. 21). La part d'avant la rupture n'est écartée que par un argument asymptotique : « dropping the pre-change part of ECB » [C58] (p. 21) ; « intuitively the ECB is overwhelmingly dominated by the post-change detection period » [C90] (p. 32).
   - **L'identité linéaire n'est pas une grandeur de détection par le guetteur.** L'identité « we claim that the relative entropy between P and Q is exactly the product of the expected post-change unmodulated LLR, D, and the expected post-change sensing effort » [C31] (p. 18) mesure ce que le sondeur tire de ses propres observations, comparées à une loi « bruit pur » : « but the observations are drawn from the pre-change distribution for all » [C60] (p. 17). Cette comparaison est faite par un observateur fictif : « representing the history of Alice’s causal information joined with oracle knowledge of the changepoint » [C61] (p. 18). C'est l'identité de Wald, côté détecteur, sans adversaire qui répartit un budget.

   Case juste : **voisin (outil)**, et rappel du cœur classique déjà cité au niveau 3 (borne par une divergence additive, ici sous forme quadratique).
2. **Le cœur classique, non revendiqué, est occupé**, et les trois pièces le resserrent :
   - **Échelle.** La loi de la racine carrée de la communication discrète est citée comme classique : « the square root law (SRL), i.e., Alice » [C5] et « bits covertly and reliably to Bob in n channel usages » [C75] (1906.08938, p. 1) ; « reflecting a square-root-law phenomenon analogous to that in covert communication. » [C25] (2605.16140, p. 2). La décroissance de L1 en √n₀ à B fixé en est un **analogue d'échelle**. Ce rapprochement est le mien : les pages portent la loi pour un nombre de bits et pour un gain de délai, pas pour un budget linéaire de décalage face à une statistique somme (constat D, corrigé). Il interdit de présenter cette échelle comme un apport.
   - **Critère d'alarme pendant l'attaque.** Le critère « alarme pendant la fenêtre d'attaque » est publié : « We refer to such an event as timely detection. » [C73] (p. 5) ; « Willie’s detection process makes sense only when timely detection occurs » [C74] (p. 6). Le constat générique « le calendrier compte face à un détecteur séquentiel » l'est aussi : 1906.08938, p. 10, 13, 14, 15 (constat H, corrigé).
   - **Forme de L2.** La forme close d'un détecteur instantané sous une émission répartie existe (1906.08938, théorème 1, p. 6-7). À fenêtre fixe, on en tire en une ligne la **forme** de L2 : décroissance avec la fragmentation et plancher au-dessus du niveau nul. L'article ne l'énonce pas (constat B, corrigé).
3. **Non trouvé dans les trois pièces lues** : l'énoncé adverse lui-même, c'est-à-dire :
   - l'égalité exacte, en loi et trajectorielle, de L1 ;
   - L4 ;
   - L2 au seuil exact, à budget total fixé et à n fini ;
   - la borne invariante de L3, ainsi que le coût du report et le prix de la garantie toujours valide ;
   - la comparaison processus e cumulé contre détecteur de rupture ;
   - la non-compensation ;
   - la validité sous dépendance ;
   - l'application aux sondes.

   « Non trouvé » ne veut pas dire « trou du champ » : plusieurs voisins plus proches sont nommés dans les pièces et non lus (point 4 et section 6).
4. **Identité de la pièce « Huang, Wang et Poor » : non vérifiée, et probablement fausse. Action à mener.**
   - `1906.08938v2` a **quatre** auteurs imprimés : « Ke-Wen Huang, Hui-Ming Wang, Senior Member, IEEE, » [C2] et « Don Towsley, Life Fellow, IEEE, and H. Vincent Poor, Fellow, IEEE » [C3] (p. 1). Titre : « LPD Communication: A Sequential Change-Point Detection Perspective » [C53].
   - La bibliographie de 2605.16140 (p. 35) distingue deux pièces : « K.-W. Huang, H.-M. Wang, D. Towsley, and H. V. Poor, “LPD communication: A sequential change-point detection perspective,” » [C92] (référence [23]) et « K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” IEEE Transactions on Information Theory, vol. 67, no. 11, pp. 7285–7303, Nov. 2021. » [C37] (référence [24], **trois** auteurs exactement).
   - La pièce à trois auteurs, parue en 2021 dans une revue de théorie de l'information, est le candidat le plus probable du rapport C2. Elle n'est pas dans le lot et je ne l'ai pas lue ; je n'ai pas lu le rapport C2 non plus, car il n'est pas dans mes fichiers nommés.
   - **M4 n'est pas clos.** Il faut verser et lire cette pièce, ainsi que Ker (2007), Bash, Goeckel et Towsley (2014, 2016) et Arumugam et Bloch (2016), **avant toute phrase publique sur L** (section 6).

## 1. Suite donnée à la contre-lecture

Chaque constat a été relu sur les pages en cause. Les calculs du constat B ont été refaits par mes propres moyens (`calcul_shewhart_v2.py`).

| constat | gravité | décision | où dans la version 2 | motif |
|---|---|---|---|---|
| A — occupation partielle de L1 par 2605.16140 trop forte | majeur | corrigé | sections 0 (point 1), 2.2, 3 (ligne L1), 4, 5, 6 (lignes 2 et 3) | Côté guetteur, la borne est quadratique et dépend de la répartition à total linéaire fixé (p. 14, 21) ; l'identité linéaire porte sur l'information du sondeur (p. 17-18) : c'est un voisin (outil), pas une occupation partielle. |
| B — calcul de Shewhart mal placé ; L2 × 1906.08938 est un voisin | majeur | corrigé | sections 0 (point 2), 2.1, 3 (lignes L1 et L2), 6 | Le test de Shewhart est un maximum sur la fenêtre (p. 4-5), pas une somme ; ma non-monotonie venait de la longueur de fenêtre ; recalcul fait : à fenêtre fixe, l'alarme décroît avec la fragmentation au-dessus d'un plancher, ce qui est la forme de L2. |
| C — portée du calendrier face aux détecteurs de rupture | mineur | corrigé | sections 2.1 (puce « Calendrier »), 3, 6 | L'effet est conditionnel à l'absence de fausse alarme avant le départ (p. 6) et sature (p. 14) ; le seul énoncé démontré est le corollaire 3 (p. 10), que j'avais mal rangé parmi les conditions nécessaires. |
| D — « exactement l'échelle » de la loi de la racine carrée | mineur | corrigé | sections 0 (point 2), 5, 6 | Les pages portent la loi pour des bits (p. 1) et un gain de délai (p. 2) ; le rapprochement avec B/√n₀ est le mien : « analogue d'échelle ». |
| E — parenthèse sur la notation de D (2605.16140, p. 19) | mineur | réserve maintenue | section 2.2 (puce « Incohérence interne ») | Ma parenthèse « P₁⁰ = P₀⁰ » est exacte (hypothèse « pas de détection passive gratuite », p. 7, [C63], vue en image) et sert à montrer que la quantité écrite est une autre divergence ; l'objection qu'elle n'égalise pas P₁⁰ et P₀¹ vise ce qu'elle ne prétendait pas ; j'ajoute la justification du contre-lecteur par (81)-(83). |
| F — incohérence de la figure 1 de Donoho et Jin ; portée de « la somme » | mineur | corrigé | section 2.3 | Vu en image p. 9 : la légende dit que les frontières diffèrent quand β > ¾, le texte de la p. 10 et la figure disent l'inverse ; sur la somme simple, la pièce n'a qu'une phrase d'intuition (p. 4), le théorème porte sur la combinaison de Fisher (p. 11). |
| G — voisins nommés et non lus manquants | majeur | corrigé | sections 0 (point 4), 6, 8 | Ker (stéganographie par lots, 2605.16140, p. 1 et 34), Bash, Goeckel et Towsley sur le guetteur qui ignore l'instant de départ (1906.08938, p. 1, 2, 15) et les attaques furtives en commande (2605.16140, p. 1, 35) sont nommés dans les pièces et manquaient à ma liste. |
| H — manques de la liste « ne doit pas affirmer » | majeur | corrigé | section 6 | J'ajoute les quatre lignes manquantes : Lo et Bloch ne doivent pas être cités comme précédent de l'invariance ; forme de L2 ; critère et calendrier publiés ; voisins de répartition non lus. Je reformule les lignes 1 à 3. |

Les décisions ne suivent pas le contre-lecteur par principe. Pour E, son objection porte sur une égalité que ma parenthèse n'affirmait pas. Pour A, je retiens aussi un point qu'il signale : mes passages 0.1 et 1.2 de la version 1 se contredisaient (occupation d'un côté, contre-indice de l'autre). La version 2 les met d'accord.

## 2. Fiches par article

### 2.1 `1906.08938v2.pdf` — Huang, Wang, Towsley, Poor, « LPD Communication: A Sequential Change-Point Detection Perspective » [C53]

- **Venue** : aucune n'est imprimée dans le PDF (prépublication, version 2 du 3 février 2020). 2605.16140 la cite comme parue en 2020 dans une revue de communications : « IEEE Transactions on Communications, vol. 68, no. 4, pp. 2474–2490, Apr. 2020. » [C36] (p. 35).
- **Cadre.** Un émetteur (Alice) veut rester discret face à un guetteur (Willie) qui lance un détecteur séquentiel de rupture.
  - « LPD » dans le titre veut dire *faible probabilité de détection*, c'est-à-dire communication discrète.
  - L'émission commence à un instant ν inconnu de Willie et dure L pas, à puissance constante q. Le signal reçu change de **variance** (énergie reçue de loi exponentielle de moyenne 1 contre 1+q), pas de moyenne seule.
  - Trois détecteurs, tous réglés à durée moyenne avant fausse alarme γ : Shewhart, la somme cumulée de Page (sigle anglais CUSUM) et Shiryaev-Roberts.
  - Le test de Shewhart est instantané : « only depends on the instantaneous sample observation and is » [C64] (p. 4) ; « the detection procedure is equivalent to sequentially comparing the received signal power to a pre-designed threshold » [C65] (p. 5). Sur une fenêtre, c'est donc un **maximum**.
  - Définition de la discrétion : « Communication is said to be covert if it ceases before being detected by Willie with high probability. » [C4] (p. 1). Mesure : « as the probability that Willie is not alerted during the transmission, i.e., the probability of a missed detection » [C9] (p. 6), conditionnellement à l'absence d'alarme avant le départ, puisque « for a given data packet to be transmitted, Alice need only consider the events of timely detection and missed detection » [C89] (p. 6). Levier de l'émetteur : « if the time duration of communication is less than the detection delay, then Willie will not be alerted with a high probability. » [C6] (p. 3).
- **Résultats.**
  - Forme close de la probabilité de discrétion sous Shewhart : « With the Shewhart test, the following theorem characterizes » [C66] (théorème 1, p. 6-7). Lu sur le PDF, non contrôlé par programme : Q = (1 − (1/γ)^{1/(1+q)})^L.
  - Récurrences exactes sous somme cumulée (théorèmes 2 et 3, p. 7-9) ; calcul numérique sous Shiryaev-Roberts (p. 8-9 et annexe C).
  - Condition nécessaire tirée du cas L = 1 (théorème 4, p. 10) ; corollaires 1 et 2 sur la faisabilité ; corollaire 3 sur l'instant de départ (voir « Calendrier »).
  - Monotonie séparée : « monotonically decreasing in both q and L. » [C67] (p. 10). Optimum intérieur en durée : « is maximized in the middle of the feasible region of L. » [C68] (p. 13). Optimisation numérique de (q, L) (p. 10-14).
  - Réglages (auteurs) : « set the ARL2FA of Willie’s detector γ = 500 » [C93] (p. 12), et θ = 0,95.
- **Calendrier (le point le plus proche de L3)** — constat C corrigé.
  - Ce que disent les pages : « a larger value of ν results in a smaller covert probability. This is because the detector accumulates more noise samples before Alice starts to transmit to Bob as ν increases. » [C13] (p. 13). La figure 4 (p. 11, vue en image) montre la somme cumulée à ν = 40 et 300, Shiryaev-Roberts à ν = 100 et 300. Ensuite : « the covert probability in the Shewhart test does not depend on ν due to the fact that the Shewhart test statistic only depends on the instantaneous signal received at each moment. » [C14] (p. 13) ; « Fig. 8 suggests that having a sufficiently large value of ν produces a lower bound on the actual performance. » [C16] (p. 14) ; « the performance of LPD communication is significantly influenced by the time difference between when Willie starts its detection procedure and when Alice starts to transmit » [C17] (p. 15).
  - **Portée.** L'effet est conditionnel à l'absence de fausse alarme avant le départ ([C89], p. 6). Il **sature** : « converges to a quasi-stationary distribution » [C71] (p. 14). Il tient à l'état initial de la statistique : « SR test is not sensitive to a statistical change that occurs at the beginning of the detection procedure » [C72] (p. 14).
  - **Seul énoncé démontré** : le corollaire 3, « Corollary 3: Under the SR test, if » [C69] ; « there exists a θ-covert (q, L)-system. » [C70] (p. 10). En version 1, je l'avais rangé à tort parmi les conditions nécessaires : il dit qu'un départ assez précoce rend toute discrétion atteignable sous Shiryaev-Roberts. Le reste est numérique, sur deux valeurs de ν par test.
  - **Lecture.** Face à un détecteur de rupture, commencer tard nuit à l'émetteur discret ; sous Shewhart, le moment du départ ne change rien. Le rapprochement avec L3 est le mien, entre détecteurs et horizons différents : c'est le sens opposé de L3 (a), qui porte sur le processus e cumulé, et c'est cohérent avec L3 (d). L'article ne compare jamais avec un processus e cumulé.
- **Répartition à budget fixé** — constat B corrigé.
  - L'article ne contient **aucune statistique somme** : il ne dit rien de L1. « L'énergie totale q·L » n'est pas une grandeur de l'article ; l'objectif optimisé est L·ln(1+q/σ²), p. 6.
  - **Calcul à fenêtre qui s'allonge** (mon calcul, `calcul_shewhart_v1.py` et `calcul_shewhart_v2.py`, sur la formule de la p. 7 ; q·L = 3, γ = 500). Q vaut 0,7885 (L = 1), 0,9192 (L = 10), 0,7866 (L = 100). La baisse aux grands L vient des fausses alarmes d'une fenêtre plus longue : sans aucune émission, Q vaut déjà 0,8186 pour L = 100. L'écart dû à l'émission seule vaut 0,2095, 0,0610 puis 0,0319, et décroît de façon monotone sur L = 1 à 200. Ces chiffres sont aussi ceux du contre-lecteur, que j'ai recalculés.
  - **Calcul à fenêtre fixe de 100 pas**, émission répartie sur m pas (même source). Lu sur le PDF, non contrôlé par programme : alarme = 1 − (1 − 1/γ)^{100−m}·Q_m(3/m). Elle vaut 0,3532 (m = 1), 0,2324 (m = 10), 0,2134 (m = 100), contre 0,1814 sans émission. Elle décroît en m de façon monotone et garde un plancher au-dessus du niveau sans émission.
  - C'est la **forme** de L2 (maximum, produit sur les pas, effondrement partiel sous fragmentation, plancher), dans un modèle de variance plutôt que de moyenne. C'est mon calcul : l'article ne fixe jamais q·L et n'énonce ni la décroissance ni le plancher.
- **Limites reconnues et ce que l'article ne fait pas.**
  - Pas de budget total, pas de garantie toujours valide, pas de dépendance entre observations, un seul émetteur.
  - Willie est restreint aux trois tests, et le problème minimax reste ouvert : « is still an open problem. » [C11] (p. 12). Les résultats sont « they can be viewed as theoretical upper bounds on the achievable LPD communication performance under sequential detection » [C12] (p. 12).
  - Hypothèses fortes : « To enable the CUSUM or SR test, Willie needs to know the transmit power of Alice » [C7] (p. 5) ; « Alice and Bob can effectively avoid the occurrence of Case 1 if they can sense Willie’s response to the alarms. » [C8] (p. 5). Le jeu entre Alice et Willie est laissé ouvert : « the problem of LPD communication can be modeled as a game played by Alice and Willie » [C10] (p. 6).
- **Voisins nommés et non lus.** L'article rappelle que la loi de la racine carrée peut être battue « when Willie does not exactly know when Alice starts to transmit (if she does) » [C76] (p. 1), dans un modèle où l'émission occupe un bloc fini « the beginning of which is random and unknown to Willie » [C77] (p. 2). Pièces correspondantes : « B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” » [C78] ; « B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” » [C79] ; « K. S. K. Arumugam and M. R. Bloch, “Keyless asynchronous covert communication,” » [C94] (p. 15). Origine de la loi de la racine carrée : « B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communication with low probability of detection on AWGN channels,” » [C95] (p. 15).
- **Incohérences et résultats trop beaux** : rien de suspect de propreté ; l'effet du calendrier ne repose que sur deux valeurs de ν par test, ce qui en limite la portée.
- **Verdict d'ensemble pour L : voisin.**

### 2.2 `2605.16140v1.pdf` — « Yun-Feng Lo and Matthieu R. Bloch » [C19], « Covert Bayesian Quickest Change Detection » [C18]

- **Venue** : aucune n'est imprimée (prépublication du 15 mai 2026). Les auteurs signalent : « Parts of this document have received assistance from generative AI tools to aid in the composition » [C34] (p. 34).
- **Cadre : rôles inversés par rapport à L.**
  - Le sondeur légitime (Alice) cherche à détecter au plus vite une rupture, dans un cadre bayésien à loi a priori géométrique, en sondant activement le canal.
  - Il doit rester discret face à un guetteur (Eve) qui fait un test binaire hors ligne : « Then Eve’s detector is a binary hypothesis test between the null hypothesis » [C26] (p. 7). Eve connaît la politique d'Alice : « we assume that Eve has full knowledge of Alice’s active policy » [C62] (p. 7). Son test n'est donc ni séquentiel, ni toujours valide.
  - Budget de discrétion attendu (sigle anglais ECB) : « We introduce the expected covertness budget (ECB) as an analytically tractable covertness metric that bounds from above the relative entropy between the observation sequences induced by active and passive sensing. » [C20] (p. 1). Sa forme : « where the instantaneous cost depends only on the current probing probability βi and channel state » [C56] (p. 14). Les auteurs le lisent comme une affaire d'intensité et de structure : « the probing sequence should both use low probing intensity and avoid inducing statistically detectable structure » [C57] (p. 14).
  - La dépendance créée par une politique en boucle fermée est traitée par majoration : « a closed-loop probing policy generally induces statistical dependence across the probing sequence » [C27] (p. 9).
- **Résultats** (formules lues sur le PDF, non contrôlées par programme).
  - Erreur totale minimale d'Eve ≥ 1 − √(½ D) par l'inégalité de Pinsker (p. 9).
  - ECB = E[Σ_{i≤τ} (χ²₀·1{i≤Γ} + χ²₁·1{i>Γ})·β_i²] (p. 15 et 21).
  - Lemme VI.1 : d·ADD + D·B ≥ |ln α| − d/ρ (p. 17), où ADD est le délai moyen de détection.
  - Identité D(P‖Q) = D·B(Π) : « we claim that the relative entropy between P and Q is exactly the product of the expected post-change unmodulated LLR, D, and the expected post-change sensing effort » [C31] (p. 18). Elle porte sur les observations du sondeur et une loi de référence « bruit pur » : « but the observations are drawn from the pre-change distribution for all » [C60] (p. 17), « representing the history of Alice’s causal information joined with oracle knowledge of the changepoint » [C61] (p. 18).
  - Lemme VI.2 (Cauchy-Schwarz) : B ≤ √(δ·ADD/χ²₁) (p. 21). Théorème VI.5 et remarque VII.7 : ADD* = |ln α|/d − D√δ/(d^{3/2}√χ²₁)·√|ln α| + O(1) (p. 22 et 32).
  - En mots : « the ECB constraint fundamentally limits the total probing effort that can be expended covertly. » [C29] (p. 16) — la contrainte **plafonne** le total linéaire, elle ne dit pas que la détectabilité en est fonction ; « which measures the total expected probing activity accumulated after the changepoint and before stopping » [C30] (p. 16) ; « explicitly quantifying the maximum square-root-order covert sensing gain possible » [C21] (p. 1).
- **Répartition dans le temps.**
  - Sous un coût quadratique, la répartition compte. L'allocation plate est indiquée, sous réserve : « The equality condition above provides a hint for how to allocate the probing probabilities » [C32] (p. 21) ; « if possible (e.g., with oracle knowledge of the changepoint), Alice should try to » [C91] (p. 21) ; « allocate a flat sequence between » [C33] (p. 22).
  - Ce n'est pas la performance exacte d'un détecteur : c'est une borne, sur laquelle les auteurs fondent leur politique.
  - **Contre-indice** à toute lecture de L1 qui dirait « la détectabilité ne dépend que du budget total, pour tout détecteur ». L'invariance de L1 est propre aux statistiques fonctions de la somme, comme le dit déjà la note v2.
- **Calendrier.** La politique est à probabilité de sondage constante. La littérature voisine propose au contraire « propose the use of a power sequence that strictly decays over time » [C24] (p. 2), pièce [30] : « H. Rao and L. Wang, “An Extensible Covert Communication Scheme Over the AWGN Channel With Feedback,” » [C96] (p. 35), non lue.
- **Voisins nommés et non lus.**
  - « In [23], [24], the authors study a covert communication problem in which an adversary attempts to detect the transmission by running a quickest change detection algorithm. » [C22] (p. 2) : [23] est 1906.08938, [24] la pièce à trois auteurs.
  - « In [25], [26], the authors introduce the problem of quickest change detection in the presence of a covert adversary that attempts to do maximum damage by controlling the changepoint and post-change distribution » [C23] (p. 2) : « “Quickest change detection in the presence of covert adversaries,” » [C97] ; « “Quickest change detection in continuous-time in presence of a covert adversary,” » [C98] (p. 35). Je n'ai pas vérifié leur lien avec 2601.20022, lu au niveau 2.
  - Stéganographie par lots : « from steganography [1]–[3] to covert communications [4]–[6] » [C80] (p. 1) ; « A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [C81] (p. 34).
  - Attaques furtives en commande : « ability to perform stealthy attacks in cyber-physical systems [15], [16] » [C82] (p. 1) ; « Security in stochastic control systems: Fundamental limitations and performance » [C83] (p. 35).
- **Chiffres (auteurs, p. 33-34).** ρ = 1/20, δ = 1/24, D ≈ 0,8318. Par rapport à l'absence de sondage, le délai moyen baisse d'environ 10 à 50 pas, soit de 63 % à 16 % en relatif.
- **Incohérence interne** (pages 7, 8 et 19 vues en image) — constat E, réserve maintenue, avec ajout.
  - Notation : P_θ^x, avec en indice l'état du canal et en exposant l'action.
  - D est défini p. 8 comme D(P₁¹‖P₀¹). L'équation (91), p. 19, écrit D(P₁¹‖P₁⁰). C'est une coquille probable, car les équations (81) à (83) imposent P₀¹ au dénominateur (justification reprise de la contre-lecture).
  - La quantité écrite est une autre divergence : P₁⁰ = P₀⁰ par l'hypothèse « pas de détection passive gratuite », qui « translates to the equality of PMFs » [C63] (p. 7). Elle vaut donc D(P₁¹‖P₀⁰), et non D.
  - L'énoncé n'est pas atteint : la preuve n'utilise que la valeur D.
- **Ce que l'article ne fait pas** : pas de budget linéaire de décalage, pas de statistique somme, pas d'alarme « avant le dommage » (le délai moyen est celui du sondeur), pas de garantie toujours valide au sens de Ville (la probabilité de fausse alarme est bayésienne), pas de plusieurs agents, pas de dépendance dans les observations honnêtes.
- **Verdict d'ensemble pour L : voisin (outil), et contre-indice de formulation pour L1.** C'est la correction du constat A.

### 2.3 `math-0410072v1.pdf` — « By David Donoho and Jiashun Jin » [C55], « HIGHER CRITICISM FOR DETECTING SPARSE HETEROGENEOUS MIXTURES » [C54]

- **Venue** imprimée : Annales de statistique, « 2004, Vol. 32, No. 3, 962–994 » [C38] (p. 1) ; tiré à part électronique.
- **Cadre** : « testing whether n normal means are all zero versus the alternative that a small fraction is nonzero. » [C39] (p. 1). On observe n moyennes normales, dont une fraction ε_n = n^{−β} est non nulle (½ < β < 1), d'amplitude μ_n = √(2r log n). Formules lues sur le PDF, p. 4. Pas de budget total.
- **Ce qu'ils établissent** — constat F corrigé.
  - **La somme simple des scores** n'a qu'une phrase d'intuition, non démontrée : « In this range the number of nonzero means is too small to be noticeable in any sum which is, in expectation, of order n, so it cannot noticeably affect the behavior of the bulk distribution of the p-values. » [C43] (p. 4). En mon calcul, B/√n = n^{½−β}·√(2r log n) → 0 pour β > ½, ce qui est la lecture de cette phrase par L1.
  - **Combinaison de Fisher** : théorème 1.5, où Fisher « is unable to separate » [C86] (p. 11), et « In our setting of extreme heterogeneity, Fisher’s method is unable to function well asymptotically » [C49] (p. 11).
  - **Maximum.** Il équivaut à la plus petite p-valeur : « another equivalent term for this is Bonferroni-based inference. » [C46] (p. 9). Théorème 1.3 (p. 10) : il n'énonce que le succès du maximum au-dessus de sa frontière ρ_Max(β) = (1 − √(1−β))².
  - Cette frontière égale la frontière optimale sur [¾, 1) : « so that Mn is effective in the range of very sparse alternatives » [C47] (p. 10). Elle est moins bonne en deçà : « so that Mn is inefficient if » [C85] ; « can be dramatically outperformed when there may be about » [C48] (p. 10). Valeurs (auteurs) : ρ*(½) = 0 contre ρ_Max(½) ≈ 0,0858. La procédure à taux de fausses découvertes a la même frontière (théorème 1.4, p. 11).
  - **Critique d'ordre supérieur** (« higher criticism » : maximum d'un score z de la fraction de p-valeurs significatives). Elle atteint partout la frontière optimale (théorème 1.2, p. 6) ; « Of course, in the cases where the amplitude/sparsity relation falls below the detection boundary, all methods fail. » [C45] (p. 6). Il en va de même pour les extensions non gaussiennes (p. 19-25), où « the best that either the maximum or the FDR-controlling methods can obtain is » [C52] (p. 25).
  - **Tout est asymptotique** : « While our theoretical work is largely asymptotic, we provide simulations in finite samples » [C40] (p. 2). Il n'y a qu'une expérience, à n = 10⁶ : « Section 4 describes some simulation experiments. » [C88] (p. 14) ; « whether our theory adequately describes practice in small samples » [C51] (p. 19).
- **Porte-t-il déjà L2 ? Non.**
  - L2 est un énoncé à n fini, au seuil exact et à budget total fixé : il dit que le maximum s'effondre avec la fragmentation, jusqu'à un plancher au-dessus de α.
  - Donoho et Jin ne fixent jamais le budget total. Ils travaillent dans le régime **épars**, où c'est la somme qui ne voit rien et le maximum qui garde une puissance : c'est l'autre face de la même dichotomie.
  - **Verdict L2 : voisin**, avec **contre-indice** pour toute phrase qui ferait du maximum la statistique faible, ou de la somme la bonne statistique, en général.
- **Lien avec la discrétion.** « Detection of covert communications. » [C41] (p. 3), où « the specific frequencies being used might change randomly from one epoch to another » [C42] (p. 3) ; et « such as in watermarking and steganography, could reasonably use the model » [C87] (p. 22). Ce sont des analogues conceptuels de la répartition, sans énoncé sur un budget.
- **L4** : « ne touche pas ». Les n unités observées en même temps sont un analogue lointain de la répartition entre agents à un même pas, sans budget ni invariance.
- **Incohérences** (lues sur le PDF) :
  - p. 5, la région est écrite 0 < β < ½, alors que tout l'article travaille sur ½ < β < 1 ;
  - p. 20, « we view this as modeling the covert communications problem of Section 1.5. » [C50], alors que ce problème est posé à la section 1.7 (p. 12-13) ;
  - **ajout de la version 2** : la légende de la figure 1 (p. 9, vue en image) dit « Two detection boundaries are only different when » [C84] suivi de « ¾ < β < 1 », alors que le texte de la p. 10 dit l'inverse ([C47], [C85]) et que la figure elle-même lui donne raison.
- **Verdict d'ensemble pour L : voisin** (L1 et L2 au niveau de la dichotomie classique), avec un contre-indice de formulation pour L2.

## 3. Table composante × article

| composante de L | 1906.08938 (Huang, Wang, Towsley, Poor) | 2605.16140 (Lo, Bloch) | math/0410072 (Donoho, Jin) |
|---|---|---|---|
| L1 — invariance terminale exacte, trajectorielle ; puissance fonction de (B, n₀, F₀, α) seulement | ne touche pas (aucune statistique somme ; discrétion fonction de q et L séparément) | voisin (outil) : borne quadratique de la détectabilité, additive dans le temps, pour toute politique causale, p. 14, 21 [C56, C59] ; identité « information du sondeur = D × effort total », p. 17-18 [C31, C60, C61] ; contre-indice : répartition plate indiquée, p. 21-22 [C91, C33] ; non fait : égalité en loi, statistique somme, budget linéaire | voisin : phrase d'intuition sur la somme, p. 4 [C43] |
| L1 — décroissance en n₀ à B fixé | voisin : loi de la racine carrée citée pour des bits, p. 1 [C5, C75] ; analogue d'échelle (mon rapprochement) | voisin : loi de la racine carrée pour un gain de délai, p. 2 [C25] ; lemme VI.2, p. 21 | ne touche pas |
| L4 — invariance de la répartition entre agents au même pas, y compris toujours valide | ne touche pas (un seul émetteur) | ne touche pas (un seul sondeur) | ne touche pas (n unités simultanées, sans budget) |
| L2 — séparation avec le max, effondrement sous fragmentation, plancher > α à n fini | voisin : forme close du détecteur instantané, produit sur les pas (théorème 1, p. 6-7 [C66]) ; à fenêtre fixe, décroissance et plancher (mon calcul et celui du contre-lecteur, non énoncés par l'article) | ne touche pas | voisin et contre-indice de formulation (régime épars : la somme échoue ; critique d'ordre supérieur optimale), p. 4, 9, 10, 11 |
| L3 — effet du calendrier | voisin : constat générique publié face à un détecteur séquentiel ; sens opposé (départ tardif défavorable à l'émetteur), conditionnel et saturant ; corollaire 3 démontré, p. 6, 10, 11, 13, 14, 15 [C69, C70, C13, C71, C72] | ne touche pas (allocation constante) ; voisin non lu cité, p. 2 [C24] | ne touche pas |
| L3 — borne inférieure invariante fonction de (B, n₀) | ne touche pas | ne touche pas | ne touche pas |
| L3 — coût du report et prix de la garantie toujours valide chiffrés | ne touche pas | ne touche pas | ne touche pas |
| Sécurité « avant le dommage » (détecteur de rupture contre processus e cumulé) | voisin : le critère « alarme pendant l'attaque » est publié, p. 5-6 [C73, C74] ; aucune comparaison avec un processus e cumulé | ne touche pas | ne touche pas |
| Non-compensation comme condition empirique | ne touche pas | ne touche pas | ne touche pas |
| Validité sous dépendance | ne touche pas | ne touche pas (dépendance des actions de sondage, pas des observations honnêtes), p. 9 [C27] | ne touche pas |
| Application aux scores de sondes internes d'un agent | ne touche pas | ne touche pas | ne touche pas |

## 4. Verdict d'ensemble sur L (table fermée)

**Occupé en partie.** La case est inchangée depuis la version 1 et le niveau 3. Elle est occupée **par le seul cœur classique**, qui n'est pas revendiqué :
- la borne par une divergence additive (2608.02698 au niveau 3 ; forme quadratique chez Lo et Bloch) ;
- l'analogue d'échelle de la loi de la racine carrée ;
- la dichotomie somme contre maximum (1007.1434 au niveau 3 ; versant épars chez Donoho et Jin) ;
- la forme close d'un détecteur instantané, d'où l'on tire la forme de L2 ;
- le critère d'alarme pendant l'attaque et le constat générique sur le calendrier.

Les composantes de l'énoncé adverse ne sont **pas trouvées dans les trois pièces lues**. La différence avec la version 1 : 2605.16140 n'occupe plus aucune composante de L1, même en partie ; c'est un voisin (outil).

## 5. Ce qui reste revendicable (formulation)

« Restent revendicables :
- l'égalité exacte, en loi et trajectoire par trajectoire, de la statistique terminale somme sous un budget **linéaire** de décalage, réparti de façon éventuellement adaptative entre agents, pas, positions et valeurs (L1, L4, y compris en lecture toujours valide aux frontières de pas) ;
- ses conséquences chiffrées en lecture toujours valide : borne inférieure invariante fonction de (B, n₀), coût du report, prix de la garantie (L3) ;
- l'énoncé de L2 au seuil exact, à budget total fixé et à n fini (effondrement du maximum et plancher strictement au-dessus de α) ;
- la comparaison, pour l'alarme avant le dommage, entre le processus e cumulé et les détecteurs de rupture ;
- la validité sous dépendance ;
- la mesure sur scores de sondes internes.

Se citent comme classiques :
- l'échelle en √n₀, analogue de la loi de la racine carrée de la communication discrète ;
- la borne de la détectabilité par une divergence additive dans le temps, pour toute allocation causale (forme quadratique chez Lo et Bloch, où la répartition compte face au détecteur optimal) ;
- la dichotomie somme, maximum et critique d'ordre supérieur (Donoho et Jin, versant épars) ;
- la forme close d'un détecteur instantané sous émission répartie (Huang et collègues, théorème 1) ;
- le critère d'alarme pendant l'attaque et le fait que le calendrier compte face à un détecteur séquentiel (Huang et collègues). »

Réserve d'ensemble : ce qui reste revendicable ne vaut que pour les pièces lues. Les voisins de la section 8 peuvent le réduire.

## 6. Ce qu'une phrase publique déclarant L ne doit pas affirmer

Je ne rédige pas cette phrase : ce rôle m'est exclu. Elle ne doit pas affirmer :
1. que l'échelle « à B fixé, la puissance décroît comme B/√n₀ » est nouvelle : c'est un analogue d'échelle de la loi de la racine carrée ([C5], [C75], [C25]) ;
2. que « la détectabilité ne dépend que du budget total » pour tout détecteur : ce n'est pas porté, et c'est contredit au niveau des bornes publiées, qui sont quadratiques et dépendent de la répartition (2605.16140, p. 21-22, [C59], [C91], [C33]) ;
3. que Lo et Bloch établissent qu'une grandeur de détection ne dépend que d'un budget total, quelle que soit la répartition. Leur borne côté guetteur est quadratique et dépend de la répartition ; leur identité linéaire porte sur l'information du sondeur (2605.16140, p. 14, 17, 18, 21). Il ne faut pas les citer comme précédent de l'invariance ;
4. que « reporter le sabotage aide l'attaquant » sans nommer la règle (le processus e cumulé). Face aux détecteurs de rupture, un départ tardif nuit à l'émetteur discret, sous condition d'absence de fausse alarme préalable et avec saturation ([C13], [C16], [C71], [C89]) ;
5. que « le calendrier compte face à un détecteur séquentiel » est un constat nouveau (1906.08938, p. 10, 13, 14, 15), ni que le critère « alarme avant la fin du dommage » l'est ([C73], [C74]) ;
6. que la forme de L2 (détecteur instantané, produit sur les pas, alarme qui baisse quand on fragmente) est sans précédent de forme : la forme close existe pour le test de Shewhart (1906.08938, théorème 1, p. 6-7). Seuls restent non trouvés le seuil exact du maximum sur n, le budget total fixé et le plancher à n fini ;
7. que le maximum est en général la statistique faible, ou la somme en général la bonne : dans le régime épars, c'est l'inverse, et la critique d'ordre supérieur domine ([C43], [C47], [C49]) ;
8. que la répartition d'un budget caché entre plusieurs objets, face à un détecteur qui agrège, n'a pas de voisin. Les pièces suivantes sont nommées et non lues :
   - la stéganographie par lots (Ker, 2007, [C81]) ;
   - le guetteur qui ignore l'instant de départ ([C76], [C78], [C79], [C94]) ;
9. que la littérature de la communication discrète face à un détecteur séquentiel de rupture a été lue en entier : seules 1906.08938 et 2605.16140 l'ont été (section 8) ;
10. que 1906.08938 est la pièce « Huang, Wang et Poor » du rapport C2.

## 7. Ce que je n'ai pas fait

- Je n'ai pas lu le rapport C2. L'identification de sa pièce « Huang, Wang et Poor » repose sur la seule bibliographie de 2605.16140.
- Je n'ai lu ni les autres pièces du lot 8, ni les pièces citées non versées (section 8). Je ne dis rien de leur contenu au-delà de leur titre imprimé.
- Les formules sont recopiées « lu sur le PDF, non contrôlé par programme » ; seules des phrases en mots sont contrôlées.
- Figures vues en image : figure 4 de 1906.08938 (p. 11) et figure 1 de Donoho et Jin (p. 9). Les autres sont lues par leur légende et le texte.
- Aucun calcul de L lui-même. Les deux calculs sur une formule d'article (`calcul_shewhart_v1.py` et `calcul_shewhart_v2.py`) sont dans l'archive.
- Je n'ai ouvert aucun fichier de l'archive de la contre-lecture : j'ai refait son calcul par mes propres moyens.

## 8. Voisins nommés dans les pièces et non lus, par priorité

| priorité | pièce (titre imprimé) | où elle est nommée | composantes de L concernées |
|---|---|---|---|
| 1 | Huang, Wang et Poor, 2021, « K.-W. Huang, H.-M. Wang, and H. V. Poor, “On covert communication against sequential change-point detection,” IEEE Transactions on Information Theory, vol. 67, no. 11, pp. 7285–7303, Nov. 2021. » [C37] | 2605.16140, p. 35 | L1 (budget), L3, sécurité avant le dommage ; M4 |
| 1 | Ker, 2007, « A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. » [C81] | 2605.16140, p. 1 et 34 | L1, L4, L2 (répartition d'une charge cachée entre objets, d'après le seul titre) |
| 1 | Bash, Goeckel et Towsley, « B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” » [C78] ; « B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” » [C79] ; Arumugam et Bloch, « K. S. K. Arumugam and M. R. Bloch, “Keyless asynchronous covert communication,” » [C94] | 1906.08938, p. 1, 2, 15 | L1 (dilution dans un horizon plus long), L3 (calendrier de l'attaquant) |
| 2 | Ramtin et collègues, « “Quickest change detection in the presence of covert adversaries,” » [C97] ; « “Quickest change detection in continuous-time in presence of a covert adversary,” » [C98] | 2605.16140, p. 2, 35 | sécurité avant le dommage (adversaire discret qui maximise le dommage) ; lien avec 2601.20022 non vérifié |
| 2 | Rao et Wang, « H. Rao and L. Wang, “An Extensible Covert Communication Scheme Over the AWGN Channel With Feedback,” » [C96] | 2605.16140, p. 2, 35 | L3 (puissance décroissante dans le temps) |
| 3 | Bash, Goeckel et Towsley, 2013, « B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communication with low probability of detection on AWGN channels,” » [C95] | 1906.08938, p. 1, 15 | échelle en √n (origine de la loi de la racine carrée) |
| 3 | Attaques furtives en commande, « Security in stochastic control systems: Fundamental limitations and performance » [C83] | 2605.16140, p. 1, 35 | attaquant à budget de furtivité borné |

## 9. Refus

Aucun refus de permission, de crochet ni de classifieur.

## Annexe — citations contrôlées (numérotation de `citations-L-v2.json`)

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
| C56 | `2605.16140v1.pdf` | 14 | where the instantaneous cost depends only on the current probing probability βi and channel state |
| C57 | `2605.16140v1.pdf` | 14 | the probing sequence should both use low probing intensity and avoid inducing statistically detectable structure |
| C58 | `2605.16140v1.pdf` | 21 | dropping the pre-change part of ECB |
| C59 | `2605.16140v1.pdf` | 21 | On the other hand, from Cauchy-Schwarz inequality, |
| C60 | `2605.16140v1.pdf` | 17 | but the observations are drawn from the pre-change distribution for all |
| C61 | `2605.16140v1.pdf` | 18 | representing the history of Alice’s causal information joined with oracle knowledge of the changepoint |
| C62 | `2605.16140v1.pdf` | 7 | we assume that Eve has full knowledge of Alice’s active policy |
| C63 | `2605.16140v1.pdf` | 7 | translates to the equality of PMFs |
| C64 | `1906.08938v2.pdf` | 4 | only depends on the instantaneous sample observation and is |
| C65 | `1906.08938v2.pdf` | 5 | the detection procedure is equivalent to sequentially comparing the received signal power to a pre-designed threshold |
| C66 | `1906.08938v2.pdf` | 6 | With the Shewhart test, the following theorem characterizes |
| C67 | `1906.08938v2.pdf` | 10 | monotonically decreasing in both q and L. |
| C68 | `1906.08938v2.pdf` | 13 | is maximized in the middle of the feasible region of L. |
| C69 | `1906.08938v2.pdf` | 10 | Corollary 3: Under the SR test, if |
| C70 | `1906.08938v2.pdf` | 10 | there exists a θ-covert (q, L)-system. |
| C71 | `1906.08938v2.pdf` | 14 | converges to a quasi-stationary distribution |
| C72 | `1906.08938v2.pdf` | 14 | SR test is not sensitive to a statistical change that occurs at the beginning of the detection procedure |
| C73 | `1906.08938v2.pdf` | 5 | We refer to such an event as timely detection. |
| C74 | `1906.08938v2.pdf` | 6 | Willie’s detection process makes sense only when timely detection occurs |
| C75 | `1906.08938v2.pdf` | 1 | bits covertly and reliably to Bob in n channel usages |
| C76 | `1906.08938v2.pdf` | 1 | when Willie does not exactly know when Alice starts to transmit (if she does) |
| C77 | `1906.08938v2.pdf` | 2 | the beginning of which is random and unknown to Willie |
| C78 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “LPD communication when the warden does not know when,” |
| C79 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “Covert communication gains from adversary’s ignorance of transmission time,” |
| C80 | `2605.16140v1.pdf` | 1 | from steganography [1]–[3] to covert communications [4]–[6] |
| C81 | `2605.16140v1.pdf` | 34 | A. Ker, “A capacity result for batch steganography,” IEEE Signal Processing Letters, vol. 14, no. 8, pp. 525–528, 2007. |
| C82 | `2605.16140v1.pdf` | 1 | ability to perform stealthy attacks in cyber-physical systems [15], [16] |
| C83 | `2605.16140v1.pdf` | 35 | Security in stochastic control systems: Fundamental limitations and performance |
| C84 | `math-0410072v1.pdf` | 9 | Two detection boundaries are only different when |
| C85 | `math-0410072v1.pdf` | 10 | so that Mn is inefficient if |
| C86 | `math-0410072v1.pdf` | 11 | is unable to separate |
| C87 | `math-0410072v1.pdf` | 22 | such as in watermarking and steganography, could reasonably use the model |
| C88 | `math-0410072v1.pdf` | 14 | Section 4 describes some simulation experiments. |
| C89 | `1906.08938v2.pdf` | 6 | for a given data packet to be transmitted, Alice need only consider the events of timely detection and missed detection |
| C90 | `2605.16140v1.pdf` | 32 | intuitively the ECB is overwhelmingly dominated by the post-change detection period |
| C91 | `2605.16140v1.pdf` | 21 | if possible (e.g., with oracle knowledge of the changepoint), Alice should try to |
| C92 | `2605.16140v1.pdf` | 35 | K.-W. Huang, H.-M. Wang, D. Towsley, and H. V. Poor, “LPD communication: A sequential change-point detection perspective,” |
| C93 | `1906.08938v2.pdf` | 12 | set the ARL2FA of Willie’s detector γ = 500 |
| C94 | `1906.08938v2.pdf` | 15 | K. S. K. Arumugam and M. R. Bloch, “Keyless asynchronous covert communication,” |
| C95 | `1906.08938v2.pdf` | 15 | B. A. Bash, D. Goeckel, and D. Towsley, “Limits of reliable communication with low probability of detection on AWGN channels,” |
| C96 | `2605.16140v1.pdf` | 35 | H. Rao and L. Wang, “An Extensible Covert Communication Scheme Over the AWGN Channel With Feedback,” |
| C97 | `2605.16140v1.pdf` | 35 | “Quickest change detection in the presence of covert adversaries,” |
| C98 | `2605.16140v1.pdf` | 35 | “Quickest change detection in continuous-time in presence of a covert adversary,” |
