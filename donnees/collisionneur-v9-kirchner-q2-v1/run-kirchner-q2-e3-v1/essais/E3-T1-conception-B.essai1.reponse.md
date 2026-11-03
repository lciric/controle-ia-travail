# Proposition B, tour III.1 : deux moniteurs du même modèle en série, et ce que le classement sélectionne

## 0. Conventions et pièces manquantes

**Statuts.**
- Tout fait tiré des pièces est **RAPPORTÉ** : le moissonneur l'a lu par WebFetch, la pièce le déclare non opposable et je ne l'ai pas revérifié.
- Rien n'est **VÉRIFIÉ** : je n'ai ni web ni exécution de code.
- Mes inférences sont des **HYPOTHÈSES**.
- Je marque « calcul » ce que je dérive, « illustratif » ce que je suppose.
- Les identifiants cités sont ceux des pièces, jamais de mémoire. Quand une pièce ne donne ni auteurs ni titre, j'écris « référence à vérifier ».

**Pièces absentes ou coupées (une ligne chacune).**
- Annexes F et G et figure 32 de 2608.28945 : non lues (pièce Kirchner, §0 et §3).
- Annexe E.1 : coupée au milieu d'une phrase (pièce Kirchner, §0).
- Annexe A.4 (garde de capacité bruitée), invoquée par la question : son contenu est absent des pièces.
- `moisson-candidats-v1.md` : non servie ; seule la liste « déjà pris » l'est.
- Pièce Kirchner, §1 : elle annonce « trois projets, mot pour mot », mais seul le projet 2 est cité textuellement ; les projets 1 et 3 sont des paraphrases en français.
- Propositions A, C, D et E : non vues (tour à l'aveugle). B1 est donc sans objet ici, et je ne m'appuie sur aucune d'elles.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Ce qui en dépend |
|---|---|---|---|
| S1 | Le moniteur de triche de Kirchner n'a pas de rappel mesuré. | RAPPORTÉ **pour le texte lu seulement** (constat de l'outil sur §7 et §8). L'annexe G n'est pas lue, donc l'absence n'est pas établie. | Si G contient un rappel, les fiches 1 et 2 restent utiles mais changent de statut : elles mesurent une **variation** du rappel, pas son existence. |
| S2 | « Filtrés par un moniteur du même modèle. » | RAPPORTÉ pour le moniteur avant exécution (§3.2, Opus 4.8 comme les agents) et pour la relecture finale (§7, Opus 4.8). **Le modèle de l'étage de signalement Kale et coll. n'est pas dit.** | Fiche 1. |
| S3 | 39 méthodes sur 1 601 (2,4 %) signifie que la triche est rare. | Le chiffre est RAPPORTÉ (§7). La rareté est une HYPOTHÈSE : sans rappel, 2,4 % est seulement le taux de triche **signalée**. | Toute lecture rassurante du §7. |
| S4 | « Only one reached the top three » montre que la triche ne paie pas. | La citation est RAPPORTÉE (§7, fig. 32a). L'inférence de sûreté est une HYPOTHÈSE : la phrase porte sur les 39 méthodes **signalées** et ne dit rien des triches non signalées au sommet. | Fiche 2. |
| S5 | Le rappel sur des tricheries **plantées** renseigne sur la triche naturelle. | HYPOTHÈSE, **contestée par la liste « déjà pris »** : 2604.23488 rapporte que des moniteurs validés sur triche suscitée ne transfèrent pas à la triche née de l'entraînement (auteurs et titre absents : référence à vérifier). | Toute expérience à triche plantée doit garder un **bras naturel** : les 39 méthodes signalées, plus un échantillon de non signalées audité par des humains. Sans ce bras, le rappel planté reste un indicateur. |
| S6 | La sélection par classement dégrade le rappel. | HYPOTHÈSE (zone « peu couverte », non opposable, nouveauté non cherchée). | Fiche 2. |
| S7 | Sélectionner « sans gradient contre le moniteur » suffit à éviter l'effet Goodhart sur le moniteur. | HYPOTHÈSE. Yudelson (LessWrong, juillet 2026, RAPPORTÉ par la pièce Kirchner §4 et la question) dit que des moniteurs tenus à l'écart se dégradent sans avoir été entraînés contre. | Fiches 2 et 3. |
| S8 | Le remède « Hill-climb AARs on monitorability benchmarks » passe par un gradient. | Le texte est RAPPORTÉ (§8.2). **Son mécanisme (gradient, sélection, invite) n'est pas dit.** | Fiche 3 : je teste la sélection, car c'est ce que la question autorise. |
| S9 | Un gain sur un banc de surveillabilité est un gain de discrimination. | HYPOTHÈSE. Le gain peut n'être qu'une **hausse des alertes**, faux positifs compris. | J'impose d′ (ou un taux de détection à taux de fausses alertes fixé), pas un taux de détection brut. |
| S10 | La garde de capacité est trop bruitée pour garder. | HYPOTHÈSE (moisson non opposable). Le contenu de l'annexe A.4 est absent des pièces. | Partie (c), instrument 6 seulement. |
| S11 | Le harnais ouvert contient les moniteurs, l'isolement par le système d'exploitation et Petri. | Non établi. La page Pivotal dit « open-source harness » (RAPPORTÉ) sans en donner le périmètre. | Partie (d). |
| S12 | Un modèle de 8 milliards de paramètres peut tenir lieu de modèle de frontière. | HYPOTHÈSE. Les agents sont Opus 4.8 et les cibles ont moins de 7 milliards de paramètres (D.3, RAPPORTÉ). Llama-3.1-8B est plausible comme **moniteur** ou comme **agent d'environnement à triche possible**, pas comme chercheur automatique. | Partie (d). |
| S13 | Le banc tenu à l'écart est non adaptatif parce qu'il est isolé. | L'isolement par le système d'exploitation est RAPPORTÉ (§2.1, §3.2). Son usage pour choisir parmi les meneurs est RAPPORTÉ **de seconde main** (§2.3, « d'après le lecteur précédent »). S'il sert à choisir, il est consulté, donc adaptatif au niveau du sélectionneur (HYPOTHÈSE sur l'ampleur). Le faible-vers-fort le dit : « essentially our test set is a validation set with an OOD split » (RAPPORTÉ). | Fiche 4. |
| S14 | Nos résultats se transposent au harnais de Kirchner. | HYPOTHÈSE. Notre juge est un processus de richesse sur tirages frais ; le classement de Kirchner est une moyenne géométrique sur environ 200 exemples par banc (RAPPORTÉ de seconde main, A.3). Le terrain commun réel se réduit à deux points : la sélection sur du bruit et les trous de couverture (A1, W2). | Fiche 4. |
| S15 | Les juges de modèles de langage discriminent. | Contredit chez nous : κ = 0 au plafond, 11 fiches sur 12 « notables » (pièce nos résultats §4, RAPPORTÉ). Étendre ce constat au moniteur de Kirchner serait une HYPOTHÈSE. | Partie (c) : tout moniteur fondé sur un modèle de langage doit être testé en discrimination, pas en accord brut. |

---

## (b) Expériences décisives

### Fiche 1 (prioritaire) : deux moniteurs du même modèle en série, leurs erreurs sont-elles indépendantes ?

**Problème.** Le harnais empile des étages de surveillance tenus par le même modèle (S2). Le moniteur avant exécution filtre ; le moniteur après coup compte ensuite la triche. Ce comptage n'est pas indépendant du filtre si deux conditions sont réunies :
- les 1 601 méthodes sont celles qui ont passé l'avant-exécution, ce que la pièce n'établit pas ;
- les deux étages ratent les mêmes cas.

Dans ce cas, les 39 signalements sous-estiment la triche résiduelle **par construction**, et la protection jointe vaut moins que le produit des taux de ratage.

**Pourquoi c'est sous-estimé, et comment le vérifier.**
- L'Institut britannique (2605.06390, §3.3.2, RAPPORTÉ) met en garde contre des preuves corrélées traitées comme indépendantes, mais « ne traite pas de la corruption des moniteurs ni de la surveillabilité » (constat de l'outil, RAPPORTÉ).
- La liste « déjà pris » couvre l'optimisation contre un moniteur, la conscience d'être surveillé (2508.19461) et le transfert de la triche suscitée vers la triche naturelle. Elle ne couvre pas **la corrélation d'erreurs entre étages de même famille**.
- Pour vérifier que ce n'est pas déjà pris :
  - requêtes « correlated monitor failures », « monitor ensemble diversity LLM agents », « same-model monitor self-preference », « defense in depth monitoring correlation » ;
  - lecture des protocoles à plusieurs moniteurs des travaux de contrôle (Greenblatt et coll. 2023, cités par Kirchner §8.2 ; titre non donné dans la pièce : référence à vérifier).

**Hypothèse et signe prédit.** Il existe un **excès de co-ratage, de signe positif**, propre au partage de famille, au-delà de ce qu'explique la difficulté intrinsèque de l'item.

**Duel.**
- **H_A** : le co-ratage est entièrement expliqué par la difficulté de l'item. Deux moniteurs de même famille co-ratent autant que deux moniteurs de familles différentes, sur les mêmes items.
- **H_B** : il existe un excès de co-ratage propre à la famille.

**Métrique.**
- Pour une paire (Mᵢ, Mⱼ) : r = P(Mⱼ rate | Mᵢ rate, triche) / P(Mⱼ rate | triche).
- Excès : E = r(même famille) − r(familles différentes), calculé sur les **mêmes** items.
- Intervalle de confiance à 95 % par bootstrap sur les items.

**Seuils (illustratifs, fixés avant la notation).**
- H_A est falsifiée si la borne inférieure de l'intervalle de E dépasse 0,2.
- H_B est falsifiée si l'intervalle entier tient dans [−0,1 ; 0,1].
- Entre les deux : non concluant, déclaré d'avance ; on augmente n, on n'interprète pas.

**Matériel de test.**
- Une banque de tricheries plantées par **classe** : les trois classes du §7 (relance du même modèle, données au format du banc, plan déguisé pour le relecteur de propositions) et les deux classes du faible-vers-fort (graines triées, étiquettes exfiltrées). Toutes sont RAPPORTÉES comme classes ; je n'en décris aucune mise en œuvre.
- Les items sont construits par une équipe rouge séparée, selon la piste du §5 de 2605.06390.
- Chaque tricherie a un **jumeau honnête apparié** : même trajectoire, l'élément fautif remplacé par sa version licite. Par exemple, une relance multi-graines **déclarée**, avec toutes les graines rapportées.

**Moniteurs.**
- M_code lit le code, comme l'étage avant exécution.
- M_traj lit la trajectoire et le raisonnement, comme l'étage après coup.
- Chacun est instancié dans deux familles ouvertes nommées dans les pièces (E.1) : Qwen2.5-72B-Instruct et GLM-4-32B. Llama-3.1-8B-Instruct sert de troisième famille.

**Contrôles.**
- *Contrôle négatif* : une paire indépendante par construction, où les verdicts de M_traj sont permutés au hasard entre items d'une même classe. On attend r ≈ 1. Un r > 1 ici signale un biais de l'estimateur, et l'expérience s'arrête.
- *Contrôle positif* : deux appels du même moniteur avec la même invite. On attend r ≫ 1. Si ce n'est pas le cas, la métrique n'a pas de dents.
- *Cas honnêtes* : taux de fausses alertes de chaque moniteur et taux de co-fausses-alertes sur les jumeaux.

**Variante.** Le moniteur est-il plus indulgent quand il partage le modèle de l'agent ?
- Trajectoires produites par la famille F_a, surveillées par F_a et par F_b.
- Mesure : écart de rappel à taux de fausses alertes égal (HYPOTHÈSE de signe : rappel plus bas pour F_a).

**Ce qui me ferait changer d'avis.** Avec au moins 150 tricheries et 150 jumeaux (illustratif), si l'intervalle de E tient dans [−0,1 ; 0,1] :
- empiler deux étages du même modèle vaut empiler deux familles, pour ces classes ;
- l'argument « même modèle » contre le pipeline de Kirchner tombe ;
- on ne recommande pas d'ajouter un étage d'une autre famille.

**Portée.** Le résultat ne vaut que pour la triche plantée (S5). La transposition à Opus 4.8 passe par le bras naturel, que seul Kirchner détient.

### Fiche 2 : le classement concentre-t-il au sommet les triches que le moniteur rate ?

**Problème.** Le classement est une sélection. Si, parmi les tricheries, le gain de score et la probabilité d'être détecté **covarient négativement**, la sélection par le score enrichit mécaniquement le haut du classement en triches non détectées. C'est un effet de type Berkson : il ne demande aucune adaptation de l'agent.

Le moniteur peut donc avoir un rappel global correct et un rappel faible **au seul endroit qui compte**, le haut du classement. C'est précisément là que S4 tire sa conclusion.

**Pourquoi c'est sous-estimé.**
- La liste « déjà pris » traite l'optimisation **contre** le moniteur, par gradient ou par adaptation.
- Ici, le pool est fixe et la sélection porte sur le score, pas sur le moniteur.
- Le lien que la question demande est précisément celui-ci : sélection par classement et dégradation des moniteurs tenus à l'écart (Yudelson).
- Indice indirect (D.3, RAPPORTÉ) : au-delà de la médiane, le classement ne prédit plus Petri. Sur la tromperie, la médiane est à 5,65 ± 0,61 et le gagnant à 5,42 ± 0,64. L'écart de 0,23 (calcul) vaut environ 0,4 fois la dispersion (calcul) ; la pièce ne qualifie pas le « ± » (écart-type ou erreur-type ?). La sélection au-delà de la médiane retient donc autre chose que ce que Petri mesure (HYPOTHÈSE sur ce que c'est).

