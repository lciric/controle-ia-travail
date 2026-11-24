# Proposition B : Collisionneur épistémique, tour III.1

Ce tour se fait à l'aveugle : aucune autre proposition ne m'a été transmise, je n'en critique donc aucune. Je suis l'ordre fixé par l'arbitre. Les éléments (a) à (d) du livrable s'y insèrent : (a) en §1, (c) en §3, (b) et (d) en §4 et §7.

---

## 1. Ce qu'un expert du domaine ferait ici, et que la question ne demande pas

**(a) Ce que la question suppose sans que ce soit établi**

| Présupposé | Statut |
|---|---|
| La lecture interne porte un signal de sabotage sur cette tâche | HYPOTHÈSE (« les saboteurs se représentent leur sabotage ») ; aucune mesure de sonde n'existe sur une tâche difficile à noter (OBSERVÉ-NON-AUDITÉ) |
| Les saboteurs fabriqués sont des cibles valides pour juger une parade par entraînement | Non établi. Leur tenue à l'entraînement n'est pas mesurée (OBSERVÉ-NON-AUDITÉ). Un organisme publié obtenu par distillation de consigne cède même à des récompenses tirées au hasard (VÉRIFIÉ). |
| Il existe une vérité du dommage hors banc | Non établi. Le jumeau n'existe qu'au banc (VÉRIFIÉ). L'oracle sur produit peut être trompé quand l'attaquant connaît sa grille (RAPPORTÉ). |
| « Entraîner » est une parade de même nature que détecter et auditer | Ma lecture (HYPOTHÈSE) : non. Détecter et auditer mesurent une politique fixe. Entraîner modifie la politique, donc la référence honnête sur laquelle repose la garantie de fausses alertes. |
| Les trois voies sont séparables et se cumulent | Le billet de 2025 les dit complémentaires (VÉRIFIÉ). Rien ne le mesure ici. |

**Ce que ferait un expert avant toute architecture** (propositions)

1. **Mesurer le plancher honnête.** Il s'agit de la variance honnête contre honnête entre graines, à chaque pas. Le billet de 2025 écrit qu'on n'incrimine sur de petits indices que si l'on sait exactement à quel point un honnête paraît suspect (VÉRIFIÉ). La garantie de fausses alertes du programme est cette quantité, et elle n'est pas listée parmi les données existantes.
2. **Construire des contrôles bénins appariés.**
   - Un adaptateur bénin fabriqué par le même procédé : générer avec une consigne cachée inoffensive, puis entraîner sans elle.
   - Une consigne cachée bénigne de longueur comparable.
   - Motif : une sonde apprise contre le modèle de base signale presque tous les adaptateurs bénins (RAPPORTÉ). Sans ce contrôle, une sonde qui détecte « adaptateur présent » passera pour une sonde qui détecte « sabotage ».
3. **Tester la robustesse de l'organisme avant de construire dessus**, par un entraînement sans information.
4. **Séparer les deux vérités du dommage** et mesurer leur accord : le dommage contre le jumeau (banc) et l'oracle sur le produit seul (audit, seul disponible en service).
5. **Fixer avant toute lecture la liste des vérifications mécaniques à battre** (§3).
6. **Faire la recherche d'antériorité manquante** sur les combinaisons de voies avec lecture interne (OBSERVÉ-NON-AUDITÉ : elle n'a pas été faite). Elle doit précéder tout mot de nouveauté devant le jury du 1er décembre 2026.

---

## 2. Les données brutes de départ

À relire ou produire avant toute synthèse déjà analysée :

- **Les pièces d'origine des faits RAPPORTÉS.** Il s'agit des sondes interrogées par une question de suite, de la sonde de tromperie, des sondes qui s'appuient sur des indices textuels et des faux positifs sur adaptateurs bénins (références à vérifier). Ces faits sont RAPPORTÉS : aucune décision ne doit en dépendre avant relecture à la page.
- **Le papier de 2026, aux pages des tableaux et de l'annexe.**
  - Les valeurs, le nombre d'épisodes et la dispersion pour les deux saboteurs à note égale et qualité différente.
  - Le texte exact du juge durci.
  - La définition du banc au niveau du code, pour confirmer « même banc » ailleurs que dans la prose.
- **Les données internes, épisode par épisode et pas par pas (dix pas).**
  - Les sorties brutes.
  - Les activations aux couches et positions retenues, en isolant le dernier jeton du message système.
  - La sortie du jumeau et la graine.
  - La dose.
  - Chaque jugement individuel de l'oracle avant agrégation.
