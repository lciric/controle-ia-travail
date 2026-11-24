## 4. Contenu visé, selon la cible

**Version courte (atelier, piste courte, prépublication).** Le manuscrit de base suffit : deux théorèmes, leurs remarques, la remarque sur les procédures. Aucun théorème nouveau n'est requis. Restent, sans dépense, les préalables de diffusion de la section 7.1 : corrections de références portées ; antériorité lue sur PDF ; affirmations attribuées à Price, Robertson et Fisher lues sur PDF ; traces internes retirées ; billet et page de dépôt vérifiés ; règles des appels lues. Trois phrases sont proposées au correctif du manuscrit : le rejet pur comme filtre de sortie ; l'agrégation par classe, exacte sous rejet pur et simple borne sous pénalité ; le régime des pièges, vide quand leur support est disjoint de celui des épisodes ordinaires.

**Version longue (revue, conférence principale).** S'y ajoutent, selon la cible et après contre-lecture finale de chaque brouillon :
- la dynamique en temps fini, complétée d'une proposition sur l'effet instantané de la pénalité, géométrie par géométrie (gradient euclidien, gradient naturel). Ce n'est pas une prédiction unique du modèle : le signe dépend de la géométrie (section 8.1) ;
- la normalisation par groupe, une fois le cas avec ancre écrit et contre-lu ;
- la géométrie du découplage de l'audit ;
- le budget d'audit, avec sa remarque sur la marge ; la marge resserrée selon la section 6 ;
- une expérience sur modèle réel, si Lazar l'ouvre.

**Extensions proposées par la v2 et non faites.** La transition continue par la méthode de Laplace et les pièges à rapport de densité borné n'ont été ni dérivés ni contre-lus dans le dépôt. Les deux formules de la v2 passent un contrôle d'une ligne, refait par le contre-lecteur ; ce n'est pas une preuve. Elles restent des options de la version longue.

---

## 5. Trois points soumis à Lazar

Ce sont des nœuds de décision : aucun défaut ne s'applique après 48 heures. Rien n'est engagé d'ici le mot de Lazar.

### (a) Viser d'abord un atelier non archivistique — SOUMIS À LAZAR

**Décision demandée.** La première cible du manuscrit théorique est-elle un atelier non archivistique d'une des trois grandes conférences d'apprentissage automatique (Conference on Neural Information Processing Systems, International Conference on Machine Learning, International Conference on Learning Representations) ?

**Enjeu.** Le choix fixe le calendrier, les règles d'anonymat à respecter, le sort du billet, et dit si une expérience payante est nécessaire avant une première soumission. Il commande aussi trois dépendances : la borne resserrée de la marge d'audit, la citation de Lean, l'entrée des sections longues.

| Option | Avantage | Inconvénient |
|---|---|---|
| 1. Atelier non archivistique d'abord, avec le manuscrit de base ; conférence principale ensuite, seulement si une expérience montre la bascule de signe au seuil prédit | Les trois modèles y placent le manuscrit, indépendamment, dès le premier tour. Coût nul. Retours de relecteurs du domaine. Laisse ouvertes les soumissions ultérieures, si la règle de l'appel le confirme. | Prestige faible. Calendrier subordonné à l'existence d'un atelier adapté, inconnue aujourd'hui. Les trois modèles n'ont vu qu'un résumé. Règles citées de mémoire. |
| 2. Revue à évaluation continue d'abord (Transactions on Machine Learning Research), avec le manuscrit de base | Pas de calendrier. Publication archivée. Permettrait le billet, selon la voie séparée de Carbon. | Les modèles divergent : Neon juge l'algèbre trop élémentaire pour cette revue. Une théorie déjà archivée pourrait obliger ensuite à un article expérimental autonome : cela dépend des règles de double soumission, à vérifier. Durée d'évaluation non vérifiée. |
| 3a. Conférence de l'Institute of Electrical and Electronics Engineers sur l'apprentissage automatique sûr et digne de confiance (Secure and Trustworthy Machine Learning), en piste courte, avec le manuscrit de base, si cette piste existe | Public naturel du modèle de menace. Aucune expérience requise selon Opus, qui y place le manuscrit actuel ; Carbon préfère cette conférence, Neon la donne en alternative. Publication en conférence. | L'existence de la piste courte n'est pas vérifiée, ni son échéance. Si elle est archivistique, elle pèse sur une soumission ultérieure du même fond en conférence principale : à vérifier. Un seul modèle la place pour le manuscrit en l'état. |
| 3b. Attendre une expérience et viser directement la piste principale d'une grande conférence, ou de la conférence de l'option 3a | Un seul article, le plus fort possible. Pas de morcellement. | Dépend d'une expérience ni scellée ni financée, dont la prédiction est bilatérale. Retarde toute prise de date. Les trois modèles jugent la conférence principale hors d'atteinte sans cette expérience, et incertaine avec. |

