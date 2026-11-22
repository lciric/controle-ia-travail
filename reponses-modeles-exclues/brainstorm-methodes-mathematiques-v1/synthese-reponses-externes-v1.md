# Synthèse comparée des réponses d'Argon, de Carbon et d'Astra sur les méthodes de mathématiques nouvelles, confrontées à la réponse de Fable — v1

- **Nature** : pièce de travail (classe C), non contre-lue. Ne lance rien, ne dépense rien, ne demande aucun GO.
- **Écrite par** : un sous-agent (Opus 5.5) de la session mère, le 21 novembre 2026, sur pièces seulement : aucune requête en ligne, aucun appel payant, aucun PDF rouvert. Les chiffres attribués à Fable sont repris de sa réponse, à la page qu'elle cite ; ils sont opposables par sa table de provenance, non par une lecture de ma part.
- **Énoncé commun** : `enonce-methodes-mathematiques-nouvelles-v1.md`, `cb9a14560056ef0c8414d3d02644d2f550ea4901ab13a9513eadb072b89e67f1` ; même empreinte dans les trois fichiers d'appel.
- **Réponse de référence** : `reponse-fable-methodes-v1.md`, `be7f12c9178a79f344355d7404dd50513ca202143b096b626f4d4be9d754cb31` ; tables de provenance des PDF `6dc19d3e…` et des captures `2863b00d…` (empreintes données par Fable).

## Attestation (avant toute synthèse)

Critère : aucune recette d'attaque contre un système réel, aucun mode de sabotage concret applicable. Les trois réponses traitent de mathématiques, de preuve formelle et de statistique ; les passages sur la triche (preuve par hypothèses contradictoires, juges trompés, évaluateurs en virgule flottante exploités) sont des modes d'échec à parer, décrits en termes généraux, non des recettes.

| réponse | fichier | sha256 | modèle servi (demandé) ; coût au prix haut | attestation |
|---|---|---|---|---|
| Argon | `reponse-argon-v1.md` | `192f016882f5d7c2445ea040bf332be16d69ab06c8b84b4e753847086166e61c` | gemini-4-argon (idem) ; 0,5951 USD | attestée : ni recette d'attaque ni mode de sabotage applicable |
| Carbon | `reponse-carbon-v1.md` | `0dfffe4d62c878737de6b55c221a36c84ad9474b41a055be05a89c9ff8f11ef7` | gemini-4-carbon (idem) ; 0,5413 USD | attestée : ni recette d'attaque ni mode de sabotage applicable |
| Astra | `reponse-astra-v1.md` | `ae47cada57d6bc8639bd08f943d23416a0057d60a29454a74ba3f93b63aa06a8` | gpt-6.2-astra (idem) ; 0,5454 USD | attestée : ni recette d'attaque ni mode de sabotage applicable |

Aucune réponse exclue. Coût total des trois appels, au prix haut : 1,6818 USD (somme des champs `cout_usd_prix_haut`).

## Verdict

