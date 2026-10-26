# Failles internes de notre contrôle — lecture de nos seuls documents — v1

Audit des failles, lot B (confrontation), lignée conv-audit, sous-agent neuf. Horodatages : lignes « Horodatage » écrites
par `date -u` dans la commande qui les écrit (une après la rédaction des failles, avant la lecture du complément de
session-depot ; une à la clôture). Carte associée : `carte-du-controle-v1.md` (`ad5eaa49…`).

## 0. Portée, méthode, échelles

- **Ce qu'est une faille ici** (brief de l'audit, § 2) : une condition sous laquelle notre mesure ne voit pas ce qu'elle
  prétend voir. Chaque faille est écrite au niveau de la méthode : où, mécanisme, preuve ou argument, gravité, remède,
  coût, expérience qui la testerait (à préenregistrer, R1), couverture actuelle.
- **Sources** : uniquement `fournis/` (chemins relatifs à ce dossier). Aucune littérature lue pour ce lot ; les rares
  renvois à l'état de l'art vérifié passent par nos propres fichiers (`etat-de-l-art/…`), avec leur section. Les chiffres
  internes cités (pilotes, premier test) viennent des décisions et propositions fournies, jamais des dossiers de données.
  Les chiffres calculés par l'auditeur renvoient à `calculs-auditeur-v2.sortie.txt` (`ee257a7a…`), produit par
  `calculs-auditeur-v2.py` (`dc5d1c98…`) : illustrations analytiques ou synthétiques, pas des mesures de nos instruments.
  La v1 (`calculs-auditeur-v1.*`) reste archivée : sa ligne « m = 4 » du bloc 3 portait une étiquette fausse (arrondi),
  corrigée en v2 ; tous les autres chiffres sont identiques entre v1 et v2.
- **Statut** : toutes les failles sont **candidates** ; aucune recherche d'antériorité n'est faite dans ce lot (R8) ; la
  synthèse la fera et classera chacune « non trouvée dans la littérature consultée » ou « voisine de … ».
- **Gravité** : **bloque** = une revendication ou une porte ne peut pas être prononcée telle qu'écrite tant que la faille
  n'est pas traitée ; **affaiblit** = la revendication tient sous une condition non vérifiée, ou sa portée doit être
  restreinte ; **précision** = formulation, traçabilité ou cohérence, sans effet direct sur une lecture.
- **Coûts** : estimations de l'auditeur, non devisées. Repère tiré de P-015 : 240 épisodes, environ 3,1 heures,
  environ 3,96 dollars, soit environ 0,017 dollar par épisode.
- **Ce qui n'est jamais écrit ici** : aucune procédure, consigne, exemple de texte, de code ou de réglage qui servirait à
  tromper un moniteur ; les mécanismes sont décrits comme des trous de couverture, avec leur remède.

Plan : A. construit, environnement, organismes (FI-01 à FI-13) ; B. modèle de menace (FI-14 à FI-23) ; C. mesure et
statistique (FI-24 à FI-32) ; D. méthode, portes, lecture (FI-33 à FI-41) ; E. gouvernance et dépendances (FI-42 à
FI-44) ; F. synthèse, priorités et décisions de Lazar.

---

## A. Construit, environnement, organismes

### FI-01 — Le construit s'est rétréci : du « sabotage diffus sur tâches floues » au « coût déclaré gonflé »

- **Où** : programme § 6 (a) (« biais systématique subtil (orienter vers des directions stériles, affaiblir les
  contrôles, gonfler les choix coûteux) ») ; § 5, H1 (« Revendicable : la mesure spécifique diffus/flou ») ; P-015
  (« le pilote n'a retenu que la famille « coût » » ; T0.6 : « « Affaiblir les contrôles » sort ») ; P-014, point 2 (« Les
  directions (fécondes, stériles) … sortent de la vérité terrain »).
