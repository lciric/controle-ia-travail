# Contre-lecture du rapport d'antériorité « T » — lot 8 — v1

- Date : 2026-11-13 ; début de la contre-lecture 22:48:53 UTC, fin de rédaction 22:56:54 UTC (heures relevées par `date -u`).
- Contre-lecteur : sous-agent neuf, modèle B ; auteur du rapport : modèle A ; A ≠ B. Je n'ai écrit ni le programme, ni les décisions, ni le rapport contre-lu.
- Objet : `docs/sources/lecture-pdf-niveau3/compte-2/rapport-T-lot8-v1.md` et son archive.

## Empreintes vérifiées (toutes concordantes)

| fichier | empreinte sha256 |
|---|---|
| `rapport-T-lot8-v1.md` | `443a83f971e691af1c64c7aa49490398c1badffb5e9986a226e05f60719feedf` (égale à l'attendue) |
| `fichiers-de-travail-T-lot8-v1.tar` | `a1d6d7a4ec39effa1b4dee3bbc3743132f8642a817cfcfbbe095afdc11eb66a9` (égale à l'attendue) |
| `2310.01153v5.pdf` (Koning, 45 pages) | `e8cd3532247d69817c47ecf7773c1da5318e87404b9e29d3d95f6fef69ab0544` (égale au compagnon `.sha256`) |
| `2102.00630v4.pdf` (Ramdas, Ruf, Larsson, Koolen, 34 pages) | `2ada73f4abaf779b06baa558f49893678feec1d5b1451e083e842dd14117fd57` (égale au compagnon) |
| `1906.09256v3.pdf` (Vovk, 34 pages) | `0a9a1f2c7e96107f4f573e9aa3dd8f1d79798b84cbbd9923bd3db2ecb81efbe3` (égale au compagnon) |

## Fichiers lus (liste exacte) et étendue

1. `docs/sources/lecture-pdf-niveau3/compte-2/rapport-T-lot8-v1.md`, en entier.
2. `docs/sources/lecture-pdf-niveau3/compte-2/fichiers-de-travail-T-lot8-v1.tar`, extraite dans mon dossier de travail : `journal-T-v1.txt` et `verifier_citations_v1.py` lus en entier ; `citations-T-v1.json` rejoué par mon script (non lu à l'œil) ; les autres fichiers de l'archive non ouverts.
3. `docs/decisions/decision-N-003-N-004-v1.md`, lignes 17 à 52.
4. `docs/notes/note-mathematique-lemme-theoreme-v2.md`, lignes 1 à 55 et 86 à 131.
5. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, lignes 154 à 171.
6. `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-contre-lecture-v1.md`, lignes 368 à 407.
7. La consigne commune `…/scratchpad/pieces-10016a61/docs/sources/lecture-pdf-niveau3/consignes-v1/consigne-commune-lecture-v1.md`, en entier.
8. Les trois PDF et leurs trois compagnons `.sha256` (le dossier du lot a été listé par `ls`, sans ouvrir aucune autre pièce). Étendue lue, sur le texte extrait page à page par `pdftotext -layout` :
   - Koning : pages 1 à 45 en entier, corps, annexes 8 à 13, preuves (section 12) et tableaux ; la liste des références (p. 27-29) lue en entier.
   - Ramdas et collègues : pages 1 à 27 et 31 à 34 en entier (corps, annexes A et B, preuves) ; la liste des références (p. 28-31) parcourue seulement par recherche de noms et de numéros.
   - Vovk : pages 1 à 27 et 31 à 34 en entier (corps, annexes A et B) ; la liste des références (p. 27-31) lue en partie, le reste par recherche de noms et de numéros.
   - Les figures n'ont été lues que par leurs légendes ; aucune valeur n'a été relevée sur un graphique.

Rien d'autre n'a été ouvert. Aucune ouverture fautive. Aucun refus d'un contrôle de permissions, d'un crochet ou d'un classifieur. Aucune commande git, aucun appel réseau, aucun appel de modèle.

## Contrôle des citations

- Script `verifier_citations_contre_lecture_v1.py` (écrit par moi, lancé par `python3 -I`) : empreinte du PDF, extraction de la page par `pdftotext` avec et sans `-layout`, normalisation (Unicode, ligatures, apostrophes, guillemets, tirets, césures, espaces), recherche de la citation.
- Essais préalables : un cas juste (réussite) ; trois cas altérés — mot changé, page fausse, empreinte fausse — (trois échecs, attendus).
- **Citations de cette contre-lecture contrôlées : 41. Échecs : 0.** Liste : `citations-contre-lecture-T-v1.json`. Toute citation anglaise entre guillemets anglais doubles ci-dessous y figure mot pour mot. Les formules sont décrites en français et marquées « lu sur le PDF, non contrôlé par programme ».
- Rejeu indépendant des 72 citations du lecteur avec mon script : 72 contrôlées, 0 échec. Ses citations existent donc bien aux pages dites ; les constats ci-dessous portent sur ce qu'on leur fait dire et sur ce qui manque.

---

## 0. Verdict d'abord

- **Sur le rapport : « tient avec corrections ».** Le verdict d'ensemble (« occupé en partie ») est juste, l'exposé du théorème d'impossibilité de Ramdas et collègues est exact, et aucune composante dite « non trouvée » n'est contredite par un théorème, une proposition ou un corollaire des trois pièces. Mais la description de l'occupation de l'unification est mal répartie (un sous-groupe déclaré « non fait » est écrit, l'autre est dit « exactement » fait alors qu'il est déduit), et la remarque de Koning la plus proche du volet « le groupe compte » n'est pas relevée. Trois constats majeurs, aucun bloquant.
- **Mon verdict sur T, table fermée : « occupé en partie ».**
- **Profondeur de lecture : suffisante pour le verdict, insuffisante sur la section 6 de Koning** (p. 20-24) et sur une ligne de la page 9. Détail en section 4.

---

## 1. Constats

### A — majeur — le sous-groupe « agents à l'intérieur de chaque pas » est écrit chez Koning, au nom près ; le rapport le dit « non fait »

- Pages : Koning p. 21 (exemple 10), p. 22, p. 23 (exemple 13), p. 23-24 (simulation 7.1), p. 35 (exemple 14).
- Ce que portent les pages. L'exemple 10 pose des lots qui arrivent l'un après l'autre : “Suppose we sequentially observe potentially unequally sized batches of data” (p. 21), et prend pour groupe le produit des groupes de permutations de chaque lot (formule lue sur le PDF, non contrôlée par programme : G_n = P_0 × P_1 × … × P_n), “where Pi is the group of permutations acting on the batch Yi” (p. 21). La page 22 précise : “we exclude permutations that swap observations across batches” et “Specifically, the groups we consider here are subgroups of the permutations on the set of the individual observations.” La simulation 7.1 donne au lot le sens d'un pas de temps et à ses éléments le sens d'unités : “In each interval of time, we receive the outcomes of a number of treated and control units” (p. 23) ; “As a batch of data, we consider the combined observations of both the treated and control units that arrived in the previous interval of time.” (p. 24).
- Lecture. Un lot par intervalle de temps, des unités à l'intérieur du lot, des permutations à l'intérieur de chaque lot et aucune d'un lot à l'autre, des lots de tailles inégales : c'est, au nom des unités près, le groupe « permutations des agents à l'intérieur de chaque pas » de N-003, écrit comme groupe produit et comme sous-groupe des permutations de toutes les observations. L'exemple 14 (p. 35) écrit le même groupe produit pour des blocs de temps consécutifs d'une seule suite : “where Pi permutes the observations within the ith batch of data”.
- Ce que le rapport dit (section 0, point 1, et section 2.3) : « Non fait : […] le second sous-groupe (permutations des agents à l'intérieur de chaque pas) ». C'est une occupation sous-estimée, et l'attribution est inversée : c'est ce sous-groupe-là qui est le plus près d'être imprimé, pas celui « du temps à l'intérieur de chaque agent » (constat B).
- Ce qui reste réellement non écrit chez Koning : un tableau à deux indices (agent, pas) où la même unité revient d'un lot à l'autre ; les deux partitions du même ensemble d'indices (par agent, par pas) considérées ensemble ; la phrase « le temps et les agents sont deux sous-groupes du même objet » ; l'usage négatif face à un attaquant.
- Réponse à la question du mandat : Koning écrit des **groupes produits** (p. 21, 23, 35) ; il écrit des permutations **à l'intérieur de chaque pas** au sens « à l'intérieur de chaque lot arrivé dans un intervalle de temps » (p. 21, 23-24) ; il n'écrit **pas** de tableau à deux indices.
- Texte corrigé proposé (section 0, point 1 du rapport) :

```text
1. **Unification temps × agents — occupée en partie par Koning (2310.01153v5).** Le cadre général est écrit :
   invariance sous un groupe compact quelconque (p. 1, 2), sous un sous-groupe (p. 13, remarque 6), et sous le
   **groupe produit des permutations à l'intérieur de lots arrivant l'un après l'autre**, présenté comme sous-groupe
   des permutations de l'ensemble des observations individuelles, plus faible que l'échangeabilité pleine (p. 21-23,
   exemples 10 et 13 ; p. 35, exemple 14). Dans la simulation 7.1 (p. 23-24) le lot est un intervalle de temps et ses
   éléments sont des unités : c'est, au nom près, le sous-groupe « agents à l'intérieur de chaque pas ». Le sous-groupe
   « temps à l'intérieur de chaque agent » est une autre instance du même exemple 10 (un lot par agent) ; Koning ne
   l'écrit pas comme groupe : dans l'application au « hot hand » il multiplie des e-valeurs calculées joueur par joueur
   en invoquant leur indépendance (p. 5, 26). **Non fait** : le tableau à deux indices I ⊂ {1..N} × {1..T}, les deux
   partitions (par agent, par pas) du même ensemble d'indices prises ensemble, l'affirmation que le temps et les
   agents sont deux sous-groupes d'un même objet, et l'usage de ce cadre pour un énoncé négatif face à un attaquant.
```

- Ligne de la table (section 5) à corriger dans le même sens : « cadre général, groupe produit par lots, lots indexés par le temps (p. 13, 21-24, 35) faits ; produit par joueur justifié par l'indépendance, non par un groupe (p. 5, 26) ; deux axes, deux partitions ensemble, usage négatif non faits ».

### B — majeur — « c'est exactement le sous-groupe permutations du temps à l'intérieur de chaque agent » : trop fort, non porté par la page

- Pages : Koning p. 5, p. 26.
- Ce que porte la page 26 : “the product of independent e-values is also an e-value”, appliqué à des données “with 26 shooters taking up to 100 shots each”. La justification imprimée du produit est l'**indépendance** des e-valeurs entre tireurs. Aucun groupe n'est posé sur l'ensemble (tireur, tir) ; aucun groupe produit n'est nommé à cet endroit ; les suites sont de longueurs inégales.
- Lecture. Qu'un produit d'e-valeurs d'échangeabilité calculées tireur par tireur soit valide sous l'invariance par le groupe produit est vrai (sachant l'orbite, la loi invariante est le produit des lois uniformes sur les orbites de chaque tireur, donc l'espérance du produit vaut un) : c'est un **calcul du contre-lecteur**, pas un énoncé de la pièce. Le rapport écrit « c'est exactement le sous-groupe […], sans qu'il soit nommé ainsi » (section 0, point 1) et « qui revient au sous-groupe » (section 2.3) sans marquer la déduction.
- Texte corrigé proposé (section 2.3, phrase sur la fusion) :

```text
fusion par produit d'e-valeurs calculées par joueur (p. 5, 26), justifiée dans la pièce par l'indépendance des
e-valeurs et non par un groupe ; qu'elle revienne à tester l'invariance sous le groupe produit « temps à l'intérieur
de chaque agent » est une déduction du lecteur (calcul, non imprimé).
```

### C — majeur — « le groupe compte » : la remarque la plus proche n'est pas relevée

- Pages : Koning p. 23 (remarque 12, exemple 12), p. 37 (exemple 18), p. 13 (remarque 6).
- Ce que porte la page 23. Remarque 12 : en passant du groupe à un sous-groupe moins riche, “we are testing a larger hypothesis than” l'invariance sous le groupe d'origine, et “This shows where the test martingale loses power compared to an e-process.” L'exemple 12 en est le cas extrême (lu sur le PDF) : le sous-groupe stabilisateur se réduit à l'identité, d'où l'impossibilité d'une martingale de test dans la filtration des données. L'exemple 18 (p. 37) exhibe une loi invariante sous des permutations par blocs seulement : “Here, the resulting order of the numbers is not invariant under all permutations”, “only the 8 orders 1234, 1243, 2134, 2143, 3412, 3421, 4312 and 4321 can occur”.
- Lecture. « Groupe plus petit, hypothèse plus large, puissance perdue » est le même fait de treillis que « une loi invariante seulement sous un sous-groupe laisse détecter un rebrassage plus large », vu du côté du testeur et non de l'attaquant. Le rapport classe ce volet « voisin (p. 13, 22-23) » sans nommer la remarque 12, et ne cite l'exemple 18 que pour T1.
- Classement : je garde « voisin » (l'énoncé du programme porte sur la loi honnête et sur le choix du groupe par l'attaquant, avec un exemple chiffré ; rien de cela n'est imprimé), mais la moitié qualitative est imprimée et doit être citée.
- Texte corrigé proposé (section 2.3, fin du paragraphe T2) :

```text
« Le groupe compte » : voisin proche. Le fait qualitatif est imprimé du côté du testeur : tester l'invariance sous
un sous-groupe moins riche, c'est tester une hypothèse plus large et perdre de la puissance (remarque 12, p. 23 ;
cas extrême de l'exemple 12, p. 23, où le sous-groupe se réduit à l'identité) ; l'invariance par lots est plus faible
que l'échangeabilité (p. 22) ; le choix du sous-groupe change la puissance (p. 13) ; l'exemple 18 (p. 37) exhibe
une loi invariante sous des permutations par blocs seulement. Non écrit : la lecture du côté de l'attaquant (une loi
honnête invariante seulement sous un sous-groupe laisse détecter un rebrassage plus large) et l'exemple chiffré à
trois agents.
```

- Et, dans la formulation « reste revendicable » (section 7, point b) : remplacer « et sa version par sous-groupe chiffrée sur un exemple (le groupe compte) » par « et sa version par sous-groupe lue du côté de l'attaquant, chiffrée sur un exemple, le fait qualitatif — sous-groupe plus petit, hypothèse plus large, puissance perdue — étant imprimé chez Koning (p. 23) ».

### D — mineur — noyau de T2 : l'occupation est juste, les briques citées ne sont pas les bonnes

- Pages : Koning p. 8 (lemme 1), p. 9, p. 11, p. 39.
- Réponse à la question du mandat. L'identité du **rebrassage seul** est imprimée : le lemme 1, “Y is an invariant random variable under a compact group G if one of the following equivalent conditions holds” (p. 8), a pour condition 3 l'égalité en loi de la variable et de sa transformée par un élément uniforme indépendant du groupe (lu sur le PDF, non contrôlé par programme) ; la section 2.5 l'écrit pour une loi quelconque, “We can also express this in terms of random variables” (p. 9), la transformée ayant la loi moyennée sur le groupe. La **composition** avec un réarrangement π_Y qui dépend des données n'est imprimée nulle part : elle est seulement déductible, en deux lignes.
- La déduction du rapport est correcte, mais elle s'appuie sur « conditions 3-4 du lemme 1 », qui supposent la variable invariante, alors que π_Y(Y) ne l'est pas a priori. Les briques qui portent réellement le pas sont : (i) pour un point fixé, l'image par un élément uniforme du groupe est uniforme sur l'orbite — “Moreover, recall that Gy ∼ Unif(Oy), for fixed y.” (p. 39 ; aussi p. 11, lu sur le PDF, à côté de la phrase “In particular, we may view the problem of testing group invariance as first observing the orbit”) ; (ii) l'absorption de la mesure de Haar, “which follows from Lemma 1 by considering the invariant random variable” Y = G et “the fact that the Haar measure on a compact group is both left- and right-invariant” (p. 9), non citée par le rapport ; (iii) la condition 5 du lemme 1 (p. 8).
- Texte corrigé proposé (section 2.3, parenthèse du raisonnement) :

```text
(pour un point fixé, son image par un élément uniforme du groupe est uniforme sur son orbite, p. 11 et p. 39 ;
la mesure de Haar absorbe la composition à gauche et à droite, p. 9 ; condition 5 du lemme 1, p. 8). L'identité du
rebrassage seul, appliqué à une variable invariante, est imprimée (lemme 1, condition 3, p. 8 ; section 2.5, p. 9) ;
sa composition avec un réarrangement dépendant des données est déduite par le lecteur, non imprimée.
```

- Le classement « occupée en partie (noyau probabiliste) » tient : ni trop fort, ni trop faible. La lecture adverse n'est écrite nulle part dans les trois pièces (recherche des mots « adversar », « attack », « undetect », « indistinguish » : la seule occurrence est le sens « intrusions observées » chez Vovk, p. 15, déjà notée par le rapport).

### E — mineur — Ramdas et collègues, classes C et K : une phrase non portée par la page, une brique plus proche non relevée

- Pages : Ramdas et collègues p. 6, p. 20-21.
- Le rapport écrit (section 3.3) : « Les alternatives markoviennes stationnaires gardent la marginale de Bernoulli et changent la dépendance ». L'article ne dit rien de tel : il fixe la probabilité du premier tirage à un demi « pour simplifier » (p. 6, lu sur le PDF, non contrôlé par programme) et ne parle ni de stationnarité ni de marginale conservée. C'est une glose du lecteur.
- Brique plus proche, non relevée : la section 4.3 oppose une source « collante » (dépendance positive, fréquences limites égales à un demi), contre laquelle l'e-processus diverge, à une source de Bernoulli à probabilité variable, contre laquelle il ne gagne rien : “The right picture confirms that this is due to the Markovian aspect of the source, and not due to the changing probabilities.” (p. 21, légende de la figure 5). C'est un contraste imprimé « dépendance changée à fréquences égales, détectée ; marginale changée sans dépendance, non détectée », pour une statistique construite pour la dépendance. Rien sur le signe de l'erreur de la somme ou du maximum : le classement « voisin » tient.
- Texte corrigé proposé (section 3.3, ligne « Classes C et K ») :

```text
- **Classes C et K — voisin.** L'e-processus conçu pour les alternatives markoviennes détecte une dépendance entre
  tirages successifs (p. 11, 26) ; la section 4.3 oppose une source « collante » à fréquences limites égales, détectée,
  à une source de Bernoulli à probabilité variable, non détectée (p. 20-21, figure 5). Rien sur le signe de l'erreur
  de la somme ou du maximum sous dépendance positive ou négative ; l'article ne parle pas de marginales conservées.
```

### F — mineur — Ramdas et collègues, « puissance un » : la condition de l'article est omise

- Pages : p. 11, p. 26.
- La phrase citée, “we prove that it has power one against any first-order Markovian alternative” (p. 26), est celle du résumé final ; le théorème 7 la borne : la chaîne ne doit pas être de Bernoulli, et la condition vaut presque sûrement “provided the chain does not have any absorbing states” (p. 11). Le rapport reprend la phrase large aux sections 3.1 et 8 (point 4).
- Texte corrigé proposé : ajouter « (alternatives qui ne sont pas de Bernoulli et sans état absorbant, p. 11) » après « puissance un contre les alternatives markoviennes d'ordre un », aux deux endroits.

### G — mineur — Ramdas et collègues, T3 : un voisin du volet « statistiques d'ordre neutralisables » est cité comme simple limite

- Pages : p. 11-12 (exemple 9).
- L'article exhibe des alternatives d'ordre supérieur “that appear to be Bernoulli when summarized by only first order transition parameters” (p. 11), contre lesquelles son e-processus d'ordre un tend vers zéro (exemple 9, p. 12). C'est une structure de dépendance choisie pour être invisible à une statistique d'ordre donnée — sans adversaire, sans réarrangement, sans garantie locale. Le rapport ne le range que dans les « limites reconnues » (section 3.4).
- Texte corrigé proposé (section 3.3, ligne T3, à ajouter) : « L'exemple 9 (p. 11-12) montre aussi une dépendance d'ordre deux invisible à la statistique des transitions d'ordre un : voisin du volet des statistiques d'ordre neutralisables, sans adversaire. » Classement inchangé (« voisin »).

### H — mineur — section 8 (« ce qu'une phrase publique ne doit pas affirmer ») : trois lignes manquent, une est à préciser

- Aucune ligne infondée : les sept lignes sont portées par les pages citées.
- Ligne 6 à préciser. Le contre-exemple de l'annexe 10.2 porte sur un vecteur “which is not an exchangeable n-vector” dont toutes les coordonnées sauf la première sont égales (dépendance positive parfaite), sur le test fondé sur la première coordonnée, et “the probability of rejection equals” un demi quel que soit le niveau (p. 38, lu sur le PDF pour la valeur) : au-dessus du niveau seulement quand celui-ci est inférieur à un demi. Ni la somme, ni le maximum, ni un processus e. La formule « moitié qualitative » du rapport est juste ; il faut ajouter « pour une statistique de position, pas pour la somme ni le maximum ».
- Lignes à ajouter :

```text
8. Que le sous-groupe « permutations des agents à l'intérieur de chaque pas » est une écriture nouvelle : c'est, au
   nom près, le groupe produit par lots de Koning, les lots arrivant un par intervalle de temps (p. 21, 23-24).
9. Que « le groupe compte » est un fait nouveau : « sous-groupe moins riche, hypothèse plus large, puissance perdue »
   est imprimé chez Koning (remarque 12, p. 23) ; seuls la lecture du côté de l'attaquant et l'exemple chiffré restent
   non trouvés.
10. Que l'impossibilité d'une martingale d'échangeabilité non triviale dans la filtration des données est propre à
    Ramdas et collègues : Vovk l'énonce (p. 8) et Koning la relit comme dégénérescence d'un sous-groupe (p. 23).
```

- Appui de la ligne 10 : “It is easy to check that for the natural underlying filtration” les seules martingales d'échangeabilité sont presque sûrement constantes (Vovk, p. 8 ; la fin de la phrase est citée par le rapport).

### I — mineur — section 9 (voisins nommés et non lus) : manques

Aucune ligne infondée : chaque voisin listé est bien nommé à la page dite (vérifié pour toutes les lignes). Manquent, par ordre d'intérêt pour T :

- Lehmann et Stein (1949), « On the theory of some non-parametric hypotheses » — Koning p. 2, 4, 5, 16, 31 (“This recovers the main result of Lehmann and Stein [1949].”, p. 16) : source classique de la puissance des tests d'invariance ; premier endroit où chercher un énoncé « puissance égale au niveau contre une alternative invariante ».
- Chung et Fraser (1958), « Randomization tests for a multivariate two-sample problem » — Koning p. 13 (“One may also replace G in (3.2) with a random variable that is uniform on a compact subgroup [Chung and Fraser, 1958].”) : origine des tests par sous-groupe, voisin de « le groupe compte ».
- Ritzwoller et Romano (2022), « Uncertainty in the hot hand fallacy: Detecting streaky alternatives to random Bernoulli sequences » — Koning p. 5, 17, 26 (“long sequences are required to detect a hot hand”, p. 26) ; Miller et Sanjurjo (2018) — Koning p. 5, 17, 26. Puissance de statistiques de séries contre des alternatives « à séries » sous le nul d'échangeabilité : voisin de T3 (r actions consécutives hautes ; l'alternative de Koning est “For simplicity, we say a player is ‘hot’ if they hit k shots in a row.”, p. 26).
- Vovk (1986), « On the concept of the Bernoulli property » — Vovk p. 4, 32-34 : décomposition « échangeable et compte binomial » (“ω should be exchangeable, and the number of 1s in it should be binomial”, p. 33), c'est-à-dire orbite contre intérieur de l'orbite.
- Page (1954), « Continuous inspection schemes » ; Poor et Hadjiliadis (2009), « Quickest Detection » ; Shiryaev (2019), « Stochastic Disorder Problems » — Vovk p. 15-16, 20 : voisins de T3 (somme cumulée de Page) et de L.
- Kallenberg (2011, 2017, 2021) — Koning p. 10, 11, 35 : décomposition des lois invariantes, noyaux d'inversion.
- Žitković ; Delbaen ; Epstein et Schneider (fork-convexité, stabilité, « rectangularité » des décisions robustes) — Ramdas et collègues p. 14-15 : voisins du volet « Réalité qui choisit pas à pas ».
- Précision d'identité : Ramdas et collègues citent « Testing randomness online », Statistical Science, 2021, comme l'approche de Vovk fondée sur la prédiction conforme (p. 8, 26, référence 36) ; cela renforce, sans l'établir, l'identité probable avec la pièce 1906.09256 notée par le rapport.

### J — mineur — Vovk, T2 : classement juste, appui à resserrer

- Pages : p. 8, p. 15, p. 25.
- Le rapport appuie « aucune martingale conforme ne peut alors croître en espérance » sur la proposition 3.1 et la remarque 3.2 (p. 7). L'appui direct est p. 25 : les valeurs p conformes “are IID and uniform on [0, 1] under any exchangeable probability measure”, et p. 15 : parier contre une suite échangeable “which is futile, and so its value decreases exponentially quickly”. Le classement « contre-indice (mécanisme du rebrassage, groupe plein, sans attaquant) » tient ; « pas nécessairement de loi P₀ » est exact.
- T1 chez Koning : « voisin » tient. La pièce dit que l'orbite des permutations est le multi-ensemble — “Permuting such a shot sequence exactly fixes the number of hits” et des échecs (p. 17) — et que le test jette l'information d'orbite ; elle n'énonce pas qu'une statistique invariante garde son taux sous un réarrangement choisi par un attaquant.
- Vovk, T3 : « validité seulement » est exact — “we do not expect the first alarm to be raised too soon under the hypothesis of randomness” (p. 17) ; aucune garantie de détection. Vovk, tests classiques : “Nonparametric statistics provides us with plenty of p-variables for testing exchangeability” (p. 5), sans énoncé sur leur neutralisation.

---

## 2. Les composantes dites « non trouvées » : recherche active

Méthode : lecture du texte complet (étendue ci-dessus), puis recherche par mots sur les 113 pages extraites — « copula », « Slepian », « adversar », « attack », « adaptive », dépendance positive ou négative (« positive dependence », « positively », « negatively », « associat »), « order statistic », « CUSUM », « cumulative sum », « scan », « sliding », « window », « autocorrel », « serial correlation », « runs test », « von Neumann », « two-way », « row », « column », « array », « partial exchangeab », « shuffl », « randomly permut », « rearrang », « undetect », « indistinguish », « powerless », « multiset » — et lecture de chaque passage trouvé.

| composante | résultat de la recherche | verdict du rapport |
|---|---|---|
| Lecture adverse de T2 (attaquant indétectable) | aucune occurrence d'un adversaire du test dans les trois pièces ; « attack » seulement chez Vovk p. 15 (intrusions observées) | confirmé : non trouvée |
| « Le groupe compte » | remarque 12 et exemple 12 de Koning (p. 23), exemple 18 (p. 37) : fait qualitatif imprimé du côté du testeur | à corriger : voisin proche, moitié qualitative imprimée (constat C) |
| Classes C et K, signes | « copula » et « Slepian » : zéro occurrence ; aucun énoncé de signe de l'erreur sous dépendance positive ou négative ; voisins : Koning p. 38, Ramdas et collègues p. 20-21 | confirmé : non trouvée ; appui chez Ramdas à corriger (constat E) |
| T3, garanties locales (balayage, somme cumulée de Page, co-élévation) | « scan », « sliding », « window » : zéro occurrence ; somme cumulée seulement chez Vovk p. 16-21, appliquée à une martingale conforme, avec validité seule | confirmé : non trouvée |
| T3, statistiques d'ordre neutralisées par un attaquant adaptatif | aucun réarrangement adverse ; voisins : Ramdas et collègues p. 26 (Réalité qui choisit pas à pas) et p. 11-12 (exemple 9) ; « adaptive » chez Koning seulement pour la taille des lots et la validité « adaptative » (p. 21, 23) | confirmé : non trouvée ; un voisin à ajouter (constat G) |
| T4 (somme lue séquentiellement, sommes partielles dominées) | rien | confirmé |
| Mesure sur activations | rien | confirmé |

Aucun théorème, proposition, corollaire, lemme ou remarque des trois pièces, corps ou annexes, n'énonce une composante que le rapport déclare « non trouvée ». Les deux endroits où le rapport sous-estime ce qui est imprimé sont des **exemples et une remarque** de la section 6 de Koning (constats A et C).

## 3. L'exposé du théorème d'impossibilité de Ramdas et collègues

- Exact. Le théorème 17 (p. 17) dit que toute loi sur les suites binaires appartient à l'enveloppe fork-convexe fermée des lois indépendantes et identiquement distribuées de Bernoulli, d'où, par le théorème 13 (p. 16), que toute “Q-NSM must be nonincreasing, and hence these never exceed one and always have zero power for any” niveau (p. 17). Cadre : “We now return to the main focus of this paper, which is binary sequences” (p. 17) ; “All martingale statements in this paper will implicitly refer to this canonical filtration.” (p. 3). Le rapport rend ces trois bornes (classe de statistiques, suites binaires, filtration des données) et distingue bien les impossibilités informelles d'une autre nature (p. 1, 5, 18, 22 ; “no test can possibly have power one” pour un seul point de rupture, p. 22) et l'impossibilité par clôture convexe (“safe and consistent e-processes do not exist and neither do valid, power-one tests.”, p. 4).
- La conclusion tient : T2 est une égalité de lois, qui vaut pour tout test et toute filtration ; le théorème 17 borne une classe de statistiques dans une filtration, contre toute alternative, et d'autres statistiques y échappent. Les deux ne se recouvrent pas. « Voisin, autre nature » est le bon classement.
- Seule réserve : la condition du théorème 7 omise (constat F).

## 4. Profondeur de lecture

Le journal du lecteur montre l'extraction à 22:38:14 et le contrôle final à 22:46:59 : moins de neuf minutes pour 113 pages, 72 citations et le rapport. Jugement, après relecture complète des trois pièces :

- **Ce qui a été bien lu** : les annexes sont couvertes (Koning annexes 9 et 10, p. 34-38 ; Vovk annexe A, p. 33 ; discussion finale de Ramdas et collègues, p. 26) ; les chiffres relevés sont exacts (vérifiés contre le texte : p. 24, 26 et 38 de Koning ; p. 22, 23 et 25 de Ramdas et collègues ; p. 6, 10, 13, 14 de Vovk) ; les 72 citations sont aux pages dites ; l'exposé de la fork-convexité est exact ; aucune surestimation d'occupation chez Ramdas et collègues ni chez Vovk.
- **Ce qui a été lu trop vite** : la section 6 de Koning. Le lecteur a vu le groupe produit par lots mais pas que les lots y sont des intervalles de temps (p. 21, 23-24) ; il n'a pas relevé la remarque 12 (p. 23) ; il a omis la phrase de la page 26 qui fonde le produit par joueur sur l'indépendance, ce qui l'a conduit à écrire « exactement » ; il n'a pas vu la propriété d'absorption de Haar (p. 9), qui est la brique directe de T2. Chez Ramdas et collègues, une glose non imprimée (constat E) et la section 4.3 non exploitée.
- **Conséquence** : aucune de ces omissions ne change le verdict d'ensemble ni ne fait passer une composante de « non trouvée » à « occupée ». Elles changent la répartition de l'occupation de l'unification et le libellé de deux lignes revendicables. Le premier risque nommé par le mandat (un énoncé de théorème ou de proposition non vu) ne s'est pas réalisé ; le risque réalisé est plus bas d'un cran (une remarque et des exemples non exploités).

## 5. Verdicts

- **Rapport : « tient avec corrections »** (constats A, B, C majeurs ; D à J mineurs ; aucun bloquant).
- **T, table fermée : « occupé en partie ».** Par composante, après corrections :

| composante | verdict après contre-lecture |
|---|---|
| Unification temps × agents | occupée en partie — plus largement que ne le dit le rapport : groupe produit par lots, lots indexés par le temps, sous-groupe des permutations de toutes les observations (Koning p. 21-24, 35) ; restent le tableau à deux indices, les deux partitions ensemble, l'usage négatif |
| T1 | voisin (inchangé) |
| T2, identité du rebrassage | occupée en partie — rebrassage seul imprimé (Koning p. 8-9), composition avec un réarrangement dépendant des données déductible, lecture adverse non trouvée ; contre-indice chez Vovk (inchangé) |
| T2, « le groupe compte » | voisin proche — moitié qualitative imprimée du côté du testeur (Koning p. 23) |
| T3, garanties locales | non trouvée ; voisin chez Vovk (validité seule) |
| T3, attaquant adaptatif contre les statistiques d'ordre | non trouvée ; voisins chez Ramdas et collègues (p. 26 ; p. 11-12) |
| Classes C et K, signes | non trouvée ; voisins (Koning p. 38 ; Ramdas et collègues p. 20-21) |
| T4 | non trouvée |
| Mesure sur activations | non trouvée |

- Formulation « reste revendicable », point (a), corrigée :

```text
(a) l'application, à un tableau de scores indexé par l'agent et par le pas, de deux sous-groupes produits de
permutations par blocs — par agent et par pas —, tous deux instances du groupe produit par lots de Koning
(2310.01153, exemple 10), considérés ensemble avec le groupe plein et mis au service d'énoncés négatifs face à un
attaquant ;
```

## 6. Ce que je n'ai pas fait

- Aucun autre PDF du lot 8 n'a été ouvert, ni aucun voisin de la section 9 du rapport ou du constat I.
- Les lignes 85 à 125 du programme et l'état d'antériorité de niveau 2, que le lecteur avait lus, n'étaient pas dans ma liste : je ne les ai pas ouverts. L'énoncé de T est pris de N-003 et de la note v2 seulement.
- Je n'ai pas vérifié les démonstrations de Koning ni de Ramdas et collègues ; j'ai vérifié ce que les pages énoncent.
- Les figures n'ont pas été lues visuellement (légendes seulement).
- Je n'ai pas exécuté la routine de reprise du dépôt ni lancé les tests : les registres me sont interdits par la consigne, comme toute commande git.
- Je n'ai pas corrigé le rapport contre-lu (scellé) ; les textes corrigés ci-dessus sont des propositions.
