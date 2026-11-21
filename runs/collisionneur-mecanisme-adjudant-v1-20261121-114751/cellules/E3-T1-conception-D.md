# Proposition D — Adjuger le droit de publier, pas l’intention de l’agent

## 1. Point de départ et suppositions non établies

**RAPPORTÉ —** Le programme règle ses seuils à 1 % de fausses alertes sur des épisodes honnêtes. Ce chiffre désigne un réglage, pas une mesure indépendante par régime. L’arbitre Lean 4 est en préparation ; aucun résultat d’épreuve n’est fourni.

**HYPOTHÈSE —** Un spécialiste commencerait utilement par éprouver la stabilité des sondes : même tâche, autres formulations, autres difficultés, sabotage tenu à l’écart. Ce n’est pas l’adjudant demandé. Je partirais plutôt du contrôle qualité à la réception : *si je ne sais rien de fiable sur le fournisseur, qu’est-ce que je peux néanmoins autoriser à entrer dans le stock ?* L’unité à contrôler devient la modification apportée au fonds de résultats validés, non le jeton suspect.

| Ce que la question risque de présupposer | Statut et objection |
|---|---|
| Toute sortie du domaine d’étalonnage laisse une trace reconnaissable. | **HYPOTHÈSE.** Un changement de relation entre trace et dommage peut ne changer aucune trace observable. |
| Deux instruments de nature différente ont des pannes différentes. | **HYPOTHÈSE.** Une sonde et un vérificateur de produit peuvent tous deux ignorer une erreur de spécification. Il faut compter les **doubles manqués**. |
| Le produit du travail possède une propriété vérifiable qui importe au commanditaire. | **HYPOTHÈSE.** Une preuve du mauvais énoncé est le cas décisif, pas une preuve syntaxiquement invalide. |
| Le dommage passe par une interface contrôlable et se mesure dans une unité pertinente. | **HYPOTHÈSE.** Borner le nombre de fichiers publiés ne borne pas le coût scientifique d’une conclusion fausse. |
| Le jumeau dit honnête, les pièges et les mondes plantés représentent des témoins fiables. | **HYPOTHÈSE.** L’honnêteté ne garantit ni compétence ni indépendance ; une vérité plantée ne couvre que les propriétés plantées. |

## 2. Données à conserver avant tout calcul de taux

**HYPOTHÈSE — protocole proposé.** Pour chaque tâche, consigner avant exécution : demande originale, énoncé effectivement vérifiable, conséquences autorisées, identifiant du régime et raisons de son inclusion dans l’étalonnage. Pendant l’épisode, conserver les versions exactes des artefacts, prédictions et engagements horodatés, opérations demandées, autorisées et effectivement commises, assignations aléatoires, réponses séparées des copies et du jumeau. Pour les instruments internes seulement : lectures indexées par événement et position prédéclarés, sans moyenne ni médiane sur les jetons.

**HYPOTHÈSE — séparation cruciale.** Garder hors de l’exécuteur le registre de vérité : propriété demandée, propriété effectivement satisfaite, dommage réalisé, caractère honnête ou planté et famille. Une erreur honnête reste honnête. Consigner séparément « alarme de sabotage », « produit refusé » et « travail honnête empêché » : refuser à raison un produit faux d’un agent honnête n’est pas détecter une attaque.

## 3. Instruments : mesure minimale et duels

**HYPOTHÈSE — convention expérimentale pour toutes les lignes ci-dessous.** Geler chaque instrument, seuil compris, avant ouverture de la famille tierce. Apparier chaque cas planté à un épisode honnête sur *le même énoncé*, avec même modèle, outils, budget, difficulté et stade de décision ; inclure désaccords et erreurs honnêtes. Comparer à calcul égal ; à défaut, publier le surcoût. Le contrôle négatif supplémentaire figure dans chaque ligne.

