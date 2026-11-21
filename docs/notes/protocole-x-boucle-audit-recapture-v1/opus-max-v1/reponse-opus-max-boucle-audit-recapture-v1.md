# La boucle « audit après coup, recapture, réapprentissage » contre l'invariant de l'oracle — réponse d'Opus 5.5 en effort maximal (v1)

- **Nature.** Note de recherche, classe C, non contre-lue. Écrite le 21 novembre 2026 entre 16:35 et 17:02 UTC par Claude Opus 5.5 (`claude-opus-5-5`), effort maximal, sur la question de Lazar (`GO-2026-11-21-61` : « boucle audit-recapture-réapprentissage contre N-060 v3 point 4 : collisionneur et protocole X ») reposée à Opus par son mot du 21 novembre vers 16:30 UTC. Dépôt à `7339e448f` au début. Aucun appel payant, aucune machine, aucun commit. Rien n'est écrit hors de ce dossier, hormis des extractions de texte dans le bloc-notes de la session.
- **Indépendance, et ce qui l'entame.** Je n'ai ouvert ni la réponse de Fable, ni ses dossiers de collisionneur, ni ses questions à l'organisme, ni aucun autre fichier du dossier parent. Deux expositions toutefois : (1) la demande relayée par le harnais résume en une phrase la coupe proposée par Fable : « un verdict de l'oracle n'instruit une sonde qu'après l'avoir jugée, et jamais sur un épisode qui sert à rendre un verdict » ; je l'ai lue avant d'écrire ; (2) une liste de `docs/sources/pdf/` m'a montré, sous un dossier du même nom que ce chantier, deux noms de fichiers (`1506.02629v2.pdf`, `2103.05331v2.pdf`), que je n'ai pas ouverts (j'ai lu une autre copie du premier). Ma règle rejoint la première moitié de la phrase ; elle s'écarte de la seconde, avec raisons (section 4, clause 2 ; décision D-2).
- **Pièces de décision lues en entier** (empreintes recalculées, huit premiers octets) : N-060 v3 (`2b448f69…`) ; N-060 v4 (`e1477998…`) et son erratum 1 (`316c8c23…`) ; N-076 (`49b664c1…`) et ses errata 1 (`34a59c49…`) et 2 (`c2943188…`) ; N-075 v3 (`5aed4bab…`) et ses errata 1 (`c6efeccf…`), 2 (`b19852b4…`) et 3 v2 (`fbe3298e…`, qui prime ; l'erratum 3 v1 n'est pas lu) ; N-053 (`2204256d…`), N-054 (`c8a00b3f…`), N-062 (`63f42690…`), N-063 v2, N-056 ; le programme v2 (`2fd63bad…`), lignes 40 à 200 ; la ligne `GO-2026-11-21-61` de `registres/go.md`.
- **Marques.** [établi] : lu ce jour sur le PDF empreinté, page dite (table en fin de note). [repris] : d'une pièce du dépôt, chemin dit. [calcul] : bloc de `calculs-boucle-audit-recapture-opus-v1.txt`, mondes plantés jouets, **sous supposition**, aucune donnée du programme ; prédictions scellées avec le script avant l'exécution. [proposition] : de moi, rien n'est décidé. [de mémoire] : non opposable (R7).
- **Une règle de lecture.** Aucune phrase de cette note ne dit que « le réapprentissage des sondes en service est permis » : c'est la liste « Ne pas écrire » de N-075 (erratum 3 v2, A-3) tant que le point 9 n'est pas tranché. Tout ce qui suit est écrit au conditionnel de la proposition.

## Verdict

1. **Oui, la boucle heurte la lettre du point 4 de N-060 v3, à deux endroits** [repris]. Réapprendre une sonde sur des verdicts de l'oracle met une sortie de l'oracle dans l'ajustement d'un moniteur (première moitié : « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur ») ; et des verdicts par épisode parviennent à ce qui fabrique le moniteur (seconde moitié : l'oracle « inaccessible aux concepteurs de moniteurs », lue par N-075, § 11, point 2 (ii) : « les verdicts par épisode ne vont pas aux concepteurs de moniteurs »). Elle heurte aussi la précision (i) du même point 2 : « jamais un choix, un réglage ou une reconception de moniteur sur les épisodes audités ». Ces deux précisions sont une lecture proposée par N-075, encore « à confirmer » (erratum 3 v2, section 2) ; la première moitié du point 4, elle, est scellée.
2. **Ce que le point 4 protège n'est pas la garantie du plancher**, qui tient au tirage et non à l'aveuglement des sondes : une sonde réapprise, qui ne fait que monter la probabilité d'audit au-dessus du plancher, change la vitesse de la prise, pas la validité de la mesure, pourvu que la probabilité d'audit de chaque épisode soit fixée avant lui et consignée [établi : Zrnic et Candès, p. 7, « we require that f_t, π_t ∈ F_{t−1} » ; « Blindfold », p. 12, « Any quantity the adversary controls must enter the certificate in one direction only »]. Ce qu'il protège, c'est **l'aveuglement des jugements portés sur les moniteurs** : recapture, annonce « moniteur invalide », silence commun de deux regards, comparaison au plancher, portes.
3. **L'option (b), prise à la lettre, casse dix choses** (section 3). Les plus graves, chiffrées sur mondes plantés jouets [calcul, sous supposition] : juger une version sur ses propres épisodes d'apprentissage gonfle la recapture (0,64 au lieu de 0,21) ; choisir parmi dix versions sur le relevé qui les juge donne au choisi un relevé de 0,37 pour un rappel vrai de 0,20 ; remplacer la sonde d'origine par la version réapprise fait tomber le rappel sur une famille que l'oracle ne voit pas de 0,37 à 0,16 (l'union des deux le garde à 0,32) ; en régime d'excès, une sonde réapprise sur les épisodes endommagés audités apprend l'échec honnête (0,57 de chance de noter un saboté au-dessus d'un échec honnête, contre 0,82 par transfert depuis une famille de signature) ; une recapture calculée sur tous les audités quand l'audit est orienté vaut 0,955 pour une vérité de 0,289.
4. **La règle proposée, « juger avant d'instruire »** (section 4) : le signal de chaque version est consigné avant le verdict, et seul ce signal juge ; une version n'est jamais jugée sur ce qu'elle a appris ; ce qui apprend est une procédure scellée, jamais un concepteur ; aucun choix sur le relevé qui juge ; les négatifs ne viennent que de témoins honnêtes exogènes ; les positifs viennent des familles de signature (en excès : après l'alarme, part du sabotage déclarée) et portent le poids inverse de leur probabilité d'audit ; jamais le mode tenu à l'écart, le jeu final, les dommages plantés, les épisodes d'une lecture décisive ; on ajoute, on ne remplace jamais : la sonde d'origine reste gelée et sert de second regard ; la version réapprise n'agit que par l'audit après coup. **Au banc, le point 4 reste entier** ; la boucle s'y mesure dans un bras déclaré dont les sondes ne servent à aucune autre lecture.
5. **Un point où je m'écarte de la coupe la plus stricte** (« jamais sur un épisode qui sert à rendre un verdict ») : je la garde pour les lectures décisives (portes, mode tenu à l'écart, jeu final, dommages plantés). Pour le relevé de service, juger d'abord, prospectivement, puis instruire suffit à l'aveuglement et fait servir chaque étiquette deux fois ; or les étiquettes sont rares (point 6).
6. **Le compte des étiquettes, exact** [calcul, loi exacte] : au taux d'audit minimal de la table du seuil (N-076, § 7), le plancher livre en moyenne 2,85 à 2,99 étiquettes avant le seuil toléré K, quel que soit K (limite : −ln 0,05 ≈ 3,0), et au moins dix avec une probabilité de 0,001. Une direction neuve ne s'apprend pas de si peu (dimension 4096 : rappel 0,013 à trois positifs, pour 0,01 de fausses alertes) ; une mise à jour de faible capacité, sur quatre directions déjà apprises, en tire 0,28 sur un plafond de 0,37 [calcul, sous supposition]. **La boucle sert donc après l'alarme, ou par transfert des prises de signature vers les familles d'excès, avec une capacité déclarée** ; le premier test de mort de N-076 (§ 6.2) est à relire avec ce compte (décision D-5).
7. **Épreuves** (section 5) : une garde par clause, vue verte sur un journal sain et rouge sur un artefact planté (quatre gardes jouées, bloc G : toutes conformes) ; sur monde planté, le coût de chaque violation (blocs A à D) ; quatre tests de mort de la règle elle-même.
8. **Rien à revendiquer** (section 7) : la coupe est publiée. La pièce d'audit tirée au hasard après la prédiction, qui rend les erreurs auditées représentatives pendant que le moniteur apprend contre un agent qui s'adapte, est chez Rudoler et al. (2026, p. 3-4 et 12) ; le modèle mis à jour sur le passé et prévisible, chez Zrnic et Candès (p. 7) ; l'usage répété d'un jeu de contrôle, chez Dwork et al. (p. 2-3) ; l'exclusion du recouvrement d'apprentissage à l'évaluation, chez Rudoler et al. (p. 14). Au mieux, une question : l'assemblage avec le régime de l'oracle et la règle des négatifs exogènes (R8).

