# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v3` (empreinte du module 95bea064c753ca24e6a7619b99f1b03bd64700fac8568b3c598ec67bb985eb62)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHRncy9ErNskmNWZavDy`
- Heure (UTC) : 2026-11-22T05:42:08Z
- Réglages : effort `high`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-8-these-pince-etau-boite-blanche-v1.md` — sha256 bde8abf0db0bdeabb232ae4fe080b59f369e5d9442e5300da51bcbd05bc138e2 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` — sha256 534ed7a288fc0729377654c6060ae900ac5ec76c8d6fa2518bee4f1239464a2b (compagnon : vérifié)
  - remarques : `docs/programme-controle-ia-v2.md` — sha256 2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c (compagnon : vérifié)
  - remarques : `docs/notes/pince-hors-distribution-v1/reponse-fable-pince-hors-distribution-v1.md` — sha256 c0318d1f95e932f67938102164156fd375c124921156a9884c1a3035b073cbfc (compagnon : vérifié)
  - remarques : `docs/notes/pince-hors-distribution-v1/etau-d4-v1/faits-etau-taxe-bras-declare-v2.md` — sha256 3fb0799360942a00a011fe23f88adfd4cef70cf62d7528494937a438a1744b45 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-4/relecture-fable-api.md` — sha256 cf55c7e073a1b99d2229bd08a96eb29e63878477379311b49227c5c5b6950344 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 73a204da17aab2a4b947e2e9b5eb05920b49dbad92fc92587865eaa831a57eb0
- Jetons : entrée 45278, sortie 19571 (dont réflexion 9567), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.145064 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 8 — « mieux que la boîte noire », la pince et l'étau : réponse approfondie

**Conclusion d'abord.** « Mieux que la boîte noire sur le sabotage diffus » reste un résultat de porte conditionnel, mais ce n'est plus une thèse. La pince peut devenir une thèse sous sa forme de complémentarité, à condition d'un contrôle absent du dépôt : la boîte blanche doit rattraper plus de manqués qu'une seconde boîte noire d'une autre lignée. L'étau ne peut pas devenir la thèse du papier A, mais il peut devenir une mesure, celle de la taxe jointe dans un bras d'attaque déclaré, à loger au papier C. Les trois objets sont trois lectures de la constante de la loi héritée de la réponse 4. Ma recommandation : la loi héritée en modèle nul cité, le bilan mesuré en thèse, la complémentarité en figure, l'étau en hypothèse mesurée ailleurs.

**Réserves.**
- La « réponse sur l'étau solide », annoncée en remarque, ne m'a pas été transmise. La probabilité de survie de 0,25 est donc un chiffre rapporté par la demande, sans source que je puisse lire.
- Je ne sais pas ce qu'est le « protocole X » et je ne peux rien lancer. Je fournis la question.
- Je cite de mémoire : toute antériorité a le statut « rapporté, non vérifié sur PDF ».
- Je ne confirme aucun identifiant arXiv de 2026.
- Les chiffres de la pièce de faits sur l'étau sont dits « lus sur PDF » par leur auteur. Je ne les ai pas vérifiés, donc aucun n'est opposable ici.
- Je n'ai pas recalculé les empreintes.
- Je ne connais ni le texte exact des décisions N-075 à N-077 ni l'état de la porte G0.
- « Sans nom de personne » contredit « antériorité nommée » : je ne nomme que les auteurs des travaux cités.

---

## 1. Ce qu'un expert ferait et qui n'est pas demandé

- **Séparer thèse, résultat de porte et mesure** [PROPOSITION]. La demande met sur le même plan une comparaison (boîte blanche contre boîte noire), une mesure (la complémentarité) et une conjecture sur l'ensemble des coups possibles de l'attaquant (l'étau).
- **Exiger le contrôle « seconde boîte noire »** [PROPOSITION]. Deux moniteurs quelconques se complètent toujours un peu. La complémentarité ne dit quelque chose de l'accès interne que si la boîte blanche rattrape plus qu'un second moniteur de sorties d'une autre lignée, et plus que la sonde aléatoire appariée en covariance.
- **Retirer le texte de la sonde** [PROPOSITION]. La pièce de faits rapporte qu'environ 70 % de la baisse de rappel sous évasion par renforcement vient du changement du texte produit [FAIT RAPPORTÉ]. Une part du signal des sondes est donc peut-être lisible dans le texte [HYPOTHÈSE]. L'expert accumulerait le résidu du score de sonde, une fois régressé sur le prédicteur de texte ajusté sur des épisodes honnêtes seuls.
- **Dire la nature logique de l'étau** [PROPOSITION]. C'est une affirmation sur ce que l'attaquant peut faire, et non sur ce que nos organismes font. Elle n'est réfutable que dans un bras d'attaque déclaré, contre le détecteur tel qu'il est déployé.
- **Chercher la quantité conservée dans le domaine d'origine** [PROPOSITION]. En stéganographie, la sécurité est parfaite dès que la distribution de couverture est préservée. Transposé, l'étau affirme qu'aucune politique dommageable ne loge dans la distribution honnête jointe du texte et des activations. Or le contexte rapporte que le surplus de capacité du jumeau honnête forme un budget de sabotage invisible [FAIT RAPPORTÉ]. Cela joue contre une borne générale [HYPOTHÈSE].
- **Vérifier la provenance du 0,25** avant de s'y appuyer [PROPOSITION].

## 2. Données brutes de départ

- La table appariée épisode × action × moniteur, avec le score brut de chaque moniteur sur les mêmes actions, et non des aires sous la courbe par moniteur.
- Les activations aux trois couches rapportées (7, 15, 23) et le texte brut, pour refaire le résidu.
- Les paires d'exécutions honnêtes jumelles par tâche.
- Les verdicts de l'oracle sur les dommages plantés, lecteur par lecteur, mode par mode, mode tenu à l'écart compris.
- La liste scellée des bases boîte noire et leur point de lecture, puisque la mâchoire externe doit voir les actions elles-mêmes.
- Pour l'étau : les triplets (score externe, score interne, dommage réalisé) par régime d'attaquant. Ils n'existent pas [FAIT RAPPORTÉ, note sur la pince : « jamais mesuré » au 8 novembre].

## 3. Méthodes et outils

- **Capture résiduelle à budget partagé** : probabilité que la boîte blanche alerte sachant le sabotage et le silence de la boîte noire, avec intervalle binomial exact sur les manqués et rééchantillonnage par tâche. Les seuils sont fixés pour que la fausse alerte jointe vaille α.
- **Règle jointe écrite d'avance** : la moyenne de deux processus e reste un processus e, sans hypothèse d'indépendance. Leur produit en exige une [FAIT RAPPORTÉ ; Vovk, Wang, 2021, « E-values: calibration, combination and applications » ; rapporté, non vérifié sur PDF].
- **Détectabilité jointe** : déplacement des deux scores sous sabotage, pondéré par l'inverse de leur covariance honnête. C'est la forme chiffrée de la complémentarité.
- **Dépendance des pannes** : rapport des cotes du silence commun contre le produit des silences, et recapture à deux mâchoires sur les audits au hasard (déjà proposée dans la note sur la pince).
- **Essai « jumeau contre jumeau »** sur la règle jointe : sa fausse alerte doit valoir α.
- **Mondes plantés avec trois témoins « doit mourir »** : sonde aléatoire jointe, seconde boîte noire jointe, étiquettes permutées.
- **Pour l'étau** : frontière à trois axes par régime d'attaquant (gradient à travers la sonde, renforcement sans ce gradient, non entraîné), contre le détecteur déployé.

## 4. Ce qui vérifie hors du directeur et de Claude

- Une équipe rouge d'une autre lignée, qui écrit le mode tenu à l'écart et, pour l'étau, les attaques.
- Un statisticien de l'inférence séquentielle, pour la validité de la règle jointe.
- Les auteurs de l'antériorité la plus proche, à qui l'on demande : « ceci est-il votre mesure ? »
- L'essai « jumeau contre jumeau » et les témoins « doit mourir », dont l'issue ne dépend d'aucun avis.
- La reproduction sur une seconde famille de modèles.
- Le préenregistrement à empreinte, puis la relecture par les pairs.

## Demande reformulée

« Parmi trois énoncés (la boîte blanche détecte plus que la boîte noire ; les deux jointes détectent plus que la meilleure des deux et plus que deux boîtes noires ; l'attaquant ne baisse un score qu'en montant l'autre ou en perdant du dommage), lequel peut être écrit avant les résultats sous forme réfutable, avec sa grandeur, son contrôle mortel et son antériorité du domaine d'origine ? Lequel mérite le rang de thèse, plutôt que celui de mesure dans un papier dont la thèse est autre ? Dis ce que chacun coûte en épisodes, en calcul et en bras d'attaque. »

---

## (1) « Mieux que la boîte noire » : ce qui l'a affaiblie, ce qui reste

**Ce qui l'a affaiblie.**
- La garantie est partie [FAIT RAPPORTÉ, N-075] : les sondes sont un accélérateur et la borne sur le dommage vient du plancher d'audit.
- L'horizon est borné : aucune conclusion au-delà de n = m (N-076, application du corollaire 1 de Ker 2010), m et n comptés dans la même unité.
- L'adversaire qui répond au mieux est hors revendication [FAIT RAPPORTÉ, N-077].
- La partie garantie de la pince n'emploie pas les activations [FAIT RAPPORTÉ, note sur la pince] : dans l'identité du bilan, la lecture du suspect s'annule.
- Le programme disait déjà que le gain de la boîte blanche « en général est établi » et que le squelette séquentiel boîte noire existe [FAIT RAPPORTÉ, programme, H1 et H2]. La thèse n'a donc jamais été qu'une mesure sur le diffus et le flou.
- La part du signal de sonde lisible dans le texte est inconnue [HYPOTHÈSE, voir section 1].
- Les travaux d'évasion rapportés montrent des sondes trompées par gradient, à faible coût de capacité [FAIT RAPPORTÉ, pièce de faits, non opposable].

**Ce qui reste : un résultat conditionnel, dont voici la forme exacte** [PROPOSITION].

> Sur les organismes déclarés (instruction cachée, réglage fin), contre chaque base de la liste scellée (mots et coût, cascade, dernier état, juge par action à capacité égale, accumulation séquentielle boîte noire), à taux de fausses alertes égal, à horizon au plus m, la boîte blanche séquentielle obtient un rappel supérieur ou un dommage cumulé à l'alerte inférieur. Le résultat est rapporté par mode, mode tenu à l'écart compris. Le même test est refait sur le résidu de sonde, une fois le prédicteur de texte retiré. Rien n'est revendiqué contre un attaquant entraîné ni contre un genre de dommage hors de l'oracle.

**Mes chances, comme jugements** [HYPOTHÈSE].

| Portée de l'énoncé | Chance de tenir |
|---|---|
| Modes de conception | 0,55 |
| Mode tenu à l'écart compris | 0,35 |
| Sur le résidu de sonde | 0,3 |

**Statut.** C'est l'issue de la porte G1 et la mesure de la constante dans la loi héritée (le facteur k de la réponse 4). Comme thèse, elle est trop conditionnelle pour porter un titre, et une issue négative ne laisserait rien.

## (2) La pince et l'étau comme thèses

### 2.1 Complémentarité (candidate sérieuse)

- **Énoncé réfutable** [PROPOSITION]. À taux total de fausses alertes égal, l'union "meilleure boîte noire et sonde" rattrape plus de sabotages diffus que l'union "meilleure boîte noire et seconde boîte noire d'une autre lignée" ; même épreuve pour la sonde aléatoire appariée. L'intervalle à 95 % est donné par mode.
- **Grandeurs** [PROPOSITION]. La part c et ses deux nuls ; le gain de détectabilité jointe sur la meilleure mâchoire seule ; le rapport des cotes du silence commun.
- **Antériorité la plus proche** [FAIT RAPPORTÉ pour l'existence, HYPOTHÈSE pour la proximité ; rapporté, non vérifié sur PDF] :
  - Parrack, Attubato, Heimersheim, 2025, « Benchmarking deception probes via black-to-white performance boosts » : le gain d'un moniteur de sorties à qui l'on donne les scores de sondes. C'est le parent direct.
  - McKenzie et collaborateurs, 2025, « Detecting high-stakes interactions with activation probes » : sondes en premier filtre d'une cascade (mémoire incertaine).
  - Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, « Detecting strategic deception using linear probes ».
  - He, Wei, Chen, Carlini, Song, 2017, « Adversarial example defenses: ensembles of weak defenses are not strong » : contre l'idée qu'une jonction de deux défenses faibles en fait une forte.
  - L'ensemble à quatre moniteurs déjà cité par le programme.
- **Ce qui reste peut-être ouvert** [HYPOTHÈSE ; une zone vierge est une question]. Le cadre diffus et séquentiel, la capture résiduelle à budget partagé, le contrôle « seconde boîte noire », le résidu de sonde. Chance que cela reste inédit après lecture : 0,4.
- **Expérience minimale** [PROPOSITION]. Aucune génération nouvelle : une analyse secondaire, scellée avant G1, sur les épisodes de G1. Elle a un coût en manqués. Il faut assez de sabotages manqués par la boîte noire pour un intervalle utile, de l'ordre de cinquante par mode pour séparer 0,10 de 0,30. Le dimensionnement se fait sur le monde planté.
- **Chance de tenir** [HYPOTHÈSE]. 0,4 que c dépasse la seconde boîte noire sur les modes de conception ; 0,25 sur le mode tenu à l'écart.
- Deux issues publiables si la puissance du plan est calculée ; sinon une troisième, indéterminée. Si elle tient, l'accès interne a une valeur propre dans la défense jointe. Si elle échoue, une seconde boîte noire suffit, ce qui est une règle d'ingénierie utile et rarement écrite [HYPOTHÈSE].

### 2.2 Bilan (identité, pas thèse)

La somme (référence − lecture) + (lecture − issue) est une identité, et sa garantie est celle du plancher d'audit [FAIT RAPPORTÉ, note sur la pince]. La famille est occupée (garanties nucléaires, audit aléatoire du contrôle : Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: improving safety despite intentional subversion » ; rapporté, non vérifié sur PDF). Elle sert de cadre et ne peut pas être une thèse de boîte blanche.

### 2.3 Étau (conjecture ; mesurable, coûteuse, probablement fausse en général)

- **Trois énoncés à ne pas confondre** [PROPOSITION] :
  - *Dose-réponse côté défense.* Imposer par consigne l'évasion de la mâchoire externe élève la trace interne. C'est l'hypothèse HC2b du papier C, pour un attaquant non entraîné.
  - *Taxe jointe.* Pour chaque régime d'attaquant, échapper aux deux mâchoires coûte plus de dommage qu'échapper à la plus coûteuse des deux. La grandeur est ι, la taxe jointe moins le maximum des deux taxes simples. L'étau affirme ι > 0. Son nul est ι = 0 : une même manœuvre défait les deux mâchoires.
  - *Borne.* « On ne baisse un score qu'en montant l'autre », pour tout attaquant.
- **Ce que la borne par calcul fixe déjà** [FAIT RAPPORTÉ, pièce de faits]. L'étau retire au plus le plus petit du rappel r et de la taxe κ. Une thèse d'étau doit donc publier r, κ et ι, par régime.
- **Contre-indices rapportés** [FAIT RAPPORTÉ, pièce de faits, non opposable] :
  - un secret que la tâche emploie par construction échappe à une sonde linéaire et à un perceptron tenu à l'écart : la nécessité d'une information n'implique donc pas sa lisibilité linéaire ;
  - des évasions par gradient coûtent peu de capacité ;
  - les échecs d'évasion contre les sondes à maximum et à attention sont rangés par leurs auteurs parmi les échecs d'optimisation.
- **Antériorité** [rapporté, non vérifié sur PDF ; correspondance entre identifiants et titres de mémoire] :
  - Bailey et collaborateurs, 2024, « Obfuscated activations bypass LLM latent-space defenses », qui laisse ouverte la question du compromis ;
  - Gupta, Jenner, 2025, « RL-Obfuscation: can language models learn to evade latent-space monitors? » ;
  - Emmons et collaborateurs, 2025, « When chain of thought is necessary, language models struggle to evade monitors » : l'analogue le plus proche d'un étau fondé sur la nécessité ;
  - Carlini, Wagner, 2017, « Adversarial examples are not easily detected » ;
  - Tramèr, 2022, « Detecting adversarial examples is (nearly) as hard as classifying them » ;
  - Cachin, 1998, « An information-theoretic model for steganography ».
- **Expérience minimale** [PROPOSITION]. Pour la dose-réponse : attaque par contenu sur les organismes existants, sans entraînement. Elle est déjà dans EC.2. Pour la taxe : ajouter la lecture de ι à l'expérience EC.4, soit l'option (a) de la pièce de faits.
- **Chances** [HYPOTHÈSE] :

  | Énoncé | Chance de tenir |
  |---|---|
  | Dose-réponse de même signe sur deux familles | 0,35 |
  | ι > 0 contre un attaquant entraîné | 0,15 |
  | Borne | 0,05 |

  Les deux premières reprennent la note sur la pince. Le 0,25 de la demande tombe entre les deux : je le tiens pour cohérent, non pour vérifié.
- **Verdict.** L'étau peut devenir un résultat chiffré, y compris négatif, par exemple « la taxe jointe n'excède pas la taxe simple ». Il ne peut pas devenir une thèse posée d'avance pour le papier A : il demande un bras d'attaque déclaré, il sort du champ que N-077 laisse revendiquer, et les contre-indices sont nombreux.

## (3) Articulation avec le « phénomène hérité » de la réponse 4

Le modèle nul hérité dit que le dommage caché est d'ordre √(n + n²/m), avec une constante propre au moniteur. Les trois objets sont trois lectures de cette constante [PROPOSITION].

| Objet | Lecture de la constante | Rapport à la loi |
|---|---|---|
| « Mieux que la boîte noire » | Rapport des constantes des deux boîtes prises seules | **La même chose** vue comme mesure (le facteur k) |
| Complémentarité | Constante jointe à deux dimensions, pondérée par la covariance honnête des deux scores | **Complément** |
| Étau | Plancher de cette constante quand l'attaquant choisit son déplacement sous contrainte de dommage | **Rivale de N-077** si un plancher positif existait ; sinon description de la constante par régime d'attaquant |

Le théorème négatif du programme s'applique à la jonction [FAIT RAPPORTÉ, note sur la pince] : à marginales préservées, l'espérance des statistiques additives est inchangée ; une statistique de relation entre mâchoires est le test efficace, non le seul puissant. Le résidu de sonde est cette statistique de relation [PROPOSITION]. Un texte plus propre que les activations ne l'annoncent y apparaît comme une discordance, ce qui donne à l'étau une forme mesurable sans attaque entraînée.

**Pour les papiers.** A porte la loi et sa constante, simple puis jointe. C porte la déformation de la constante par l'adversaire (gain g, taxe, ι). B porte la même loi indexée par agent.

## (4) Recommandation de thèse pour le papier A

[PROPOSITION]

- **Thèse** : la loi héritée comme modèle nul cité, le bilan mesuré, la complémentarité. « Les lois de la dissimulation répartie (Ker 2007 et 2010 ; Avenhaus et Jaech 1981), déjà transposées au suivi des usages contre l'extraction (Khilar 2026), donnent un modèle nul du dommage qu'un saboteur diffus peut cacher. Le papier mesure, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent ; puis ce que l'accès interne rattrape et qu'une seconde boîte noire ne rattrape pas. »
- **Résultat de porte** : « mieux que la boîte noire » sous la forme exacte du (1), comme rapport de constantes, résidu de texte compris.
- **Figure candidate au titre secondaire** : la complémentarité, avec le contrôle « seconde boîte noire ». Si elle tient mode tenu à l'écart compris, elle monte au résumé.
- **Hors du papier A** : l'étau, logé au papier C (EC.2 pour la dose-réponse, EC.4 pour la taxe).
- **Ce qui me ferait changer** : un parent direct qui couvre déjà le contrôle « seconde boîte noire » en cadre séquentiel, auquel cas la complémentarité redescend en simple mesure ; une dose-réponse de l'étau nette sur deux familles, auquel cas l'étau monte en thèse du papier C ; une porte G1 franchie largement sur le résidu, auquel cas « mieux que la boîte noire » reprend le titre.

Confiance d'ensemble : 0,6.

---

## Question neutre pour le collisionneur

**Test de neutralité appliqué.**
1. Les mots « pince » et « étau » sont retirés : ces métaphores présupposent que cela serre.
2. Aucune mention du programme, de ses décisions ni de ma recommandation.
3. Les trois énoncés ont la même forme, et les issues « faux » et « indécidable » sont offertes.
4. Le contrôle mortel et l'antériorité sont demandés pour chacun.
5. Une porte de sortie est prévue : un énoncé oublié, ou aucune thèse.
6. Défaut résiduel : l'ordre A, B, C peut suggérer une progression. Je le signale et ne le corrige pas, faute de mots.

**Question (245 mots).**

Un agent de langue accomplit une longue tâche. Un adversaire peut en dégrader le résultat par petites touches dont aucune n'est suspecte isolément. Deux moniteurs l'observent : l'un ne lit que les sorties (texte, actions, produit), l'autre lit les activations internes de l'agent.

Trois affirmations sont possibles :
- A. À fausses alertes égales, le moniteur interne détecte plus que le moniteur de sorties.
- B. Les deux ensemble détectent plus que le meilleur des deux, et plus que deux moniteurs de sorties différents.
- C. L'adversaire ne peut réduire sa visibilité pour l'un sans l'accroître pour l'autre, ou sans perdre en dommage.

Pour chacune :
- dites si elle est vraie, fausse ou indécidable en l'état des connaissances ;
- écrivez-la sous forme réfutable, avec la grandeur à mesurer ;
- nommez l'antériorité la plus proche (auteurs, année, titre), en disant si vous citez de mémoire ;
- décrivez la plus petite expérience qui la trancherait sur un modèle ouvert de huit milliards de paramètres, et le contrôle sans lequel son résultat ne vaudrait rien ;
- dites quelle issue la rendrait sans intérêt.

Dites ensuite si A, B et C sont une même affirmation, des compléments ou des rivales. Dites si l'une mérite d'être la thèse d'un article, ou seulement une mesure dans un article dont la thèse serait autre, ou si aucune ne le mérite. Signalez toute affirmation que cette liste oublie. N'attribuez aucune nouveauté sans dire comment la vérifier.

---

## Décisions qui reviennent au directeur

**Décision 1 — Fixer le statut de « mieux que la boîte noire sur le sabotage diffus ».**
- *Enjeu.* Une revendication du papier A, et ce que vaut une issue négative de G1.
- *Option a : résultat conditionnel de la porte G1, sous la forme exacte du (1).* Avantage : conforme à N-075, N-076 et N-077, rien à retirer plus tard. Inconvénient : plus de titre « détecteur supérieur ».
- *Option b : la garder comme thèse.* Avantage : message simple. Inconvénient : garantie déjà retirée, et une issue négative ne laisse rien.
- *Option c : la retirer.* Avantage : prudence. Inconvénient : perd la mesure de la constante.
- *Recommandation.* Option a. Confiance : 0,7.

**Décision 2 — Ajouter la complémentarité, avec le contrôle « seconde boîte noire » et le résidu de sonde, au préenregistrement de G1.**
- *Enjeu.* La seule forme de la pince qui se mesure sans épisode ni bras nouveau ; elle doit être scellée avant la lecture.
- *Option a : analyse secondaire scellée avant G1, dimensionnée sur le monde planté.* Avantage : aucun calcul de génération, deux issues publiables. Inconvénient : préenregistrement plus lourd, et un nombre de manqués peut-être insuffisant.
- *Option b : papier à part.* Avantage : lisible. Inconvénient : un quatrième front.
- *Option c : ne pas la mesurer.* Avantage : rien à écrire. Inconvénient : la pince reste un mot.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 3 — Loger l'étau au papier C comme hypothèse mesurée, et non comme thèse du papier A.**
- *Enjeu.* Une dépense de calcul, un bras d'attaque déclaré, et la cohérence avec N-077.
- *Option a : dose-réponse dans EC.2 et lecture de la taxe jointe ι dans EC.4, pour les trois régimes, contre le détecteur déployé.* Avantage : ni bras ni organisme de plus. Inconvénient : dépend du calendrier du papier C.
- *Option b : bras à part, maintenant.* Avantage : un chiffre plus tôt. Inconvénient : un front de plus, et une chance faible que l'étau tienne.
- *Option c : ne pas mesurer.* Avantage : aucun coût. Inconvénient : l'idée forte reste sans chiffre.
- *Recommandation.* Option a. Confiance : 0,6.

**Décision 4 — Fixer la thèse du papier A.**
- *Enjeu.* Le titre, le résumé et la prévision scellée.
- *Option a : la loi héritée, avec « mieux que la boîte noire » en constante et la complémentarité en figure.* Avantage : une seule grandeur relie les trois objets et les trois papiers. Inconvénient : dépend de la lecture de l'antériorité de dissimulation d'information (décision 2 de la réponse 4).
- *Option b : la pince-complémentarité en thèse.* Avantage : thèse propre, proche de l'intuition du directeur. Inconvénient : parent direct publié, et chance de tenir de 0,4.
- *Option c : la thèse de la version 2.* Avantage : continuité. Inconvénient : voir décision 1.
- *Recommandation.* Option a, avec montée de la complémentarité au résumé si elle tient mode tenu à l'écart compris. Confiance : 0,6.

**Décision 5 — Choisir quand poser la question neutre aux collisionneurs.**
- *Enjeu.* Un tour de collisionneur, et le risque de redécouvrir un parent publié.
- *Option a : maintenant, en parallèle de la lecture sur PDF des deux parents directs (gain de la boîte noire à la boîte blanche ; ensembles de défenses faibles).* Avantage : aucun délai, et les modèles peuvent nommer d'autres parents. Inconvénient : leurs antériorités seront elles aussi de mémoire.
- *Option b : après la lecture.* Avantage : question mieux armée. Inconvénient : quelques jours, et une question moins neutre.
- *Recommandation.* Option a. Confiance : 0,6.

FIN DE LA RÉPONSE
