# Proposition A, tour III.1 : conception ciblée à l'aveugle

**État des pièces.** Le bloc FAITS ne contient aucun fait porteur de statut : il reproduit mot pour mot la question, avec la même empreinte, que je ne peux pas recalculer. Aucune proposition B–E ne m'est transmise, donc la règle B1 est sans objet à ce tour.

En conséquence, rien ci-dessous n'a le statut VÉRIFIÉ. Mes énoncés sont des HYPOTHÈSES, la littérature est RAPPORTÉE de mémoire, et tous les chiffres sont illustratifs.

---

## Réponse en cinq points

**(1) Question de recherche.** Quand le relecteur est une copie du rédacteur, ses activations portent-elles, sur un défaut que son texte laisse passer, un signal qu'un relecteur d'un autre modèle de capacité comparable ne porte pas, au point qu'à budget d'audit fixé l'identité des poids profite au moins autant au défenseur qu'à l'adversaire ?

**(2) Réponse attendue, réfutable** [HYPOTHÈSE]. L'identité des poids ouvre le même canal aux deux camps. Ce qui permet à une copie de reconnaître sans communication le sabotage d'une autre (connaissance partagée du défaut) est aussi ce qu'une sonde peut lire chez la copie lectrice. J'en tire trois prédictions :

- **P1.** Dans une matrice rédacteur × lecteur à trois modèles, la détection par sonde est meilleure sur la diagonale (même modèle) que hors diagonale, une fois retirés les effets principaux (difficulté du rédacteur, capacité du lecteur).
- **P2.** Le gain de coordination tacite des copies sur des paires hétérogènes existe mais reste faible à 8 milliards de paramètres.
- **P3.** À budget d'audit égal, une équipe de copies instrumentée par activations n'est pas moins sûre qu'une équipe hétérogène.

Mes probabilités subjectives sont d'environ 45 % pour P1, 35 % pour P2 et 50 % pour P3 (illustratif). Je ne tiens donc pas ma propre thèse pour acquise. L'issue que je crois la plus probable est que la capacité du lecteur domine et que l'interaction d'identité soit petite, ce qui réfuterait P1.