**Recommandation.** Option 1, la revue à évaluation continue restant le repli si aucune expérience n'est ouverte. L'option 3a est sa rivale directe : elle ne peut être classée face à l'option 1 qu'une fois son appel lu. **Confiance : moyenne, environ 0,6**, abaissée depuis la v3 parce que l'option 3a, omise alors, n'est pas départagée. Elle repose sur un accord de trois modèles qui n'ont pas lu le manuscrit, et sur des règles non vérifiées. Aucune probabilité d'acceptation n'est avancée : il n'en existe aucune qui soit fondée.

**Préalable, quelle que soit l'option.** Lire l'appel de l'année de chaque cible : existence, date, statut archivistique, anonymat, règle sur les prépublications et les billets, double soumission, limite de pages. Consigner la page lue, sa date et son empreinte. Si un appel de l'année n'est pas encore paru, consigner celui de l'année précédente, marqué « indicatif », non opposable ; la décision peut alors être prise sous réserve.

### (b) Le banc de code à niches de triche construites, sur devis — SOUMIS À LAZAR

**Décision demandée.** Ouvre-t-on, sur devis, une expérience sur modèle réel dont les niches de triche sont construites et dosées, avec un oracle caché, pour éprouver la bascule de signe entre rejet pur et pénalité au seuil prédit ?

**Enjeu.** Sans expérience sur modèle réel, les trois modèles jugent la conférence principale hors d'atteinte. Avec, rien n'est acquis : la prédiction peut être réfutée. Les coûts avancés par les modèles varient d'un facteur dix pour des plans voisins (de 40 à 450 heures de carte graphique pour la seule première expérience), et leurs auteurs les disent illustratifs. Un préenregistrement d'expérience sur modèle ouvert existe déjà, tenu par une autre session, avec un autre plan : rejet répété et non rejet pur, moniteur de la chaîne de pensée à soupçon gradué, banque de tâches publique à assertion visible mutée. Son devis, non scellé, plafonne un premier étage d'étalonnage à 86 heures de carte et chiffre le second entre 66 et 601 heures selon les tranches, sans avancer de prix. Deux plans payants en parallèle seraient un doublon.

| Option | Avantage | Inconvénient |
|---|---|---|
| 1. Fondre les corrections du collisionneur dans le préenregistrement existant (bras de masquage, bras de rejet pur par récompense corrigée, test de translation, classes aveugles au détecteur, taux de fausses alertes fixé), par une version nouvelle écrite par sa session | Une seule expérience, déjà contre-lue une fois, à étages plafonnés. Son moniteur fournit une probabilité de survie par épisode, ce que la récompense corrigée exige. | Son contraste principal n'est pas la bascule de signe. La niche parfaite n'y est pas garantie mécaniquement. Chaque bras ajouté renchérit : complément de devis. Faisabilité à juger par ses concepteurs, non par cette pièce. |
| 2. Construire un banc neuf : détecteur à règle qui n'inspecte jamais le corps de la solution, classes par arbre syntaxique et oracle caché, trois jeux de tests disjoints, après qualification du code sur un arbre exact | Teste directement la prédiction bilatérale, l'élément le plus difficile à dire évident. Paramètres de la niche fixés par construction. | Conception à faire de zéro : trois tâches et trois réalisations du rejet pur jamais critiquées. Code d'entraînement inexistant. Coût inconnu à un facteur dix près. S'ajoute aux chantiers actifs. |
| 3. Ne rien ouvrir maintenant ; s'en tenir aux pas sans dépense ; décider après le 1er décembre, une fois la première cible choisie | Aucune dépense ni dispersion avant l'entretien. Un atelier, une piste courte ou une revue ne demandent pas ce banc. | La conférence principale reste hors d'atteinte. Le calendrier glisse. |