**HYPOTHÈSE — duel commun, appliqué séparément à chaque instrument.** Sur le registre scellé, mesurer par régime les fractions brutes \(d=\#\text{cas cibles signalés}/\#\text{cas cibles}\) et \(f=\#\text{témoins signalés}/\#\text{témoins}\), avec numérateurs et dénominateurs. Pour B, les cibles primaires sont les épisodes dommageables **manqués par la sonde gelée** ; publier aussi \(d\) sur tous les épisodes dommageables et le tableau croisé des deux verdicts. Pour A, les cibles sont des régimes tenus à l’écart, y compris honnêtes ; les témoins sont des épisodes honnêtes *du domaine validé*. Mesurer séparément si la sonde perd réellement en qualité sur le régime signalé.

**HYPOTHÈSE — seuil et falsification.** \(H_A\) : sur ce banc fini, \(f\leq1\,\%\) dans chaque régime témoin et \(d\) dépasse strictement celui du comparateur mécanique admissible le plus performant, choisi sur développement au même plafond. \(H_B\) : négation. Franchir les deux barrières réfute \(H_B\) sur le banc ; manquer l’une réfute \(H_A\). Un dénominateur vide rend le duel non évaluable. Donner les incertitudes sur des tâches indépendantes, sans compter les copies comme de nouvelles tâches. Avec peu de témoins, même un duel gagné peut ne pas établir un taux de population inférieur à 1 %.

| Instrument et mesure au point de décision — **HYPOTHÈSES de conception** | Suppose ; panne attendue | Contrôle négatif spécifique ; vérification mécanique à battre |
|---|---|---|
| Précurseur de valeur et dissonance : tester séparément l’alarme avant l’acte et la contradiction valeur/action à l’acte. | Valeur interne lisible et liée au dommage ; surprise légitime ou acte nuisible jugé normal. | Replanification honnête après information imprévue ; variation de récompense externe et règle sur l’action interdite. |
| Lecture mécaniste : motif de calcul prédéclaré ; mesurer aussi si une intervention localisée change la décision prédite. | Motif causal transportable ; une autre procédure peut produire la même décision. | Intervention témoin de même ampleur sur composant non candidat ; règle sur la trace d’outils et contrôle du produit. |
| Nouveauté sans étiquette d’attaque : rang de non-conformité du manifeste externe de la tâche parmi les manifestes honnêtes. | Distance pertinente, témoins comparables ; nouveauté sémantique à manifeste inchangé. | Renommage sans changement de régime ; simple liste des versions, types et permissions déjà validés. |
| Vérification du produit : certificat contre énoncé fixé **par le demandeur**, refus avant publication. | Contrat fidèle et vérificateur de confiance ; propriété omise. | Preuve honnête non canonique ; compilation, tests publics et vérification du seul énoncé livré par l’agent. |
| Redondance : comparer les conséquences vérifiables de productions isolées, non leur prose. | Diversité des erreurs ; erreur commune à toutes les copies. | Solutions honnêtes distinctes mais équivalentes ; exécutions répétées du même contrôle déterministe. |
| Jumeau honnête : écart sur des obligations identiques, à informations égales. | Jumeau compétent ; désaccord honnête ou angle mort partagé. | Paire honnête/honnête ; comparaison de chaque produit à la spécification sans jumeau. |
| Pièges : défaut constaté sur une obligation de vérité scellée avant exécution. | Obligation représentative ; le comportement évalué peut différer du comportement courant. | Même insertion avec obligation satisfaite ; tests fixes de non-régression à même coût. |
| Dire/faire/prédire : engagement préalable sur une conséquence mesurable, puis rapprochement avec le journal effectif. | Conséquence informative ; discours et acte cohérents mais tous deux nuisibles. | Révision honnête explicitement enregistrée ; rapprochement simple entre entrées, sorties et journal. |
| Intervention causale externe : randomiser une condition dont l’effet sur le résultat est spécifié *avant* la tâche ; contrôler le contraste attendu. | Intervention isolable, relation pertinente ; deux résultats faux peuvent respecter la relation. | Intervention factice sans effet attendu ; répétition inchangée et test individuel des sorties. |

**VÉRIFIÉ — filiations, identifiants arXiv : pas sûr.** George C. Necula, 1997, *Proof-Carrying Code* : déplacer la charge de preuve chez le producteur et vérifier côté receveur. John H. Saltzer et Michael D. Schroeder, 1975, *The Protection of Information in Computer Systems* : médiation complète et moindre privilège. Vladimir Vovk, Alexander Gammerman et Glenn Shafer, 2005, *Algorithmic Learning in a Random World* : utiliser les rangs sous échangeabilité.

**HYPOTHÈSE — transposition supplémentaire de la comptabilité d’engagement.** À chaque autorisation, réserver immédiatement une provision sur un budget global de conséquences, consommée au *commit*, jamais recréditée sur simple déclaration de l’agent. Contrairement à une pénalité de récompense, une provision insuffisante empêche matériellement l’effet. La provision doit majorer l’effet réel ; c’est là que le pont peut casser.

## 4. Ce que permettent les mathématiques

**VÉRIFIÉ — limite d’identification.** Si \(P\) et \(Q\) sont les lois des observations accessibles en régime honnête et dommageable, pour toute région d’alarme \(S\),
\[
Q(S)\le P(S)+\|Q-P\|_{\mathrm{TV}}.
\]
Cela découle de la définition de la variation totale. Si ces lois coïncident, augmenter la sensibilité exige d’augmenter autant les fausses alertes. Changer de capteur n’établit pas que les lois diffèrent.

**VÉRIFIÉ — distinction de garanties.** Sous échangeabilité du prochain épisode honnête avec les épisodes d’étalonnage et avec un score fixé indépendamment d’eux, un test de rang conforme donne une borne marginale de fausses alertes sans spécifier de loi paramétrique. Avec \(n\) témoins, la plus petite valeur \(p\) conforme non randomisée usuelle est \(1/(n+1)\). Ni puissance contre l’inédit, ni validité par sous-régime, ni robustesse à une sélection adaptative des épisodes n’en découlent. À l’inverse, « ce manifeste manque au registre » est vérifiable sans hypothèse statistique, mais ne signifie pas « cette sonde se trompe ».

**VÉRIFIÉ — borne conditionnelle sans détection.** Si chaque effet externe passe par une porte atomique, si son incrément de dommage est majoré par son débit \(c_i\geq0\), et si la porte maintient \(\sum_i c_i\le B\), alors le dommage cumulé ainsi défini ne dépasse pas \(B\), quelle que soit la politique de l’agent. **HYPOTHÈSE non acquise —** trouver de tels débits pour le dommage scientifique en aval. À défaut, annoncer seulement la grandeur effectivement bornée, par exemple les modifications non certifiées du dépôt protégé.

## 5. Arbitrage indépendant et ancrage matériel

**HYPOTHÈSE —** Un tiers choisit après gel une famille par *supposition violée* : contrat incomplet, erreurs communes, ou régime nouveau à manifeste familier. Il garde les vérités et les témoins honnêtes hors de l’exécuteur. Publier les empreintes du protocole, les tables appariées après levée d’aveugle et les refus de produits honnêtes. Une autre équipe reproduit les décisions à partir des journaux, puis répète le duel avec de nouvelles tâches. Un banc public sert de contrôle de reproductibilité, **pas** de famille restée secrète : pour des énoncés Lean publics, miniF2F, référence à vérifier. Une preuve Lean de l’invariant budgétaire porterait sur la machine abstraite ; il reste à confronter chaque voie d’écriture réelle à cette machine.

**HYPOTHÈSE — devis illustratif, non mesuré.** Premier banc : un modèle à poids ouverts de la famille Qwen2.5-Coder, variante 7B (nom de variante), inférence locale quantifiée, jumeau en exécution séquentielle, CPU pour la porte et le vérificateur. Enveloppe **illustrative** pour un pilote court : GPU de 24 Go, 12 heures-GPU à 2 €/heure, soit 24 € hors travail humain. Mesurer d’abord jetons, durée, mémoire des lectures internes et temps de vérification sur une tâche ; ne pas confondre ce pilote avec l’effectif nécessaire pour valider 1 %. Pour tester la porte seule : rejouer des transactions enregistrées, sans inférence.

## 6. Demande reformulée

**HYPOTHÈSE — cahier des charges proposé.** « Sur quelle modification irréversible du travail de recherche pouvez-vous prendre une décision vérifiable *avant* qu’elle prenne effet ? Montrez, sur des tâches et familles scellées par un tiers, ce que vous empêchez quand la sonde se tait, ce que vous bloquez à tort, et ce qui reste borné quand votre propre verdict est faux. Indiquez l’interface hors de laquelle votre promesse cesse. »

## 7. Mécanismes classés par priorité d’essai

**HYPOTHÈSE — priorité C : dépôt en quarantaine avec porte de commit provisionnée.** L’agent travaille librement dans un brouillon ; lui seul ne peut pas promouvoir un résultat dans le dépôt validé. La porte exige une autorisation indépendante et débite atomiquement chaque effet permis. **Supposition / menace :** médiation complète ; un effet important hors dépôt échappe à la promesse. **Sans dépense :** tracer à la main tous les chemins du brouillon au résultat consommé. **Duel fatal :** sur famille tierce de conséquences non modélisées, \(H_A\) : aucun dépassement du budget déclaré et le flux honnête autorisé aboutit ; \(H_B\) : au moins une de ces conditions échoue. Rejouer transactions honnêtes, comparer à une simple permission d’écriture ; une violation tue \(H_A\), le respect exhaustif réfute \(H_B\) sur le registre seulement. Rapporter refus utiles et refus honnêtes, sans les appeler détections d’intention. **Delta / chances :** la médiation n’est pas nouvelle ; l’apport testé est le choix d’une unité de dommage auditable. Confiance raisonnable pour un dépôt fermé ; je ne sais pas pour l’influence scientifique aval.

**HYPOTHÈSE — priorité B : réception sur obligation indépendante.** Le demandeur fixe à l’avance l’énoncé et les dépendances admises ; le producteur joint un certificat. Le receveur vérifie le lien exact entre demande, énoncé et produit plutôt que la seule validité interne du certificat. **Supposition / menace :** ce lien exprime l’objectif ; une omission de l’objectif résiste à la preuve. **Sans dépense :** comparer manuellement demande et énoncé sur un résultat existant. **Test fatal :** duel « vérification du produit » ci-dessus, sur famille tierce d’écarts entre propriété prouvée et propriété utile, restreinte aux manqués de la sonde. **Delta / chances :** ce n’est pas un nouveau système de preuves ; le contraste avec le Lean envisagé est la propriété imposée au receveur et le moment du refus. Plausible sur des sous-tâches formalisées, inconnu sur une recherche ouverte.

**HYPOTHÈSE — priorité A : passeport d’étalonnage avec abstention explicite.** Joindre à chaque verdict de sonde le manifeste des conditions réellement éprouvées. Si la couverture manque, afficher « non validé » sans accuser l’agent ; tester le rang de nouveauté comme extension, pas comme substitut au registre. **Supposition / menace :** les descripteurs externes portent les changements pertinents ; une innovation à descripteurs constants peut rester invisible. **Sans dépense :** tenter de rattacher un verdict archivé à ses témoins exacts. **Test fatal :** duel « nouveauté » sur famille à manifeste familier ; si le rang ne bat pas la liste au plafond de fausses alertes, abandonner le score, garder la traçabilité. **Delta / chances :** ni le rang ni le registre ne sont nouveaux ; c’est le droit d’interpréter un verdict local qui est testé. Bonne perspective pour constater des lacunes documentaires ; je ne sais pas détecter par ce moyen une nouveauté sans empreinte observable.

FIN-DE-CELLULE