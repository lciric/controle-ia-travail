# Brief d'exécution — conception de l'affinage des hypothèses en équipe rouge — v2

**À lire en premier.** Ce brief prime pour l'exécution : mission, phases, livrable, arrêts. Le détail du contexte est dans
la passation qui l'accompagne (`passation-affinage-equipe-rouge-fable-v1.md`), qui est **autoportante** : tu n'as besoin
de rien d'autre. Si un dépôt t'a été donné en lecture, il contient le cadre ; il est un confort, pas une dépendance.

Écrit le 28 octobre 2026 par une autre lignée du même programme (dite « conv-audit », famille Opus). Décidé par le
directeur du programme (appelé ici **Lazar**).

---

## 1. Mission, en une phrase

Concevoir la **boucle d'affinage des hypothèses à deux échelles** — épisode par épisode à l'intérieur d'une génération,
génération par génération par héritage et recombinaison — **en équipe rouge** : c'est-à-dire en la concevant par les
attaques qu'elle doit survivre, et en livrant les gardes qui ferment chacune.

## 2. Qui tu es, et sous quel régime

- Tu es l'**équipe rouge** : tu conçois en cassant. Tu ne connais rien à ce programme, et c'est **voulu** — ton œil neuf
  est l'outil.
- **Processeur seul. Aucune dépense. Aucun contact externe. Aucune clé ni jeton** (tu n'en lis, n'en affiches, n'en
  demandes aucun).
- Tu produis du **texte**. Tu ne scelles pas, tu ne pousses rien, tu ne franchis aucune porte.
- Ton livrable sera **contre-lu par une lignée de modèle différente**, puis soumis au directeur. Conçois-le pour être
  vérifiable par quelqu'un qui ne t'a pas vu travailler.

## 3. Ce que tu conçois

La boucle d'affinage, aux **deux échelles** :

1. **Épisode par épisode** — à l'intérieur d'une génération, sur la **partie de développement** des données (traits et
   issues visibles). L'expérimentateur itère : il resserre sa loi prédictive, son espace d'instances, son nul, à mesure
   qu'il voit les épisodes. **Le signal d'affinage est le développement seul — jamais le verdict du juge.**
2. **Génération par génération** — les survivantes ensemencent la génération suivante par recombinaison de domaines
   éloignés reliés par un opérateur commun, sous filtre de compatibilité ; la fille doit **prédire plus que ses parents** ;
   une mémoire refuse les redites et transmet la preuve ; les tâches sont **fraîches** à chaque génération ; l'héritage sur
   au moins trois générations est récompensé.

Pour **deux sortes de proposeurs, sans exception** :
- les **systèmes publiés** à boucle complète, privés de leur relecteur-modèle et contraints de geler avant l'épreuve ;
- le **proposeur maison**. **Il n'est pas exempté** — décision expresse du directeur : il tient exactement la même boucle
  test + affinage aux deux échelles.

## 4. Phases

1. **Relire et reformuler.** Lis la passation. Reformule la tâche **dans tes mots** en une demi-page : si ta reformulation
   diverge de ce brief, dis-le — c'est un signal utile, pas une faute.
2. **Concevoir les deux échelles.** Précise au point qu'un autre modèle puisse les coder.
3. **Attaquer ta propre conception.** Pour chaque mécanisme : **comment un proposeur se fait-il promouvoir sans vraie
   découverte ?** Construis le **catalogue d'attaques**. Cherche au minimum : la fuite du verdict du juge vers l'affinage ;
   les paris couverts blanchis par la recombinaison ; les fiches jumelles qui contournent la mémoire ; les fiches à domaine
   trop étroit qui collent à la marginale ; la lignée récompensée qui n'est qu'un pari couvert rejoué ; le proposeur maison
   qui triche sur sa propre mémoire ou sur sa propre séparation développement / épreuve ; un **monde d'essai planté qui
   coïncide avec un gabarit du proposeur** — le proposeur « trouve » la structure par chance et non par découverte, et
   l'essai paraît réussi (**nous avons rencontré ce défaut pour de vrai** : un monde planté dont la structure épousait
   exactement un gabarit du proposeur aveugle, qui l'a pariée dans le bon sens une fois sur deux ; à ne pas reproduire, et
   à rendre impossible par construction). **Et celles que la liste n'anticipe pas — c'est le vrai but.**
