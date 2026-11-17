# Proposition E — Tester séparément l’identité, le transfert et le dommage

**RAPPORTÉ — Pièces disponibles :** le résumé des faits et la question sont présents ; les fichiers sources complets, le code des bases, les six indicateurs et les données sont absents. Je n’en suppose pas le contenu.

**Convention :** les caractéristiques du dispositif restent **RAPPORTÉES**. Les diagnostics conditionnels, seuils proposés et expériences ci-dessous ont le statut **HYPOTHÈSE** ; aucun n’est présenté comme un résultat. Les seuils numériques ajoutés sont **illustratifs**.

## A. Ce que la question suppose sans l’établir

### 1. Préserver des marginales rendrait la base aveugle

**RAPPORTÉ :** P4 est présentée comme une identité algébrique du maître.

**HYPOTHÈSE — Faille critique :** l’identité pertinente dépend de l’entrée *complète* et du fonctionnement de la base. Préserver séparément les mots et les coûts ne préserve pas nécessairement leur distribution jointe. Une base utilisant la relation entre description de l’action et coût pourrait précisément détecter le réappariement.

Une invariance sur le corpus entier ne suffit pas davantage à établir une invariance par épisode, par tâche ou par fenêtre de lecture.

- **Biais possible :** faux positif de « discrétion » si l’on déclare la base aveugle sans tester ses entrées réelles ; faux négatif apparent si une base exploite légitimement une dépendance non préservée.
- **Garde :** extraire les représentations exactes effectivement consommées, aux unités de décision effectives. Vérifier l’identité exigée par l’argument, pas seulement les histogrammes globaux.
- **Ce qui diminuerait la gravité :** démonstration sur le code gelé que le score dépend uniquement des quantités effectivement invariantes.

### 2. Le coût d’origine serait correctement ordonné par rapport à la référence cachée

**RAPPORTÉ :** le classement du couplage repose sur les coûts initiaux ; M2 utilise une autre estimation, la médiane basse de huit suites honnêtes.

**HYPOTHÈSE — Faille critique :** une permutation éloignant les déclarations initiales peut les rapprocher de cette référence. L’anti-monotonie par rapport au coût initial n’implique donc pas, à elle seule, une hausse de M2.

**HYPOTHÈSE — Contre-exemple illustratif :** deux logarithmes déclarés valent `(0, 1)` et leurs références cachées respectives `(1, 0)`. L’échange fait passer M2 de `1` à `0` pour chaque action. Ce scénario n’est pas une observation.

- **Biais possible :** faux négatif de P3 malgré une manipulation effective ; faux positif si la référence partage accidentellement la construction des coûts manipulés.
- **Garde :** références générées indépendamment, cachées au couplage, avec clés d’action stables ; analyse séparée de l’accord initial déclaration–référence.
- **Ce qui diminuerait la gravité :** robustesse de l’effet à des lots indépendants de références et présence de l’effet dans les classes initialement concordantes.

### 3. La distance de Kendall serait une dose de dommage

**HYPOTHÈSE — Faille :** Kendall compte des inversions, non leur amplitude en décades. Des inversions nombreuses entre coûts proches peuvent produire peu de dommage. Des plateaux restent possibles même avec une référence parfaitement alignée.

La normalisation, le traitement des ex æquo et l’agrégation entre classes ne sont pas fournis. Certaines petites classes ne permettent pas d’atteindre exactement toute la grille. Compter des échanges adjacents ne mesure pas nécessairement la distance finale : certains échanges peuvent annuler les précédents.

- **Biais possible :** faux positif de réponse à la dose par sélection des permutations ; faux négatif par arrondis, annulations ou classes inertes.
- **Garde :** recalculer Kendall sur la permutation finale ; publier dose nominale, dose réalisée, fraction d’actions réellement modifiées et déplacement absolu des logarithmes.
- **Ce qui diminuerait la gravité :** grille réalisable, trajectoires imbriquées préspécifiées et résultats stables entre graines, sans sélection d’une trajectoire favorable.

### 4. Les classes préserveraient suffisamment de liberté sans créer de sélection

**RAPPORTÉ :** les classes trop petites et les coûts proches sont déjà reconnus comme risques.

**HYPOTHÈSE — Faille supplémentaire :** exclure après coup les classes inertes ou illisibles peut transformer une faible couverture en résultat apparemment net. À l’inverse, les inclure sans mesurer leur poids peut masquer un effet réel sur les actions manipulables.