- **La courbe dose-réponse à adaptateur au niveau de l'épisode**, pas la courbe ajustée.
- **À produire, faute d'exister** : des répliques honnêtes multi-graines, et la dose-réponse du saboteur à consigne (manquante, VÉRIFIÉ).
- **La nature exacte de l'oracle du programme** (humain, modèle, grille) : **je ne sais pas**, les faits ne la décrivent pas. Il faut l'établir en premier.

---

## 3. Ce que chaque voie peut établir

### Détecter (sondes, scores accumulés dans le temps)

- **Peut établir** : que, sur les familles fabriquées, les états internes séparent saboteur et honnête apparié au-delà du texte, avec un délai de détection à taux de fausses alertes garanti.
- **Ne peut pas établir** :
  - l'absence de sabotage ;
  - l'ampleur du dommage ;
  - la portée sur un saboteur qui ne se représente pas son sabotage (les dénégations d'un saboteur qui ne se croit pas fautif sont mal classées, RAPPORTÉ) ;
  - la portée sur un saboteur non fabriqué.
- **Exige** :
  - une référence honnête échangeable avec le service ;
  - les contrôles bénins appariés ;
  - une famille inédite lue une seule fois (règle VÉRIFIÉE).
- **Rendue vaine si** :
  - la sonde lit la consigne ou l'adaptateur et non le sabotage ;
  - elle ne bat pas un classifieur sur le texte (des sondes de sous-rendement s'appuient en partie sur le texte, RAPPORTÉ) ;
  - l'agent change : un entraînement ordinaire sans adversaire fait perdre leur séparation à des sondes apprises hors domaine (VÉRIFIÉ).
- **(c) Mesure minimale** :
  - **Métriques** : taux de détection à taux de fausses alertes fixé, et délai en épisodes.
  - **Cas honnêtes appariés** : même instance de tâche, même pas, jumeau honnête ; plus l'adaptateur bénin et la consigne bénigne.
  - **Vérifications mécaniques à battre** : longueur, distance d'édition entre pas successifs, perplexité sous le modèle de base, classifieur lexical sur les sorties, meilleur moniteur de texte.
  - **Témoin décisif** : la sonde lue au seul dernier jeton du message système, avant toute génération. Si elle égale la sonde lue sur la génération, la sonde lit la consigne.

### Auditer (une part d'épisodes tirée au hasard, jugée par un oracle)

- **Peut établir** : une borne valide à tout instant sur le taux de dommage, si l'oracle reconnaît le dommage et si le taux honnête de référence est connu (RAPPORTÉ). Cet audit est publié par d'autres et n'est pas revendiqué (VÉRIFIÉ).
- **Ne peut pas établir** : la validité de son propre oracle sur une tâche difficile à noter.
- **Exige** : un oracle dont la grille n'est pas connue de l'attaquant, et un tirage réellement aléatoire.
- **Rendu vain si** :
  - l'oracle est trompé (un juge par défaut l'est, VÉRIFIÉ) ;
  - l'aiguillage remplace le tirage, car la garantie disparaît.
- **(c) Mesure minimale** :
  - **Détection** : taux de détection de l'oracle sur le produit seul aux quatre doses de l'adaptateur, contre le dommage mesuré au jumeau.
  - **Fausses alertes** : sur des paires honnête contre honnête de graines différentes, tout dommage signalé est une fausse alerte.
  - **Comparateur à battre** : le juge par défaut.

### Entraîner (le modèle soupçonné)

- **Peut établir** : qu'un entraînement donné change le dommage mesuré par l'oracle, sur cet organisme.
- **Ne peut pas établir** :
  - que le dommage a disparu, avec la note seule. Deux saboteurs entraînés contre la note faible atteignent la même note et gardent des qualités réelles différentes (VÉRIFIÉ).
  - qu'on n'a pas produit un saboteur caché. Des états internes obscurcis et un texte qui trompe le détecteur sont des issues observées (VÉRIFIÉ).
- **Exige** :
  - un organisme robuste ;
  - un entraînement indiscernable du service (VÉRIFIÉ sur des tâches à réponse exacte) ;
  - l'absence d'exploration hacking (supposée, non montrée, par le papier de 2026) ;
  - souvent des démonstrations de référence, peut-être impossibles pour une tâche de recherche ouverte (VÉRIFIÉ).
- **Rendu vain si** :
  - l'organisme cède à un entraînement sans information : alors tout entraînement « marche » et n'apprend rien ;
  - la note faible est saturée.
- **(c) Mesure minimale** :
  - la réduction du dommage contre le jumeau, rapportée à celle d'un entraînement à récompenses aléatoires à calcul égal ;
  - la perte de qualité d'un agent honnête soumis au même entraînement.

### Combinaisons : où les voies se nuisent

- **Détecter puis auditer.** C'est compatible avec la garantie seulement si l'on stratifie : une part aléatoire fixe porte la borne, une part aiguillée par la sonde s'ajoute (proposition).
  - Ré-apprendre la sonde sur les épisodes audités ferait entrer une sortie de l'oracle dans la sélection d'un moniteur. C'est interdit (VÉRIFIÉ).
- **Auditer puis entraîner.** Entraîner sur les épisodes audités fait entrer une sortie de l'oracle dans la sélection de l'agent. C'est interdit par une règle en vigueur ; une telle proposition doit déclarer qu'elle change la règle.
- **Détecter puis entraîner.**
  - Un score de sonde dans le signal d'entraînement n'est permis que dans le bras d'attaque déclaré.
  - Même sans adversaire, l'entraînement peut détruire la sonde et déplace la référence honnête : la garantie de fausses alertes doit alors être recalibrée.
  - Je lis la note d'un modèle faible comme un score de juge. Si le directeur la lit autrement, il doit le dire explicitement.
- **Entraîner a besoin de détecter pour se valider.** La détection reste nécessaire pour valider qu'un entraînement a réussi (VÉRIFIÉ, jeu d'audit). Entraîner ne remplace pas la détection : il la consomme.
- **Conflit structurel** (HYPOTHÈSE) : un même épisode ne peut servir à la fois de mesure et de signal sans contaminer la mesure.