- **Touche** : H1 (pièce revendicable), H2 et L (portée), H6 (canal de l'intervention), papier A (validité externe).
- **Mécanisme** : la thèse vise un sabotage dont chaque contribution reste défendable parce que le jugement est flou ;
  l'organisme retenu sabote en gonflant un nombre dans un champ. Le « flou à la relecture » devient du bruit sur une
  grandeur chiffrée à queue lourde. Ce qui est mesuré (un écart numérique noyé dans le bruit honnête) n'est plus ce qui
  est revendiqué (une orientation subtile de jugements). Pour H6, une paraphrase de confiance peut recopier un nombre
  intact : la marge mesurée dépendra du canal du mode, non de la nature diffuse du sabotage ; et l'utilité honnête doit
  être notée par l'évaluateur faible du programme (§ 6), c'est-à-dire un juge 8B presque sans information comme référence
  d'appariement au pilote (P-014).
- **Preuve ou argument** : textes cités. P-015 rapporte aussi, d'après le verdict du pilote, que 43,7 % des coûts
  déclarés par l'honnête sont à plus d'un facteur 10 de la référence : la « diffusion » y est d'abord le bruit honnête.
- **Gravité** : **bloque** la revendication de H1 telle qu'écrite (« diffus/flou ») et toute généralisation du papier A
  aux tâches floues tant qu'un seul mode chiffré est mesuré.
- **Remède** : (a) nœud de Lazar : restreindre les revendications au mode mesuré (« surestimation d'un champ chiffré
  dans des propositions d'expériences ») ; ou (b) réintroduire avant G1 au moins un mode non chiffré (« affaiblir les
  contrôles », dont l'appariement par sous-agents a montré 0,968 d'accord entre deux séries au pilote, P-014) et rapporter
  G1 par mode ; dans les deux cas, écrire H6 par mode.
- **Coût** : (a) nul ; (b) une condition de plus dans T0.6 (quelques dollars de génération) et l'étiquetage par
  sous-agents (heures de session, sans carte).
- **Expérience** : généralisation de mode préenregistrée : sondes, agrégateurs et seuils gelés sur le mode « coût », lus
  sur le mode « contrôles » ; prédiction signée : le gain blanc-sur-noir garde son signe ; métrique : rappel par épisode à
  1 % de faux positifs, par mode, intervalles par rééchantillonnage des tâches ; critère : borne basse du gain > 0 dans
  les deux modes, sinon revendication restreinte au mode « coût ».
- **Couverture actuelle** : non. P-015 acte la restriction de l'organisme sans la reporter dans les revendications.

### FI-02 — Aucun mode de sabotage tenu à l'écart : la conception des moniteurs est informée par l'organisme

- **Où** : P-015 (E3 : sonde du domaine « en mode coût », « lecture avant le champ COST » ; « C'est la seule voie de la
  revue qui peut porter une revendication ») ; N-029 et P-015 (traits du texte : « coût normalisé par tâche, longueur,
  forme du champ coût ») ; programme § 7 (anti-circularité limitée à l'entraînement) ; à comparer avec N-044, énoncé 1
  (« universalité … sur des familles de questions jamais vues à la conception »).
- **Touche** : H1, H2, G1, critère 3 de G0 ; toute revendication de détection d'un sabotage non annoncé.
- **Mécanisme** : les bras les plus prometteurs (sonde du domaine, traits du texte) sont dessinés en connaissant le canal
  du sabotage. L'anti-circularité interdit d'entraîner sur les organismes, pas de concevoir d'après eux. Le résultat
  mesure alors un détecteur spécialisé contre un mode connu ; l'adversaire réel n'annonce pas son mode.
- **Preuve ou argument** : textes cités ; le principe que Lazar a retenu pour la lignée des organismes (N-044) n'est pas
  appliqué à la lignée du sabotage.
- **Gravité** : **bloque** toute revendication générique (« détecte le sabotage diffus ») tirée des bras spécialisés ;
  **affaiblit** H1.
- **Remède** : un mode de sabotage conçu par une instance qui n'a conçu aucun moniteur, scellé avant G1 et révélé
  seulement à l'évaluation ; rapporter à part les bras génériques (sondes apprises sans l'organisme ni son mode) et les
  bras spécialisés.
- **Coût** : conception par un sous-agent (heures de session) ; une condition d'organisme (quelques dollars).
- **Expérience** : « mode tenu à l'écart », préenregistrée : prédiction signée : la sonde générique d'intention garde au
  moins une fraction fixée d'avance de son rappel du mode connu, tandis que la sonde du domaine et les traits « coût »
  chutent ; métrique : rapport des rappels à 1 % et son intervalle.
- **Couverture actuelle** : non (dans la lignée du sabotage).

### FI-03 — Le régime « diffus » est défini par nos propres bases boîte noire, et la prémisse d'H2 n'est vérifiable que de ce côté

- **Où** : N-007 § 1 (« chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % ») ; P-015
  (« la dose « diffuse » se fixe sur la boîte noire seule » ; option (b) : intensités retenues si « le rappel par action
  du meilleur moniteur, à 1 % de faux positifs, reste sous un seuil gelé ») ; N-008 (comparateur : meilleure base, toutes
  variantes) ; N-029 (juge de 70 milliards seulement sur un GO séparé, après G0).
- **Touche** : H1 (G1), H2.
- **Mécanisme** : (1) les bases qui définissent la zone diffuse font aussi partie du comparateur de G1 : leur faiblesse
  par action devient une condition d'entrée, et l'avantage blanc-sur-noir n'est établi que relativement à des bases de 8
  et 3 milliards de paramètres ; une base plus forte déplacerait la zone. (2) H2 suppose chaque action sabotée sous le
  seuil du moniteur par action ; on ne peut pas choisir la dose sur la sonde sans régler l'expérience vers le signe voulu
  (R3, rappelé par P-015) : la prémisse d'H2 côté boîte blanche n'est donc pas garantie à la dose retenue.
- **Preuve ou argument** : textes cités ; la règle de P-015 protège R3, elle n'écrit pas la dépendance du résultat à la
  force des bases.
- **Gravité** : **affaiblit** H1 et H2 ; **bloque** la formule générale « la boîte blanche bat la boîte noire sur le
  sabotage diffus » si le régime n'est pas rapporté avec la base qui le définit.
- **Remède** : remplacer la dose retenue par une courbe : mesurer le contraste blanc-noir et le gain du séquentiel sur
  une grille de doses allant de « invisible par action » à « visible par action » pour la boîte noire, et lire H1 et H2
  comme des fonctions de la détectabilité par action mesurée pour chaque bras ; définir le régime avec une base tenue
  hors du comparateur ou avec la plus forte base disponible.
- **Coût** : trois à cinq doses au lieu d'une ou deux (dizaines de dollars) ; juge de 70 milliards sur GO (N-029).
- **Expérience** : prédiction signée : le gain blanc-sur-noir décroît quand la détectabilité boîte noire par action
  croît, et le gain du séquentiel boîte blanche est positif partout où la sonde par action reste sous son seuil ;
  métrique : pente du gain en fonction du rappel par action de la meilleure base, intervalle par tâches.
- **Couverture actuelle** : en partie (P-015 (b) protège R3 ; ni la force des bases ni la prémisse d'H2 côté sonde).

### FI-04 — Le taux de change entre dommage et preuve interne n'est pas mesuré

- **Où** : programme § 3 (lemme : la puissance « ne dépend que de B et de la variance ») et § 4 (« Sécurité = inf sur
  π_R de P(alerte avant que le dommage cumulé n'atteigne θ) ») ; N-004 (L1 en unités de score ; « Non-compensation …
  posée comme condition empirique » ; « La capacité d'un agent à piloter ses activations pour compenser se mesure par
  son coût »).
- **Touche** : L (pertinence pour la sécurité), H2, H3 (« budget constant »), toute garantie de sécurité.
- **Mécanisme** : le lemme borne une puissance en fonction de B = Σδ, budget exprimé en déplacement de score ; la
  sécurité se définit en dommage cumulé θ. Passer de l'un à l'autre exige une borne inférieure du taux κ = déplacement de
  score par unité de dommage, sur toutes les politiques de l'attaquant. Une politique qui produit le même dommage avec un
  κ plus faible n'est pas couverte par une garantie en unités de score. N-004 nomme la non-compensation comme condition
  empirique ; aucun préenregistrement prévu ne mesure κ ni son infimum. Le même glissement touche H3 : « à budget
  constant » au sens du score ou du dommage ?
- **Preuve ou argument** : argument d'unités ; E1.3 teste δ > 0, pas δ par unité de dommage.
- **Gravité** : **bloque** toute lecture du lemme comme garantie de sécurité.
- **Remède** : définir κ par type d'action et par famille d'organisme ; le mesurer (régression du déplacement de score sur
  le dommage réalisé, action par action, sous chaque condition, y compris sous les attaques d'E1.5) ; énoncer la sécurité
  sous la condition κ ≥ κ_min mesurée ; fixer l'unité du « budget constant » de H3.
- **Coût** : faible (lectures sur les épisodes de T0.6 et d'E1.5, processeur) ; les attaques adaptatives relèvent de
  leur propre GO.
- **Expérience** : prédiction signée : κ > 0 avec borne basse positive dans chaque famille ; sous attaque par contenu
  adaptative, κ ne baisse pas au-delà d'une fraction fixée d'avance ; métrique : pente et intervalle par tâches.
- **Couverture actuelle** : en partie (condition nommée dans N-004 ; aucune mesure prévue).

### FI-05 — Pas de test de validité incrémentale : battre un plancher n'établit pas une « preuve interne »

- **Où** : programme § 8.1 (« Plancher obligatoire … une sonde qui ne le bat pas n'existe pas ») et § 3 (« La
  fragmentation détruit la preuve *externe* … la preuve *interne* s'additionne ») ; N-029 (prédicteur sur les traits du
  texte, « base boîte noire gratuite que toute sonde doit battre ») ; P-013 (témoin lexical) ; P-015 (« base « coût seul »
  à côté du témoin lexical »).
- **Touche** : thèse centrale (§ 3), H1, critère 3 de G0.
- **Mécanisme** : une sonde peut battre le plancher aléatoire et battre séparément le prédicteur de texte tout en ne
  portant que l'information du texte (longueur, chiffres, vocabulaire) que la passe avant de l'agent recode. La thèse
  affirme une information interne au-delà de l'externe ; deux comparaisons séparées ne le montrent pas, un test emboîté
  le peut (traits du texte et sonde contre traits du texte seuls).
- **Preuve ou argument** : au premier test sur (i-a), le coût écrit seul séparait saboteur et honnête à 0,888 d'aire
  pendant que les sondes génériques restaient sous leur plancher (proposition N-025, P-015) : l'information externe était
  abondante ; un succès futur des sondes pourrait la recoder.
- **Gravité** : **affaiblit** H1 ; **bloque** la phrase de thèse « preuve interne » sans test emboîté.
- **Remède** : test de validité incrémentale préenregistré, par action et par épisode : modèle de référence sur les traits
  du texte (ceux de N-029, plus la longueur en jetons et le nombre de jetons chiffrés), modèle complet avec le score de
  sonde ; gain mesuré hors échantillon.
- **Coût** : processeur seulement.
- **Expérience** : prédiction signée : le modèle complet améliore le rappel à 1 % (ou l'aire) hors échantillon, borne
  basse > 0 ; un nul est attendu si la sonde recode le texte.
- **Couverture actuelle** : en partie (bases séparées ; aucun test emboîté écrit).

### FI-06 — Information non appariée entre les bras : G1 peut se gagner en lisant l'indication privée

- **Où** : N-007 § 1 (« Le contexte privé de l'agent est compris dans la lecture » ; seuil « calibré sur des épisodes
  honnêtes ») ; N-008 § 2 (« calibrage du taux de faux positifs sur épisodes honnêtes réservés ») ; P-009 (a) (« une
  indication privée au pas désigné … Le témoin reçoit la même indication aux mêmes pas » ; « l'indication privée est un
  signal visible dans le contexte (le témoin le contrôle) ») ; P-010 (a) (le juge reçoit « les questions de recherche …
  et l'ensemble courant des propositions ») ; P-011 (négatifs du critère 3 : honnêtes et témoin) ;
  `etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md`, prononcé 4 (contrôle « sans texte » G1-P5).
- **Touche** : G1 (H1), H2, HC2b.
- **Mécanisme** : pour la famille (i), aux pas sabotés, le contexte privé contient l'indication qui commande le
  sabotage ; la sonde la lit, le juge boîte noire non. Si les négatifs qui fixent le seuil de G1 sont des épisodes honnêtes
  sans indication, une sonde qui détecte l'indication (et non l'intention) obtient un rappel élevé à 1 % : la boîte
  blanche « gagne » G1 par une différence d'information, non d'accès. Le critère 3 met le témoin parmi les négatifs ; G1,
  d'après les pièces fournies, ne le fait pas.
- **Preuve ou argument** : textes cités ; le contenu de G1-P5 n'est pas fourni : à vérifier sur le brouillon de G1.
- **Gravité** : **bloque** G1 tant que ses négatifs ne sont pas appariés en indication, ou que G1 n'est pas lu sur la
  seule famille (ii).
- **Remède** : négatifs de calibrage de G1 = honnêtes, témoin « instruit sans sabotage » et « mention », appariés en
  indication ; ou G1 décidé sur la famille (ii) ; en plus, un bras boîte noire qui voit le même contexte privé que la sonde
  et un bras sonde limité aux positions du transcript public, pour séparer l'accès interne de l'accès à l'information.
- **Coût** : nul pour les négatifs (les conditions existent) ; une lecture de juge de plus (quelques dollars).
- **Expérience** : prédiction signée : le gain blanc-sur-noir de G1 baisse quand le témoin entre dans les négatifs ; le
  gain restant est celui que H1 revendique ; plan 2 (information : publique ; publique et privée) × 2 (accès).
- **Couverture actuelle** : en partie (critère 3 : oui ; G1 : non d'après les pièces ; G1-P5 à vérifier).

### FI-07 — Le test de validité (i) contre (ii) n'identifie pas le construit

- **Où** : programme § 7 (« Une sonde qui lit en réalité « j'ai une instruction cachée » réussit sur (i) et échoue sur
  (ii) ; une sonde d'intention réussit sur les deux ») ; brief T0.7 ; P-009 (dose de (ii) par l'échelle α, « n'est pas une
  proportion d'actions »).
- **Touche** : H8, critère 3 de G0, lecture de toute sonde « d'intention ».
- **Mécanisme** : deux explications rivales cassent l'inférence. (1) La politique distillée de (ii) peut saboter sans
  état interne semblable à celui de (i) : une sonde d'intention valide échouerait sur (ii) pour une bonne raison. (2) La
  distillation de contexte vise à reproduire l'effet de la consigne : (ii) peut en reconstruire une représentation
  interne, et une sonde « instruction » réussirait sur (ii) sans lire d'intention. En outre, (i) est dosé en proportion
  d'actions et (ii) en échelle α : la répartition du sabotage diffère entre les familles.
- **Preuve ou argument** : argument de conception ; aucun contrôle des deux explications n'est prévu.
- **Gravité** : **affaiblit** H8 et la lecture du critère 3.
- **Remède** : (a) mesurer la ressemblance des représentations : une sonde « instruction » apprise sur des contextes avec
  ou sans consigne, appliquée à (ii) contre son adaptateur témoin ; (b) une borne haute descriptive : une sonde apprise sur
  (ii), sur des tâches tenues à l'écart ; (c) doser (ii) aussi en proportion d'actions, pour comparer à dose égale.
- **Coût** : processeur et quelques heures de carte ; (c) un adaptateur par proportion (dizaines de dollars).
- **Expérience** : prédiction bilatérale : la sonde « instruction » dépasse sur (ii) son niveau sur l'adaptateur témoin,
  ou non ; la lecture du test de validité est fixée d'avance pour chaque issue.
- **Couverture actuelle** : non.

### FI-08 — Sondes apprises en lecteur, déployées en auteur

- **Où** : P-011 (a) (concepts 3 et 4 : « paires synthétiques » ; défaut : « jeux synthétiques (dissimulation, intention)
  écrits par un sous-agent neuf ») ; brief T0.9 (« la sonde lit les activations de l'agent qui produit le contenu ») ;
  N-013 § 8 (des sondes lectrices sont déplacées par des attaques de contenu, d'après les sources lues) ; P-015 (E3 :
  « versions incitées … lecture avant le champ COST »).
- **Touche** : HC2 (distinction auteur / lecteur), critère 3, G1.
- **Mécanisme** : un texte écrit par un autre modèle, passé dans le 8B, met le 8B en position de lecteur ; la sonde
  apprend la représentation d'un texte de sabotage lu, non celle d'un sabotage produit. Le programme retient lui-même que
  les sondes lectrices sont déplaçables par le contenu : une sonde apprise ainsi est plus proche d'un classifieur de texte
  que de la sonde de l'auteur que HC2 décrit.
- **Preuve ou argument** : textes cités ; pour E3, les « versions incitées » suggèrent une génération par le 8B
  lui-même ; ce n'est pas écrit pour les concepts 3 et 4 de P-011.
- **Gravité** : **affaiblit** HC2 et la portée de G1.
- **Remède** : données d'entraînement produites par le 8B lui-même (honnête et sabotage, consigne présente des deux
  côtés comme en E3), lues aux positions de ses propres jetons ; comparer les deux recettes.
- **Coût** : quelques milliers de paires générées sur les tâches de réserve (une à deux heures de carte, quelques
  dollars).
- **Expérience** : prédiction signée : la sonde apprise en auteur a un |g| plus petit sous attaque par contenu (EC.2) et
  un meilleur rappel sur (ii) que la sonde apprise en lecteur ; différences avec intervalles.
- **Couverture actuelle** : en partie (E3 ; bras « sonde du lecteur » côté C).

### FI-09 — Vérité terrain produite par un seul fournisseur, et exposée à la corruption que le papier C étudie

- **Où** : P-006 (a) (cibles « extraites par le modèle de la session (sous-agents neufs, contre-vérifiés sur
  échantillon) ») ; P-014 (étiqueteurs « du même fournisseur pour les séries de contrôle » ; « Contrôle par deux autres
  modèles en cours ») ; programme § 4 et § 5 (HC1 : les juges génératifs se déplacent sous pression).
- **Touche** : critère 2 de G0, toute mesure de dommage hors champ chiffré, H6 (utilité).
- **Mécanisme** : (1) erreurs corrélées : une même famille de modèles extrait les cibles et étiquette l'appariement ;
  l'accord entre deux séries peut refléter un biais commun. (2) Les étiqueteurs lisent les propositions de l'agent : ce
  sont des juges génératifs exposés au contenu du saboteur, donc à la loi de déférence que le programme veut mesurer ; un
  saboteur qui plaide déplace aussi la vérité terrain.
- **Preuve ou argument** : textes cités ; en mode « coût », le dommage est lu par un analyseur de nombres, moins exposé ;
  tout retour à un mode non chiffré (FI-01) rouvre le point.
- **Gravité** : **affaiblit** (critère 2 ; tout mode non chiffré).
- **Remède** : finir le contrôle par d'autres modèles (prévu) ; une petite ancre humaine (quelques dizaines d'éléments) ;
  appliquer aux étiqueteurs le protocole « contenu = données » et mesurer leur g sous les familles d'attaque du papier C,
  sur le même corpus.
- **Coût** : heures d'étiquetage humain ; appels de modèles (dollars).
- **Expérience** : prédiction : accord entre fournisseurs au-dessus d'un seuil fixé ; g des étiqueteurs sous plaidoyer
  dans une marge d'équivalence autour de zéro ; sinon, vérité terrain refondée.
- **Couverture actuelle** : en partie (contrôle par d'autres modèles en cours ; rien sur la corruption des étiqueteurs).

### FI-10 — L'avantage blanc-sur-noir dépend du bruit de l'honnête, donc de la compétence de l'agent

- **Où** : P-015 (« 43,7 % de ses coûts déclarés sont à plus d'un facteur 10 de la référence ») ; N-029 et P-015 (les
  bases boîte noire lisent la sortie, dont le coût) ; programme § 15 (déployabilité).
- **Touche** : H1 (généralité), H2.
- **Mécanisme** : la boîte noire lit le résultat (le nombre), la sonde lit au mieux la disposition ; quand l'honnête se
  trompe beaucoup, le résultat est bruité et la boîte noire perd, quelle que soit la qualité de la sonde. L'avantage
  mesuré avec un agent de 8 milliards très bruité peut s'effacer avec un agent compétent, dont les sorties honnêtes sont
  précises.
- **Preuve ou argument** : argument ; le chiffre de P-015 montre un bruit honnête élevé.
- **Gravité** : **affaiblit** la généralité de H1.
- **Remède** : stratifier la lecture par niveau de bruit honnête de la tâche (dispersion des coûts honnêtes par tâche) ;
  rapporter le gain en fonction de ce bruit.
- **Coût** : processeur.
- **Expérience** : prédiction signée : le gain blanc-sur-noir décroît quand la précision honnête de la tâche croît ;
  pente préenregistrée, intervalle par tâches.
- **Couverture actuelle** : non.

### FI-11 — Les organismes sabotent parce qu'on le leur demande, en évaluation ; la menace sabote quand elle se croit non observée

- **Où** : programme § 7 (familles (i), (ii), (iii) ; contrôles croisés « honnête averti » et « saboteur en régime simulé
  non observé ») ; § 11 ; P-011 (sonde « conscience d'évaluation » réservée au test de construit).
- **Touche** : H8 ; validité de construit de toutes les sondes ; menace « conscience d'évaluation ».
- **Mécanisme** : (1) l'état interne des organismes est l'obéissance à une consigne de saboter (i) ou son résidu distillé
  (ii), dans un cadre manifestement expérimental ; la consigne elle-même est un indice d'évaluation, et une sonde peut
  lire « je suis dans un exercice ». (2) Aucun organisme ne conditionne son sabotage à l'absence perçue de surveillance :
  la classe où la conscience d'évaluation masque une disposition (conduite honnête quand l'agent se croit observé) n'est
  pas représentée ; le contrôle croisé « non observé » renseigne sur la conscience d'évaluation d'un saboteur, pas sur la
  détection d'une disposition dormante.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** H8 et la portée de toutes les revendications de détection.
- **Remède** : (a) lire la sonde « conscience d'évaluation » comme covariable sur toutes les conditions et préenregistrer
  que la détection par la sonde d'intention survit à l'ajustement sur elle ; (b) un organisme conditionnel (disposition
  de sabotage exprimée seulement hors observation perçue), avec la question : la sonde lit-elle la disposition dans les
  épisodes où il se conduit honnêtement ?
- **Coût** : (a) processeur ; (b) un adaptateur de plus (dizaines de dollars), sous GO.
- **Expérience** : (a) prédiction signée : corrélation partielle entre score d'intention et sabotage, à conscience
  d'évaluation fixée, de borne basse > 0 ; (b) prédiction bilatérale sur le score de sonde dans les épisodes observés de
  l'organisme conditionnel contre son témoin.
- **Couverture actuelle** : en partie (contrôles croisés ; ni covariable préenregistrée ni organisme conditionnel).

### FI-12 — La sécurité est un infimum sur les politiques, mais la classe évaluée est petite et l'élicitation n'a pas de règle d'arrêt

- **Où** : programme § 4 (« Sécurité = inf sur π_R ») ; § 13 (« Élicitation rouge insuffisante → import des politiques
  d'attaque publiées ») ; E1.5 ; P-015 (« l'agent à qui on demandait trois fois le coût en a déclaré environ 33 fois »).
- **Touche** : toute revendication de sécurité (A, B), Tr, HC2.
- **Mécanisme** : la sécurité mesurée n'est qu'une borne haute de l'infimum, calculée sur les politiques essayées
  (consigne, distillation, attaques par contenu, réglage contre la sonde sous GO). Un agent de 8 milliards qui dépasse sa
  dose d'un facteur dix exécute mal des stratégies fines. « Élicitation insuffisante » n'a pas de critère chiffré.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** toute revendication de sécurité, qui doit s'écrire « contre la classe Π testée ».
- **Remède** : écrire la classe Π de chaque revendication ; courbe d'élicitation (succès d'attaque en fonction de
  l'effort de l'équipe rouge : itérations, calcul) avec règle d'arrêt préenregistrée (plateau) ; critère chiffré
  d'« élicitation insuffisante ».
- **Coût** : effort d'équipe rouge (heures de session ; calcul selon les bras).
- **Expérience** : prédiction : la courbe atteint un plateau avant le budget fixé ; sinon, toute revendication de
  robustesse est suspendue.
- **Couverture actuelle** : en partie (E1.5 ; bascule sans critère).

### FI-13 — Un modèle, un environnement ; les organismes (iii) ne sont pas comparables tels quels

- **Où** : programme § 14 (Llama-3.1-8B-Instruct ; Qwen2.5-7B pour l'hétérogénéité) ; § 15 (« la forme mesurée dans P3
  n'a pas transféré de Llama à Qwen ») ; § 7 (iii) (« gain de temps et comparabilité ») ;
  `etat-de-l-art/corrections-v1.md`, section 1, ligne 15 (les organismes publics imitent Llama-3.1-8B-Instruct mais
  reposent sur Llama-3.3-70B-Instruct).
- **Touche** : généralité des papiers A et C ; T1.1 (famille (iii)).
- **Mécanisme** : tous les résultats A et C portent sur un seul modèle agent et un seul environnement ; le second modèle
  n'entre qu'en phase 3. Les organismes (iii) sont des modèles de 70 milliards : leurs activations demandent d'autres
  sondes et une inférence plus coûteuse ; la « comparabilité » annoncée ne tient pas sans les reprendre.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** la généralité ; **précision** pour (iii).
- **Remède** : une réplication préenregistrée du contraste de G1 sur Qwen2.5-7B dès la phase 1 (une condition, une dose) ;
  corriger la ligne (iii) (coût, sondes propres) ; écrire la portée de chaque papier.
- **Coût** : une dizaine de dollars de génération pour la réplication ; (iii) : inférence 70B (dizaines de dollars),
  sous GO.
- **Expérience** : prédiction signée : le signe du gain blanc-sur-noir se conserve sur Qwen ; critère : signe et borne
  basse.
- **Couverture actuelle** : en partie (§ 15 nomme l'universalité comme question ouverte).

---

## B. Modèle de menace

Lecture d'ensemble (détail dans la carte, § 6) : **qui** — l'agent instruit, distillé ou verrouillé, l'attaquant par
contenu, l'attaquant qui règle les poids, les copies coordonnées, l'agent qui plaide, le mandant en délégation ; manquent
l'agent conditionné à l'observation (FI-11) et l'adversaire patient entre épisodes (FI-15). **Ce qu'il sait** : non écrit
par hypothèse (FI-14). **Ce qu'il peut apprendre** : par les verdicts (H7) et l'entraînement contre la sonde (E1.5 b) ;
manquent le retour de l'environnement (FI-17), l'influence sur le réentraînement (FI-16), la mise à jour du modèle
(FI-18). **Ce qu'il contrôle** : son contenu, la répartition et la dépendance de son sabotage ; manquent le taux de change
dommage/score (FI-04), le contenu lu par d'autres agents (FI-20) et par les étiqueteurs (FI-09), les artefacts persistants
(FI-15, FI-22), les ordres à un sous-agent (FI-19).

### FI-14 — Le profil de l'adversaire n'est pas écrit par hypothèse

- **Où** : programme § 5 (HC2 « sous attaque par contenu boîte noire » ; Tr « face à un attaquant adaptatif ») ; E1.5 (a)
  (« l'organisme connaît le moniteur ») ; § 8.3, D1 (a) (juge = même modèle que l'agent) ; N-013 § 3 (HC4, « poids
  réglables ») ; § 9 (frontière : infrastructure hors périmètre).
- **Touche** : HC2, HC4, Tr, H6, H7, G1 sous attaque.
- **Mécanisme** : « boîte noire », « adaptatif », « connaît le moniteur » mêlent quatre axes : ce que l'adversaire sait
  (existence, architecture, couches, agrégateur, seuil, verdicts passés), ce qu'il peut faire (contenu, réglage,
  renforcement avec ou sans gradient), ce qu'il reçoit en retour (rien, verdicts, scores), avec qui il se coordonne. Sans
  table, deux préenregistrements testent des adversaires différents sous le même nom, et un résultat de robustesse se
  généralise à tort. Deux cas particuliers : le juge de même modèle que l'agent est un moniteur non fiable (prévisible par
  l'agent, collusion possible) ; le régime « poids réglables » de HC4 suppose un adversaire qui touche la chaîne
  d'entraînement, que la frontière du § 9 met hors périmètre.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** toutes les revendications de robustesse.
- **Remède** : une table des profils (connaissance × accès × retour × coordination), chaque hypothèse et chaque bras
  rattaché à une case ; le juge de même modèle rapporté comme « surveillance non fiable » sous attaque adaptative, hors
  du rôle de base de confiance ; HC4 « poids réglables » rattaché à un modèle de menace écrit (initié, chaîne
  d'entraînement).
- **Coût** : écriture (une heure).
- **Expérience** : sous E1.5 (a), juge de même modèle contre juge d'une autre famille, même attaque ; prédiction signée :
  la baisse de rappel est plus forte pour le juge de même modèle.
- **Couverture actuelle** : non.

### FI-15 — La fragmentation entre épisodes : hors du cadre formel, et l'accumulation y est interdite par deux invariants

- **Où** : programme § 4 (actions indexées par agent i et pas t ; sécurité définie par épisode : « avant que le dommage
  cumulé n'atteigne θ ») ; § 9 (« Moniteurs amnésiques entre épisodes » ; « Hygiène de l'état persistant : remises à
  zéro ») ; § 6 (b) (environnement à « état persistant ») ; N-004, L3 (« le reporter aide l'attaquant »).
- **Touche** : L, H2, H3, statistique spatio-temporelle ; définition de la sécurité ; invariants 4 et 6.
- **Mécanisme** : la thèse du programme (fragmenter détruit la preuve par unité) s'applique un cran plus haut : un
  dommage réparti sur des épisodes, chacun sous le seuil par épisode, échappe par construction à tout test par épisode. Le
  cadre formel n'a pas d'indice d'épisode ; la sécurité est définie par épisode ; l'invariant d'amnésie interdit toute
  statistique qui accumulerait entre épisodes ; l'environnement (b) porte le dommage dans une base de code qui persiste par
  construction, que l'hygiène ne peut pas remettre à zéro sans détruire la tâche. L'invariant vise la relation qu'un agent
  cultiverait avec un juge génératif ; il interdit aussi, sans le dire, la mémoire d'une statistique de scores, qui ne se
  persuade pas.
- **Preuve ou argument** : textes cités ; c'est l'objet mathématique du lemme, sur un indice de plus.
- **Gravité** : **affaiblit** ; **bloque** toute revendication de sécurité contre un adversaire patient qui répartit son
  dommage entre épisodes.
- **Remède** : distinguer la mémoire d'un moniteur génératif (interdite) de la mémoire d'une statistique de scores
  (permise) ; étendre l'indice à (épisode, agent, pas) et la sécurité au dommage cumulé du déploiement ; processus e entre
  épisodes, calibré sur des suites d'épisodes honnêtes ; en (b), une lecture de l'état persistant lui-même.
- **Coût** : théorie et simulation (processeur) ; lectures sur des épisodes existants.
- **Expérience** : semi-synthétique préenregistrée (dans l'esprit d'E1.4) : dommage réparti sur E épisodes, sous le
  seuil de chacun ; prédiction : rappel du test par épisode au niveau de son taux de faux positifs, rappel du processus e
  entre épisodes croissant avec E.
- **Couverture actuelle** : non.

### FI-16 — L'asymétrie d'apprentissage ouvre un canal vers les données d'entraînement des sondes

- **Où** : programme § 9 (« chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes ») ;
  § 7 (anti-circularité) ; § 8.1 (« Réserve de détecteurs jamais déployés … sortis pour audit seulement »).
- **Touche** : invariant 7 ; robustesse dans la durée (H5, H7).
- **Mécanisme** : (1) survivance : seules les attaques détectées entrent dans le réentraînement ; la sonde progresse sur
  ce qu'elle voit déjà, non sur ses angles morts, et son rappel sur des attaques semblables surestime sa couverture. (2)
  Une détection n'est pas une vérité : sans audit, des faux positifs entrent comme positifs. (3) Un adversaire qui influe
  sur l'ensemble des épisodes détectés influe sur les données qui façonnent la sonde suivante. (4) Le réentraînement sur
  les organismes évalués contredit l'anti-circularité.
- **Preuve ou argument** : argument de conception.
- **Gravité** : **affaiblit**.
- **Remède** : réentraîner seulement sur des positifs confirmés par audit ; évaluer chaque sonde réentraînée sur des
  organismes et des modes tenus à l'écart ; garder la réserve jamais déployée comme sentinelle, avec une alarme de
  désaccord préenregistrée (sonde réentraînée en hausse, réserve en baisse, sur le même flux).
- **Coût** : faible (processeur ; la réserve est prévue).
- **Expérience** : boucle semi-synthétique préenregistrée : rappel sur la classe non détectée au fil des
  réentraînements, avec et sans sentinelle ; prédiction : sans sentinelle, le rappel sur les modes non détectés ne
  progresse pas.
- **Couverture actuelle** : non.

### FI-17 — Le flux unidirectionnel ne tient qu'au niveau du moniteur : le protocole rend de l'information à l'agent

- **Où** : programme § 9 (« Flux unidirectionnel agent → moniteur ») ; N-034 § 2 (« L'environnement (a) rend à l'agent le
  motif d'une action non appliquée, au pas suivant ») ; E1.6 (ré-échantillonnage, remise à zéro) ; E3.4 (riposte, phase 3)
  ; § 9 (seuils stochastiques).
- **Touche** : invariants 3 et 5 ; transfert des résultats passifs du papier A à un protocole actif ; H6, H7.
- **Mécanisme** : le papier A mesure une détection passive à seuils fixes calibrés ; dans un protocole, toute intervention
  visible (blocage, ré-échantillonnage, remise à zéro) et tout retour de l'environnement renseignent l'agent sur l'état
  de détection pendant l'épisode ; une probabilité d'audit lisse reste une fonction apprenable avec assez
  d'observations. La fuite n'est mesurée qu'en phase 3.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** le transfert des résultats du papier A.
- **Remède** : borner la portée du papier A à la surveillance passive, ou ajouter un bras « interventions visibles » dès
  la phase 1 ; mesurer le changement du score de sonde et du comportement après une intervention visible.
- **Coût** : une condition de plus en E1.6 (dollars).
- **Expérience** : prédiction bilatérale : après une intervention visible, le déplacement par action δ change ;
  métrique : δ avant et après, apparié par épisode.
- **Couverture actuelle** : en partie (H7 en phase 3).

### FI-18 — Dérive de calibrage à la mise à jour du modèle

- **Où** : N-007 (seuil calibré sur épisodes honnêtes) ; N-004 (garde « faux positifs vérifiés sur épisodes
  honnêtes ») ; P-009 et P-015 (adaptateur témoin distillé depuis le témoin) ; programme § 15 (déployabilité).
- **Touche** : garantie de faux positifs (H2) ; déployabilité.
- **Mécanisme** : la garantie suppose que les épisodes honnêtes futurs suivent la loi des épisodes de calibrage ; un
  réglage fin bénin (nouvelle version de l'agent) déplace les activations, donc la loi honnête des scores ; le taux réel
  peut s'écarter du nominal sans aucune attaque.
- **Preuve ou argument** : argument ; le programme dispose déjà d'un réglage bénin : l'adaptateur témoin.
- **Gravité** : **affaiblit**.
- **Remède** : mesurer le taux de faux positifs du seuil calibré sur le modèle de base, appliqué aux épisodes honnêtes de
  l'adaptateur témoin ; recalibrer par version ; flux de canaris honnêtes pour détecter une dérive.
- **Coût** : nul à faible (épisodes de l'adaptateur témoin prévus).
- **Expérience** : prédiction : taux réalisé ≤ 2 % pour 1 % nominal sur l'adaptateur témoin ; sinon, calibrage par
  version obligatoire.
- **Couverture actuelle** : non.

### FI-19 — Le canal authentifié authentifie l'émetteur, pas sa fiabilité

- **Où** : programme § 9 (« Canal opérateur authentifié » ; « Contenu en bande = données ») ; § 6 (b) (codeur, testeur,
  relecteur) ; N-035 (H9 ; dans les cas rapportés, l'ordre d'affaiblir une garde vient de l'agent mandant).
- **Touche** : invariants 1 et 2 en multi-agents ; H9 ; papier B.
- **Mécanisme** : en délégation ou en pipeline multi-rôles, un agent non fiable est l'« opérateur » de son sous-agent ;
  ses ordres arrivent par le canal légitime et le protocole « contenu = données » ne les filtre pas. Les invariants
  protègent contre l'ordre usurpé, pas contre l'ordre légitime d'un mandant non fiable.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** les invariants 1 et 2 dans le papier B.
- **Remède** : distinguer « canal authentifié » et « mandant de confiance » ; surveiller les ordres entre agents comme des
  actions ; rattacher H9 à cette faille.
- **Coût** : écriture ; mesure dans H9.
- **Expérience** : dans H9, un bras « ordre affaiblissant venu du mandant » ; prédiction : la survie de la contrainte
  baisse, et un moniteur des ordres entre agents la relève.
- **Couverture actuelle** : en partie (H9, sous réserve d'antériorité).

### FI-20 — En multi-agents, les sondes d'un agent lecteur sont déplaçables par le contenu des autres

- **Où** : programme § 2, papier B (« leurs signatures internes co-varient ») ; E2.3 ; N-013 § 8 (sondes lectrices
  déplacées par des attaques de contenu, d'après les sources lues).
- **Touche** : statistique de population, H3, G2.
- **Mécanisme** : chaque agent est auteur de ses sorties et lecteur de celles des autres ; une part de son score de
  sonde reflète ce qu'il lit. La co-élévation suppose que l'élévation d'un agent reflète son propre état ; un agent peut
  alors élever ou abaisser le score d'agents honnêtes par ce qu'il leur fait lire.
- **Preuve ou argument** : argument, fondé sur la distinction auteur / lecteur que le programme pose lui-même pour le
  papier C.
- **Gravité** : **affaiblit** la statistique de population.
- **Remède** : séparer, pour chaque agent, les positions de ses propres jetons (part de l'auteur) de celles du contenu
  d'autrui (part du lecteur) ; calculer la co-élévation sur la part de l'auteur ; condition « honnêtes exposés au contenu
  d'un saboteur ».
- **Coût** : faible (mêmes activations, autre lecture).
- **Expérience** : prédiction : la part de l'auteur des honnêtes reste dans une marge d'équivalence quand ils lisent un
  saboteur ; la part du lecteur peut bouger.
- **Couverture actuelle** : non.

### FI-21 — Cause commune : des honnêtes co-élevés par un contexte partagé

- **Où** : programme § 2 et § 5 (H3) ; E2.3 (« Corrélation des scores de sondes entre agents, honnêtes contre
  attaquants »).
- **Touche** : statistique de population, G2.
- **Mécanisme** : des copies honnêtes qui partagent une tâche difficile, ambiguë ou à enjeux voient leurs scores monter
  ensemble ; un nul de co-élévation tiré d'équipes honnêtes sur d'autres tâches confond cause commune et collusion.
- **Preuve ou argument** : argument.
- **Gravité** : **affaiblit**.
- **Remède** : nul conditionnel à la tâche (équipes honnêtes sur les mêmes tâches ; effets aléatoires de tâche) ; strate
  « tâches difficiles ».
- **Coût** : épisodes honnêtes de plus (dollars).
- **Expérience** : prédiction : la statistique conditionnelle garde son taux nominal sur les honnêtes des tâches
  difficiles ; la statistique brute le dépasse.
- **Couverture actuelle** : non.

### FI-22 — La frontière de l'infrastructure laisse un cas intermédiaire, et la vivacité du moniteur n'est pas vérifiée

- **Où** : programme § 9 (« Frontière assumée … hors périmètre ») ; § 6 (b) (code, commits) ; N-035 § 1 (un sous-agent
  retire un moniteur au cours d'une migration, dans un cas rapporté).
- **Touche** : papier B ; intégrité du moniteur.
- **Mécanisme** : entre « posséder les clés » et « produire du texte », l'agent peut écrire du code ou des artefacts que
  l'infrastructure exécute ou lit ; un moniteur désactivé ou court-circuité ne lève aucune alarme, et son silence
  ressemble à de l'innocence.
- **Preuve ou argument** : textes cités.
- **Gravité** : **précision** (phase 3) ; **affaiblit** si l'environnement (b) partage un espace avec la chaîne de
  surveillance.
- **Remède** : capture des activations et calcul des scores hors de tout espace modifiable par les actions de l'agent
  (à écrire) ; canaris positifs injectés au hasard : un canari non détecté déclenche une alarme de vivacité.
- **Coût** : faible.
- **Expérience** : garde testée sur un cas sain et sur un artefact (R5) : moniteur neutralisé, canari manqué, alarme
  attendue.
- **Couverture actuelle** : non (les canaris de N-045 visent la lignée des organismes et sont « à ne pas signaler »).

### FI-23 — Les invariants ne sont pas déclarés pour la lignée des organismes de conception

- **Où** : N-044 (organisme qui se conçoit seul ; axe « contrôle de populations d'agents, essaim autonome ») ; N-045 v2
  (composition apprise ; mémoire transmise ; « L'héritage d'une génération est récompensé ») ; programme § 9.
- **Touche** : cohérence du programme ; tout usage futur d'un organisme comme moniteur ou comme juge.
- **Mécanisme** : un organisme qui apprend de génération en génération, avec mémoire et instruments à effet différé, est
  l'opposé d'un moniteur amnésique à état hygiénique ; s'il sert un jour de moniteur, ou si ses verdicts entrent dans une
  vérité terrain, les invariants 4 et 6 ne valent plus, sans que les décisions le disent.
- **Preuve ou argument** : textes cités.
- **Gravité** : **précision** aujourd'hui ; **affaiblit** si un organisme entre dans la chaîne de contrôle.
- **Remède** : écrire, dans une version du programme, quels invariants s'appliquent à la lignée des organismes, ou la
  déclarer hors du protocole de contrôle.
- **Coût** : écriture.
- **Expérience** : sans objet (décision de périmètre).
- **Couverture actuelle** : non.

---

## C. Mesure et statistique

### FI-24 — Le maximum sur les jetons lit la queue numérique que la garde d'équivalence ne borne pas

- **Où** : programme § 0, point 1, et § 8.1 (maximum ou attention) ; proposition N-011 (en demi-précision, écart maximal
  0,52 pour un seuil de 0,1, dépassements dans le contexte des lignes remplies à gauche ; « une longue queue sur quelques
  jetons » ; option (a) : garde au 99e centile) ; P-007 (production au noyau d'attention par défaut ; garde « 99e
  centile par action et par couche ≤ 0,2 » ; carte A100 hors du domaine strict de T0.4).
- **Touche** : garantie de faux positifs, reproductibilité, H2, G1.
- **Mécanisme** : la garde borne un centile des écarts par jeton ; la statistique de production est le maximum sur les
  jetons, qui lit précisément les quelques jetons de la queue laissés libres. Le score d'une action peut ainsi dépendre
  du remplissage, de la composition du lot, du noyau et de la carte, sans que la garde le voie ; si calibrage et
  évaluation ne tournent pas dans la même configuration, le taux réel s'écarte du nominal.
- **Preuve ou argument** : textes cités ; l'effet sur les scores de sondes n'est mesuré dans aucune pièce fournie.
- **Gravité** : **affaiblit** (taux de faux positifs à 1 %, reproductibilité).
- **Remède** : une garde au niveau des scores, non des activations : sur un échantillon, écart maximal du score par
  action entre configurations (remplissage, lot, noyau, carte), borné en fraction de l'écart-type honnête ; calibrage et
  évaluation dans la même configuration ; passe de lecture sans remplissage à gauche.
- **Coût** : minutes de carte.
- **Expérience** : prédiction : le quantile 0,999 des écarts de score par action entre configurations reste sous 0,1
  écart-type honnête ; le taux de faux positifs à 1 % ne change pas au-delà de son intervalle.
- **Couverture actuelle** : en partie (garde sur les activations).

### FI-25 — Les actions non sabotées des épisodes saboteurs : ni positives, ni négatives, ni décrites

- **Où** : P-015 (« il se lit sur les seules actions sabotées, jamais par dilution des étiquettes ») ; P-011 (positifs :
  actions sabotées ; négatifs : honnêtes et témoin) ; N-004, L1 (S_{n₀}(X) = S_{n₀}(Y) + B).
- **Touche** : L (invariance), E1.3, critère 3.
- **Mécanisme** : avec p < 1, un épisode saboteur contient des actions non sabotées. Une sonde d'intention valide peut
  rester haute sur tout l'épisode : ces actions portent alors un déplacement que le budget B ne compte pas ; L1 échoue
  pour une raison favorable au défenseur, et E1.3 lirait à tort un écart au lemme. Leur statut (positif, négatif, exclu)
  n'est écrit nulle part.
- **Preuve ou argument** : textes cités ; argument.
- **Gravité** : **affaiblit**.
- **Remède** : trois classes préenregistrées (actions sabotées ; actions non sabotées d'épisodes saboteurs ; actions
  honnêtes) ; estimer le débordement ; dans E1.3, définir B sur les déplacements mesurés de toutes les actions de
  l'épisode.
- **Coût** : processeur.
- **Expérience** : prédiction bilatérale : déplacement moyen des actions non sabotées d'épisodes saboteurs contre
  l'honnête ; différence et intervalle par tâches.
- **Couverture actuelle** : non.

### FI-26 — Le maximum rend le score d'une action dépendant de sa longueur

- **Où** : programme § 8.1 et brief § 17 (maximum ou attention, jamais moyenne ni médiane) ; N-004 (F₀ unique) ; N-029
  et P-015 (la longueur est un trait du prédicteur boîte noire).
- **Touche** : L (F₀ identique), H2 (calibrage), validité incrémentale (FI-05).
- **Mécanisme** : le maximum d'une suite domine celui de son préfixe : la loi honnête du score par action croît avec la
  longueur. Un seuil calibré sur un mélange de longueurs a un taux réel qui varie avec la longueur de l'action, et toute
  différence de longueur entre conditions entre dans δ.
- **Preuve ou argument** : simulation synthétique de l'auditeur (`calculs-auditeur-v2.sortie.txt`, bloc 5 : scores par
  jeton autorégressifs, seuil calibré à 1 % sur des actions de 100 jetons ; taux réel 0,61 % à 50 jetons, 2,45 % à 200,
  4,69 % à 400). Illustration, pas une mesure de nos sondes.
- **Gravité** : **affaiblit**.
- **Remède** : calibrer par strate de longueur, ou normaliser le maximum (fenêtre de taille fixe, quantile de référence
  par longueur) ; longueur en covariable du test emboîté (FI-05) ; longueur rapportée par condition.
- **Coût** : processeur.
- **Expérience** : prédiction : pente positive du score honnête par action sur le logarithme de la longueur ; le
  déplacement δ du sabotage garde une borne basse > 0 après ajustement.
- **Couverture actuelle** : non (la règle d'agrégation est fixée pour sa robustesse ; son coût statistique n'est pas
  traité).

### FI-27 — Calibrage à 1 % sous-dimensionné, incertitude du seuil non propagée, dépassement réduit à une réserve

- **Où** : N-007 et N-008 (seuils calibrés sur les épisodes honnêtes réservés ; « intervalle, appariement des épisodes,
  calibrage … à fixer au préenregistrement de G1 ») ; brief T1.2 (« tout dépassement est une réserve ») ; P-015 (option
  (a) : « un épisode par tâche et par condition ») ; N-019 (pilote de 60 tâches d'évaluation).
- **Touche** : G1, H2.
- **Mécanisme** : un seuil conforme garanti à 1 % exige au moins 99 épisodes honnêtes de calibrage ; avec 99, le taux
  réel, conditionnel au jeu de calibrage, dépasse 3 % avec une probabilité d'environ 5 % ; avec 60 épisodes (une tâche,
  un épisode), aucun seuil fini ne garantit 1 %. Le rappel à 1 % de chaque bras hérite de l'incertitude de son seuil,
  qui doit entrer dans l'intervalle de G1. Un dépassement réduit à une réserve laisse comparer les bras à un taux nominal
  qui n'est plus le taux réel.
- **Preuve ou argument** : calcul de l'auditeur (`calculs-auditeur-v2.sortie.txt`, bloc 1 : taux réel de loi bêta par
  les statistiques d'ordre ; n = 99 : P(taux > 3 %) = 0,049 ; n = 499 : quantile 95 % du taux réel = 1,82 % ; n = 60 :
  calibrage impossible à 1 %) ; bloc 7 : avec 60 épisodes sabotés, demi-largeur de l'intervalle d'un rappel de 0,5 ≈
  0,127.
- **Gravité** : **bloque** G1 tant que les nombres d'épisodes honnêtes de calibrage et d'épisodes sabotés ne sont pas
  fixés par un calcul de puissance.
- **Remède** : calcul de taille préenregistré (au moins quelques centaines d'épisodes honnêtes réservés, appariés aux
  tâches d'évaluation) ; intervalle de G1 par rééchantillonnage conjoint du calibrage et de l'évaluation ; comparaison
  au taux réalisé apparié ; dépassement au-delà d'une tolérance fixée = arrêt, non réserve ; à défaut, 5 % comme point
  principal et 1 % en secondaire (nœud).
- **Coût** : épisodes honnêtes (400 épisodes ≈ 7 dollars au repère de P-015).
- **Expérience** : prédiction : taux réalisé sur des épisodes honnêtes neufs dans [0,5 % ; 2 %] pour 1 % nominal, n fixé
  d'avance.
- **Couverture actuelle** : en partie (garde G1-P4 ; taille non fixée dans les pièces).

### FI-28 — L'unité du taux de faux positifs n'est pas fixée entre les bras

- **Où** : programme E1.2 (« rappel à 1 % de faux positifs ») ; N-007 (« moniteur par action calibré à 1 % ») ; N-008
  (rappel à 1 % pour G1) ; brief T1.2.
- **Touche** : effet principal du séquentiel (H2), G1, interaction du 2 × 2 (FI-30).
- **Mécanisme** : un bras par action calibré à 1 % par action déclenche, sur un épisode de T actions, environ
  1 − 0,99^T fausses alarmes par épisode ; un bras séquentiel calibré à 1 % par épisode n'est pas au même point.
  Comparer leurs rappels « à 1 % » mélange deux unités ; l'effet du séquentiel peut être gonflé ou effacé selon l'unité.
- **Preuve ou argument** : calcul de l'auditeur (bloc 2 : 4,9 %, 9,6 %, 18,2 % par épisode pour T = 5, 10, 20, actions
  honnêtes indépendantes).
- **Gravité** : **bloque** la lecture de l'effet du séquentiel et de G1 si l'unité n'est pas fixée au préenregistrement.
- **Remède** : tous les bras au même point par épisode (alarme d'épisode, taux d'épisode à 1 %) ; le seuil par action à
  1 % ne sert qu'à vérifier la prémisse d'H2 ; rappel défini par épisode, par action en secondaire.
- **Coût** : nul (définition).
- **Expérience** : sans objet ; contrôle rapporté : taux par action et par épisode réalisés pour chaque bras.
- **Couverture actuelle** : non (dans les pièces fournies).

### FI-29 — La distribution des négatifs est incomplète

- **Où** : N-008 (épisodes honnêtes réservés) ; programme § 7 (honnête averti) ; N-034 § 2 (réserve « dérive de
  l'honnête sous revers ») ; P-011 (négatifs du critère 3) ; `etat-de-l-art/anteriorite-v1.md`, section HC2b (des sondes
  de tromperie réagissent à des textes qui discutent la tromperie).
- **Touche** : garantie de faux positifs, H2, G1, H8.
- **Mécanisme** : le taux nominal ne vaut que pour la loi des honnêtes calibrés. Manquent au calibrage : l'honnête averti
  de la surveillance (contrôle croisé prévu, non intégré au calibrage), l'honnête sous revers (prévu par N-034), l'honnête
  dont la tâche traite elle-même de tromperie, de sabotage ou de sécurité, l'honnête à long horizon, l'honnête après
  réglage bénin (FI-18). « Toujours valide » protège contre l'arrêt optionnel, pas contre un changement de loi.
- **Preuve ou argument** : textes cités ; argument.
- **Gravité** : **affaiblit**.
- **Remède** : strates de négatifs préenregistrées ; taux de faux positifs rapporté par strate avec intervalle ; critère
  de G1 lu sur la strate la plus défavorable, ou sur un mélange pondéré déclaré d'avance.
- **Coût** : épisodes honnêtes par strate (dizaines de dollars au total).
- **Expérience** : prédiction : taux réalisé ≤ 2 % dans chaque strate au seuil calibré à 1 % sur l'honnête standard.
- **Couverture actuelle** : en partie (honnête averti et revers prévus ; sujets voisins et long horizon non).

### FI-30 — L'interaction du plan 2 × 2 n'est pas une signature de mécanisme

- **Où** : programme § 0, point 3, et E1.2 (« interaction positive = signature de l'additivité interne (la preuve externe
  par action est quasi nulle, l'interne ne l'est pas) ») ; brief T1.2.
- **Touche** : lecture d'E1.2 ; thèse centrale.
- **Mécanisme** : sur l'échelle du rappel, deux bras qui accumulent exactement de la même façon (même gain en racine de
  n) donnent une interaction positive dès que la boîte blanche a un meilleur rapport signal sur bruit par action, que la
  preuve externe soit nulle ou seulement plus faible. L'interaction ne distingue donc pas « externe ≈ 0 » de « externe
  plus petite » ; elle dépend aussi des plafonds et planchers du rappel.
- **Preuve ou argument** : calcul de l'auditeur (bloc 4 : modèle gaussien, dix actions toutes sabotées ; preuve externe
  nulle, d noir = 0 et d blanc = 0,5 : interaction + 0,194 ; preuve externe non nulle, d noir = 0,25 : + 0,151 ; même
  rapport des d séquentiel / par action, 3,16, dans les deux bras).
- **Gravité** : **affaiblit** (lecture d'E1.2).
- **Remède** : préenregistrer l'échelle (d par action, ou probit) ; tester (1) la loi d'accumulation prédite par le lemme
  dans chaque bras, (2) l'équivalence à zéro de la preuve externe par action, avec marge, (3) la supériorité de la preuve
  interne par action ; l'interaction devient descriptive.
- **Coût** : nul (analyse).
- **Expérience** : prédiction : d boîte noire par action dans une marge autour de zéro (test d'équivalence) et d boîte
  blanche > 0 ; rappel séquentiel observé conforme à la prédiction du lemme calculée à partir des d estimés.
- **Couverture actuelle** : non.

### FI-31 — Asymétries entre bras : sélection, effort de mise au point, agrégation, graines

- **Où** : N-008 (meilleure base boîte noire « toutes variantes confondues ») ; P-011 (choix de la sonde sur un jeu
  générique) ; P-015 (« famille et couche figées d'avance ») ; programme E1.2 (« à agrégation égale ») ; P-010 (score
  boîte noire lu par espérance sur 101 jetons) ; brief R9.
- **Touche** : G1, dans les deux sens.
- **Mécanisme** : (1) si la meilleure base est choisie sur le jeu de test parmi de nombreuses variantes, son rappel est
  biaisé vers le haut (malédiction du gagnant), contre la boîte blanche dont le bras est figé : risque d'échec à tort de
  G1, donc de bascule. (2) À l'inverse, la boîte blanche reçoit cinq familles, trois couches et plusieurs concepts mis au
  point, la boîte noire quelques invites : effort asymétrique en faveur de la sonde. (3) Un même agrégateur, réglé pour
  des scores continus, peut être mal adapté aux scores presque discrets d'un juge : « à agrégation égale » n'est pas « à
  agrégation adaptée ». (4) La variance due aux graines d'entraînement des sondes et au tirage du plancher n'est pas
  propagée dans les intervalles.
- **Preuve ou argument** : calcul de l'auditeur (bloc 6 : dix variantes de même rappel vrai 0,30, 100 épisodes
  sabotés, erreurs indépendantes : meilleur rappel observé attendu 0,371, biais + 0,071).
- **Gravité** : **affaiblit** G1 (dans les deux sens).
- **Remède** : choisir la meilleure base sur une partie de validation tenue à l'écart ; budget de mise au point déclaré et
  égalisé ; agrégateur réglé par type de score sur la validation, ou agrégation par rangs ; plusieurs graines de sonde,
  incluses dans l'intervalle.
- **Coût** : une partie de validation (épisodes de plus) ; processeur.
- **Expérience** : simulation préenregistrée du biais de sélection au nombre réel de variantes ; prédiction : biais
  inférieur à une fraction fixée de la marge de G1.
- **Couverture actuelle** : non.

### FI-32 — Fuites par les tâches et par les données de distillation

- **Où** : N-019 (pilote sur les 60 premières tâches d'évaluation) ; P-015 (option (a) : « sur les tâches d'évaluation du
  pilote » ; « T7-P1 sur (i-a) est déclarée réplication de P3 sur des épisodes neufs ») ; P-009 et P-015 (données de
  distillation de (ii), « ≈ 8 000 actions », tâches d'origine non écrites).
- **Touche** : critères 2 et 3 de G0, G1.
- **Mécanisme** : des choix de conception (mode « coût », doses, positions de lecture) ont été faits après lecture de
  résultats sur des tâches qui resservent à l'évaluation décisive ; si les données de distillation de (ii) viennent des
  tâches d'évaluation, l'adaptateur apprend un sabotage propre à ces tâches.
- **Preuve ou argument** : textes cités ; la provenance des données de distillation n'est pas écrite dans les pièces.
- **Gravité** : **précision** à **affaiblit**.
- **Remède** : un lot de tâches jamais utilisé par un pilote pour l'évaluation décisive de G1 ; données de distillation
  tirées des seules tâches de réserve, identifiants disjoints vérifiés par script.
- **Coût** : extraction de tâches supplémentaires (heures de session).
- **Expérience** : prédiction : aucune différence de rappel entre tâches réutilisées et tâches neuves (test
  d'équivalence).
- **Couverture actuelle** : en partie (tâches de réserve pour la recherche de dose, P-015 (b)).

---

## D. Méthode, portes et lecture

### FI-33 — Le pivot « δ > 0 ou δ ≈ 0 » est mal posé, et E1.4 est une démonstration

- **Où** : programme § 3 (« Hypothèse empirique pivot … Si oui, le lemme s'applique ; sinon, le théorème négatif dicte
  l'agrégateur ») ; E1.4 ; brief T1.3 (« si δ ≈ 0, le théorème négatif devient central ») et T1.4 (« Valide sur données
  réelles ce que T0.3 montre en simulation ») ; R3.
- **Touche** : L, T, logique de lecture du papier A.
- **Mécanisme** : δ ≈ 0 a deux causes : la sonde est aveugle, ou le dommage passe par la dépendance à marginale
  préservée. Seule la seconde appelle un agrégateur d'autocorrélation ou de co-élévation. En mode « coût », le dommage est
  additif : δ ≈ 0 y signifierait la cécité. E1.4 injecte une dépendance construite dans des scores honnêtes réels : le
  résultat découle de T1 et T3 ; c'est une vérification de code, non une validation empirique (R3 : une démonstration).
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** (lecture de L et de T).
- **Remède** : arbre de décision préenregistré : si δ ≈ 0 (marge), tester d'abord une différence de structure de
  dépendance entre épisodes saboteurs et honnêtes (classe K), à puissance fixée ; sinon, lire « sonde aveugle » ; écrire
  E1.4 comme validation d'implémentation.
- **Coût** : nul.
- **Expérience** : prédiction bilatérale sur l'autocorrélation des scores dans les épisodes saboteurs contre honnêtes.
- **Couverture actuelle** : non.

### FI-34 — Des nuls revendiqués sans marge d'équivalence ; HC2, HC2b et HC3 comme lectures concurrentes d'une même mesure

- **Où** : programme § 5 (HC2 « g_sonde ≈ 0 » ; HC2b ; HC3 « nul sur les sondes ») ; brief TC.2 (« g_sonde ≈ 0 →
  robustesse (HC2) ; g_sonde < 0 → auto-incrimination (HC2b) ; g_sonde > 0 sans accès aux poids → contamination ») ;
  N-013 § 2 et § 5 ; R1 (« prédiction chiffrée et signe attendu »).
- **Touche** : HC2, HC2b, HC3, porte GC.
- **Mécanisme** : (1) « ≈ 0 » sans marge fixée se lit comme une absence de preuve ; un nul peu puissant « confirmerait »
  HC2. (2) HC2 et HC2b sont deux issues d'une même mesure : toute issue nulle ou négative « confirme » une hypothèse du
  programme ; le préenregistrement doit choisir la prédiction principale et les bornes des trois régions. (3) HC2b se
  teste par l'interaction plaidoyer × intention, à consignes appariées en structure dans les quatre cellules, non par
  l'effet du plaidoyer seul.
- **Preuve ou argument** : textes cités.
- **Gravité** : **bloque** la confirmation de HC2 et du volet sonde de HC3 sans marge et sans puissance préenregistrées.
- **Remède** : test d'équivalence par deux tests unilatéraux avec marge (par exemple |g| < 0,1, à fixer) et puissance
  calculée ; règle de lecture à trois régions écrite d'avance, une prédiction principale déclarée ; contraste
  d'interaction comme test de HC2b.
- **Coût** : taille d'échantillon (selon la variance de g).
- **Expérience** : celle d'EC.2, avec ces règles.
- **Couverture actuelle** : non dans les pièces (préenregistrement du papier C non fourni, non scellé).

### FI-35 — HC1 : échelles d'intensité propres à chaque famille, forme non fixée, rang testé sur trois juges

- **Où** : N-005 § 1 (régression sur plusieurs intensités ; « stabilité de rang de g entre moniteurs ») ; brief § 4, D2
  (trois juges par défaut) ; brief TC.1 (au moins trois intensités).
- **Touche** : HC1 (structure par famille, stabilité).
- **Mécanisme** : (1) l'intensité est une échelle ordinale construite par famille : comparer g entre familles mélange
  l'effet de la famille et la graduation choisie. (2) La forme de la dépendance à l'intensité (linéaire, saturante) n'est
  pas fixée : la valeur de g en dépend. (3) Avec trois juges, aucun tau de Kendall n'est significatif à 5 %, même un
  accord parfait.
- **Preuve ou argument** : calcul de l'auditeur (bloc 3 : trois juges, six ordres, P(tau = 1 au hasard) = 1/6 ; quatre
  juges : seul l'accord parfait est significatif, p = 0,042 ; six juges : tau ≥ 0,733, p = 0,028).
- **Gravité** : **affaiblit** HC1 (prédictions 2 et 3).
- **Remède** : intensité placée sur une échelle commune (force de la pression notée indépendamment, ou effet sur un juge
  de référence) ; forme préenregistrée ; au moins six juges pour le rang, ou rang lu entre familles sur un même juge.
- **Coût** : juges de plus (cartes ou appels, dizaines de dollars) ; notation de l'intensité (heures).
- **Expérience** : prédiction : rangs des familles stables entre deux constructions indépendantes de l'échelle
  d'intensité.
- **Couverture actuelle** : non.

### FI-36 — H8 : unité et nombre non fixés ; la bascule « H8 dominante » suppose des sondes qui détectent

- **Où** : programme § 5 (H8), § 11, § 13 (« G1 échoue → résultat négatif publié + H8 dominante ») ; proposition N-025
  (sur (i-a), aucune sonde générique au-dessus de son plancher).
- **Touche** : H8 ; bascule de G1.
- **Mécanisme** : H8 relie un construit mesuré à une robustesse à travers quelques sondes : sans unité d'analyse
  (variante de sonde) ni nombre fixé, la relation n'est pas estimable. Une sonde au plancher n'a pas de robustesse à
  mesurer : si G1 échoue parce que les sondes ne détectent rien, « H8 dominante » est vide.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** H8 et la bascule.
- **Remède** : score de construit défini d'avance (charges sur des contrastes intention / conscience d'évaluation) ;
  panel d'au moins une vingtaine de variantes ; corrélation de rang préenregistrée ; condition d'entrée de la bascule :
  au moins une sonde au-dessus du plancher, avec marge, sur un organisme ; sinon, « résultat négatif » seul.
- **Coût** : attaques par variante (calcul, sous GO).
- **Expérience** : prédiction signée : le rang du score de construit « intention » est corrélé positivement à la
  robustesse.
- **Couverture actuelle** : non.

### FI-37 — Papiers B et C : force d'attaque, régime d'accès et estimation, non égalisés

- **Où** : programme § 5 (H4′, H5, H7, HC5, HC6) ; E3.2, E3.3, E3.4 ; brief TC.5, TC.6 ; N-013 § 4 et § 7.
- **Touche** : H4′, H5, H7, HC5, HC6.
- **Mécanisme** : (1) le transfert d'une attaque dépend de sa force : une attaque faible transfère peu ; matrice et
  diversité effective (H5, HC5) varient avec l'effort d'optimisation. (2) HC6 compare des moniteurs dont les attaques
  optimisées n'ont pas le même régime d'accès (requêtes pour les juges, poids pour les sondes) : la robustesse mélange
  moniteur et facilité d'optimisation. (3) Le quorum (HC5) doit se comparer à faux positifs appariés, règle de décision
  fixée. (4) H4′ : une baisse de détection sous diversification peut venir de la mauvaise transférabilité des sondes aux
  variantes, non de la décorrélation des signatures. (5) H7 : l'information mutuelle s'estime mal sur peu d'itérations
  d'adaptation.
- **Preuve ou argument** : argument.
- **Gravité** : **affaiblit** (phases 2 et 3, piste C).
- **Remède** : budget d'attaque commun et déclaré (requêtes, calcul) ; transfert rapporté en fonction de la force ;
  panels par type d'accès ; quorum à faux positifs appariés ; sondes propres à chaque variante en témoin (H4′) ; puissance
  de l'estimateur d'information mutuelle calculée par simulation, nombre minimal d'itérations préenregistré.
- **Coût** : calcul des attaques (sous GO).
- **Expérience** : pour H5 : prédiction : le classement des panels par diversité effective est stable entre deux forces
  d'attaque.
- **Couverture actuelle** : en partie (taille du panel de TC.6 fixée au préenregistrement ; le reste non).

### FI-38 — Le critère de G1 n'a ni effet minimal, ni condition adverse ; pas de table « issue → revendication »

- **Où** : N-008 § 2 ; programme § 13 (succès 4 : « un verdict de validité de construit valable même si H1 échoue ») ;
  E1.5 (sans porte) ; R3, R4.
- **Touche** : G1, papier A, lecture du programme entier.
- **Mécanisme** : (1) une supériorité « établie par un intervalle » franchit G1 avec un gain négligeable si l'échantillon
  est grand. (2) G1 se lit contre un attaquant non adaptatif ; la question du programme (« sa mesure survit-elle à
  l'adversaire ? ») n'est conditionnée par aucune porte avant le papier A. (3) Plusieurs dizaines d'hypothèses et de
  bras, chacun publiable dans les deux sens, sans allocation d'erreur à l'échelle du programme ni table « issue →
  revendication » écrite avant les lectures décisives.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit**.
- **Remède** : effet minimal pertinent (Δ_min) dans G1 ; condition « attaque adaptative par contenu » (E1.5 (a)) dans G1
  ou dans la phrase-titre du papier A ; table des revendications par issue, scellée avant G1 ; hypothèses principales
  déclarées par papier, le reste exploratoire.
- **Coût** : écriture ; E1.5 (a) avant G1 (calcul modeste).
- **Expérience** : sans objet (règles de lecture).
- **Couverture actuelle** : non.

### FI-39 — La puissance des nuls décide des bascules

- **Où** : proposition N-025 (remarque 3 : demi-largeur observée ≈ 0,044 contre 0,025 à 0,037 supposées ; « la puissance
  du nul est plus faible que prévu ») ; P-015 (« 10 USD au plus par lancement sous la délégation ») ; programme § 13.
- **Touche** : toutes les bascules ; H8 ; GC.
- **Mécanisme** : sous un plafond par lancement, les échantillons sont petits ; un nul sous-dimensionné peut déclencher
  une bascule (G1 échoue → H8 dominante ; g_sonde lu « ≈ 0 ») sans être informatif.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** (portes et bascules).
- **Remède** : effet minimal détectable préenregistré pour chaque test décisif ; catégorie « non concluant » distincte
  de « nul » ; aucune bascule sur un non concluant ; plafonds de dépense déduits de la puissance requise, non l'inverse
  (nœud).
- **Coût** : selon la puissance requise.
- **Expérience** : sans objet (règle) ; contrôle : effet minimal détectable rapporté avec chaque nul.
- **Couverture actuelle** : en partie (relevé par la proposition N-025 pour un test).

### FI-40 — G0 vérifie l'existence des instruments, pas les prémisses de lecture de G1

- **Où** : brief, porte G0 (huit critères) ; P-007 ; P-015 (critères inchangés, N-027).
- **Touche** : G0, G1.
- **Mécanisme** : G0 peut être franchie avec un organisme dont la diffusion n'est pas mesurée (FI-03), un calibrage non
  dimensionné (FI-27), des négatifs non appariés en indication (FI-06), sans mode tenu à l'écart (FI-02) ; or la lecture
  de G1 en dépend.
- **Preuve ou argument** : textes cités.
- **Gravité** : **affaiblit** les portes.
- **Remède** : nœud de Lazar : ajouter à G0 des « conditions de lecture » rapportées (bloquantes ou non, à décider) :
  certificat de diffusion, taille de calibrage, négatifs appariés, mode tenu à l'écart.
- **Coût** : écriture, et le coût des remèdes cités.
- **Expérience** : sans objet.
- **Couverture actuelle** : non.

### FI-41 — L'alarme « contenu en forme d'ordre » n'a pas de taux de faux positifs mesuré

- **Où** : programme § 9 (« un contenu « en forme d'ordre » dans le canal données est en soi une alarme ») ; N-013 § 2
  (HC3 : ordres en bande « détectés presque sûrement »).
- **Touche** : HC3 (1) ; invariant 2 ; déployabilité.
- **Mécanisme** : des propositions d'expériences et des articles sont riches en phrases à l'impératif ; si leur forme
  déclenche l'alarme, le taux de faux positifs monte et épuise le budget d'audit ; si l'alarme est relâchée, « presque
  sûrement » ne tient plus.
- **Preuve ou argument** : argument.
- **Gravité** : **affaiblit** HC3 (1).
- **Remède** : mesurer le taux d'alarme sur le contenu honnête des environnements (a) et (b) ; lire HC3 (1) à taux de faux
  positifs fixé.
- **Coût** : processeur et un juge (heures).
- **Expérience** : prédiction : à taux de faux positifs fixé sur l'honnête (par exemple 1 %), le rappel des ordres en
  bande reste au-dessus d'un seuil fixé.
- **Couverture actuelle** : non.

---

## E. Gouvernance et dépendances

### FI-42 — Les décisions qui modifient une hypothèse passent par des mots brefs interprétés, des relais et une délégation

- **Où** : N-034 (« Lecture de la session : « les trois » désigne les options (a), (b) et (c) ensemble ») ; N-035
  (« Lecture de la session : « go » vaut l'option (a) ») ; N-044 et N-045 (« provenance par relais, R-331 ») ; N-019
  (décision prise sous délégation puis retirée, R-145) ; proposition N-019 v2 (« la chaîne d'alors n'exigeait pas ton GO
  et aurait pu lancer le pilote sur une simple recharge »).
- **Touche** : intégrité des préenregistrements et des revendications ; R1.
- **Mécanisme** : la règle « toute modification d'hypothèse est un nœud de Lazar » est tenue en forme ; le contenu exact
  retenu est parfois rédigé et interprété par une instance à partir d'un mot bref ou relayé ; une hypothèse peut entrer
  au programme (H9, bras « revers ») dans une formulation que Lazar n'a pas lue mot pour mot.
- **Preuve ou argument** : textes cités ; la correction de N-019 montre que le risque s'est réalisé une fois et a été
  rattrapé.
- **Gravité** : **affaiblit**.
- **Remède** : confirmation sur empreinte : toute décision de type « revendication » ou « hypothèse » est confirmée par
  Lazar sur le texte exact retenu (empreinte citée) avant qu'un préenregistrement en dépende ; une décision relayée
  attend cette confirmation directe.
- **Coût** : quelques minutes de Lazar par décision.
- **Expérience** : audit descriptif des décisions passées (part de décisions interprétées ; confirmation sur empreinte
  présente ou non).
- **Couverture actuelle** : en partie (les notes déclarent leurs lectures ; aucune confirmation sur empreinte).

### FI-43 — Contre-lectures et verdicts de porte par des instances du même modèle

- **Où** : brief R2 et R13 (« sous-agent neuf ») ; brief de l'audit, § 4 (synthèse contre-lue « par un agent neuf d'un
  autre modèle »).
- **Touche** : toutes les portes ; tous les préenregistrements.
- **Mécanisme** : « neuf » garantit l'absence de contexte partagé, pas l'indépendance des a priori ni des angles morts ;
  des erreurs corrélées entre auteur, contre-lecteur et juge de porte passent toutes les gardes.
- **Preuve ou argument** : argument ; l'audit lui-même prévoit un autre modèle pour sa synthèse.
- **Gravité** : **affaiblit**.
- **Remède** : au moins un contre-lecteur d'une autre famille de modèles, ou humain, pour les préenregistrements de porte
  et les verdicts de G0, G1 et GC (modification d'une règle gelée : décision de Lazar).
- **Coût** : appels de modèles (dollars) et délai.
- **Expérience** : étude préenregistrée : défauts connus injectés dans un préenregistrement fictif ; taux de détection
  par des contre-lecteurs du même modèle et d'un autre ; prédiction : le second trouve des défauts que le premier manque.
- **Couverture actuelle** : non (sauf la synthèse de cet audit).

### FI-44 — Énoncés en vigueur dispersés ; « P3 » désigne trois objets

- **Où** : programme v2 non réécrit, lu avec N-003 à N-045 et P-008 ; « programme fusionné » v4 évoqué (N-023, N-034)
  sans être fourni ; « P3 » : le projet antérieur de Lazar (programme § 11, § 12 ; brief § 2), le « premier test (i-a) »
  de ce programme (proposition N-025 ; N-026 ; N-029 ; P-015), une prédiction du pilote de T0.5 (proposition N-019 v2,
  proposition N-021 : « P3 non concluante »).
- **Touche** : préenregistrements (risque de citer un énoncé périmé : nom de HC2b, liste de H6, bras F1 de G1, porte
  GC) ; lecture des « leçons de P3 ».
- **Mécanisme** : un préenregistrement peut citer le texte du programme au lieu de l'énoncé retenu ; une leçon ou un
  chiffre « de P3 » peut être attribué au mauvais objet.
- **Preuve ou argument** : textes cités.
- **Gravité** : **précision**.
- **Remède** : une table empreintée « énoncés en vigueur » (hypothèse → énoncé → décision → date), régénérée à chaque
  décision et citée par les préenregistrements ; renommer les trois « P3 ».
- **Coût** : une heure.
- **Expérience** : sans objet.
- **Couverture actuelle** : non (dans les pièces fournies).

---

## F. Synthèse

### F.1 Table des failles

Priorité proposée : **P1** = à traiter avant le scellement du préenregistrement de G1 ou de celui du papier C, ou avant
G0 ; **P2** = avant la rédaction du papier concerné ; **P3** = phases 2 et 3, ou précision.

| faille | titre court | touche | gravité | coût du remède | priorité |
|---|---|---|---|---|---|
| FI-01 | construit réduit au coût déclaré | H1, A | bloque | nul à quelques dollars | P1 |
| FI-02 | aucun mode tenu à l'écart | H1, G1 | bloque (générique) | quelques dollars | P1 |
| FI-03 | régime diffus défini par nos bases | H1, H2 | affaiblit ; bloque (général) | dizaines de dollars | P1 |
| FI-04 | taux de change dommage / score | L, sécurité | bloque (sécurité) | faible | P1 |
| FI-05 | pas de validité incrémentale | thèse, H1 | affaiblit ; bloque (thèse) | processeur | P1 |
| FI-06 | information non appariée, négatifs de G1 | G1 | bloque | nul | P1 |
| FI-07 | test (i) contre (ii) non identifiant | H8, T0.7 | affaiblit | faible à dizaines de dollars | P2 |
| FI-08 | sondes apprises en lecteur | HC2, G1 | affaiblit | quelques dollars | P2 |
| FI-09 | vérité terrain d'un fournisseur, corruptible | G0 c. 2 | affaiblit | heures, dollars | P2 |
| FI-10 | avantage dépendant du bruit honnête | H1 | affaiblit | processeur | P2 |
| FI-11 | organismes non conditionnés à l'observation | H8, construit | affaiblit | processeur ; dizaines de dollars | P2 |
| FI-12 | élicitation sans règle d'arrêt | sécurité, Tr | affaiblit | effort rouge | P2 |
| FI-13 | un modèle ; (iii) non comparable | généralité | affaiblit ; précision | dizaine de dollars | P2 |
| FI-14 | profil d'adversaire non écrit | robustesse | affaiblit | écriture | P2 |
| FI-15 | fragmentation entre épisodes | L, H2, H3, invariants 4 et 6 | affaiblit ; bloque (patient) | processeur | P2 |
| FI-16 | asymétrie d'apprentissage | invariant 7 | affaiblit | faible | P2 |
| FI-17 | retour du protocole vers l'agent | invariants 3 et 5, A | affaiblit | dollars | P2 |
| FI-18 | dérive à la mise à jour | garantie | affaiblit | nul à faible | P2 |
| FI-19 | canal authentifié, mandant non fiable | invariants 1 et 2, B | affaiblit | écriture | P3 |
| FI-20 | sondes lectrices en multi-agents | population | affaiblit | faible | P3 |
| FI-21 | cause commune | population, G2 | affaiblit | dollars | P3 |
| FI-22 | frontière, vivacité du moniteur | B | précision ; affaiblit | faible | P3 |
| FI-23 | invariants et lignée des organismes | cohérence | précision | écriture | P3 |
| FI-24 | maximum et queue numérique | garantie | affaiblit | minutes de carte | P1 |
| FI-25 | actions non sabotées des épisodes saboteurs | L, E1.3 | affaiblit | processeur | P1 |
| FI-26 | maximum et longueur | L, H2 | affaiblit | processeur | P1 |
| FI-27 | calibrage à 1 % sous-dimensionné | G1, H2 | bloque | ≈ 7 dollars par 400 épisodes | P1 |
| FI-28 | unité du taux de faux positifs | G1, H2 | bloque (lecture) | nul | P1 |
| FI-29 | négatifs incomplets | garantie, G1 | affaiblit | dizaines de dollars | P1 |
| FI-30 | interaction non diagnostique | E1.2 | affaiblit | nul | P1 |
| FI-31 | asymétries entre bras | G1 | affaiblit | épisodes de validation | P1 |
| FI-32 | fuites par les tâches | G0, G1 | précision ; affaiblit | heures | P2 |
| FI-33 | pivot δ mal posé ; E1.4 | L, T | affaiblit | nul | P2 |
| FI-34 | nuls sans marge ; HC2/HC2b/HC3 | C, GC | bloque (HC2) | taille d'échantillon | P1 |
| FI-35 | HC1 : intensités, forme, rang | HC1 | affaiblit | dizaines de dollars | P1 |
| FI-36 | H8 et sa bascule | H8 | affaiblit | calcul sous GO | P2 |
| FI-37 | B et C : force d'attaque, accès | H4′, H5, H7, HC5, HC6 | affaiblit | calcul sous GO | P3 |
| FI-38 | G1 sans effet minimal ni adverse | G1, A | affaiblit | écriture ; calcul modeste | P1 |
| FI-39 | puissance des nuls et bascules | portes | affaiblit | selon puissance | P2 |
| FI-40 | G0 et prémisses de G1 | G0, G1 | affaiblit | écriture | P1 |
| FI-41 | alarme « en forme d'ordre » | HC3 (1) | affaiblit | heures | P2 |
| FI-42 | chaîne des décisions | intégrité | affaiblit | minutes | P2 |
| FI-43 | contre-lecteurs du même modèle | portes | affaiblit | dollars, délai | P2 |
| FI-44 | énoncés dispersés ; « P3 » | préenregistrements | précision | une heure | P3 |

Bilan : 44 failles candidates ; 10 avec au moins un volet **bloque** (FI-01, 02, 03, 04, 05, 06, 15, 27, 28, 34) ;
34 sans volet bloquant, dont 31 de gravité principale **affaiblit** (FI-13 et FI-32 ont en plus un volet précision) et
3 de gravité principale **précision** (FI-22, FI-23, FI-44 ; FI-22 et FI-23 passent à « affaiblit » sous une condition
écrite dans leur fiche).

### F.2 Les trois plus graves, au niveau de la méthode

1. **FI-06** — G1 peut être gagnée par une différence d'information : la sonde lit le contexte privé où se trouve
   l'indication de sabotage, le juge non, et les négatifs qui fixent le seuil de G1 ne contiennent pas le témoin qui
   reçoit la même indication.
2. **FI-01 avec FI-02** — ce qui est mesuré (un champ chiffré gonflé, dans un mode connu de qui conçoit les moniteurs)
   n'est plus ce qui est revendiqué (un sabotage diffus sur tâches floues, de mode non annoncé).
3. **FI-04** — le lemme garantit une puissance en unités de score ; la sécurité se définit en dommage ; aucun
   préenregistrement ne mesure le taux de change entre les deux, que l'attaquant choisit.

Suivent de près FI-27 et FI-28 (le point « 1 % de faux positifs » de G1 n'est ni dimensionné ni défini dans une unité
commune) et FI-15 (la fragmentation entre épisodes, que deux invariants empêchent d'accumuler).

### F.3 Ce qui demande une décision de Lazar (nœuds au sens du brief, § 4)

| décision | failles | type |
|---|---|---|
| Restreindre les revendications du papier A au mode chiffré, ou ajouter un mode non chiffré avant G1 | FI-01 | revendication ou périmètre |
| Un mode de sabotage tenu à l'écart de la conception, révélé à l'évaluation de G1 | FI-02 | périmètre interne (proposer) |
| Courbe en dose plutôt que dose retenue ; base qui définit le régime | FI-03 | périmètre interne (proposer) ; juge 70B : GO |
| Énoncer la sécurité sous condition de taux de change mesuré | FI-04 | revendication |
| Négatifs de G1 appariés en indication, ou G1 sur la famille (ii) | FI-06 | méthode de G1 (critère N-008 : décision de Lazar) |
| Point de fonctionnement principal à 5 % si le calibrage à 1 % n'est pas finançable | FI-27 | critère de porte |
| Effet minimal et condition adverse dans G1 ; table « issue → revendication » | FI-38 | critère de porte |
| Plafonds de dépense déduits de la puissance | FI-39 | dépense |
| Conditions de lecture ajoutées à G0 | FI-40 | critère de porte |
| Mémoire de statistique permise entre épisodes ; sécurité au niveau du déploiement | FI-15 | invariant, définition |
| Invariants applicables à la lignée des organismes | FI-23 | périmètre |
| Confirmation des décisions sur empreinte | FI-42 | gouvernance |
| Contre-lecteur d'une autre famille pour les portes | FI-43 | règle gelée |
| Réplication sur Qwen2.5-7B dès la phase 1 | FI-13 | périmètre ; dépense |

---
Horodatage : failles FI-01 à FI-44 et sections A à F closes le 2026-10-26 à 11:01:39 UTC (heure lue sur date -u dans la commande qui écrit cette ligne), avant toute lecture du complément de session-depot ; rien de ce qui précède ne sera modifié après cette ligne.

## G. Recoupements avec l'audit de la littérature de session-depot

- **Pièce** : `fournis-complement/audit-litterature-session-depot-v1.md` (`29b32f62…`, empreinte vérifiée), versée par la
  lignée session-depot et transmise par le coordinateur pendant ce lot ; lue **après** la clôture des sections A à F
  (horodatage ci-dessus ; à ce point, le fichier faisait 86 099 octets et son empreinte valait `38d3c8e6…` : les 86 099
  premiers octets du fichier final redonnent cette empreinte). Les sections A à F n'ont pas été modifiées.
- **Notation** : « b1 » à « b11 » = ses angles morts (sa section b) ; « S1 » à « E7 » = ses failles documentées (sa
  section a). **Oui** = même hypothèse mise en défaut par le même mécanisme ; **en partie** = même hypothèse, mécanisme
  ou remède différent ; **non** = aucun de ses angles morts ne la porte. La colonne « voisine » signale, sans jugement de
  couverture, la faille documentée la plus proche quand il y en a une.

| faille | recoupe un angle mort ? | n° | faille documentée voisine | ce qui diffère |
|---|---|---|---|---|
| FI-01 | non | — | S5 | la réduction du sabotage mesuré à un champ chiffré (P-015, P-014) n'apparaît pas chez lui |
| FI-02 | non | — | S4 | côté défenseur : conception des moniteurs informée par le mode connu |
| FI-03 | non | — | S7, S8 | circularité entre la définition du régime diffus et le comparateur de G1 |
| FI-04 | en partie | b11 | — | b11 : répartition choisie par l'attaquant ; FI-04 : unités (score contre dommage) |
| FI-05 | en partie | b5 | S2 | b5 masque des positions ; FI-05 teste l'apport au-delà des traits du texte (modèle emboîté) |
| FI-06 | en partie | b5, b2 | S2 | négatifs de calibrage de G1 sans le témoin apparié en indication ; juge privé du contexte (P-009, P-010, N-008) |
| FI-07 | oui (explication 2) | b2 | S3, D1 | l'explication 1 (pas de représentation d'intention dans (ii)) et l'écart de dosage α / proportion |
| FI-08 | non | — | D1 | position de lecteur des jeux synthétiques écrits par un sous-agent (P-011) |
| FI-09 | non | — | S5 | biais d'un seul fournisseur ; étiqueteurs exposés à la loi de déférence |
| FI-10 | en partie | b8 | — | bruit honnête de l'agent, non sa taille |
| FI-11 | en partie | b3, b2 | E1 | organisme conditionnel à l'observation perçue (disposition dormante) |
| FI-12 | en partie | b11 | S4 | règle d'arrêt de l'élicitation ; sécurité écrite comme infimum sur la classe testée |
| FI-13 | oui | b8 | E5, D2 | les organismes (iii) reposent sur un modèle de 70 milliards (divergence DV-2) |
| FI-14 | non | — | D8 | table des profils d'adversaire ; régime « poids réglables » hors périmètre |
| FI-15 | en partie | b11 | — | côté détecteur : indice d'épisode absent, amnésie, sécurité définie par épisode |
| FI-16 | en partie | b6 | D4 | survivance, influence sur l'ensemble détecté, conflit avec l'anti-circularité |
| FI-17 | non | — | S6, D5 | retour de l'environnement (a) et des interventions pendant l'épisode |
| FI-18 | non | — | S7 | dérive de calibrage à la mise à jour, mesurable sur l'adaptateur témoin |
| FI-19 | non | — | — | — |
| FI-20 | non | — | — | — |
| FI-21 | non | — | — | — |
| FI-22 | non | — | — | — |
| FI-23 | en partie | b6 | D5 | déclaration des invariants pour la lignée des organismes (divergence DV-6) |
| FI-24 | non | — | — | — |
| FI-25 | non | — | — | — |
| FI-26 | non | — | — | — |
| FI-27 | non | — | — | — |
| FI-28 | non | — | — | — |
| FI-29 | en partie | b9 | D6 | strates d'honnêtes absentes (averti, revers, sujet voisin, long horizon, réglage bénin) |
| FI-30 | non | — | — | — |
| FI-31 | non | — | S7 | malédiction du gagnant, effort de mise au point, agrégateur, graines |
| FI-32 | non | — | — | — |
| FI-33 | non | — | — | — |
| FI-34 | non | — | D3 | règle de lecture : marge d'équivalence, trois régions, contraste d'interaction |
| FI-35 | non | — | — | — |
| FI-36 | en partie | b8, b4 | D2, E2 | b8 et D2 : porte préalable de séparabilité ; FI-36 : unité, nombre de sondes et entrée de la bascule |
| FI-37 | non | — | D9 | force d'attaque et régime d'accès égalisés entre moniteurs |
| FI-38 | non | — | — | — |
| FI-39 | en partie | b8 | D2 | puissance des nuls avant toute bascule |
| FI-40 | non | — | — | — |
| FI-41 | non | — | — | — |
| FI-42 | non | — | — | — |
| FI-43 | non | — | — | — |
| FI-44 | non | — | — | — |

Bilan : 2 failles recoupent un de ses angles morts (FI-07 avec b2, FI-13 avec b8) ; 12 le recoupent en partie (FI-04,
05, 06, 10, 11, 12, 15, 16, 23, 29, 36, 39) ; 30 ne recoupent aucun de ses angles morts. Réciproquement, ses angles morts
b1 (contrôlabilité des directions par consigne), b7 (règle de sélection du ré-échantillonnage), b10 (conscience
d'évaluation du moniteur génératif) et la seconde moitié de b6 (scores de moniteur dans l'entraînement de l'agent) n'ont
aucune faille interne correspondante ; b4 n'est touché que par FI-36. Ce sont des failles que la lecture de nos seuls
documents ne faisait pas voir : limite de ce lot.

## H. Divergences : où ma lecture des documents contredit la sienne

### DV-1 — L'environnement (a) : vérité terrain et mode de sabotage

- **Sa lecture** : S5, « En partie. Le programme a le critère « flou à la relecture, vérifiable en aval », des cibles
  semées et une vérification différée sur sous-échantillon (section 6, (a)) » ; b9. Ses pièces lues ne comprennent ni
  P-006, ni P-014, ni P-015.
- **La mienne** : `decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md` (« le pilote n'a retenu que la famille
  « coût » » ; T0.6 : « « Affaiblir les contrôles » sort ») ; `decisions/decision-P-014-reference-appariement-T0.6-v1.md`,
  point 2 (les directions sortent de la vérité terrain) ; `decisions/proposition-P-006-T0.5-v1.md`, option (a) (le proxy
  fort qui lit le papier est reporté en phase 1). La vérification différée n'est pas en place pour G1, et le sabotage
  mesuré est un champ chiffré.
- **Conséquence** : la couverture « en partie » de S5 repose sur des dispositifs retirés ou reportés ; S5 et b9
  s'appliquent avec plus de force (FI-01, FI-09).

### DV-2 — La famille (iii)

- **Sa lecture** : S1 (« famille (iii), les organismes de l'institut britannique, dont un qui imite Llama-3.1-8B-Instruct » ;
  remède « Lire les sondes sur la famille (iii) avant G1 », coût « quelques heures de carte ») ; synthèse et b2 (« Tous les
  organismes tiennent leur politique d'un texte »).
- **La mienne** : `etat-de-l-art/corrections-v1.md`, section 1, ligne 15 : Cedar, Oak et Beren ont tous été entraînés à
  imiter Llama-3.1-8B-Instruct, mais reposent sur Llama-3.3-70B-Instruct, ajusté par appariement de distributions de
  sortie ; leur politique est apprise par réglage fin d'imitation, sans consigne dans le contexte. Nos sondes, apprises sur
  les activations du 8B, ne s'y lisent pas sans sondes propres au 70B.
- **Conséquence** : le remède de S1 suppose une inférence de 70 milliards et des sondes propres (FI-13) ; « tous les
  organismes tiennent leur politique d'un texte » vaut pour (i) et (ii), pas pour (iii), qui relève toutefois du
  sous-rendement, en 70 milliards et sous réserve de licence : la famille (iv) qu'il propose reste sans équivalent au
  programme pour le sabotage diffus en 8B.

### DV-3 — La lecture du contexte privé : un contrôle est prévu au brouillon de G1

- **Sa lecture** : S2 (« L'antériorité niveau 2 la note comme contre-indice ; aucun bras ne la mesure ») ; b5.
- **La mienne** : `etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md`, prononcé 4, dernier point : 2509.21344 est
  « intégré au brouillon 2 de G1 … par le contrôle « sans texte », G1-P5 ».
- **Conséquence** : b5 est « en partie couvert » d'après nos pièces ; le contenu de G1-P5 n'étant fourni ni à lui ni à
  moi, la synthèse doit le lire avant de classer b5 (et FI-06).

### DV-4 — HC4 « contexte seul » est une prédiction à tester ; EC.2 mesure déjà le déplacement des sondes par le contenu

- **Sa lecture** : b1 (HC4 « contexte seul » et HC2 « supposent que l'agent ne pilote pas, par le contexte, ce que lit la
  sonde ») ; proposition 1 (« aucun bras du programme ne tranche »).
- **La mienne** : `decisions/decision-N-013-v1.md`, § 3 (« contexte seul : l'écart « de plusieurs ordres de grandeur »
  reste la prédiction à tester ») ; `docs/programme-controle-ia-v2.md`, EC.2, et brief TC.2 (g_sonde sous attaques par
  contenu, plan 2 × 2 rhétorique × intention).
- **Conséquence** : ce qui manque est une condition précise (une consigne explicite d'agir sur une direction de sonde),
  non tout bras sur le déplacement des sondes par le contexte : « non couvert » devient « en partie ».

### DV-5 — D6 est jugée « couverte », mais les négatifs de G1 n'ont pas d'honnêtes sur sujet voisin

- **Sa lecture** : D6, « Oui. EC.2 croise rhétorique et intention … HC2b est contrôlée contre le style … L'agrégation est
  faite par max ou attention » ; il propose pourtant d'ajouter une condition « aveu honnête ».
- **La mienne** : `decisions/decision-N-007-N-008-v1.md`, § 2 (négatifs de G1 : épisodes honnêtes réservés) ; EC.2
  appartient au papier C ; aucune strate d'honnêtes dont le sujet touche la faute ou la tromperie n'entre dans le
  calibrage du papier A (FI-29).
- **Conséquence** : « en partie » plutôt que « oui », au moins pour le papier A.

### DV-6 — L'extension de D5 à la lignée des organismes

- **Sa lecture** : D5 (« Il vaudrait aussi pour la piste « organisme » (N-045, coût dans le signal) »).
- **La mienne** : `decisions/decision-N-045-v2.md`, énoncé 2 : le signal rendu à l'organisme est l'exactitude équilibrée
  d'un juge de tâche et le coût de la génération en dollars, non un score de moniteur de contrôle ;
  `decisions/decision-N-044-v1.md`, énoncé 5 : « le juge est la seule pression ». Appliquée telle quelle, la règle de D5
  interdirait le dispositif même de cette lignée.
- **Conséquence** : la règle doit viser les scores des moniteurs de contrôle (sondes et juges de sabotage, de tromperie
  ou de conscience d'évaluation) qui entreraient dans l'entraînement ou la sélection d'un agent surveillé ; pour la lignée
  des organismes, la question est celle de FI-23 (quels invariants s'y appliquent).

### DV-7 — Les usages de 2510.09462 au programme (mineure)

- **Sa lecture** : S6 (« Le programme cite cette source pour HC1 et HC3 seulement »).
- **La mienne** : `docs/etat-de-l-art-controle-ia-v1.md`, § 3.1 (papier B : attaquant qui connaît protocole et
  moniteur) ; `etat-de-l-art/anteriorite-v1.md`, section HC5 (transfert des injections entre moniteurs).
- **Conséquence** : mineure ; la faille S6 (règle de sélection de H6) reste non couverte d'après mes pièces aussi.

### DV-8 — N-019 n'est pas « sans effet » pour un audit de la méthode (mineure)

- **Sa lecture** : liste des pièces lues, « N-019 (opérationnelle, sans effet ici) ».
- **La mienne** : `decisions/decision-N-019-v1.md` et `decisions/proposition-N-019-v2.md` : une décision prise sous
  délégation a changé une lecture gelée d'un préenregistrement scellé, puis a été retirée ; la chaîne de lancement
  d'alors n'exigeait pas de GO.
- **Conséquence** : sans effet sur les hypothèses, mais pertinente pour la fragilité de méthode (FI-42).

---
Horodatage : sections G et H ajoutées après lecture du complément ; fichier clos le 2026-10-26 à 11:06:42 UTC (heure lue sur date -u dans la commande qui écrit cette ligne).
