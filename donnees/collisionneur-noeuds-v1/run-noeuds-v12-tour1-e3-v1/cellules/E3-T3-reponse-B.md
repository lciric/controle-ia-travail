# Proposition B — Tour III.3 : réponse aux critiques

## Préambule

Je traite ci-dessous chaque critique adressée à ma proposition par A, C et D. Pour chaque point : acceptée, rejetée avec raison, ou transformée en test. Puis les expériences corrigées et la réponse à la question de l'arbitre.

---

## Réponses aux critiques de A sur B

### A-1. N1 — « le duel T2 est vrai par construction »

**Acceptée.** A a raison : injecter un décalage de ±2 sur la grandeur exacte que T2 mesure garantit le rejet par tautologie arithmétique. Le duel que je proposais ne teste pas si T2 détecte une pathologie pertinente pour les bras. Je retire ce duel.

**Correction** : remplacer par un duel sur deux familles d'artefacts (repris de la structure de D, en le disant) :

- **Artefact α** : modifier la fréquence du concept rare planté par statut (ce que T2 mesure directement).
- **Artefact β** : permuter la fréquence de l'étiquette *retenue* entre statuts, à concept rare planté inchangé (ce que T2 ne mesure pas, et ce que l'ancienne grandeur mesure).

H_A : T2 détecte α et ne détecte pas β ; l'ancienne grandeur (rapport sans seuil) détecte β. H_B : T2 détecte aussi β, ou l'ancienne grandeur ne détecte pas β. Issue : si T2 est aveugle à β et que l'ancienne grandeur le voit, le rapport sans seuil est justifié comme garde complémentaire. Si T2 voit β, le rapport est redondant. Si l'ancienne grandeur ne voit pas β (erreur type trop grande), aucune garde ne fonctionne et l'estimand doit être repensé. Graines : 990200–990399 (hors de toute plage déclarée), générateur scellé comme contrôle négatif. Coût : processeur seul, ≈ 50 s, 0 USD.

### A-2. N1 — « la pièce qui trancherait exécute N avant scellement »

**Acceptée.** A a raison : mesurer la corrélation entre rareté et précision de N exécute le bras candidat avant scellement, ce que la liste d'arrêt interdit (Pièce 3, l. 689–735 : « exécution d'une méthode avant scellement → arrêt »). Je retire cette pièce.

**Correction** : la pièce de remplacement est le duel α/β ci-dessus, qui n'exécute aucun bras candidat — seulement le générateur et la fonction scellée `v5_rarete`. Le témoin d1c (permis, car c'est un témoin, pas un bras candidat) peut être mesuré en complément pour vérifier si la rareté de l'étiquette retenue affecte d1c.

### A-3. N1 — « seuil d'audit 2,0 choisi après lecture »

**Acceptée.** Le seuil 2,0 est posé entre les valeurs lues (2,87 et 1,94). C'est un paramètre modifié après lecture.

**Correction** : le seuil de l'audit R4 sur l'ancienne grandeur est fixé à la valeur du seuil gelé original de V5, soit **0,5** (Pièce 3, S13 : VÉRIFIÉ). L'audit se déclenche si l'ancienne grandeur dépasse 0,5 — c'est le même critère qu'avant, mais comme déclencheur d'audit et non comme arrêt. On sait qu'il sonnera (les valeurs sont 2,87 et 1,94), mais l'audit examine si les bras exploitent la différence, et son issue est un rapport scellé, pas un arrêt automatique. Le seuil n'est pas nouveau : il est celui de S13.

### A-4. N1 — « V5 n'est pas un booléen par monde »

**Acceptée.** V5 est un écart entre moyennes sur l'ensemble des mondes, pas un taux par monde. La formulation « fausses alertes ≤ 5 % » que j'employais dans la mesure minimale n'a pas de sens pour V5.

**Correction** : la mesure minimale de V5 est reformulée. Sur 300 mondes de validation à graines neuves, T2 doit donner un écart < 0,5 pour le générateur scellé (VÉRIFIÉ par le diagnostic : 0,137 en M_bien, Pièce 2, §1.3). Sur le générateur cassé (artefact α), T2 doit donner un écart > 0,5. C'est un test à une seule réalisation par condition, pas un taux.

