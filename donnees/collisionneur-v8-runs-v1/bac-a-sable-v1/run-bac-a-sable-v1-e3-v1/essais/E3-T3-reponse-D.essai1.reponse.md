# Proposition D — Tour III.3

Je ne réponds qu’aux sections visant D. Pièces toujours absentes ou non servies : synthèse N12–N13, PDF Avalon, CL13–CL14 et durcissement v50 ; je n’en reconstitue rien. Les corrections ci-dessous sont des **HYPOTHÈSES** de protocole, non des résultats.

## 1. Réponse aux critiques

### Critiques de A

| Critique | Décision | Correction |
|---|---|---|
| Portails à zéro exception sans effectif ; un zéro observé n’est qu’une borne. | **Acceptée.** | Les duels tranchants portent désormais sur l’**énumération exhaustive d’une banque finie gelée**, non sur un taux dans une population. Toute inférence ultérieure exigera échantillonnage, effectif, niveau et puissance préenregistrés, avec intervalles ; elle ne sera pas maquillée en duel B4. |
| E2 : résultat déterminé par le dosage des ruptures et comparateurs impossibles à battre. | **Acceptée, transformée en test.** | Strates de ruptures gelées avant exécution, résultats publiés par strate. Suppression de l’exigence « faire mieux que chaque comparateur » : une égalité est informative, et seule la détection incrémentale prévue pour une strate donnée est comptée. |
| E4 : une détection incrémentale fabricable à volonté. | **Acceptée.** | Comparateur unique choisi avant la banque finale, cas étiquetés par une référence externe, banque adversariale tenue à l’écart. La conclusion reste bornée à cette banque. |
| « Contact non expliqué » et « hors couverture » permettent des jugements a posteriori. | **Acceptée.** | Suppression des explications après alerte. Définition des contacts et carte de couverture gelées avant les résultats ; aucune reclassification après un vert ou une alerte. |
| E7 : « ses propres outils » ne définit pas une indépendance. | **Acceptée.** | Liste préenregistrée des composants devant être distincts, et de ceux pouvant rester communs — notamment l’algorithme d’empreinte. Le tiers reçoit les cas à l’aveugle. |
| E3 : tolérance temporelle non identifiable sur processeurs partagés. | **Acceptée.** | Le temps est retiré du critère binaire. Rejeux et transcriptions brutes conservés pour décrire le bruit ; aucune borne temporelle ne conditionne le portail. |
| Désaccord bibliographique sur N-version. | **Rejetée comme objection au protocole, acceptée sur la forme.** | Des titres distincts peuvent avoir des dates distinctes. Cette antériorité n’étant pas nécessaire aux expériences, je la retire du livrable plutôt que de trancher sans pièce bibliographique servie. |
| Conditions de perte de puissance et contrôles nuls. | **Acceptées.** | Banque nulle traversant tout le pipeline, ablation connue hors couverture préclassée, tiers aveugle et comparaison canaris/télémétrie seule deviennent obligatoires. |

J’accepte également le défaut transversal nommé par A : la banque finale sera constituée par une main ne connaissant pas l’instrument, puis tenue à l’écart. Le TD ne sera donc plus seulement un TD sur ce que l’auteur du détecteur savait planter.

### Critiques de B

| Critique | Décision | Correction |
|---|---|---|
| D ne teste que la provenance, jamais un artefact de provenance parfaite mais scientifiquement faux. | **Acceptée.** | Ajout d’**E8-correction** : constante déterministe, mauvais test statistique et calcul honnête, tous avec empreintes cohérentes ; vérité établie indépendamment sur données synthétiques à solution connue. |
| E3 teste le format du canal, pas l’exploitation de son contenu. | **Acceptée.** | Séparation entre **E3-canal**, simple conformité de la transcription, et **E9-signal**, qui éprouve l’effet de verdicts répétés et du matériau intergénérations. |
| E4 ne contrôle pas une défaillance commune, notamment un interpréteur partagé. | **Acceptée.** | Cas obligatoire d’erreur commune aux deux environnements, distinct des divergences bénignes. Une concordance sur ce cas interdit toute conclusion d’indépendance. |
| L’option « ne pas exécuter » contredit l’objet des tests de mort. | **Rejetée.** | C’est un repli lorsque le portail échoue, non un substitut présenté comme une vérification. Les expériences corrigées continuent de tester l’exécution ; différer évite seulement de transformer un portail non éprouvé en récompense. |
| E1 est aveugle à toute faille hors de sa liste ; E5 et E7 n’estiment rien sans loi d’échantillonnage. | **Acceptées.** | E1 est explicitement un test de conformité à une liste, dont la couverture est publiée. E5 et E7 deviennent des décisions exactes sur banque, sans prétention populationnelle. |
| Contrôles manquants : provenance correcte/correction fausse ; ablation non couverte ; exploitation du verdict. | **Acceptées.** | Ils deviennent respectivement centraux dans E8, E6 et E9. |

### Critiques de C