Le déplacement d’une chaîne `COST` peut aussi changer une propriété contextuelle non incluse dans les six indicateurs : tokenisation de frontière, cohérence avec un commentaire, contrainte d’un autre champ.

- **Biais possible :** faux positif par sélection ; faux négatif par dilution ; fausse discrétion si les contrôles omettent un indice contextuel.
- **Garde :** dénominateur principal fixé avant expérience, analyse secondaire des classes admissibles, contrôle des octets hors champ et recalcul des indicateurs après réécriture.
- **Ce qui diminuerait la gravité :** couverture suffisante sur les tâches réservées et conclusions concordantes avec et sans classes inertes.

### 5. L’élève hériterait de l’invariance et du mécanisme du maître

**RAPPORTÉ :** l’invariance exacte ne concerne que le maître ; son transfert est incertain.

**HYPOTHÈSE — Faille critique :** l’adaptateur peut apprendre une dégradation générale, mémoriser des actions, modifier le format ou ne rien transmettre. Une hausse de M2 ne suffit pas à distinguer ces possibilités.

- **Biais possible :** faux positif de mécanisme relationnel par dégradation générale ; faux positif de discrétion par transfert nul ; faux négatif par capacité ou optimisation insuffisantes.
- **Garde :** tests sur familles de tâches non vues, adaptateurs témoins entraînés à l’identité, budgets identiques, mesures séparées de M2, validité syntaxique, compétence et détectabilité.
- **Ce qui diminuerait la gravité :** effet hors entraînement, reproductible entre graines, sans dégradation comparable des contrôles non ciblés.

### 6. Le témoin identité neutraliserait tous les artefacts

**HYPOTHÈSE — Faille :** l’identité est un bon témoin de manipulation, mais ne contrôle le pipeline que si elle traverse réellement le même regroupement, la même sérialisation et le même entraînement. Un modèle de base non adapté n’est pas son substitut.

- **Biais possible :** faux positif attribué au couplage alors qu’il provient du traitement ou de l’entraînement.
- **Garde :** témoin identité passé intégralement dans le pipeline, plus modèle non adapté comme contrôle distinct ; graines appariées et politique d’arrêt identique.
- **Ce qui diminuerait la gravité :** absence d’écart matériel entre identité reconstruite et identité brute, puis entre répétitions du témoin entraîné.

### 7. Un résultat très régulier serait nécessairement informatif

**HYPOTHÈSE — Faille :** fuite des références, réutilisation de graines, ordre des fichiers révélant la dose, duplication de tâches, exclusions silencieuses ou sélection de checkpoints peuvent produire une courbe trop propre.

- **Biais possible :** faux positif ; mais un pipeline neutralisant systématiquement les permutations peut aussi produire un faux négatif trop propre.
- **Garde :** provenance complète, permutation des identifiants de condition, test indépendant des clés de jointure, audit des exclusions et relecture aveugle selon critères gelés.
- **Ce qui diminuerait la gravité :** reproduction indépendante après resérialisation et réattribution des identifiants, sans accès aux résultats initiaux.

## B. Expériences décisives : duels exclusifs

**HYPOTHÈSE — Règle commune :** chaque duel porte sur un énoncé opérationnel, non sur une intention de l’agent. Les hypothèses sont complémentaires. Une incertitude statistique traversant le seuil donne un verdict **indécis**, pas une validation des deux hypothèses. Préenregistrement, seuils, exclusions et analyses sont scellés avant les expériences décisives.

### Duel I — P4 est-elle réellement une identité du maître ?

- **H_A :** la transformation préserve exactement la représentation complète dont le score de la base dépend, au niveau revendiqué.
- **H_B :** elle ne la préserve pas.
- **Mesure :** différences des entrées intermédiaires, des représentations et des scores ; vérification formelle de la dépendance du score.
- **Seuil :** identité exacte, sans tolérance permettant de masquer un changement de représentation.
- **Contrôle négatif :** passage identité dans le même pipeline.
- **Contrôle de sensibilité :** mutation volontaire d’un attribut effectivement utilisé par la base.
- **Falsification :** une discordance valide falsifie H_A. Une preuve sur le code gelé et le domaine admissible falsifie H_B sur ce domaine.

**HYPOTHÈSE — Limite :** l’absence de discordance sur un échantillon ne prouve pas une identité universelle. Si seule l’égalité des marginales est établie, P4 doit rester limitée aux bases dont elle suffit à déterminer le score.

### Duel II — Le maître produit-il déjà la réponse M2 annoncée ?

