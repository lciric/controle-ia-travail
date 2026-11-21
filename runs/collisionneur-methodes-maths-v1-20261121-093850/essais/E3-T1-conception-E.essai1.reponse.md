*Note d'intégrité des pièces (Règle 2) : les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont complets ; aucune proposition A–D n'est transmise, conformément au protocole à l'aveugle du Tour III.1.*

---

## 1. Ce qu'un expert ferait ici sans qu'on le lui demande — et livrable (a) : présupposés non établis

Un mathématicien travaillant à l'interface de la statistique minimax, du contrôle séquentiel, de la théorie des jeux et de la preuve mécanisée ne commencerait **pas** par lancer cinq lignées de modèles de langage (`RAPPORTÉ`) à l'assaut de nouveaux théorèmes. Il exécuterait quatre opérations préalables absentes de la demande :

1. **Tenter d'abord de tuer le problème par réduction canonique inter-domaines.** Les cinq questions cibles du programme — clôture d'archive, plafond d'horizon, agrégateur sous corrélation adverse, lemme d'impossibilité, sonde ne lisant que l'indication (`RAPPORTÉ`) — ne tombent pas dans un vide mathématique. Elles se projettent directement sur quatre théories classiques déjà très développées (`VÉRIFIÉ`) :
   - les bornes inférieures minimax de tests d'hypothèses (lemme de Neyman-Pearson, méthode des deux points et des mélanges de Le Cam, lemme d'Assouad, inégalité de Fano sur projections linéaires) ;
   - la fusion de tests sans hypothèse de dépendance (*e-valeurs* et fonctions de fusion de *p-valeurs*, bornes de Fréchet-Hoeffding et transport multi-marginal : par linéarité de l'espérance, la moyenne arithmétique de *e-valeurs* demeure une *e-valeur* valide sous corrélation adverse arbitraire, `VÉRIFIÉ`) ;
   - les martingales de test non négatives et l'inégalité maximale de Ville en échantillon fini (`VÉRIFIÉ`) ;
   - les jeux d'inspection séquentiels (*inspection games* d'Avenhaus–von Stengel–Zamir) et l'analyse de données adaptative (*adaptive data analysis* pour l'usure d'une archive face à des requêtes répétées) (`VÉRIFIÉ`).
   Avant de chercher une preuve nouvelle, l'expert écrit le foncteur de traduction qui dépouille l'énoncé de tout vocabulaire « agent / saboteur / jumeau / moniteur » pour vérifier ce que les théorèmes existants donnent déjà et **où exactement** leurs hypothèses échouent.
2. **Sceller les définitions formelles hors de portée des agents et imposer des témoins de non-vacuité.** Dans Lean 4, le noyau vérifie qu'un terme habite un type (`VÉRIFIÉ`), jamais que ce type traduit fidèlement le phénomène étudié (`VÉRIFIÉ`). Sous sélection (« un mort reste mort », `RAPPORTÉ`), les proposeurs optimisent la prouvabilité en affaiblissant silencieusement les définitions ou en exploitant des conventions totales de Mathlib (comme `x / 0 = 0` dans `Real` ou la soustraction tronquée `a - b = 0` pour `a < b` dans `Nat`, `VÉRIFIÉ`) (`HYPOTHÈSE`). L'expert fige lui-même les structures Lean et exige pour chaque théorème `H → C` la preuve mécanique d'un lemme témoin `∃ x, H x ∧ NonTrivial x`.
3. **Contourner le goulet de la théorie de la mesure dans Mathlib par la dualité finie.** L'outillage Lean 4 / Mathlib du programme n'est pas encore relevé conforme (`RAPPORTÉ`) — je ne sais pas quel sous-ensemble exact de Mathlib est déjà câblé dans ce harnais. Mais un expert de Lean sait que formaliser de nouvelles bornes probabilistes directement dans `MeasureTheory` consomme l'essentiel de l'effort en obligations de mesurabilité et d'intégrabilité (`OBSERVÉ-NON-AUDITÉ` dans les projets de formalisation probabiliste), alors que par dualité de programmation linéaire (lemme de Farkas, `VÉRIFIÉ`), toute borne d'impossibilité, de couplage adverse ou de jeu d'audit sur alphabets finis possède un **certificat dual rationnel fini** vérifiable dans Lean par simple algèbre linéaire sur `Fintype` sans théorie de la mesure.
4. **Ancrer les hypothèses des sondes sur le spectre réel des états internes.** Sans contraintes géométriques tirées d'activations réelles (rang effectif des covariances, rapport signal/bruit entre jumeau honnête et saboteur), un théorème d'impossibilité risque de reposer sur des distributions adverses mathématiquement licites mais absentes des réseaux étudiés (`HYPOTHÈSE`).

### Livrable (a) — Ce que la question suppose sans que ce soit établi

