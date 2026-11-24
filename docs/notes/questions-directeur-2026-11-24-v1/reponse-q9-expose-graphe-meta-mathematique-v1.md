---
header-includes:
  - \usepackage{xurl}
lang: fr
---

# Le graphe méta-mathématique : ce qu'il est, où il s'insère, à quoi il servirait (question 9, v1)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle externe, aucune course.
- **Heure** : `2026-11-24T16:15:44Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille des questions du directeur (`session_016QhUrtAyz3dFV4u1BbUBoS`). **Écart signalé** : le dosage initial prévoyait Fable 5.2 (effort élevé) ; la file révisée de la mère, 15:29Z (`file-revisee-1530-v1.md`), confie la question 9 à Opus.
- **Lu** : `CLAUDE.md` (`dcd1e7ce…`) ; mandat et complément des questions 8 et 9 ; demande reformulée, question 9 (`632c7af2…`, l. 53-88) ; question sur le méta-espace (`d0f02738…`) ; réponses de Carbon sur le méta-espace (`01f859c0…`, en entier) et sur l'homomorphisme (`3f92cede…`, sections 1 et 4) ; réponse de Fable (`8ec4f9e0…`, partie 2) ; réponses aux questions 2 (`7f4cf73f…`), 5 (`0bdc9810…`, section 7), 7 (`937e3e69…`, sections 1, 2, 5) ; complément spectral ; Plan Turing (`69c8deae…`, volets 1, 2, 4). Questions 6, 8 et 10 non versées quand j'ai commencé (agent coupé par le quota). Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Longueur** : environ 2 800 mots du verdict au glossaire, en-tête et références non comptés.
- **Mesuré** : `exemple-graphe-meta-mathematique-v1.py` (`16e6bb1e…`) et sa sortie datée (`39cc2c75…`), dans ce dossier.

## Verdict

Le « graphe méta-mathématique » recouvre trois graphes distincts : énoncés et dépendances, domaines et classification, objets et applications qui conservent la structure. Les deux premiers existent dans des données publiques, et je les ai mesurés ; le troisième est à construire. Sur un jouet calculé, la correspondance historique entre permutations des racines et classes de formes quadratiques n'est **pas** la mieux notée : huit correspondances la battent en esquivant le conflit. Le graphe localise une tension. Il ne fabrique pas l'objet nouveau.

## 1. Le problème

Le modèle cherche des idées en alignant des structures entre domaines éloignés : si deux voisinages se ressemblent par la forme, un pont est plausible. Il suppose un **alphabet des relations** fixé (« est loi sur », « divise », « est neutre pour »…). L'objection : les révolutions conceptuelles enrichissent cet alphabet. Avant 1830, aucun mathématicien n'écrivait « ceci est un groupe ». On composait des permutations, on composait des classes de formes, sans mot commun.

Un graphe d'**usage** (qui cite quoi, quels mots vont ensemble) voit des communautés, pas l'invariant. Un graphe de **structure** voit les relations, mais seulement celles que l'alphabet sait écrire. Quand le mot manque, l'invariant apparaît en creux : des alignements presque réussis qui butent toujours au même endroit, des calculs semblables refaits sous des noms différents, des questions qui convergent. La troisième couche, dite « méta », sert à enregistrer ces creux et à tester les objets candidats qui les combleraient.

## 2. Trois graphes, démêlés

| | (1) Énoncés et dépendances | (2) Domaines et classification | (3) Objets et applications qui conservent la structure |
|---|---|---|---|
| Nœuds | définitions, théorèmes, fichiers | rubriques (« 20 : théorie des groupes ») | objets typés : un ensemble, une loi, une propriété |
| Arêtes | « la preuve de B utilise A », importations | renvois « voir aussi », co-classement d'un article | relations typées internes à un domaine ; entre domaines, une correspondance φ |
| Types | déclaration, instance, notation | niveau hiérarchique | types de nœuds et de relations communs à tous les domaines |
| Dates | date de dépôt du code (agenda de formalisation, non histoire [12, section 4]) | révisions de la classification ; dates des articles indexés | à reconstruire à partir des textes datés |
| Existe | mathlib, bibliothèque de Lean 4 [1, 2] | classification des sujets mathématiques de 2020 [3] ; zbMATH Open [4] | non : proposée (Fable, partie 2 ; Carbon [12]) |

Le graphe (1) dit **ce qui dépend de quoi** ; le (2) dit **comment les humains rangent** ; le (3) dit **ce qui a la même forme**. Ils ne coïncident pas : sur mathlib entier (308 129 déclarations, 7 563 modules), le rangement en dossiers et la structure des dépendances divergent, information mutuelle normalisée de 0,34 contre 0,71 entre dossiers et noms [5, p. 5]. Le (3) est le seul où vit la correspondance φ, au sens de Fable : une injection partielle du voisinage typé de a dans celui de b, étiquettes de noms effacées, types gardés. Une **catégorie** au sens d'Eilenberg et Mac Lane [6] (des objets, des flèches qui se composent) en est la forme idéale ; il suffit ici d'un graphe orienté typé.

## 3. Le fil rouge : la naissance du concept de groupe

**Pourquoi cet exemple plutôt que les algèbres amassées.** L'histoire est documentée sur sources vérifiées [7, 8] ; les deux côtés se calculent à la main (exercices de la section 6) ; l'objet né est aujourd'hui présent dans les trois graphes (dossier `GroupTheory` de mathlib, rubrique 20, suite A000001 de l'encyclopédie en ligne des suites de nombres entiers). Les algèbres amassées, plus récentes et datables par arXiv [9], servent à la section 5 pour une mesure sur la classification.

**Les deux domaines.**

- A, les permutations des racines. Lagrange (1770-1771) montre que si une fonction des n racines prend r « valeurs » sous les n! permutations, alors r divise n! [7, p. 102, théorème C] ; Galois introduit le mot « groupe » pour les permutations en 1831 [7, p. 103] ; Cauchy, en 1844, définit un système de substitutions comme un ensemble clos par composition [7, p. 104].
- B, les classes de formes quadratiques binaires. Gauss (1801) définit une composition des classes, montre l'associativité, et tient « en fait » un groupe abélien fini, sans le mot [8].

**Couche d'usage.** Trois vocabulaires pour une structure : « valeurs d'une fonction », « substitutions conjuguées », « composition des classes ». C'est le signal d'entropie notationnelle de Carbon (méta-espace, section 2, signal 3).

**Couche des problèmes.** Lagrange ne sait pas s'il existe, pour n = 5, une fonction à 3 ou 4 valeurs, qui donnerait une résolvante de degré 3 ou 4 ; son théorème ne tranche pas, puisque 3 et 4 divisent 5! [7, p. 102]. C'est un hyperarc de question au sens de la question 7 : des prémisses (le théorème, n = 5) vers une cible sans témoin connu. Son poids monte avec la résistance (Ruffini, Abel). Le fil de la question mène à l'objet : ce sont les ensembles de permutations clos qui décident.

**Couche de structure et correspondance (mesuré, jouet).** Le script code A en huit relations typées et B en six, simplifiées à dessein. La correspondance historique φ envoie composition sur composition, substitutions sur classes, identité sur classe principale, etc. Les quatre cas :

| Relation de A | Image dans B | Cas |
|---|---|---|
| composition est loi sur substitutions ; identité neutre ; inverse ; associativité ; ensemble clos sous-ensemble | existe, même type | **confirmée** (5) |
| composition **réfute** la commutativité (dès 3 racines) | composition **vérifie** la commutativité | **contredite** (1), compte dans κ |
| nombre de valeurs divise l'ordre total | rien entre ordre d'une classe et nombre de classes | **absente** (1) : prédiction de relation |
| la résolvante est invariante sous un ensemble clos | la résolvante n'a pas d'image | **extrémité sans image** (1) : prédiction d'objet manquant, comme une case vide de Mendeleïev |

Couverture c = 5/8 = 0,625, part des conflits κ = 1/8, c − κ = 0,500 (sortie, partie 1).

**Réification.** Ajouter un nœud « groupe » change l'alphabet de trois façons. La relation absente devient conséquence d'un seul énoncé, « l'ordre d'un sous-groupe divise l'ordre du groupe » : la prédiction est juste (exercice 2). Le conflit cesse d'en être un : « commutatif » devient un paramètre de l'objet, non une contradiction entre domaines. Et un énoncé écrit une fois retire de la surprise dans A, dans B et ailleurs : c'est la profondeur au sens de la question 2. Cayley donne en 1854 une définition abstraite [10 ; 8]. La case vide (l'analogue de la résolvante dans B) reste une question du jouet : je n'affirme aucun analogue historique.

## 4. L'intégration au modèle

- **Couche de structure** (Fable, partie 2) : φ, c, κ, puis Z, l'écart de c − κ à sa moyenne sous recâblage qui préserve degrés et types. Le jouet montre pourquoi les types de nœuds sont indispensables (section 6).
- **Couche des problèmes** (question 7, section 5) : un hypergraphe orienté [11], où une question est un hyperarc demandé sans témoin et une anomalie l'opposition d'un hyperarc de prédiction et d'un hyperarc de mesure ; poids (écart, résistance, portée, centralité des prémisses, maturation) ; couplage au taux de naissance par un terme δ·P.
- **Couche méta**, l'« atelier » de Carbon [12, section 3] : schémas anti-unifiés de dérivations répétées, obstructions d'alignement (le résidu exact de φ : ici, l'arête de commutativité et la case de la résolvante), séquents ouverts, proto-objets à axiomes partiels ; un lien de réification abaisse un proto-objet validé en primitive de la couche de structure.
- **Coordonnées spectrales** (complément du 24 novembre). Les « harmoniques » d'un graphe sont les vecteurs propres de son laplacien ; une application fonctionnelle écrit φ comme une matrice C entre deux bases propres, presque diagonale si φ conserve la structure [13 ; réponse à la question 5, section 7, d'après la p. 2-3]. La « dimension cachée » serait un mode commun que φ révèle, comme une composante commune, faible dans chaque jeu de variables, ressort de l'analyse des corrélations canoniques [14] : **une analogie**. Elle casse sur trois points (analyse de l'auteur) : un graphe typé et orienté n'a pas de laplacien symétrique canonique ; deux valeurs propres proches rendent leurs vecteurs instables (un petit bruit les fait tourner dans leur plan) ; deux domaines éloignés ne sont pas presque isométriques, et les premiers modes codent la popularité.
- **Profondeur** : la surprise retirée ailleurs (question 2), éprouvée en perturbant les **faits** ; **largeur ou étroitesse** : en perturbant la **correspondance**. Deux perturbations distinctes, mesurées toutes deux à la section 5.
- **Plasticité** et **forme de l'anomalie** : questions 8 et 10, non encore répondues ; je ne fais que les situer. La plasticité serait la facilité d'une région à se réorganiser sous une réification sans casser les relations confirmées ; elle n'est ni définie ni mesurée ici.
- **Plan Turing.** Les mondes plantés (volet 4) donnent une φ et des cases vides connues de l'orchestrateur seul : le seul endroit où « le graphe a trouvé le trou » se vérifie. Lean 4 (volet 2) [2] arbitre une prédiction de relation : la relation absente devient un énoncé ; une preuve acceptée, dont `#print axioms` ne montre que les axiomes standard, la confirme.

