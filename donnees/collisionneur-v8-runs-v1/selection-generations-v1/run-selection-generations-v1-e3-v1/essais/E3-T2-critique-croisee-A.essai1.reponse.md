# Proposition A — Tour III.2 : critique croisée de méthode

**Conventions.** Les pièces servies sont RAPPORTÉES ; leurs chiffres d'exécution sont OBSERVÉS-NON-AUDITÉS (je n'ai rien rejoué). Tout ce que j'avance sur les conceptions B à E est une analyse : statut HYPOTHÈSE sauf mention. Tout nombre nouveau est **illustratif**. Aucune pièce transmise n'est absente ou coupée ; le code `pont_v1.py` n'est pas servi, je ne lui attribue rien. Notation commune : m = nombre de lois jugées dans une génération, N = effectif d'épreuve, α = 0,05, seuil e-BH log(m/α), KL = divergence par épisode entre la loi testée et le nul informé ; la richesse log W d'une loi vraie croît en espérance comme N·KL (sous indépendance des épisodes, HYPOTHÈSE de régime).

Un défaut traverse les quatre textes et je le dis une fois : plusieurs duels H_A/H_B ne sont pas exhaustifs (zone d'issues où aucune des deux n'est réfutée) et aucun texte sauf E ne nomme cette zone « indécis ». Je le signale par duel plutôt que de le répéter.

---

## Sur la proposition B

### (a) Défauts de méthode