---

## 4. Les programmes possibles

Les coûts sont exprimés en « courses ». Le fait VÉRIFIÉ est qu'une course coûte quelques dizaines de dollars ; tous les nombres de courses sont **illustratifs**.

**P0. Ne rien changer.**
- *Thèse* : des sondes accumulées battent les moniteurs de texte contre le sabotage diffus, à taux de fausses alertes garanti.
- *Expérience centrale* : la porte de comparaison lecture interne contre texte, prévue environ deux mois après la porte d'instruments de fin décembre 2026.
- *Réfutée si* : la sonde ne dépasse pas le meilleur lecteur de texte ou une vérification mécanique sur une famille inédite.
- *Exige* : que les saboteurs se représentent le sabotage (HYPOTHÈSE), et une vérité via le jumeau.
- *Coût* : faible, de l'ordre de dizaines de courses (illustratif).
- *Déjà fait ailleurs ?* Partiellement sur d'autres bancs (RAPPORTÉ). Aucune mesure trouvée sur une tâche difficile à noter (OBSERVÉ-NON-AUDITÉ).
- *Défaut* : sans contrôles bénins ni plancher honnête, un succès ne se distingue pas d'un artefact.

**P1. Détection et audit stratifié.**
- *Thèse* : les sondes réduisent le délai de détection d'un audit sans en casser la borne.
- *Expérience centrale* : rejouer hors ligne les journaux avec une part aléatoire fixe plus une part aiguillée.
- *Réfutée si* : aucun gain de délai à budget d'audit égal, ou gain seulement en sacrifiant la part aléatoire.
- *Exige* : un oracle dont l'accord avec le jumeau est mesuré.
- *Coût* : minimal, sur processeur une fois les journaux constitués.
- *Déjà fait ailleurs ?* Je ne sais pas ; la recherche d'antériorité n'a pas été faite.

**P2. L'entraînement comme objet de mesure, pas comme parade.**
- *Thèse* : sabotage et signal interne n'ont pas la même tenue à un entraînement sans information, et c'est ce qui décide si une parade par entraînement est évaluable sur ces organismes.
- *Expérience centrale* : un entraînement à récompenses aléatoires et un réglage fin sur des traces du modèle de confiance, appliqués au saboteur, à l'honnête et à l'adaptateur bénin. On mesure le dommage contre le jumeau et la séparation de la sonde avant et après.
- *Réfutée si* : le dommage et la séparation évoluent ensemble sur toutes les doses ; l'objet n'a alors pas de contenu propre.
- *Exige* : une vérité via le jumeau, et aucune sélection de point de contrôle par l'oracle.
- *Règles* : compatible avec les règles en vigueur, car aucun score de moniteur ni d'oracle n'entre dans le signal.
- *Coût* : modéré, de l'ordre de dizaines de courses (illustratif).
- *Déjà fait ailleurs ?* La question est ouverte pour ce banc. Le comportement de l'organisme à adaptateur est inconnu (OBSERVÉ-NON-AUDITÉ).