| Critique | Décision | Correction |
|---|---|---|
| H_A et H_B ne sont pas complémentaires lorsque TD et FA évoluent séparément. | **Acceptée.** | Dans chaque duel, H_A est maintenant la **conjonction complète** des conditions d’acceptation, spécificité comprise ; H_B est sa négation logique. Ainsi, détection positive avec FA non nulle falsifie H_A sans laisser les deux issues indécises. |
| E6 : ablations choisies en connaissant la suite, donc sensibilité vraie par construction. | **Acceptée.** | Ablations composées indépendamment de la lecture des tests de la suite, avec opérateur de lecture aveugle et strates couverte/non couverte gelées. |
| E7 ne teste que la cohérence du paquet ; une falsification antérieure au manifeste reste invisible. | **Acceptée.** | E7 est renommée et bornée à la **reproduction documentaire**. Un paquet cohérent mais forgé avant capture est obligatoire ; son acceptation documentaire ne vaut jamais validation scientifique. |
| Les modèles binomiaux rendent les critères à zéro défaut non jugeables ou asymptotiquement auto-réfutants. | **Acceptée comme conséquence d’une inférence populationnelle.** | Je supprime cette inférence des duels : décision exhaustive sur banque, puis estimations séparées si un échantillonnage défini devient disponible. |
| E3 : un maximum d’écarts temporels à queue lourde finit par franchir toute tolérance. | **Acceptée.** | Suppression du maximum temporel comme critère de verdict. |
| Contrôles manquants : substitution capture/exécution, sortie modifiée avant scellement, ablation fantôme, forge cohérente à la source. | **Acceptés.** | Ils entrent dans E2, E6 et E7. Si l’exécuteur ne consomme pas effectivement les octets capturés, E2 échoue sur sa prétention de lien, sans reclassement hors périmètre. |

### Critiques de E

| Critique | Décision | Correction |
|---|---|---|
| Banque finie : décision exacte mais portée étroite. | **Acceptée.** | C’est désormais la règle générale, avec conclusion explicitement limitée à la banque et à la configuration. |
| E2 : spécificité absente de H_A. | **Acceptée.** | H_A inclut rejets attendus **et** acceptations honnêtes ; H_B en est le complément. |
| E3 : la normalisation peut effacer l’information recherchée. | **Acceptée.** | Transcriptions brutes conservées, normalisation gelée avant lecture et champs supprimés eux-mêmes audités. Aucune égalité des lois n’est déduite d’une absence de différence observée. |
| E4 : « meilleur bac » choisi après observation ; divergence sans vérité externe. | **Acceptée.** | Comparateur figé avant la banque finale ; seules les erreurs établies extérieurement comptent comme détections. Le coût par détection devient secondaire et n’est pas calculé sur un dénominateur nul. |
| E6 : couverture auto-déclarée. | **Acceptée.** | Carte de couverture indépendante et antérieure ; les ablations hors couverture ne gonflent jamais TD. |
| E7 : outils propres insuffisants et capture conditionnée à sa consommation. | **Acceptée.** | Dépendances déclarées, tiers aveugle, et vérification mécanique que l’entrée exécutée est la capture relue. |
| Contrôles finaux et exigence B4. | **Acceptés.** | Banque réservée, variations honnêtes, traces brutes, erreurs communes, ablations préclassées et paquets concordants mais incorrects sont intégrés. Les estimations imprécises restent des estimations, non des issues de duel. |

## 2. Expériences corrigées

### Protocole commun

Pour chaque banque : auteur indépendant du détecteur, calibration séparée, banque finale gelée et tenue à l’écart, cas honnêtes appariés, banque nulle, cas plantés défensifs et règles de validité publiées avant exécution. Après gel, aucun cas n’est retiré ou reclassé.

**Règle B4 commune.** H_A est une propriété exactement décidable sur toute la banque ; H_B est sa négation. Si H_A est observée, H_B est falsifiée **sur cette banque**. Sinon, H_A est falsifiée. Un contrôle non joué compte contre le portail. Aucun résultat n’est extrapolé en taux universel.

- **E1 — Exécution réelle et portail minimal.**  
  H_A : tous les contrôles obligatoires de S0/S1 sont réellement joués et passent, les charges honnêtes restent acceptées après redémarrage, sans « ESSAI RÉEL NON JOUÉ ». H_B : au moins une clause échoue.  
  Les failles hors liste ne sont pas couvertes ; E1 ne démontre ni étanchéité générale ni non-circularité.

- **E2 — Lien capture–exécution–relecture.**  
  H_A : la capture externe, l’exécution des octets capturés, l’ancrage externe des sorties et le manifeste rejettent toutes les ruptures prévues dans les strates couvertes et acceptent tous les honnêtes. H_B : une clause échoue.  
  Sont obligatoires : substitution entre capture et exécution, modification de sortie avant scellement, journal tronqué et banque nulle. Les comparaisons avec empreinte seule, journal seul et reconstruction seule sont publiées par strate.

