# Proposition E — Vérifier une propriété, pas une archive

**Pièces absentes ou partielles :** la synthèse N12–N13, le PDF Avalon, CL13–CL14 et le durcissement v50 ne sont pas servis ; les pièces 1, 3 et 4 sont des extraits ; je n’en reconstruis pas le contenu.

**Convention.** Les prescriptions et expériences ci-dessous ont le statut **HYPOTHÈSE — conception proposée**, non celui de résultats. Les seuils, tailles d’échantillon, durées et budgets nouveaux sont **illustratifs**. Une vérification documentaire ne vaut pas validation en exécution.

## Position propre

**HYPOTHÈSE — option proposée.** Séparer trois décisions :

- **admissibilité de l’exécution** : environnement, provenance et collecte conformes ;
- **validité de l’artefact** : propriété scientifique ou informatique vérifiée indépendamment ;
- **autorisation d’exploitation** : résultat utilisable, seulement exploratoire, ou mis en quarantaine.

L’option manquante est **la réexécution externe selon une spécification indépendante**, plutôt que la certification de toute l’histoire du bac producteur. Un artefact peut être correctement attribué à une exécution et scientifiquement faux ; inversement, une reproduction indépendante peut établir une propriété sans certifier chaque événement de sa production.

**HYPOTHÈSE — confiance et limite.** Confiance qualitative modérée dans cette séparation comme réduction de la circularité ; aucune estimation défendable du risque résiduel avec les pièces disponibles. Le pire cas est une défaillance commune de la spécification, du collecteur et du vérificateur, acceptée par plusieurs exécuteurs. Garde : aucun accord entre exécuteurs ne remplace un oracle indépendant de correction.

---

## A. Ce que la question suppose sans l’établir

| Supposition | Statut et objection |
|---|---|
| Le durcissement actuel permet une exécution réelle sûre. | **RAPPORTÉ :** le dossier décrit des contre-lectures et un durcissement. **VÉRIFIÉ — documentaire :** la pièce 1 déclare explicitement que v48 n’a pas exercé `bwrap` en réel. Cela ne tranche pas l’état des versions ultérieures. |
| Le déplacement du vérificateur suffit à supprimer la circularité. | **HYPOTHÈSE :** il sépare un domaine de modification, mais pas nécessairement la spécification, les dépendances, les auteurs ni la sélection adaptative sur les verdicts. |
| Des empreintes externes authentifient l’exécution. | **HYPOTHÈSE non établie :** elles identifient les octets reçus, sous confiance dans le collecteur. Elles ne prouvent seules ni leur origine, ni leur exécution, ni leur correction. |
| Le témoin public de série protège contre un producteur malveillant. | **RAPPORTÉ :** la pièce 2 lui attribue une fonction anti-confusion et anti-rejeu. **HYPOTHÈSE :** contre une source compromise capable de reprendre le témoin courant, cette fonction ne constitue pas une authentification. |
| Un journal d’appels système prouve toute l’identité d’exécution. | **HYPOTHÈSE non établie :** il faut établir sa complétude, son intégrité, son association à l’exécution et la couverture des dépendances pertinentes. Une trace ne démontre pas la sémantique du calcul. |
| La diversité d’implémentation donne une indépendance des erreurs. | **HYPOTHÈSE :** les exécuteurs peuvent partager noyau hôte, image, bibliothèques, interpréteur, oracle ou erreur de spécification. |
| Toucher un canari signifie sonder intentionnellement la plateforme. | **HYPOTHÈSE :** un accès peut être incident ; l’absence d’accès peut aussi accompagner un sondage non couvert. Le canari mesure d’abord un événement défini, pas une intention. |
| Un délai réseau dépassé établit une fermeture. | **VÉRIFIÉ — documentaire :** la sonde proposée classe le délai en « fermée ». **HYPOTHÈSE critique :** plusieurs causes compatibles avec une sortie ouverte peuvent produire ce délai ; l’attribution à une barrière n’est donc pas établie. |
| Des suites publiques peuvent certifier l’étanchéité. | **RAPPORTÉ :** aucune suite publique n’est nommée dans les faits. **HYPOTHÈSE :** une suite finie peut réfuter certaines garanties, pas établir l’absence générale d’évasion. |
| L’attestation matérielle est disponible et économiquement justifiée. | **HYPOTHÈSE :** aucune offre compatible, politique d’attestation, configuration ni tarification correspondante n’est fournie. Le devis CPX32 ne les établit pas. |

**OBSERVÉ-NON-AUDITÉ :** les essais hors machine décrits dans la pièce 2 sont indicatifs et non opposables selon leur auteur ; je ne les transforme pas en validation de la plomberie réelle.

---

## B. Architecture minimale et frontières de confiance

