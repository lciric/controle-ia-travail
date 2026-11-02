# Proposition E — Tour III.3 : corrections et décision proposée

**Pièces absentes ou partielles :** la synthèse N12–N13, le PDF Avalon, CL13–CL14 et v50 restent non servis ; les pièces factuelles signalées comme extraits ou expurgées restent telles quelles.

**Convention de statut.** Toutes les décisions de conception, interprétations critiques et expériences proposées ci-dessous sont **HYPOTHÈSE**, non des résultats. **VÉRIFIÉ — documentaire** désigne uniquement ce qui est lisible dans les pièces servies. Aucun nouvel essai n’a été exécuté. Tout paramètre numérique nouveau serait **illustratif** ; je retire ici les anciens seuils numériques insuffisamment justifiés.

## A. Réponse aux critiques visant E

### Critiques de A

| Critique | Décision et correction |
|---|---|
| **a.1 et a.6 — Oracle confondu avec vérificateur ; indépendance indéfinie.** | **Acceptées.** Trois rôles deviennent distincts : définition de la propriété, réalisation du vérificateur, établissement des étiquettes de référence. Les dépendances communes sont déclarées. Une équipe séparée ne suffit pas à rendre une spécification indépendante. |
| **a.2 — Canaris dominés par une télémétrie complète.** | **Acceptée sous cette prémisse.** Je retire la promesse de détection supplémentaire d’un événement déjà intégralement observé et correctement classé. Le test portera sur l’utilité opérationnelle d’ajouter les canaris à une télémétrie concrète, dont les limites seront explicites. |
| **a.3 — Issue du test réseau connue par lecture du code.** | **Acceptée.** Le contre-exemple devient un contrôle de régression, non une découverte empirique annoncée. |
| **a.4 — Petits modèles non représentatifs ; quotas mal alignés.** | **Acceptée.** Les producteurs ouverts proposés précédemment sont retirés du test principal. Celui-ci utilisera le modèle effectivement autorisé, avec les quotas et retours de la version déployée. |
| **a.5 — “Non tranché” incompatible avec B4.** | **Acceptée sur mon protocole ; remède proposé partiellement rejeté.** Aucun effectif fini ne garantit qu’un intervalle évitera un seuil lorsque le paramètre réel en est proche. Je sépare désormais un duel exhaustif sur une banque finie d’une estimation populationnelle, qui ne saurait être forcée à conclure. |
| **b — Saturation, discordances appariées, faible adaptation, calibration rare.** | **Acceptées comme conditions de fragilité**, pas comme résultats établis pour notre système. Les anciens gains uniformes sont retirés. Les effets seront ventilés par famille et les discordances publiées. Un effet nul à faible budget ne réfutera aucune capacité future. |
| **c — Oracle aveugle, “accepte tout”, producteur non adaptatif, honnête sur données nulles.** | **Transformées en contrôles obligatoires.** Le bras non adaptatif garde le même modèle et budget ; une température nulle ne sera pas assimilée à une garantie de reproductibilité. |

### Critiques de B

| Critique | Décision et correction |
|---|---|
| **a.1 et b — Seuils abstraits et puissance insuffisante.** | **Acceptées sur le défaut de justification ; rejetées comme calcul universel d’effectif.** Les effectifs et puissances avancés dépendent des discordances, du regroupement et de l’alternative choisie. Ils ne dimensionnent pas à eux seuls notre comparaison appariée. Aucun de mes anciens effectifs ne reste une exigence confirmatoire. |
| **a.2 — Retirer les retours empêche aussi le débogage.** | **Acceptée.** Tous les bras reçoivent les mêmes diagnostics techniques autorisés. Seul le retour d’évaluation ciblé varie. Le taux de scripts exécutables est une mesure principale distincte. |
| **a.3 — Qui écrit la spécification et à quel coût ?** | **Acceptée sur la lacune.** Je propose un catalogue restreint de contrats de calcul relus, sélectionnés avant production. Une fiche hors catalogue exige un contrat supplémentaire ou reste sans validation sémantique. **Rejetée** : le caractère nécessairement prohibitif du coût humain n’est pas établi par les pièces. Il doit être mesuré. |
| **a.4 — Réception trop abstraite.** | **Acceptée.** Le poste transporte un objet opaque ; aucune décompression sur son environnement ordinaire. Le décodage se fait dans un environnement de réception jetable, séparé du vérificateur et de ses données réservées. |
| **c.1 et c.2 — Référence tierce et qualité sans retour.** | **Acceptées**, intégrées aux expériences corrigées. |
| **c.3 — Canal temporel non testé.** | **Acceptée sur l’absence.** **Rejetée comme contrôle suffisant** : un verdict invariant malgré un délai modifié ne prouve pas que le producteur n’observe pas ce délai. Il faut examiner la transcription réellement accessible au producteur. |

