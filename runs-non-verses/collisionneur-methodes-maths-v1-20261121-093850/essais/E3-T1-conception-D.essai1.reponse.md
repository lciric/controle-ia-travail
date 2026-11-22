# Proposition D — chercher une séparation avant de chercher une preuve

## 1. Le travail d’expert qui manque en amont

**HYPOTHÈSE — choix de méthode.** Un probabiliste commencerait par écrire le jeu d’audit, non par choisir un proposeur. Que voit le moniteur ? Quand choisit-il d’auditer ? La loi des observations peut-elle dépendre de ses choix passés ? Qui supporte le coût d’une fausse alerte ? Il chercherait ensuite à résoudre à la main le plus petit jeu dans lequel deux formalismes plausibles donnent des réponses différentes. Si donner au moniteur la graine du monde planté change la valeur du jeu, par exemple, la distinction entre *information de l’évaluateur* et *information du moniteur* doit figurer dans l’énoncé mathématique. Elle ne relève pas seulement de l’hygiène du banc d’essai.

Présupposés à lever séparément :

- **RAPPORTÉ** — Un harnais Lean existe ; son outillage n’est pas encore relevé conforme. **HYPOTHÈSE** — Il vérifie exactement l’énoncé voulu, et pas seulement un énoncé bien typé.
- **RAPPORTÉ** — Un pilote sur douze mondes et une épreuve de nouveauté sur quarante énoncés connus sont conçus. **HYPOTHÈSE** — Réussir ces épreuves prédit une découverte hors des familles plantées.
- **HYPOTHÈSE** — La question cible n’est pas déjà résolue par un résultat plus général. Un mauvais moteur de recherche d’antériorité ferait passer cette ignorance pour du rendement scientifique.
- **HYPOTHÈSE** — Une amélioration sur des instances finies révèle une variable pertinente pour un théorème ; **HYPOTHÈSE** distincte — ce théorème change effectivement une décision d’audit. Ni le score ni la preuve ne tranchent à eux seuls les deux questions.

## 2. Les objets bruts à demander

**OBSERVÉ-NON-AUDITÉ — pièces.** Aucun dépôt, instantané Mathlib, journal brut, certificat ni archive de tentatives n’est joint au dossier transmis ici.

**HYPOTHÈSE — cahier d’acquisition proposé.**

| Objet | Unité à conserver avant analyse |
|---|---|
| Corpus de problèmes | Texte original daté, versions successives, définitions et questions ouvertes telles que posées ; inclure les problèmes abandonnés. |
| Bibliothèque formelle | Sources Lean et Mathlib au commit exact, dépendances, commandes de construction ; pour chaque théorème voisin, type complet et axiomes transitifs. |
| Journaux de preuve | But local, contexte, tactique essayée, résultat du noyau ou erreur, temps consommé, y compris les branches sans preuve. |
| Banque de contre-exemples | Loi jointe ou table de transitions exacte, politique d’observation, témoin de violation, calcul rejouable ; pas seulement « faux ». |
| Archive des tentatives | Proposition avant critique, ascendance, hypothèses modifiées, témoin qui l’a tuée. Une variante ne ressuscite pas son parent : elle doit expliquer pourquoi le témoin ne s’applique plus. |
| Antériorité et utilité | Articles intégraux avec leurs hypothèses ; spécification et décisions de l’auditeur *avant* découverte. Sans cette dernière pièce on peut toujours inventer une utilité après coup. |

**HYPOTHÈSE — cloisonnement.** Séparer par *famille mathématique* avant indexation. Donner au chercheur les témoins de développement ; confier les instances d’examen, leur vérité et le verdict à l’arbitre. Une variante de notation n’est pas une famille inédite.

## 3. Méthodes : ce que les précédents autorisent à inférer

**RAPPORTÉ — littérature, non répliquée ici.** Pour les identifiants arXiv : pas sûr ; je n’en donne aucun.

