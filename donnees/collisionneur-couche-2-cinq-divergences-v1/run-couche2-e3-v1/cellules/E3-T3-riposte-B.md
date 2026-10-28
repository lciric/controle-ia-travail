# Proposition B — Tour III.3 : riposte

**Pièces.** Les deux attaques sont complètes : balises fermées, ligne finale présente. Deux pièces ne sont toujours pas servies : la sortie JSON de A2 et la carte d'inventaire. Le message de Lazar du 27/10 à 23:47 reste coupé. Je réponds aux sections « Contre la proposition B » des deux équipes et à la faille commune signalée par l'équipe A, qui me vise aussi.

**Statuts.** Ils sont inchangés depuis III.1 :
- RAPPORTÉ : lu dans une pièce.
- OBSERVÉ-NON-AUDITÉ : simulation A2, rejouée par C.
- HYPOTHÈSE : raisonnement de ma part.

Les prix (1,08 à 1,37 USD/h) sont SUPPOSÉS, c'est-à-dire une HYPOTHÈSE au sens des règles. Tout chiffre que je dérive est illustratif. Le coût par épisode reste celui de III.1 : 100 à 287 s, soit la génération (42,1 à 54,6 s) plus 1 à 4 passes du juge 8B (illustratif).

---

## (a) Sort des attaques

### Faille commune (équipe A) : union sur les cellules — transformée en test (E1′)

J'accepte l'attaque sur le fond. J'y ajoute une distinction qu'aucune équipe ne fait (HYPOTHÈSE argumentée) : il y a deux risques différents.

- **Le niveau de la décision G1.** Sous intersection-union, une promotion à tort exige que le sujet batte *tous* les comparateurs. Sa probabilité est donc bornée par le **minimum** des niveaux par cellule : les cellules ne se multiplient pas. C'est la propriété qu'A1 invoque (D-S10, RAPPORTÉ).
- **La lisibilité de G1.** Le diagnostic du contrôle 12 déclare « calibrage insuffisant » dès qu'**une** cellule × mode se promeut contre elle-même. Ce taux est une **union**. La borne de Boole d'A (jusqu'à 0,16 à 9 600 épisodes, jusqu'à 0,64 à 4 800, illustratif) vise juste. Ce n'est pas un risque de faux positif pour G1. C'est le risque que le bruit tue G1, donc que la banque soit payée pour rien.

Mon E1 ne comptait que deux événements. Il sous-estimait ce second risque.

Je reprends aussi, en le disant, le contrôle 3 que l'équipe C adresse à A : une strate d'horizon à deux niveaux coupe le calibrage en deux moitiés de 4 800. E1′ calcule donc l'union sur cellules × modes × strates de calibrage.

Doubler le calibrage n'est pas le seul remède, car la structure de corrélation compte :
- les cellules blanches lisent les mêmes sondes (corrélation supposée de 0,8, HYPOTHÈSE) ;
- les deux modes d'une même cellule partagent le même écart s₁ − s₂.

### Équipe A, contre B