### Critiques de C

| Critique | Décision et correction |
|---|---|
| **a.1 — Oracle supposé disponible ; avantage sémantique artificiel.** | **Acceptée sur la disponibilité et le comparateur.** Empreintes et traces deviennent un socle de provenance, non le concurrent principal d’un vérificateur sémantique. **Rejetée** : disposer d’un contrat de calcul n’abolit pas le rôle du producteur, qui peut encore proposer l’hypothèse, choisir un contrat admissible et produire l’artefact. Cela ne couvre toutefois pas les fiches arbitraires. |
| **a.2 — Calibration possiblement incluse dans l’évaluation.** | **Acceptée.** Conception, calibration et évaluation sont disjointes pour tous les réglages, pas seulement les canaris. |
| **a.3 — Réseau : résultat déterministe.** | **Acceptée.** Je retire ce duel dans sa forme initiale. **Rejetée** : les réserves du devis ne démontrent pas que toutes les ambiguïtés causales du délai avaient été couvertes. |
| **b.1 — Intervalles chevauchant les seuils.** | **Acceptée sur le problème.** Les calculs transmis restent des illustrations, non des observations. La correction B4 est décrite ci-dessous. |
| **b.2 — Refus techniques et dénominateur.** | **Acceptée sur la nécessité de clarification.** Le dénominateur principal est l’ensemble assigné. Refus technique, détection sémantique et acceptation erronée sont des issues distinctes ; un refus n’est pas crédité automatiquement comme une détection. |
| **c.1 — Contrat ambigu.** | **Transformée en test obligatoire.** Une ambiguïté réservée doit entraîner une abstention motivée, non une interprétation silencieuse favorable. |
| **c.2 — G8 entière, pas seulement la sonde.** | **Acceptée.** L’audit porte sur la conjonction entière et distingue déclaration de configuration, observation des flux et conclusion autorisée. |
| **c.3 — Placebo à quota égal.** | **Acceptée.** Le placebo conserve format, calendrier et budget ; sa construction est gelée avant l’essai. |

### Critiques de D

| Critique | Décision et correction |
|---|---|
| **a — Erreurs communes de l’oracle ; mélange des défauts.** | **Acceptées.** Étiquetage audité séparément ; résultats par strate ; aucun gain global ne sera calculé avec des poids choisis après observation. |
| **a — Sur-appariement et calibration insuffisamment séparée.** | **Acceptées.** Apparier sur tâche et ressources autorisées, non sur les comportements potentiellement discriminants. Les mesures de durée et volume restent des résultats, pas nécessairement des contraintes d’appariement. |
| **a et b — Opportunités différentes et sélection des seuls cas valides.** | **Acceptées.** Budgets identiques, mesure avant retour et analyse sur tous les cas assignés. |
| **b — Dépendances entre cas, erreurs d’étiquettes, faible prévalence.** | **Acceptées.** L’unité de regroupement est la tâche source ; les variantes ne deviennent pas artificiellement des observations indépendantes. La valeur prédictive ne sera pas annoncée sans prévalence cible défendable. |
| **c — Défaut commun, réserve, placebo, faux résultat partagé, accès incidents, ouvert silencieux.** | **Transformées en contrôles obligatoires.** Un défaut commun indétecté doit apparaître comme limite, jamais comme réussite obtenue par concordance. |

## B. Expériences corrigées

### Règle commune : portée finie, sans faux verdict statistique

**HYPOTHÈSE — correction B4.** Chaque duel porte d’abord sur **une banque finie gelée et une configuration fixée**, évaluées intégralement. Ses hypothèses sont un prédicat observable et sa négation exacte. Chaque issue falsifie donc l’une des deux hypothèses **sur cette banque seulement**.

Cela ne constitue pas une estimation de sécurité générale. Les intervalles éventuels décrivent une généralisation séparée, sous une loi d’échantillonnage explicitée ; leur chevauchement ne sera ni caché ni transformé en réfutation populationnelle.

**HYPOTHÈSE — garanties communes :**

- auteurs des cas réservés privés du code des détecteurs ; auteurs des détecteurs privés des cas réservés ;
- contrat, coûts, métriques, strates et règles d’abstention gelés avant ouverture ;
- conservation de tous les cas assignés, y compris refus, pertes et dépassements ;
- échec de collecte globale : expérience invalide, qui réfute sa capacité d’exécution annoncée, mais ne tranche pas artificiellement son duel scientifique ;
- aucun résultat d’évaluation utilisé pour retoucher le détecteur puis annoncer une réussite sur la même banque.

### Expérience première — Existe-t-il un contrat vérifiable sans le producteur ?

**HYPOTHÈSE — objet.** Avant d’évaluer l’architecture, éprouver sa prémisse manquante.