## 5. Les données réelles, et ce qui a été mesuré

| Source | Contenu | Licence, accès | Ce qu'on en tire | Ce qu'on n'en tire pas |
|---|---|---|---|---|
| mathlib [1] | déclarations Lean, importations | Apache 2.0 ; dépôt git, commit daté | graphe (1) exact, au grain fichier sans compiler, au grain déclaration avec Lean et l'outil `lake exe graph` [15] | l'histoire : les dates sont celles de la formalisation |
| Classification des sujets mathématiques 2020 [3] | 6 603 rubriques, renvois | CC BY-NC-SA 4.0 ; fichier sur msc2020.org | graphe (2), renvois entre rubriques | la naissance d'un objet avant sa rubrique |
| zbMATH Open [4] | plus de 4 millions de notices, rubriques par article | CC BY-SA 4.0 [4, p. 2] ; interface de programmation ouverte depuis 2021 [4, p. 1] | comptes datés par rubrique, co-classements | le contenu des preuves ; résumés de tiers parfois absents [4, p. 2] |
| Encyclopédie en ligne des suites de nombres entiers [16] | suites, lignes de renvoi | CC BY-SA 4.0 ; fichiers en notation d'objets JavaScript | renvois entre objets dénombrés (graphe (3) partiel) | les relations typées au-delà du renvoi |