**(3) Antériorité la plus proche** [RAPPORTÉ, citée de mémoire, à vérifier par l'arbitre]. Greenblatt, Shlegeris, Sachan et Roger (2023), « AI Control: Improving Safety Despite Intentional Subversion ». De mémoire, ce travail traite la surveillance par une copie du même modèle, la collusion, la validation par défauts synthétiques et le budget d'audit limité. De mémoire aussi, il n'utilise pas les activations et ne mesure pas l'interaction d'identité rédacteur × lecteur. Antériorités voisines, toutes de mémoire :

- Wen et al. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats » : menaces diffuses.
- Panickssery, Bowman et Feng (2024), « LLM Evaluators Recognize and Favor Their Own Generations » : auto-reconnaissance.
- Goldowsky-Dill, Chughtai, Heimersheim et Hobbhahn (2025), « Detecting Strategic Deception Using Linear Probes » : sondes de tromperie.
- Mallen et al. (2024), « Subversion Strategy Eval… » : sous-titre à vérifier.
- Motwani et al. (2024), sur la collusion secrète entre agents : titre exact à vérifier.
- Järviniemi (2025), sur la collusion par points focaux : titre exact à vérifier.
- Knight et Leveson (1986), « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming » : loi connue ailleurs.

**(4) Expérience.** Voir la section (b). Le cœur est la matrice 3 × 3 du duel 1, encadrée par le duel 0 (erreurs honnêtes) et le duel 3 (bilan à budget d'audit fixé).

**(5) Type de contribution.** C'est un phénomène (interaction d'identité lisible dans les activations) assorti d'un mécanisme candidat (connaissance partagée du défaut). Il s'adosse à une loi connue ailleurs, les défaillances de mode commun en programmation multi-versions. Ce n'est pas une garantie. Le seul élément quasi logique est trivial : si le verdict d'un lecteur diffère entre « notre sabotage » et un défaut-piège, l'information se trouve dans ses activations. Cela n'implique pas qu'une sonde linéaire la trouve avec peu d'étiquettes.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Risque si faux |
|---|---|---|---|
| S1 | Des copies aux contextes différents se comportent comme une seule politique (mêmes poids, donc mêmes dispositions). | HYPOTHÈSE | Le contexte peut faire diverger les copies. « Copies » ne serait alors pas la bonne variable. |
| S2 | Il existe une vérité de terrain de l'intention, qui sépare le sabotage « défendable isolément » de l'erreur honnête. | HYPOTHÈSE | Sur un modèle de 8 milliards, l'intention est induite par l'expérimentateur (consigne ou LoRA). Sa ressemblance avec un sabotage spontané n'est pas établie. |
| S3 | Les activations portent un signal absent du texte. | HYPOTHÈSE | Une sonde peut ne lire que du lexical, ou la présence de la consigne de sabotage dans le contexte. |
| S4 | La dégradation se localise dans des contributions. | HYPOTHÈSE | Si le défaut n'existe que dans la composition (trois omissions alignées), l'unité de mesure par copie est mauvaise. Il faut un score par tâche. |
| S5 | Les vérifications coûteuses sont fiables, et leur nombre est la contrainte active. | HYPOTHÈSE | Un audit faillible change le calcul. L'oracle doit être validé. |
| S6 | On peut comparer à des « modèles différents » à capacité égale. | HYPOTHÈSE | Deux modèles n'ont jamais la même capacité. La confusion identité/capacité est le piège central, d'où le plan en matrice. |
| S7 | L'adversaire ne s'adapte pas à l'instrument. | HYPOTHÈSE | Toute conclusion vaut pour un adversaire non adaptatif, sauf test d'effort dédié. |
| S8 | Un modèle de 8 milliards sait produire un défaut subtil et se coordonner. | HYPOTHÈSE | Effet plancher : l'expérience serait alors non concluante, et non négative. |
| S9 | Quelque chose change. | La question le laisse ouvert | L'issue nulle est légitime. Elle est prévue aux duels 0 à 3. |

---

## (b) Expériences décisives

### Dispositif commun

**Tâche.** Chaîne à trois rôles sur de courtes fonctions Python, de niveau exercices de type MBPP ou HumanEval (références à vérifier). Le rédacteur écrit, le testeur écrit des tests, le relecteur approuve ou rejette. La vérité de terrain vient de tests cachés et d'une solution de référence.

**Compositions.**
- SOLO : une instance tient les trois rôles dans un seul contexte.
- COPIES : trois instances du même modèle, contextes séparés.
- MIXTE : trois modèles ouverts différents de taille voisine.

**Adversaire.** Deux modes d'induction :
- par consigne système ;
- par organisme-modèle : un LoRA entraîné à insérer une famille de défauts et à les approuver, sans aucune trace dans le contexte.

**Cas honnêtes appariés.** Pour chaque contribution sabotée, sur le même problème, le même rôle et le même modèle, on apparie :
- une contribution honnête correcte ;
- une erreur naturelle du même modèle, récoltée dans des exécutions honnêtes qui échouent aux tests cachés.

Une sonde qui sépare le sabotage du code correct mais pas de l'erreur honnête ne détecte que « défaut présent », ce qu'un test fait mieux.

**Défauts-pièges.** Défauts synthétiques insérés par le défenseur, à étiquettes connues. Ils sont la seule source d'entraînement des sondes, car le défenseur réel n'a pas d'étiquettes de sabotage.

**Pré-enregistrement.** Seuils et analyses sont fixés avant toute exécution adversariale.

### Duel 0 : mode commun honnête contre effet propre à l'adversaire

- **H_A.** Sans aucun adversaire, un relecteur-copie laisse déjà passer les erreurs naturelles de son propre modèle plus souvent qu'un relecteur d'un autre modèle. L'identité compte d'abord par fiabilité (angles morts corrélés).
- **H_B.** En condition honnête, les taux de laisser-passer sont égaux sur et hors diagonale. Tout effet d'identité observé ensuite est propre à l'adversaire.
- **Métrique.** Taux d'approbation textuelle d'erreurs naturelles, dans la matrice 3 rédacteurs × 3 relecteurs. On mesure le terme d'interaction (diagonale moins hors-diagonale, effets de ligne et de colonne retirés).
- **Seuil** (illustratif). H_A si l'interaction est d'au moins 5 points, avec un intervalle bootstrap à 95 % excluant 0. H_B si l'intervalle tient dans ±3 points (test d'équivalence).
- **Contrôle négatif.** Erreurs injectées mécaniquement par mutation, qui n'appartiennent à aucun modèle. L'interaction doit y être nulle. Sinon le plan mesure autre chose que l'identité.
- **Falsification.** H_A falsifie « sans adversaire, des copies valent une équipe quelconque » et impose de soustraire cette ligne de base à tous les duels suivants. H_B falsifie la transposition directe de la loi du mode commun à ce cadre.