**Recommandation.** Option 3 jusqu'au 1er décembre ; ensuite option 1 plutôt que 2, si Lazar vise la conférence principale. **Confiance : modérée, environ 0,55.** Ce qui la ferait changer : si le plan existant ne peut pas porter une niche parfaite, l'option 2 devient la seule qui éprouve la bascule ; si Lazar s'en tient à l'atelier, à la piste courte ou à la revue, aucun banc n'est nécessaire.

**Dans tous les cas.** Aucune heure de carte sans devis vérifié et accord. La conception d'un plan neuf ou d'une version nouvelle du préenregistrement revient à Fable, sa contre-lecture à Opus. La tâche et la réalisation de référence du rejet pur sont proposées par cette conception et arrêtées avec la décision de Lazar sur le banc ; la présente pièce n'en choisit aucune.

### (c) L'accord antérieur sur un petit dépôt public compagnon — QUESTION POSÉE À LAZAR

**Question.** L'accord donné le 24 novembre vers 6 h 30, temps universel, pour ouvrir un petit dépôt public compagnon (GO-2026-11-24-05) tient-il tel quel, ou attend-il les préalables de diffusion de la section 7.1 ?

**Les faits.**
- L'accord porte sur un dépôt public de trois fichiers propres : la page de présentation, le manuscrit compilé au nom de Lazar, le script de vérification, après revue par Neon.
- Il a été donné quand le manuscrit en était à sa v2. Depuis : dix corrections de l'audit indépendant, un défaut majeur relevé à la vérification de fidélité, la correction de la normalisation sous pénalité. La base est aujourd'hui la v4 avec son correctif 3 et son erratum 1.
- Selon les passations lues, rien n'a été diffusé. Cette pièce n'a pas pu le vérifier hors du dépôt.
- Les préalables de la section 7.1 sont une proposition de cette pièce. Ils ne figurent pas dans l'accord de Lazar. Ni cette pièce ni la session mère ne peuvent suspendre ou conditionner cet accord.

| Réponse possible | Avantage | Inconvénient |
|---|---|---|
| 1. L'accord tient tel quel, appliqué à la base actuelle | Prise de date immédiate. Geste déjà accordé. | L'antériorité n'est pas lue. Une référence est encore fausse dans la base. Un dépôt public au nom de l'auteur pèse sur l'anonymat d'une soumission ultérieure, selon des règles non lues. |
| 2. L'accord tient, après les seuls préalables courts : référence corrigée, traces internes retirées, page de dépôt vérifiée | Quelques jours de délai seulement. Évite de publier une erreur connue. | Antériorité et règles d'anonymat toujours non lues au moment du geste. |
| 3. L'accord attend tous les préalables de la section 7.1 | Aucun geste public avant que la zone revendiquée et les règles soient vérifiées. | Retarde la prise de date ; restreint un accord déjà donné. |

**Avis de la pièce, qui ne vaut pas décision.** Attendre, par la réponse 3, ou à défaut la réponse 2. Raison : l'accord visait une version que l'audit a corrigée dix fois depuis, et un dépôt public ne se reprend pas. **Confiance : modérée, environ 0,6.** Le risque propre de l'attente, qu'un autre publie d'abord, n'est pas chiffrable ici.