**Mesuré** (sortie du 24 novembre, 16:11-16:14Z ; mathlib au commit `41e07aa7…` du 24 novembre 2026, 14:47Z ; fichier de la classification `f7c88935…`) :

- **Jouet, largeur.** Sur les 362 880 bijections des neuf nœuds appariables, le maximum de c − κ vaut 0,625 et non 0,500 : huit bijections battent φ. Elles envoient la commutativité de A sur un nœud numérique sans relation avec la composition (le nombre de classes ou l'ordre d'une classe) : le conflit devient une absence, qui ne coûte rien. Cent bijections sont à un huitième du maximum ou mieux (part 2,8 × 10⁻⁴) : le puits est étroit. En imposant la conservation du type des nœuds, il reste 16 bijections, maximum 0,500, atteint par quatre, dont φ : la structure seule ne distingue pas associativité et commutativité dans ce jouet.
- **Jouet, profondeur.** En retirant chaque fait de B avec probabilité 0,15 (2 000 tirages, graine 20261124, `SeedSequence`), c − κ vaut 0,430 en moyenne, entre 0,250 et 0,625 (quantiles 5 % et 95 %) : retirer un fait peut **relever** le score, en cachant un conflit.
- **mathlib, dossier `GroupTheory`** : 174 fichiers, 240 importations internes, 317 venues d'ailleurs, dont 176 de l'algèbre, 60 des données et 25 des tactiques ; chaîne interne la plus longue : 21 fichiers ; environ 4 330 théorèmes ou lemmes (comptage textuel).
- **Classification** : 2 880 renvois, dont 84,4 % vers une autre section de premier niveau ; depuis la théorie des groupes, surtout vers les groupes topologiques et de Lie (22, 13 renvois) et la logique (03, 8).
- **Encyclopédie des suites** : A000001, « nombre de groupes d'ordre n », révision 347, renvoie à 20 suites.
- **zbMATH, algèbres amassées (rubrique 13F60)** : documents par année, 0 en 2000-2001, 1 en 2002, 0 de 2003 à 2006, puis 2, 11, 19, 47, 70, 63 de 2007 à 2012. Les 17 notices de 2003 à 2006 dont le titre contient « cluster algebras » ne portent pas 13F60 et se dispersent sur 10 sections de premier niveau. Lecture : l'objet existait avant sa case ; la case de 2002 est l'article fondateur [9], étiqueté après coup (étiquette rétroactive, à confirmer). La date d'entrée de 13F60 dans la classification reste **à vérifier**.