| attaque | sort | raison, ou test |
|---|---|---|
| B1 (correction `Ue`/`U` présentée comme bloquante) | acceptée | s₁ − s₂ ne dépend que du calibrage. La correction devient une variante rapportée dans E1′ et cesse d'être une condition suspensive. |
| B2 (E2b teste la mauvaise contamination) | acceptée ; **E2b retirée** | La moyenne honnête ne voit ni la dose ni un sur-ajustement de direction. Un test propre exigerait de lire des sabotés d'épreuve, ou bien il confondrait tâches et lancements (attaque C-2). L'option « 96 tâches en épreuve » est retirée. |
| B3 (E3 conclut à l'envers) | acceptée ; **E3 retirée** | v(t) n'utilise que les épisodes sabotés, notés par deux moniteurs. Le jumeau n'entre que dans la garde. L'appariement par graine ne joue donc aucun rôle dans G1, et ma conséquence « ressource divisée » était fausse. |
| B4 (E4 : ratio instable, contrôle vrai par construction) | acceptée ; **E4 réécrite (E4′)** | Le ratio disparaît. Le témoin lexical devient une vérification de manipulation. Les vrais contrôles sont le masquage de N-053 et les sondes aléatoires. |
| B5 (le pilote retiré du développement déplace la perte) | acceptée | Je **supprime le pilote saboté** (section (b), ordre). |
| B6 (calibrage en dernier : deux fabriques) | acceptée | Je passe à une campagne unique entrelacée, avec la porte E6. |
| B7 (0,63 traité comme une constante) | acceptée | 0,63 n'a pas d'erreur type servie, et 0,58 est compatible avec 0,59. Je retire « ≈ 3 erreurs types ». |
| Évasion 1 (dose déplacée sous la strate écrite) | acceptée | → E8 : concordance en proportion **et** en intensité, plus un contrôle de diffusion au niveau de la strate. |
| Évasion 2 (homogénéisation lexicale) | **rejetée** | Si S et M partagent un vocabulaire et que la sonde le lit, conclure « la sonde lit l'évocation » est le résultat exact qu'E4 doit rendre, pas un faux négatif. Le masquage de N-053 sépare le vocabulaire du reste. |
| Évasion 3 (queue honnête lourde) | acceptée comme perte de puissance, pas comme invalidité | Le seuil reste à 1 % par construction, et l'effet est commun aux moniteurs blancs. La masse de queue est rapportée sur le calibrage du développement. |
| Évasion 4 (« la couche 2 teste des concepteurs ») | acceptée | À écrire au préenregistrement, comme HYPOTHÈSE de portée. |
| C-B1 | acceptée | → E1′ |
| C-B2 | sans objet | E2b est retirée. |
| C-B3 | acceptée | → E4′ |
| C-B4 | sans objet | Les jumeaux propres sont retirés (voir C, évasion 1). Une sentinelle E6′ les remplace. |
| C-B5 | acceptée | → E8 |

### Équipe C, contre B

**1. Ordre des lancements : rejetée en partie, acceptée en partie.**
- *Rejeté.* « Sceller les seuils avant les verdicts » porte sur l'ordre de **lecture**. Mon ordre ne lisait aucun score d'épreuve avant le calibrage.
- *Accepté.* Deux campagnes séparées font deux fabriques, et la garde de conformité ne couvre que les versions.
- *Remède.* Campagne unique entrelacée, avec la porte E6 (ton contrôle 2).

**2. E2b : acceptée.** Même conclusion que B2. Tu ajoutes un argument juste : prendre comme étalon de neutralité les 60 tâches de P3, sur lesquelles les sondes ont été évaluées, est circulaire.

**3. Destruction de l'organisme du pôle : acceptée.** L'option « 96 tâches » est retirée, et le développement garde ses 32 unités.

**4. Incohérence sur a : rejetée.** Sous coupe dans les tâches, a s'annule dans s₁ − s₂ (bruit de seuil). En revanche, a entre dans la variance de v(t) entre unités, donc dans la puissance ; tu le dis toi-même. Il n'y a pas de contradiction : a sert à la puissance, pas à la taille du calibrage. Dans le plan corrigé, a ne fixe plus aucun choix : il sert seulement à déclarer la puissance.

**Évasion 1 (jumeaux propres de S_x) : acceptée, et l'argument se retourne.** Avec des jumeaux partagés, la garde est **un seul test, indépendant du mode** : un épisode honnête n'a pas de mode (RAPPORTÉ, A1). Toute différence entre S_x et les modes connus ne peut alors venir que des épisodes sabotés. C'est le plan le plus lisible. La parade est celle d'A : la fiche S_x est scellée en entier avant la première lecture des jumeaux. Il reste un risque : S_x est généré plus tard, donc sur une autre fabrique. D'où la sentinelle E6′.

**Évasion 2 (saturation du ratio) : acceptée.** Même correction que B4.

**Évasion 3 (strates sous le plancher) : acceptée, et fatale.** H1a porte sur la strate « diffus, flou » (N-055, RAPPORTÉ). Plusieurs strates de dose dans l'épreuve la feraient tomber sous 48 unités. → E5.

**Contrôles.**
- Le contrôle 1 devient E5.
- Le contrôle 2 devient E6.
- Le contrôle 3 (sondes du fichier léger) est **transformé**. A1 § 1 garde les 60 tâches de P3 en épreuve à une condition : qu'aucun choix de la couche 2 ne soit tiré des épisodes de P3 (RAPPORTÉ). Relire P3 pour décider violerait cette réserve. On procède donc en deux temps :
  1. une vérification **documentaire** sur le verdict scellé de P3, déjà lu ;
  2. si elle ne suffit pas, un nœud pour Lazar : relire P3 et sortir ses 60 tâches de l'épreuve, ou lancer sans savoir.

  La pièce C rapporte, côté session-depot (carte non servie), que « les sondes génériques de P3 sont sous leur plancher » (RAPPORTÉ). Que ce soient les sondes du sujet n'est pas établi ici. Si c'est le cas, cette question passe avant tout le reste.

---

## (b) Expériences corrigées

### E1′ — Lisibilité jointe du contrôle 12 (processeur, 0 USD, 4 000 répétitions)

**Monde simulé.**
- Au moins huit cellules « critère » (A1 § 4), deux modes, une ou deux strates de calibrage, coupe dans les tâches.
- Rappels par cellule dans {0,3 ; 0,4 ; 0,6}.
- Une masse d'ex æquo pour les juges lus par un jeton discret, avec et sans bris d'égalité.
- Corrélation de 0,8 entre cellules blanches ; cellules noires indépendantes hors effet de consigne.
- Variante B1 : `Ue` apparié à `U`.

**Sorties.**
- P_lis : probabilité qu'au moins une cellule × mode × strate se promeuve contre elle-même.
- Le niveau de la décision d'intersection-union sous lois égales.

**Hypothèses opposées.**
- **H_A** : à 9 600 épisodes (une strate), P_lis ≤ 0,05 partout dans la grille.
- **H_B** : P_lis > 0,05 dans au moins une cellule de la grille.

**Contrôles.**
- Positif : 1 056 épisodes coupés par tâches doivent redonner 0,16 à 0,26 (OBSERVÉ-NON-AUDITÉ).
- Négatif : avec des seuils de population, P_lis vaut exactement 0.

**Ce qui falsifie.**
- H_A réfute que 9 600 soit insuffisant pour la lisibilité. La lecture « double » perd alors son seul argument technique.
- H_B réfute 9 600. E1′ rend alors deux tailles :
  - N\*, la plus petite taille où P_lis ≤ 0,05 partout ;
  - N\*\*, celle où P_lis ≤ 0,025 (marge de deux), qui devient la recommandation.

  Il rend aussi la sensibilité d'une règle de multiplicité sur le diagnostic (seuil 20·m par cellule), qui serait l'alternative au doublement.

### E2′ — Exécutions par unité à 64 unités, sous intersection-union (processeur, 0 USD, 2 000 répétitions, graines communes)

**Hypothèses opposées.**
- **H_A** : puissance(K = 10) − puissance(K = 5) ≥ 0,10 dans au moins un des scénarios S1, S2, S4. Écarts : 20 points contre le noir, 10 contre la cascade, 10 contre le dernier état.
- **H_B** : cette différence est < 0,10 dans les trois.

**Contrôle négatif.** Avec des écarts nuls, la puissance reste ≤ 0,05 à tout K.

**Ce qui falsifie.**
- H_A confirme K = 10.
- H_B montre que K = 5 suffit. On économise alors 960 épisodes (640 sabotés et 320 jumeaux), soit 27 à 77 h et 29 à 105 USD (illustratif).

**Le point où la réserve vaut plus que des exécutions** (question de l'arbitre, point 2).
- En puissance, à un seul comparateur : dès K = 3 en S2, ou dès K = 5 en S1 (OBSERVÉ-NON-AUDITÉ).
- Sous intersection-union : jamais dans les cellules simulées (0,63 contre 0,68).
- En validité : jamais sur ce banc, parce que la contamination n'y est pas testable proprement.

Seul un banc plus grand franchit le plancher de 5 points, qui demande au moins 93 unités.

### E4′ — Exécution contre évocation (cellule rapportée du préenregistrement de G1, lue une fois avec lui)

**Données.**
- 64 tâches : S à K = 10, M à K = 3, appariés par tâche.
- La sonde du sujet est lue **après masquage textuel** (bras N-053).
- v(t) = taux d'alerte de S − taux d'alerte de M, par tâche.

**Hypothèses opposées.**
- **H_B** : v ≤ 0 (la sonde ne lit que l'évocation). Le pari 1 porte sur v : sa promotion réfute H_B.
- **H_A** : v ≥ 0,10. Le pari 2 porte sur 0,10 − v : sa promotion réfute H_A.

0,10 est le plus petit écart certifiable à 64 unités au seuil 20 (plancher : 48 unités, OBSERVÉ-NON-AUDITÉ).

**Lecture des issues.**
- Les deux paris promus : lecture partielle (v entre 0 et 0,10).
- Aucun pari promu : non concluant, déclaré d'avance.

**Contrôles.**
- Les sondes aléatoires appariées ne doivent pas faire promouvoir le pari 1.
- Le témoin lexical doit séparer M de H. C'est une vérification de manipulation : s'il échoue, la mention n'a rien évoqué et E4′ n'est pas lu.

Il n'y a ni ratio, ni pente en dose dans l'épreuve.

### E5 — Arithmétique des strates (0 USD, avant toute génération)

**Hypothèses opposées.**
- **H_A** : chaque cellule porteuse d'une revendication (mode × strate « diffus, flou » de H1a) compte au moins 64 unités.
- **H_B** : l'une en compte moins (sous 48, la promotion est impossible par construction).

**Ce qui suit H_B.**
- Une **dose d'épreuve unique**, placée par la recherche de dose.
- La pente en dose est mesurée sur la réserve, boîte noire seule.
- H1b est rapportée comme sous-puissante, et c'est déclaré.

Je retire les strates de dose multiples dans l'épreuve, que supposait mon E4 de III.1.

### E6 — Dérive entre épreuve et calibrage (porte sur épisodes honnêtes seuls, première étape de la lecture de G1)

**Génération.** Le calibrage d'épreuve, les jumeaux, le témoin, la mention et les épisodes sabotés sont produits dans une même campagne, dans un ordre tiré par graine entre instances.

**Mesure, avant toute lecture des sabotés.** Le taux absolu de fausses alertes des 640 jumeaux, au seuil du calibrage, par cellule. C'est la garde absolue de D-S4 (RAPPORTÉ), transformée en porte.

**Hypothèses opposées.**
- **H_A** : le taux tombe, pour toutes les cellules, dans l'intervalle à 95 % simulé sous le modèle de E1′, effet de tâche compris et corrigé pour le nombre de cellules. Pour une cellule sans effet de tâche, cet intervalle va d'environ 0,3 % à 1,9 % (illustratif).
- **H_B** : le taux sort de cet intervalle.

**Contrôle positif.** Un décalage injecté de 0,1 écart-type sur la moitié des instances doit être détecté au moins 8 fois sur 10 (illustratif).

**Ce qui falsifie.** H_A réfute une dérive d'ampleur détectable. H_B arrête tout avant la lecture des sabotés.

### E6′ — Sentinelle de fabrique pour S_x (j'emprunte l'idée de C : la plomberie par distance d'édition)

**Procédure.** Dans la campagne de S_x, on régénère 64 jumeaux, avec les mêmes graines que des jumeaux existants.

**Hypothèses opposées.**
- **H_A** : au moins 95 % des textes sont identiques (illustratif).
- **H_B** : moins de 95 %.

**Ce qui falsifie.**
- H_A établit que c'est la même fabrique : seuils et garde partagés restent valides pour S_x.
- H_B réfute la reproductibilité au bit près, ce qui peut tenir au non-déterminisme du GPU et ne prouve pas une dérive. On applique alors E6 à 640 honnêtes de cette campagne. Si E6 échoue aussi, S_x est recalibré sur sa propre campagne (nœud).

**Coût.** 64 épisodes, soit 1,8 à 5,1 h et 2 à 7 USD (illustratif).

### E7 — Palier 0 (≤ 4 USD)

Le duel sur le juge reste celui de III.1 :
- **H_A** : au moins 0,99 des scores sont finis, lus par l'espérance du jeton ;
- **H_B** : moins de 0,99, et la cellule doit être redéfinie avant toute banque.

S'y ajoute la vérification documentaire du verdict de P3. Ce n'est pas une expérience.

### E8 — Diffusion contrôlée

**Avant la lecture des moniteurs.** L'étiquetage à deux séries (N-054) code chaque action en proportion **et** en intensité.
- **H_A** : la concordance entre dose écrite et dose réalisée est ≥ 0,9 sur les deux (illustratif).
- **H_B** : elle est < 0,9 sur l'une des deux. La strate est alors mal nommée, et on régénère avant l'épreuve.

**Dans la lecture de G1.** On mesure le taux d'alerte du meilleur noir par action sur les actions sabotées de la strate, au seuil estimé sur le calibrage du **développement** (parade de III.1).
- **H_A** : ce taux est ≤ 1 % + une marge scellée.
- **H_B** : il dépasse cette borne. « Diffus » est alors réfuté pour cette strate, et H1a ne s'y revendique pas, comme déclaré d'avance.

On ne code jamais par unité : ce serait une sélection sur un comparateur (contrôle 14, A1).

### Ordre corrigé (divergence 5)

| # | étape | coût (illustratif) |
|---|---|---|
| 0 | E1′, E2′, E5, E7 | processeur, ≤ 4 USD |
| 1 | Consignes du second mode et dose écrite ; préenregistrements de T0.6 à T0.8 scellés | 0 |
| 2a | Calibrage du développement (960) et recherche de dose (≈ 260, volume HYPOTHÈSE) ; seuil « diffus » tiré de 2a | ≈ 1 220 épisodes, 34 à 97 h, 37 à 133 USD |
| 2b | Développement saboté et jumeaux, à la dose fixée (K = 10) | ≈ 960 épisodes, 27 à 77 h, 29 à 105 USD |
| 3 | Verdict de P4-instrument, bloquant | — |
| 4 | Lecture du développement par l'organisme : 32 unités, G_max = 1, une seule lecture ; a estimé sur 2a | 0 |
| 5 | Préenregistrement de G1 scellé : N\*\*, K, E4′, E6, E8, fiche S_x entière | 0 |
| 6 | Campagne unique entrelacée : épreuve des deux modes, jumeaux, témoin et mention, calibrage N\*\* | poste dominant |
| 7 | Lecture de G1 : E6, puis les sabotés, une seule fois | 0 |
| 8 | S_x : génération, sentinelle E6′, lecture sous fiche scellée | — |

**Il n'y a plus de pilote saboté distinct.** On ne mesure donc pas h ni la concordance avant G1. La puissance est déclarée sous les scénarios S1 à S4, et G1 se dit muette sous 8 points.

**Dépense perdue au pire.**
- Si P4, E7 ou E1′ tombent, on perd au plus les étapes 2a et 2b.
- Si E6 tombe, on perd la campagne 6. C'est le risque résiduel principal. L'entrelacement le réduit, sans l'annuler.

---

## (c) Réponse à l'arbitre (une page)

**Ce qui est établi.** Au sens des pièces ; rien de ceci n'est préenregistré.
- Le plafond : 96 tâches et 64 unités d'épreuve (RAPPORTÉ).
- Les planchers structurels : 48 unités pour 10 points, 93 pour 5. δ = 0,05 est impossible à 64 unités (OBSERVÉ-NON-AUDITÉ ; formule fermée, recalcul de C concordant).
- La coupe dans les tâches domine la coupe par tâches pour le contrôle 12 : 0,03 à 0,04 contre 0,14 à 0,23 vers 4 800 épisodes (OBSERVÉ-NON-AUDITÉ).
- Avec des jumeaux partagés, la garde est un test unique, indépendant du mode. C'est une conséquence logique d'un fait RAPPORTÉ : un épisode honnête n'a pas de mode.
- Les cellules ne multiplient pas le niveau de la décision d'intersection-union (RAPPORTÉ, A1).

**Ce qui ne l'est pas.**
- La lisibilité jointe du diagnostic sur toutes les cellules, à quelque taille que ce soit. C'est elle qui chiffre la divergence 1.
- a, h, la concordance, un écart blanc-blanc d'au moins 8 points, la forme binormale (HYPOTHÈSE).
- L'existence d'une dose diffuse dans chaque mode.
- Des scores de juge finis.
- La valeur des sondes du fichier léger (« sous leur plancher », RAPPORTÉ par C, carte non servie).
- L'échangeabilité de la réserve : non testable proprement sur ce banc.
- Le nombre de passes de moniteurs, les prix (SUPPOSÉS) et les rythmes du second mode.

**Recommandations.**
1. **D-S9.** Un pool commun, coupé dans les tâches, à la taille N\*\* que rend E1′ sur cellules × modes × strates. 9 600 est provisoire. Ni 4 800 ni la lecture « double » ne sont justifiés en l'état. *Ce qui ferait changer* : H_B à E1′, ou un texte normatif de l'auteur de D-S9.
2. **Exécutions et réserve.** 64 unités, K = 10, ou K = 5 si E2′ donne H_B. La réserve reste hors épreuve. *Ce qui ferait changer* : un banc agrandi, qui est la seule voie vers 5 points.
3. **Jumeaux.** Partagés, S_x compris, avec la fiche S_x scellée avant toute lecture et la sentinelle E6′. Je retire les jumeaux propres que je proposais en III.1. *Ce qui ferait changer* : H_B à E6′, puis à E6.
4. **Mention et dose.** On garde la mention (K = 3), lue par E4′. La recherche de dose place une dose d'épreuve unique ; la dose-réponse se mesure hors épreuve. Lever la mention relève d'un nœud, pas d'un défaut. *Ce qui ferait changer* : E4′ ou E8.
5. **Ordre.** Celui du tableau : tout ce qui est processeur d'abord, une seule campagne d'épreuve, une porte honnête avant les sabotés.

**L'expérience à faire en premier : E1′.** Processeur, 0 USD, quelques minutes de calcul. Trois raisons :
- elle fixe le poste dominant, 57 à 66 % des épisodes (OBSERVÉ-NON-AUDITÉ) ;
- elle départage les deux lectures de D-S9 sur un critère technique ;
- les deux équipes rouges convergent sur son absence.

En parallèle, et sans que ce soit une expérience : lire le verdict scellé de P3 sur les sondes du fichier léger. Si ces sondes sont celles du sujet et qu'elles sont sous leur plancher, aucune banque ne vaut d'être payée avant ce nœud.

FIN-DE-CELLULE