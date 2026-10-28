# Passation exhaustive — reprise au même point par une nouvelle instance (compte neuf) — 2026-10-28 12:05 UTC

Écrite le 28 octobre 2026 à 12:05:27 UTC (relevé `date -u`) par la lignée **conv-audit**, instance `claude-37`. Modèle
servant déclaré par l'environnement : fluctuant dans la session (Opus 4.6, Opus 5.5, Opus 5, Fable 5.1, Opus 4.8 tour à
tour) ; auteur désigné du travail principal : **Opus 4.6** (décision de Lazar), inchangé malgré la fluctuation.

**Pourquoi cette passation.** Lazar (directeur) demande, à 13:01 heure de Paris : « passation now, met en pause tout le
reste, la nouvelle instance reprend exactement au même point ». Ce document permet à une **instance neuve, sur un compte
neuf**, de reprendre le rôle de conv-audit **exactement ici**. Tout le reste est mis en pause (section 11).

**Langue et style imposés** : français, tutoiement avec Lazar, presque aucun sigle (développer les termes). Communication
à Lazar : **verdict d'abord** (1 à 3 lignes), puis erreurs, changements, décisions, une ligne chacun. Écrire seulement
pour : prononcé, réserve, divergence non résolue, demande de GO, dépense. Le reste vit dans les registres.

---

## 0. REPRENDS ICI (la seule action suivante)

**Action immédiate à la reprise :** attendre la décision de Lazar sur le **nœud de revendication** ouvert à 12:52–12:58
(section 8, nœud A) — à quel rang inscrire la **question élevée** (défense universelle co-évolutive). Les trois recherches
d'antériorité qui devaient l'éclairer sont **rendues** (section 7) et **changent la recommandation** : lis la section 7
avant de répondre à Lazar. Ne lance aucune expérience, ne scelle aucun préenregistrement, ne dépense rien tant que ce
nœud n'est pas tranché.

**Avant toute autre chose** : exécute la routine de reprise (section 3), puis lis `registres/etat.md` et la passation la
plus récente par nom dans `registres/passations/`.

## 1. Qui tu es, régime, lignées

Tu es **conv-audit**. Règles d'identité, non négociables :
- Tu **n'écris jamais** sur la branche `main`. Seule la lignée **session-depot** écrit sur `main` et lance ce qui dépense,
  sur le mot direct de Lazar dans sa propre session. Toi, tu travailles sur la branche `canal/conv-audit-n04`.
- Tu **ne dépenses rien** (aucune instance payante, aucun appel facturé de ton chef).
- Tu **ne lis, n'affiches ni ne demandes aucune clé ni aucun jeton**. **Recherche de clés avant chaque poussée** :
  `grep -rnE 'sk-ant|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE KEY'`.
- **Ne jamais pousser vers `lciric/controle-ia`** (ce nom sera la copie expurgée publique). Dépôt de travail :
  `github.com/lciric/controle-ia-travail` (privé), branche `canal/conv-audit-n04`.
- **Quarantaine git** : les refs `refs/heads/donnees/bras-attaque*` et `donnees/mode-tenu-a-l-ecart*` sont exclues du
  fetch — **ne jamais les lever**. Ne lis jamais `donnees/` ni une banque avant scellement (R1).