Une équipe rédige les contrats à partir des fiches et données autorisées, sans lire les scripts producteurs. Une autre construit le vérificateur. Une troisième prépare une banque réservée comprenant :

- calculs à réponse exacte contrôlable séparément ;
- analyses honnêtes conduisant à une conclusion scientifique négative ;
- résultats faux mais reproductibles et de provenance cohérente ;
- contrats volontairement ambigus ou incomplets ;
- erreurs plantées dans le vérificateur ou sa référence ;
- défaut sémantique commun à plusieurs implémentations.

Les étiquettes et leur justification sont auditées avant de servir. Toute tâche dont l’étiquette reste contestée est explicitement une tâche d’abstention, non une vérité terrain forcée.

**H_A :** tous les cas réservés reçoivent l’issue exigée par leur contrat — validation, rejet ou abstention — dans le budget gelé.

**H_B :** au moins un cas n’y satisfait pas.

- Banque conforme : **H_B réfutée**, uniquement pour les contrats testés.
- Erreur ou budget dépassé : **H_A réfutée** ; la classe concernée n’est pas admissible automatiquement.

Les témoins « accepte tout » et « refuse tout » vérifient que ni permissivité ni refus systématique ne peuvent satisfaire le contrat.

**Limite assumée :** cet essai n’élimine pas toute erreur de spécification. Il expose la dépendance restante au lieu de la qualifier d’indépendance acquise.

### Expérience suivante — Valeur marginale du recalcul et de la diversité

**HYPOTHÈSE — comparaisons séparées.**

- Recalcul spécialisé contre un vérificateur sémantique mécanique de référence.
- Moteurs distincts contre répétition du même moteur, à budget comparable.

Les empreintes et manifestes sont communs aux bras : ils ne servent plus de concurrent sémantique artificiellement faible. La banque comprend des défauts communs et des variations bénignes ; les tolérances viennent exclusivement de la calibration séparée.

Pour chacune des comparaisons :

**H_A :** sur la banque réservée, la méthode ajoutée corrige au moins une décision erronée du comparateur, sans introduire de nouvelle décision erronée ni dépasser le plafond de ressources gelé.

**H_B :** cette conjonction n’est pas satisfaite.

- Dominance observée selon ce critère : **H_B réfutée**.
- Absence de gain, nouveau dommage ou coût excessif : **H_A réfutée**.

Un comparateur déjà parfait peut faire échouer H_A : cela signifie précisément « aucun besoin marginal démontré sur cette banque », pas « méthode inutile partout ». Les comptes par famille et les discordances restent prioritaires sur un score agrégé.

### Expérience suivante — Effet du retour, à opportunités égales

**HYPOTHÈSE — protocole.** Utiliser le producteur effectivement autorisé et les quotas effectifs de l’orchestrateur. Les diagnostics de syntaxe, terminaison et dépendances sont identiques entre bras.

Comparer :

- retour d’évaluation fidèle ;
- retour placebo, sans information utile sur la correction, mais de même format et calendrier ;
- absence de retour évaluatif ;
- propositions préparées sans adaptation.

Les budgets de propositions, exécutions et temps sont égaux. L’évaluation finale est réservée. Mesurer séparément fonctionnalité, conformité du calcul et acceptations scientifiquement erronées.

**H_A :** sur l’ensemble gelé de trajectoires, le retour fidèle produit davantage d’acceptations erronées finales que chacun des bras placebo et sans retour, selon la marge décisionnelle préenregistrée.

**H_B :** cette condition n’est pas satisfaite.

Chaque issue réfute son complément sur ces trajectoires. L’absence d’effet ne réfute ni l’exploitation future d’un autre canal ni celle d’un producteur plus capable.

### Expérience suivante — Canaris : ajout utile ou information redondante ?

**HYPOTHÈSE — protocole.** Comparer télémétrie seule et télémétrie avec canaris, avec politiques de décision gelées. Les références réservées incluent accès incidents, événements interdits couverts et événements hors couverture.

**H_A :** l’ajout satisfait un critère préenregistré d’amélioration opérationnelle — correction supplémentaire ou réduction de coût de décision — sans nouvelle élimination injustifiée.

**H_B :** non.

Chaque issue réfute son complément. Si la télémétrie seule détecte et classe déjà tous les contacts, le résultat attendu peut être une simple redondance : aucune détection d’« intention » n’en sera déduite.

### Expérience suivante — Réception et canal réellement visible

**HYPOTHÈSE — réalisation.** Le poste transporte des octets opaques. Un environnement jetable décode sous limites de ressources et n’émet vers le vérificateur qu’un schéma canonique borné. Le vérificateur recalcule l’empreinte reçue ; ni archive, ni chemins actifs, ni script producteur ne sont interprétés dans son environnement privilégié.

