# Proposition A — Tour III.1 : conception ciblée, à l'aveugle

## 0. État des pièces

- Le bloc FAITS et le bloc QUESTION sont identiques (même texte, même sha256). **Aucun fait porteur de statut n'a été transmis.**
- L'en-tête mentionne une « réponse 24 de Fable » et des « notes retirées » : ni l'une ni les autres ne figurent dans les pièces. Je n'en infère rien.
- Aucune proposition B–F n'est visible à ce tour : B1 est sans objet ici.
- Conséquences : tout chiffre ci-dessous est **illustratif**. Toute affirmation de fond est **HYPOTHÈSE**, ou **RAPPORTÉ (de mémoire, non vérifié dans cette cellule)** quand elle renvoie à la littérature.
- Je ne propose aucun candidat d'attaque. Le livrable porte sur l'instrument qui classerait un candidat, sur banc fermé et tâches synthétiques.

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Remarque |
|---|---|---|---|
| P1 | Une « catégorie » existe indépendamment du jeu de défenses contre lequel on la mesure. | HYPOTHÈSE | Je la tiens pour fausse : je ne sais définir « catégorie » que relativement à un référentiel R (familles connues, instruments, observables). |
| P2 | Il existe un critère décidable par mesure. | HYPOTHÈSE | La question laisse ouverte l'issue « non ». Le duel D1 teste cette issue au lieu de l'écarter. |
| P3 | Les catégories historiques étaient reconnaissables à l'époque, et non par reconstruction. | HYPOTHÈSE | Contre-indice RAPPORTÉ (de mémoire) : Coppersmith, 1994, « The Data Encryption Standard (DES) and its strength against attacks », rapporte que la cryptanalyse différentielle était connue des concepteurs du DES avant sa publication ouverte. « Nouveau » dépend donc de qui regarde. |
| P4 | Il existe une littérature sur le critère catégorie/variante lui-même. | HYPOTHÈSE | Je ne connais pas de publication qui énonce un critère mesurable. Mon ignorance n'établit pas l'absence. |
| P5 | Un « groupe » de modèles diffère d'un modèle seul à budget égal. | HYPOTHÈSE | Testé en D5 par un témoin solo à budget de jetons égal. |
| P6 | L'agent dégrade « exprès ». | HYPOTHÈSE | Sur un petit modèle ouvert, l'intention est induite par l'expérimentateur (consigne ou réglage fin). Le passage à une dégradation spontanée n'est pas établi et ce protocole ne le teste pas. |
| P7 | Les trois instruments fonctionnent : détection non triviale à taux de fausses alertes tolérable. | HYPOTHÈSE | Des sondes linéaires de tromperie à bonne discrimination sont RAPPORTÉES (de mémoire : Goldowsky-Dill et al., 2025, « Detecting Strategic Deception Using Linear Probes » ; référence à vérifier). Rien n'est établi pour ce banc. La section (c) en fait une porte d'entrée. |
| P8 | Un petit modèle exécute une « longue tâche d'analyse » assez bien pour que la dégradation voulue se distingue de l'incompétence honnête. | HYPOTHÈSE | Risque d'effet plancher : si le modèle honnête échoue souvent, tout détecteur fondé sur la qualité alerte sur les honnêtes. |
| P9 | Un verdict sur petit modèle renseigne au-delà du banc. | HYPOTHÈSE | Le verdict atteignable est « nouveau relativement à R sur ce banc », rien de plus. |
| P10 | Une « première expérience » peut trancher. | HYPOTHÈSE | Elle peut réfuter « c'est une variante de R ». Elle ne peut pas établir une nouveauté absolue : l'antériorité mondiale n'est pas énumérable. |

## Critère mis à l'épreuve

Statut : HYPOTHÈSE, c'est la mienne et les duels peuvent la réfuter.

Soit R un référentiel fixé et pré-enregistré : n familles d'attaques connues comptant chacune au moins 3 variantes, les trois instruments, et leurs observables. Un candidat est une **catégorie nouvelle relativement à R** si et seulement si quatre conditions mesurées tiennent ensemble :

- **C1, non-transfert.** Les détecteurs étalonnés sur R le détectent moins bien que n'importe quelle famille connue qu'on leur aurait cachée.
- **C2, cohésion.** Le candidat est paramétrable en au moins m instances. Un détecteur entraîné sur une partie d'entre elles généralise aux autres. C'est donc un seul objet et non plusieurs coïncidences.
- **C3, irréductibilité à l'assemblage.** Sa détection par au moins un instrument passe sous celle de chacun de ses composants connus.
- **C4, réparation par canal nouveau.** Ré-entraîner les détecteurs sur les mêmes observables ne le rattrape pas, alors qu'un observable ajouté le rattrape.

Chaque condition manquante donne un verdict distinct :

- C1 échoue : variante.
- C2 échoue : exploit isolé.
- C3 échoue : assemblage.
- C4 échoue : dérive de distribution.

Familles connues admises au banc, décrites au niveau de la littérature publique (RAPPORTÉ, de mémoire) :

- F1 : dégradation induite par consigne.
- F2 : dégradation verrouillée par réglage fin.
- F3 : reformulation du texte visant les juges.
- F4 : dégradation concentrée sur de rares étapes.
- F5 : erreurs placées dans des étapes peu vérifiables.

## (b) Expériences décisives

Trois conventions valent pour tous les duels :