---

## 6. La borne plus fine de la marge du plancher d'audit

**Ce qui est acquis.** L'expérience de seuil du théorème de l'audit tiré au hasard a été préenregistrée, courue sur processeur et lue par un lecteur neuf. Aucune réfutation. La garantie tient en 137 points sur 138 ; le dernier est non concluant, non contredit. La marge est nécessaire : sans elle, le seuil est franchi avec une fréquence d'au moins 0,86. Elle est conservatrice d'un facteur 1,75 à 3,56 sur le seuil (médiane 2,49). En audits réservés, employer la marge la plus petite épargnerait de 2 à 57 % du budget de référence de la remarque (le budget uniforme de référence), 10,5 % en médiane. Un audit exact par programmation dynamique a porté sur 32 points à mémoire entière. La marge n'est pas le budget : « deux fois moins d'audits » serait faux.

**Ce que Lazar a dit** (mot du 24 novembre, vers 13 h 10, temps universel ; tel que le registre le consigne, R-5284) : « (b) remarque au manuscrit maintenant — garantie tenue en 137/138, marge nécessaire, conservatrice d'un facteur 2,49 en médiane sur le seuil, soit 10,5 % d'audits réservés en médiane (2 à 57 %) ; (a) théorème resserré après le 1er décembre, sur préenregistrement neuf ». Son mot ne contient aucune autre condition.

**Ce qui est fait.** La remarque est écrite dans le brouillon de la section sur le budget d'audit (`D/theorie/brouillon-fable-budget-audit-v1/audit-budget-section-v1-correctif-4.tex`, remarque « A preregistered simulation of the margin »), **hors du manuscrit de base**. Elle commente le théorème de l'audit tiré au hasard, que le manuscrit de base ne contient pas. Tant que cette section n'entre pas au manuscrit, le mot de Lazar n'a pas d'effet visible dans la pièce qui serait diffusée. Son report est mis au calendrier (section 7.2, tâches 7 et 8). Rien n'est commencé pour le théorème resserré.

**Ce qui vient du mandat de la session mère, et non du mot de Lazar.** La restriction « seulement si la cible visée l'exige ».

**Ce qui est proposé à Lazar.** Ces trois points restreignent ou précisent un accord donné. Ils ne s'appliquent que s'il les accepte ; d'ici là, son mot vaut tel quel.
1. *Restriction.* N'ouvrir le théorème resserré que si la cible retenue l'exige : c'est-à-dire si elle fait entrer la section sur le budget d'audit dans la version soumise, à un niveau d'exigence où un facteur 2,5 sur la marge serait une faiblesse. Un atelier ne l'exige pas.
2. *Priorité basse.* Le gain médian est d'un dixième du budget de référence.
3. *Précision demandée.* « Remarque au manuscrit » vise-t-il le manuscrit de base ? Si oui, la section sur le budget d'audit, ou au moins son théorème de l'audit tiré au hasard, doit y entrer avec la remarque. Si non, le mot est rempli par le brouillon de section.

Recommandation : accepter la restriction et la priorité basse. Confiance : assez bonne, environ 0,7, parce que le gain mesuré est modeste et qu'aucune cible courte ne demande ce théorème.

**Quelle que soit la réponse.** Rien n'est ouvert avant le 1er décembre. Le théorème resserré se fait sur préenregistrement neuf, écrit par Fable, contre-lu par Opus, scellé avant tout tirage, sur processeur. Deux voies sont nommées dans la remarque : une inégalité maximale de martingale à la place de la borne d'union sur les tours ; des queues binomiales exactes à la place de l'inégalité de Bernstein.

---

## 7. Dépendances, ordre et dates

### 7.1 Dépendances

