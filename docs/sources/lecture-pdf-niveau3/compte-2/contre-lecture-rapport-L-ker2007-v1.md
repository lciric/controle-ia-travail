# Contre-lecture du rapport “L — la lettre de Ker (2007)” v1

- Début du travail : 2026-11-14 07:02:24 UTC (relevé par `date -u` à l'extraction de l'archive). Ce fichier est écrit le 2026-11-14 07:07:55 UTC (relevé par `date -u` dans la commande qui l'écrit).
- **Rôle : contre-lecteur, modèle B.** L'auteur du rapport est le modèle A ; A ≠ B. Je n'ai écrit ni le programme, ni les décisions, ni aucun rapport antérieur.
- Consigne : `consigne-lecteur-compte-2-v1.md`, sha256 `cb0623c4aff841a815dc628691f407308acbeeeceb274db96d1f2ba3c8c77ff5`, vérifiée.
- Objet : `rapport-L-ker2007-v1.md`, sha256 `81b965d5c9d239feedf570880dd2eb5e5f26d6b5848b4c4a5ff7afcf57e94d6a`, vérifiée ; son archive `fichiers-de-travail-L-ker2007-v1.tar`, sha256 `ccab65a20c8c1abd3e65b545325ad5fed549f438847325e265e41adc2088502e`, vérifiée, extraite dans mon dossier de travail.
- Pièce : « A Capacity Result for Batch Steganography » [C1], fichier `ker-2007-capacity-result-batch-steganography.pdf`, 4 pages, sha256 `73113e2de45bf7b9dd93350238b07a2c45f00d29f62b2be1457d042ce2dd98e9`, égale à celle de son compagnon `.sha256`.
- Vérification avant écriture : un `ls` du seul dossier `compte-2/` a montré qu'il n'existait ni `contre-lecture-rapport-L-ker2007-v1.md` ni `fichiers-de-travail-contre-lecture-L-ker2007-v1.tar`.
- **Citations contrôlées par programme : 30 citations, 0 échec** (`citations-contre-lecture-L-ker2007-v1.json`, dans l'archive, sha256 `2cee4bf98efc7dc434c8ce6cfb23e09bb7e5790539cddb2448bc3ec674936f50`).
  - Script écrit par moi (`controle_citations_contre_lecture_ker2007_v1.py`), essayé d'abord sur un cas juste (réussi) et deux cas altérés (texte changé ; bonne phrase, mauvaise page : refusés tous deux).
  - Premier passage complet : 1 échec (citation 8, lignes de deux colonnes entrelacées dans le texte extrait). Citation remplacée par une phrase voisine de la même page ; second passage : 0 échec. Le journal du premier passage est gardé dans l'archive.
  - Les 40 citations du lecteur, rejouées par mon script : 40 réussies, 0 échec.
- Convention : les guillemets français sont réservés aux extraits anglais de la pièce, tous contrôlés et suivis de [Cn] (numéro dans mon JSON). Les extraits du rapport, les mots cherchés et les étiquettes sont entre guillemets droits ou courbes.
- Les formules sont lues sur l'image des pages et marquées “lu sur le PDF, non contrôlé par programme”. Les chiffres portent leur nature : “auteurs” ou “calcul”.

## Fichiers lus et étendue

1. La consigne commune, en entier.
2. Le rapport contre-lu, en entier ; son archive (journal, script, JSON, journaux de contrôle).
3. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 53 à 77 ; `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 85.
4. `rapport-L-voisins-v2.md` (sha256 `649f471e583b1700efa127fb2ef258f9338be322d343529f7fa859c42ff44466`, vérifiée) : sections 0 (occupations), 4 (verdict), 5, 6 et 7 (“Ce qui reste distinctif”), soit les lignes 33 à 64 et 174 à 224, repérées par la liste des titres.
5. La pièce : 4 pages sur 4 lues ligne à ligne en texte (`pdftotext`, avec et sans `-layout`), puis 4 pages sur 4 lues en image pour les formules et la figure 1. Recherche par mots dans le texte : “average”, “mean”, “sequen”, “threshold”, “maxim”, “adapt”, “sum”, “martingale”, “optimal”, “uniform”, “known”.

Non lu : le fichier `interdits-communs-v2.md`, que la consigne fait lire au lecteur ; mon mandat borne mes lectures aux fichiers qu'il nomme, je m'y suis tenu. Les renvois du rapport à 2605.16140 (p. 34) et à Bash et collègues (p. 27) ne sont pas vérifiables par moi (pièces hors de mon mandat).

Aucune commande git, aucun réseau, aucun appel de modèle, aucune recherche récursive dans le dépôt, aucune suppression, aucune ouverture fautive. Aucun refus.

## 0. Verdict en tête

- **Verdict sur le rapport : tient avec corrections.** La case d'ensemble (“occupé en partie”) et le verdict sur le cœur de L1 sont justes. Quatre constats majeurs (A, B, C, D) portent sur la rédaction de ce que la lettre démontre et sur ce qui reste distinctif ; aucun n'est bloquant, aucun ne change une case.
- **Mon verdict sur L (table fermée) : occupé en partie.**
- Sens des corrections : deux vont vers plus d'occupation (B : borne explicite à N fini, pour tout test ; D : le résidu de L3 (b) tient en une ligne), deux vers moins (A : la décroissance n'est démontrée que pour la répartition égale ; C : les valeurs inégales ne sont pas couvertes pour l'invariance de la somme).

## 1. Ce que la pièce démontre, relu page par page

### 1.1 Théorème 1 (p. 2) — hypothèses exactes

- Décalage pur : « We further assume that the estimation error distribution does not depend on the true value being estimated. » [C2] (p. 1) ; formule (1), lue sur le PDF, non contrôlée par programme : Pr[X < x] = Ψ(x − p).
- Densité d'erreur ψ à support infini, « at least twice continuously differentiable » [C10] (p. 2), avec (log ψ)'' minoré (lu sur le PDF).
- Erreurs indépendantes entre objets : « are assumed independent. » [C6] (p. 1).
- N objets de même capacité C ; charge totale M ; proportions 0 ≤ p_i ≤ 1 avec C·Σp_i = M (lu sur le PDF, p. 1). Le décalage par objet est donc plafonné à 1.
- La répartition est un vecteur fixé : « We say that a Steganographer’s embedding strategy is a choice of » [C3] p_1, …, p_N (p. 1). N est connu d'avance : « is known to both parties, before any embedding takes place. » [C29] (p. 4).
- α* dans ]0, 1[, β* dans ]0, 1 − α*[ (définition 1, lue sur le PDF, p. 2).
- Le rapport rend ces hypothèses correctement (section 0, point 2). Une précision manque : (log ψ)'' minoré ne sert qu'à la partie 2 (borne d'entropie relative, p. 3) ; la partie 1 n'emploie que le support infini et la positivité de ψ sur [−1, 0] (p. 2-3, lu sur le PDF).

### 1.2 Ce qui est démontré, et pour quel détecteur

- **Partie 1** : « There is a pooling strategy for the Warden such that, no matter what the Steganographer’s embedding strategy, » [C11] si M/√N → ∞, le stéganographe est à risque pour N assez grand. Détecteur : le compte des signes, « The Warden will count the number of positive estimates » [C14], qui n'est pas dit optimal : « It is a modification of the simplest pooling strategy investigated in [1] and certainly is not an “optimal” strategy in practice. » [C13]. C'est une **borne inférieure** de la détection, pour **toute répartition**, avec **un** détecteur.
- **Partie 2** : « There is an embedding strategy for the Steganographer such that, no matter what the Warden’s pooling strategy, » [C12] si M/√N → 0, le stéganographe n'est pas à risque. Répartition : « The Steganographer’s embedding strategy is simply to split the payload equally between all covers. » [C20] (p. 3) ; l'égalité de l'entropie relative du lot à N fois celle d'un objet repose sur « embedding strategy, identically distributed » [C22] (p. 3). Détecteur : tout test, « This will suffice to bound the Warden’s ability to perform (2), no matter what pooling strategy they use. » [C21], où « Any such test is called a pooling strategy. » [C4] (p. 1). C'est une **borne supérieure** de la détection, pour **tout test**, avec **une** répartition (égale).
- L'énoncé du théorème est asymptotique : « we are only able to determine capacity a) asymptotically and b) without regard to the multiplicative constant of » [C9] (p. 2). Mais les inégalités de la preuve sont à N fini :
  - p. 3, lu sur le PDF, non contrôlé par programme : entropie relative du lot = N fois celle d’un objet < N·B·p²/2 = B·M²/(2N·C²), et (5) : d(α, β) ≤ D_KL(X₀‖X₁). La constante B est explicite (c'est le minorant de (log ψ)'' changé de signe ; B = 15000 dans l'exemple de la p. 4, auteurs ; recalculé : −14999,9995, calcul).
  - p. 2-3, lu sur le PDF, non contrôlé par programme : β < Φ(C₂ − C₃·M/√N) + C₁/√N (formule (4)). C₂ et C₃ se lisent dans la ligne qui précède et dans (6) : C₂ = −Φ⁻¹(α*/2)·√((1−q)/(1−q̄)), C₃ = A/(C·√(q̄(1−q))). Seule C₁ (reste de Berry-Esséen) n'est pas donnée : « Then there is some constant » [C18].

### 1.3 “La décroissance en n₀ à budget fixé est occupée” : juste, mais mal attribuée

- À M fixé et N croissant, on est dans le cas M/√N → 0 : c'est la **partie 2**. La décroissance de la détection est donc démontrée **pour la répartition égale, contre tout test**, à N fini et avec constante explicite (borne en M²/N). Elle n'est pas démontrée “pour toute répartition”, ni “avec le test des signes” : la partie 1 donne une borne inférieure de la détection, qui décroît avec N mais ne prouve pas que la détection décroît.
- Pour la statistique somme de L1, le transfert à toute répartition se fait par l'invariance de la somme (Ker 2006, rapport des voisins v2), que la lettre n'énonce pas : c'est un assemblage de deux pièces, en une ligne (calcul), pas un énoncé imprimé.
- La lettre rappelle le constat de 2006 sous la forme capacité : « risk of detection increases. But the investigation was limited » [C8] (p. 2). Elle n'imprime nulle part la phrase “à charge totale fixée, la détection décroît avec N” ; la borne en M²/N la contient.
- La case “occupée” tient. Elle est même plus ferme que ne l'écrit le rapport (N fini, constante, tout détecteur), mais sur un périmètre plus étroit (répartition égale).

### 1.4 Formule (4), p. 3

J'ai refait l'enchaînement (calcul) : lemme 1 avec une constante C₁ qui ne dépend que des bornes q et q̄ de (3), donc uniforme en la répartition ; majoration du dénominateur par N·q̄(1−q) pour le terme négatif et minoration par N·q(1−q̄) pour le terme positif ; théorème des accroissements finis, q − q_i = −p_i·ψ(p̂) ≤ −A·p_i avec A = inf de ψ sur [−1, 0] ; somme : −A·M/C. L'enchaînement tient.

- **Oui** : (4) majore l'erreur de second type du compte des signes par une fonction de (M, N) seulement — à ψ, C et α* fixés —, pour toute répartition fixée d'avance de proportions dans [0, 1], et l'inégalité vaut pour tout N (« which not only gives asymptotic behaviour but also bounds the difference from the asymptotic distribution function. » [C17], p. 2).
- **Trois réserves que le rapport ne fait pas** :
  1. Le niveau n'est pas tenu à N fini : la preuve donne α < α*/2 + C₁/√N (lu sur le PDF, p. 2), puis « which, for sufficiently large » [C19] N, moins de α*. Le seuil P* n'est pas un seuil de niveau α* à N fini ; C₁ est inconnue. La borne n'est donc ni chiffrable ni attachée à un niveau garanti à N fini.
  2. C'est une **inégalité de pire cas**, pas une invariance. La loi du compte des signes dépend de la répartition (q_i = 1 − Ψ(−p_i) n'est pas linéaire en p_i). Exemple, calcul : erreur gaussienne réduite, N = 100, total 2 ; espérance du compte 50,80 si la charge est répartie également, 50,68 si elle est concentrée sur deux objets. La lettre le dit en général : « so there is no UMP test; the results in [1] illustrate vividly how the performance of a pooling strategy can be heavily dependent on the embedding strategy. » [C28] (p. 4). Et l'auteur juge ses inégalités lâches : « we note that it is the extravagant inequalities in Section II-A which are primarily responsible for the gap. » [C27] (p. 4).
  3. Elle exige un décalage par objet plafonné (p_i ≤ 1) : A est le minimum de ψ sur [−1, 0] (A ≈ 0,9997 × 10⁻⁴ dans l'exemple, auteurs ; recalculé 0,99970 × 10⁻⁴, calcul).
- **Est-ce L3 (b) à horizon fixe ?** Non, c'est autre chose. L3 (b) (note v2, lignes 312 à 314) est la minoration “alarme d'ici n₀” ≥ “franchissement terminal”, rendue fonction de (B, n₀) **par l'invariance exacte L1 de la somme**. Son contenu à horizon fixe est donc L1 lui-même, dont le précédent le plus proche est Ker 2006 (même statistique, égalité en loi), pas la formule (4) (autre statistique, inégalité). Ce que (4) apporte de neuf : une garantie de détection fonction du seul total **pour des valeurs inégales**, imprimée.
- **“Voisin” : juste.** Pas trop faible : ni lecture toujours valide, ni même statistique, ni invariance, niveau asymptotique. Pas trop fort : l'idée “garantie de détection fonction du seul budget total, quelle que soit la répartition” y est imprimée et démontrée. “Le plus proche à ce jour” est à nuancer (constat D).

### 1.5 Cœur de L1 (invariance de la somme)

- Le mot “average” ne figure dans aucune des 4 pages (recherche par mots ; “mean” n'y apparaît que pour le théorème des accroissements finis et pour « Note that we do not require that the error has zero mean » [C23], p. 3). La seule somme de la lettre est celle des indicatrices de signe : « we have a sum of not-identically distributed random variables so we cannot use the central limit theorem as in [1]. » [C16] (p. 2).
- Pour le compte des signes il n'y a pas d'invariance (1.4, réserve 2). **La lettre n'occupe pas le cœur de L1**, ni pour la somme des scores, ni pour le test des signes. Le rapport a raison (section 0, point 1 ; section 4).

### 1.6 Valeurs inégales, queues lourdes, adaptativité

- **Valeurs inégales.** Admises : « In [1] we also imposed the constraint that all cover objects used for embedding had to contain the same amount of payload: the “uniform embedding” assumption. We relax this latter condition in this paper. » [C7] (p. 1, note 1). Mais elles ne servent qu'à la partie 1 (borne du compte des signes). La partie 2 revient à la répartition égale ([C20], [C22]). L'invariance de la somme sous valeurs inégales n'est imprimée nulle part dans la lettre. “Désormais couvertes” est exact pour la garantie de détection, inexact comme levée du résidu de L1 (constat C).
- **Queues lourdes.** Exact : « such a bound exists for many common distributions with infinite support including Gaussian, Cauchy, Logistic, and the Student » [C24] (p. 3). Vérifié par calcul : (log ψ)'' ≥ −2 pour la loi de Cauchy réduite. Les deux moitiés du théorème valent donc sans variance finie.
- **Adaptativité.** La phrase citée, « Note that the covers are considered uniform, not only in their capacity but also to prevent the Steganographer embedding adaptively. » [C5] (p. 1), vise le choix selon le contenu des objets. L'adaptativité de L (des δ_k qui dépendent des scores déjà observés) n'est pas nommée ; elle est hors du modèle, parce que la répartition est un choix fixé ([C3]), que N est connu d'avance ([C29]) et que la preuve traite les indicatrices comme indépendantes. “Exclue” est exact ; “exclue par hypothèse ([J10])” attribue à la phrase plus qu'elle ne dit (constat F).

### 1.7 Le séquentiel

Réservé : « This sequential setting is a little different from the batch setting considered here, and further work will be needed to study it. » [C30] (p. 4). Le rapport a raison. Une précision (calcul, constat H) : la borne de la partie 2 vaut pour tout test de (2) ([C4], [C21]) ; l'événement “alarme d'ici N” d'une règle lue en séquence dans le lot est un tel test. La lettre borne donc par le haut, en M²/N, la détection de toute règle, séquentielle comprise, sous répartition égale. Elle ne dit rien du calendrier, du coût du report ni du prix de la garantie toujours valide.

## 2. Constats

| constat | gravité | page | citation à l'appui | texte du rapport visé | texte corrigé proposé |
|---|---|---|---|---|---|
| A — | majeur | p. 2-3 | [C11], [C12], [C20], [C21], [C22] | Section 3, ligne “L1 — décroissance en n₀”, section 4, section 5 et section 6 point 1 : "La lettre la démontre pour la capacité, en ordre, pour toute répartition non adaptative, queues lourdes comprises" ; "avec le test des signes". | "La lettre démontre la décroissance de la détection à charge totale fixée pour la répartition égale, contre tout test (partie 2, borne d'entropie relative en M²/N), queues lourdes comprises. Pour toute répartition, elle démontre l'autre moitié : une garantie de détection par le compte des signes dès que M/√N tend vers l'infini (partie 1). Le transfert de la décroissance à toute répartition, pour la somme, passe par l'invariance de Ker 2006 : assemblage en une ligne, non imprimé." |
| B — | majeur | p. 3 (et p. 2, p. 4) | [C9], [C18], [C21] ; formules (5), (4), (6) lues sur le PDF | Section 0 point 2 et section 2 : "en ordre asymptotique, sans constante" ; section 0 point 3 : "Les constantes ne sont pas données". | "L'énoncé du théorème est asymptotique et sans constante. La preuve, elle, donne des inégalités à N fini : d(α, β) < B·M²/(2N·C²) pour tout test sous répartition égale, avec B explicite ; et la formule (4) avec C₂ et C₃ explicites (ligne précédant (4), et (6)), seule C₁ restant non donnée. La décroissance à charge fixée est donc imprimée à N fini, avec constante, pour tout détecteur." |
| C — | majeur | p. 1 (note 1), p. 3 | [C7], [C20], [C22], [C16] | Section 5 : "Valeurs inégales — couvertes par la lettre pour la loi de capacité. Ce n'est plus un résidu de L1 au-delà de l'écriture trajectorielle." ; section 2, ligne “valeurs inégales” ; section 7 : "valeurs inégales couvertes". | "Valeurs inégales — admises par la lettre dans la seule partie 1 (garantie de détection par le compte des signes). La partie 2 revient à la répartition égale. L'invariance de la somme sous valeurs inégales n'est imprimée ni dans la lettre ni chez Ker 2006 : le résidu de L1 décrit dans le rapport des voisins v2 (valeurs inégales, adaptatif, trajectoire ; une ligne ; remarque citée) est inchangé." |
| D — | majeur | p. 2-3, p. 4 | [C14], [C16], [C17], [C27], [C28] ; formule (4) lue sur le PDF | Section 0 point 3 : "La partie 1 du théorème est la pièce la plus proche à ce jour de L3 (b)" ; section 5 : "Ce qui reste distinctif est la seule couche “toujours valide”". | "Verdict “voisin” maintenu. La formule (4) est une inégalité de pire cas pour une autre statistique (le compte des signes, dont la loi dépend de la répartition), pas une invariance. Le contenu à horizon fixe de L3 (b) est L1 lui-même, dont le précédent le plus proche reste Ker 2006 ; la formule (4) y ajoute une garantie fonction du seul total pour des valeurs inégales. Ce qui reste distinctif de L3 (b) est le passage à la lecture toujours valide, qui est l'inclusion “franchissement terminal ⊂ alarme d'ici n₀” jointe à L1 : mathématiquement une ligne, à présenter comme telle." |
| E — | mineur | p. 2 | [C15], [C19], [C18] | Section 0 point 3 et section 2 : "à N fini (le reste de Berry-Esséen est explicite en C₁/√N)". | "L'inégalité (4) vaut pour tout N, mais le niveau du test n'est borné que par α*/2 + C₁/√N, avec C₁ non donnée : à N fini, ni le niveau ni la borne ne sont chiffrables. La borne suppose aussi un décalage par objet plafonné à 1 (A est le minimum de ψ sur [−1, 0])." |
| F — | mineur | p. 1, p. 4 | [C5], [C3], [C29] | Section 0 point 2 : "répartition quelconque mais non adaptative" appuyée sur [J10] ; section 6 point 5 : "elle l'exclut par hypothèse ([J10])". | "La phrase [J10] écarte le choix selon le contenu des objets. L'adaptativité au sens de L (valeurs dépendant des scores déjà observés) n'est pas nommée : elle est hors du modèle (répartition fixée d'avance, N connu d'avance, indicatrices indépendantes dans la preuve). Une phrase publique dira “non traitée”, pas “exclue en toutes lettres”." |
| G — | mineur | — | (cohérence interne du rapport) | Section 7 : "La revendication restante est la couche séquentielle et toujours valide." | "Restent non trouvés : la couche séquentielle et toujours valide (L4 sur plusieurs pas, L3 : calendrier, coût du report, prix de la garantie ; processus e cumulé contre détecteur de rupture), mais aussi, hors de cette couche, L2 au seuil exact, la validité sous dépendance, la non-compensation et l'application aux sondes — comme l'écrit la section 5 du même rapport." |
| H — | mineur | p. 1, p. 3 | [C4], [C21], [C30] | Section 3, ligne “L3 — calendrier, coût du report, prix du toujours valide” : "ne touche pas ; séquentiel réservé". | "Ne traite pas le séquentiel (réservé, p. 4). À noter : la borne de la partie 2 vaut pour tout test du lot, donc aussi pour l'événement “alarme d'ici N” d'une règle lue en séquence (déduction du contre-lecteur, non imprimée) : borne supérieure en M²/N de toute détection sous répartition égale. Une phrase publique ne dira pas qu'aucune borne de détection en fonction du budget total n'atteint les règles séquentielles." |
| I — | mineur | p. 2-3 | [C10], [C24], [C23] | Section 0 point 4 : "Le théorème vaut pour toute densité dont (log ψ)'' est minoré". | Ajouter : "La condition sur (log ψ)'' ne sert qu'à la partie 2 ; la partie 1 ne demande que le support infini et ψ positive et continue sur [−1, 0]. Aucune condition de moyenne nulle. Conséquence à queues lourdes : le compte des signes atteint l'ordre √N là où la moyenne de Ker 2006 ne l'atteint pas ; la somme n'y est donc pas le détecteur d'ordre optimal." |
| J — | mineur | p. 4 | [C25], [C26] | Section 8 : "J'ai vérifié à l'œil l'enchaînement des inégalités des p. 2-3 sans le recalculer." ; journal : texte et images lus entre 06:58:07 et 06:59:31. | Profondeur : lecture rapide (moins de deux minutes pour les deux passes), suffisante pour 4 pages au vu des citations, mais sans recalcul. Recalcul fait ici : l'enchaînement de (4) tient ; les bornes de la p. 4 se retrouvent (1,1635 × 10⁶ et 0,0081210, calcul ; rapport de 1,43 × 10⁸, soit huit ordres de grandeur). Le rapport peut écrire "recalculé par le contre-lecteur". La formule « If we pass to the limit we can tighten (4) to » [C25] passe de α*/2 à α* : sans effet sur les verdicts. |

## 3. Réponses aux cinq points du mandat

1. **Théorème 1.** Hypothèses rendues exactement (précision I). Capacité en racine de N démontrée en deux moitiés : garantie de détection pour toute répartition avec le compte des signes ; impossibilité de détecter pour la répartition égale contre tout test. “Décroissance en n₀ à budget fixé : occupée” : juste ; attribution à corriger (A), fermeté à relever (B).
2. **Formule (4).** Oui, borne fonction du seul total, pour toute répartition fixée d'avance, valable pour tout N ; mais niveau asymptotique, C₁ inconnue, décalage par objet plafonné (E). Ce n'est pas L3 (b) à horizon fixe : c'est une inégalité de pire cas pour une autre statistique (D). “Voisin” : juste.
3. **Cœur de L1.** Non occupé par la lettre, ni pour la somme (absente) ni pour le compte des signes (pas d'invariance). Le rapport a raison.
4. **Valeurs inégales** : admises pour la partie 1 seulement ; le résidu de L1 n'est pas levé (C). **Queues lourdes** : exact. **Adaptativité** : hors du modèle, exact ; la phrase citée vise autre chose (F).
5. **“Ce qui reste distinctif” resserré à la couche séquentielle et toujours valide** : trop étroit dans la section 7 du rapport (G), juste dans sa section 5 ; et, pour L3 (b), cette couche tient en une ligne (D).

## 4. Mon verdict sur L (table fermée) et par composante

**Occupé en partie.**

| composante de L | verdict | pièce et page |
|---|---|---|
| L1, cœur — égalité en loi de la somme, toute répartition | occupée en partie, par Ker 2006 seul ; la lettre ne touche pas (aucune statistique moyenne ; pas d'invariance pour le compte des signes) | lettre, p. 2 [C14, C16], p. 4 [C28] |
| L1 — décroissance en n₀ à budget fixé | occupée : Ker 2006 (moyenne, forme capacité) ; lettre : démontrée pour la répartition égale contre tout test, à N fini, constante explicite | lettre, p. 2-3 [C12, C20, C21, C22] |
| L4 — plusieurs pas, frontières de pas, toujours valide | voisin (cas d'un seul pas, par Ker 2006) ; la lettre ne touche pas | — |
| L2 — maximum au seuil exact, n fini | non trouvé ; contre-indice général de la lettre (la performance dépend de la répartition) | lettre, p. 4 [C28] |
| L3 (b) — borne inférieure invariante, lecture toujours valide | non trouvé en lecture toujours valide ; voisin : formule (4) (garantie fonction du seul total, valeurs inégales, autre statistique, horizon fixe, niveau asymptotique) ; contenu à horizon fixe = L1 (Ker 2006) ; résidu : une ligne | lettre, p. 2-3 [C11, C14, C17, C19] |
| L3 — calendrier, coût du report, prix de la garantie toujours valide | non trouvé ; séquentiel réservé ; borne supérieure générique en M²/N (constat H) | lettre, p. 3 [C21], p. 4 [C30] |
| processus e cumulé contre détecteur de rupture | non trouvé | — |
| non-compensation | non trouvé | — |
| validité sous dépendance | non trouvé ; indépendance posée | lettre, p. 1 [C6] |
| scores de sondes internes | non trouvé | — |

“Non trouvé” veut dire non trouvé dans la lettre et dans ce que j'ai lu du rapport des voisins v2 ; je n'ai lu ni le lot 8 ni les pièces de Ker 2006 et de Bash et collègues.

## 5. Ce qu'une phrase publique ne doit pas affirmer (ajouts ou retouches à la section 6 du rapport)

1. que la lettre démontre la décroissance de la détection à budget fixé pour toute répartition : elle la démontre pour la répartition égale, contre tout test (A) ;
2. que cette décroissance n'est connue qu'en ordre asymptotique : la borne en M²/N est à N fini, avec constante (B) ;
3. que la lettre couvre les valeurs inégales pour l'invariance de la somme (C) ;
4. que la formule (4) est une invariance, ou un test de niveau garanti à N fini (D, E) ;
5. que la borne invariante de L3 (b) est un résultat substantiel au-delà de L1 : c'est une inclusion d'événements jointe à L1 (D) ;
6. que la lettre exclut en toutes lettres l'adaptativité au sens de L (F) ;
7. qu'aucune borne de détection fonction du budget total n'atteint les règles séquentielles (H).

Je ne rédige pas la phrase publique. Le resserrement de la revendication est une décision du directeur.

## 6. Réserves de propreté (règle R4) et limites de cette contre-lecture

- Le rapport ne présente pas de résultat trop beau ; ses 40 citations se retrouvent toutes.
- Mes déductions marquées “calcul” (transfert par l'invariance, résidu d'une ligne de L3 (b), portée de la partie 2 aux règles séquentielles) sont des raisonnements de contre-lecteur, non imprimés dans la pièce ; ils demandent leur propre vérification avant tout usage.
- Voisins nommés dans la pièce et non lus : références [1] (Ker 2006, lu par le lecteur, pas par moi) et [2] (Cachin 2004), p. 4.

## 7. Refus

Aucun refus de permission, de crochet ni de classifieur. Aucune ouverture fautive.

## Annexe — citations contrôlées (`citations-contre-lecture-L-ker2007-v1.json`, dans l'archive)

Pièce unique : `ker-2007-capacity-result-batch-steganography.pdf`.

| id | page | citation exacte |
|---|---|---|
| C1 | 1 | A Capacity Result for Batch Steganography |
| C2 | 1 | We further assume that the estimation error distribution does not depend on the true value being estimated. |
| C3 | 1 | We say that a Steganographer’s embedding strategy is a choice of |
| C4 | 1 | Any such test is called a pooling strategy. |
| C5 | 1 | Note that the covers are considered uniform, not only in their capacity but also to prevent the Steganographer embedding adaptively. |
| C6 | 1 | are assumed independent. |
| C7 | 1 | In [1] we also imposed the constraint that all cover objects used for embedding had to contain the same amount of payload: the “uniform embedding” assumption. We relax this latter condition in this paper. |
| C8 | 2 | risk of detection increases. But the investigation was limited |
| C9 | 2 | we are only able to determine capacity a) asymptotically and b) without regard to the multiplicative constant of |
| C10 | 2 | at least twice continuously differentiable |
| C11 | 2 | There is a pooling strategy for the Warden such that, no matter what the Steganographer’s embedding strategy, |
| C12 | 2 | There is an embedding strategy for the Steganographer such that, no matter what the Warden’s pooling strategy, |
| C13 | 2 | It is a modification of the simplest pooling strategy investigated in [1] and certainly is not an “optimal” strategy in practice. |
| C14 | 2 | The Warden will count the number of positive estimates |
| C15 | 2 | the type-I and type-II errors are bounded by |
| C16 | 2 | we have a sum of not-identically distributed random variables so we cannot use the central limit theorem as in [1]. |
| C17 | 2 | which not only gives asymptotic behaviour but also bounds the difference from the asymptotic distribution function. |
| C18 | 2 | Then there is some constant |
| C19 | 2 | which, for sufficiently large |
| C20 | 3 | The Steganographer’s embedding strategy is simply to split the payload equally between all covers. |
| C21 | 3 | This will suffice to bound the Warden’s ability to perform (2), no matter what pooling strategy they use. |
| C22 | 3 | embedding strategy, identically distributed |
| C23 | 3 | Note that we do not require that the error has zero mean |
| C24 | 3 | such a bound exists for many common distributions with infinite support including Gaussian, Cauchy, Logistic, and the Student |
| C25 | 4 | If we pass to the limit we can tighten (4) to |
| C26 | 4 | It turns out that these two bounds on detection reliability are a long way apart. |
| C27 | 4 | we note that it is the extravagant inequalities in Section II-A which are primarily responsible for the gap. |
| C28 | 4 | so there is no UMP test; the results in [1] illustrate vividly how the performance of a pooling strategy can be heavily dependent on the embedding strategy. |
| C29 | 4 | is known to both parties, before any embedding takes place. |
| C30 | 4 | This sequential setting is a little different from the batch setting considered here, and further work will be needed to study it. |