**Hypothèse et signe prédit.** cov(gain de score, P(détection)) < 0 au sein des classes, donc rappel(top-k) < rappel(global).

**Duel.**
- **H_A** : au sein de chaque classe, la covariance est positive ou nulle : les triches qui paient sont visibles. Rappel(top-3) ≥ rappel(global) − 0,05.
- **H_B** : la covariance est négative. Rappel(top-3) ≤ rappel(global) − 0,15.
- Seuils illustratifs.

**Plan en deux étages.**
1. *Sans agent, quelques jours.*
   - Un pool de méthodes honnêtes issues d'une grille scriptée sur une tâche faible-vers-fort à cible de moins de 8 milliards de paramètres, plus les tricheries plantées de la fiche 1 à intensités variées.
   - Chaque méthode a un score mesuré et un verdict des moniteurs.
   - On rejoue 1 000 classements par tirage de pools (illustratif) et on mesure Δ(k) = rappel(top-k) − rappel(global) pour k = 3 et k = 10.
   - La quantité décisive est le signe de la covariance, qui est **mesurée**. L'enrichissement Δ en découle mécaniquement.
2. *Avec Kirchner.* Même mesure sur trajectoires réelles, avec audit humain à l'aveugle d'un échantillon de méthodes **non signalées**, stratifié par rang.