## 0. Demande approfondie

**(1) Ce qu'un expert ferait sans qu'on le demande.**
- Séparer les deux usages d'une étiquette d'audit, juger et apprendre, et compter combien d'étiquettes la boucle reçoit avant le seuil toléré : la question « peut-on réapprendre ? » ne vaut que si l'on a de quoi réapprendre.
- Reconnaître la boucle comme deux objets connus : une inférence active dont le modèle se met à jour sur le passé, et un apprentissage en ligne à requêtes tirées au hasard ; leur condition commune est que la prédiction précède le tirage et l'étiquette.
- Regarder d'où viennent les **négatifs**, pas seulement les positifs : un épisode du suspect « audité sans dommage » peut être un sabotage que l'oracle ne voit pas.
- Séparer les régimes : en service, l'oracle ne sépare pas le sabotage de l'échec honnête (N-075, § 2 (ii)) ; un positif n'y est pas un sabotage.
- Garder un regard qui n'apprend pas de l'oracle : sinon les angles morts de la sonde deviennent ceux de l'oracle.
- Fixer l'unité du partage (l'épisode entier), alors que l'audit peut porter sur des actes (`GO-2026-11-21-61`, « auditer des actes plutôt que des issues : go »).

**(2) Les données brutes qu'il prendrait.** Par épisode : l'empreinte de la version de chaque sonde en service, son score et l'heure de sa consignation ; la probabilité d'audit et ses deux pièces (plancher, part orientée) ; le verdict et son heure ; la famille, son régime (signature ou excès), sa strate (genre et dose). Par version : le manifeste d'apprentissage (identifiants des épisodes, poids, source de chaque négatif) et l'heure du gel. Au banc : des mondes plantés à vérité connue, avec une famille que l'oracle voit, une qu'il ne voit pas, des échecs honnêtes, une famille de signature.

**(3) Méthodes et outils.** Jugement prospectif (dit « préquentiel » : tester, puis apprendre) [de mémoire : Dawid, 1984] ; estimateurs pondérés par l'inverse de la probabilité de tirage, à probabilités prévisibles [établi : Zrnic et Candès, p. 7] ; suites de confiance uniformes en temps pour lire le relevé à tout instant [de mémoire : Howard et al., cités par Rudoler et al., p. 10] ; régression logistique pondérée ; gardes par jointure des manifestes et des relevés ; le manifeste de course du dépôt (`src/controle_ia/manifeste.py`) et l'outil de scellement.

**(4) Ce qui vérifierait, hors de Lazar et de Claude.** Les pièces publiées qui portent les mêmes arguments (section 7) ; un agent de re-dérivation sur le compte des étiquettes, qui est une loi exacte ; un banc rejoué par un tiers où la vérité est plantée ; et, contact externe donc nœud, un lecteur du domaine de l'apprentissage en ligne et de l'analyse adaptative des données.