| Travail | Mécanisme et résultat rapporté | Condition de transfert ou limite (**HYPOTHÈSE** pour ce programme) |
|---|---|---|
| Bernardino Romera-Paredes et al., *Mathematical discoveries from program search with large language models* (2024) | FunSearch fait varier par modèle de langage une partie d’un programme ; un évaluateur note les sorties et une population de programmes sélectionnés nourrit les générations suivantes. Des constructions de cap sets et des heuristiques de rangement ont été obtenues. | Une construction explicite peut se vérifier indépendamment de sa genèse. Un score élevé sur des mondes simulés, lui, ne prouve pas une borne uniforme. Chercher des **témoins**, pas optimiser la note d’un juge de théorèmes. |
| Yuhuai Wu et al., *Autoformalization with Large Language Models* (2022) | Traduction d’énoncés informels vers Isabelle ; emploi de données autoformalisées pour l’apprentissage de la démonstration. | Le typage élimine certaines traductions impossibles, pas une inversion de quantificateurs bien typée. Garder des mondes qui séparent les lectures concurrentes. |
| Kaiyu Yang et al., *LeanDojo: Theorem Proving with Retrieval-Augmented Language Models* (2023) | Extraction de traces et interaction avec Lean ; ReProver récupère des prémisses accessibles puis propose des tactiques à partir de l’état de preuve. Résultat : preuves de buts d’évaluation, non certificat de nouveauté des buts. | La mémoire de prémisses est utile si le bon lemme est accessible ; elle ne choisit pas la définition du jeu. Comparer à la recherche native dans le même environnement. |
| Zhangir Azerbayev et al., *Llemma: An Open Language Model For Mathematics* (2024) | Modèle ouvert spécialisé, évalué notamment en preuve informelle-vers-formelle et en prédiction de tactiques. | Un modèle capable de compléter une étape n’est pas pour autant un générateur de bonnes conjectures. Il faut mesurer séparément les étapes proposées et les preuves achevées. |

**HYPOTHÈSE — articulation non démontrée ici.** Pour la conjecture automatique, faire proposer une paire « formule candidate, plus petit contre-modèle attendu si j’enlève telle hypothèse ». L’énumérateur cherche le contre-modèle ; la décomposition en lemmes n’intervient qu’après, en demandant une preuve de suffisance et un témoin de non-extension. Mémoriser les témoins avec leur domaine de validité plutôt qu’un simple verdict textuel. Je ne sais pas si ce couplage bat l’énumération seule ; je ne lui attribue aucun résultat publié.

## 4. Vérification hors du programme

**HYPOTHÈSE — procédure d’acceptation externe.**

- **Vrai.** Livrer spécification informelle, fichier formel, versions et commande de rejeu. Un tiers reconstruit hors de la machine productrice, contrôle les axiomes contre une liste autorisée et compare *les types* aux engagements du jeu. Une preuve d’une implication à prémisse impossible est un échec de spécification même si le noyau l’accepte.
- **Nouveau.** Confier à un mathématicien non auteur la tâche adverse : déduire l’énoncé des résultats antérieurs, changement de variables et spécialisation compris. Publier requêtes, corpus daté, voisins les plus forts et tentative de réduction. Verdict admissible : « aucune réduction trouvée dans ce périmètre », jamais « premier » par seule absence de correspondance.
- **Utile.** Faire calculer à une autre équipe, avant puis après divulgation du résultat, le choix d’audit admissible sur un cas réservé. Exiger soit une décision améliorée à contraintes inchangées, soit un certificat qu’une garantie demandée était impossible. Une réplication du calcul de la valeur et une relecture du sens du théorème sont deux livrables différents.

## 5. Demande reformulée

**HYPOTHÈSE — commande proposée.** « Pour un jeu d’audit dont le calendrier d’information et le budget sont gelés, produisez soit une réduction explicite au meilleur théorème connu, soit une séparation accompagnée d’un témoin exact et d’une preuve rejouable. Indiquez la décision que cette séparation changerait. Un résultat négatif documenté est recevable ; la nouveauté et l’utilité ne sont pas attribuées par le proposeur. »