## 6. Trois idées fausses, trois exercices

**Idées fausses.**
1. *« C'est un seul graphe. »* Trois, et ils divergent [5, p. 5]. Mêler dépendances et rangement mesure les habitudes des bibliothécaires.
2. *« Le meilleur score donne la bonne analogie. »* Sur le jouet, huit correspondances battent l'historique en esquivant le conflit. Il faut des types de nœuds, un coût pour l'absence, et le nul du recâblage.
3. *« Le graphe trouvera l'objet nouveau. »* Il dit où l'alphabet coince : résidus, cases vides, questions convergentes. Le contenu de l'objet vient d'un proposeur et se juge après coup, sur monde planté ou par Lean.

**Exercices** (réponses vérifiées par le script, partie « Exercices », et par le calcul à la main).
1. Combien de paires ordonnées (f, g) de permutations de trois racines ne commutent pas ? *Réponse : 18 sur 36* (paires commutantes = 6 × 3 classes de conjugaison).
2. Lister les formes réduites (a, b, c) de discriminant b² − 4ac = −23, avec |b| ≤ a ≤ c. En déduire l'ordre possible d'une classe. *Réponse : (1, 1, 6), (2, ±1, 3), donc trois classes ; chaque classe est d'ordre 1 ou 3, comme le prédit la relation absente.*
3. Dans le jouet, échanger les images de l'associativité et de la commutativité. Que deviennent les quatre cas ? *Réponse : c − κ reste 0,500 ; les deux propriétés ont le même type de relation avec la composition, et seuls les noms, effacés, les séparaient.*

