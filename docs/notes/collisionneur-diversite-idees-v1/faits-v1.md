# Faits pour le collisionneur : diversifier les idées des proposeurs de l'organisme d'idéation — v1

Résumé écrit le 12 novembre 2026 (début à 20:13 UTC, heure relevée par `date -u`) par un opérateur neuf de la session mère
(Claude Opus 5.5), qui n'a écrit ni le verdict résumé, ni la course, ni le collisionneur. Sources : le verdict scellé de la
course v67 de l'organisme, `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md`
(sha256 `d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459`, empreinte vérifiée), sections 4.2, 4.5, 5 et 6 ;
le texte scellé de la course (préenregistrement v2, `80fe4f03…`), sections 0, 1, 3.5 à 3.7, pour la seule mécanique ; le
registre des décisions du programme, lignes R-2441 à R-2443.

**Filtre volontaire.** Ce fichier ne contient **aucune loi plantée** (ni vraie, ni fausse, ni cas d'instrument), aucun
paramètre de la loi du monde, aucun paramètre de la loi connue de départ, aucune taille d'effet du monde. Le collisionneur
conseille sur la conception ; il n'est ni proposeur ni juge de l'organisme, et il ne doit pas voir ce qu'un proposeur ne voit
pas.

**Statuts.** VÉRIFIÉ : relu par l'opérateur dans le fichier cité. RAPPORTÉ : dit par le verdict, le texte scellé ou le
registre, non revérifié. HYPOTHÈSE : supposition. Les nombres ci-dessous sont des mesures rapportées par le verdict, sauf
mention « illustratif ».

## 1. L'organisme d'idéation (mécanique de la course v67)

- **Monde planté** (RAPPORTÉ) : un monde jouet, « S-V1 », dont la loi est connue de l'expérimentateur humain (l'oracle) :
  une loi de probabilité sur **3 issues**, à partir de **2 traits réels** (z0, z1) et de 2 sous-populations. Chaque épisode
  donne des traits et une issue tirée de la loi cachée.