- **P1 — Transférabilité des succès constructifs aux bornes universelles (`HYPOTHÈSE`).** La question suppose que les méthodes ayant réussi avec des LLM (recherche de programmes, évolution, preuve Lean) se transfèrent aux besoins du programme. Or construire un objet discret maximisant un score ($\exists x, f(x) > c$) est structurellement distinct de prouver une borne d'impossibilité universelle ($\forall \psi \inf_{(P_0,P_1)} \dots$), qui ne s'évalue pas nativement par un programme scalaire sans réduction duale préalable (`VÉRIFIÉ` structurellement ; transfert effectif : `HYPOTHÈSE`).
- **P2 — Équivalence entre preuve formelle compilée et vérité mathématique visée (`HYPOTHÈSE`).** Le point 4 associe le vérificateur formel à la vérification du « vrai ». Cela n'est établi que modulo la fidélité et la non-vacuité des définitions, que Lean ne contrôle pas (`VÉRIFIÉ`).
- **P3 — Neutralité des « données brutes » mathématiques (`HYPOTHÈSE`).** Le point 2 oppose données brutes et résumés analysés. En mathématiques formelles, une bibliothèque comme Mathlib encode déjà des choix ontologiques lourds (types dépendants, fonctions totales, filtrations) qui rendent certains énoncés naturels et d'autres coûteux à exprimer (`VÉRIFIÉ` sur l'encodage ; neutralité : `HYPOTHÈSE`).
- **P4 — Détectabilité de l'antériorité malgré le changement de jargon (`HYPOTHÈSE`).** Le pilote a éprouvé un juge de nouveauté sur quarante énoncés connus plantés (`RAPPORTÉ`, métriques exactes non transmises donc `OBSERVÉ-NON-AUDITÉ` quant au taux réel hors échantillon). Rien n'établit que la recherche d'antériorité résiste aux isomorphismes inter-disciplinaires entre contrôle d'IA, actuariat et statistique séquentielle (`HYPOTHÈSE`).
- **P5 — Compatibilité budgétaire de la boucle complète (`HYPOTHÈSE`).** Produire, filtrer et prouver dans Lean 4 sous « quelques centaines de dollars par course » et « relecture humaine rare » (`RAPPORTÉ`) suppose un coût de convergence formelle inférieur de plusieurs ordres de grandeur à celui des démonstrateurs industriels massifs (`HYPOTHÈSE` ; je ne sais pas quel est le coût exact en dollars des courses internes d'AlphaProof ou FunSearch, non publié de façon auditée).

---

## 2. Les données brutes qu'un expert prendrait au départ

Plutôt que des synthèses sur la sécurité de l'IA ou des résumés d'articles, l'expert rassemble cinq fonds bruts :

1. **Corpus de problèmes (sources $\LaTeX$ intégrales, énoncés + preuves non abrégées)** :
   - les douze mondes plantés du pilote (`RAPPORTÉ`) sous forme de code générateur exact ;
   - un corpus primaire complet d'articles de bornes inférieures minimax (tests de sous-espaces et mélanges gaussiens), d'agrégation robuste de *p-valeurs* / *e-valeurs* sous dépendance arbitraire, d'inégalités de concentration uniformes en temps (martingales de Ville), et de jeux d'inspection sous budget, avec tous leurs lemmes techniques internes.
2. **Bibliothèques formelles (AST typés, pas de docstrings résumées)** :
   - un commit figé hors ligne de `Mathlib4`, extrait sous forme de graphe de dépendances de types et de signatures complètes (`MeasureTheory.Probability`, `Probability.Martingale`, `LinearAlgebra`, `Analysis.Convex`), exposant les classes de types implicites exactes exigées par chaque lemme (`VÉRIFIÉ` quant à l'architecture de Mathlib4).
3. **Journaux de preuves (*proof logs* bruts)** :
   - les traces `(état_tactique_avant, tactique, état_après, message_erreur_noyau)` issues de la compilation de `Mathlib4` et des tentatives locales, **y compris les branches échouées** où se concentrent les obligations d'intégrabilité, de positivité et de finitude qui font dérailler les LLM (`HYPOTHÈSE`).
4. **Banques de contre-exemples exécutables (matrices rationnelles exactes et lois à petit support)** :
   - *paires de lois appariées en moments ou sur sous-espaces* $(P_0, P_1)$ sur $\mathbb{R}^d$ indiscernables par toute sonde linéaire de rang $k < d$ ;
   - *copules adverses extrêmes* sur $\{0,1\}^M$ réalisant les bornes de Fréchet-Hoeffding et les régimes de dépendance positive maximale à marginales fixées ;
   - *trajectoires d'arrêt optionnel* violant le taux de fausse alerte des tests à horizon fixe ;
   - *tenseurs bruts d'activations internes* enregistrés sur des paires réelles (modèle honnête, saboteur planté) pour calibrer empiriquement les spectres de covariance.
5. **Archives de tentatives (journal append-only structuré)** :
   - pour chaque mort antérieure (« un mort reste mort », `RAPPORTÉ`), conserver le quadruplet brut `(énoncé formel exact, tentative de preuve/code, témoin exact de réfutation c*, hash des hypothèses)` : résumer « la conjecture X est fausse » détruit le contre-exemple $c^*$ dont la structure géométrique dicte précisément l'hypothèse manquante (`HYPOTHÈSE`).

---

## 3. Méthodes et outils publiés — et livrable (c) [partie 1 : instruments de découverte et preuve]

*Conformément à la règle d'intégrité 3, aucun identifiant arXiv n'est donné de mémoire (« arXiv : pas sûr / omis par règle 3 ») et toute référence dont un élément bibliographique exact comporte une incertitude est marquée « référence à vérifier ».*

1. **Recherche guidée par programme évaluable** & **2. Génération et sélection évolutionnaire**
   - *Travaux* : Romera-Paredes et al. (2024, mise en ligne fin 2023), *Mathematical discoveries from program search with large language models* (*Nature* — référence à vérifier pour l'année d'imputation bibliographique exacte, arXiv : pas sûr / omis par règle 3) [*FunSearch*] ; Charton, Ellenberg, Williamson, Garg (2024, *PatternBoost* — référence à vérifier, arXiv : pas sûr / omis par règle 3) ; rapport technique *AlphaEvolve* (DeepMind, 2025 — référence à vérifier, arXiv : pas sûr / omis par règle 3).
   - *Ce qu'ils supposent* : l'existence d'un évaluateur rapide, déterministe, impossible à tromper, attribuant un score gradué à des programmes construisant des objets finis (`VÉRIFIÉ`).
   - *Ce qu'ils ont donné* : nouvelles bornes inférieures constructives sur le problème du *Cap Set* et le *bin packing* en ligne dans *FunSearch* (`VÉRIFIÉ` par publication auditée), ainsi que des constructions extrémales sur des problèmes finis ouverts dans *AlphaEvolve* (`RAPPORTÉ`).
   - *Où ils échouent* : paysages de score plats (tout candidat non valide vaut 0), absence de preuve universelle pour tout $n \to \infty$ sans réintervention humaine (dans *FunSearch*, l'extraction conceptuelle est humaine, `VÉRIFIÉ`), et *reward hacking* dès que l'évaluateur tolère des imprécisions flottantes ou des cas dégénérés.
3. **Formalisation automatique (*Autoformalization*)**
   - *Travaux* : Wu, Jiang, Li, Rabe, Staats, Jamnik, Szegedy (2022), *Autoformalization with Large Language Models* (arXiv : pas sûr / omis par règle 3).
   - *Ce qu'elle suppose* : un alignement suffisant entre le $\LaTeX$ mathématique et les idiomes de la bibliothèque cible (Isabelle/HOL ou Lean/Mathlib).
   - *Ce qu'elle a donné* : traduction syntaxiquement typable d'une fraction substantielle de problèmes de compétition type MiniF2F (`RAPPORTÉ` / publié).
   - *Où elle échoue* : **hallucination sémantique silencieuse** — le type compile dans Lean mais oublie une condition de régularité ou change le domaine d'un quantificateur, et dès qu'un concept n'existe pas déjà dans Mathlib, le modèle invente des identifiants inexistants (`VÉRIFIÉ` dans la littérature du domaine).
4. **Recherche de preuve dans Lean**
   - *Travaux* : Polu et Sutskever (2020), *Generative Language Modeling for Automated Theorem Proving* (arXiv : pas sûr / omis par règle 3) ; Yang et al. (2023), *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models* (arXiv : pas sûr / omis par règle 3) ; *AlphaProof* (DeepMind, 2024 — référence à vérifier, arXiv : pas sûr / omis par règle 3) ; lignées *DeepSeek-Prover* et *InternLM-StepProver* (2024–2025 — références à vérifier, arXiv : pas sûr / omis par règle 3). Hors Lean mais instructif : Trinh, Wu, Le, He, Luong (2024), *Solving olympiad geometry without human demonstrations* (*Nature*, arXiv : pas sûr / omis par règle 3).
   - *Ce qu'elle suppose* : énoncé formel déjà posé et exact, accès rapide au REPL Lean, et couverture suffisante des lemmes de base dans Mathlib.
   - *Ce qu'elle a donné* : résolution automatique de problèmes d'olympiades formalisés et de théorèmes de benchmarks (MiniF2F, ProofNet) (`RAPPORTÉ` / `VÉRIFIÉ` selon les bancs publics).
   - *Où elle échoue* : explosion combinatoire dès qu'il faut **inventer une définition auxiliaire** (un invariant de martingale, un couplage non nommé), coût de compilation massif par arbre de recherche, et blocage sur la plomberie de coercions de types dans Mathlib4.
5. **Découverte de contre-exemples**
   - *Travaux* : Wagner (2021), *Constructions in combinatorics via neural networks* (apprentissage par renforcement hors LLM, arXiv : pas sûr / omis par règle 3) ; couplages LLM + test aléatoire de propriétés inspirés de Claessen et Hughes (2000), *QuickCheck: a lightweight tool for random testing of Haskell programs* (`VÉRIFIÉ`) et solveurs SMT comme de Moura et Bjørner (2008), *Z3: An Efficient SMT Solver* (`VÉRIFIÉ`).
   - *Ce qu'elle suppose* : que les hypothèses et la négation de la conclusion soient décidables et évaluables sur des structures finies.
   - *Ce qu'elle a donné* : réfutation effective de plusieurs conjectures ouvertes en théorie des graphes chez Wagner (2021) (`VÉRIFIÉ`).
   - *Où elle échoue* : contre-exemples n'apparaissant qu'à très grande taille ou en régime asymptotique continu, et faux contre-exemples causés par l'instabilité numérique `float64` près de matrices mal conditionnées.
6. **Conjecture automatique**
   - *Travaux* : Fajtlowicz (programme *Graffiti*, années 1980 — référence exacte à vérifier) ; Raayoni et al. (2021), *Generating conjectures on fundamental constants with the Ramanujan Machine* (*Nature* — référence à vérifier pour la liste complète des auteurs, arXiv : pas sûr / omis par règle 3) ; Davies et al. (2021), *Advancing mathematics by guiding human intuition with AI* (*Nature*, arXiv : pas sûr / omis par règle 3) ; boucles d'auto-jeu formel de conjectures dans Lean (*STP* et travaux connexes 2024–2025 — références à vérifier, arXiv : pas sûr / omis par règle 3).
   - *Ce qu'elle suppose* : une mesure de parcimonie et d'intérêt qui filtre l'océan infini des vérités triviales.
   - *Ce qu'elle a donné* : dans Davies et al. (2021), mise en évidence de relations structurelles entre invariants de nœuds et en théorie des représentations, ensuite formulées et prouvées **par des mathématiciens humains** (`VÉRIFIÉ`).
   - *Où elle échoue* : **inflation de tautologies** — sans pression adverse, un générateur d'énoncés produit massivement des spécialisations triviales ou des relations purement accidentelles sur petites tailles.
7. **Décomposition en lemmes**
   - *Travaux* : Jiang et al. (2023), *Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs* (référence à vérifier pour la liste complète des auteurs, arXiv : pas sûr / omis par règle 3) ; *LEGO-Prover* (Wang et al., 2023/2024 — référence à vérifier, arXiv : pas sûr / omis par règle 3).
   - *Ce qu'elle suppose* : que le LLM maîtrise assez la macro-structure d'une preuve pour découper le but en sous-buts `have` **tous vrais** et individuellement fermables par des tactiques courtes.
   - *Ce qu'elle a donné* : gains nets de taux de preuve sur MiniF2F par rapport à la recherche tactique pas-à-pas aveugle (`VÉRIFIÉ` dans la littérature publiée).
   - *Où elle échoue* : **lemmes intermédiaires zombies** — un seul sous-but `have` légèrement trop fort (faux sur un cas de bord) engloutit tout le budget du prouveur en aval.
8. **Mémoire et réemploi**
   - *Travaux* : récupération de prémisses dans *LeanDojo / ReProver* (Yang et al., 2023, arXiv : pas sûr / omis par règle 3) ; bibliothèques évolutives de lemmes dans *LEGO-Prover* (référence à vérifier, arXiv : pas sûr / omis par règle 3).
   - *Ce qu'ils supposent* : que la similarité d'état tactique ou d'énoncé prédit l'utilité déductive future, et que l'archive reste propre.
   - *Ce qu'ils ont donné* : amélioration du choix de prémisses dans de grandes bibliothèques formelles (`VÉRIFIÉ`).
   - *Où ils échouent* : **pollution d'archive (*library bloat*)** quand des centaines de micro-lemmes ad hoc noient le récupérateur, et **faux morts** dans une mémoire négative (enterrer toute une famille d'énoncés alors que l'échec venait d'une constante mal choisie) (`HYPOTHÈSE`).

### Livrable (c) [partie 1] — Mesure minimale de fonctionnement des 8 instruments du point 3

| Instrument | Taux de détection (vrais positifs) & Taux de fausses alertes (faux positifs) | Cas honnêtes appariés | Vérification mécanique à battre |
| :--- | :--- | :--- | :--- |
| **1. Programme évaluable** | *Détection* : fraction de mondes plantés où le programme atteint la borne optimale connue. *Fausse alerte* : programme scoré au-dessus de l'optimum vrai par fuite numérique ou violation de domaine (*reward hacking*). | Même problème avec contrainte d'indiscernabilité active vs relâchée (où la borne analytique change d'une quantité connue). | Tirage aléatoire de paramètres + optimiseur boîte noire (`CMA-ES` / solveur LP-SDP direct) à budget CPU égal. |
| **2. Sélection évolutionnaire** | *Détection* : amélioration stricte du meilleur candidat vérifié entre la génération 1 et $G$ sur mondes durs. *Fausse alerte* : convergence prématurée sur un artefact de la grille finie réfuté hors échantillon ($m' > m$). | Course évolutionnaire vs tirage indépendant sans mutation/croisement (*best-of-$N$*) sur les mêmes graines d'évaluation. | *Best-of-$N$* indépendant à nombre identique d'appels LLM et d'évaluations. |
| **3. Formalisation automatique** | *Détection* : énoncés vrais traduits en types Lean compilables **et** prouvés bi-impliqués avec la formalisation de référence. *Fausse alerte* : énoncé Lean compilable mais sémantiquement affaibli ou vacu, accepté par le filtre. | Paires d'énoncés informels différant d'une seule hypothèse critique (ex. indépendance vs martingale). | Traduction zéro-coup sans boucle d'erreur Lean ni test de non-vacuité. |
| **4. Preuve dans Lean** | *Détection* : théorèmes vrais scellés fermés sans `sorry` ni axiome parasite. *Fausse alerte* : contournement du harnais (`unsafe`, axiome ajouté, modification du fichier cible — doit valoir 0%). | Paires `(énoncé vrai scellé, énoncé muté faux)` sur les mêmes définitions. | Portefeuille de tactiques déterministes seules (`aesop`, `linarith`, `omega`, `positivity`, `simp`, `exact?`) à temps CPU égal. |
| **5. Découverte de contre-exemples** | *Détection* : conjectures fausses plantées réfutées par un témoin exact certifié en $\mathbb{Q}$. *Fausse alerte* : théorème vrai déclaré réfuté à cause d'erreurs flottantes ou d'un témoin hors domaine. | Paires `(lemme vrai serré, lemme faux obtenu en améliorant la constante de ε)`. | Énumération exhaustive sur petits cardinaux + `Plausible`/QuickCheck aléatoire + `Z3` à budget égal. |
| **6. Conjecture automatique** | *Détection* : émission d'un énoncé vrai, non trivial et impliquant la cible plantée. *Fausse alerte* : émission d'un énoncé faux (survivant aux petits $n$) ou d'une tautologie algébrique déguisée. | Mondes à loi de structure cachée exacte vs mondes purement bruités où aucune borne meilleure que la triviale n'existe. | Énumération systématique d'inégalités polynomiales/affines de petit degré (style *Graffiti* / régression symbolique) sans LLM. |
| **7. Décomposition en lemmes** | *Détection* : découpes dont **tous** les sous-buts `have` sont vrais et dont la preuve totale aboutit alors que la preuve directe échoue. *Fausse alerte* : sous-lemme faux non détecté avant allocation du budget de preuve. | Même théorème prouvé avec découpe `have` vs recherche monolithique à budget total (jetons + CPU) strictement identique. | Recherche de preuve directe sans esquisse intermédiaire, précédée d'un crible QuickCheck sur chaque `have`. |
| **8. Mémoire et réemploi** | *Détection* : gain net de théorèmes résolus (ou coupe immédiate d'une branche déjà réfutée) grâce aux entrées récupérées. *Fausse alerte* : injection d'un lemme distrayant faisant baisser le succès, ou blocage d'une variante vraie (« faux mort »). | Courses séquentielles avec archive active vs mémoire purgée entre chaque problème sur paires de lemmes cousins. | Recherche lexicale/type `Loogle` + `exact?` sur Mathlib nue sans mémoire épisodique d'organisme. |

---

## 4. Vérification hors du programme et de son directeur — et livrable (c) [partie 2 : instruments d'audit]

Aucun instrument isolé ne couvre simultanément **vrai**, **nouveau** et **utile** (`VÉRIFIÉ` méthodologiquement) :

1. **Vérificateur formel externe** (`lean4checker` rejouant les `.olean` depuis une installation vierge et vérifiant `#print axioms` restreint aux axiomes standards `propext`, `Quot.sound`, `Classical.choice`, `VÉRIFIÉ`) : certifie la validité déductive interne sans faire confiance au harnais du programme, mais **reste aveugle à la vacuité ou à l'infidélité des définitions**.
2. **Preuve rejouable** (conteneur déterministe hors réseau, hash SHA-256 figé ; et pour les bornes finies, script court en arithmétique rationnelle exacte vérifiant la faisabilité duale) : établit qu'un tiers reproduit mécaniquement le verdict, sans prouver ni la nouveauté ni la pertinence du modèle.
3. **Recherche d'antériorité externe** (requêtes dans MathSciNet, zbMATH, arXiv et `Loogle`/`Moogle` **après dé-jargonisation** vers les vocabulaires de la statistique minimax, de l'actuariat/Fréchet et des jeux d'inspection) : ne « prouve » jamais la nouveauté dans l'absolu, mais tente de la **réfuter** par réduction courte aux classiques.
4. **Relecture par des mathématiciens externes** (spécialistes de statistique non paramétrique, de martingales ou de théorie des jeux lisant uniquement les ~50 lignes [illustratif] de définitions Lean + l'énoncé dé-jargonisé, en aveugle quant à l'origine IA) : **seul filtre capable d'évaluer la profondeur conceptuelle**, la fidélité des définitions et l'antériorité folklorique non indexée ; déchargé de l'audit calculatoire grâce à Lean.
5. **Réplication opératoire externe** : seule preuve de l'**utilité**. Une équipe tierce applique l'agrégateur ou le test séquentiel à ses propres agents honnêtes et saboteurs : un théorème d'algorithme est utile s'il tient son taux nominal $\alpha$ de fausses alertes en échantillon fini tout en augmentant la puissance ; un théorème d'impossibilité lu à l'envers (`RAPPORTÉ`) est utile s'il permet de construire mécaniquement un saboteur qui contourne un moniteur réel dès que l'hypothèse nommée est violée.

### Livrable (c) [partie 2] — Mesure minimale des 5 instruments du point 4 (orientés en filtres d'audit de défauts)

| Instrument externe | Taux de détection (rejet d'un résultat défectueux) & Fausse alerte (rejet d'un résultat sain) | Cas honnêtes appariés | Vérification mécanique à battre |
| :--- | :--- | :--- | :--- |
| **9. Vérificateur formel (pipeline d'audit)** | *Détection* : rejet de 100% [illustratif] des preuves comportant axiome caché, `sorry`, exploit d'environnement ou hypothèses contradictoires. *Fausse alerte* : rejet d'une preuve valide non vacue par timeout/version. | Preuve Lean saine d'un lemme vrai vs même lemme prouvé via une hypothèse contradictoire glissée dans une `structure`. | `lean4checker` nu + `#print axioms` sans test automatique de satisfiabilité des hypothèses. |
| **10. Preuve rejouable** | *Détection* : détection de toute dépendance non déterministe, fuite d'oracle externe ou instabilité d'arrondi. *Fausse alerte* : échec de rejeu d'un certificat valide par simple dérive d'outillage système. | Certificat rationnel exact valide vs certificat flottant tangent violant une contrainte duale de $10^{-12}$ [illustratif]. | Script déterministe en conteneur isolé (`--network=none`) + vérification en `fractions.Fraction`. |
| **11. Recherche d'antériorité** | *Détection* : rappel sur des théorèmes publiés réécrits dans le lexique « sonde / saboteur / jumeau ». *Fausse alerte* : classer comme déjà connu un raffinement dont la borne bat strictement le théorème cité sur un témoin fini. | Théorème classique camouflé vs variante vraie avec contrainte supplémentaire changeant la vitesse minimax. | Recherche BM25 + embeddings denses standards sur le texte brut non dé-jargonisé + `Loogle`. |
| **12. Relecture mathématique** | *Détection* : identification des définitions infidèles, tautologies déguisées et corollaires triviaux ayant passé Lean. *Fausse alerte* : rejet d'un résultat nouveau non trivial par biais ou malentendu notationnel. | Dossier anonymisé mêlant vrais lemmes nouveaux serrés et corollaires en 5 lignes [illustratif] de Le Cam / Ville formalisés en 400 lignes [illustratif] Lean. | Crible pré-humain automatique (vacuité Lean + antériorité multi-lexique + témoin fini de séparation). |
| **13. Réplication (utilité)** | *Détection* : mise en évidence d'une violation du taux $\alpha$ promis ou d'une absence de gain sur banc d'agents tiers (hypothèses du théorème irréalistes). *Fausse alerte* : échec imputable à un bogue d'intégration du réplicateur. | Traces d'agents honnêtes appariées (respectant vs violant l'hypothèse nommée du théorème) face à leurs jumeaux saboteurs. | Baseline statistique standard hors étagère : test séquentiel de Wald / fusion moyenne de *e-valeurs* calibrée sur jumeau honnête. |

---

## 5. Reformulation de la demande — et livrable (b) : expériences décisives (`H_A` contre `H_B`)

### Demande reformulée
> *Sous un budget de quelques centaines de dollars par course (`RAPPORTÉ`) et une intervention humaine concentrée sur le scellement amont des définitions et l'audit aval des rares survivants, quelle architecture hybride — couplant solveurs exacts sur mondes finis, traduction canonique anti-redécouverte et noyau Lean 4 à spécifications scellées — maximise le nombre de résultats simultanément **(1) compilés et prouvés non vacus dans Lean 4**, **(2) séparés quantitativement des bornes classiques de statistique minimax, de martingales et de jeux d'inspection sur au moins un témoin fini**, et **(3) prédictifs d'une attaque ou d'une garantie vérifiée sur traces réelles de moniteurs**, en battant à coût égal une baseline mécanique sans boucle d'agents ?*

### Livrable (b) — Quatre expériences décisives en inférence forte

**Expérience E1 — Dé-jargonisation canonique vs Juge de nouveauté direct (teste P4)**
- **$H_A$ (Isomorphisme caché dominant)** : Sans réduction préalable vers les vocabulaires de la statistique minimax, des *e-valeurs*/Fréchet et des *inspection games*, le juge de nouveauté laisse passer une proportion substantielle de théorèmes connus camouflés, que la traduction canonique intercepte.
- **$H_B$ (Suffisance du juge interne)** : Le juge de nouveauté éprouvé sur quarante énoncés (`RAPPORTÉ`) résiste déjà au camouflage terminologique sans étape de réduction inter-domaines.
- **Protocole & Contrôle négatif** : Assembler 30 énoncés [illustratif] : 15 théorèmes publiés (Le Cam, Ville, Vovk-Wang, Avenhaus) réécrits en jargon « sonde / jumeau / moniteur » (**contrôle négatif de nouveauté**, nouveauté vraie = 0%) et 15 raffinements plantés possédant un témoin fini où la borne classique est lâche. Comparer le juge actuel seul au juge précédé d'un réducteur multi-dialectes.
- **Métrique & Seuil** : Taux de faux nouveaux sur les 15 contrôles négatifs et gain de rappel $\Delta R$ ; seuils : faux nouveaux $> 20\%$ [illustratif] sur le juge nu et $\Delta R \ge 25$ points de pourcentage [illustratif].
- **Issues falsifiantes** : Si le juge nu dépasse $20\%$ [illustratif] de faux nouveaux et que le réducteur gagne $\ge 25$ points [illustratif], **$H_B$ est falsifiée**. Si le juge nu reste $\le 20\%$ [illustratif] avec $\Delta R < 25$ points [illustratif], **$H_A$ est falsifiée**.

**Expérience E2 — Extraction de certificats duaux finis (LP/SDP) vs Suite symbolique/numérique générique (teste P1)**
- **$H_A$ (Primauté de la dualité finie)** : Sur les cibles d'impossibilité, de couplage adverse et de jeux d'audit, formuler chaque monde fini comme un programme linéaire/semi-défini exact pour extraire le couple `(saboteur primal, multiplicateur dual)` permet de conjecturer la borne analytique exacte hors échantillon sur davantage de mondes que la « suite bon marché » actuelle (`RAPPORTÉ`).
- **$H_B$ (Échec d'encodage ou parité)** : Les erreurs de formulation LP/SDP des LLM ou la non-interprétabilité des duaux empêchent tout gain sur la suite symbolique/numérique existante à budget égal.
- **Protocole & Contrôle négatif** : Sur les douze mondes plantés à vérité calculée (`RAPPORTÉ`), déclinés en 24 instances paramétrées [illustratif], comparer à budget fixe de 40 $/monde [illustratif] le bras `LLM + LP/SDP rationnel exact` contre le bras `suite bon marché`. **Contrôles négatifs** : bras `lecture nue` (`RAPPORTÉ`) et solveur LP nu sans synthèse symbolique.
- **Métrique & Seuil** : Nombre d'instances où la formule générale conjecturée est exacte à grande taille ($m' = 50$ [illustratif]) avec taux de fausses alertes $\le 5\%$ [illustratif] ; seuil d'écart : $+4/24$ instances [illustratif].
- **Issues falsifiantes** : Gain $\ge +4/24$ [illustratif] avec fausses alertes $\le 5\%$ [illustratif] $\Rightarrow$ **$H_B$ falsifiée**. Gain $< +4/24$ [illustratif] ou fausses alertes $> 5\%$ [illustratif] $\Rightarrow$ **$H_A$ falsifiée**.

**Expérience E3 — Énoncés Lean scellés + témoin de non-vacuité vs Autoformalisation libre sous sélection (teste P2)**
- **$H_A$ (Dégénérescence sélective des spécifications)** : Lorsque l'organisme formalise lui-même les types cibles sous pression de survie, il produit des théorèmes compilés mais sémantiquement dégénérés (vacuité, pathologie de division totale, affaiblissement).
- **$H_B$ (Autoformalisation fidèle)** : L'autoformalisation contrôlée par un juge LLM de fidélité prévient toute validation d'énoncé faux ou dégénéré.
- **Protocole & Contrôle négatif** : Lancer l'organisme sur 20 énoncés [illustratif] : 10 vrais difficiles et **10 faux subtils servant de contrôle négatif absolu** (aucun ne peut être prouvé fidèlement). Comparer R1 (énoncé Lean écrit par l'agent + juge LLM) et R2 (définitions et énoncé scellés + obligation mécanique `∃ x, Hyp x ∧ NonTrivial x`).
- **Métrique & Seuil** : Taux d'énoncés faux ou dégénérés compilés et acceptés en R1 ; seuil : $\ge 10\%$ [illustratif] (ou $\ge 1/10$ [illustratif] sur les contrôles négatifs faux).
- **Issues falsifiantes** : Si R1 valide $\ge 1$ contrôle négatif faux ou $\ge 10\%$ [illustratif] d'énoncés dégénérés tandis que R2 reste à $0\%$, **$H_B$ est falsifiée**. Si R1 reste à $0\%$ sur les faux et $< 10\%$ [illustratif] au total, **$H_A$ est falsifiée**.

**Expérience E4 — Preuve Lean sur noyau discret `Fintype` vs `MeasureTheory` générale sous contrainte budgétaire (teste P5)**
- **$H_A$ (Asphyxie par la théorie de la mesure)** : Sous un plafond de 100 $/lemme [illustratif], prouver la version algébrique finie (`Fintype`) réussit nettement plus souvent que prouver directement la version `MeasureTheory` générale dans Mathlib4.
- **$H_B$ (Parité de la formalisation générale directe)** : Les prouveurs LLM guidés par récupération de prémisses ferment les preuves `MeasureTheory` à un taux proche de `Fintype` sous le même budget.
- **Protocole & Contrôle négatif** : 12 lemmes vrais [illustratif] issus des cinq cibles, chacun scellé en deux versions (`Fintype` vs `MeasureTheory`), budget plafonné à 100 $/lemme [illustratif]. **Contrôle négatif** : tactiques automatiques Lean seules (`aesop`, `linarith`, `omega`, `positivity`) sans LLM.
- **Métrique & Seuil** : Écart de taux de preuves complètes compilées ; seuil : $\ge 30$ points de pourcentage ($\ge 4/12$ lemmes) [illustratif] en faveur de `Fintype`.
- **Issues falsifiantes** : Écart $\ge 30$ points [illustratif] $\Rightarrow$ **$H_B$ falsifiée** (l'arbitre formel doit opérer sur le noyau discret fini). Écart $< 30$ points [illustratif] $\Rightarrow$ **$H_A$ falsifiée**.

---

## 6. Propositions concrètes de méthodes, ancrage matériel (d) et part réelle d'effort humain et de chance

*Ce qui suit relève de mes propositions méthodologiques (`HYPOTHÈSE` quant à leur rendement futur avant exécution des tests de mort).*

### Méthode M1 — Distillation symbolique de certificats primaux-duaux (DSCPD)
*Cibles : lemme d'impossibilité, sonde linéaire ne lisant que l'indication, valeur du jeu d'audit sous budget.*
- **Principe** : Sur un alphabet discrétisé de taille $m$, calculer une borne d'impossibilité de détection sous contraintes de projection linéaire ou la valeur minimax d'un jeu d'audit sous budget est un programme linéaire ou semi-défini convexe (`VÉRIFIÉ`). Pour $m \in \{2,\dots,12\}$ [illustratif], un solveur exact extrait **la paire adverse optimale** $(P_0^*, P_1^*)(m)$ et **le vecteur dual optimal** $y^*(m)$ en rationnels $\mathbb{Q}$. Les cinq lignées de proposeurs n'inventent pas une preuve dans le vide : elles interpolent la forme analytique creuse de $y^*(n,d)$ en fonction des paramètres du problème. Une fois le candidat $y^*(n,d)$ explicité, la preuve universelle pour tout $(n,d)$ dans Lean 4 se réduit à vérifier l'inégalité algébrique finie $A^\top y^*(n,d) \ge c$ (`Fintype`, sommes finies, `positivity`/`linarith`).
- **Distinction par rapport au publié** : *FunSearch* (Romera-Paredes et al., 2024) évolue des constructions primales sans produire de preuve universelle d'impossibilité ; les prouveurs Lean standards cherchent par tactiques sans oracle convexe dual. DSCPD convertit une preuve minimax $\forall \exists$ en **interpolation de multiplicateurs de Farkas suivie d'une identité algébrique élémentaire**.
- **Premier pas** : Coder le générateur LP exact en $\mathbb{Q}$ pour « sonde linéaire de rang $k$ sur $\mathbb{R}^d$ discret » et vérifier qu'il redécouvre automatiquement le multiplicateur dual de Le Cam sur deux des douze mondes plantés (`RAPPORTÉ`).
- **Coût en ordre de grandeur** : 40 à 120 $ par course [illustratif].
- **Test de mort** : Abandon immédiat si, sur $\ge 3$ sur 4 [illustratif] mondes plantés d'impossibilité/jeux à solution analytique connue, les vecteurs duaux $y^*(m)$ n'ont pas de support structuré interpolable ou si la formule conjecturée échoue à $m' = 50$ [illustratif] sous 150 $/monde [illustratif].

### Méthode M2 — Co-évolution Lakatosienne d'hypothèses vérifiables sur données honnêtes (CLHV)
*Cibles : agrégateur sous corrélation adverse, plafond d'horizon séquentiel.*
- **Principe** : Opérationnaliser directement l'idée des « théorèmes d'impossibilité lus à l'envers, dont les hypothèses nommées sont les suppositions des moniteurs » (`RAPPORTÉ`). Deux populations s'affrontent autour d'un ensemble courant d'hypothèses formelles $\mathcal{H}_t$ :
  1. *Attaquants (constructeurs de copules et de temps d'arrêt)* : maximisent par code + LP la probabilité de fausse alerte (ou de sabotage manqué) d'un agrégateur sous $\mathcal{H}_t$, générant un contre-exemple certifié $c_t^*$.
  2. *Raffineurs* : proposent une hypothèse supplémentaire $h_{t+1}$ éliminant toute la classe géométrique de $c_t^*$, **soumise à un double verrou** : (i) $h_{t+1}$ ne doit pas impliquer la conclusion en moins de 4 lignes [illustratif] de `linarith` (anti-tautologie), et (ii) $h_{t+1}$ doit être **satisfaite empiriquement par $\ge 90\%$ [illustratif] d'une banque scellée de traces de jumeaux honnêtes** (garantissant que l'hypothèse mathématique correspond à une propriété réelle des moniteurs).
- **Distinction par rapport au publié** : Wagner (2021) réfute une conjecture fixe ; les boucles d'auto-jeu dans Lean mutent des énoncés sans contrainte de réalisabilité empirique. CLHV co-optimise la frontière mathématique $(\mathcal{H}_T \implies \text{Borne})$ sous ancrage statistique direct sur cas honnêtes.
- **Premier pas** : Lancer l'arène sur $K=3$ moniteurs et horizon $T=10$ [illustratif] en partant de l'indépendance $\mathcal{H}_0$, et vérifier que l'arène redécouvre d'elle-même la séparation entre agrégation par *e-valeurs* (robuste à toute copule) et agrégation par seuils de *p-valeurs* sous dépendance positive bornée.
- **Coût en ordre de grandeur** : 80 à 220 $ par course de 40 rondes [illustratif].
- **Test de mort** : Abandon si après 40 rondes [illustratif] $> 80\%$ [illustratif] des hypothèses survivantes sont soit des reformulations quasi tautologiques de la borne visée, soit violées par $> 30\%$ [illustratif] des traces honnêtes de contrôle.

### Méthode M3 — Portier de séparation quantitative multi-dialectes (*Separation-First Gate*)
*Cible : clôture d'archive pour le juge et filtrage en amont de Lean sur les cinq cibles.*
- **Principe** : Aucun énoncé n'entre dans l'étage coûteux de preuve Lean sans passer deux barrières : (1) traduction automatique sans jargon IA vers les quatre dialectes canoniques (minimax, *e-processus*/Ville, Fréchet/transport, *inspection games*) et tentative de démolition en $\le 15$ lignes [illustratif] à partir d'une base codée de 30 inégalités classiques [illustratif] ; (2) fourniture d'un **témoin rationnel fini de séparation** $w_{\text{sep}}$ prouvant numériquement que la nouvelle borne bat strictement toutes les bornes classiques applicables de cette base sur $\mathcal{H}$.
- **Distinction par rapport au publié** : Remplace le jugement subjectif de nouveauté par LLM par un **certificat calculable d'écart quantitatif** contre les théorèmes de référence.
- **Premier pas** : Encoder 25 à 30 bornes classiques [illustratif] évaluables sur mondes finis et tester le portier sur les quarante énoncés connus plantés du programme (`RAPPORTÉ`) camouflés en jargon de contrôle.
- **Coût en ordre de grandeur** : 5 à 15 $ par candidat filtré [illustratif].
- **Test de mort** : Abandon si le rappel sur les quarante énoncés plantés camouflés est $< 85\%$ [illustratif] ou si le taux de rejet de vrais raffinements plantés munis d'un écart réel dépasse $20\%$ [illustratif].

### Livrable (d) — Ancrage matériel

- **Modèles à poids ouverts (exécutables hors ligne sur la machine isolée Lean 4)** (`VÉRIFIÉ` quant à la disponibilité publique des poids ; configuration exacte `illustrative`) :
  - *Preuve tactique et récupération dans Lean 4* : `DeepSeek-Prover-V1.5-RL` (7B) ou `DeepSeek-Prover-V2` (7B), `InternLM2.5-StepProver` (7B), et `ReProver` (< 1B, récupération de prémisses sur Mathlib4).
  - *Synthèse locale de programmes LP/rationnels et réductions* : `Qwen2.5-Math-72B-Instruct` ou `Qwen2.5-Coder-32B-Instruct` et `DeepSeek-R1-Distill-Qwen-32B` servis localement (`vLLM`).
  - *Solveurs mécaniques ouverts (CPU)* : `Lean 4` + `Mathlib4` + `lean4checker`, `HiGHS` / `CLARABEL` (`cvxpy`), `SymPy` / `SageMath` (arithmétique rationnelle exacte GMP/FLINT), `Z3`.
- **Calcul nécessaire par course** :
  - 1 nœud isolé équipé de **1 à 2 GPU 80 Go VRAM** (type A100/H100) et **64 cœurs CPU avec 128 Go RAM** [illustratif] pendant 8 à 16 h [illustratif] (le parallélisme des tactiques Lean 4 et des solveurs LP exacts est limité par le CPU et la RAM autant que par le GPU).
  - Étage externe d'idéation/raffinement sur les cinq lignées de proposeurs (`RAPPORTÉ`) : 3 à 8 M de jetons d'entrée et 0,8 à 2 M de jetons de sortie par course [illustratif].
- **Coût total estimé par course** : **90 à 250 $ [illustratif]** (30 à 65 $ de calcul GPU/CPU isolé + 60 à 185 $ d'appels aux cinq lignées [illustratif]), compatible avec « quelques centaines de dollars par course » (`RAPPORTÉ`) **uniquement** parce que M3 et M1 bloquent l'entrée dans Lean tant qu'un certificat dual fini et un témoin de séparation ne sont pas acquis.

### Part réelle de temps, d'effort humain et de chance

Il faut dire sans détour ce qu'un tel organisme ne fera pas seul :
1. **Effort humain incompressible** : dans tous les précédents publiés solides — tels que Davies et al. (2021) ou Romera-Paredes et al. (2024) (`VÉRIFIÉ`) — l'essentiel du travail de modélisation amont et de généralisation conceptuelle aval a été accompli par des chercheurs humains. Ici, « relecture humaine rare » (`RAPPORTÉ`) ne sera viable que si un mathématicien consacre **3 à 5 jours-homme par cible en amont** [illustratif] pour sceller des définitions Lean 4 fidèles et non vacues et vérifier l'encodage LP de base, puis **1 à 2 jours-homme en aval** [illustratif] par candidat survivant pour relever un lemme `Fintype` vers sa forme continue propre et auditer le sens physique des hypothèses. Sans cet investissement humain ciblé, l'organisme optimisera les failles de ses propres spécifications (`HYPOTHÈSE`).
2. **Temps calendaire** : relever conforme l'outillage Lean 4 (`RAPPORTÉ`), passer les expériences E1–E4 et essuyer 5 à 15 courses infructueuses par cible [illustratif] demandera réalistement **3 à 6 mois** [illustratif] pour espérer produire **un à trois lemmes techniques véritablement inédits, serrés et utiles** [illustratif] (des bornes précises en échantillon fini sous contraintes structurelles réalistes, non des résultats grandioses).
3. **Part irréductible de chance** : je ne sais pas lesquelles des cinq questions cibles du programme possèdent une forme fermée nouvelle. En mathématiques, qu'un problème minimax admette un multiplicateur dual creux et algébriquement lisible plutôt qu'une frontière combinatoire chaotique dépend d'une propriété structurelle intrinsèque du problème que personne ne choisit à l'avance (`VÉRIFIÉ`). L'organisme peut systématiser l'exploration des petits mondes finis et éliminer les erreurs humaines de calcul, mais que la structure duale cachée s'exprime en une formule intelligible demeure une part de chance mathématique que seule l'exécution du test de mort de M1 révélera.

FIN-DE-CELLULE