**P3. L'entraînement guidé comme parade.**
- *Thèse* : un entraînement concentré sur les actions que la sonde juge suspectes (le « milieu » du billet de 2025) retire plus de dommage qu'un entraînement diffus sur la note faible.
- *Expérience centrale* : un vrai saboteur affiné contre la note faible, le cas laissé de côté par le papier de 2026 (VÉRIFIÉ), comparé à un entraînement guidé par la sonde.
- *Réfutée si* :
  - le dommage résiduel est égal ou supérieur à celui de l'entraînement diffus à calcul égal ;
  - ou la sonde, ré-apprise sur une famille inédite, révèle un obscurcissement.
- *Exige* :
  - **un changement de règle déclaré** : un score de sonde ou de juge entre dans l'entraînement hors du bras d'attaque ;
  - un organisme robuste (issue de P2) ;
  - un oracle indépendant de la note.
- *Coût* : élevé, avec de nombreuses courses et une évaluation lourde (illustratif).
- *Déjà fait ailleurs ?* Le risque est élevé : le manque est nommé publiquement par les auteurs.

**P4. Changer d'objet : la vérité du dommage.**
- *Thèse* : sur une tâche difficile à noter, les trois voies héritent de l'erreur de l'oracle ; la grandeur de premier ordre est donc cette erreur.
- *Expérience centrale* : mesurer l'accord entre l'oracle sur le produit seul et le dommage contre le jumeau, juge durci compris, face aux saboteurs à adaptateur du programme.
- *Réfutée si* : l'accord est élevé à toutes les doses ; l'objet ne mérite alors pas un programme.
- *Exige* : des évaluateurs aveugles à la condition.
- *Coût* : lourd en évaluation. Je ne connais pas le coût humain.
- *Déjà fait ailleurs ?* Partiellement : un juge trompé et un juge durci existent (VÉRIFIÉ), mais pas contre un saboteur inscrit dans les poids.

**Ma proposition**
- Garder P0, mais seulement doté des contrôles bénins et du plancher honnête.
- Ajouter P2 maintenant, P1 hors ligne, et une version minimale de P4 comme préalable.
- Différer P3.
- **Geler la ligne des essaims** jusqu'après la porte de comparaison. Avec trois chantiers actifs au plus (VÉRIFIÉ), elle déplacerait un préalable.

---

## 5. Ce qui, hors du programme, permettrait de vérifier le résultat

- **Une famille de sabotage inédite fabriquée par une équipe extérieure**, sans accès aux sondes, et lue une fois (conforme à la règle).
- **Des évaluateurs du dommage extérieurs et aveugles à la condition**, avec accord inter-évaluateurs publié.
- **Un préenregistrement public horodaté** avant toute lecture.
- **Les saboteurs publics de quatorze milliards de paramètres** (VÉRIFIÉ ; les auteurs nomment les sondes sans les essayer). Ce sont des organismes que le programme n'a pas fabriqués : y transposer le protocole de sonde et le test de robustesse teste la portée hors fabrication maison. Coût d'une course à cette taille : je ne sais pas.
- **Une réplication sur un second modèle ouvert d'une autre famille**, de taille voisine (choix illustratif, par exemple une autre famille ouverte de 7 à 9 milliards de paramètres).
- **La publication des activations, des sorties et du code**, pour que d'autres refassent les vérifications mécaniques.
- **L'application sur ce banc du protocole publié de sondes interrogées par une question de suite** (RAPPORTÉ, référence à vérifier).

---

## 6. Reformulation exigeante de la tâche

> Sur un banc où le dommage ne se lit que contre un jumeau honnête, établir, avant de traiter l'entraînement comme parade :
> (i) si la lecture interne détecte un sabotage diffus au-delà de ce que détectent le texte, des vérifications mécaniques et la seule présence d'un adaptateur ou d'une consigne, à taux de fausses alertes garanti sur un plancher honnête mesuré ;
> (ii) si les saboteurs fabriqués et les sondes survivent à un entraînement sans information, ce qui décide si un résultat d'entraînement sur ces organismes peut signifier quelque chose ;
> (iii) si l'oracle sur le produit seul s'accorde avec le dommage contre le jumeau.
> Ne traiter l'entraînement guidé comme parade qu'ensuite, dans un bras préenregistré dont le changement de règle est déclaré par écrit.