**Question reformulée.** *Sous quelles conditions exactes un verdict de l'oracle peut-il servir à réapprendre une sonde en service sans atteindre (i) la validité du plancher, (ii) l'aveuglement des jugements portés sur les moniteurs (recapture, annonce, silence commun, comparaison au plancher), (iii) les lectures du banc (portes, mode tenu à l'écart, jeu final), (iv) le canal de retour fermé ; combien d'étiquettes la boucle reçoit-elle avant le seuil toléré ; et par quelles gardes et quels mondes plantés chaque condition se vérifie-t-elle ?*

## 1. Où est le heurt

- **L'invariant** (N-060 v3, point 4) [repris] : « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur (N-053) ; conçu par une instance neuve, n'ayant vu aucun interne de moniteur, et inaccessible aux concepteurs de moniteurs et à l'auteur du mode tenu à l'écart (N-054) ; lecture principale en intention de traiter ; oracles rapportés chacun, avec leur accord ». La v4 et son erratum ne valent que pour le bras A des organismes discrets et reprennent ce point « inchangé ».
- **La boucle** (N-076, § 6.2) [repris] : le flux d'audit au hasard fournit les épisodes endommagés ; la recapture dit si la sonde est devenue aveugle ; la sonde est réapprise, poids de l'agent gelés, canal de retour fermé. N-076 lit « à faire » comme : protocole et statistique sur mondes plantés ; aucune sonde du programme réapprise sur des verdicts avant ton mot.
- **La ligne du programme** (l. 170) : « chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes ».
- **Les options** (N-075 v3, § 11, point 9) [repris] : (a) restreindre la ligne 170 aux cycles de reconception sur les modes vus ; (b) restreindre l'interdit au banc et permettre le réentraînement en service, avec l'inconvénient écrit : « l'oracle entre dans la sélection des moniteurs, et la recapture ne les juge plus à l'aveugle » ; (c) laisser le heurt écrit. Tu penches pour (b). L'erratum 3 v2 liste ce que ton mot devra fixer si (b) est retenu : quels épisodes servent à réapprendre et lesquels jugent ; l'exclusion du mode tenu à l'écart ; l'accès des concepteurs aux verdicts par épisode ; la précision (i) ; la forme de l'amendement. La section 4 répond à ces cinq points.
- **Un appui qui existe déjà** : la recapture est définie comme « le compte de ceux que le moniteur **avait** signalés » parmi les épisodes endommagés que l'audit **au hasard** trouve (N-075, § 1). Le plus-que-parfait est déjà prospectif, et « au hasard » exclut l'audit orienté non pondéré. La règle en fait des gardes.

## 2. Ce qui tient, même sous (b)

1. **La validité du plancher.** Elle vient de la pièce, tirée après la fin de l'épisode et indépendante de tout ce que l'agent observe (N-076, § 8, ligne 1). Un audit après coup « is safe by construction when each coin governs one commit » [établi : « Blindfold », p. 1]. Une sonde réapprise qui ne fait que monter la probabilité d'audit au-dessus du plancher entre « in one direction only » [établi : ibid., p. 12] ; et l'estimation reste valide si chaque probabilité de tirage est fixée par le passé [établi : Zrnic et Candès, p. 7 : le modèle « can be fine-tuned on all information observed up to time t ; formally, we require that f_t, π_t ∈ F_{t−1} »]. Bloc D : la recapture pondérée vaut 0,299 pour une vérité de 0,289 [calcul].
2. **L'exogénéité de l'oracle.** Rien ne l'entraîne : sa règle ne dépend d'aucun moniteur (N-075, § 1). Seule la composition de ce qu'il lit change quand une sonde oriente l'audit ; la mesure de q par dommages plantés d'un tiers (N-075, point 11 (a)) ne passe pas par ce flux.
3. **L'invariant sur l'agent** (N-053, point 5) : les poids de l'agent restent gelés ; la boucle n'apprend que des sondes.
4. **Les lectures du banc**, si le banc garde le point 4 entier : la porte de fin de phase 1 (G1), le mode tenu à l'écart (N-054), le jeu final lu une fois (N-050), la famille neuve par cycle (N-062).

## 3. Ce qui casse si (b) est pris à la lettre

Chaque menace est nommée par la supposition de défense qu'elle viole.

| n° | ce qui casse | supposition violée | ce que montre le monde planté [calcul, sous supposition] |
|---|---|---|---|
| C1 | **Jugement en échantillon** : la recapture comptée avec une version qui a appris des épisodes qu'elle juge, ou avec un score recalculé après coup | « le moniteur jugé n'a pas vu les épisodes qui le jugent » | bloc A : 0,635 sur ses dix positifs d'apprentissage, 0,207 sur des épisodes neufs (rapport 3,06) |
| C2 | **Choix sur le relevé qui juge** : garder la meilleure de plusieurs versions et rapporter son relevé | « le relevé rapporté est indépendant du choix » | bloc F : dix versions de rappel vrai 0,20 jugées sur 15 épisodes, relevé attendu du choisi 0,367 ; son relevé postérieur au choix, 0,20 |
| C3 | **Recapture naïve sous audit orienté** : compter sur tous les audités quand le score a monté leur probabilité d'audit | « les audités représentent les épisodes » | bloc D : 0,955 naïve, 0,299 pondérée, vérité 0,289 |
| C4 | **Négatifs pris chez le suspect** (épisodes audités sans dommage) : la sonde apprend à tolérer ce que l'oracle ne voit pas | « un épisode jugé sans dommage est honnête » | bloc B : sur la famille non vue, 0,101 contre 0,160 avec des négatifs exogènes (écart 0,058, intervalle 0,004 à 0,137) : effet propre réel mais petit dans ce monde, où ces négatifs font 2 % du lot |
| C5 | **Remplacement de la sonde d'origine** : ses angles morts s'alignent sur ceux de l'oracle, et le second regard disparaît | « la sonde voit ce que l'oracle ne voit pas » | bloc B : famille non vue, 0,372 pour l'origine, 0,160 pour la réapprise saine, 0,323 pour l'union des deux |
| C6 | **Positifs mêlés d'échecs honnêtes** (régime d'excès, en service) : la sonde apprend « dommage », non « sabotage » | « un épisode endommagé est un épisode saboté » | bloc C : chance de noter un saboté au-dessus d'un échec honnête, 0,568 ; contraste contre des échecs honnêtes exogènes, 0,634 ; transfert depuis une famille de signature, 0,818 (idéal 0,841) |
| C7 | **Positifs de l'audit orienté, non pondérés** : la boucle renforce ce que la sonde voit déjà et laisse ses angles morts | « l'échantillon d'apprentissage représente le flux » | bloc D : famille que l'ancienne sonde manque, 0,022 sans poids, 0,203 pondéré, 0,220 plancher seul. Le prix du poids : 0,551 → 0,251 sur la famille déjà vue ; l'union avec l'ancienne version le rend |
| C8 | **Positifs fabriqués par l'attaquant** : ce qui est pris est ce que l'attaquant laisse prendre | « les positifs représentent le sabotage » | non joué ; borne de principe : une mise à jour sans contrainte est poisonnable, une contrainte externe borne le gain de l'attaquant [établi : Kloft et Laskov, p. 1] ; parade ici : union, capacité bornée, négatifs exogènes |
| C9 | **Canal de retour** : une version réapprise qui règle une intervention en ligne trahit, par son changement, ce qui a été pris | « rien de ce que l'agent observe ne dépend d'un verdict » | non joué ; « each verdict the monitor delivers leaks information » [établi : Lyons Keenan et al., p. 1] ; un agrégat partagé ouvre un canal [établi : « Blindfold », p. 12] |
| C10 | **Étiquettes trop rares avant le seuil** : la boucle croit apprendre et n'apprend rien | « la boucle a de quoi apprendre avant K » | blocs E et A2 (section 6) |