- **E1 (dents du pôle)** — *Vrai par construction / fuite* : les « témoins vrais » de la banque sont, d'après pièce 7 § a.3 (RAPPORTÉ), « confirmés sur une moitié du développement ». Un témoin vrai sélectionné parce qu'il passe sur le développement est optimiste par sélection ; E1 mesure alors la puissance sur des effets choisis pour être visibles, pas la puissance sur un effet de force nominale. *Confondant* : « force ≥ 0,5 » (vocabulaire de la couche 1 bis) et « log-rapport de cotes 0,6 » (pièce 7 § a.4) sont deux paramétrisations ; B les emploie comme si elles se répondaient sans conversion.
- **E3 (conjonction)** — *Confondant* : les tests de mort s'exécutent sur des données locales ou de développement (pièce 1 § 9.2), le pôle sur l'épreuve. Un ensemble de survivantes discordant entre les deux filtres peut refléter la différence des données, pas la non-redondance des filtres. B ne sépare pas « même donnée, filtres différents » de « données différentes ».
- **E4 (fuite)** — *Estimateur mal défini* : le ratio W_fille(partagée)/W_fille(fraîche) porte sur des log-richesses qui peuvent être négatives (pièce 4 : log W −135 sous le nul des filles, OBSERVÉ-NON-AUDITÉ). Un ratio de quantités signées change de sens selon le signe du dénominateur. Le « contrôle » (W_mère aussi gonflé) est circulaire : il confirme la fuite par la fuite.
- **E5 (ablation)** — *Non-comparabilité des issues* : dans le bras « sans pôle », « survivante » signifie « notable chez les juges-modèles » ; dans le bras « avec », « promue par le juge figé ». Les deux numérateurs ne mesurent pas la même chose ; sans épreuve finale commune aux deux bras (ce que D et E proposent, je m'en sers en le disant), le ratio ne compare rien.
- **E6 (mémoire)** — *Vrai par construction* : si la signature prédictive inclut le signe (c'est le cas si elle est calculée sur la loi, pièce 2 § 1.8), une « opposée » a une empreinte différente par définition. Le cas difficile n'est pas le signe inversé mais la même loi sur une population ou un moniteur voisin, ou deux lois différentes de même sortie sur la sonde.
- **Statuts** : B étiquette « VÉRIFIÉ » des résultats de simulation (pièce 6) qu'il n'a pas rejoués. Ce sont des OBSERVÉS-NON-AUDITÉS ; règle 1.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1** : seuil log(m/α) avec m = 20 → ≈ 6 nat (illustratif). Puissance nulle dès que N·KL < 6, soit KL < 0,021 nat par épisode à N = 288. Si l'effet du témoin est déjà capté par le prédicteur « connu » (KL → 0 après conditionnement), la loi est **non jugeable**, non « fausse ». Décision sur 5 témoins : si la probabilité de promotion vaut 0,3 par témoin, P(0 sur 5) ≈ 0,17 (illustratif) — H_A est réfutée à tort une fois sur six.
- **E3** : avec 10 fiches et p(survie TdM) ≈ p(promue) ≈ 0,1, l'espérance du nombre de fiches discordantes est de l'ordre de 1 ; la différence |S_filtre| − |S_conj| est un entier 0–2, variance de Poisson : non jugeable sous ces effectifs.
- **E4** : la variance de log W sous le nul croît avec N ; comparer une épreuve partagée de N₁ et une fraîche de N₂ sans normalisation confond l'optimisme avec N₁/N₂. Estimateur jugeable : différence (log W_partagée − log W_fraîche)/N, bornée en espérance sous le nul par log m / N (illustratif ; à démontrer).
- **E5** : test exact de Fisher à 10 par bras : différence minimale détectable ≈ 0,5 (illustratif) ; si le taux réel de reclassement est 0,2, puissance de l'ordre de 0,15. Ratio par euro avec 0 à 2 survivantes : variance relative non bornée.
- **E6** : seuils 0,8 et 0,2 sur n = 10 : intervalle binomial ≈ ±0,25 ; les seuils tombent presque toujours dans l'intervalle → indécis. Il faut n ≥ 40 par classe (illustratif) pour séparer 0,8 de 0,5.

### (c) Contrôles négatifs dont l'absence est fatale

- E1 : loi « connu + 0 » (effet nul sur le même moniteur) jugée en même temps que le témoin vrai, pour vérifier que le nul informé absorbe le connu ; sans elle, une promotion peut récompenser une redite du connu.
- E3 : fiche dont la prédiction est vraie sur le développement mais sans épreuve disponible — elle doit sortir « différée », pas « éliminée » ; sans ce témoin, la conjonction compte l'absence de banque comme une mort.
- E4 : lois figées sans retour intergénérationnel (aucune sélection), jugées sur les deux épreuves — c'est la seule base du ratio sous le nul.
- E5 : témoins faux « rhétoriquement conformes » (classe C de pièce 1 § 6) plantés dans le bras sans pôle ; s'ils y sont « notables », la métrique de B les compte comme survivantes.
- E6 : paire « même loi, vocabulaire disjoint » (doublon prédictif sans doublon lexical) ; l'absence rend la garde textuelle invisible.

---

## Sur la proposition C

### (a) Défauts de méthode

- **E1 (architecture de survie)** — *Résultat vrai par construction* : les 5 « témoins de couche 3 » exigent par définition un trait absent de la banque ; le bras 1 (conjonction stricte, rejet de la sortie 2) ne peut pas les promouvoir, quel que soit le pôle. L'issue « bras 1 à 0/5 sur la couche 3 » qui réfute H_A est garantie avant l'expérience. Ce duel compare deux conventions administratives, pas deux hypothèses sur le monde (B4 non respecté : H_A et H_B peuvent être fausses ensemble, R_V ∈ ]0,40 ; 0,80[). *Fuite* : la pondération e-BH « par richesse a priori du test de mort » emploie un score calculé sur les mêmes fiches ; valide seulement si les données du test de mort sont indépendantes de l'épreuve et si Σw_i = m est fixé avant lecture — C ne l'écrit pas.
- **E2 (fuite)** — *Confondant* : dans un monde nul, l'inflation du FDR sous épreuve fixe dépend de la capacité de l'opérateur de recombinaison à exploiter le bit de survie. Un résultat « FDR ≤ 0,06 » peut signifier « l'opérateur est faible », non « la réutilisation est sûre ». La borne O(k log M/N) est posée sans dérivation (HYPOTHÈSE présentée en formule).
- **E3 (héritage négatif)** — *Confondant* : le bras « contexte complet » a un prompt plus long ; un effet sur la diversité peut tenir à la longueur, pas au contenu. « Mêmes graines de température » sur Kimi et Argon : aucune pièce ne rapporte un contrôle de graine sur ces API ; la réplication appariée est supposée.
- **E4 (ablation)** — *Confondant principal* : le bassin P (5 meilleures au pôle) est par construction un sous-ensemble des fiches traduisibles (sortie 1) ; le bassin J (5 meilleures aux juges-modèles) peut contenir des fiches non traduisibles. Les filles de J échouent davantage au pont, et le « bras pôle » gagne par testabilité, non par vérité. Il manque un bras à parents tirés au hasard parmi les admissibles. *Estimateur biaisé* : la métrique Nats/$ somme (log W − log(m/α)) sur les seules promues — c'est un excès conditionnel à la promotion (malédiction du vainqueur), systématiquement positif même sous le nul.
- **Tableau (c), ligne 2** : témoins vrais des tests de mort « exacts par construction sur les données de développement » ; le test de mort les confirme alors par construction, et le taux ≥ 0,80 ne mesure rien.
- **Attribution fautive** : C identifie le modèle de 8 milliards de la banque à « llama-3.1-8b » en citant pièce 10 § 3. Pièce 10 cite ce modèle comme celui d'un papier externe (2609.36490), pas celui de la banque T0.5. Aucune pièce servie ne nomme le modèle de la banque. C présente une inférence comme un fait VÉRIFIÉ : règle 1 et 3.
- **Statuts** : plusieurs « VÉRIFIÉ » sur des lectures non rejouées (pièces 4, 5, 6, 7) ; même remarque que pour B.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E1** : pour un témoin de couche 1 à log-cotes 0,6 sur 300 épisodes, pièce 7 § a.4 (RAPPORTÉ, approximation dite optimiste) demande ≈ 150 épisodes seul et ≈ 300 avec 17 lois : le témoin est au bord du seuil ; R_V oscille entre 0,4 et 0,8 par le seul bruit d'échantillonnage. e-BH pondéré : si les poids w_i sont corrélés aux e-valeurs sous le nul, le FDR n'est plus contrôlé ; condition à vérifier : Cov(w_i, log W_i | nul) = 0.
- **E2** : séparer FDR = 0,05 de FDR = 0,10 avec 100 courses : écart type ≈ 0,025, intervalle ±0,05 : les deux seuils (0,06 et 0,10) se recouvrent presque toujours → indécis. Il faut ≈ 400 à 800 courses (illustratif) ; faisable en simulation seulement.
- **E3** : différence de 20 points sur 20 fiches par bras : écart type ≈ 0,15 ; puissance de l'ordre de 0,3 (illustratif). D_JS sur une sonde grille à peu de points sature vers log 2 et ne discrimine plus.
- **E4** : 5 parents, 20 filles, promotions attendues 0 à 3 par bras : « au moins 2 fois plus » distingue 1 de 2 — loi de Poisson, non jugeable. Nats/$ : si les coûts diffèrent d'un ordre de grandeur entre couches (C le dit lui-même), le ratio est piloté par le dénominateur.
- **Ligne 6 du tableau** : rappel ≥ 0,85 sur 10 hypothèses masquées : 8/10 et 9/10 ne se distinguent pas de 0,85.

### (c) Contrôles négatifs dont l'absence est fatale

- E1 : un bras 1 où la couche 3 est comptée « différée » ; sans lui, le résultat est une tautologie.
- E2 : un opérateur de recombinaison adversarial (oracle sur les bits de survie, cas pire) dans le monde nul ; sans lui, « sûr » ne vaut que pour l'opérateur courant.
- E3 : archive de même longueur mais hors sujet (E le propose ; je le reprends) ; sans elle, l'effet de longueur reste confondu.
- E4 : bassin J restreint aux fiches traduisibles, et bassin aléatoire parmi les admissibles ; sans ces deux bras, le pôle ne peut pas être distingué de la testabilité ni du hasard. Un monde où toutes les fiches sont fausses, pour mesurer le taux de « promotions » par bras sous le nul.
- Tableau ligne 3 : la base « Mann-Whitney + Holm » doit tourner sur les mêmes épisodes et le même nul informé ; sinon la comparaison « pari séquentiel contre test fixe » confond méthode et données.

---

## Sur la proposition D

### (a) Défauts de méthode

- **E1** — *Vrai par construction* : H_A (« toutes les fiches peuvent recevoir immédiatement les deux tests ») est déjà fausse d'après les pièces (épreuve T0.5 lue, tests de mort jamais activés ; RAPPORTÉ). Le duel est tranché avant d'être joué ; il ne mesure que le pont, ce que D pourrait dire tel quel.
- **E2** — *Appariement impossible* : « mêmes fiches initiales, mêmes proposeurs » sur des modèles d'API non déterministes n'est pas un appariement ; et « banque réelle fraîche » n'existe pas. Le seuil « borne supérieure sous 0,05 » n'est pas chiffré en effectif.
- **E3 et E4** — *Fuite instrument / évaluation* : la métrique « familles nouvelles confirmées » repose sur une canonisation (empreinte de loi, arbre syntaxique) qui est **la mémoire elle-même**, c'est-à-dire l'un des instruments comparés. Le bras « mémoire minimale » est évalué avec son propre compteur de familles. Il faut une canonisation tierce, gelée, indépendante des deux bras.
- **E5** — *Bras « sans pôle » non spécifié* : comment ses parents sont-ils choisis ? Sans règle, le bras est un bras libre. *Multiplicité asymétrique* : à coût total égal, le bras sans pôle économise les traductions et passe plus de fiches à l'épreuve finale ; sous le nul, il obtient ≈ α·m_final fausses confirmations, proportionnelles à m_final — il « gagne » par multiplicité. D doit contrôler le FDR séparément par bras sur l'épreuve finale.
- **Trois états** : « différée hors population reproductrice » est raisonnable, mais produit une dérive de lignée vers la testabilité (E le nomme comme pire cas) ; D ne propose aucune mesure de cette dérive.
- Quasi-absence de nombres : acceptable pour une conception, mais chaque duel est **non jugeable tel qu'écrit** ; je le compte comme défaut de méthode plutôt que comme prudence.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E2** : montrer que FDR ≤ 0,05 avec une borne supérieure d'intervalle à 95 % exige, pour un FDR vrai de 0,03, environ 1 000 campagnes nulles (illustratif) ; sur 100 campagnes, 5 fausses promotions donnent une borne ≈ 0,11 : H_A est réfutée par le seul manque d'effectif. Ce duel ne peut être joué qu'en simulation massive.
- **E3, E4, E5** : les comptes de familles sont de petits entiers (loi de Poisson de moyenne λ ≤ 3, illustratif) ; une différence de 1 n'est jamais significative ; le rendement par euro ajoute la variance du coût. Condition de jugeabilité : λ par bras ≥ 10 ou réplication par populations indépendantes ≥ 10 (illustratif).
- **E4** : « part maximale d'une lignée » est une statistique d'ordre très instable à petite population (5 à 20 fiches) ; sa distribution sous allocation uniforme doit être calculée avant de parler de collapse.
- **E5** : l'épreuve finale contrôle le FDR par bras seulement si m_final est connu par bras et si le seuil est log(m_final/α) **par bras** ; sinon, le bras le plus prolifique domine.

### (c) Contrôles négatifs dont l'absence est fatale

- E1 : témoins « aller-retour » T1/T2 (déjà en pièce 7 § g) ; D s'y réfère, fine.
- E2 : campagnes 100 % nulles en nombre suffisant (≥ 1 000 en simulation, illustratif).
- E3/E4 : paires « même loi, lexique disjoint » et « lexique commun, lois distinctes » **évaluées par un canoniseur tiers**, pas par la mémoire testée.
- E5 : bras à parents tirés au hasard parmi les admissibles ; monde où toutes les fiches sont fausses pour mesurer les fausses familles confirmées par bras ; témoins plantés **dans l'épreuve finale** elle-même.

---

## Sur la proposition E

### (a) Défauts de méthode

E est le texte qui sépare le mieux réfutation et indécision ; les défauts sont ailleurs.

- **Organisation statistique** : « admissibilité d'abord (test de mort sur données distinctes), puis e-BH sur toutes les admissibles » n'est valide que si les données du test de mort sont indépendantes de l'épreuve. Si tests de mort et épreuve tirent dans le même vivier de tâches (N-049), une dépendance par tâche existe ; E pose le problème du sous-ensemble final mais ne traite pas celui de l'admissibilité.
- **Duel « pont fidèle »** : les altérations sont écrites par le concepteur ; le pont (gardes de traçabilité, pièce 7 § d) attrape par construction les altérations numériques. La mesure de p_erreur dépend donc de la part d'altérations non numériques (population, unité, quantificateur) dans le banc, que E ne fixe pas. *Couverture* : E la demande mais ne la met pas dans le duel ; un pont qui renvoie tout a p_erreur = 0.
- **Duel « fuite »** : G est une différence de « performances » sur une « échelle gelée » non nommée. Si l'échelle est log W, elle n'est pas comparable entre épreuves d'effectifs différents ; si c'est une exactitude, elle ne reflète pas ce que le juge mesure. L'unité de réplication (lignée randomisée) est bonne mais le nombre de lignées n'est pas dimensionné.
- **Duel « filtre »** : conditionner les deux bras sur l'admissibilité corrige le confondant de C ; je m'en sers. Défaut : δ_utile « fixé selon le coût opérationnel » rend H_A/H_B exclusives par convention et non par contenu ; le duel teste une décision, pas une loi — acceptable si dit, et E le dit à moitié.
- **Duel « archive »** : frontière Δ = 0 « définitionnelle ». Avec des comptes de confirmations entiers et petits, un intervalle « entièrement positif » ou « entièrement non positif » n'arrive presque jamais ; H_B (Δ ≤ 0) est en pratique irréfutable. Le duel est honnête mais stérile tel que dimensionné.
- **Garde de diversité** — *fuite instrument / évaluation* : les « familles prédictives » sont définies par la même canonisation (arbre syntaxique, mécanisme) que celle qu'utilise la recombinaison ; la couverture D mesure alors l'instrument avec sa propre règle. Le contrôle « catégories permutées » le corrige partiellement, pas pour la définition des catégories.
- **Pire cas** (dérive vers les lois faciles à traduire) : bien nommé, non mesuré. Une mesure existe : corrélation entre le code de sortie du pont à la génération g et la survie de la lignée à g + 2.
- Noms de modèles ouverts donnés de mémoire avec réserve explicite : conforme à la règle 3 ; je n'ajoute rien.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **p_erreur ≤ 5 %** : borne haute à 95 % sous 5 % avec 0 erreur observée exige n ≥ 60 fiches altérées (règle de trois, illustratif) ; avec les 16 fiches du premier essai de pièce 7, le duel est indécis quelle que soit l'issue.
- **G** : sous le nul, l'optimisme de la sélection du meilleur parmi m est de l'ordre de log m en richesse, soit log m / N par épisode (illustratif) ; à m = 20, N = 150 : ≈ 0,02 nat par épisode. Un seuil G = 0,05 sur une autre échelle n'est pas rattaché à cet ordre de grandeur ; il faut exprimer G en nat par épisode ou recalculer le seuil.
- **Δ (filtre, archive)** : différence de deux Poisson de moyennes λ₁, λ₂ ; pour réfuter Δ ≤ 0 avec λ₁ = 2λ₂ = 2 par population, il faut ≈ 15 populations indépendantes par bras (illustratif). Sans ce dimensionnement, le résultat est « indécis » par construction.
- **D (couverture)** : si le nombre de catégories K excède le nombre de confirmations, la couverture est bornée par le second et ne mesure plus la garde.

### (c) Contrôles négatifs dont l'absence est fatale

E les a presque tous (paraphrases, lois figées, vivier sans relation aptitude–fécondité, archive hors sujet, catégories permutées). Les absences :

- **Contrôle positif de puissance** dans le duel « filtre » : un vivier avec une lignée féconde plantée de force connue, qui doit être détectée ; sans lui, un Δ indécis est indiscernable d'un dispositif aveugle, et « indécis » devient une sortie éternelle.
- **Vivier entièrement nul** (toutes les fiches fausses) dans les duels « filtre » et « archive » : le « vivier sans relation » n'est pas un vivier nul ; il faut connaître le nombre de fausses confirmations par bras sous le nul.
- **Témoins plantés dans l'audit final** lui-même ; sans eux, l'audit « jamais utilisé » peut être sans dents sans qu'on le sache (c'est le cas documenté de la couche 1, pièce 5, RAPPORTÉ).
- **Fiche à deux nombres** (le pont choisit le mauvais) dans le duel « pont fidèle » : la traçabilité ne la détecte pas, puisque les deux nombres sont cités.

---

## Ce que je retiens des quatre, en le disant (B1)

Je reprends d'E l'audit final commun et le conditionnement des bras sur l'admissibilité ; de D l'épreuve finale supplémentaire ; de C le monde nul en simulation pour la fuite (mais à 10 fois plus de courses et avec un opérateur cas-pire) ; de B rien que je n'aie déjà, sauf E6 refait avec des paires « même loi, lexique disjoint ». Aucun des quatre ne dimensionne ses duels ; sous les effectifs écrits, la plupart sont indécis avant lecture, et deux (C-E1, D-E1) sont tranchés avant lecture.

FIN-DE-CELLULE