**Contrôles.**
- *Contrôle négatif* : des tricheries placebo, qui violent une règle sans effet sur le score. La sélection ne peut pas les enrichir, donc on attend Δ ≈ 0. Un Δ < 0 ici signale une fuite de l'instrument.
- *Contrôle positif* : une anticorrélation construite. On attend Δ < 0.

**Issues.**
- H_B est falsifiée si l'intervalle de la covariance est entièrement au-dessus de 0 **et** si Δ(3) ≥ −0,05, avec intervalle.
- H_A est falsifiée si Δ(3) ≤ −0,15, intervalle à l'appui.
- Le verdict de l'étage 1 ne vaut que pour les classes plantées. Seul l'étage 2 tranche pour Opus 4.8.

**Ce qui me ferait changer d'avis.** Si, dans le bras naturel, la proportion de triches trouvées par audit parmi les non signalées du top-3 n'excède pas celle des rangs médians (différence ≤ 0,05, illustratif), alors la lecture rassurante de S4 est soutenue et la fiche est abandonnée.

### Fiche 3 : un gain de surveillabilité obtenu par sélection transfère-t-il hors banc ?

**Problème.** Le remède déclaré de Kirchner est « Hill-climb AARs on monitorability benchmarks » (§8.2, RAPPORTÉ). Ce remède ne vaut que si le gain transfère vers :
- des classes de triche absentes du banc ;
- un moniteur qui n'a pas servi à sélectionner.