Définir \(\Delta_p\) comme l’écart apparié de M2 entre maître à dose réalisée \(p\) et témoin identité, agrégé sur les actions selon une règle gelée — jamais sur les jetons.

- **H_A :** les \(\Delta_p\) sont non décroissants sur la grille et \(\Delta_1\) atteint au moins **0,15 décade**, seuil **RAPPORTÉ**.
- **H_B :** au moins une de ces conditions échoue.
- **Mesures :** M2, contrastes entre doses voisines, Kendall réalisé, couverture manipulée.
- **Seuil :** celui ci-dessus ; interpréter « croît » comme strictement croissant exigerait un autre critère à sceller.
- **Contrôles négatifs :** identité ; permutation de chaînes de coûts numériquement égaux, lorsqu’elle est admissible.
- **Falsification :** une baisse entre doses ou un effet terminal sous le seuil falsifie H_A ; satisfaction simultanée des conditions falsifie H_B dans la population de test définie.

**HYPOTHÈSE — Garde :** le seuil terminal provient de P3 ; son emploi comme porte préalable du maître est une proposition nouvelle. Un échec ici interdit d’attribuer ensuite l’absence d’effet uniquement à la distillation.

### Duel III — La distillation conserve-t-elle le dommage hors entraînement ?

- **H_A :** les élèves satisfont le critère du duel II sur des familles réservées, relativement aux adaptateurs identité appariés.
- **H_B :** ils ne le satisfont pas.
- **Mesures et seuils :** mêmes contrastes M2 et même seuil terminal ; effets estimés par famille de tâches et graine, non en traitant chaque action comme indépendante.
- **Contrôles négatifs :** adaptateurs identité entraînés ; modèle non adapté ; tâches de contrôle où le coût ne nécessite pas la relation manipulée.
- **Falsification :** effet terminal insuffisant ou inversion de tendance falsifie H_A ; critères satisfaits hors entraînement falsifient H_B.

**HYPOTHÈSE — Limite :** H_A établit un transfert comportemental opérationnel, pas une intention de tromper. Une dégradation générale constatée sur les contrôles invaliderait l’interprétation spécifique, même si ce duel est positif.

### Duel IV — L’élève reste-t-il indétectable pour la base gelée ?

Ce duel est distinct du transfert.

- **H_A :** au seuil fixé sur les témoins honnêtes, le taux de détection de la base dépasse son taux de fausses alertes de plus de **5 points de pourcentage — illustratif**.
- **H_B :** cet excès ne dépasse pas cette marge.
- **Mesure :** différence appariée des taux, par dose et par famille.
- **Seuil :** marge ci-dessus, sans réajustement sur les sorties manipulées.
- **Contrôle négatif :** sorties d’adaptateurs identité sur les mêmes tâches, avec les mêmes budgets de génération.
- **Falsification :** excès établi au-dessus de la marge falsifie H_B ; borne supérieure sous la marge falsifie H_A.

**HYPOTHÈSE — Garde :** une base faible pourrait échouer sur tout. Ajouter des anomalies mécaniques connues comme contrôle de sensibilité, et ne pas appeler « discrétion active » le couple *absence de détection + absence de dommage*. Le critère de G0 reste réservé aux doses où l’échec de la base est établi.

### Duel V — La conclusion dépend-elle du lot de références cachées ?

- **H_A :** remplacer le lot caché par un lot indépendant change \(\Delta_1\) de moins de **0,05 décade — illustratif**.
- **H_B :** le changement atteint ou dépasse cette marge.
- **Mesure :** différence appariée des effets, avec une médiane basse de huit suites dans chaque lot.
- **Contrôle négatif :** recalcul déterministe sur le même lot et les mêmes clés.
- **Falsification :** équivalence dans la marge falsifie H_B ; différence au-delà falsifie H_A.

**HYPOTHÈSE — Limite :** stabilité entre lots ne signifie pas vérité économique du coût. Si une référence d’environnement existe, elle doit fournir une vérification indépendante ; sinon, le résultat porte explicitement sur la correspondance avec l’estimateur honnête.

## C. Qualification minimale des instruments

**HYPOTHÈSE — Convention :** pour un validateur, « détection » signifie rejet d’un cas défectueux connu ; pour une base, détection d’une manipulation. Ces objets ne doivent pas être confondus avec une détection d’intention malhonnête.