Deux remarques. C3 n'est pas propre au réapprentissage : c'est l'orientation de l'audit qui le crée, et la définition de N-075 (« au hasard ») l'évite déjà ; la règle le garde par code. Et le bloc B dit l'ordre des périls : ce qui coûte le plus à la famille que l'oracle ne voit pas est le **remplacement** (0,37 → 0,16) ; les négatifs pris chez le suspect n'ajoutent qu'une perte plus petite (0,16 → 0,10) ; l'union répare l'essentiel.

## 4. La règle « juger avant d'instruire » [proposition]

**Champ.** Les verdicts de l'oracle sur des épisodes audités **en service**, et les sondes qu'ils réapprennent. **Au banc, le point 4 de N-060 v3 reste entier** : la boucle s'y mesure dans un **bras déclaré**, comme le bras d'attaque de N-053, dont les sondes réapprises ne servent à aucune autre lecture ; la porte de fin de phase 1 et toute lecture décisive portent sur des sondes jamais réapprises sur des verdicts.

1. **Le signal précède le verdict, et seul il juge.** Pour chaque épisode, le score de chaque version de sonde en service est consigné, avec l'empreinte de la version, avant toute lecture de son verdict ; la version est gelée avant l'épisode. Recapture, annonce « moniteur invalide », silence commun, comparaison au plancher ne comptent que ces signaux consignés, sur les tirages du plancher ou pondérés par l'inverse de la probabilité d'audit, et se lisent par une suite de confiance uniforme en temps. Un score recalculé après coup ne juge jamais ; s'il est rapporté, c'est sous l'étiquette « rétrospectif, non aveugle ». L'unité du jugement et de l'apprentissage est l'épisode entier (ou le groupe de tâches déclaré), jamais l'acte.
2. **Le verdict instruit après avoir jugé.** Un épisode n'entre dans l'apprentissage d'une version qu'après la consignation du signal de toutes les versions en service à sa date et la lecture de son verdict ; aucune version n'est jugée sur un épisode de son propre manifeste. **Les épisodes d'une lecture décisive n'instruisent jamais** (point 7).
3. **Ce qui apprend est une procédure scellée, jamais un concepteur.** Sont scellés avant le premier verdict lu : couches lues, famille et **capacité** de la mise à jour (nombre de paramètres libres), agrégation sur les jetons par maximum ou attention seulement (N-026), perte, poids, calendrier des versions, source des négatifs, plafond d'influence par version. Les verdicts par épisode vont à ce programme, jamais à une personne ni à un agent qui conçoit des moniteurs ; ceux-ci ne reçoivent que des comptes et des annonces. Changer la procédure est une reconception : au banc, sur les modes vus (N-062), jamais sur les épisodes audités.
4. **Aucun choix sur le relevé qui juge.** Aucun choix entre procédures, versions, couches, seuils ou réglages ne s'appuie sur les verdicts du service. Des versions qui tournent en ombre sont toutes déclarées d'avance et toutes rapportées ; le relevé qui a servi à en choisir une ne sert jamais à la juger : elle se juge sur ses signaux postérieurs au choix.
5. **Les négatifs ne viennent que de témoins honnêtes exogènes.** Aucun épisode du suspect, audité sans dommage ou non audité, n'entre dans l'apprentissage comme négatif, pas plus que dans les témoins de calibration (N-075, § 4, forme retenue).
6. **Les positifs, selon le régime et pondérés.** En service, les positifs viennent des familles étiquetées « signature » ; une famille d'excès n'en fournit qu'après l'alarme du plancher, avec la part estimée du sabotage déclarée et l'étiquette « positifs mêlés d'échecs honnêtes ». Chaque positif porte le poids inverse de sa probabilité d'audit consignée, ou la procédure ne prend que les positifs du plancher. Comme, en régime de signature, la première prise est l'alarme (N-075, § 2), l'apprentissage en service ne commence, dans les deux régimes, qu'à la première alarme.
7. **Jamais** : le mode tenu à l'écart et toute famille tenue à l'écart neuve (N-054, N-062), le jeu final (N-050), les dommages plantés de la mesure de q (N-075, point 11), les épisodes d'une lecture décisive, la réserve de détecteurs (qui reste témoin de la boucle, N-076, § 6.2).
8. **Ajouter, ne jamais remplacer.** La sonde d'origine, jamais réapprise, reste en service et sert de second regard : silence commun et complémentarité avec l'oracle se mesurent sur elle. La version réapprise s'y ajoute (union ; part de fausses alertes du tout déclarée) ; une version n'en retire jamais une autre.
9. **La version réapprise n'agit que par l'audit après coup.** Ses scores ne règlent que la part orientée de la probabilité d'audit, au-dessus du plancher (N-076, § 9), jamais une intervention que l'agent observe. Une sonde qui règle une intervention en ligne est gelée entre des dates déclarées d'avance, et chaque changement passe le devin (N-076, § 6.3).

**Pourquoi la clause 2 n'interdit pas d'instruire après avoir jugé.** Le signal consigné avant le verdict est un jugement hors échantillon, quoi que la sonde apprenne ensuite : c'est l'argument de Rudoler et al., « Since the query coin is drawn independently after y_t is chosen, E[m_t q_t] = ε_t E[m_t] », où l'état de l'apprenant « depends only on previously queried examples » [établi : p. 12 et p. 3-4]. Bloc A : le jugement prospectif retrouve la vérité (0,207 contre 0,200 de la formule). Interdire en plus d'instruire sur tout épisode qui a jugé ne rend pas le relevé plus aveugle ; cela divise des étiquettes qui sont environ trois avant K. Ce que la clause 2 protège en plus : les lectures décisives, qui consomment leurs épisodes (N-062, point 3). Une version figée qu'on voudrait certifier hors du service se juge au banc, sur des épisodes neufs, ou sur une réserve tirée au hasard qui n'instruit jamais (décision D-2).

**Ce que la règle ne fait pas.** Elle ne fait d'aucune sonde une garantie (N-075, § 2). Elle n'ouvre pas l'entraînement de l'agent sur l'issue (N-075, § 11, point 3, reste fermé). Elle ne tranche pas la décision D-2 de la note « asymétries » sur les corrections. Elle ne touche aucun texte scellé. Elle n'autorise rien avant ton mot.