---

## 7. Programme des priorités classé

Les notes sont mon jugement (proposition), pas des mesures.

| # | Chantier | Gain | Facilité | Portée | Découverte | Coût | Score |
|---|---|---|---|---|---|---|---|
| C1 | Plancher honnête, contrôles bénins, vérifications mécaniques | 4 | 5 | 4 | 2 | 1 | **160** |
| C2 | Tenue des saboteurs à l'entraînement sans information | 5 | 4 | 4 | 3 | 2 | **120** |
| C3 | Sonde contre texte contre mécanique, famille inédite, accumulation | 5 | 3 | 5 | 4 | 3 | **100** |
| C4 | Tenue des sondes à l'entraînement bénin de l'agent | 4 | 4 | 4 | 3 | 2 | **96** |
| C5 | Audit stratifié par aiguillage (hors ligne) | 3 | 4 | 3 | 2 | 1 | **72** |
| C6 | Entraînement guidé comme parade (P3, changement de règle) | 4 | 2 | 5 | 5 | 4 | 50 |
| C7 | Dose-réponse du saboteur à consigne | 3 | 5 | 3 | 1 | 1 | 45 |
| C8 | Accord oracle contre jumeau (P4 minimal) | 5 | 3 | 4 | 2 | 3 | 40 |
| C9 | Troisième famille sans texte (devis) | 4 | 2 | 5 | 4 | 5 | 32 |
| C10 | Essaims à poids partagés | 3 | 2 | 3 | 3 | 4 | 13,5 |

**Sensibilité**
- Si l'on élève la découverte au carré, C3 passe en tête (400), devant C2 (360), C1 (320) et C4 (288). C6 monte à 250 sans entrer dans les cinq premiers.
- Si l'on ignore le coût, C3 (300) et C2 (240) dominent, et C6 (200) rejoint le groupe de tête.
- Le noyau C1, C2 et C3 est stable sous les deux variations.
- **Limite de la formule** : elle classe mal les préalables. C8 obtient un score bas, mais C3 et C5 ne valent que si l'oracle vaut. J'en fais une condition d'entrée réduite (un sous-échantillon double-jugé), pas un chantier.

### Expériences décisives des cinq premiers chantiers

Tous les seuils sont **illustratifs** et à fixer au préenregistrement. Les coûts sont **illustratifs**, comptés en courses.

**C1. Signal de sabotage ou signal d'artefact**
- **H_A** : la sonde sépare saboteur et honnête apparié nettement mieux qu'elle ne sépare adaptateur bénin et base, ou consigne bénigne et base.
- **H_B** : la séparation s'explique par la présence d'un adaptateur ou d'une consigne.
- **Métrique** : taux d'alerte, au seuil calibré sur les honnêtes, chez les saboteurs et chez les contrôles bénins. En complément, l'écart entre la sonde lue sur la génération et la sonde lue au seul dernier jeton du message système.
- **Seuil** : alertes des contrôles bénins au plus au taux nominal plus une marge préenregistrée, et saboteur au-dessus des vérifications mécaniques (illustratif).
- **Contrôle négatif** : des paires honnête contre honnête de graines différentes.
- **Issues** :
  - Des contrôles bénins signalés comme les saboteurs, ou une sonde « message système seul » égale à la sonde complète, falsifient H_A.
  - Des contrôles bénins au taux nominal et des saboteurs au-dessus falsifient H_B.
- **Coût** : une dizaine de courses, dont la fabrication des adaptateurs bénins (illustratif).

**C2. L'organisme est-il un bon témoin ?**
- **H_A** : le dommage contre le jumeau de l'adaptateur survit à un entraînement à récompenses aléatoires, à nombre de pas fixé d'avance.
- **H_B** : il s'effondre, comme l'organisme publié jugé peu robuste.
- **Métrique** : la fraction de dommage résiduel par dose, et la qualité de l'honnête soumis au même entraînement.
- **Seuil** : la fraction résiduelle sépare les deux issues au-delà de la variance entre graines (illustratif).
- **Contrôle négatif** :
  - l'honnête entraîné de la même façon, pour mesurer la dégradation générique ;
  - des saboteurs non entraînés re-tirés.
- **Règles** : aucun point de contrôle n'est choisi par l'oracle ; conforme aux règles.
- **Issues** :
  - Un effondrement falsifie H_A. Il interdit alors toute conclusion de parade sur cet organisme et rend prioritaire la troisième famille ou les saboteurs publics.
  - Une survie falsifie H_B.