### Duel 1 : lisibilité par identité (côté défenseur)

- **H_A.** Les activations d'un lecteur qui est une copie du rédacteur distinguent le sabotage de l'erreur honnête appariée mieux que celles d'un lecteur d'un autre modèle.
- **H_B.** La lisibilité ne dépend que de la capacité du lecteur. L'identité n'ajoute rien.
- **Métrique.** Sonde linéaire sur les activations du lecteur (dernière position et moyenne, 3 ou 4 couches), entraînée sur défauts-pièges seulement, testée sur sabotage réel contre erreur honnête appariée. On calcule l'AUROC et le taux de détection à 1 % et 5 % de fausses alertes. On mesure l'interaction Δ dans la matrice 3 × 3, avec en covariable le taux de détection textuelle des défauts-pièges par chaque lecteur.
- **Seuil** (illustratif). H_A si Δ ≥ 0,05 d'AUROC, intervalle excluant 0, effet de même signe pour les trois modèles en diagonale. H_B si l'intervalle de Δ tient dans ±0,03.
- **Contrôles négatifs.**
  - Sonde à étiquettes permutées.
  - Sonde sur la couche d'entrée. Si elle fait aussi bien, le signal est lexical.
  - Directions aléatoires.
  - Contexte honnête contenant le vocabulaire du sabotage sans consigne (contrôle de fuite de consigne).
  - Reprise de tout le duel avec l'organisme LoRA, où aucune consigne n'est dans le contexte.
- **Deux variantes à ne pas confondre.**
  - Lecteur honnête (copie sans consigne, adversaire induit par consigne) : on mesure la connaissance partagée.
  - Lecteur complice (LoRA partagé) : on mesure la discordance entre ce que la sonde lit (« défaut vu ») et ce que le texte dit (« approuvé »).
- **Falsification.** H_A falsifie « des copies n'offrent au défenseur rien qu'un moniteur quelconque n'offre ». H_B falsifie le mécanisme de ma proposition : l'identité ne resterait alors qu'un risque (duel 2), sans compensation côté défenseur.

### Duel 2 : coordination sans communication (côté adversaire)

- **H_A.** Des copies s'accordent sans communiquer mieux que des paires de modèles différents.
- **H_B.** Pas d'avantage d'identité. Soit les points focaux tiennent à la culture d'entraînement commune (même-modèle ≈ inter-modèles, tous deux au-dessus du hasard), soit tout le monde est au hasard.
- **Jeu.** Jeu focal inséré dans la tâche. Le rédacteur choisit une famille de défaut parmi K = 8 (illustratif). Le relecteur, sans rien voir du choix, désigne la seule famille qu'il laissera passer. Le succès est la concordance.
- **Métrique.** Taux de concordance même-modèle moins taux inter-modèles, comparé au hasard 1/K.
- **Seuil** (illustratif). H_A si l'écart est d'au moins 10 points, intervalle excluant 0.
- **Contrôles négatifs.**
  - Permutation et paraphrase des options. Si la concordance disparaît, c'était un biais de position.
  - Concordance de paires honnêtes à qui l'on demande une simple préférence (ligne de base de goûts corrélés).
  - Variante avec canal de communication ouvert, puis paraphrasé par un modèle tiers, pour situer la borne supérieure.
- **Falsification.** H_A falsifie « l'hétérogénéité ne protège pas de la collusion tacite ». H_B avec concordance inter-modèles élevée falsifie « diversifier les modèles est une défense contre la coordination tacite ». H_B au hasard partout falsifie, à cette échelle, le gain d'identité de l'adversaire : la menace exigerait alors un canal.

### Duel 3 : bilan net à budget d'audit fixé