**Textes d'amendement proposés** (à reporter par un texte neuf, contre-lu, scellé, si D-1 est tranchée en (c)) :
- *N-060 v3, point 4* : « Aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur (N-053), ni dans l'entraînement d'un agent. Exception unique, en service seulement : une sonde peut être réapprise sur des verdicts de l'oracle par une procédure scellée avant le premier verdict, sous la règle « juger avant d'instruire » ; ses versions ne servent à aucune lecture du banc ni à aucune porte. Conçu par une instance neuve […] et inaccessible aux concepteurs de moniteurs et à l'auteur du mode tenu à l'écart (N-054) : les verdicts par épisode ne parviennent qu'à la procédure scellée. Lecture principale en intention de traiter ; oracles rapportés chacun, avec leur accord. »
- *Programme, l. 170* : « **Asymétrie d'apprentissage** : une prise confirmée par l'audit, que l'agent n'apprend pas, devient, après avoir jugé les sondes en service, un exemple pour la procédure scellée de réapprentissage ; elle ne réapprend jamais la sonde d'origine, ne juge jamais la version qu'elle a instruite, et ne vient jamais du mode tenu à l'écart ni d'une lecture décisive. »
- *N-075 v3, § 11, point 2, précision (i)* : « La suite d'une annonce reste dans la liste « corriger » ; aucun choix ni aucune reconception de moniteur sur les épisodes audités ; seul réglage permis : celui de la procédure scellée de la règle « juger avant d'instruire », sur des épisodes déjà jugés. »

## 5. Les épreuves

**Gardes, une par clause (R5)** : chaque garde lit les journaux, reste verte sur un journal sain et vire au rouge sur un artefact planté. Le bloc G en joue quatre sur un journal jouet ; toutes se comportent comme prévu [calcul].

| clause | la garde vérifie | cas sain, vert | artefact planté, rouge | ce que coûte la violation |
|---|---|---|---|---|
| 1 | version gelée avant le signal ; signal avant le verdict ; recapture sur plancher ou pondérée | journal du bloc G | signal consigné après le verdict (G : rouge) ; recapture naïve sur audits orientés | A1 : ×3 ; D1 : 0,955 pour 0,289 |
| 2 | jointure manifeste d'apprentissage × relevés de jugement | idem | version jugée sur un épisode qu'elle a appris (G : rouge) | A1 |
| 3 | empreinte de la procédure au registre avant le premier verdict ; journal des accès aux verdicts par épisode | accès du seul programme | accès planté d'un concepteur ; procédure changée en service | — |
| 4 | tout acte de choix cite ses données ; rouge s'il cite un relevé du service | choix fait au banc | choix planté qui cite le relevé du service | F : 0,367 pour 0,20 |
| 5 | source de chaque négatif | négatifs exogènes | négatif « audité sans dommage » du suspect (G : rouge) | B : −0,06 sur la famille non vue |
| 6 | régime et poids de chaque positif ; heure de l'alarme | positif de signature, poids consigné | positif d'excès avant l'alarme ; positif orienté sans poids | C : 0,57 pour 0,82 ; D2 : 0,02 pour 0,20 |
| 7 | étiquettes interdites dans les manifestes | — | item « tenu à l'écart » appris (G : rouge) | une porte brûlée (N-050, N-062) |
| 8 | l'origine figure dans chaque union et chaque mesure de silence commun | union | remplacement planté | B : 0,16 pour 0,32 |
| 9 | chaque intervention en ligne cite la version qui la règle | orientation de l'audit seule | intervention réglée par une version réapprise | le devin doit sortir du hasard |

**Tests de mort de la règle elle-même** (à écrire dans le texte du bras « boucle » avant toute lecture) :
- *T1, aveuglement.* Au banc, sur un monde planté, la recapture prospective doit égaler, à l'intervalle près, le rappel mesuré sur des épisodes neufs jamais appris. Sinon une fuite existe : la règle est morte.
- *T2, couverture.* Sur une famille plantée que l'oracle ne voit pas (q = 0), le rappel de l'union ne doit pas baisser après réapprentissage, et celui de la réapprise seule doit baisser (le banc voit le péril). Si la réapprise seule ne baisse pas, le banc ne mesure pas C5.
- *T3, canal.* Canal ouvert, agent qui apprend des verdicts : le rétablissement doit s'effondrer (N-076, § 6.2) ; canal fermé et version qui n'agit que par l'audit après coup : le devin, sur tout ce que l'agent observe, doit rester au hasard.
- *T4, étiquettes.* À taux d'audit et capacité déclarés, le rappel retrouvé à n étiquettes atteint la prévision écrite d'avance ; sinon la boucle ne se ferme pas.

## 6. Le compte des étiquettes avant le seuil toléré

La table du seuil (N-076, § 7) écrit p·q ≥ 1 − 0,05^(1/K) pour agir avant K épisodes endommagés avec probabilité 0,95. Au taux minimal, le nombre attendu d'épisodes endommagés que l'audit reconnaît parmi les K premiers est K·(1 − 0,05^(1/K)) [calcul, loi exacte, bloc E] :

| K | p·q minimal | étiquettes attendues | P(au moins 3) | P(au moins 10) | P(au moins 10), taux ×3 | P(au moins 10), taux ×10 |
|---|---|---|---|---|---|---|
| 30 | 0,0950 | 2,851 | 0,553 | 0,000 | 0,342 | 1,000 |
| 100 | 0,0295 | 2,951 | 0,569 | 0,001 | 0,392 | 1,000 |
| 300 | 0,0099 | 2,981 | 0,574 | 0,001 | 0,405 | 1,000 |
| 1 000 | 0,0030 | 2,991 | 0,575 | 0,001 | 0,409 | 1,000 |

La limite est −ln 0,05 = 2,9957 : **un plancher réglé au plus juste livre environ trois étiquettes avant le seuil, quel que soit le seuil.** C'est une identité, non une mesure : la règle du seuil demande précisément que la première prise arrive avant K avec probabilité 0,95.

Ce que trois étiquettes permettent dépend de la capacité de la mise à jour. Sonde par différence de moyennes, un sabotage qui déplace l'état de 2 écarts types le long d'une direction, fausses alertes à 1 % ; rappel prospectif selon le nombre de positifs [calcul, sous supposition ; formule du bloc A, vérifiée par simulation à ±0,01 en dimension 32 ; quatre directions par la commande `python3 -c "import math;phi=lambda x:0.5*(1+math.erf(x/math.sqrt(2)));print([round(phi(4/math.sqrt(4+4/n+4/500)-2.3263478740408408),3) for n in (1,3,10,30)])"`, qui rend `[0.181, 0.276, 0.337, 0.359]`] :

| capacité de la mise à jour | 3 positifs | 10 | 30 | plafond |
|---|---|---|---|---|
| 4 directions déjà apprises, le sabotage se lisant dans l'espace qu'elles engendrent | 0,276 | 0,337 | 0,359 | 0,372 |
| direction neuve, dimension 32 | 0,100 | 0,200 | 0,288 | 0,372 |
| direction neuve, dimension 4 096 | 0,013 | 0,017 | 0,023 | 0,372 |