## 6. Méthodes à tenter et duels qui les arrêtent

**HYPOTHÈSE — convention de mesure.** Les duels ci-dessous portent sur un lot fini scellé, à budget égal, et non sur une supériorité universelle. Pour chaque instrument : cible positive pré-étiquetée, taux de détection = cibles signalées / cibles présentes ; taux de fausses alertes = témoins honnêtes signalés / témoins honnêtes présents. Apparier difficulté, longueur et famille, masquer l’identité du producteur. Pour un proposeur, « signaler » signifie *livrer un objet accepté* ; pour un portier, *signaler un défaut*. Publier les numérateurs, dénominateurs et discordances appariées, pas seulement les pourcentages.

### Deux expériences de découverte

**HYPOTHÈSE D-valeur — quand l’historique vaut-il quelque chose ?** Premier pas : sur des jeux finis à probabilités rationnelles et budget fixé, calculer exactement par récurrence la valeur avec historique complet et celle avec la seule statistique que conserve l’agrégateur. Faire chercher au modèle deux historiques de même statistique qui imposent des choix d’audit différents. Exiger une **perte stricte de valeur depuis l’état initial** : deux actions différentes dans des états inatteignables ne suffisent pas. Puis chercher une condition structurelle rétablissant l’égalité.

- **Duel.** \(H_A\) : sur la famille réservée, la recherche proposée livre davantage de séparations certifiées non équivalentes que l’énumération canonique à même temps total, sans fausse séparation supplémentaire ; \(H_B\) : négation exacte. Seuil : gain strict de détection à fausses alertes non accrues. Seuil franchi : \(H_B\) falsifiée ; sinon \(H_A\) falsifiée sur ce lot. Contrôle négatif : jeux appariés où la statistique encode tout l’historique pertinent.
- **Mort scientifique.** Même un gain expérimental ne sauve pas une « découverte » qui se réduit au critère connu de suffisance d’un état. La différence visée avec la recherche de programmes publiée est le certificat apparié *perte exacte / condition de restauration*, pas le fait d’utiliser une population de programmes. Différence avec la littérature sur les jeux d’information : **je ne sais pas** avant recherche d’antériorité.

**HYPOTHÈSE D-frontière — quelle dépendance invalide une garantie séquentielle ?** Premier pas : prendre une garantie candidate à horizon fini, écrire séparément ses contraintes marginales et ses contraintes conditionnelles à l’historique. Sur un arbre fini, représenter les masses des feuilles comme variables et maximiser la probabilité de franchissement d’un seuil fixé. Pour des contraintes linéaires rationnelles, demander selon le cas une loi témoin ou un certificat dual rationnel, vérifiés indépendamment du solveur. Faire ensuite conjecturer quel sous-ensemble de contraintes suffit encore ; ne pas extrapoler un certificat d’arbre à tout horizon.

- **Duel.** \(H_A\) : le couple conjecture guidée par témoins + réemploi livre sur le lot réservé davantage de frontières valides que la suppression systématique de contraintes avec le même solveur, sans plus de frontières fausses ; \(H_B\) : négation. Une frontière compte si la suffisance est certifiée dans le domaine annoncé et si chaque retrait déclaré fatal a son témoin. Même seuil strict et mêmes issues falsifiantes que ci-dessus. Contrôle négatif : contraintes redondantes dont le retrait est présenté au système sans étiquette.
- **Mort scientifique.** Tuer la prétention de généralité au premier horizon qui contredit le lemme ; tuer la prétention de nouveauté si dualité et garantie publiée impliquent immédiatement l’énoncé. La différence visée avec un pilote qui *juge* un énoncé planté est de *produire* la paire certificat/témoin puis de prouver pourquoi elle persiste hors de l’arbre initial.