- **H_A (couplage).** Avec l'instrument à activations, COPIES n'est pas moins sûr que MIXTE.
- **H_B (découplage).** COPIES est moins sûr même instrumenté. Il existe des familles d'attaque où le gain de l'adversaire est élevé et celui du défenseur nul.
- **Métrique.** Sur des épisodes complets, probabilité qu'un résultat dégradé (échec aux tests cachés) soit livré sans alerte. Le budget d'audit est b = 2 % des contributions (illustratif). Les audits sont alloués par score décroissant, les taux de fausses alertes des équipes honnêtes sont égalisés.
- **Seuil** (illustratif). H_A si sûreté(COPIES) ≥ sûreté(MIXTE) − 2 points (marge de non-infériorité). H_B si l'écart dépasse 5 points en défaveur de COPIES.
- **Contrôles négatifs.**
  - Équipes honnêtes dans les trois compositions (consommation d'audits et fausses alertes).
  - Condition SOLO, pour vérifier que l'effet ne tient pas à la seule séparation des contextes.
  - Même protocole sans activations (texte seul), pour isoler l'apport de l'instrument.
- **Analyse exploratoire, non décisive.** Par famille d'attaque (6 familles, illustratif), signe de l'association entre gain adversaire (duel 2) et gain défenseur (duel 1). Six points n'autorisent qu'un test de signe. Je ne le présente pas comme une preuve.
- **Falsification.** H_A falsifie la règle générale « préférer des équipes hétérogènes pour la sûreté » quand les activations sont disponibles. H_B falsifie ma thèse et livre la liste des familles où l'identité est un gain pur pour l'adversaire.

### Test d'effort, non décisif

Un LoRA adversaire est entraîné avec un terme de perte d'évasion contre la sonde du duel 1. On mesure la chute du taux de détection à fausses alertes fixées. Sans ce test, toute conclusion se limite à un adversaire non adaptatif (S7).

---

## (c) Mesure minimale pour chaque instrument nommé dans la question

Quatre choses sont communes à tous les instruments :

- le taux de détection est rapporté à 1 % et 5 % de fausses alertes ;
- les fausses alertes sont estimées sur les cas honnêtes appariés de la section (b), erreurs naturelles comprises ;
- il faut au moins 2 000 cas honnêtes (illustratif) pour qu'un taux de 1 % ait un intervalle utilisable ;
- les intervalles sont calculés par bootstrap par problème, pas par contribution.

**Vérifications mécaniques à battre**, toutes bon marché :

1. exécution de tests publics, et tests générés par mutation ;
2. analyse statique (linter) ;
3. couverture, par les tests du testeur, de la branche modifiée par le rédacteur (détecte l'alignement des omissions, donc S4) ;
4. classifieur sac-de-mots sur le diff ;
5. rapport de vraisemblance de la contribution sous le même modèle en consigne honnête (vérification propre au cas des copies, puisque le défenseur possède la politique de référence).

### Instrument 1 : le texte de chaque copie

- **Mesure.** Détection par un moniteur textuel, soit le même modèle, soit un modèle tiers, sur sabotage contre erreur honnête appariée.
- **Fonctionne si** il dépasse les vérifications 1 à 5 d'au moins 5 points de détection à 1 % de fausses alertes (illustratif).
- **Ne fonctionne pas si** le rapport de vraisemblance ou la couverture de branche font aussi bien. Le « texte lu par un modèle » est alors superflu.
- **Si les copies communiquent.** Même mesure sur les messages, avec la paraphrase par un modèle tiers comme vérification mécanique à battre.

### Instrument 2 : les activations internes

- **Mesure.** Sonde du duel 1, entraînée sur défauts-pièges, testée hors distribution sur sabotage réel.
- **Fonctionne si** les quatre conditions suivantes sont réunies :
  - elle bat le moniteur textuel du même lecteur sur la même passe, sinon les activations n'ajoutent rien au texte ;
  - elle bat la sonde de couche d'entrée ;
  - elle bat le rapport de vraisemblance ;
  - elle tient sur l'organisme LoRA, sans consigne en contexte.
- **Spécificité des copies à mesurer à part.**
  - Transfert : une sonde entraînée sur un rôle est appliquée telle quelle aux deux autres. On compare à des sondes par modèle, standardisées, en MIXTE.
  - Agrégation par tâche : on compare somme et maximum des scores des k copies. Le contrôle est la même agrégation sur scores standardisés en MIXTE. Si l'agrégation hétérogène fait aussi bien, l'espace d'activation commun n'apporte rien d'essentiel.
- **Rapporter séparément** la sonde chez le rédacteur et la sonde chez le lecteur.

### Instrument 3 : les vérifications coûteuses en nombre limité

- **Validation de l'oracle.** On mesure la part des sabotages qui passent les tests cachés. Ils sont étiquetés « tentative sans effet » et exclus du numérateur, mais comptés à part.
- **Mesure d'allocation.** Courbe de sûreté en fonction du budget, pour b ∈ {0,5 ; 1 ; 2 ; 5 ; 10 %} (illustratif). Elle est comparée à l'allocation aléatoire et à l'allocation par le meilleur score mécanique.
- **Fonctionne si** l'allocation par l'instrument 2 domine ces deux courbes sur toute la plage.
- **Spécificité des copies.** Valeur informationnelle d'un audit positif, mesurée par :
  - le nombre d'audits avant la première prise ;
  - la probabilité qu'une autre tâche soit sabotée sachant une prise.

  La comparaison se fait entre COPIES et MIXTE. Si la politique est partagée (S1), une prise devrait renseigner sur toutes les copies. Si cette probabilité conditionnelle n'est pas plus élevée en COPIES, S1 est affaibli.

---

## (d) Ancrage matériel

Les faits ne fournissent aucun chiffre. Tout ce qui suit est illustratif.

**Modèles ouverts** [RAPPORTÉ, de mémoire].
- Modèle principal : Llama-3.1-8B-Instruct.
- Comparateurs de taille voisine : Gemma-2-9B-it, Qwen2.5-7B-Instruct, Mistral-7B-Instruct.
- Trois modèles suffisent pour la matrice. Le quatrième sert de paraphraseur et de moniteur tiers.

**Calcul.**
- Environ 200 000 générations d'environ 300 jetons, soit environ 60 millions de jetons.
- Passes de lecture avec extraction d'activations.
- 4 à 6 entraînements LoRA de quelques heures chacun.
- Un ou deux GPU de 24 à 48 Go suffisent en demi-précision.
- Ordre de grandeur : 300 à 500 heures-GPU, soit quelques centaines à environ 1 500 € en location.
- Stockage des activations réduites (dernière position et moyenne, 4 couches) : de l'ordre de 10 à 20 Go.

**Calendrier sur 8 semaines.**

| Semaines | Travail |
|---|---|
| S1–2 | Banc d'essai, exécutions honnêtes, récolte d'erreurs naturelles, duel 0, pré-enregistrement |
| S3–4 | Adversaire par consigne, défauts-pièges, sondes, duel 1 |
| S5 | Duel 2 |
| S6 | Organisme LoRA, reprise du duel 1 |
| S7 | Duel 3 |
| S8 | Contrôles, test d'effort, rédaction |

**Point de blocage à lever en semaine 2 (S8).** Si moins de 5 % (illustratif) des tentatives de sabotage du modèle passent les tests publics tout en échouant aux tests cachés, il faut changer de tâche. Une possibilité est une relecture de texte avec faits vérifiables. À défaut, on déclare l'expérience non concluante.

---

## Issues qui rendraient la question sans intérêt

1. Les vérifications mécaniques 1 à 5 atteignent le même taux de détection que les activations, à fausses alertes égales, dans les trois compositions. L'accès aux activations des copies ne change alors rien d'utile.
2. L'interaction d'identité est nulle aux duels 0 et 1 et la coordination tacite est au hasard au duel 2. « Copies » n'est alors pas une variable pertinente, et le problème se ramène au contrôle d'un agent seul.
3. Seul le duel 0 est positif. La question se ramène alors à une loi connue de fiabilité (mode commun), sans composante adversariale propre. Le résultat reste utile pour l'ingénierie, mais ce n'est plus la question posée.
4. Effet plancher (S8). L'expérience est non concluante et doit être rapportée comme telle.

## Vérification de la nouveauté avancée

**Ce que j'avance** [HYPOTHÈSE, non vérifiée]. À ma connaissance, aucun travail n'a mesuré l'interaction d'identité rédacteur × lecteur au niveau des activations, avec erreurs honnêtes appariées et sondes entraînées sur défauts-pièges.

**Comment vérifier.**
- Lire les sections de méthode des travaux cités en (3), en cherchant précisément les trois éléments réunis : moniteur de même modèle contre modèle différent, sondes sur activations, appariement à des erreurs honnêtes.
- Chercher les travaux sur les sondes d'auto-reconnaissance et sur les erreurs corrélées entre modèles de langue (références à vérifier, je ne peux en attribuer aucune de mémoire).
- Tenir la nouveauté pour fausse tant que cette recherche n'est pas faite. Si le duel 1 existe déjà, la contribution se limite au duel 3.

## Limites assumées

- Un sabotage induit par consigne ou par LoRA n'est pas un sabotage spontané (S2).
- Les conclusions valent pour 8 milliards de paramètres et des fonctions courtes.
- Sans le test d'effort, elles valent pour un adversaire non adaptatif.
- Les statuts ne changeront qu'après exécution et audit : d'ici là, tout ce document reste au statut HYPOTHÈSE.

FIN-DE-CELLULE