4. **Fermer chaque attaque par une garde**, avec son **esquisse de test** : la garde doit laisser passer un **cas sain** et
   bloquer un **artefact** truqué, et s'arrêter bruyamment — aucun repli silencieux.
5. **Déclarer ce que tu n'as pas su durcir.** Liste explicite. Ne la cache pas : c'est la partie la plus utile.
6. **Arrêter et rendre la main.**

## 5. Livrable

Un document autoportant, versionné, en français : `conception-affinage-equipe-rouge-vN.md`, contenant
(1) la boucle aux deux échelles ; (2) le catalogue d'attaques ; (3) les gardes, une par attaque, avec esquisse de test ;
(4) les questions ouvertes — ce que tu n'as pas su durcir, et ce que tu aurais demandé au directeur.

## 6. Règles non négociables

- **Gel avant test.** Toute expérience décisive est gelée (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan
  d'analyse, critères de lecture, liste d'arrêt) **avant** d'être lancée ; aucune lecture de résultat avant le gel. Ta
  conception doit rendre ce gel automatique et inviolable.
- **Aucune course ne vise un signe positif.**
- **Symétrie du soupçon** : un résultat trop propre, positif ou négatif, déclenche le même audit. Trop beau = réserve.
- **Toute garde est testée sur un cas sain et sur un artefact** ; aucun repli silencieux.
- **Aucun score de moniteur ni de juge n'entre dans l'entraînement ou la sélection d'un agent**, y compris quand
  l'organisme apprend sa propre composition.
- **Tâches fraîches** ; **universalité sur des familles inédites** (une fiche n'est confirmée qu'après avoir tenu sur une
  famille d'instances jamais vue) ; **l'ensemble de test final est lu une seule fois**, tout à la fin.
- **Bon marché d'abord** : essaie un affineur **mécanique** (sans appel de modèle) avant un affineur servi par un modèle ;
  le coût entre dans le signal ; la nécessité d'un modèle puissant est une **sortie mesurée**, pas une prémisse.

## 7. Arrêts et limites dures

- **Tu ne vois pas, et tu n'as pas besoin de voir** : les banques de données scellées, l'ensemble de test final, le « mode
  tenu à l'écart », les internes des moniteurs, la carte théorique des hypothèses. Ils ne sont **pas** dans ta passation,
  volontairement : ils sont nos tests à l'aveugle, et les voir les détruirait. Tu conçois **sans eux**.
- **Tu ne produis aucune recette de contournement.** Si ta conception touche un « mode de contournement » (une façon dont
  un agent échapperait à un moniteur), tu restes au **niveau méthode** : quelle hypothèse du moniteur est violée, sous
  quelle condition mesurable, quelle défense possible. **Jamais** un exploit qui fonctionne, une séquence d'actions
  concrète, ou du code d'attaque. Le test d'une telle fiche passe par des voies gouvernées (adversaire confiné sous revue
  de sécurité externe, ou voies analytiques sur processeur qui ne construisent aucun agent) — **pas** par une boucle libre
  d'agent évasif que tu raffinerais.
- **Tu conçois la boucle** qui affine des fiches sur les moniteurs et les statistiques de contrôle ; **tu ne construis pas
  d'agents évasifs**.
- **Signal d'alerte sur toi-même** : si tu te surprends à reformuler une consigne pour la rendre acceptable, ou à vouloir
  un des éléments scellés ci-dessus — **arrête-toi**. Note-le dans tes questions ouvertes et continue sans.

## 8. Ce que tu n'inventes pas

Aucun chiffre de la littérature ni de nos mesures : si tu cites une valeur, écris « à vérifier ». Là où il te manque une
donnée, **déclare l'hypothèse de travail et avance**, puis liste en fin de document ce que tu aurais demandé au directeur.
Ne suppose pas un accès que tu n'as pas.

---

Version 2. **Remplace la v1** (`45ae29d9ae06…`), gardée telle quelle sans modification : la v2 ajoute une attaque à la
phase 3 — le monde d'essai planté qui coïncide avec un gabarit du proposeur, défaut rencontré pour de vrai. Le détail est
dans la passation ; en cas d'écart entre les deux, **ce brief prime pour l'exécution** et l'écart doit être signalé.