### Base de confiance relative à une propriété

**HYPOTHÈSE — conception proposée.** Écrire une fiche par propriété à protéger, avec adversaire, observateur, dépendances et contre-exemple admissible.

- **Pour le confinement :** matériel, hyperviseur éventuel, noyau hôte pertinent, noyau invité éventuel, moteur d’isolation, configuration effective et contrôleur de ressources.
- **Pour la provenance :** contrôleur externe, source des images, collecteur, stockage append-only administré séparément, horloge ou ordre causal externe.
- **Pour la correction :** spécification, données de référence, parseur et vérificateur. Le modèle producteur reste explicitement hors confiance.

Le poste de Lazar ne devrait pas interpréter directement une archive active provenant de la machine. La réception et le décodage doivent eux-mêmes passer par un environnement limité, sans privilège sur le poste ou le vérificateur.

**HYPOTHÈSE — distinction à auditer.** `bwrap`, gVisor, Firecracker et Kata ne sont pas des variantes interchangeables :

- `bwrap` s’appuie sur le noyau hôte ;
- gVisor interpose une interface de noyau en espace utilisateur ;
- Firecracker introduit une frontière de machine virtuelle ;
- Kata organise des charges conteneurisées dans des machines virtuelles, selon une configuration à préciser.

Une machine virtuelle change donc la frontière technique, mais ne résout ni l’erreur d’oracle ni l’apprentissage du verdict. L’inventaire exact doit être confirmé sur les versions retenues.

### Canal étroit et adaptation

**HYPOTHÈSE — conception proposée.** Recevoir uniquement un format canonique, borné, sans chemins actifs, extensions exécutables ni résolution externe. Calculer les empreintes **à la réception externe**, puis associer l’ensemble au travail attendu dans un registre non modifiable par le producteur.

Le producteur ne reçoit ni traces du vérificateur, ni diagnostics riches, ni données réservées. Taille, ordre, délai et verdict restent des canaux potentiels. Ils comptent si le producteur peut observer leur effet ou ajuster ses propositions successives ; un canal non observable par lui ne constitue pas automatiquement un signal d’apprentissage.

### Attestation : trois affirmations distinctes

**HYPOTHÈSE — conception proposée.**

- **Identité des octets :** collecte externe et empreinte.
- **Liaison à une exécution :** contrôleur externe liant image, entrée, commande autorisée et sortie ; acquisition protégée.
- **Correction :** recalcul, preuve vérifiée ou test indépendant de la propriété.

L’attestation matérielle ne doit être ajoutée que si le modèle de menace inclut un hôte ou un opérateur d’infrastructure non fiable et qu’une offre attestable couvre effectivement la charge. Elle déplace alors la confiance vers matériel, micrologiciel, chaîne de certificats et politique de vérification ; elle ne certifie pas la vérité scientifique.

---

## C. Expériences décisives : duels préenregistrés

**HYPOTHÈSE — cadre commun.** Constituer un corpus fermé, étiqueté par un arbitre indépendant, avec défauts documentaires, fonctionnels et de collecte non offensifs. Chaque cas défectueux est apparié à un cas honnête de même tâche, format, dépendances, durée et volume comparables.

Les hypothèses ci-dessous sont exclusives **sur ce corpus et cette configuration**, pas sur tous les programmes. Une exécution invalide est un échec du protocole expérimental, pas une issue favorable. Pour généraliser au-delà du corpus, publier des intervalles d’incertitude ; s’ils chevauchent le seuil, conclure « non tranché ».