- **E3 — Contrat du canal, sans prétention de circularité.**  
  H_A : les transcriptions satisfont exactement le contrat gelé, y compris après inspection des champs supprimés, et aucun honnête n’est rejeté. H_B : une clause échoue.  
  Le bruit temporel est mesuré descriptivement, sans seuil décisionnel.

- **E4 — Apport de la diversité.**  
  H_A : le second environnement détecte au moins une erreur étiquetée extérieurement que manquent le bac unique présélectionné et sa duplication, sans désaccord sur les honnêtes. H_B : détection incrémentale nulle **ou** désaccord honnête.  
  Une erreur commune aux deux interpréteurs et des divergences bénignes sont obligatoires. L’accord ne vaut pas correction.

- **E5 — Canaris comme détecteurs de contact.**  
  H_A : tous les contacts définis sont journalisés, aucun honnête réservé n’alerte, et le résultat est comparé à la télémétrie sans leurres. H_B : une clause échoue.  
  La granularité — lecture, ouverture, listage — est gelée. L’absence de contact ne mesure toujours pas l’absence de sondage.

- **E6 — Sensibilité et limites des suites publiques.**  
  H_A : toute ablation préclassée couverte empêche le vert ; la configuration intacte et l’ablation fantôme restent vertes. H_B : une clause échoue.  
  Les ablations préclassées non couvertes sont publiées séparément. Un vert après l’une d’elles falsifie spécifiquement l’assertion plus forte « vert ⇒ toutes les gardes présentes ».

- **E7 — Reproduction documentaire par un tiers aveugle.**  
  H_A : le tiers reproduit les paquets honnêtes, rejette les altérations postérieures au scellement et ne révèle aucune dépendance interdite par la liste gelée. H_B : une clause échoue.  
  Un paquet forgé coherent­rement avant capture peut être documentairement concordant : il doit alors rester explicitement **non validé scientifiquement**.

- **E8 — Correction, propriété absente d’E2 et E7.**  
  Sur des données dont la réponse analytique est connue, H_A : le recalcul indépendant du plan préenregistré classe correctement tous les cas, tandis que la provenance seule accepte au moins un cas faux. H_B : une clause échoue.  
  Une fiche dont le préenregistrement ne permet pas de construire cette référence n’est pas déclarée corrigée.

- **E9 — Exploitation du signal de retour.**  
  Sur une suite figée de tâches et de politiques productrices, H_A : les retours véridiques répétés produisent au moins une acceptation fausse supplémentaire par rapport aux contrôles à exécution unique, sans retour adaptatif et à retours aléatoires de même quota ; le matériau fidèle contre matériau-bruit est testé séparément. H_B : aucun de ces effets n’apparaît dans la suite.  
  Le taux de scripts fonctionnels est publié pour ne pas confondre apprentissage du verdict et simple dégradation de la tâche.

## 3. Réponse à l’arbitre

### Ce qui est établi

- **VÉRIFIÉ documentairement** : la v48 servie n’a exercé aucun `bwrap` réel ; ses exécuteurs sont factices et ses résultats sont annoncés exploratoires. L’amorce, S0 et S1 restent à jouer.
- **VÉRIFIÉ documentairement** : l’expérimentateur reçoit des réponses entre tours, et du matériau peut servir à la génération suivante. L’hypothèse « il ne voit que le verdict final » ne décrit donc pas la chaîne servie.
- **RAPPORTÉ** : le devis v3 décrit des gardes et une machine jetable ; ses essais hors machine sont **OBSERVÉ-NON-AUDITÉ**, indicatifs et non opposables.
- **RAPPORTÉ** par la lecture vérifiée servie : Avalon formule la circularité du hachage dans le même bac. Son transfert comportemental à cet organisme reste une **HYPOTHÈSE**.
- **VÉRIFIÉ documentairement** : aucune suite publique d’étanchéité n’est nommée dans les pièces.

### Ce qui n’est pas établi

Aucun taux réel de détection, de fausse alerte ou de désaccord n’est disponible. Une empreinte externe lie des octets reçus ; elle ne prouve ni qu’ils ont été exécutés, ni que leur calcul est correct. Journal, reconstruction, diversité et reproduction tierce n’ont pas de gain mesuré ici. Les canaris ne mesurent que des contacts choisis. Disponibilité, prix et utilité d’une attestation matérielle ne sont pas établis.

### Première expérience

Geler d’abord la liste des contrôles et la petite banque indépendante, puis exécuter **E1 dans S0/S1 sur la machine réelle**, avec cas sain, gardes retirées et reprise après redémarrage. Tout contrôle non joué ou toute exception falsifie H_A et arrête l’activation ; leur réussite ne falsifie H_B que pour cette configuration et cette liste.

E2 vient ensuite, puis E8 avant de donner au portail une prétention de correction. Tant que ces maillons ne sont pas joués, les verdicts restent exploratoires, ne deviennent pas un signal de récompense, et toute issue indéterminée arrête sans repli silencieux.

FIN-DE-CELLULE