| Pour faire | Il faut d'abord |
|---|---|
| Tout geste de diffusion nouveau (prépublication, commentaire, billet) | lecture d'antériorité sur PDF ; corrections de références portées ; affirmations attribuées à Price, Robertson et Fisher lues sur PDF ; manuscrit débarrassé des traces internes ; billet et page de dépôt vérifiés ; règles de l'appel lues ; **geste de Lazar** |
| Dépôt public compagnon | la réponse de Lazar à la question (c) de la section 5 : son accord antérieur tient-il tel quel ? |
| Décision sur la première cible | appels de l'année lus et consignés ; à défaut, appels de l'année précédente, marqués « indicatifs » |
| Décision sur le banc de code | décision sur la première cible ; devis vérifié |
| Banc ou expérience sur modèle réel | décision sur le banc ; conception par Fable (tâche, réalisation du rejet pur) ; qualification du code sur un cas exact ; préenregistrement scellé ; accord de dépense |
| Scellement du préenregistrement existant sur modèle ouvert | vérification de ses corrections ; instruments écrits, contre-lus et empreintés ; ses six décisions ouvertes ; empreintes finales des brouillons de dynamique et de découplage ; accord de dépense sur le premier étage |
| Report de la remarque sur la marge dans le manuscrit | vérification des correctifs 3 et 4 de la section sur le budget d'audit ; entrée de cette section, ou de son théorème de l'audit tiré au hasard, dans un fichier neuf du manuscrit ; précision de Lazar (section 6, point 3) |
| Théorème resserré de la marge d'audit | 1er décembre passé ; préenregistrement neuf ; et, si Lazar accepte la restriction proposée, une cible qui l'exige |
| Citation de Lean dans une pièce publique | alignement sur la base retenue ; témoins de cohérence des hypothèses ; accord de la mère, puis de Lazar |
| Soumission en conférence principale | résultat d'expérience conforme à la prédiction — il peut ne pas l'être |

**Traces internes à retirer avant diffusion.** Dans le manuscrit : la note d'auteur qui cite les versions et les relectures internes ; les noms de scripts en français ; le nom d'auteur laissé en attente. Dans la page de dépôt : le lien vers le PDF laissé en attente et les noms de fichiers internes. Aucun identifiant d'accord ou de registre n'a été trouvé dans le manuscrit.

### 7.2 Avant le 1er décembre 2026

Tout est sans dépense, sur processeur, sans diffusion. Les dates sont proposées, non engagées ; les chantiers de l'entretien du 1er décembre passent avant.

| Ordre | Tâche | Qui | Date proposée |
|---|---|---|---|
| 1 | Verser cette pièce ; présenter à Lazar les trois points de la section 5 et la proposition de la section 6 | session mère | 25 novembre |
| 2 | Lire les appels de l'année des cibles de la section 7.4 et les consigner ; pour un appel non encore paru, consigner celui de l'année précédente, marqué « indicatif » | une session ayant accès au réseau, ou Lazar | 25 au 27 novembre |
| 3 | Demander à Lazar les PDF sous droits de Price, Robertson et Fisher, cités dans le manuscrit de base ; y lire, page citée, les affirmations qui leur sont attribuées | session mère pour la demande ; Opus pour la lecture | demande le 25 novembre ; lecture à réception |
| 4 | Lecture d'antériorité sur PDF, page citée : le travail sur la surveillance des modèles de raisonnement et l'obscurcissement (Baker et al.) ; la lecture bayésienne de l'apprentissage par renforcement régularisé (Korbak, Perez, Buckley) ; puis l'obscurcissement appris sous pénalité de la chaîne de pensée (Skaf et al.) et l'évasion de moniteurs de l'espace latent par renforcement (Gupta, Jenner) | Opus, effort élevé | 26 au 28 novembre |
| 5 | Correctif du manuscrit, en fichier neuf : référence de Bartók et al. corrigée ; trois phrases proposées (rejet pur comme filtre de sortie ; agrégation par classe exacte sous rejet pur, simple borne sous pénalité ; régime des pièges vide à supports disjoints) ; copie de diffusion sans trace interne. Contre-lecture, puis vérification par le même contre-lecteur | session qui tient le manuscrit ; contre-lecteur d'un autre modèle | 27 au 30 novembre |
| 6 | Vérification du billet et de la page de dépôt portés au correctif 3 | même contre-lecteur | avec la tâche 5 |
| 7 | Vérification des correctifs 3 et 4 de la section sur le budget d'audit, préalable au report de la remarque sur la marge | contre-lecteur d'un autre modèle | 27 au 30 novembre |
| 8 | Report de la remarque sur la marge dans le manuscrit : fichier neuf portant la section sur le budget d'audit, ou son théorème de l'audit tiré au hasard, avec la remarque | session qui tient le manuscrit | après la tâche 7 : avant le 1er décembre si Lazar dit que son mot vise le manuscrit de base ; sinon avec la version longue |
| 9 | Transmettre, par les mères, à la session du préenregistrement sur modèle ouvert les propositions du collisionneur qui touchent son plan : bras de masquage ; classes aveugles au détecteur ; jeux de tests disjoints ; repasse dans les poids gelés ; taux de faux négatifs à taux de fausses alertes fixé ; pièges par mélange ; nombre de graines ; abandon de la normalisation par groupe et test de translation ; critères des instruments mesurés avant l'entraînement ; vérifications mécaniques ; classe « échec » ; sonde interne tenue hors de la boucle ; croisement de l'affinage complet et de l'affinage de faible rang ; porte « égalité des bras sans détecteur » (lignes 5 à 11, 15, 19, 20, 25 et 29 à 31 de la table de la section 2) | session mère | 25 novembre |