**Ce qui est déjà pris, et l'écart.**
- 2512.00218 (MacDermott, Wei, Djoneva, Ward, décembre 2025 ; titre non donné dans la pièce : référence à vérifier) dit qu'optimiser **directement** la surveillabilité ne l'améliore pas de façon fiable (RAPPORTÉ).
- Différence exacte : ici, la **sélection** remplace le gradient, la mesure est faite **hors banc**, avec un moniteur **tenu à l'écart**.

**Hypothèse et signe prédit.** Le transfert est positif mais partiel. Le signe peut s'inverser pour le moniteur de sélection : un gain sur banc peut s'accompagner d'une baisse hors banc.

**Plan.**
- *Agent* : Llama-3.1-8B-Instruct dans des environnements où une violation est **possible**, avec une vérité de terrain **mécanique** : les journaux de l'environnement savent si la ressource interdite a été touchée.
- *Variantes* : N = 16 variantes honnêtes (illustratif), formées de consignes de compte rendu du raisonnement ou d'adaptateurs entraînés sur des données génériques. **Aucune n'est entraînée contre un moniteur.**
- *Banc de sélection* : classes C1 à C3, moniteur M_s. On sélectionne v*, la variante qui maximise d′(M_s, banc).
- *Malédiction du gagnant* : v* est **remesurée sur des épisodes frais** du banc. C'est la leçon de notre juge : promouvoir sur tirages frais, pas sur les tirages qui ont servi à choisir.
- *Hors banc* : classes C4 et C5 tenues à l'écart, moniteur M_h d'une autre famille.