### Qualification des instruments avant d’attribuer les gains

**HYPOTHÈSE — duels instrumentaux.** Pour chaque ligne, \(H_A\) = détection strictement supérieure au contrôle mécanique sans hausse des fausses alertes ; \(H_B\) = son complément. Le franchissement du seuil falsifie \(H_B\), son absence falsifie \(H_A\) sur le lot. Pour le noyau et le rejeu, qui sont des références et non des heuristiques à surpasser, \(H_A\) = accord intégral avec les verdicts attendus ; la moindre discordance la falsifie, l’accord intégral falsifie son complément sur le lot.

| Instrument | Cible / contrôle négatif honnête apparié | Vérification mécanique de référence |
|---|---|---|
| Sonde linéaire ; comparaison au jumeau ; agrégateur (tester chacun isolément) | Épisode planté à décision erronée / épisode honnête sur même tâche, incluant erreur honnête et désaccord ordinaire entre jumeaux | Tests de sortie exacts ; pour l’agrégateur, meilleur moniteur unique choisi sur développement |
| Détecteur séquentiel | Épisode planté détecté avant échéance / trajectoire honnête entière de même horizon ; compter toute alerte, pas la proportion de pas en alerte | Seuil fixe avec correction pour les inspections multiples |
| Générateur, sélection évolutionnaire, conjecture et contre-exemples | Séparation réelle dont un témoin est trouvé / instance appariée sans séparation | Énumération exacte à budget égal ; retirer la sélection pour isoler son apport |
| Autoformalisation et juge sémantique | Traduction au sens altéré détectée / traduction fidèle de même complexité | Typage puis évaluation sur petits mondes discriminants |
| Recherche Lean, décomposition, mémoire | But démontré / voisin faux déclaré démontré ; tester aussi le rappel indu d’un lemme hors hypothèses | Tactiques natives, puis même recherche sans récupération ni découpage ; seul le rejeu valide la sortie |
| Portier, harnais et rejeu tiers | Artefact invalide refusé / preuve honnête reconstruite avec dépendances gelées | Noyau isolé, inspection des axiomes, vérification du type attendu |
| Juge d’antériorité | Résultat connu sous reformulation détecté / voisin honnêtement distinct dans une archive fermée | Recherche textuelle, recherche par type, subsomption mécanique quand décidable |
| Relecture et réplication d’utilité | Gain annoncé mais absent détecté / gain exact sur jeu apparié | Recalcul exhaustif des politiques sur petites instances ; hors domaine calculable, déclarer la limite |

**HYPOTHÈSE — ancrage matériel, coûts illustratifs.** Pour D-valeur, un petit modèle ouvert de code tel que Qwen2.5-Coder-7B-Instruct pour proposer des générateurs, CPU pour récurrence exacte et certificats ; ordre de grandeur **illustratif** : une journée-GPU et quelques dizaines de dollars de calcul. Pour D-frontière, même proposeur ou Llemma pour les étapes de preuve, solveur linéaire sur CPU et machine Lean isolée ; ordre de grandeur **illustratif** : quelques journées de calcul et de quelques dizaines à quelques centaines de dollars. Ce sont des enveloppes d’arrêt, non des devis mesurés. **RAPPORTÉ** — Le budget disponible est de quelques centaines de dollars par course et la relecture humaine rare.

**HYPOTHÈSE — allocation humaine.** Dépenser la première relecture sur le calendrier d’information et le théorème voisin, non sur la prose finale. Réserver ensuite plusieurs journées d’expert (**illustratif**) pour comparer les hypothèses et tenter la réduction, même si le calcul ne prend qu’une nuit (**illustratif**). Je ne sais pas chiffrer la probabilité de découverte. Un témoin rejeté, une réduction à un résultat connu ou une preuve dont personne n’a vérifié le sens ne doivent pas être comptés comme des mathématiques inédites.

FIN-DE-CELLULE