| Duel | Hypothèses exclusives et métrique | Contrôle négatif | Issues falsifiantes |
|---|---|---|---|
| **Séparation contre simple déplacement** | **H_A :** le vérificateur externe accepte encore un artefact dont la propriété est fausse selon l’oracle indépendant. **H_B :** il n’en accepte aucun dans le corpus. Mesure : fausses acceptations, avec disponibilité honnête mesurée séparément. | Artefacts honnêtes appariés ; vérificateur qui refuse tout pour révéler une réussite artificielle. | Une fausse acceptation réfute H_B. Aucun cas accepté à tort réfute H_A **sur le corpus seulement**. |
| **Recalcul indépendant contre empreintes et traces seules** | **H_A :** à taux de fausses alertes ≤ **5 % illustratifs**, le recalcul gagne au moins **10 points illustratifs** de détection. **H_B :** ce critère n’est pas atteint. | Même propriété calculée correctement, notamment avec variations autorisées de représentation. | Critère atteint : H_B réfutée. Sinon : H_A réfutée. |
| **Diversité réelle contre duplication** | Comparer deux implémentations distinctes à deux exécutions du même moteur, avec mêmes tâches et budget déclaré. **H_A :** diversité = gain de détection ≥ **10 points illustratifs**, hausse des fausses alertes ≤ **2 points illustratifs**. **H_B :** non. Mesurer aussi les échecs communs. | Calculs honnêtes avec sources de non-déterminisme autorisées. | Gain conforme réfute H_B ; gain insuffisant ou trop de fausses alertes réfute H_A. |
| **Canaris contre télémétrie mécanique** | **H_A :** les canaris gagnent ≥ **10 points illustratifs** de détection d’événements interdits étiquetés indépendamment, à fausses alertes ≤ **5 % illustratifs**. **H_B :** non. | Charges honnêtes appariées avec découverte légitime de ressources et mêmes dépendances. | Critère atteint réfute H_B ; sinon réfute H_A. Aucune issue ne prouve une intention. |
| **Validité de la garde réseau** | Banc simulé ou environnement autorisé sous contrôle de l’opérateur, sans exploration de tiers. **H_A :** un état sans preuve de fermeture peut être classé « fermé ». **H_B :** aucun état de cette catégorie ne l’est. Métrique : fermetures faussement certifiées. | État réellement fermé, observé indépendamment ; état indéterminé conservé comme tel. | Un faux certificat réfute H_B ; aucun sur la matrice gelée réfute H_A sur cette matrice. |
| **Apprentissage du verdict** | Comparer évaluations répétées accessibles et évaluation finale réservée, avec mêmes ressources de proposition. **H_A :** le retour accessible accroît les fausses acceptations réservées d’au moins **10 points illustratifs**. **H_B :** accroissement inférieur. | Propositions honnêtes et condition sans retour du vérificateur. | Franchissement réfute H_B ; absence de franchissement réfute H_A pour le budget testé. |

**HYPOTHÈSE — priorité.** Le premier duel utile est celui du recalcul indépendant. S’il ne détecte rien de plus, il faut déterminer si le corpus est insuffisant ou si la spécification indépendante n’existe pas réellement, avant de financer une architecture plus complexe.

---

## D. Mesure minimale de chaque instrument

**HYPOTHÈSE — définition commune.**  
**TD** = cas défectueux signalés / cas défectueux valides.  
**FA** = cas honnêtes signalés / cas honnêtes valides.

Publier aussi refus techniques, essais ignorés et temps dépassés : aucun ne doit disparaître du dénominateur sans justification. Pour les instruments de provenance, « défectueux » signifie violation de provenance, non erreur scientifique.

| Instrument | TD et FA à mesurer ; honnêtes appariés | Vérification mécanique à battre |
|---|---|---|
| VM jetable ; noyau et bac versionnés | Détection des configurations non conformes et refus injustifiés de configurations conformes ; mêmes tâches et ressources. | Inventaire externe, contrôle de configuration effective, tests natifs. Ajouter destruction effectivement constatée. |
| Constructions reproductibles | Détection de divergences pertinentes ; faux signalements de variations autorisées. | Comparaison externe des artefacts et manifeste complet des dépendances. |
| Canal étroit et empreintes externes | Détection des violations d’intégrité ou de schéma ; rejets de sérialisations honnêtes équivalentes. | Parseur strict, limites de taille, canonicalisation, empreinte externe. |
| Vérificateur externe | TD des propriétés réellement fausses ; FA sur solutions correctes appariées. | Recalcul indépendant, contraintes de types, invariants et tests déterministes. |
| Journaux d’appels système | Détection des ruptures de collecte ou de liaison ; FA sur traces honnêtes avec ordonnancement variable. | Registre externe des travaux, contrôle de terminaison et rapprochement entrées-sorties. |
| Attestation matérielle | Détection des états non conformes à la politique ; rejets d’états autorisés. | Politique d’images signées et contrôles externes ordinaires. Mesurer fraîcheur et couverture attestée. |
| Redondance diverse | Détection supplémentaire et FA supplémentaire ; cas honnêtes numériquement sensibles. | Duplication du même moteur et même oracle indépendant. |
| Canaris journalisés | TD des événements interdits couverts, FA des accès honnêtes incidents ; pas de taux d’« intention détectée ». | Liste d’accès autorisés, télémétrie de ressources et décisions de politique. |
| Suites publiques | TD des non-conformités couvertes ; FA sur configurations officiellement supportées. | Tests du projet, configuration statique et contrôles de santé. |
| Préenregistrement et témoins | Détection des analyses non conformes au plan ; FA sur déviations explicitement permises. | Validation mécanique du manifeste, ordre causal externe, comparateur gelé. |
| Tiers reproducteur et audit | Détection des désaccords de provenance ou de périmètre ; FA sur variations autorisées. | Recalcul automatique externe des empreintes et comparaison des manifestes. L’audit doit apporter autre chose que répéter ces calculs. |