**Métrique.**
- T = [d′_hors(v*) − d′_hors(base)] / [d′_banc,frais(v*) − d′_banc,frais(base)].
- d′ est calculé sur les épisodes à violation contre les épisodes honnêtes de la même tâche, avec la vérité de terrain mécanique.
- Le taux de violation est rapporté **à part** : être plus surveillable n'est pas être plus honnête.

**Duel.**
- **H_A** : transfert, T ≥ 0,5.
- **H_B** : pas de transfert, T ≤ 0,1, valeurs négatives comprises.
- Seuils illustratifs. Si le dénominateur est indistinguable de 0 sur épisodes frais, il n'y avait pas de gain à transférer ; on le rapporte comme tel, sans conclure.

**Contrôles.**
- *Contrôle négatif 1* : une variante tirée au hasard parmi les 16. On attend un gain frais ≈ 0.
- *Contrôle négatif 2* : une sélection sur un banc placebo, aux étiquettes permutées. On attend un gain frais ≈ 0.
- *Cas honnêtes* : une hausse des fausses alertes sur les épisodes honnêtes, à détection égale, est comptée contre la variante.

**Issues.**
- T ≥ 0,5 falsifie H_B : la sélection sur banc est un remède plausible au premier ordre.
- T ≤ 0,1 falsifie H_A : le banc de surveillabilité, même sans gradient, n'est pas un instrument de sûreté hors de ses classes.