### A-5. N3 — « le duel confond diversité et valeur ; lier D-j à N9 est un non sequitur »

**Partiellement acceptée.** Le quartile de κ ne mesure pas l'utilité de la paire ; un κ bas peut être du bruit. Le critère « identique sur ≥ 2 lots » n'a pas d'effectif (un seul lot au pré-pilote — Pièce 9 : VÉRIFIÉ). Je retire le duel et le critère de redondance.

Sur le lien D-j / N9 : **rejetée**. Le substitut inspiré de Gu et Krenn emprunte leur *méthode* (traits de graphe, prédiction de lien), pas leur modèle ni leur graphe (Pièce 20 SD-4, §5 : VÉRIFIÉ). Mais si HB échoue sur le domaine où la méthode a été validée (optique et physique quantique), cela affaiblit l'argument analogique pour son transfert au contrôle des IA. Ce n'est pas un non sequitur : c'est une condition de confiance réduite, pas une invalidation logique. Je reformule : « si HB échoue, la confiance sur D-j = oui passe de 0,60 à 0,40 (illustratif) ; la décision reste à Lazar ».

### A-6. N4 — « condition 3 contradictoire ; mesure minimale vraie par construction »

**Acceptée sur la mesure minimale.** L'argmax bat le tirage aléatoire sur son propre score par construction. Je retire cette mesure.

**Partiellement acceptée sur la condition 3.** Le chiffre « ≈ 2 paires de niches » après retrait des trois structures est effectivement HYPOTHÈSE (non sourcé). La table canal × distance ne dépend pas de la liste des structures, donc retirer des structures ne change le profil qu'à travers la probabilité de partage, pas les paires de niches éligibles.

**Correction** : la condition 3 est reformulée. Les jeux de données ne sont pas comptés (CA1-04 acceptée). Les trois structures séquentielles (`om_somme_cumulee_temps_arret`, `om_martingale_e_processus`, `me_test_sequentiel_cusum`) restent comptées, avec une limite écrite : « ces structures sont imposées par le texte I à presque toutes les fiches ; leur partage peut refléter le plan expérimental plutôt qu'une proximité méthodologique ». La mesure de l'instrument est : sur le jeu d'essai synthétique (Pièce 11, 10 fiches, VÉRIFIÉ), le bras sélectionne une paire du profil quand il en existe une, et une paire de repli sinon — vérifié par code (Pièce 11 : 5 dans le profil, 36 hors profil, 4 refusées).

### A-7. N5 — « métrique non estimable »

**Acceptée.** Un classifieur sur les comptes de sortie à une seule exécution n'a aucun pouvoir discriminant. L'aire de 0,60 est posée sans loi de référence.

**Correction** : je retire le duel par classifieur. La garde pertinente est celle de la ligne 30 de la table R5 : l'essai R5 vérifie que le coffre journalise toute lecture et qu'une lecture non journalisée est détectée (cas sain / artefact). La question n'est pas « la sortie fuit-elle ? » mais « la lecture est-elle journalisée et bornée ? ». L'option (a) tient si les quatre conditions que j'avais posées sont remplies (journal, artefact de la ligne 30, ordre opaque d'É6, sortie sans liste triée par classe).

### A-8. N6 — critiques des duels DL

**Partiellement acceptée.** DL-1 : le duel oppose coefficient ≥ 0,70 au coefficient de M5 ; A a raison que le contraste apparié iVAE − M5 est nécessaire, pas seulement le seuil absolu. Je reformule : H_A = coefficient apparié iVAE − M5 > 0 sur ≥ 37/50 mondes ; H_B = sinon. DL-3 : A a raison que l'échec en R2⁻ peut venir de la puissance. Le duel doit comparer la puissance attendue en R2⁻ à celle mesurée, et le fond ajouté à 90 % des paires-années (Pièce 15, DL-3) doit être déclaré comme facteur de confusion potentiel. DL-5 : A a raison que 50 mondes ne séparent pas 0,01 de 0,02. Je retire le duel et retiens l'option (1) sur la base de la vérification par permutation (exacte par construction, fausse détection 0,010, Pièce 15, M §30 : RAPPORTÉ). DL-12 : VS5-01 (Pièce 18) invalide la prémisse donnée pour M1 dans l'option 1 ; je maintiens l'option 1 mais la raison est corrigée : « le centrage ne favorise plus M1 ; il peut l'handicaper ; cette limite est écrite dans la v3, et M1 est rapportée en descriptif sous centrage ».