- **Grammaire des lois** (VÉRIFIÉ dans `orchestrator/pole/evaluateur_lois_v62.py` du dépôt public de l'organisme) : six
  formes, `fixe`, `softmax` (poids par issue et par trait, biais), `par_sous_population`, `melange`, `si_sinon` (condition sur
  un trait et un seuil, ou sur la sous-population), `transformee` ; bornes ±4 sur les coefficients (RAPPORTÉ). Une loi est
  une fiche au gabarit fermé {énoncé, loi prédictive}.
- **Archive de départ** (RAPPORTÉ) : une loi connue, **K1**, déclarée d'avance, qui n'utilise que le trait z0 ; « informative
  mais faible ».
- **Proposeurs** (RAPPORTÉ) : **Kimi** (`kimi-k3.1-pro`) et **Argon** (`gemini-4-argon`), chacun derrière un relais local qui
  tient la clé ; **un appel par fournisseur et par génération**, au plus 6 lois chacun. Ils reçoivent une **vue** : la
  description publique du monde, la grammaire, et les lois de l'archive (K1 plus les lois retenues), **jamais un verdict**.
  **Aucun modèle de la famille Claude** ne joue de rôle dans l'organisme : les lois plantées du monde S-V1 ont été écrites par
  un modèle de cette famille (texte scellé, section 3.5).
- **Gardien** (RAPPORTÉ) : mécanique (grammaire, bornes, évaluation sur un jeu factice fixe), aucun modèle.
- **Juge** (RAPPORTÉ) : statistique, calculé par l'orchestrateur hors de tout agent, sur un **engagement scellé** avant les
  données. Pour chaque fiche : **valeur e** contre un **nul** (« nul v8 ») qui contient **les lois de l'archive de la
  génération** (K1 et les lois déjà retenues), une bibliothèque de lois aveugles fixes, et une classe de **recombinaisons**
  de ces lois (copie renommée, mélange avec l'uniforme, mélange avec une loi aveugle, loi tempérée et inclinée) ;
  200 tirages frais par fiche ; règle de Benjamini et Hochberg sur les valeurs e, m fixé à 22 ; seuil le plus strict
  log(22/0,05) ≈ 6,09. Une fiche qui n'apporte rien au-delà de l'archive et de ses recombinaisons n'est pas promue : c'est la
  **garde contre les copies**.
- **Limite connue du juge** (RAPPORTÉ, texte scellé section 1 et verdict section 6) : il tient dans la classe de tricheries
  que son nul couvre et **cède hors d'elle** (audit A1-v3 : « brèche hors classe établie », 24 sur 24 sur un autre monde) ;
  la classe non couverte comprend des recombinaisons par morceaux, des produits et des compositions de lois connues.
- **Test de mort** (RAPPORTÉ) : chaque loi promue est exécutée dans un bac isolé (`bwrap`, sans réseau) par un
  expérimentateur (Kimi) ; test imposé : gain moyen par épisode du log-score sur la marginale empirique d'une tranche de
  400 épisodes frais, seuil « au moins 0,02 » nat ; verdict calculé par l'orchestrateur sur le fichier brut. Argon vérifie,
  témoin seulement.
- **Sélection et génération suivante** (RAPPORTÉ) : sont retenues les lois promues **et** survivantes ; la génération
  suivante lit la sélection scellée, sert aux proposeurs l'archive augmentée, et juge contre elle.

## 2. Ce que la course v67 a donné (RAPPORTÉ, verdict sections 4.2, 4.5, 5)

- **Issue confirmée C1** : « la chaîne garde (classe couverte, ce monde, cette taille) » ; une génération et demie ; rien sur
  la qualité ni la diversité des idées.
- **Génération 1** : 11 fiches réelles jugées (Kimi en a rendu 5, Argon 6), **toutes promues** (log e de 6,68 à 14,58),
  **toutes survivantes** au test de mort, toutes « vraies » selon l'oracle. Le verdict l'explique sans fuite : **K1 ignore le
  trait z1 ; toute loi qui ajoute z1 bat nettement K1**. Ces 11 lois sont des **variantes proches d'un même constat**
  (ajouter z1) ; trois lois de Kimi partagent la même base ; « ce ne sont pas 11 idées » (réserve R-5). Certaines sont de
  forme `si_sinon` ou `par_sous_population`.
- **Génération 2** : archive = K1 plus les 11 retenues (37 membres dans le nul) ; 12 fiches réelles jugées, **aucune promue**
  (log W maximal de −1,08 à −6,40) ; donc aucun test de mort, sélection vide. Des **copies renommées** de quatre retenues,
  plantées par l'orchestrateur, sont refusées en course et seraient toutes promues si la sélection n'était pas lue : la garde
  contre les copies a fonctionné.
- **Lecture du verdict** : 12 refus sur 12 en génération 2 « ne disent rien d'une capacité à progresser au-delà » ; le compte
  de la génération 1 ne dit rien de la diversité.
- **Recherche de fuite** (verdict 4.5) : une recherche mécanique de la loi plantée dans les contextes servis aux proposeurs
  a signalé deux touches numériques en génération 2, relues comme **coïncidence** (un nombre rond d'une loi retenue) ; la
  réserve R-1 demande de les rapporter. Fuite de la tranche dans les contextes : aucune.
- **Réserve R-2** : la réponse brute des proposeurs n'a pas été gardée (dossier des sessions vide) ; aucun témoin
  d'isolement par test n'est versé.
- **Coût** : modèles 1,99 USD pour toute la course (Kimi 1,14, Argon 0,86 ; 46 appels relayés, dont 4 de proposeurs) ;
  machine ≈ 0,27 USD.

## 3. Ce que le directeur a décidé après le verdict (RAPPORTÉ, registre R-2442, R-2443, 12 novembre 2026)

- **Accord de principe** pour une course à **plusieurs générations** ; avant toute dépense : préenregistrement neuf,
  contre-lecture, devis, ligne de dépense à son mot.
- Mots du directeur, verbatim : « C'est un défaut de conception : il faut regrouper les doublons au sein d'une même
  génération. : go. et comment diversifier les idees ? DEMANDE A ARGON ET A ASTRA AUSSI, et au collisionneur. Pour plusieurs
  générations, il faut un monde plus riche : plusieurs traits cachés, des interactions, des effets de tailles variées. : go »
- Décisions prises : (1) **regroupement des doublons au sein d'une génération** (aujourd'hui, deux fiches proches d'une même
  génération sont jugées chacune contre l'archive de la génération précédente, pas l'une contre l'autre) ; (2) **monde plus
  riche** : plusieurs traits cachés, interactions, effets de tailles variées ; (3) le préenregistrement de la course à
  plusieurs générations exige : monde plus riche, regroupement des doublons, réponses brutes des proposeurs et témoins
  d'isolement versés, **plusieurs graines ou mondes** pour la sensibilité aux effets faibles, et une **mesure de la
  diversité des idées retenues**.
- Mondes neufs (RAPPORTÉ, ligne de dépense GO-2026-11-12-05) : génération de 50 mondes plantés neufs, gardés privés. La
  question de savoir si leurs lois sont écrites par un programme ou par un modèle (et lequel) est posée au directeur ; les
  proposeurs de la famille Claude ne redeviennent possibles que si ces lois ne sont pas écrites par un modèle de cette famille.

## 4. Contraintes du programme qui ne se discutent pas ici

1. **Juge hors des agents** (décision N-064, RAPPORTÉ) : statistique calculée par l'orchestrateur, engagement scellé avant
   les données, nul formé des lois connues, comparaisons multiples contrôlées. Aucun modèle ne décide d'une promotion.
2. **N-053** (RAPPORTÉ) : aucun score d'un moniteur ou d'un juge du programme dans un signal d'entraînement ou de sélection
   d'un agent. **N-058** : la composition des proposeurs (modèles, rôles, parts du budget) se juge sur **l'oracle du monde
   planté et le coût**, jamais sur le verdict du juge.
3. **N-045** (RAPPORTÉ) : le bon marché d'abord, le cher sur preuve, à budget égal ; témoin « meilleur de N tirages » ou « un
   modèle, vote à k, coût apparié » ; pilote de bruit A/A avant toute comparaison.
4. **N-044** (RAPPORTÉ) : l'objectif ultime est l'universalité mesurée sur des familles de mondes inédites.
5. **Vue des proposeurs** : jamais un verdict, jamais l'oracle, jamais une loi plantée, jamais la tranche du test de mort.
   Les pièces du monde S-V1 sont publiques (dépôt public de l'organisme) : **aucun Web** pour un rôle de l'organisme.
6. **Règles** : préenregistrement scellé avant toute expérience décisive, aucune lecture de résultat avant (R1) ; même audit
   devant un résultat trop propre, positif ou négatif (R4) ; une version neuve porte un nom neuf (R12) ; verdict par un
   lecteur neuf sur critères gelés (R13) ; toute dépense sous devis et accord du directeur.

## 5. Points ouverts que la question touche (HYPOTHÈSE de l'opérateur, à discuter)

- Une même consigne et une même vue servies à deux modèles, un appel chacun, peuvent produire des idées corrélées ; le
  monde S-V1 n'offrait qu'un seul constat fort au-delà de K1.
- Le regroupement des doublons, une récompense de la nouveauté ou une consigne de diversité peuvent pousser les proposeurs
  vers la classe que le nul ne couvre pas (voir la limite du juge, section 1).
- Toute mesure de diversité calculée sur le contenu des lois (formes, traits utilisés, distance entre prédictions) doit
  pouvoir être fixée et scellée avant la course.