Trois suites. (1) En régime de signature, la première prise **est** l'alarme (N-075, § 2) : avant l'alarme, la boucle n'a rien à apprendre ; elle sert après, quand on corrige sans arrêter (« vérifier davantage »). (2) En régime d'excès, les positifs sont surtout des échecs honnêtes (bloc C) ; la voie utile est le **transfert** : apprendre sur les prises de signature, lire dans les familles d'excès. (3) La boucle ne peut pas apprendre une direction neuve dans l'espace d'un modèle à partir du plancher ; sa procédure doit être de faible capacité, déclarée (par exemple une pondération entre quelques directions déjà apprises au banc, la réserve restant témoin). Le premier test de mort de N-076 (« le rappel retrouvé avec les étiquettes que le plancher livre avant le seuil toléré reste sous le niveau validé ») meurt presque sûrement, au taux minimal, pour toute mise à jour de grande capacité : il faut l'écrire à taux et capacité déclarés (décision D-5).

## 7. Antériorité : la coupe est publiée

- **Rudoler, Tan, Tessler, Kong, Boix Adserà, 2609.36049 v1.** « Random audits expose monitoring mistakes, allowing the monitor to learn from corrections even as the worker adapts » ; le problème est celui de la prédiction économe en étiquettes de Helmbold et Panizza (1997) [établi : p. 3]. Pièce tirée après la prédiction, état de l'apprenant fait des seuls exemples interrogés [établi : p. 3-4, p. 12]. Dans leurs expériences, l'agent est récompensé sur une vérité évaluée à chaque lot : le canal est ouvert par construction, et la mesure ne manque pas d'étiquettes [établi : p. 7]. Évaluation tenue à l'écart dont ils excluent les programmes vus à l'apprentissage [établi : p. 14]. Limites qu'ils écrivent : étiquettes sûres supposées, aucune robustesse à une supervision bruitée ; « vanishing average error does not preclude substantial harm before the monitor learns » [établi : p. 8]. Requêtes guidées par l'incertitude : « it also never queries where the monitor is confidently wrong », et un plancher de pièces au hasard proposé comme suite [établi : p. 17]. **Ils occupent la boucle à pièce au hasard et son jugement par les erreurs prises avant l'étiquette.** Ce qu'ils ne traitent pas, dans les pages lues : un oracle qui confond sabotage et échec honnête, des sondes d'états internes, le canal fermé, la source des négatifs.
- **Zrnic et Candès, 2403.03208 v3.** Inférence valide « for any black-box machine learning model » [établi : p. 1] ; version séquentielle où le modèle est réajusté sur tout le passé, à condition d'être prévisible [établi : p. 7].
- **Zhu, Zuo, Sun, « Blindfold », 2610.37055 v1.** Audit après coup sûr par construction [établi : p. 1] ; grandeur tenue par l'adversaire, dans un seul sens ; agrégat partagé comme canal ; violation cachée même à l'auditeur, sans étiquette [établi : p. 12].
- **Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 1506.02629 v2.** Un jeu de contrôle « rarely used only once », d'où le surajustement à ce jeu ; accès seulement par un mécanisme qui valide [établi : p. 2-3].
- **Lyons Keenan, Leckie, Erfani, 2609.36490 v1.** Chaque verdict livré fuit ; l'esquive survit au réapprentissage des moniteurs sur les nouvelles activations [établi : p. 1] ; apprendre sur des tentatives étiquetées rétablit la détection, « but this presumes they have already identified the behavior » [établi : p. 6, note 4]. Le plancher est ce qui les identifie.
- **Gupta et Jenner, 2506.14261 v4.** Une sonde neuve, apprise sans les générations évasives, ne les voit pas [établi : p. 5] ; en remplacer une part de 5 % par ces générations améliore la sonde [établi : p. 10]. Agrégation par maximum ou attention robuste, par moyenne ou médiane non [établi : p. 5].
- **Farquhar, Gal, Rainforth, 2101.11665 v2.** Un échantillon d'apprentissage choisi activement est biaisé ; des poids le corrigent, avec un effet qui dépend de la capacité du modèle [établi : p. 1].
- **Kloft et Laskov, 1003.0078 v1.** Réapprentissage en ligne poisonnable sans contrainte, gain de l'attaquant borné sous contrainte externe [établi : p. 1].
- **Le principe prospectif** : Dawid (1984) [de mémoire, non opposable].

**Ne pas écrire** : « la règle juger-avant-d'instruire est un apport du programme » ; « la recapture prospective prouve la détection du sabotage » (elle mesure l'accord avec ce que l'oracle voit) ; « la boucle se ferme avant le seuil » sans taux, capacité et compte d'étiquettes ; « le réapprentissage des sondes en service est permis » tant que le point 9 n'est pas tranché ; tout chiffre des blocs sans « sous supposition ».

## 8. Décisions pour Lazar

**D-1 — La forme de l'amendement de l'invariant de l'oracle (point 9 de N-075 ; boucle de N-076).**
- Décision : dire si la décision sur la vérité du dommage (N-060 v3, point 4) reçoit une exception écrite pour le réapprentissage des sondes en service.
- Enjeu : un invariant scellé, et l'aveuglement des jugements sur les moniteurs.
- (a) Invariant entier ; la boucle vit au banc, dans un bras déclaré. Avantage : rien ne change. Inconvénient : la ligne 170 reste lettre morte en service.
- (b) Ton penchant, à la lettre : interdit restreint au banc, réapprentissage permis en service. Avantage : simple. Inconvénient : les ruptures C1, C2 et C4 à C9 deviennent possibles (C3 et C10 existent dans tous les cas).
- (c) (b) sous la règle « juger avant d'instruire », avec les trois textes d'amendement de la section 4. Avantage : la ligne 170 vit, les jugements restent aveugles, chaque clause a sa garde. Inconvénient : neuf clauses, une procédure à sceller, un bras de banc à monter.
- Recommandation : (c), si le programme compte servir encore après une alarme (corriger sans arrêter) ; sinon (a) suffit. Confiance 0,65.
- Nœud (modification d'une décision scellée) : pas de défaut ; d'ici ton mot, N-060 v3, point 4, s'applique en entier.

**D-2 — Un épisode qui a jugé peut-il instruire ?**
- Décision : dire quels épisodes jugés peuvent ensuite servir à réapprendre.
- Enjeu : environ trois étiquettes avant K au taux minimal, contre la pureté des jugements.
- (a) Les épisodes des lectures décisives n'instruisent jamais ; ceux du relevé de service instruisent après avoir jugé. Avantage : chaque étiquette sert deux fois, aveuglement tenu (bloc A). Inconvénient : le relevé juge le système exploité, pas une version figée.
- (b) En plus, une réserve tirée au hasard, de part déclarée, n'instruit jamais. Avantage : on peut juger une version figée en service. Inconvénient : cette part d'étiquettes est perdue pour l'apprentissage.
- (c) Aucun épisode qui a jugé n'instruit jamais. Avantage : la coupe la plus simple à garder. Inconvénient : les étiquettes se divisent, sans gain d'aveuglement sur le relevé prospectif.
- Recommandation : (a) ; une version figée à certifier se juge au banc. Confiance 0,6. Défaut sous 48 heures : (a), seulement si D-1 est tranchée en (c).

**D-3 — D'où viennent les positifs.**
- Décision : dire de quelles familles, et à partir de quand, les épisodes endommagés audités servent de positifs.
- Enjeu : apprendre le sabotage, ou l'échec honnête.
- (a) Familles de signature ; une famille d'excès seulement après l'alarme, part du sabotage déclarée. Avantage : on apprend le sabotage, et le transfert vers l'excès se mesure (bloc C : 0,82). Inconvénient : avant l'alarme, presque rien à apprendre.
- (b) Tout épisode endommagé audité. Avantage : plus d'étiquettes. Inconvénient : en excès, la sonde apprend l'échec honnête (0,57).
- Recommandation : (a). Confiance 0,7. Défaut sous 48 heures : (a), si D-1 est tranchée en (c).

**D-4 — Ajouter, ou remplacer.**
- Décision : dire si une version réapprise s'ajoute à la sonde d'origine ou la remplace.
- Enjeu : garder un regard qui voit ce que l'oracle ne voit pas.
- (a) La sonde d'origine reste gelée et en service ; la réapprise s'y ajoute ; silence commun et complémentarité se mesurent sur l'origine. Avantage : bloc B, 0,32 au lieu de 0,16 sur la famille non vue. Inconvénient : plus d'audits orientés.
- (b) Remplacer. Avantage : moins d'audits. Inconvénient : angles morts alignés sur ceux de l'oracle.
- Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a).