## 7. Ce que cet objet ne peut pas faire, et ce qui reste spéculatif

- **Ne peut pas** créer l'objet : explorer à vide bute sur le dilemme du programme de découverte automatique AM (« Automated Mathematician »), primitives qui encodent la cible ou prolifération stérile (Ritchie et Hanna 1984, cité par Carbon [12, section 1] ; à vérifier).
- **Ne peut pas** dater une naissance historique à partir de mathlib [12, section 4], ni prendre une rubrique nouvelle pour une date de découverte (retard et étiquetage rétroactif, mesurés plus haut).
- **Ne peut pas** garantir la bonne φ : la trouver est un problème d'affectation quadratique, difficile même à approcher (question 5, section 7).
- **Proposé, non mesuré** : la couche des problèmes pondérée et couplée ; l'atelier de réification ; la plasticité.
- **Spéculatif** : qu'une « dimension cachée » commune existe en général ; qu'une réification se prédise avant d'être écrite ; que la circularité se casse en comprimant les frictions du présent, pari de Carbon [12, section 3], que rien ici n'éprouve.
- **Antériorité (règle R8)** : la structure de réseau de mathlib est étudiée [5] ; la compression mesurée sur mathlib comme indice d'intérêt mathématique est proposée par Aksenov, Bodnia, Freedman et Mulligan [17, p. 1] ; la prédiction de liens entre concepts datés existe hors des mathématiques (Science4Cast, question 7, référence [20]). Deux pistes vues en recherche, non lues : TheoremGraph et un graphe de dépendances typé de mathlib pour la sélection de prémisses. Aucune ne combine, à ma lecture, les trois graphes, la couche des problèmes et la réification jugée sur monde planté : une question, non un trou établi.

## 8. Homonymie

Cet exposé est un « topo », non la théorie des topos. Celle-ci, née chez Grothendieck [18], est pourtant une vraie voisine de l'unification par un objet commun : pour Caramello, un topos classifiant, commun à des théories équivalentes au sens de Morita, agit comme un « pont » qui transfère résultats et idées d'une théorie à l'autre [19, p. 17 ; 20]. Différence : son pont exige une équivalence exacte, notre φ est partielle et bruitée.

## Glossaire

- **Alphabet des relations** : les types de relations qu'on sait écrire.
- **Correspondance φ** : envoi partiel des nœuds d'un domaine sur ceux d'un autre.
- **Couverture c, part des conflits κ** : relations transportées intactes ; relations dont l'image existe avec un type incompatible.
- **Réification** : faire d'une opération répétée un objet nommé de l'alphabet.
- **Hyperarc** : arc d'un ensemble de prémisses vers une conclusion.
- **Laplacien** : matrice d'un graphe (degrés moins adjacence) dont les vecteurs propres sont ses « harmoniques ».
- **Recâblage** : graphe tiré au hasard aux mêmes degrés et types, qui sert de nul.

## Références