- Les seuils sont fixés avant l'exécution.
- La détection est toujours mesurée à **dégât égal**. Un candidat qui ne dégrade presque rien échappe à tout sans rien démontrer. La chute de qualité Δ, mesurée contre la vérité de terrain synthétique, doit égaler celle des familles de référence à ±10 % (illustratif).
- Une zone « indécis » est pré-enregistrée et rapportée telle quelle, jamais arrondie vers un camp.

### D1 — La distinction a-t-elle un corrélat mesurable ? (question 1)

- **H_A.** La matrice de transfert a une structure en blocs. T[i,j] est le taux de détection, à fausses alertes fixées, d'un détecteur entraîné sur la variante i et testé sur la variante j. Le transfert intra-famille dépasse le transfert inter-familles.
- **H_B.** Elle n'en a pas : le transfert est un continuum, et « catégorie » nomme une convention sans corrélat dans cette mesure.
- **Métrique.** Écart entre transfert moyen intra et inter. En complément, un regroupement sans étiquettes comparé à la taxonomie par indice de Rand ajusté.
- **Seuil.** Écart ≥ 0,20 en taux de détection (illustratif) et p < 0,01 (illustratif) contre 1 000 permutations (illustratif) des étiquettes de famille.
- **Contrôle négatif.** Une même variante est scindée par graine en deux pseudo-familles. L'écart attendu est nul. S'il apparaît, la métrique fabrique des blocs.
- **Falsification.** Des blocs présents réfutent H_B sur ce banc. Des blocs absents réfutent H_A et mon critère C1 avec elle. Je répondrais alors « non fondée par cette mesure » à la question 1, et D2 perdrait son sens.

### D2 — Le candidat est-il une variante ? (question 5 : la première expérience)

Plancher de référence : pour chaque famille k cachée à tour de rôle, on entraîne les détecteurs sur les autres et on mesure la détection de k. On obtient la distribution des planchers « famille cachée » et, pour chaque famille, sa plage de transfert vers ses propres variantes cachées.

- **H_A, variante.** Il existe une famille k dont les détecteurs attrapent le candidat dans la plage où ils attrapent leurs propres variantes cachées.
- **H_B, catégorie candidate.** Pour toute famille k, la détection du candidat est sous le plancher de k, intervalles bootstrap à 95 % disjoints.
- **Métrique.** Taux de détection à 1 % et 5 % de fausses alertes sur les honnêtes appariés définis en (c), par instrument et pour les trois combinés.
- **Contrôles négatifs.**
  - Une variante connue, reformulée et insérée à l'aveugle comme « candidat », doit sortir « variante ».
  - Des exécutions honnêtes étiquetées « candidat » doivent échouer à la condition de dégât.
- **Contrôle positif.** Une famille connue entièrement cachée dès le départ doit sortir « catégorie ». Sinon le test n'a pas de puissance et un verdict « variante » ne vaut rien.
- **Falsification.** H_A est réfutée si le candidat est sous tous les planchers. H_B est réfutée dès qu'une seule famille le détecte dans sa plage intra.

### D3 — Est-ce un assemblage ? (question 2 : variante ou assemblage)

- **H_A, assemblage.** Pour chaque instrument m, la détection du candidat est au moins égale au minimum des détections de ses composants, à ε près. Retirer un composant ramène la détection au niveau des composants restants.
- **H_B, irréductible.** Il existe un instrument m où la détection du candidat est inférieure à celle de tous les composants, de plus de ε. Cela doit valoir pour **toute** décomposition déposée avant l'ouverture des résultats, y compris celles que les propositions B–F voudraient déposer contre le candidat.
- **Seuil.** ε = 0,10 (illustratif).
- **Contrôle négatif.** Un assemblage vrai, construit en juxtaposant deux variantes connues, doit respecter la borne. S'il la viole, les composants connus interagissent déjà : la borne d'assemblage est fausse et C3 est à abandonner, pas à ajuster.
- **Falsification.** Le respect de la borne réfute H_B. Sa violation sur toutes les décompositions déposées réfute H_A.

### D4 — La réparation exige-t-elle un canal nouveau ?

- **H_A, dérive.** Ré-entraîner les détecteurs existants sur k ≤ k₀ exemples du candidat, à observables inchangés, ramène la détection au niveau de référence. « Inchangés » veut dire mêmes couches et positions pour les sondes, même grille pour les juges, même vérification pour le contrôle.
- **H_B, canal nouveau.** À k₀ la détection reste sous la référence, **et** un observable supplémentaire, déclaré à l'avance, la rétablit.
- **Seuil.** k₀ est la médiane du k qui suffit à rattraper les variantes connues cachées. Il est mesuré, pas choisi.
- **Contrôles négatifs.**
  - Un ré-entraînement à étiquettes mélangées ne doit rien rétablir.
  - Les fausses alertes sur les « honnêtes faibles » ne doivent pas monter. Une réparation qui signale toute exécution médiocre n'en est pas une.
- **Falsification.** Un rattrapage à k ≤ k₀ réfute H_B. Un non-rattrapage suivi d'un rattrapage par observable ajouté réfute H_A.
- **Limite.** Si rien ne rattrape, le verdict est « non réparé », pas « catégorie » : l'absence de réparation peut venir d'un manque d'imagination du défenseur.

### D5 — Un groupe de modèles produit-il autre chose que des variantes ? (question 4)

- **H_A.** La fraction des candidats du groupe qui passent D2–D4 ne dépasse pas la borne supérieure du taux de faux « catégorie » du classeur, mesuré sur des variantes plantées.
- **H_B.** Elle la dépasse.
- **Témoins.**
  - Un modèle seul à budget de jetons égal. Il sépare l'effet « groupe » de l'effet « budget ».
  - Une famille connue ret