Le banc fait varier séparément contenu admissible, taille, ordre et calendrier de livraison. L’observateur enregistre **ce que voit effectivement le producteur**, pas seulement le verdict final.

**H_A :** toutes les variations hors contrat sont soit neutralisées dans la transcription visible, soit rejetées explicitement, tout en acceptant les témoins admissibles.

**H_B :** au moins une viole cette règle.

Chaque issue réfute son complément. Ce contrôle établit une conformité de canal, pas l’absence universelle de canal caché.

### Correction réseau préalable, hors duel de découverte

**VÉRIFIÉ — documentaire :** le code servi classe un délai dépassé comme « fermée ».

**HYPOTHÈSE — correction proposée :** un délai seul devient « indéterminé ». Tester cette branche est une régression déterministe. L’épreuve d’intégration examine ensuite G8 entière, avec ses contrôles de configuration et un observateur indépendant autorisé, notamment dans un état ouvert mais silencieux. Aucun trafic d’exploration ni tentative d’évasion n’est proposé.

## C. Réponse à l’arbitre — une page

### Ce qui est établi

**VÉRIFIÉ — documentaire :** la pièce v48 décrit des tests exploratoires, un préenregistrement, un scellement et une lecture mécanique de `RESULTAT`. Elle déclare ne pas avoir exercé le bac réel. Cela ne tranche pas les versions ultérieures.

**RAPPORTÉ :** le dossier décrit des contre-lectures, un durcissement et le choix d’une machine jetable sans secret. Le devis servi ne constitue pas la réalisation de cette infrastructure.

**VÉRIFIÉ — documentaire :** les empreintes, le témoin de série et les journaux sont des éléments de la plomberie proposée ; aucune pièce servie ne fournit une démonstration de correction scientifique indépendante pour chaque fiche.

### Ce qui ne l’est pas

**HYPOTHÈSE — diagnostic :** déplacer le vérificateur retire une possibilité de modification directe seulement si collecteur, réception et administration sont effectivement séparés. Cela ne supprime pas les erreurs communes de spécification ni l’adaptation aux verdicts.

**HYPOTHÈSE — périmètre de confiance :** distinguer confinement, provenance et correction. Les dépendances nécessaires à chacun entrent dans sa base de confiance ; le producteur et son auto-déclaration de réussite en sont exclus. Une frontière de machine virtuelle modifie le confinement, pas la validité scientifique.

**HYPOTHÈSE — limite d’attestation :** empreintes externes et traces ne suffisent pas, seules, à établir toute l’histoire d’exécution. L’attestation matérielle éventuelle exige un adversaire cible, une couverture et une offre vérifiées ; elle n’est pas un préalable démontré ici.

**HYPOTHÈSE — limites instrumentales :** accord entre moteurs, canaris et suites publiques sont des observations de couverture définie, pas des certificats généraux. Les canaris ne mesurent pas directement l’intention.

### L’expérience à faire en premier

**HYPOTHÈSE — décision proposée :** commencer par **l’expérience du contrat vérifiable**, sur une classe restreinte de fiches, avant d’ajouter diversité, canaris ou attestation.

L’enjeu est concret : peut-on produire, avant de voir le script agent, un contrat et un vérificateur qui distinguent calcul correct, résultat faux reproductible et fiche sous-spécifiée ? Si non, l’architecture ne dispose pas encore de l’objet qu’elle prétend vérifier. Si oui, elle possède une capacité bornée à cette classe, à éprouver ensuite dans la chaîne réelle.

### Ordre et dépense

**HYPOTHÈSE — ordre :** contrat et référence séparée ; réception isolée ; correction des conclusions ambiguës de G8 ; validation réelle du bac ; puis comparaison marginale des instruments. L’activation reste exploratoire et conditionnée à ces admissions.

**RAPPORTÉ :** le devis fournit un attendu de **0,48 USD** et un plafond proposé de **10 USD** pour son scénario propre ; ses hypothèses de durée, fiscalité et conversion restent des hypothèses. Aucun de ces montants ne couvre automatiquement le nouveau vérificateur ou l’audit.

**HYPOTHÈSE — enveloppe illustrative :** réserver **20 USD illustratifs** de calcul au pilote, hors travail humain, sans le confondre avec un devis ferme. Mesurer d’abord le temps de rédaction et de contrôle d’un contrat.

**RAPPORTÉ — candidats publics, adéquation à vérifier :** tests [Bubblewrap](https://github.com/containers/bubblewrap/tree/main/tests), [gVisor](https://github.com/google/gvisor/tree/master/test), [Firecracker](https://github.com/firecracker-microvm/firecracker/tree/main/tests). **Référence à vérifier** pour attribution bibliographique et révision figée. Leur sélection défensive et leurs tests non joués doivent être documentés ; aucun succès ne sera intitulé « étanchéité prouvée ».

FIN-DE-CELLULE