### Fiche 4 (organisme public) : couverture ou réutilisation, qu'est-ce qui fait passer une fausse méthode ?

**Problème.** Kirchner isole le banc tenu à l'écart par le système d'exploitation. Cet isolement protège contre la **fuite**. Il ne protège ni contre la **réutilisation** du banc pour choisir parmi les meneurs (S13), ni contre un **trou de couverture**.

Nos résultats montrent le second mode sur notre propre juge : en W2, recombinaison de lois de l'archive, une fausse loi a été promue dans 12 unités sur 12, **avec ou sans retour des verdicts** (nos résultats §3, RAPPORTÉ). Le premier mode, la réutilisation, n'est mesuré nulle part dans les pièces.

**Déjà connu, et l'écart.** La réutilisation adaptative d'un ensemble réservé est un thème établi de statistique (Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, « The reusable holdout: Preserving validity in adaptive data analysis », *Science*). L'apport ici n'est pas le principe : c'est la **décomposition chiffrée** entre réutilisation et couverture dans une boucle de la forme de celle de Kirchner.

**Plan factoriel sur l'organisme, avec les tricheurs scriptés existants.**
- *Règle* :
  - R1 : choix final par un banc réservé fixe, consulté à chaque sélection (n consultations) ;
  - R2 : processus de richesse sur tirages frais semés par l'empreinte de l'engagement (le juge actuel).
- *Classe* : dans la nulle (lignes v8) ou hors de la nulle (W2).
- *Retour des verdicts* : oui ou non.
- *Volume* : 1 000 courses par cellule pour les tricheurs scriptés (illustratif).

**Duel, sur les classes couvertes par la nulle.**
- **H_A** : la réutilisation est bénigne à cette échelle. Sous R1, le taux de fausse promotion reste ≤ 2α jusqu'à n = 16.
- **H_B** : la réutilisation domine. Sous R1, le taux monte vers la borne écrite d'avance 1 − (1 − α)ⁿ, qui vaut 0,560 à n = 16 (nos résultats §3, RAPPORTÉ). Le seuil d'acceptation de H_B est un taux ≥ 0,3 (illustratif).

**Duel secondaire, sur la classe hors nulle.**
- **H_A′** : R2 corrige aussi W2. Taux de fausse promotion ≤ 0,05.
- **H_B′** : R2 ne corrige pas W2. Taux ≥ 0,8, avec ou sans retour.
- A1 favorise H_B′ (RAPPORTÉ), mais avec des agents de langage. Le test sur scripts sert de réplication.

**Contrôle négatif.** Un proposeur aléatoire dans un monde sans signal : on attend un taux ≤ α sous R2. v8 donne déjà 0 sur 1 000 sur 11 lignes (RAPPORTÉ).

**Issues.**
- Si H_A tient et H_B′ aussi : pour une boucle à la Kirchner, le danger principal est la couverture. Il faut une équipe rouge des classes, pas des tirages frais.
- Si H_B tient : le banc réservé de Kirchner, s'il sert à choisir, doit être remplacé par des tirages frais.
- Les deux issues falsifient quelque chose.

---

## (c) Mesure minimale de chaque instrument nommé

Pour chaque instrument : taux de détection et de fausses alertes, cas honnêtes appariés, et vérification mécanique à battre. Un instrument fondé sur un modèle de langage qui ne bat pas la vérification mécanique à taux de fausses alertes égal n'ajoute rien pour cette classe (HYPOTHÈSE de méthode, pas un résultat).