1. **Les trois modèles ignorent les pièces de 2026 que Fable a lues** (deux tiers des zéros de zêta, explosion forcée de Navier–Stokes annoncée par OpenAI, contre-exemple aux distances unité, lot des 721 manuscrits). Argon contredit frontalement les pièces primaires (« rien d'établi », « faux pour les modèles de langage ») ; Carbon et Astra se taisent ou disent « je ne sais pas ». Sur les annonces, la réponse de Fable prime.
2. **Sur les méthodes, les trois convergent avec Fable** (évaluateur exact en rationnels, témoin fini, certificat, juge formel, nouveauté jugée par un humain du domaine) **et apportent trois choses qu'elle n'a pas** : la réduction, par dualité, d'une garantie universelle à un certificat algébrique fini, derrière un théorème passerelle écrit une fois par un humain (Argon, Carbon) ; la garde de non-vacuité obligatoire (Argon, Carbon) ; des cibles et des témoins plantés précis et justes, dont deux que j'ai vérifiés par calcul (Astra).
3. **Divergences réelles** : le rôle des relecteurs à base de modèles (Argon les supprime, Fable les garde comme filtre affecté à un mode d'échec) ; l'accessibilité de Lean en probabilités à notre budget (Argon et Carbon la disent nulle, les pièces de Fable montrent des formalisations autonomes à quelques centaines de dollars dans les domaines où la bibliothèque est mûre, et Statlib rend celui-ci plus mûr) ; le moment du premier statisticien extérieur (Astra : avant les courses ; Fable : au premier résultat) ; l'optimisme sur la probabilité d'un résultat publiable (Argon, Carbon) contre « aucun taux de base » (Fable, Astra).

---

## 1. Argon

### Ce qu'Argon apporte que Fable n'a pas
- **Le théorème passerelle de dualité faible sur espace fini** : un humain prouve une fois en Lean que tout vecteur de poids rationnels satisfaisant les contraintes marginales borne l'erreur de tout détecteur sur {0,1}^K ; l'agent ne fournit plus qu'un tenseur rationnel, et Lean ne vérifie que des égalités et inégalités linéaires (méthode 1). Fable parle d'évaluateur exact (sa proposition A) et de lemmes de bibliothèque (C), pas de ce pont qui fait d'un témoin numérique un théorème formel.
- **La garde de non-vacuité** : tout énoncé produit est accompagné d'une preuve formelle d'existence d'un objet satisfaisant toutes ses hypothèses (§ 1 point 4, § 4). Fable a les « lemmes d'essai » et le juge standard, pas ce témoin d'existence obligatoire.
- **Synthèse de fonctions de pari polynomiales** pour la détection séquentielle, avec mort en quelques millisecondes par solveur de satisfiabilité modulo théories si la richesse devient négative quelque part, puis mort si le délai de détection ne bat pas la moyenne arithmétique d'e-valeurs ou le test de Page à somme cumulée (méthode 2).
- **Petite taille exacte, puis conjecture, puis certificat en sommes de carrés injecté dans Lean** (méthode 3), avec un critère d'arrêt original : si la hauteur arithmétique des dénominateurs explose entre N = 4 et N = 6, la frontière n'a probablement pas de forme close, on arrête.
- **Données brutes** : banques de lois jointes extrémales en fractions exactes ; chaînes d'inégalités extraites des sources TeX ; journal de mort contenant le message exact du noyau à la ligne qui casse.

### Où Argon contredit Fable
- **Annonces** : voir § 5. Argon tient pour faux ou non établi ce que les pièces primaires de Fable établissent ou annoncent.
- **Lean en probabilités** : « un agent échouera à 100 % sur les coercions de types » ; « la recherche arborescente s'épuisera en quelques minutes ». Les pièces de Fable montrent, en 2026, une boucle simple « modèle général et compilateur » qui refait neuf problèmes d'Erdős (`2605.22763`, p. 2, 11), la formalisation autonome de théorèmes d'articles à 189, 257 et 624 dollars (`2606.05400`, p. 13), 2 problèmes sur 68 avec preuve Lean à 300 dollars (`2609.25050`, p. 1, 6). Fable ajoute la réserve que ces succès sont limités aux domaines où la bibliothèque est mûre (`2605.22763`, p. 11) et propose d'écrire contre Statlib (e-valeurs, identité de Wald, Fano, Bretagnolle–Huber [captures]). La consigne d'Argon d'« éviter à tout prix » la théorie des probabilités de Mathlib ignore Statlib.
- **Juges à base de modèles** : Argon les supprime pour la validité ; seul un exécuteur de code déterministe juge avant Lean. Fable garde des relecteurs à base de modèles, aveugles, affectés chacun à un mode d'échec, comme filtre en amont du juge formel (sa proposition B, d'après `2608.13637`, p. 18). Divergence de dessin, non de principe : ni l'un ni l'autre ne confie la vérité à un modèle.
- **Probabilité de succès** : « chance élevée de découvrir une borne analytique inédite et publiable » si la frontière extrémale est régulière. Fable : « incertaine ; aucun taux de base n'existe pour notre domaine ».
- **Ce qui distingue ses méthodes** : Argon affirme que « la littérature utilise des familles de paris standard » ; zone vierge séduisante non vérifiée (R8). Fable range la même idée en question, dans une zone très occupée.

### Références citées par Argon
| référence (titre ; identifiant) | statut |
|---|---|
| *Mathematical discoveries from program search with large language models* (FunSearch) ; Nature 625 | dans les tables (`romera-paredes-2024-nature-625-funsearch.pdf`) ; l'identifiant arXiv 2312.02475 donné par Argon : **non vérifié** |
| *PatternBoost: Constructions in Mathematics with a Little Help from AI* ; arXiv 2411.00566 | dans les tables |
| AlphaGeometry (Trinh et al., Nature 2024) | **non vérifié** |
| AlphaProof (DeepMind 2024, « pas de publication arXiv ») | dans les tables sous Hubert et al., Nature 2025 |
| *Constructions in combinatorics via neural networks* ; arXiv 2104.14516 | dans les tables |
| *Draft, Sketch, and Prove* ; arXiv 2210.12283 | dans les tables |
| *LEGO-Prover: Neural Theorem Proving with Growing Libraries* (identifiant « pas sûr ») | dans les tables (arXiv 2310.00656) |
| *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models* ; arXiv 2306.15626 | **non vérifié** |
| DeepSeek-Prover-V1.5 (Xin et al. 2024) | **non vérifié** |
| *The Ramanujan Machine* (Nature 2021) | dans les tables (arXiv 1907.00205 v4 ; la version Nature non) |
| QuickSpec (Claessen et al.) | **non vérifié** |
| Yongji Wang et al., Physical Review Letters (profils d'explosion) | **non vérifié** |
| Chen et Hou, explosion d'Euler 3D avec bord ; arXiv 2210.07191 | **non vérifié** |
| outils : Pantograph, lean4export, Lean4Checker, nanoda, LeanSearch, Moogle, Duper, Lean-auto | **non vérifiés** (le juge standard, Comparator, est dans les tables) |
| auteurs de fond sans titre (Shafer, Vovk, Ramdas, Tsybakov, Wu, Embrechts, Puccetti) | **non vérifiés** |

Chiffres **à vérifier** (aucun PDF) : AlphaProof « jours-machines de processeurs spécialisés (TPU) par problème » (Fable, `hubert-2025`, p. 5 : deux à trois jours d'apprentissage au moment de l'épreuve, ordre compatible) ; Wagner « une demi-douzaine de conjectures réfutées » ; « 200 lignes de lemmes » ; « 150 lignes » de pont ; « 3 à 6 semaines » et « 80 % du succès » humains ; tous ses coûts (30–80, 100–200, 50–150 USD), qui sont des propositions non chiffrées sur pièce.

---

## 2. Carbon

### Ce que Carbon apporte que Fable n'a pas
- **Le dictionnaire de traduction et la recherche d'antériorité « déshabillée »** : chaque cible réécrite sans les mots « IA, moniteur, agent, contrôle », puis cherchée dans quatre littératures, dont deux absentes des zones de Fable (D-B4) : l'agrégation de risques sous dépendance inconnue (actuariat, *joint mixability*) et la détection décentralisée à capteurs corrélés (traitement du signal). C'est l'apport le plus utile à la veille si son gel est levé.
- **Trois théorèmes passerelles** prouvés une fois par un humain : Le Cam sur type fini, dualité faible d'agrégation, inégalité de Ville par récurrence sur un arbre fini d'horizon T. Même idée qu'Argon, plus complète ; la troisième remplace les filtrations infinies.
- **La réduction aux mesures discrètes** (théorème de Richter–Rogosinski, ou de Tchakaloff : un problème linéaire sous m contraintes d'espérance atteint son extremum sur une mesure à au plus m + 1 atomes ; énoncé **à vérifier**). Elle justifie le passage au fini, que Fable pose sans justification.
- **La séparation des deux architectures** : impossibilité = existence d'un témoin (recherche) ; garantie = universel, donc synthèse d'un certificat dual. Fable a « les deux sens », pas cette séparation des pipelines.
- **« Réfuter d'abord »** : aucun sous-lemme n'entre dans Lean avant d'avoir survécu à une recherche adverse (5 000 départs de descente de gradient projetée sur le simplexe) d'une loi du nul qui le viole ; règle d'arrêt si plus de 20 % des survivants s'avèrent faux en Lean. Fable a la recherche adverse d'une violation du lemme clé (proposition D), pas cette porte systématique ni son seuil.
- **Le test qui demande si un théorème est nécessaire** : si un moniteur qui résout en ligne, à chaque pas, le point-selle minimax bat toutes les formes closes trouvées, abandonner la recherche de formes closes et embarquer le solveur sous l'inégalité de Ville.
- **Recherche évolutive de mélanges d'Ingster** pour des bornes d'impossibilité à plusieurs détecteurs, avec un monde caché de parité comme épreuve de mort (méthode B), et le filtre « dalmatien » de Graffiti (ne garder qu'une conjecture qui bat strictement les bornes connues sur au moins un cas).
- **Trois bases canoniques pour l'utilité**, sur traces tenues hors de la boucle : moyenne arithmétique d'e-valeurs, Shiryaev–Roberts ou test de Page à somme cumulée, borne de Bretagnolle–Huber à deux points.
- **Épreuve de mort par redécouverte aveugle** de trois connus (moyenne de Vovk–Wang, facteur deux fois la moyenne des p-valeurs de Rüschendorf pour deux p-valeurs, Chebyshev–Olkin–Pratt bivariée) sous 100 USD : rejoint la banque de connus plantés de Fable, avec des cibles nommées.

### Où Carbon contredit Fable
- **Dépôt `TestingLowerBounds`** recommandé comme donnée de départ. La capture versée par Fable (`testing-lower-bounds-README.md`, `76f6f461…`) dit : « This repository is no longer maintained. Its code has been migrated to Statlib ». Carbon est dépassé ; la recommandation de Fable (Statlib, D-B3) tient.
- **Ville dans Mathlib** : Carbon place « l'inégalité maximale de Ville/Doob » dans `Mathlib.Probability.Martingale`. Fable : Doob et l'arrêt optionnel y sont, aucun module nommé pour Ville (recherche par noms sur la branche principale, à refaire sur la version épinglée).
- **Vérificateur** : `lean4checker` et `SafeVerify` (non vérifiés) là où Fable prend Comparator, intégré au cœur de Lean depuis la version 4.35.0 selon sa notice [capture `leanprover-comparator-README.md`, ligne 3]. Pas une contradiction de principe ; l'outil standard est celui de Fable.
- **Lean en probabilités** : « engloutira 90 % de votre budget » ; même objection qu'à Argon.
- **Optimisme** : « chance sérieuse » d'un à trois résultats publiables en trois à six mois. Fable : aucun taux de base ; repère mesuré le plus proche, 2 problèmes sur 68 à 300 dollars (`2609.25050`, p. 1, 6), sur un autre domaine.
- **Effort humain** : « 1 à 2 mois à plein temps » avant toute course productive, contre « des heures à quelques jours » par évaluateur chez Fable. Deux estimations sans source.

### Références citées par Carbon
| référence | statut |
|---|---|
| *AlphaEvolve* (Novikov et al., 2025, « arXiv pas sûr ») | dans les tables (arXiv 2506.13131) |
| FunSearch (Nature 2024) | dans les tables |
| Wagner, *Constructions in combinatorics via neural networks* | dans les tables (2104.14516) |
| PatternBoost (Charton, Ellenberg, Williamson, Wagner 2024) | dans les tables (2411.00566) |
| Graffiti (Fajtlowicz, Discrete Mathematics 1988) | **non vérifié** |
| Davies et al., *Advancing mathematics by guiding human intuition with AI*, Nature 2021 | dans les tables (Nature 600) |
| LeanDojo / ReProver (NeurIPS 2023) | **non vérifié** |
| DeepSeek-Prover-V1.5 et V2 | **non vérifié** |
| AlphaProof | dans les tables |
| *Draft, Sketch, and Prove* (ICLR 2023) | dans les tables (2210.12283) |
| LEGO-Prover (ICLR 2024) | dans les tables (2310.00656) |
| Vovk et Wang (Biometrika 2020 ; Annals of Statistics 2021) | **non vérifié** |
| Rüschendorf 1982 ; Puccetti et Wang 2015 | **non vérifié** |
| Tsitsiklis et Athans (IEEE Transactions on Automatic Control 1985) | **non vérifié** |
| Lorden 1971 ; Pollak 1985 ; Moustakides 1986 ; Shiryaev–Roberts ; Ville 1939 | **non vérifiés** |
| Grünwald, de Heide et Koolen (Journal of the Royal Statistical Society B, 2024) | **non vérifié** |
| Richter–Rogosinski, Tchakaloff ; Chebyshev–Olkin–Pratt ; Ingster | **non vérifiés** |
| dépôt `TestingLowerBounds` (Degenne) | dans les tables (README : migré vers Statlib) |
| dépôt `PFR` | **non vérifié** |
| `Mathlib.Probability.Martingale` | dans les tables (capture `OptionalStopping.lean`) |
| `lean4checker`, `SafeVerify` | **non vérifiés** |
| Wang, Lai, Gómez-Serrano, Buckmaster (Physical Review Letters 2023) ; prépublications avec DeepMind 2025 | **non vérifié** |
| Chen et Hou (Euler 3D avec bord) | **non vérifié** |
| documentation de Bloom et Tao sur les problèmes d'Erdős | **non vérifié** (le même fait est chez Fable par `2511.16072`, p. 25 et 54) |

Chiffres **à vérifier** : profil numérique « à résidu 10⁻¹³ » ; AlphaEvolve « nombre de contact en dimension 11 » et « recouvrement minimal d'Erdős » (Fable ne cite en dimension 11 que les 604 sphères de la Station, `2608.23691`, p. 1-2) ; Tsitsiklis–Athans « NP-difficile même pour deux capteurs » ; « 90 % du budget », « 70 % du succès », « 95 % éliminées », « 20 % » ; tous ses coûts. Concordant avec les pages lues par Fable : AlphaEvolve sur plus de 50 problèmes, environ 20 % d'améliorations, produit 4 × 4 complexe en 48 multiplications (`2506.13131`, p. 1, 3, 10).

---

## 3. Astra

### Ce qu'Astra apporte que Fable n'a pas
- **Partir d'une décision** : un statisticien extérieur et un utilisateur du moniteur choisissent avant toute course une décision qu'un théorème pourrait changer, fixent le modèle d'observation, les dépendances permises, le risque, et la meilleure borne déjà connue ; puis on tente la réduction à un connu **sans modèle de langage**. Fable a l'utilité comme « décision de dessin changée », mais en sortie, pas en entrée.
- **Une base sans proposeur** : comparer l'organisme à la même recherche exacte sans proposeur à base de modèle. La « voie nue » de Fable (N-045) reste une boucle de modèle ; celle d'Astra n'en a pas.
- **Un témoin planté juste pour l'agrégation** : avec les seules marges Pr₀(Xᵢ = 1) = p, sup Pr₀(S ≥ k) = min(1, mp/k). **Vérifié ici par calcul** : Markov donne le majorant ; si mp ≤ k, une k-partie uniforme avec probabilité mp/k donne des marges (mp/k)(k/m) = p ; si mp > k, le mélange d'une k-partie uniforme (poids 1 − λ) et de l'ensemble plein (poids λ = (p − k/m)/(1 − k/m), dans [0, 1] pour k < m) donne des marges p et Pr(S ≥ k) = 1.
- **Une cible séquentielle neuve pour nous : les observations qui se chevauchent.** Si la calibration n'est garantie que conditionnellement à un instant d'émission antérieur à la révélation précédente, l'inégalité de Ville ne s'applique plus au produit. Témoin planté, **vérifié ici** : deux scores valant tous deux 2Z, Z pièce équitable dans {0, 1} ; chacun a moyenne 1 ; le produit vaut 4Z, de moyenne 2. Cette faille vise directement des moniteurs à étiquettes retardées. Base à battre : Henzi–Ziegel (non vérifié).
- **Une cible d'impossibilité sur l'audit** : quand l'audit ciblé sur le premier score a-t-il une valeur minimax strictement positive sur l'audit aléatoire, à budget moyen et fausse alerte égaux sous les deux hypothèses ; confronter à Huber–Strassen et à la comparaison d'expériences de Blackwell ; mort si le gain vient d'un budget inégal ou d'un usage de la seconde mesure avant son achat.
- **La paire construction–obstruction** : une loi qui atteint la borne et un certificat dual qui la majore, revérifiés par un petit vérificateur rationnel indépendant du solveur, certifient l'instance avant même que Lean soit prêt.
- **Une phrase de prudence à reprendre** : une borne à horizon fini ne sera pas annoncée comme valable à tout temps d'arrêt.

### Où Astra contredit Fable
- **Moment du statisticien extérieur** : Astra le veut avant les courses (hypothèses) et après (antériorité). Fable recommande (a) des noms et un brouillon prêts, envoi au premier résultat, et (b) un contact dès maintenant seulement si Lazar connaît quelqu'un (D-B6). Astra défend l'option (b) de Fable. Contact externe : nœud dans les deux cas.
- **Annonces** : pas de contradiction ; Astra dit « je ne sais pas » et refuse les totaux de communiqué, comme Fable. Il ignore les pièces de 2026 sauf Aletheia.
- Sur `formal-conjectures`, concordant avec la capture versée : des énoncés, pas des preuves.

### Références citées par Astra
| référence | statut |
|---|---|
| énoncé de l'Institut Clay | **non vérifié** (lu par Fable par un outil de résumé, non opposable) |
| Platt et Trudgian, *The Riemann hypothesis is true up to 3·10¹²* | **non vérifié** |
| *Discovery of Unstable Singularities* | **non vérifié** |
| erdosproblems.com | **non vérifié** (non capturé) |
| *Towards Autonomous Mathematics Research* (agent Aletheia) | dans les tables (arXiv 2602.10177, p. 1-2) |
| *Mathematical discoveries from program search with large language models* | dans les tables |
| *AlphaEvolve: A coding agent for scientific and algorithmic discovery* ; arXiv 2506.13131 | dans les tables |
| Wagner ; Davies et al. | dans les tables |
| *Autoformalization with Large Language Models* ; arXiv 2205.12615 | dans les tables |
| *Draft, Sketch, and Prove* ; arXiv 2210.12283 | dans les tables |
| *LeanDojo* ; arXiv 2306.15626 | **non vérifié** |
| *DeepSeek-Prover-V2* ; arXiv 2504.21801 | **non vérifié** |
| `leanprover-community/mathlib4` ; `google-deepmind/formal-conjectures` | dans les tables (captures) |
| bornes de Hailperin ; tests minimax de Huber–Strassen ; comparaison d'expériences de Blackwell | **non vérifiés** |
| Henzi et Ziegel, *Valid sequential inference on probability forecast performance* | **non vérifié** |

Chiffres **à vérifier** : la hauteur 3·10¹² de Platt et Trudgian. Les deux identités mathématiques d'Astra sont vérifiées par calcul ci-dessus et n'ont pas besoin de PDF.

---

## 4. Trois idées de méthode les plus solides, tous modèles confondus

**1. La paire construction–obstruction sur l'agrégation de détecteurs sous dépendance partiellement contrainte** (Fable A, Argon méthode 1, Carbon méthode A, Astra course A).
- *Premier pas sans dépense* : un évaluateur exact en rationnels (programme linéaire sur les lois jointes de deux à quatre détecteurs binaires) et, à part, un vérificateur de vingt lignes qui revérifie loi primale et certificat dual ; table d'admission par témoins : retrouver sup Pr₀(S ≥ k) = min(1, mp/k) (vérifié ici), le facteur deux de Rüschendorf pour deux p-valeurs et la moyenne de Vovk–Wang (ces deux derniers à vérifier sur PDF avant d'en faire des témoins) ; faire mourir le minimum non corrigé.
- *Test qui la tue* : l'évaluateur laisse vivre un témoin faux ou rate un connu planté ; la loi conjecturée manque une taille ou un paramètre tenus à l'écart ; le support dual se fragmente quand la grille s'affine (pas de forme close) ; une spécialisation publiée (bornes de Hailperin, agrégation de risques) donne déjà la formule ; la même recherche sans proposeur à base de modèle trouve la même formule à coût moindre.

**2. « Réfuter d'abord » pour les processus de test séquentiels sur arbres finis, chevauchement des observations compris** (Carbon méthode C, Astra course B, Argon méthode 2).
- *Premier pas sans dépense* : sur un arbre fini de scores à deux valeurs, un programme linéaire exact qui maximise la probabilité que le produit franchisse 1/α avant l'horizon sous les contraintes de calibration, pour un calendrier d'émission donné ; le témoin planté 2Z (vérifié ici) doit être retrouvé comme violation ; un falsificateur adverse sur le simplexe doit retrouver la violation plantée.
- *Test qui la tue* : le falsificateur manque la violation plantée ; plus de 20 % des candidats qui lui survivent s'avèrent faux ensuite ; une borne existante (séparation en sous-suites, Henzi–Ziegel) est déjà exacte ; un moniteur qui résout numériquement le point-selle à chaque pas bat toute forme close trouvée (alors aucun théorème neuf n'est utile, seul le solveur l'est).

**3. Le pont formel écrit une fois, la garde de non-vacuité, le juge standard** (Argon, Carbon ; Fable C pour le juge et Statlib).
- *Premier pas sans dépense* : sur la version épinglée de Mathlib et de Statlib, relever par lecture ce qui existe pour la dualité faible sur type fini et pour Ville sur arbre fini ; écrire comme fichiers de défi, sans définition maison, l'énoncé du pont et son théorème d'existence d'un objet qui satisfait toutes les hypothèses ; vérifier que la commande du juge standard existe à cette version (déjà la décision D-B2 par défaut).
- *Test qui la tue* : un énoncé planté à hypothèses contradictoires passe la garde ; le pont ne s'écrit pas sans définition maison ; la preuve du pont ne se ferme pas dans l'outillage déjà accordé ; le pont est déjà dans Statlib (alors on le réemploie : « non neuf », par choix).

Réserve (R4) : la convergence des quatre modèles sur ces trois idées est un a priori partagé, non une preuve de fécondité ; aucune n'a de taux de base dans notre domaine.

## 5. Affirmations publiques où un modèle externe dit autre chose que les pièces primaires lues par Fable

| sujet | ce que dit le modèle externe | ce que disent les pièces lues par Fable |
|---|---|---|
| Riemann | **Argon** : aucune avancée vérifiée produite par une IA ; les annonces sont des hallucinations ou des approximations numériques. **Carbon**, **Astra** : hypothèse non résolue, rien d'autre (Astra cite Platt–Trudgian, non vérifié). | Hypothèse non résolue (accord). Mais : au moins deux tiers des zéros simples et sur la droite critique, argument « découvert et écrit par Claude », vérifié par les signataires, lu par deux spécialistes, formalisé en Lean (`2608.13637`, p. 1, 15, 19), réexposé (`2610.24612`, p. 1) et redémontré autrement (`2609.02882`, p. 1). Quasi-hypothèse 7/8 d’OpenAI : annoncée, non établie. Argon est contredit. |
| Navier–Stokes | **Les trois** : le problème du millénaire n'est pas résolu ; seuls existent des profils numériques d'explosion (réseaux informés par la physique) et la preuve de Chen et Hou pour Euler avec bord, sans modèle de langage. Carbon définit le problème comme la seule question sans force. | OpenAI, 8 septembre 2026 : explosion en temps fini pour une force lisse à support compact, « établit l'alternative (C) » de l'énoncé officiel, et (D) (p. 1, 166 pages), formalisée en Lean ; **contestée** : la voie n'atteint pas le problème sans force (`2609.20803`, p. 1-2), la formalisation n'est pas la preuve écrite (`2610.08144`, p. 2, 4). Explosion d'Euler forcé et de deux équations voisines par deux analystes aidés de modèles (déclaration de Buckmaster, p. 1). Les trois modèles ignorent ces pièces ; « non établi » reste juste, la raison donnée est périmée. |
| Problèmes ouverts « résolus par dizaines » | **Argon** : faux pour les modèles de langage ; seuls FunSearch, AlphaGeometry, AlphaProof et Wagner. **Carbon** : AlphaEvolve améliore environ 20 % de plus de 50 problèmes de construction (concordant) ; pour Erdős, majorité de redécouvertes bibliographiques, très peu de résolutions authentiques (concordant pour octobre 2025 ; attribution à Bloom et Tao non vérifiée). **Astra** : je ne sais pas, unité d'audit = le numéro du problème. | Contre-exemple aux distances unité d'Erdős par un modèle d'OpenAI, digéré par neuf mathématiciens (`2605.20695`, p. 1) ; un problème ouvert résolu avec l'aide de GPT-5 (`2511.16072`, p. 54) ; 721 manuscrits d'octobre 2026, 42 % formalisés, trois retirés le lendemain, aucun relu par les pairs à la mi-octobre (captures, `2610.17090`, p. 3) ; 2 sur 68 à 300 dollars (`2609.25050`) ; 9 sur 353 (`2605.22763`). Argon est contredit ; Carbon et Astra sont incomplets, non contraires. |
| AlphaProof | **Argon** : « pas de publication arXiv » (laisse entendre aucune publication). | Publié dans Nature en 2025 (Hubert et al., dans les tables). |

## 6. Ce que je n'ai pas vérifié
- Aucun PDF rouvert ; les pages citées pour Fable sont les siennes. Aucune des références « non vérifiées » n'a été cherchée (pas de requête en ligne).
- Quatre captures seulement ouvertes et leur empreinte recalculée, conforme à la table : `testing-lower-bounds-README.md`, `statlib-README.md`, `formal-conjectures-README.md`, `leanprover-comparator-README.md`.
- Les deux identités d'Astra sont vérifiées à la main, non par programme.