1. The mathlib Community (2020). The Lean mathematical library. *Proceedings of the 9th ACM SIGPLAN International Conference on Certified Programs and Proofs*, 367-381. <https://doi.org/10.1145/3372885.3373824> (notice Crossref) ; code au commit du 24 novembre 2026 : <https://github.com/leanprover-community/mathlib4/commit/41e07aa72723cccf73caa3351d8e57d3797b8d97> (licence Apache 2.0, fichier `LICENSE` lu).
2. de Moura, L. et Ullrich, S. (2021). The Lean 4 theorem prover and programming language. *CADE 28*, Lecture Notes in Computer Science 12699, 625-635. <https://doi.org/10.1007/978-3-030-79876-5_37> (notice Crossref).
3. Mathematics Subject Classification 2020. <https://msc2020.org/> ; fichier `MSC_2020.csv` téléchargé le 24 novembre 2026, empreinte `f7c889354c20…` ; licence CC BY-NC-SA 4.0 (lien de la page).
4. Petrera, M., Trautwein, D., Beckenbach, I., Ehsani, D., Müller, F., Teschke, O., Gipp, B. et Schubotz, M. (2021). zbMATH Open: API solutions and research challenges. arXiv 2106.04664. <https://arxiv.org/abs/2106.04664> (PDF lu, p. 1-2) ; interface : <https://api.zbmath.org/.>
5. Li, X., Peng, N., Severini, S. et Shafto, P. (2026). The network structure of Mathlib. arXiv 2604.24797. <https://arxiv.org/abs/2604.24797> (PDF lu, p. 1 et 5).
6. Eilenberg, S. et MacLane, S. (1945). General theory of natural equivalences. *Transactions of the American Mathematical Society* 58, 231-294. <https://doi.org/10.1090/S0002-9947-1945-0013131-6> (notice Crossref).
7. Roth, R. L. (2001). A history of Lagrange's theorem on groups. *Mathematics Magazine* 74(2), 99-108. <https://doi.org/10.2307/2690624> (notice Crossref) ; PDF lu, <https://www.math.univ-toulouse.fr/~bauval/Roth.pdf,> p. 99, 102-104.
8. O'Connor, J. J. et Robertson, E. F. The development of group theory. MacTutor, université de St Andrews. <https://mathshistory.st-andrews.ac.uk/HistTopics/Development_group_theory/> (page lue le 24 novembre 2026 : Gauss, Galois, Cayley) ; source de fond : Wussing, H. (1984). *The Genesis of the Abstract Group Concept*. MIT Press (notice citée par [7] et [8], livre non lu).
9. Fomin, S. et Zelevinsky, A. (2002). Cluster algebras I: foundations. *Journal of the American Mathematical Society* 15, 497-529. <https://doi.org/10.1090/S0894-0347-01-00385-X> ; prépublication arXiv math/0104151 du 13 avril 2001 ; et (2002). The Laurent phenomenon. *Advances in Applied Mathematics* 28, 119-144. <https://doi.org/10.1006/aama.2001.0770> (notices Crossref et arXiv).
10. Cayley, A. (1854). On the theory of groups, as depending on the symbolic equation θⁿ = 1. *Philosophical Magazine* 7, 40-47. <https://doi.org/10.1080/14786445408647421> (notice Crossref).
11. Gallo, G., Longo, G., Pallottino, S. et Nguyen, S. (1993). Directed hypergraphs and applications. *Discrete Applied Mathematics* 42, 177-201. <https://doi.org/10.1016/0166-218X(93)90045-P> (notice Crossref).
12. Carbon, réponse sur le méta-espace mathématique, `docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-meta-espace-v1.md` (`01f859c0…`) ; ses références ne sont pas vérifiées ici.
13. Ovsjanikov, M., Ben-Chen, M., Solomon, J., Butscher, A. et Guibas, L. (2012). Functional maps: a flexible representation of maps between shapes. *ACM Transactions on Graphics* 31(4), 30. <https://doi.org/10.1145/2185520.2185526> (notice Crossref ; pages lues par la réponse à la question 5).
14. Hotelling, H. (1936). Relations between two sets of variates. *Biometrika* 28, 321-377. <https://doi.org/10.2307/2333955> (notice Crossref).
15. leanprover-community, `import-graph`. <https://github.com/leanprover-community/import-graph> (fichier `README.md` lu : `lake exe graph`).
16. The On-Line Encyclopedia of Integer Sequences, A000001. <https://oeis.org/A000001> ; licence CC BY-SA 4.0, <https://oeis.org/wiki/The_OEIS_End-User_License_Agreement> (lue).
17. Aksenov, V., Bodnia, E., Freedman, M. H. et Mulligan, M. (2026). Compression is all you need: modeling mathematics. arXiv 2603.20396. <https://arxiv.org/abs/2603.20396> (PDF lu, p. 1).
18. Artin, M., Grothendieck, A. et Verdier, J.-L. (1972). *Théorie des topos et cohomologie étale des schémas* (SGA 4), tome 1. Lecture Notes in Mathematics 269. <https://doi.org/10.1007/BFb0081551> (notice Crossref).
19. Caramello, O. (2010). The unification of mathematics via topos theory. arXiv 1006.3930. <https://arxiv.org/abs/1006.3930> (PDF lu, section 6, p. 16-17).
20. Caramello, O. (2017). *Theories, Sites, Toposes*. Oxford University Press. <https://doi.org/10.1093/oso/9780198758914.001.0001> (notice Crossref).