| Instrument | Détection et fausses alertes | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| 1. Moniteur avant exécution (même modèle, lit le code, §3.2) | Rappel par classe interdite (données distillées, données de banc) au taux de fausses alertes fixé à 5 % (illustratif). | Même code avec des données licites de même taille et de même format. | Recouvrement exact et par n-grammes entre données d'entraînement et items des bancs, réserve comprise ; liste blanche des sources de données. |
| 2. Moniteur après coup (échafaudage Kale et coll., puis relecture Opus 4.8, §7) | Rappel par classe du §7 au taux de fausses alertes fixé ; r de la fiche 1 avec l'étage 1. | Relances déclarées avec toutes les graines ; propositions dont le code exécuté correspond au plan. | Décompte des exécutions par configuration dans les journaux et comparaison du meilleur score au maximum attendu sous la loi du bruit ; différence structurelle entre plan proposé et code exécuté. |
| 3. Classement (moyenne géométrique des fractions d'écart, §2.2) | Capacité à placer une méthode à gain réel nul sous une méthode à gain réel : stabilité des rangs en test-retest par nouvelles graines. | La même méthode rejouée. | Classement après tirage aléatoire des graines. Si le top-3 change autant sous ce seul bruit, il ne mesure pas les méthodes. |
| 4. Banc tenu à l'écart (§2.1, §3.2) | Détection de fuite : fuite plantée contre absence de fuite. Sur-optimisme : écart entre score réservé et score sur tirages frais, en fonction du nombre de consultations (fiche 4). | Méthodes jamais exposées. | Journaux d'accès du système d'exploitation, pour la fuite. Pour la réutilisation, aucune vérification mécanique ne suffit, d'où la fiche 4. |
| 5. Petri (Sonnet 4.6 auditeur et juge, A.6) | Ce n'est pas un détecteur : il faut sa fiabilité test-retest et sa discrimination entre un point de contrôle à comportement dégradé connu et sa base. | Le même point de contrôle réaudité. | Un juge plus simple, à grille fixe, sur les mêmes conversations. Avec une dispersion de l'ordre de 0,6 (D.3, RAPPORTÉ, « ± » non qualifié), un écart de 0,23 n'est pas interprétable sans cette mesure (calcul). |
| 6. Garde de capacité (réussite ou échec, §2.3) | Taux de bascule du verdict quand on réévalue deux fois les mêmes poids (fausses disqualifications et faux passages) ; rappel sur des méthodes plantées connues pour dégrader une capacité. | Mêmes poids réévalués. | Une comparaison directe à seuil sur les mêmes évaluations. **Annexe A.4 absente : je ne peux pas dire quel bruit est en cause.** |
| 7. Banc de surveillabilité (remède du §8.2) | d′ hors banc avec un moniteur tenu à l'écart (fiche 3) ; taux de fausses alertes sur épisodes honnêtes. | Épisodes sans violation, établis par vérité de terrain mécanique. | Les journaux de l'environnement eux-mêmes. Si la violation est mécaniquement observable, le banc doit faire mieux que les journaux sur les classes qu'ils ne voient pas. |
| 8. « Better control scaffolding » (§8.2) | Sûreté et utilité sous une équipe rouge (cadre de Greenblatt et coll., cité par Kirchner ; référence à vérifier pour le titre). | Exécutions honnêtes du même protocole. | Le protocole sans surveillance, mais avec les vérifications mécaniques 1 à 4. |
| 9. Notre juge statistique | Déjà mesuré (RAPPORTÉ) : 0 sur 1 000 sur 11 lignes fatales ; l'ancien nul promouvait l'artefact 395 fois sur 1 000. **Rappel attendu nul hors nulle par construction** : W2, 12 sur 12. | Lois neuves : coût en puissance de 0,005 et 0,020. | Sans objet. Ce qui reste à mesurer, c'est la couverture : liste des classes hors nulle, déterminée par équipe rouge. |
| 10. Seuil d'alarme séquentiel (si un moniteur de Kirchner passe en ligne) | Taux de fausses alertes sous effets d'épisode. | Épisodes honnêtes entiers. | Notre T0.3 (RAPPORTÉ) : le seuil de Ville unilatéral donne 0,21 à 0,35 de fausses alertes sous fort effet d'épisode ; un seuil calibré sur 1 000 épisodes honnêtes tient 0,046 à 0,055. Tout seuil doit être calibré sur des épisodes honnêtes entiers. |
| 11. Tricheurs scriptés et attaque A1 | Ce sont des étalons, pas des détecteurs. Leur mesure minimale est qu'ils fassent échouer l'ancien instrument (contrôle positif, 395 sur 1 000). | — | — |
| 12. Juges de modèles de langage (étage des fiches) | κ et écart propre famille contre autre famille, pas l'accord brut. | — | Chez nous, κ = 0 au plafond (RAPPORTÉ). |

---

## (d) Ancrage matériel

Sauf mention contraire, toutes les durées et tous les coûts de cette partie sont **illustratifs**. Les seules données des pièces sont : environ 30 minutes de carte graphique par méthode pour des cibles de moins de 7 milliards de paramètres (D.3) et 22 dollars par heure d'agent dans le faible-vers-fort (annonce du 14 avril). Toutes deux sont RAPPORTÉES.

| Fiche | Modèles ouverts | Calcul | Coût (illustratif) | Délai |
|---|---|---|---|---|
| 1 | Qwen2.5-72B-Instruct, GLM-4-32B, Llama-3.1-8B-Instruct, comme moniteurs | Inférence seule : environ 300 items × 3 familles × 2 moniteurs × environ 10 000 jetons, soit environ 18 millions de jetons (calcul sur supposé). De l'ordre de 10 à 50 heures-H100. | Quelques dizaines à quelques centaines de dollars. | Quelques jours, plus le temps de l'équipe rouge (le vrai goulot). |
| 2, étage 1 | Cible de moins de 8 milliards de paramètres ; moniteurs de la fiche 1 | Environ 300 méthodes × 0,5 heure-carte (la seconde valeur vient de D.3), soit environ 150 heures-carte (calcul sur supposé). | Quelques centaines de dollars. | Environ une semaine. |
| 2, étage 2 | Trajectoires d'Opus 4.8 | Chez Kirchner ; audit humain d'environ 100 méthodes non signalées (supposé). | Temps humain, non chiffrable ici. | Dépend de l'accès. |
| 3 | Llama-3.1-8B-Instruct (agent), 16 variantes, deux familles de moniteurs | Environ 16 × 600 épisodes, plus la notation par les moniteurs ; une à deux cartes pendant quelques jours. | Une à quelques centaines de dollars. | Quelques jours, plus la construction des environnements instrumentés. |
| 4 | Aucun pour les scripts ; un agent de langage en second temps (comme Argon en A1) | Processeur ; le code existe déjà (929 essais, RAPPORTÉ). | Négligeable pour les scripts. | Un à trois jours. |

**Ordre recommandé et raison.**
1. Fiche 1 d'abord : c'est la seule qui soit décisive sans agent et sans accès au harnais, et son issue H_B changerait directement le pipeline de Kirchner.
2. Puis fiche 4 sur l'organisme, faisable tout de suite.
3. Puis fiche 2, étage 1.
4. Fiche 3 en dernier : c'est la plus dépendante de S12.

**Ce qui me ferait réordonner.**
- Si l'annexe G de Kirchner contient déjà une mesure de rappel **par étage**, avec la corrélation entre étages, la fiche 1 passe derrière la fiche 2.
- Si la recherche de nouveauté de la fiche 1 renvoie un travail publié qui mesure l'excès de co-ratage entre moniteurs de même famille, la fiche 1 est retirée comme « déjà pris ».

FIN-DE-CELLULE