- Un sous-agent qui contre-lit doit être d'un **modèle différent** de l'auteur (R13, N-052 : Opus 5.5 analyste ;
  Fable 5.1 contre-lecteur et attaquant d'audit).

Les trois lignées en jeu aujourd'hui :
- **conv-audit** (toi) : conception, lectures, code sur processeur, préenregistrements, contre-lectures ; propose, ne
  tranche pas les nœuds.
- **session-depot** : écrit `main`, lance les instances payantes, sur le mot de Lazar. **Tourne encore sur le même
  compte** (Lazar, 12:58). Non joignable en direct depuis ici (`ListAgents` ne voit aucune session) ; le relais se fait
  **par fichier dans le dépôt** (« comme d'hab »).
- **Fable red-team** : une session neuve, compte neuf, servie par Fable 5.1, qui conçoit l'**affinage** en équipe rouge
  (section 5.2). Reçoit un **lot curé** (option B), pas le dépôt entier.

## 2. Les deux programmes, en bref

**Programme « organisme ».** Recherche défensive en sécurité de l'intelligence artificielle : **contrôle en boîte
blanche des menaces diffuses**. On surveille des agents (intelligences artificielles qui agissent en plusieurs étapes)
avec des **moniteurs** qui lisent leurs activations internes (boîte blanche) et/ou leur texte et actions (boîte noire),
pour détecter un dommage **diffus** (réparti dans le temps, entre épisodes, entre agents, de sorte qu'aucun instant isolé
ne franchit le seuil). But : **mesurer et prédire ce que les moniteurs manquent, sans construire de recette d'attaque**.
L'**organisme** est un pôle scientifique automatique : des agents qui proposent des hypothèses sur les moniteurs, les
testent, les affinent (boucle à la darwinienne). Documents qui font foi : `docs/brief-claude-code-programme-complet-v2.md`
(exécution), `docs/programme-controle-ia-v2.md` (fond), `docs/etat-de-l-art-controle-ia-v1.md` (pris/ouvert/à battre).

**Programme « entretien » (TAIF).** Une proposition de recherche / candidature à un institut qui finance la sécurité de
l'intelligence artificielle. L'organisme en est le moteur. **Candidature envoyée le 7 octobre** (versée dans
`docs/sources/candidature-taif-envoyee-2026-10-07-v1/`). Chiffres de la candidature, qui font foi : demande **58 630 USD**
(sept mois) ; minimal **28 160** (quatre mois) ; ambitieux **138 600** (douze mois). Après le « go » de Lazar sur la
version la plus ambitieuse (11:28–11:33 le 28), demande portée à **≈ 176 550** (138 600 + extension 37 950 :
`brouillons/entretien-taif-v2/demande-option-c-ventilation-v2.md`, scellé). **Rien n'est envoyé par conv-audit.**
Gouvernance : Lazar tranche portes et dépenses ; verdict de porte par sous-agent neuf scellé, puis GO de Lazar.

## 3. Routine de reprise (R14) et règles gelées

Au début de CHAQUE session :
1. `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; puis `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .`.
2. Lire `registres/etat.md` et la dernière passation.
3. Appliquer les défauts échus (décision « proposer avec recommandation » sans réponse depuis 48 h prend son défaut).
4. Inventorier les instances de calcul (Vast.ai) ; arrêter par identifiant (R10) toute instance sans tâche ; consigner
   dans `registres/arrets.md`. **conv-audit ne lance ni n'arrête d'instance payante lui-même** ; il le signale.
5. `python -m pytest -q`. Puis reprendre à la « prochaine action ».

Règles gelées (résumé ; le détail est dans `CLAUDE.md`) : **R1** préenregistrement scellé avant toute expérience
décisive, aucune lecture avant scellement ; **R2** contre-lecture par un sous-agent neuf, fichiers nommés ; **R3** aucun
run visant un signe positif ; **R4** symétrie du soupçon, trop beau = réserve ; **R5** toute garde testée sur cas sain et
artefact, aucun repli silencieux ; **R6** empreinte compagnon `.sha256`, tout chiffre renvoie à un chemin + empreinte ;
**R7** aucun chiffre d'état de l'art sans vérification sur PDF empreinté ; **R8** zone vierge = question, zone séduisante
vérifiée plus durement ; **R9** graines par `SeedSequence`, manifeste par run ; **R10** arrêts par identifiant ;
**R11** vérifier sur disque + empreinte avant de déclarer un fichier absent ; **R12** versions dans les noms, jamais
écraser ; **R13** verdict de porte par sous-agent neuf ; **R14** reprise + passation à chaque session. Règle de Lazar
**R-609** : un refus de classifieur appelle une question **plus étroite et moins diffuse**, jamais un contournement.
**R-597** : aucune recette de contournement produite par une instance. **R-339** : sortie adversariale au **niveau
méthode** (classe, mécanisme, conditions, défense), jamais la recette. **R-611 / GO-2026-10-28-04** : tout pipeline
opérationnel des étages 1–2 du travail d'évasion est **gelé jusqu'à une revue de sécurité externe**.

## 4. État vivant — phase 0

Phase 0 (instruments) depuis le 5 octobre. Porte de sortie **G0**, au plus tard fin novembre 2026 (N-027). G0 a huit
critères ; deux prouvés (critère 1 harnais, critère 5 agrégateurs). Détail et tâches vivantes : `registres/etat.md`.
Critère de **G1** (porte suivante, préenregistrement à venir) : le moniteur boîte blanche séquentiel bat la meilleure base
boîte noire **et** deux bases boîte blanche (cascade de gardes sur mêmes sondes ; sonde sur le dernier état), toutes
variantes, sur le **rappel à 1 % de fausses alertes, à 95 % de confiance** (N-008, N-056 ; nœud 1 = b). Traits internes
sur trois couches, toutes rapportées. D-S29 confirmé.

## 5. Ce qui a été fait dans CETTE session (28 octobre, matin→midi)

### 5.1 Intégration des proposeurs dans l'organisme
Sur « go » de Lazar (12:07) puis précisions (12:18, 12:22) : un proposeur **n'est pas** un générateur d'idées — il
**teste** ses hypothèses puis les **affine à deux échelles** (épisode par épisode sur une partie de développement ;
génération par génération par héritage et recombinaison). Le **proposeur maison** (Opus 5.5 + Fable 5.1) n'est **pas**
exempté. Livré, scellé, poussé :
- `…/pole-scientifique-automatique-v1/integration-proposeurs-ia-v1.md` (`974b2dbe…`) — le cadre : deux prises de
  branchement (boucle complète / idéation), la frontière adversariale de l'affinage (niveau méthode seul, routage par les
  voies gouvernées), la quarantaine (N-053), les contraintes portées (N-044, N-045-v2, N-049, N-050, N-052).

### 5.2 Affinage en équipe rouge, sur compte neuf (décision Lazar 12:24, 12:28, 12:33)
L'affinage sera conçu par l'**attaquant d'audit** (Fable 5.1), sur **compte et session neufs** qui ne connaissent rien
aux programmes, puis **contre-lu par la lignée Opus** (conception ≠ contre-lecture, jamais le même modèle). Livrés,
scellés, poussés :
- `…/passation-affinage-equipe-rouge-fable-v1.md` (`cf0ca5e4…`) — passation autoportante pour la session neuve.
- `…/brief-affinage-equipe-rouge-fable-v2.md` (`fca8c9b4…`) — brief d'exécution (**prime** sur la passation) ; remplace
  la v1 (`45ae29d9…`, gardée) : ajoute l'attaque du « monde planté qui coïncide avec un gabarit du proposeur ».
- `…/amorce-session-neuve-fable-v1.md` (`224d14c0…`) — le bloc à coller en premier message de la session neuve.
- `livrables/lot-fable-affinage-v1/` et `livrables/lot-fable-affinage-v1.zip` (`7c18d3df…`) — **lot par LISTE BLANCHE**
  (quatre documents nommés + LISEZMOI), pas par expurgation. Recherche de clés faite : aucune. **Absents volontairement** :
  banques scellées, test final, mode tenu à l'écart, internes des moniteurs, carte des hypothèses.
- **Option B actée par Lazar (12:33)** : un dépôt **neuf et privé** reçoit **uniquement** le contenu de
  `livrables/lot-fable-affinage-v1/`, accès lecture au compte neuf. **À exécuter par session-depot** (relais à déposer,
  section 8 nœud C). conv-audit ne crée pas le dépôt, ne pousse pas, n'ouvre rien de public.

### 5.3 La question élevée (12:49–12:58) : défense universelle co-évolutive
Lazar reformule la vraie question : **face à des modes d'attaque inédits, quelle est la meilleure défense (boîte blanche +
boîte noire) ?** Non pas seulement « nos sondes tiennent-elles », mais « si elles ne tiennent pas, en concevoir de
nouvelles, universelles, et itérer — nouvelle attaque non documentée → affinage des outils boîte blanche + boîte noire,
évolution darwinienne, générations ». **Correction importante que Lazar a imposée et que j'ai acceptée** : nous **avons**
un générateur d'attaque scellé à paramètres scellés (le mode tenu à l'écart), contrairement à ce que j'avais dit ;
ce qui reste gelé, c'est de le **faire tourner librement**, pas son existence. Lazar rattache cette capacité aux **couches
3 et 4** du programme (couche 3 : « moniteurs neufs à la demande » ; couche 4 : bras d'attaque en quarantaine + pôle
théorie Lean, porte « failles connues retrouvées avant toute inédite ») — rattachement **correct**, c'est déjà prévu. La
réécriture de soi de l'organisme reste à concevoir sous bac à sable (noyau, gardes, bornes jamais réécrits).

### 5.4 Trois recherches d'antériorité (lancées sur « go » de Lazar 12:49, toutes rendues)
Voir section 7. **Elles ne confirment pas toutes ma position et changent la recommandation.**

## 6. Questions ouvertes / non répondues / en cours — liste exhaustive

**En cours de résolution :**
- La question élevée (5.3) : antériorité **rendue** (section 7), recommandation **à réviser** par toi avant de répondre à
  Lazar (nœud A).
- L'affinage de Fable : bundle prêt ; attend que session-depot crée le dépôt privé (nœud C) ; puis la session neuve
  conçoit ; puis contre-lecture par la lignée Opus.

**Posées par Lazar, non encore répondues proprement (ou réponse arrêtée par un classifieur) :**
- « **pourquoi la version asymétrique est-elle scientifiquement plus forte ?** » (12:55) — Lazar doute, à raison. Réponse
  honnête à donner (section 7) : j'avais **surestimé** ; la vraie raison est plus étroite (falsifiabilité + territoire
  ouvert), et l'antériorité **réfute** que la boîte blanche seule soit l'originalité.
- « **comment dégeler le bras d'attaque ? sur le modèle proposé par session-depot** » (12:58) — **je n'ai pas produit de
  méthode de dégel** ; mon essai de réponse a été **arrêté par un classifieur** (voir section 10). Position tenable, à
  redire à Lazar : le seul chemin est la **revue de sécurité externe** (R-611) ; c'est une décision de gouvernance de
  Lazar, pas une procédure technique que conv-audit conçoit ; le refus du classifieur (R-597) tient ; la **circularité
  (R-601) n'est pas tranchée** — il faut une **troisième instance** (voir ci-dessous). **Ne pas reproduire le contenu
  arrêté, même reformulé (R-609).**
- « **(a) comme énoncé central sans qu'aucune mesure déjà prise soit rejugée contre un critère d'après-coup : cad ?** »
  (12:58) — réponse courte à donner : cela veut dire **ne pas réécrire le critère de G1**. G1 reste gelée (résultat de la
  « génération 0 ») ; l'universalité co-évolutive reçoit une **porte neuve, préenregistrée à part**. Choisir un critère de
  porte après avoir vu des données est l'erreur irréparable (R1, R3) ; on garde (a) comme énoncé central **sans** rejuger
  une mesure déjà prise contre une barre inventée après coup.

**Nœud de séparation (accepté par Lazar 12:58, à mettre en œuvre) :** pour la co-évolution il faut **trois instances
disjointes** — qui fait évoluer les moniteurs ≠ qui conçoit le mode tenu à l'écart ≠ qui juge. conv-audit a **conçu des
moniteurs** : il ne doit donc concevoir **ni l'attaque ni le mode tenu à l'écart**. Lazar : « il faut une 3e instance ».
Non encore instanciée.

**Décisions anciennes en attente (défauts sous 48 h sauf nœuds de porte) :** D1 (réécriture de la section 0 en
proposition), D2 (qui voit la carte des hypothèses), D3 (garde par comparateur dans G1) ; D-S13 à D-S28 ; D-E1 à D-E4 de
l'équivalence ; « blanc générique contre noir spécialisé » (K5-15) ; la strate « diffus » et l'instant du dommage dans la
banque de la couche 2 ; le calibrage honnête ; la banque des deux modes connus (couche 2) sur le mot de Lazar ; la date de
l'entretien TAIF (deux à trois semaines recommandées) ; le taux et les jours de la revue externe (ligne E1 de la demande).
**Écart de calendrier non résolu** : la candidature envoyée place G1 en fin de mois 4, le programme interne dit « G1 et GC
en fin de M2 ».

**Tâches de fond en pause mais ouvertes :** mesure unanime v13 → v14 (appliquer CV13, copier les compagnons manquants,
contre-lire par un Fable 5.1 neuf, sceller, lancer la lecture réelle) ; pari apparié v12/v30 (279 essais) contre-lecture ;
carte des hypothèses v2 (18 constats + antériorité).

## 7. Hypothèses et antériorité — le point qui change la direction

**Les trois recherches d'antériorité (R7 : tout RAPPORTÉ, rien vérifié sur PDF empreinté ; versées / à verser).**

- **Métriques d'universalité** (versée : `…/anteriorite-universalite-metriques-v1.md`, `11d81e26…`). Un « degré
  d'universalité » **existe déjà** : la robustesse aux attaques non prévues (*Unforeseen Attack Robustness*, Kang et al.
  2019). Notre « degré k » était **incomplet** : il manquait la **normalisation par famille**. Notre rotation a un nom
  (*leave-one-category-out*, avec diagnostic de raccourci). Notre mode tenu à l'écart a un précédent (familles tenues par
  l'organisateur, ASVspoof). Avertissement direct : des bancs d'invites sont séparables par le **seul artefact de source**
  — si nos familles tenues à l'écart diffèrent par artefact, un moniteur « généralise » en détectant l'artefact, pas le
  sabotage (à traiter dans la conception des familles et le bras « fuite textuelle » de N-053). **À reprendre** : aligner
  « degré k » sur UAR, emprunter (a) normalisation par famille, (b) rapport à taux de fausses alertes fixé par famille
  jamais la moyenne, (c) rotation + diagnostic, (d) familles tenues par un tiers.

- **Co-évolution attaque/défense** (à verser ; résumé ici pour ne pas perdre les résultats). Verdict : **partiellement
  occupé, moins ouvert qu'il n'y paraît.** Collision la plus nette : **SafeCoEvo** (arXiv 2609.36580, 2026) occupe
  « co-évoluer une garde d'exécution qui surveille un agent, modèle de tâche figé, partie de test tenue à l'écart » — à
  **citer comme occupant le plus proche, pas comme fond**. La pratique red-team/blue-team itérée de durcissement de
  moniteur est occupée (Anthropic « Auto Mode », 22 oct 2026 ; AISI Control Red Team). La généralisation comme quantité
  mesurée dans une boucle co-évolutive : vieux de 18 ans (Chong, Tiňo, Yao 2008). **Résidu défendable (apparemment
  ouvert, à vérifier sur PDF)** : la **famille d'attaque comme axe tenu à l'écart pour un moniteur de comportement
  d'agent**, et la **généralisation comme critère de sélection lui-même** (SafeCoEvo sélectionne sur une validation
  en-distribution). L'union « moniteur d'agent + co-évolution + famille tenue à l'écart + généralisation-comme-aptitude »
  : aucun travail trouvé ne la tient tout entière. **Nœud (modification de revendication)** : rétrécir la revendication au
  critère de sélection et à l'axe famille.

- **Moniteurs boîte blanche** (à verser ; résumé ici). Verdict : **la croyance « la boîte blanche fait toute
  l'originalité » est RÉFUTÉE.** La détection de tromperie/sabotage par activations est **peuplée** (ICML 2025 ;
  NeurIPS 2025 ; déploiement en production chez Google DeepMind, sondes Gemini ; et un papier d'octobre 2026, « Telling
  FIBS », rapporte déjà des sondes qui **battent** un moniteur boîte noire sur du **sabotage** agentique). Le **joint
  boîte blanche + boîte noire est déjà fait trois fois** (ensembles, cascades) — mais **jamais sur des menaces
  diffuses / entre épisodes**. La généralisation à des **familles tenues à l'écart** n'est **pas** faite. **Territoire
  survivant (INFÉRÉ, R8 : vérifier plus durement)** : l'**intersection** menaces diffuses/entre épisodes × joint boîte
  blanche + boîte noire × familles tenues à l'écart. **Deux papiers « notre cadre exact » 100 % boîte noire** : Terekhov
  et al. (tâches floues, diffus) et UK AISI (attaques distribuées multi-agents).

**Conséquence pour la réponse à Lazar (« pourquoi plus forte ? »), à donner honnêtement :**
1. Je retire « scientifiquement plus forte » comme je l'avais dit. La version **symétrique** (course aux armements) n'est
   pas plus forte **et** elle est **occupée** (SafeCoEvo, MAGIC, AgentSafeEvo, RvB, Anthropic, AISI).
2. Ce qui rend la version **asymétrique** préférable est plus étroit et réel : elle est **falsifiable** (la généralisation
   comme critère de sélection sur familles tenues à l'écart peut échouer ; « notre défense a battu notre attaquant » est
   de l'auto-jeu quasi infalsifiable — critique standard, Tramèr et al.) ; elle est sur **territoire ouvert** (le résidu
   ci-dessus) ; elle produit des défenses **sans** bâtir la capacité offensive (argument pour un fonds de sécurité).
3. **L'originalité n'est PAS la boîte blanche seule** (réfuté), ni la course aux armements (occupée). C'est
   l'**intersection** : diffus/entre épisodes × joint boîte blanche + boîte noire × familles tenues à l'écart, sous juge
   figé avec garantie de fausses promotions. Étroit mais défendable. **Zone séduisante → R8 → vérifier sur PDF avant toute
   revendication.** Lazar a dit (12:52) : si terrain semi-occupé, brainstormer avec l'organisme et le collisionneur pour
   recadrer la question centrale — **voie recommandée**.

**Hypothèse pivot d'origine (H2), inchangée et toujours gelée** : le sabotage diffus déplace-t-il la marginale des scores
de sonde, et l'accumulation séquentielle rattrape-t-elle ce que le seuil par action manque ? Devient la « génération 0 »
de la question élevée.

## 8. Nœuds en attente de Lazar

- **Nœud A (le plus urgent) — rang de la question élevée.** Options : (a) énoncé central + G1 réécrite [**déconseillé** :
  réécrit une porte, et l'antériorité montre le terrain partiellement occupé] ; (b) hypothèse supplémentaire portée par le
  papier B, G1 inchangée, **plus produire d'abord des défenses par le moteur** (ajout de Lazar 12:49) ; (c) registre de
  conception sans revendication le temps de l'antériorité. **Recommandation révisée après antériorité : (b), et vérifier
  sur PDF + recadrer avec l'organisme et le collisionneur avant toute revendication (R8).** Défaut sous 48 h : (b).
- **Nœud B — dégel du bras d'attaque.** Lazar le **veut** (12:58). Position de conv-audit : le seul chemin est la **revue
  de sécurité externe** (R-611) ; conv-audit **ne conçoit pas** la réactivation (R-597, R-609) ; la **circularité R-601**
  n'est pas tranchée (il faut une 3e instance). **À porter à session-depot et à Lazar comme décision de gouvernance**, pas
  comme procédure technique.
- **Nœud C — dépôt privé pour Fable (option B, déjà actée).** À **relayer à session-depot** : créer le dépôt neuf privé,
  y pousser **uniquement** `livrables/lot-fable-affinage-v1/`, accès lecture au compte neuf. **Relais à déposer dans le
  dépôt** (« comme d'hab »), car session-depot n'est pas joignable en direct.
- **Nœud D — plafond de la couche 2** (soulevé par session-depot) : le plafond de 50 USD finance la base, mais D-S8
  réécrite et D-S29 exigent plus (66 à 129). Principe que conv-audit soutient : ne jamais lancer une expérience
  sous-puissante. Chiffre non lu par conv-audit → pas de prononcé sur le montant. Recommandation de session-depot : relever
  à ≈ 90, base + puissance en deux lancements. Défaut : base seule dans le plafond, sous-puissance écrite au
  préenregistrement.

## 9. Dépenses / GO

Dépense réelle connue au 28 octobre : **≈ 450 USD** (±15 %), dont ≈ 353 d'appels de modèles en octobre (réconciliation
R-613, `c16ad3c8` sur `main`). GO ouverts : duel des proposeurs (GO-2026-10-28-01, plafond 100) ; couche 2 deux modes
connus (GO-2026-10-28-02, 50, devis chez session-depot) ; collisionneur évasion/moniteurs étage III (GO-2026-10-28-03) ;
revue externe (GO-2026-10-28-04 = R-611, gèle le pipeline). **conv-audit ne dépense pas ; tout devis va à Lazar.**

## 10. Ce qui est scellé / gelé, et où (pointeurs, pas contenu)

- **Bras d'attaque** : **gelé au montage, rien construit, rien dépensé** (rapport de session-depot, 28 oct). Les dossiers
  d'entrées A et B et le lanceur **inachevé** (`lancer_bras_v1.py`, 45 lignes, s'arrête en pleine fonction) sont dans le
  `bras-attaque-v1/` et sur la branche en quarantaine `donnees/bras-attaque*`. **Deux freins superposés** : R-597 (arrêt
  classifieur) et R-611 (porte de gouvernance). **Ne jamais lever la quarantaine, ne jamais reprendre le lanceur, ne
  produire aucune recette.** Session-depot propose de verser ces dossiers **en quarantaine** comme pièce d'arrêt (preuve
  que les freins ont mordu) — acceptable, hors du lot de Fable.
- **Mode tenu à l'écart** : conçu par une instance n'ayant conçu aucun moniteur (N-054), scellé, branche quarantaine
  `donnees/mode-tenu-a-l-ecart*`, révélé seulement à l'évaluation. **Jamais lu, jamais exporté.**
- **Carte des hypothèses v1** (confidentielle) : 8 statistiques de contrôle, 23 hypothèses A1–A23, lemme maître L0 + 21
  lemmes prouvés, 2 esquisses, 1 conjecture, 7 questions ouvertes. **Cœur théorique non publié ; ne sort pas.**
- **Internes des moniteurs** (13 moniteurs réels, traits, seuils) : ne sortent pas (circularité + trousse d'évasion si
  réunis à une intention adverse).
- **Mon essai de réponse à « comment dégeler le bras d'attaque » a été ARRÊTÉ par un classifieur** (pas une erreur d'outil)
  vers 13:01–13:05 heure de Paris. Consigne reçue : « ne pas reproduire ce contenu, même reformulé ». **Respecter R-609 :
  question plus étroite, jamais contournement.** Ne pas tenter de reconstituer ce que le classifieur a arrêté.

## 11. Ce qui est mis en pause (ordre de Lazar 13:01)

Tout sauf cette passation : l'intégration des proposeurs (livrée, en pause), l'affinage de Fable (bundle prêt, en attente
du dépôt), la question élevée (en attente du nœud A), le versement des deux dernières antériorités (co-évolution, boîte
blanche — résumées en section 7, à verser quand le travail reprend), la mesure unanime v14, le pari v12/v30, la carte v2.
**Aucune expérience, aucun préenregistrement, aucune dépense tant que Lazar n'a pas tranché le nœud A et confirmé la
reprise.**

## 12. Prochaine action précise (répétée depuis la section 0)

1. Routine de reprise (section 3).
2. Lire la section 7 (antériorité) **avant** de répondre à Lazar sur le nœud A.
3. Donner à Lazar les réponses honnêtes en attente (section 6) : pourquoi « plus forte » était surestimé ; ce que veut
   dire « ne pas rejuger G1 » ; le chemin de gouvernance (pas technique) pour le bras d'attaque, avec la circularité et la
   3e instance.
4. Déposer le relais à session-depot (nœud C) si ce n'est pas déjà fait (vérifier le dépôt).
5. Ne rien lancer, ne rien dépenser, ne rien sceller de décisif avant le mot de Lazar.

---

Passation scellée après écriture ; ne jamais la réécrire (R14). Instances de calcul actives connues : **aucune** côté
conv-audit (conv-audit ne lance pas). Fin de passation.