### A-9. N10 — « ratio sans unité commune »

**Acceptée.** Le ratio performance/jailbreak n'a pas d'unité commune sans fonction d'utilité de l'attaquant. Je retire le ratio comme métrique.

**Correction** : la métrique est reformulée comme un *diagramme de Pareto* (performance de tâche, taux d'évasion) à budget d'attaque fixé, où chaque point est un niveau de couches défendues. La question « le prix est-il supérieur au gain » est remplacée par : « existe-t-il un point du diagramme où l'évasion est réduite sans perte de performance sous un seuil gelé ? ». Ce seuil doit être fixé avant exécution. La vérification hors programme reste : un groupe extérieur avec GPU et modèle ≥ 8B.

### A-10. N11 — critiques de l'oracle et du transport

**Acceptée sur l'oracle.** Le critère « au moins une fiche partageant κ > 0,3 » est trop permissif : avec 4 parents sur 10 fiches, P(au moins un parent dans la paire) ≈ 0,67 (calcul de A, VÉRIFIÉ par moi : 1 − C(6,2)/C(10,2) = 1 − 15/45 = 0,667). L'oracle ne discrimine pas les bras. **Acceptée sur le transport** : le ρ de Spearman sur 3 bras ne peut atteindre p < 0,05 (p_min = 1/6 ≈ 0,167). La condition de transport est non jugeable.

**Correction** : voir la section N11 corrigée ci-dessous.

---

## Réponses aux critiques de C sur B

### C-1. N1 — « vrai par construction » (même que A-1)

**Acceptée.** Traitée ci-dessus.

### C-2. N3 — « confusion par le dénominateur et fuite du pré-pilote »

**Acceptée.** C a raison : le pré-pilote ne comporte qu'un seul lot, et confondre la valeur marginale de κ avec la redondance des bras est une erreur. Traité ci-dessus (A-5).

### C-3. N11 — « fuite circulaire en faveur du bras basique »

**Acceptée.** L'oracle par κ > 0,3 est la fonction objectif du bras basique. Le bras méta maximise les structures partagées sous canal faible ; Gu-Krenn cherche des concepts jamais reliés (κ historique nul). L'oracle biaise la sélection par construction.

**Correction** : voir N11 corrigé ci-dessous.

### C-b1. N3 — puissance nulle du test de quartile

**Acceptée.** Sur un essai de Bernoulli unique (1 lot, 1 paire), la puissance est 0. Traitée ci-dessus.

### C-b2. N5 — puissance nulle du classifieur

**Acceptée.** Le classifieur sur comptes agrégés a une AUC identiquement 0,50 sur un run unique. Traitée ci-dessus (A-7).

### C-b3. N11 — p_min = 0,167 pour le Spearman à 3 bras

**Acceptée.** Même constat que A-10. Traitée ci-dessus.

### C-c1. Pour N1, contrôle sur N_β0 et M_inertes

**Acceptée.** Ajoutée au duel α/β : calculer la même grandeur pour N_β0 et sur M_inertes.

### C-c2. Pour N11, taux de fausses découvertes avec leurre

**Acceptée.** Intégrée dans N11 corrigé.

---

## Réponses aux critiques de D sur B

### D-1. N1 — « le générateur cassé teste exactement ce que T2 mesure » (même que A-1)

**Acceptée.** Traitée ci-dessus.

### D-2. N3 — « non-redondance mal définie »

**Acceptée.** Traitée ci-dessus (A-5).

### D-3. N4 — « validation tautologique du score »

**Acceptée.** Traitée ci-dessus (A-6).

### D-4. N10 — « ratio sans unité commune »

**Acceptée.** Traitée ci-dessus (A-9).

### D-5. N11 — « oracle trop permissif ; date de coupure SUPPOSÉ »

**Acceptée sur l'oracle.** La date de coupure fin 2025 est HYPOTHÈSE (les LLM ouverts ont des coupures variables). **Correction** : la date de coupure de chaque proposeur est déclarée au manifeste avant dépense ; les ponts plantés doivent être publiés après la plus tardive de ces dates.

### D-b. N1, N3, N5, N6, N9, N11 — conditions de puissance

**Partiellement acceptée.** Les points de D sur les estimands non identifiables (N1 : corrélation écologique), sur l'AUC appariée (N9 : son propre estimand et intervalle), et sur les corrélations intra-sous-session (N11) sont justes. Les corrections sont intégrées dans les sections corrigées.

### D-c. Contrôles négatifs

**Acceptée** pour les deux familles d'artefacts (N1), les leurres à un seul parent (N11), et les trois témoins obligatoires pour N10. Intégrés ci-dessous.

---

## N11 corrigé — Règle de reconduction et ponts plantés

**(1) La règle de reconduction**

**Grandeurs** : par bras b, sur l'oracle synthétique (bisociation v3) : taux de vrais promus (les « proches » et les « surfaces » rapportés séparément, jamais dans le numérateur du taux). Coût par vrai trouvé.

**Critère de retrait** : borne haute à 95 % de la précision du bras candidat au retrait, inférieure à la borne basse du meilleur bras, sur les mêmes mondes appariés. *Contrôle* : un bras fantôme tirant ses paires uniformément (repris de C, en le disant) ; si ce bras fantôme échappe au retrait, le critère est réfuté.

**Part minimale d'exploration** : 20 % (illustratif) des fusions de chaque génération au bras le moins performant.

**Calcul de puissance** : sur le synthétique à 2 400 mondes (Pièce 3, S15), avec σ ≈ 15 (S9), pour détecter un écart de 5 points : puissance ≈ 0,89. Pour E1′ : le nombre de ponts est inconnu (HYPOTHÈSE) ; ≥ 50 ponts nécessaires pour 10 points de précision à puissance 0,80 (calcul binomial). Pour la course 2 à 8 fusions/bras : hors de portée (puissance ≈ 0,07 pour 10 points).

**(2) Les ponts plantés**

**Source** : articles publiés après la date de coupure la plus tardive des proposeurs (déclarée au manifeste), établissant un lien entre deux sous-domaines du contrôle des IA, sélectionnés par session-depot avec PDF empreinté, hors de la vue de conv-audit (même cloison que M6b, DEP2c).

**Combien** : 4 (illustratif).

**Plantation** : chaque pont produit deux « fiches parentes » (une par sous-domaine), tronquées de toute mention du lien et de tout contenu postérieur à la date de coupure. Les fiches sont introduites dans le vivier avec un identifiant opaque. La clé des ponts est scellée avant dépense.

**Juge de correspondance** : un pont est « trouvé » par un bras si la paire sélectionnée contient les **deux** parents du pont (pas un seul — correction de la critique de A, C et D). Si les deux parents ne sont pas dans le lot non aiguillé, le pont est « non testable » pour cette sous-session, rapporté.

**Contrôles négatifs** (repris de A, C et D) : (i) leurres à un seul parent (fausse correspondance attendue = 0) ; (ii) paires à deux parents sans mécanisme commun (chimères) ; (iii) bras fantôme uniforme.

**Risque de non-ressemblance** : rapporter le rang moyen des ponts trouvés par le meilleur bras vs le bras fantôme.

**(3) Le transport**

Le test de concordance sur 3 bras est retiré (p_min = 0,167, non jugeable). Le transport est évalué de manière descriptive : le classement des bras sur le synthétique, sur E1′ et sur les ponts plantés est rapporté côte à côte. Si les trois classements divergent, aucune règle automatique ne s'applique ; la décision revient à Lazar. Si les trois convergent, c'est un argument (non une preuve) pour appliquer la règle synthétique au réel.

**(4) Effet sur le pré-pilote**

Les ponts plantés doivent être éprouvés au pré-pilote : 1 à 2 ponts, étape protégée (même cadre que M6b). La chaîne (plantation → aiguilleur → bras → fusion) est testée. Le coût est ≈ 0,5 USD (illustratif). Le protocole de sélection (qui, quand, cloison) suit DEP2c.

---

## Réponse à la question de l'arbitre : ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi

1. **N1** : V5 échoue par sa propre définition, pas par un défaut du code (OBSERVÉ-NON-AUDITÉ, Pièce 2, diagnostic sur 200 mondes avec réserves explicites). La cause est que les deux statuts « d'opérateur » ont des étiquettes de pont suivant une loi non égalisée par S16d. L'erreur type d'une différence entre statuts (0,29–0,60) est au niveau du seuil (0,5). Aucune variante du générateur permise par S16a ne passe.

2. **N4** : le pré-pilote n'éprouvera le profil du bras méta que dans une minorité de lots (zéro paire dans le profil avec 0,59–0,67 à 6 fiches, 0,25–0,36 à 10 fiches — Pièce 10, CA1-05 ; Pièce 11, §6 ; confirmé par la contre-lecture).

3. **N5** : le brouillon se contredit (A21 interdit la lecture de la clé ; É5 l'exige — Pièce 12, §C, VÉRIFIÉ). La v55 journalise les lectures par programme.

4. **N10** : dans le monde gaussien du pilote, à classe de fonctions égale (maxout à 9 unités), l'équilibre est presque pur (62 % et 54 % — Pièce 22, RAPPORTÉ) ; le levier est la capacité de la classe, pas le tirage au hasard. La défense unique ne converge pas. Bailey et al. montrent un prix de l'évasion qui croît avec le nombre de couches (Pièce 24, p. 23, RAPPORTÉ sur un seul modèle et une tâche).

5. **N-058** : la composition se juge sur l'oracle et le coût, jamais sur le verdict du juge (Pièce 26b, VÉRIFIÉ, décision scellée).

### Ce qui n'est pas établi

1. **N1** : si l'écart de rareté de l'étiquette retenue est exploitable par les bras (aucune mesure, l'exécution de N avant scellement est interdite).

2. **N3/N9** : si le substitut Gu-Krenn apporte une information non redondante pour le contrôle des IA (le vocabulaire est absent de leurs 37 960 concepts — Pièce 20 SD-4, §5, VÉRIFIÉ).

3. **N6** : si le centrage intra-strate nuit ou aide la prédiction invariante (VS5-01, Pièce 18 : la prémisse est inexacte ; effet non mesuré).

4. **N10** : si le résultat local (gaussien, linéaire/maxout) se transporte à de vrais modèles (Pièce 22 : « rien sur les vrais modèles »).

5. **N11** : si un classement des bras sur le synthétique se transporte au réel (aucune mesure ; le test de concordance à 3 bras est non jugeable).

### L'expérience à faire en premier

**Le duel α/β de N1** (deux familles d'artefacts pour T2 et l'ancienne grandeur), sur les mondes d'essai 990200–990399. Raison :

- **Il débloque tout le reste.** N1 → N11 (la règle de reconduction dépend de la bisociation v3) → N4 (si les ponts plantés doivent être éprouvés au pré-pilote). Sans résolution de N1, la v3 ne peut pas être écrite, et le gel du pré-pilote attend (D-h (a) tranché → N4 → pré-pilote).
- **Il est gratuit.** Processeur seul, ≈ 50 secondes, 0 USD, aucun LLM, aucune dépense.
- **Il est falsifiable des deux côtés.** Si T2 est aveugle à l'artefact β et que l'ancienne grandeur le voit : l'option B (T2 + rapport sans seuil) est justifiée. Si T2 voit β : le rapport est redondant, l'option A suffit. Si l'ancienne grandeur ne voit pas β non plus : aucune garde ne fonctionne, et il faut repenser l'estimand avant d'écrire la v3.
- **Il ne viole aucune règle.** Aucun bras candidat n'est exécuté. Seuls le générateur et la fonction scellée sont utilisés. Les graines sont hors de toute plage déclarée.

FIN-DE-CELLULE