**HYPOTHÈSE — seuil canari.** Aucun seuil éliminatoire universel n’est défendable ici. Un événement explicitement interdit peut justifier une quarantaine technique ; éliminer scientifiquement la fiche exige une règle distincte. Le seuil serait choisi sur une tranche de calibration, puis gelé et évalué sur une tranche réservée.

### Suites publiques : candidats, pas certificats

**RAPPORTÉ — ressources publiques candidates, adéquation et révision à vérifier :**

- Bubblewrap, tests du projet : <https://github.com/containers/bubblewrap/tree/main/tests>
- gVisor, infrastructure de tests : <https://github.com/google/gvisor/tree/master/test>
- Firecracker, tests du projet : <https://github.com/firecracker-microvm/firecracker/tree/main/tests>
- Linux Test Project, complément pour les primitives du noyau : <https://github.com/linux-test-project/ltp>

**Référence à vérifier** pour auteurs, année, intitulé bibliographique et révision figée de chacune de ces ressources.

**HYPOTHÈSE — lecture correcte.** Je ne les présente pas comme des suites exhaustives d’étanchéité. Un expert doit sélectionner les tests défensifs pertinents, documenter leurs privilèges et leur couverture, puis consigner réussites, échecs et tests non joués. Aucun développement interne de tentatives d’évasion n’est proposé.

---

## E. Ancrage matériel, coût et ordre

### Modèles ouverts et calcul

**HYPOTHÈSE — candidats.** Qwen2.5-Coder-7B-Instruct pour produire les artefacts ; DeepSeek-Coder-6.7B-Instruct comme second producteur. Versions, licences, empreintes et disponibilité à vérifier avant sélection. Ils ne servent pas d’oracles.

**HYPOTHÈSE — dimensionnement illustratif.**

- **100 paires illustratives** par famille de défauts pour un pilote ; ce volume ne certifie pas un faible taux d’événements rares.
- Vérification mécanique sur CPU ; **8 à 16 Go de RAM illustratifs**, selon les tâches.
- Inférence quantifiée séquentielle sur GPU de **24 Go illustratifs** ; débit à mesurer avant devis ferme.
- Budget pilote : **8 GPU-heures × 1 USD/GPU-heure = 8 USD illustratifs** ; calcul externe et stockage : **5 USD illustratifs** ; enveloppe arrondie : **20 USD illustratifs**, hors travail humain.
- Audit indépendant : **une journée illustrative**, prix non estimable sans périmètre et devis.

**RAPPORTÉ — devis fourni.** La pièce 2 donne une CPX32 à **0,0577 EUR/h hors taxes**, un attendu de **0,48 USD** et un plafond proposé de **10 USD** pour son propre scénario. Ces montants ne couvrent pas automatiquement GPU, second hôte, attestation ou audit. Ses durées, conversion monétaire et fiscalité restent des hypothèses du devis.

### Ordre avant activation

**HYPOTHÈSE — plan proposé.**

1. **Spécifier la propriété et l’oracle indépendant.** Sans eux, ne pas appeler « vérification » la lecture de `RESULTAT`.
2. **Geler code, données, environnement et protocole de réception.** Administrer séparément le vérificateur.
3. **Corriger les critères d’admission ambigus**, notamment « délai ⇒ fermeture » ; conserver l’indéterminé.
4. **Éprouver la chaîne réelle**, avec témoins appariés et suites publiques sélectionnées ; pas seulement des exécuteurs factices.
5. **Comparer au socle mécanique**, puis autoriser uniquement l’usage exploratoire prévu.
6. **Mesurer ensuite** valeur marginale des canaris, diversité et journaux détaillés.
7. **Différer l’attestation matérielle** tant que son adversaire cible, sa couverture et son offre commerciale ne sont pas établis.

### Antériorités et pièce décisive

**RAPPORTÉ — références attribuables :**

- Ken Thompson, 1984, *Reflections on Trusting Trust*.
- David A. Wheeler, 2009, *Fully Countering Trusting Trust through Diverse Double-Compiling*.
- Algirdas Avizienis, 1985, *The N-Version Approach to Fault-Tolerant Software*.

**HYPOTHÈSE — portée.** La double compilation diverse concerne une relation précise entre compilateurs et sources ; elle ne justifie pas directement « deux bacs d’accord ⇒ artefact correct ». L’exécution en plusieurs versions motive surtout la mesure des défaillances communes.

**HYPOTHÈSE — pièce qui trancherait.** Un rapport externe reproductible, sur corpus réservé apparié, montrant **ce que le vérificateur détecte au-delà des contrôles mécaniques**, ses fausses alertes, ses refus techniques et les dépendances encore communes. Sans cette pièce, l’architecture reste une proposition de défense, pas un résultat de non-circularité.

FIN-DE-CELLULE