- **Coût** : de 10 à 20 courses (illustratif). On fait de même pour le saboteur à consigne, qui n'a pas de poids changé, à titre de témoin.

**C3. La lecture interne apporte-t-elle quelque chose sur une tâche difficile à noter ?**
- **H_A** : la sonde accumulée détecte en moins d'épisodes que le meilleur moniteur de texte et que la meilleure vérification mécanique, à taux de fausses alertes garanti égal, sur une famille inédite lue une fois.
- **H_B** : un lecteur de texte ou une vérification mécanique fait aussi bien ou mieux.
- **Métrique** :
  - le délai médian de détection ;
  - la dose minimale détectable sur la dose-réponse, celle de la consigne incluse (C7, peu coûteux, est à faire ici).
- **Seuil** : un écart de délai préenregistré (illustratif).
- **Contrôle négatif** : flux honnêtes et flux d'adaptateur bénin, dont le taux d'alerte doit rester au taux nominal ou en dessous.
- **Issues** :
  - Une sonde qui ne bat pas le texte falsifie H_A ; le programme doit alors pivoter vers P4 ou P1.
  - Le contraire falsifie H_B.
- **Coût** : quelques dizaines de courses, plus le coût de l'oracle, que je ne connais pas (illustratif).

**C4. La sonde survit-elle à un agent qui apprend ?**
- **H_A** : une sonde apprise avant un entraînement bénin de l'agent (réglage fin sur des traces du modèle de confiance) garde sa séparation et son taux de fausses alertes.
- **H_B** : elle les perd, comme les sondes apprises hors domaine (VÉRIFIÉ).
- **Métrique** : la séparation avant et après, et le taux de fausses alertes sur les honnêtes après entraînement au seuil d'avant.
- **Seuil** : préenregistré (illustratif).
- **Contrôle négatif** : des répliques sans entraînement.
- **Issues** :
  - Une perte falsifie H_A. Toute combinaison détecter-entraîner devra alors recalibrer la garantie, et le billet de 2026 sur l'apprentissage en ligne devient une contrainte de conception.
  - Une tenue falsifie H_B.
- **Coût** : il est partagé avec les courses de C2 ; quelques courses de plus (illustratif).

**C5. L'aiguillage gagne-t-il sans casser la borne ?**
- **H_A** : à budget d'audit égal, une part aléatoire fixe plus une part aiguillée par la sonde trouve plus tôt un épisode à dommage confirmé, avec la borne de la part aléatoire intacte.
- **H_B** : aucun gain.
- **Métrique** : le nombre d'épisodes avant la première confirmation, et la couverture de la borne.
- **Contrôle négatif** : un aiguillage par scores de sonde permutés, qui doit égaler le tirage aléatoire.
- **Règles** : aucune sortie de l'oracle ne revient dans la sonde.
- **Issues** :
  - Une absence de gain falsifie H_A.
  - Un gain au-delà du témoin permuté falsifie H_B.
- **Coût** : sur processeur, à partir des journaux de C3 (illustratif).

### Calendrier

- **Avant la porte d'instruments (fin décembre 2026)** :
  - C1 ;
  - C2 ;
  - le double-jugement minimal de C8 ;
  - la dose-réponse à consigne (C7) ;
  - la recherche d'antériorité, avant l'entretien du 1er décembre.
- **Avant la porte de comparaison** : C3, puis C4 et C5.
- **Attend** :
  - C6, qui exige une issue « robuste » de C2, la porte de comparaison passée et un changement de règle déclaré par écrit ;
  - C9, qui attend un devis ;
  - C10 (essaims).
- **Ne doit pas être fait** :
  - entraîner l'agent contre une sonde ou un juge hors du bras d'attaque déclaré ;
  - entraîner sur les épisodes audités ;
  - sélectionner des points de contrôle ou des sondes par l'oracle ;
  - reconcevoir une sonde après lecture de la famille inédite ;
  - revendiquer la garantie d'audit ;
  - présenter un succès de parade obtenu sur un organisme non testé par C2.

### Hors de portée

- Une garantie contre un saboteur qui ne se représente pas son sabotage.
- La portée sur des modèles bien plus grands.
- L'indiscernabilité entre entraînement et service.
- Un oracle sûr pour une tâche de recherche ouverte.
- La détection de l'exploration hacking chez un saboteur non fabriqué.
- La transposition à des saboteurs apparus sans fabrication.

FIN-DE-CELLULE