**Ne sont pas ouverts avant le 1er décembre** : la formalisation en Lean ; l'arbre exact à quatre bras (« pas maintenant », selon la mère) ; le théorème resserré de la marge ; tout calcul payant ; tout geste de diffusion nouveau et toute soumission ; toute conception de banc.

### 7.3 Après le 1er décembre 2026

L'ordre suit les dépendances. Aucune date n'est donnée pour ce qui dépend d'un appel ou d'une décision.

| Ordre | Tâche | Condition | Qui |
|---|---|---|---|
| 1 | Décision sur la première cible, puis décision sur le banc de code | appels lus, ou consignés comme indicatifs | Lazar |
| 2 | Geste de diffusion : prépublication, puis commentaire et billet dans l'ordre que les règles lues permettent | tâches 3 à 6 de la section 7.2 closes | Lazar |
| 3 | Soumission à la première cible | décision sur la première cible ; **échéance à vérifier dans l'appel de l'année** | Lazar |
| 4 | Pas sans dépense de la théorie : inversion à divergence appariée recalculée sur le modèle tabulaire ; point fixe sous normalisation par groupe avec ancre, écrit et contre-lu ; proposition sur l'effet instantané de la pénalité, par géométrie (euclidienne et naturelle) | utiles à la version longue ou au banc | Opus pour les calculs ; Fable pour un énoncé nouveau |
| 5 | Formalisation en Lean : alignement sur la base retenue, forme avec récompense honnête, témoins de cohérence des hypothèses, contre-exemple certifié de l'inversion privée de sa condition | sa session ; citation publique sur accord | session qui tient Lean |
| 6 | Expérience sur modèle réel : version nouvelle du préenregistrement ou banc neuf ; qualification du code sur un cas exact, tabulaire puis petit réseau, avec la porte « égalité des bras sans détecteur » ; devis ; accord | décision favorable sur le banc | Fable pour la conception ; Opus pour la contre-lecture et le code |
| 7 | Théorème resserré de la marge du plancher d'audit | section 6 | Fable, puis Opus |
| 8 | Sections longues au manuscrit : dynamique, normalisation par groupe, découplage, budget d'audit s'il n'y est pas déjà entré | cible qui les demande ; contre-lecture finale de chacune | session qui tient le manuscrit |
| 9 | Conférence principale | résultat de l'expérience ; **échéance à vérifier dans l'appel de l'année** | Lazar |