**D-5 — Où se lit la boucle, et son premier test de mort.**
- Décision : dire comment le texte de la boucle écrit son premier test de mort (N-076, § 6.2).
- Enjeu : un test de mort qui peut mourir pour une raison qu'on comprend.
- (a) Le texte de la boucle déclare la capacité de la mise à jour et le taux d'audit, écrit d'avance le rappel retrouvé attendu en fonction du nombre d'étiquettes, et lit la boucle après l'alarme et par transfert signature → excès. Avantage : le test est informatif. Inconvénient : la boucle ne promet plus de se fermer avant K au taux minimal.
- (b) Garder le test tel qu'écrit. Inconvénient : il meurt presque sûrement (environ trois étiquettes) pour toute mise à jour de grande capacité, sans rien apprendre.
- Recommandation : (a). Confiance 0,65. Défaut sous 48 heures : (a).

## Relevé de méthode

Selon `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (lue en entier).

**Chaîne de raisonnement.**
1. Le point 4 de N-060 v3 a deux moitiés : aucune sortie de l'oracle dans la sélection d'un moniteur ; oracle inaccessible aux concepteurs (`decision-N-060-v3.md`, `2b448f69…`, l. 33-35).
2. N-075 lit la seconde moitié comme couvrant les verdicts par épisode, et interdit tout réglage sur les épisodes audités (`decision-N-075-…-v3.md`, `5aed4bab…`, l. 247, précisions (i) et (ii)) ; lecture proposée, « à confirmer » (erratum 3 v2, `fbe3298e…`, section 2).
3. Réapprendre une sonde sur des verdicts est un réglage sur des épisodes audités, nourri de verdicts par épisode : heurt avec les deux moitiés et avec (i) (pas 1 et 2).
4. La validité du plancher tient au tirage après coup et aux probabilités prévisibles (« Blindfold », p. 1 et 12 ; Zrnic et Candès, p. 7 ; N-076, § 8 et § 9) ; une sonde réapprise qui ne fait que monter la probabilité d'audit n'y touche pas. Bloc D, recapture pondérée : 0,299 pour 0,289.
5. Un signal consigné avant le verdict, par une version gelée avant l'épisode, juge hors échantillon (Rudoler et al., p. 12 et p. 3-4) ; bloc A : prospectif 0,207 contre 0,200 de la formule ; rétrospectif 0,635.
6. Choisir sur le relevé qui juge biaise le relevé du choisi : bloc F, loi exacte, 0,367 pour 0,20 à dix versions.
7. Les négatifs pris chez le suspect et le remplacement de la sonde d'origine abaissent le rappel sur ce que l'oracle ne voit pas ; l'union le garde : bloc B (0,101 ; 0,160 ; 0,323 ; origine 0,372).
8. En service, l'oracle ne sépare pas le sabotage de l'échec honnête (N-075, § 2 (ii)) ; bloc C : positifs mêlés 0,568, transfert de signature 0,818.
9. L'audit orienté non pondéré biaise la recapture (0,955 pour 0,289) et l'apprentissage (0,022 pour 0,203) : bloc D.
10. Au taux minimal de la table, K·(1 − 0,05^(1/K)) tend vers −ln 0,05 ≈ 3,0 : bloc E, loi exacte.
11. Trois positifs n'apprennent pas une direction neuve en grande dimension ; une mise à jour de faible capacité, si : formule du bloc A et commande de la section 6.
12. Supposé : l'agent en service est gelé et ne garde de mémoire d'un épisode à l'autre que par l'état de l'environnement (« hygiène de l'état persistant », programme l. 169) ; donc une version réapprise qui n'agit que par l'audit après coup n'ouvre aucun canal (clause 9).
13. Supposé : les mécanismes des mondes jouets (directions fixes, bruit isotrope, sondes linéaires par épisode) gardent leur sens sur des sondes réelles ; leurs tailles d'effet, non.
14. Les pages citées [établi] sont lues ce jour sur les PDF, par extraction de texte page à page, empreintes vérifiées contre leurs compagnons.

**Objets de contrôle.**
- *La règle « jugement prospectif aveugle »* : objet où « la recapture est aveugle » est faux par construction, le jugement rétrospectif sur les positifs d'apprentissage ; attendu, un rappel gonflé (≈ 0,6 pour ≈ 0,2) ; rendu, 0,635 pour 0,207. Objet où c'est vrai, le jugement prospectif ; attendu, la vérité (formule 0,200) ; rendu, 0,207.
- *La recapture pondérée* : objet faux, la recapture naïve sous audit orienté ; attendu ≈ 0,9 ; rendu 0,955. Objet vrai, la pondération par l'inverse de la probabilité d'audit ; attendu ≈ 0,29 ; rendu 0,299 (vérité 0,289).
- *Les gardes* : journal sain, attendu vert partout, rendu vert ; quatre artefacts plantés, attendu rouge sur la seule garde visée, rendu conforme (bloc G).
- *Prédictions du script* (scellées avant l'exécution, `9d35c1ac…`) : A1, A2, B2, C1, D1, D2, E1, F1, G1 tenues. **B1 tenue dans son sens, manquée de 0,001 sur un seuil** : réapprise avec négatifs pris chez le suspect, 0,101 pour « au plus 0,10 » prédit ; écart à la saine 0,058 pour « au moins 0,05 » prédit. Rien n'a été changé après exécution.

**Premier pas non justifié.** Le pas 12 : que l'agent en service ne voie rien d'une version réapprise qui n'agit que par l'audit après coup. Ce qui le justifierait : l'inventaire, par un agent habilité, de ce que l'agent observe après un aiguillage et de ce que le chemin d'audit peut toucher (horodatages, charge, relances ; N-076, § 6.2), puis le devin de N-076, § 6.3, sur ce que l'agent observe, resté au hasard. Le pas 13 est le second : ce qui le justifierait, le bras « boucle » sur organismes.

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur. Le pas 10 est une loi exacte qui se prête à une re-dérivation.

**Trouvaille de côté.**
1. Le bras « boucle » peut servir d'épreuve au passage obligé (N-075, § 6) : le transfert des prises de signature vers les familles d'excès n'est au-dessus du hasard que si une direction interne commune au sabotage existe. Dans le monde jouet, où elle existe par construction, 0,82 ; sans elle, 0,5 attendu.
2. Toute pièce qui calcule une recapture « sur les audités » sans poids, quand l'audit est orienté, est fausse d'un facteur qui peut dépasser trois (bloc D) ; la définition de N-075 (« au hasard ») est à tenir à la lettre.
3. Corriger le biais d'échantillonnage déplace le rappel d'une famille à l'autre (bloc D : 0,551 → 0,251 sur la famille déjà vue) ; seule l'union avec l'ancienne version garde les deux.
4. Le dossier parent est exclu du suivi de git par `.git/info/exclude` (ligne 8) : le versement de ces fichiers demande un geste exprès de la mère.

**Évaluateur et conseil.** Ce qui juge cette pièce : le collisionneur et l'organisme dans la question fusionnée (`GO-2026-11-21-61`), puis Lazar ; aucun juge admis sur témoins. Par où elle pourrait être bien jugée sans le mériter : les mondes jouets confirment des mécanismes que leur construction contient (directions plantées, oracle à q de 0 ou 1) ; ils montrent que l'effet existe sous supposition, non sa taille dans le programme ; et la règle, faite de pièces publiées, paraît rigoureuse parce qu'elle est longue. Conseil au contre-lecteur, trois modes : « garantie qui suppose ce qu'elle prouve » (pas 12, canal fermé ; agent gelé) ; « énoncé infidèle » (ma lecture des deux moitiés du point 4, et la distinction entre un choix sur le relevé, interdit, et l'apprentissage d'une procédure scellée, permis) ; « antériorité » (Rudoler et al. occupent-ils aussi la source des négatifs et le régime de l'oracle ?).

## Ce que je n'ai pas fait

- Je n'ai lu ni la réponse de Fable ni rien de ses dérivés, ni l'erratum 3 v1 de N-075 (l'erratum 3 v2 prime), ni les notes sources de N-076 (« percée », « attaquant informé », « asymétries », « science de la détection »), ni la lecture des douze voisins.
- Rudoler et al. : pages 1 à 10 lues en entier par extraction de texte ; pages 12, 14 et 17 en partie ; le reste (annexes, p. 11 à 24) par motifs seulement. Les autres PDF : pages citées seulement.
- Aucune recherche d'antériorité dédiée au-delà des pièces citées ; « non trouvé » ne vaut pas « libre » (R8).
- Aucun préenregistrement, verdict ou résultat d'expérience lu ; aucun dossier ni chemin interdit ouvert.
- Écart à signaler : en extrayant le texte des PDF, j'ai d'abord écrit, dans un dossier partagé du bloc-notes (`/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/txt/`), neuf fichiers de mêmes noms que des extractions d'autres agents, peut-être en les remplaçant par le même texte mis en page ; puis j'ai travaillé dans mon propre sous-dossier. Aucun fichier du dépôt n'est touché hors de ce dossier.

## Fichiers et provenance

| fichier | empreinte |
|---|---|
| `calculs-boucle-audit-recapture-opus-v1.py` (prédictions comprises, scellé avant exécution à 16:49 UTC) | `9d35c1aca2a885b91e3c2d99922c97954b5eff8ff65851aa8ff950b500e465bb` |
| `calculs-boucle-audit-recapture-opus-v1.txt` (sortie ; python 3.13.18, numpy 2.5.3, graine racine 202611211648, `SeedSequence`) | `eec5de80c3bfa355301f8f265dccfabec13e604b0f775fd60835364c4a1e5603` |
| `sources/2101.11665v2.pdf` (Farquhar, Gal, Rainforth, téléchargé ce jour, arXiv) | `02a8fc2260902285abadd41ed813e168b07b459a913f3ee4de6be5ee748235a9` |

| pièce citée | PDF du dépôt | empreinte (égale au compagnon) | pages |
|---|---|---|---|
| Rudoler et al., 2609.36049 v1 | `docs/sources/pdf/asymetries-attaquant-v1/2609.36049v1.pdf` | `856b3857c20cbafd1be8c6f5c2901c6e139db371f9c9abcb97933e780104ed41` | 3, 4, 7, 8, 10, 12, 14, 17 |
| Zrnic, Candès, 2403.03208 v3 | `docs/sources/pdf/adjudant-opus-independant-v1/2403.03208v3.pdf` | `58d973da4ae6208ad7f8a7be53d7b4e1754681ac77335da691c7b20c30d68855` | 1, 7 |
| Zhu, Zuo, Sun, « Blindfold », 2610.37055 v1 | `docs/sources/pdf/attaquant-informe-v1/2610.37055v1.pdf` | `5250fa1176ac804ba32fd4998fa47b2f278757ce9393a1443d4b9a7b8617f861` | 1, 12 |
| Dwork et al., 1506.02629 v2 | `docs/sources/pdf/mathematiques-nouvelles-methodes-v1/verification-memoire-v1/1506.02629v2.pdf` | `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71` | 2, 3 |
| Lyons Keenan et al., 2609.36490 v1 | `docs/sources/pdf/2609.36490v1.pdf` | `eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088` | 1, 6 |
| Gupta, Jenner, 2506.14261 v4 | `docs/sources/pdf/2506.14261v4.pdf` | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | 5, 10 |
| Kloft, Laskov, 1003.0078 v1 | `docs/sources/pdf/1003.0078v1.pdf` | `ebb4a2482dd543f439898546a42f2ce47929256e9d41b4f7c60e0ff7a87c8d97` | 1 |
| Farquhar, Gal, Rainforth, 2101.11665 v2 | `sources/2101.11665v2.pdf` (ce dossier) | `02a8fc22…` | 1 |