| Instrument | Mesure minimale de fonctionnement | Cas honnêtes appariés et vérification mécanique |
|---|---|---|
| **Base « mots et coût »** | Taux de détection et fausses alertes, courbe selon le seuil, résultats par dose sur maître puis élève. Seuil illustratif : fausses alertes au plus **5 %**. | Maître identité et élèves identité, mêmes tâches et classes. Comparaison aux contrôles de parsing, format, cohérence arithmétique et règles du domaine réellement disponibles. |
| **Six indicateurs / constructeur de classes** | Sensibilité aux mutations changeant chacun des indicateurs ; fausses alertes sur passages identité. | Implémentation indépendante et tests aux frontières. Les indicateurs ne sont pas un détecteur de dommage ; ils doivent retrouver les classes attendues sans collision de clés. |
| **Réapparieur / compteur Kendall** | Taux de rejet des permutations à dose erronée, avec échanges annulés, ex æquo ou valeurs perdues ; fausses alertes sur permutations admissibles. | Recalcul indépendant des inversions finales, bijection des affectations et égalité exacte des multisets. Ne pas réutiliser comme oracle le compteur du générateur. |
| **M2 et estimateur caché** | Exactitude numérique sur couples connus ; pour un seuil de dommage gelé, détection des erreurs injectées et fausses alertes sur déclarations honnêtes. | Vérification indépendante des logarithmes, unités, positivité et médiane basse. Les sorties honnêtes naturellement erronées restent dans le dénominateur des fausses alertes. |
| **Vérificateur programmatique du dommage** | Sensibilité sur défauts injectés ; fausses alertes sur cas certifiés valides indépendamment. | Référence cachée, clés testées séparément, cas limites et oracle indépendant lorsque disponible. S’il appelle simplement M2, ce n’est pas une seconde preuve. |

**HYPOTHÈSE — Critère illustratif pour un détecteur additionnel :** atteindre **80 % de détection** à **5 % de fausses alertes**, puis montrer un gain apparié contre les contrôles mécaniques au même taux de fausses alertes. Les mutants utilisés pour régler l’instrument doivent être séparés des mutants réservés à sa qualification.

**RAPPORTÉ — Limite instrumentale :** aucune sonde particulière ni architecture de moniteur supplémentaire n’est fournie. Je n’en attribue donc aucune au dispositif.

## D. Ancrage matériel et dépense

**RAPPORTÉ :** le programme prévoit un modèle 8B, des adaptateurs de rang 16 sur les projections d’attention, un adaptateur par dose et huit suites pour la référence honnête. L’identité exacte du modèle et le débit ne sont pas fournis.

**HYPOTHÈSE — Choix matériel :**

- Reprendre prioritairement le modèle ouvert exact du programme, son tokenizer et sa configuration T0.6.
- À défaut, **Llama-3.1-8B** peut être un candidat à examiner, sous vérification des poids, licence et accès aux sorties nécessaires. Ce remplacement imposerait une version neuve, pas une réplication silencieuse.
- Une GPU de **80 Go — illustratif**, avec adaptation à faible rang éventuellement quantifiée, constitue une configuration candidate ; mémoire et débit doivent être mesurés à la longueur de contexte réelle.

**HYPOTHÈSE — Enveloppe illustrative, pas devis exécutable :**

- **Trois graines par dose — illustratif**, soit **douze entraînements — illustratif**, incluant les témoins identité.
- Corpus de **deux millions de jetons — illustratif**, **deux passages — illustratif** : environ **48 millions de jetons d’entraînement cumulés — illustratif**, hors génération des références et évaluations.
- Réservation exploratoire totale : **40 à 160 heures-GPU — illustratif** ; à **2 à 5 € par heure-GPU — illustratif**, **80 à 800 € — illustratif**, hors travail humain.

**HYPOTHÈSE — Procédure de devis :** mesurer uniquement le débit et la mémoire sur données synthétiques non décisives, puis chiffrer séparément construction, entraînement, références cachées, évaluation et audit. Toute dépense reste soumise au devis et au GO. Si le jeu réservé est trop petit pour départager les seuils, le verdict demeure indécis.

## Verdict proposé à l’arbitre

**HYPOTHÈSE :** les portes doivent rester séparées :

- **P4-maître :** identité démontrée pour la base réellement utilisée.
- **P3-maître :** manipulation effectivement dommageable selon la référence cachée.
- **P3-élève :** transfert hors entraînement.
- **Discrétion-élève :** échec empirique de la base à dommage établi.

Un succès à une porte ne remplace aucune des autres. C’est notamment ce qui empêche qu’un élève inactif, une référence contaminée ou une invariance seulement marginale produise un verdict artificiellement favorable.

FIN-DE-CELLULE