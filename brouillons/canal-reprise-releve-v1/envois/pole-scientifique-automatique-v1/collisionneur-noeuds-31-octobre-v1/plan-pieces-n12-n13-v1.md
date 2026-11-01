# Plan des pièces N12-N13 — v1

**N12** = rouvrir ou non les couches 3 et 4 de l'organisme. **N13** = tester ou non une récompense collective. Ce plan met en pièces les décisions de Lazar du 1er novembre 2026 à 09:43 UTC (R-1042 de `registres/decisions.md`), les onze apports seuls et les neuf divergences non résolues de la synthèse du collisionneur.

## En-tête

- **Rédacteur** : sous-agent neuf, modèle Opus 5.5 (`claude-opus-5-5`), lignée conv-audit. Je n'ai écrit ni la question, ni l'annexe, ni les critères, ni la synthèse, ni la relecture, ni aucune cellule.
- **Dates** (`date -u`) : début de lecture 09:44:54 UTC ; début d'écriture 09:57:47 UTC ; fin d'écriture en pied de page.
- **Statut** : brouillon v1, non scellé, non commité, sans compagnon `.sha256` (consigne). C'est un plan. Il ne décide rien, ne vaut pas préenregistrement et ne franchit aucune porte. Niveau méthode.
- **Limites** : rien lu sous `donnees/` (ni cellules, ni faits servis). Aucun appel de réseau ni de modèle, aucun `git fetch`. N-045, N-053, N-058 et le registre des feux verts sont lus sur la référence locale `origin/main` (`45853968`). Les positions des espèces viennent de la synthèse seule, qui attend un erratum (section 7).
- **Garde de sécurité** (RN-14 de la relecture ; R-1012 : « pas de conception de mécanisme ») : aucun paramètre de conception d'un entraînement de l'organisme sous récompense collective, ni d'une génération de code par l'organisme, n'est reproduit ici. Les pièces renvoient aux cellules et aux préenregistrements à venir. Le sujet « auto-organisation de l'organisme inspirée d'Avalon » est suspendu et n'est pas traité.
- **Réserve de famille** : je suis du modèle de l'auteur de la relecture et de celui de la lecture vérifiée d'Avalon, et de la même famille que Fable et Opus 4.6, qui portent sept des onze apports.

### Pièces lues et empreintes recalculées (`sha256sum`)

| Pièce | SHA-256 |
|---|---|
| Relecture Opus de la synthèse, `…/collisionneur-noeuds-31-octobre-v1/relecture-opus-synthese-n12-n13-v1.md` | `c05949af2b93f6af4facec06009a89da9b05b033b1e401edfc1de6fcba51d2a7` (égale au compagnon) |
| Synthèse, copie hors dépôt `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/n12-n13/synthese-n12-n13-v1.md` | `b1d28f0d43245c3534d469f38e77bf4e14da2a70f39f4f1bd76a0b42c96b8cb4` (égale au compagnon) |
| Question v2, `question-collisionneur-n12-n13-couches-recompense-v2.md` | `9faee0aadf01b4837fa67df414ed4552519d80c6c31c9326976c27e391de6986` (égale au compagnon) |
| Annexe du tour 2, `annexe-tour-2-n12-n13-v1.md` | `9dc13ece12d3864cc255b66dbdae869c9219887f932dfa83ab91714a22e0156d` (égale au compagnon) |
| `registres/decisions.md` de la branche (R-1037, R-1038, R-1041, R-1042, l. 1001–1006) | `af0091bfd160cf6316303d9196fd096e5131236a0e4b9b6e3db8edb54473da9a` (pas de compagnon) |
| Message n° 313, `brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-11-01_n313.md` | `f0a38aad82369f0ae2bb2273caa6d26f4061d00d840b32a4fd786276cc7299e4` (égale au compagnon) |
| N-045 v2 (`origin/main:docs/decisions/decision-N-045-v2.md`) | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` (égale au compagnon) |
| N-053 v1 (`origin/main`) | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` (égale au compagnon) |
| N-058 v1 (`origin/main`) | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` (égale au compagnon) |
| Lecture vérifiée d'Avalon, `docs/notes/rlcr-v1/lecture-verifiee-avalon-m1-v1.md` | `a8251ea8bca96acad1443eea24a090e7b254efa1d17d1fec6119ff9544c40583` |
| Lecture vérifiée de Damani, `docs/notes/rlcr-v1/lecture-verifiee-damani-rlcr-v1.md` | `4e29301af66bf702387ff5923018979c65ea9cde702dce93862b65031a1c9bc0` |
| `origin/main:registres/go.md` (l. 175–176 : feux verts du 1er novembre) | `93d4bc8a272fe4ecf17aa66ed1070e2667745e4fa2d37125d10d28a74e73ce4f` |

## 0. Lexique : à quoi renvoie chaque nom

- **Les quatre espèces du collisionneur** : **Fable** = espèce A (Claude Fable 5.1) ; **Opus 4.6** = espèce B ; **Argon** = espèce C (Gemini 4 Argon) ; **Kimi** = espèce D (Kimi K3.1 Pro). Les renvois du type « A-T3 E3″ » désignent une cellule (T1 conception, T2 critique croisée, T3 réponse) et une section de cette cellule, comme dans la synthèse.
- **Couche 3** : moniteurs neufs écrits à la demande, plus réécriture de soi restreinte dans un bac à sable. **Couche 4** : pôle théorie et vérification formelle par l'assistant de preuve Lean (question v2, l. 15). Attention : R-1041 (3) appelle aussi « couche 4 » la production d'attaques neuves en quarantaine. Ce n'est pas le même objet (réserve 1).
- **Étape 2** : l'étape où l'organisme apprend sa composition (N-045).
- **N-045** (25 octobre) : la composition est apprise, le coût entre dans le signal, les voies bon marché passent d'abord. **N-053** (26 octobre), point 5 : aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, piste « organisme » comprise. **N-058** (28 octobre) : la composition se juge sur l'oracle du monde planté et le coût, jamais sur le verdict du juge ; la sélection des **fiches** reste permise, pas celle des **agents**.
- **Oracle planté** : la vérité connue d'un monde où un tiers a planté des structures et des témoins.
- **Taux de signalement de départ** : proportion des cas où le modèle de départ, sans entraînement, signale quand il le doit.
- **Canaris « à ne pas signaler »** : cas où rien n'est à signaler. Ils servent à compter les faux signalements.
- **Règles du dépôt citées** : R1 préenregistrement scellé avant toute expérience décisive, simulation comprise ; R2 contre-lecture par un sous-agent neuf ; R4 même audit dans les deux sens (« trop propre » = réserve) ; R5 toute garde essayée sur un cas sain et sur un artefact, sans repli silencieux ; R9 graines par `SeedSequence` ; R10 arrêt par identifiant d'instance ; R11 vérifier sur disque avant de déclarer absent ; R13 verdict par un sous-agent neuf.
- **RN-xx** : constats de la relecture Opus (`c05949af…`), cités chaque fois avec leur objet.
- **Qui** : **conv-audit** = moi et mes sous-agents, sur processeur, sans dépense, sans lire `donnees/`. **session-depot** = la session qui tient les données, le noyau, les devis et les dépenses. **Lazar** = décision.
- **Coût** : **sans dépense** = processeur et heures d'agent ; **dépense faible** = inférence de quelques heures, ou appels de quelques dizaines de dollars au plus (devis et feu vert quand même) ; **avec dépense** = entraînement. Les ordres de grandeur sont ceux des espèces, **illustratifs**, jamais opposables.

## 1. En bref

- **21 pièces** : 10 sans dépense, 9 à dépense faible, 2 avec dépense. Les quatre volets de R-1042 et les onze apports sont tous couverts. Plusieurs pièces en servent plusieurs.
- **Faisables tout de suite, sans dépense** : l'erratum de la synthèse (P01, session-depot) ; la grille des étiquettes (P02), la clause du résidu (P03), la règle de réexamen (P04, sauf la date), la simulation du crédit plat (P05) et la note de circularité (P06), chez conv-audit ; l'inventaire des journaux des juges (étape 0 de P08, session-depot). Les préenregistrements de P10 et P12 peuvent aussi être rédigés dès maintenant, sans être scellés.
- **Sept décisions de Lazar restent** (section 5), plus les feux verts de dépense sur devis. Aucune n'a de défaut à 48 heures.
- **Rien ne cite la synthèse ni ne part au collisionneur avant l'erratum** (section 7), le tour 2 en premier.

## 2. Pièces des décisions de Lazar (R-1042)

### P03 « clause du résidu du catalogue »

Réalise **N12 (b)** (la mesure inscrite au préenregistrement de l'étape 2, « go ») et l'**apport n° 10 de Kimi**.

- **Quoi** : une clause à insérer au préenregistrement de l'étape 2. Le **résidu** est la part des familles de témoins plantés, tenues à l'écart, qu'aucune composition atteignable sous N-045 ne détecte, au budget de la meilleure composition, avec un intervalle par famille. Le **catalogue** comprend tout ce que N-045 laisse composer **ou entraîner** : espèces de frontière et instruments locaux entraînés (sondes, adaptateurs ; énoncés 1 et 5). Selon RN-05, seuls le code écrit hors catalogue et la preuve formelle sont hors de N-045.
- **Ce qu'elle montrerait** : s'il existe un besoin chiffré que N-045 ne couvre pas. Résidu nul dans l'intervalle : couches 3 et 4 fermées sur preuve. Résidu au-dessus du seuil gelé : réexamen (P04).
- **Cas sain** : une famille plantée que le catalogue peut représenter par construction donne un résidu nul.
- **Artefacts** : une famille plantée par le tiers hors de ce que le catalogue peut représenter doit apparaître dans le résidu. Avec un oracle permuté, le résidu est déclaré non interprétable et n'est pas lu.
- **Coût** : la clause est sans dépense. La mesure tourne dans l'étape 2, sous son devis.
- **Qui** : conv-audit rédige ; l'auteur du préenregistrement de l'étape 2 l'insère ; Lazar a dit « go ».
- **Préenregistrement (R1)** : oui, comme partie de celui de l'étape 2, avec seuil gelé et contre-lecture (R2).
- **Ordre** : rédiger maintenant ; sceller avec l'étape 2. Dépend de P01 (RN-05 : couverture exacte de N-045).

### P04 « règle de réexamen »

Réalise la **date de réexamen de N12 (b)**, l'**apport n° 5 d'Opus 4.6** (calendrier) et l'**apport n° 4 d'Opus 4.6** (coût d'opportunité d'un organisme figé).

- **Quoi** : une règle écrite d'avance. N12 est réexaminé au premier de trois événements : la lecture scellée du résidu (P03), la date butoir (décision « date de réexamen »), ou le déclencheur de coût d'opportunité. Ce coût se calcule par une formule gelée : familles manquées (résidu) × leur poids × durée restante, contre le coût et les risques nommés d'une ouverture (circularité du bac à sable, N-053, effets indirects selon Kimi).
- **Ce qu'elle montrerait** : que la fermeture a une fin, et à quel prix on la maintient.
- **Cas sain** : résidu nul, donc coût d'opportunité nul et pas de réexamen avancé.
- **Artefacts** : un résidu planté connu doit déclencher la règle. Une date butoir passée sans résultat de l'étape 2 déclenche le réexamen sur les pièces disponibles (P10, P19), sans prolongation tacite.
- **Coût** : sans dépense. **Qui** : conv-audit rédige ; Lazar fixe la date.
- **R1** : la règle est gelée avant toute lecture de l'étape 2 (elle entre dans la clause P03).
- **Ordre** : maintenant ; dépend de la décision « date de réexamen » et de P03.

### P10 « essai preuve formelle contre suite bon marché »

Réalise le **second volet de N12 (b)**.

- **Quoi** : comparer, à coût apparié, l'assistant de preuve Lean à une suite bon marché (tests, mutations, scripts, relecture par un modèle d'une autre famille). La comparaison porte sur une banque d'énoncés et de preuves courtes où un tiers a planté des erreurs, classe par classe, mêlées à des preuves saines. Sous-pièce **P10a « banque d'erreurs plantées »** : un sous-agent neuf la construit et la scelle, et ne fait tourner aucun des deux bras. Matériau de départ possible : les coquilles de Damani relevées par un lecteur neuf (citées par Fable et Argon).
- **Ce qu'elle montrerait** : pour chaque classe d'erreurs, le rappel et les fausses alertes de chaque bras, et si Lean bat la suite sur au moins une classe à coût apparié. La conclusion est bornée à la banque (Fable, Kimi).
- **Cas sain** : sur les preuves saines, les fausses alertes sont comptées.
- **Artefacts** : (i) les erreurs plantées par classe mesurent le rappel ; (ii) une erreur plantée dans la **traduction** de l'énoncé en Lean (spécification fausse, preuve juste) ne doit pas être créditée à Lean (Kimi : « une preuve ne valide pas une spécification ») ; (iii) les politiques triviales (« tout est faux », « tout est sain ») doivent échouer (annexe K d'Avalon, « score the trivial policies », lecture vérifiée § 4).
- **Coût** : dépense faible. Pas de carte graphique, mais des appels de sous-agents à chiffrer. Illustratif : Argon « 0 dollar de carte, quelques dollars d'appels », « 3 h par énoncé » ; Opus 4.6 « processeur, quelques jours » ; Fable et Kimi ne chiffrent pas.
- **Qui** : conv-audit conçoit le protocole et le préenregistrement ; un tiers construit P10a ; session-depot chiffre les appels et exécute si les sous-agents Lean sont de son côté (n° 313, point 1) ; un lecteur neuf rend le verdict ; Lazar donne le feu vert sur devis.
- **R1** : oui, car son résultat décide d'une ouverture. La correspondance « résultat → forme d'ouverture » y est gelée (décision « forme de la couche 4 ») ; contre-lecture (R2). Réserve R4 : l'accord à quatre sur ce comparateur est « trop propre » (synthèse) ; le préenregistrement dit quel résultat ferait conclure contre la suite bon marché autant que pour elle.
- **Ordre** : préenregistrement rédigeable maintenant ; scellement après la décision « forme de la couche 4 » et P01 ; banque après le scellement. Indépendant de l'étape 2.

### P12 « pré-test du signalement de départ »

Réalise **N13 (a), premier volet**, et le **pré-test** de la précaution d'Avalon.

- **Quoi** : mesurer, sans entraînement, sur le modèle de départ que l'étape 2 entraînerait : le taux de signalement quand il est dû, le taux de faux signalements sur les canaris, la part « non évaluable ». Les étiquettes viennent de la grille P02. Les scénarios viennent d'un **lot de calibration distinct** du lot d'évaluation tenu à l'écart. Le lot tenu à l'écart n'est pas lu avant P17 : sinon les concepteurs l'auraient vu.
- **Ce qu'elle montrerait** : si un essai payant peut mesurer une chute. Avec un taux nul ou plein, aucun essai ne le peut (carte R-1038). Le pré-test fournit aussi la base du plancher et de la chute maximale à geler pour P17.
- **Cas sain** : avec une instruction explicite de signaler, on attend un taux élevé.
- **Artefacts** : outil de signalement indisponible, donc « non évaluable » et non « omission » ; la politique « signaler toujours » est trahie par les canaris ; un fichier de mesure absent arrête la lecture, sans valeur par défaut.
- **Coût** : dépense faible, inférence seule. Illustratif : Fable « quelques heures de carte » ; Argon « quelques dollars d'inférence » ; Kimi « dépense faible ».
- **Qui** : conv-audit rédige le préenregistrement ; session-depot fait le devis, tient les scénarios et exécute ; un lecteur neuf lit ; Lazar donne le feu vert.
- **R1** : oui, court. La bande de jugeabilité est gelée avant la lecture. Les espèces divergent (Fable : sous 0,3, l'essai payant n'est pas payé ; Argon : entre 0,40 et 0,90 ; illustratifs). La bande se déduit de la chute minimale détectable calculée par P05, pas d'un choix au jugé.
- **Ordre** : après P02, P09 et P05. Le modèle de départ doit être fixé avant ; changer de modèle exige un feu vert (interdit du dépôt).

### P08 « audit de calibration des juges existants »

Réalise **N13 (a), second volet**, et le **go sur Damani** (recalibration a posteriori des juges existants, sans dépense, chez session-depot).

- **Quoi** : d'abord l'**étape 0, inventaire** : les confiances ou probabilités de jetons des juges actuels sont-elles journalisées par fiche, avec la vérité de l'oracle ? Ce n'est pas établi (RN-08 (iv)). Si oui, on calcule le score de Brier, l'erreur de calibration et l'aire sous la courbe de discrimination, toujours les trois ensemble. On les calcule avant et après une recalibration de Platt (ajustement logistique a posteriori) ou isotonique (ajustement monotone a posteriori), ajustée sur une partie des familles et évaluée sur les familles tenues à l'écart. Lignes de base : verdict binaire du juge, confiance constante au taux de base, confiance uniforme, étiquettes permutées.
- **Ce qu'elle montrerait** : si la confiance des juges porte de l'information au-delà de leur verdict, et si une recalibration bon marché suffit. On saurait alors si entraîner un juge local par récompense de calibration aurait un objet. Elle ne montre rien de l'efficacité de cette récompense : Damani ne teste pas de recalibration de Platt ; son comparateur est un classifieur entraîné de 7 milliards de paramètres (RN-08 (iii) ; lecture vérifiée de Damani, l. 65). L'ordre « recalibration d'abord » repose sur le coût.
- **Cas sain** : un juge dont la confiance est informative, sur un sous-ensemble à vérité connue, a une aire au-dessus de 0,5.
- **Artefacts** : étiquettes permutées, aire proche de 0,5 ; une confiance constante qui coïncide avec un taux de base extrême donne une calibration flatteuse, que l'aire démasque (cas CommonsenseQA, lecture vérifiée de Damani, l. 217, 223) ; un journal sans vérité d'oracle fait refuser l'audit, sans imputation.
- **Coût** : sans dépense (processeur ; Opus 4.6 : « quelques minutes », illustratif). Si les confiances ne sont pas journalisées, re-servir les juges devient une dépense faible, sur devis.
- **Qui** : session-depot (les paires sont sous `donnees/`) ; conv-audit rédige le préenregistrement court sans lire les données ; un lecteur neuf lit.
- **R1** : oui, court, car l'audit conditionne une dépense (entraîner ou non un juge local). Ne pas y écrire « le post-hoc fait jeu égal ou mieux hors domaine » : c'est faux sur les moyennes hors domaine (RN-08 (ii)). Si la confiance est lue comme moyenne des probabilités de jetons, c'est un bras de diagnostic, jamais une mesure de production (N-026).
- **Ordre** : inventaire tout de suite ; audit ensuite, en parallèle de P12.

### P17 « bras de récompense collective à trois bras »

Réalise **N13 (b)** et la **précaution d'Avalon** (go).

- **Quoi** : dans l'étape 2, après son dessin et un devis, trois bras : un bras sous récompense collective ; un bras sous récompense individuelle, comparé à information et effectif égaux (principe de la convergence n° 10 de la synthèse ; forme non reproduite, RN-14) ; un **bras témoin non entraîné**, à poids gelés. Un quatrième bras mono-agent seulement si P13 montre un effet de l'effectif à poids fixes (décision « témoin mono-agent »). Le signalement est mesuré dans les trois bras à chaque point de contrôle, point 0 compris, par agent et par run. Les positifs et les négatifs d'omission viennent du même point de contrôle et des mêmes poids (convergence n° 3). La graine d'entraînement est l'unité d'inférence (convergence n° 1).
- **Précaution d'Avalon, intégrée** : (i) scénarios de signalement scellés par un tiers avant tout entraînement, jamais servis à l'entraînement ; (ii) pré-test P12 ; (iii) signalement et canaris absents de toute récompense ; (iv) plancher absolu de signalement et chute maximale gelés d'avance, à partir de P12 et du bruit du pilote A/A (deux runs du même bras, qui ne doivent pas différer ; N-045, énoncé 6 (i)) ; leur franchissement vaut arrêt et interdit toute intégration à l'organisme, quel que soit le gain d'utilité (Kimi) ; (v) qui lit : P16.
- **Ce qu'elle montrerait** : grâce au témoin, elle sépare l'effet de l'entraînement (bras entraînés contre témoin) de l'effet du collectif (collectif contre individuel). Deux bras ne le font pas (RN-06) : selon la lecture vérifiée d'Avalon (réserve 1), tout entraînement qui ne récompense pas le signalement peut le faire baisser.
- **Cas sain et artefacts** : ceux des gardes de P16. Plus : dans le bras témoin, aucune chute au-delà du bruit du pilote A/A.
- **Coût** : avec dépense. Illustratif, avec un écart de deux ordres de grandeur entre espèces : Fable « dizaines d'heures de carte par bras » ; Argon « 40 à 120 dollars » (premier tour, non rechiffré) ; Kimi « 300 à 1 500 heures de carte » ; Opus 4.6 « 600 à 3 000 heures de carte ».
- **Qui** : conception et préenregistrement dans l'étape 2 (auteur à désigner) ; devis par session-depot ; feu vert de Lazar ; verdict par un sous-agent neuf (R13).
- **R1** : oui, avec contre-lecture (R2).
- **Ordre** : après le dessin de l'étape 2, P03, P05 (puissance), P07, P11 (mesure de pression, divergence n° 3), P12 (jugeabilité, plancher), P13 (décision « témoin mono-agent ») et P16.

### P16 « lecteur des signalements et gardes de la précaution »

Réalise **« qui lit »** (« à nommer », R-1042) et les gardes (i), (iii) et (iv) de la précaution. **Ma proposition pour « qui lit »** comporte trois niveaux.

1. **Une garde mécanique**, hors de la machine qui entraîne (Kimi : « journalisation et arrêt hors du bac à sable »). À chaque point de contrôle, elle lit les mesures scellées et les compare au plancher et à la chute maximale gelés. Un franchissement ou une mesure manquante déclenche l'arrêt par identifiant d'instance (R10), consigné dans `registres/arrets.md`, et bloque toute promotion.
2. **Un lecteur neuf par point de contrôle** : un sous-agent ni auteur du préenregistrement, ni de l'entraînement, ni de l'analyse. Il est lancé par conv-audit, car celui qui entraîne ne lit pas. Il reçoit les seules mesures scellées, les seuils gelés et les empreintes. Il rend un verdict scellé : « au-dessus », « franchi » ou « non jugeable ». Tout « franchi » et tout « non jugeable » partent à Lazar.
3. **Lazar seul** lève un arrêt : c'est un écart à un préenregistrement scellé, donc un nœud.

- **Gardes** : cloisonnement (le manifeste des données d'entraînement est comparé aux empreintes du lot tenu à l'écart) ; récompense sans signalement (les entrées de la fonction de récompense excluent tout champ de signalement et de canari) ; arrêt (ci-dessus).
- **Cas sains** : mesures au-dessus du plancher, on continue ; données sans recouvrement, acceptées ; récompense conforme, acceptée.
- **Artefacts** : mesure injectée sous le plancher, arrêt ; fichier de mesure absent, arrêt, sans repli silencieux ; scénario tenu à l'écart injecté dans l'entraînement, refus ; récompense qui lit un champ de signalement, refus.
- **Coût** : sans dépense (code et essais sur processeur).
- **Qui** : Lazar (décisions « qui lit » et « portée de l'arrêt ») ; session-depot code les gardes (noyau) ; conv-audit lance les lecteurs.
- **R1** : les seuils vivent dans le préenregistrement de P17 ; les gardes relèvent de R5.
- **Ordre** : avant P17.

## 3. Les onze apports seuls : la pièce qui réalise ou éprouve chacun

### Apport n° 1 — Fable : diffusion sans entraînement, à poids fixes → **P13 « diffusion à poids fixes »**

- **Quoi** : à poids fixes, faire varier le nombre d'agents et la possibilité de communiquer, puis lire le signalement par agent et par run. Le plan est celui de Fable (A-T1 E3′, A-T3 E3′′), renvoyé et non reproduit (RN-14). Les auteurs d'Avalon nomment ce mécanisme (diffusion de responsabilité) sans le tester (lecture vérifiée, § 3.1).
- **Ce qu'elle montrerait** : si le signalement baisse avec l'effectif sans aucun entraînement. Une baisse par run signale la diffusion. Une baisse par agent, avec un taux par run constant, signale la coordination. Un effet du seul canal signale le canal. Si l'effectif compte, une partie de la chute d'Avalon n'exige pas l'entraînement, et le témoin mono-agent de P17 devient nécessaire. P13 ne conclut rien sur une origine dans l'entraînement (critique de Kimi).
- **Cas sain** : avec un seul agent, on retrouve le taux de P12.
- **Artefacts** : un agent instruit de toujours signaler donne un taux par run proche de 1 (la mesure compte bien « au moins un ») ; des étiquettes d'agent permutées ne donnent aucun effet. Les agents d'un même run sont corrélés, donc l'unité d'inférence est le run (critique d'Argon).
- **Coût** : dépense faible. Illustratif : Fable « quelques heures de carte ».
- **Qui** : conv-audit préenregistre ; session-depot, sur un devis groupé avec P12.
- **R1** : oui. **Ordre** : après P12, dont l'effectif 1 est le pré-test.

### Apport n° 2 — Fable : troisième mécanisme de la chute (raisonnement contracté) → **P14 « raisonnement contracté »**

- **Apport** : au fil de l'entraînement, le raisonnement d'Avalon devient télégraphique (p. 61 ; lecture vérifiée, § 3.4). Cela rendrait l'action de signaler moins probable sans changer ce que le modèle reconnaît.
- **Quoi** : à poids fixes, imposer des budgets de raisonnement de longueurs différentes. Mesurer à la fois la reconnaissance (alerte verbalisée, et sonde boîte blanche existante si elle est disponible) et l'action (signalement émis). Dans P17, la longueur du raisonnement par point de contrôle est rapportée comme covariable, hors critères.
- **Ce qu'elle montrerait** : si un raisonnement raccourci fait baisser l'action à reconnaissance constante (« envisagé et non fait », lecture vérifiée, § 3.4). Elle montrerait que le mécanisme est plausible à poids fixes, pas qu'il cause la chute sous entraînement.
- **Cas sain** : un budget long reproduit P12.
- **Artefacts** : un budget qui couperait l'appel de l'outil de signalement lui-même produirait un effet de format ; l'appel de l'outil reste donc hors du budget de raisonnement. Contrôle supplémentaire : longueur imposée par un remplissage neutre, sans changement de contenu.
- **Coût** : dépense faible, non chiffrée par l'espèce, sur le même devis que P12.
- **Qui** : conv-audit préenregistre ; session-depot exécute. **R1** : oui. **Ordre** : après P12, dans le même lot que P13.

### Apport n° 3 — Fable : « faux trilemme » → **P18 « sondes sur les trois bras »**

- **Apport** : un bras de l'étape 2 (option (c1)) et un objet d'étude pour les sondes (option (c3)) ne s'excluent pas : le bras collectif produit l'omission, le bras individuel sert de contrefactuel. Réserve RN-02 : Argon et Kimi le reprennent en substance, l'apport n'est donc pas strictement seul.
- **Quoi** : une clause du préenregistrement de P17. Les sondes boîte blanche et boîte noire s'appliquent aux épisodes des trois bras. Les positifs et les négatifs viennent du même point de contrôle et des mêmes poids. Un prédicteur sur les traits du texte sert de base obligatoire (N-029). Aucune moyenne ni médiane sur les jetons en production (N-026).
- **L'objection d'Opus 4.6, omise par la synthèse (RN-04)**, entre ici. L'omission d'Avalon n'a qu'un point de décision : elle n'est diffuse qu'en partie (lecture vérifiée, § 3.2 ; R-1013). Pour que (c3) serve la menace diffuse du programme, les scénarios de P17 doivent comprendre des omissions réparties sur plusieurs points de décision. Sinon on mesure une omission simple et on conclut que les sondes « marchent » sur un cas plus facile que la cible (pire cas nommé par Opus 4.6).
- **Ce qu'elle montrerait** : si une sonde détecte l'omission produite par l'entraînement mieux que le texte, à régime égal.
- **Cas sain** : des omissions plantées dans les épisodes du bras témoin sont détectées.
- **Artefacts** : une sonde qui classerait le bras ou le point de contrôle au lieu de l'omission est démasquée par l'appariement au même point de contrôle et par la permutation des étiquettes de bras (« sélection sur la variable dépendante », synthèse, N13 (1)).
- **Coût** : dépense marginale faible (activations extraites d'épisodes déjà produits par P17).
- **Qui** : préenregistrée avec P17 ; session-depot exécute. **R1** : oui, dans P17. **Ordre** : avec P17, après P15.

### Apport n° 4 — Opus 4.6 : coût d'opportunité d'un organisme figé → **P04** (formule et déclencheur)

- **Ce qu'elle montrerait** : le prix de la fermeture, chiffré par le résidu au lieu d'être supposé nul.
- **Cas sain** : résidu nul, coût nul. **Artefact** : un résidu planté connu donne le coût attendu, ce qui vérifie le calcul.
- **Coût** : sans dépense. **Qui** : conv-audit. **R1** : la formule est gelée dans la clause P03. **Ordre** : avec P03 et P04.

### Apport n° 5 — Opus 4.6 : calendrier → **P04** (date butoir, décision « date de réexamen »)

- **Apport** : si l'étape 2 consomme dix des douze mois, il ne reste rien pour les couches.
- **Ce qu'elle montrerait** : que le réexamen a lieu même si l'étape 2 glisse.
- **Cas sain** : un résultat de l'étape 2 avant la date butoir déclenche le réexamen à ce résultat. **Artefact** : une date butoir passée sans résultat déclenche le réexamen quand même, sans prolongation tacite.
- **Coût** : sans dépense. **Qui** : conv-audit ; Lazar fixe la date. **R1** : non (règle de gouvernance), mais elle est écrite avant toute lecture. **Ordre** : maintenant.

### Apport n° 6 — Opus 4.6 : l'oracle de N-058 ne mesure pas le signalement → **P09 « canaris de signalement »**

- **Quoi** : ajouter au monde planté de l'étape 2, et aux scénarios de P12, des cas où un signalement est dû et des canaris « à ne pas signaler », scellés par un tiers. Ils vont dans une **colonne séparée**, qui n'entre jamais dans le critère de composition de N-058. Sinon le signalement deviendrait récompensé par la sélection : ce serait contraire à la précaution (iii), et c'est l'erreur qu'Argon a retirée en T3. Le principe est déjà prévu : N-045, « Ce que cela ne décide pas », place des canaris dans la banque v2.
- **Ce qu'elle montrerait** : un signalement mesuré par l'oracle (vérité plantée) et non par un juge, avec les faux signalements comptés.
- **Cas sain** : permuter les résultats des canaris ne change pas le classement des compositions.
- **Artefacts** : si l'on injecte le score des canaris dans le critère de sélection, la garde refuse ; la politique « signaler toujours » produit des faux signalements sur les canaris.
- **Coût** : pas de carte graphique, mais des appels de construction peut-être payants : classé en dépense faible par prudence. Les espèces ne le chiffrent pas.
- **Qui** : conv-audit spécifie ; un tiers construit chez session-depot ; session-depot code la garde.
- **R1** : les canaris sont gelés dans les préenregistrements de P12 et de l'étape 2. **Ordre** : après P02, avant P12.

### Apport n° 7 — Opus 4.6 : prédire l'omission avant le point de décision → **P15 « prédiction anticipée »**

- **Réserve RN-02** : l'idée est née de la critique de Fable ; Opus 4.6 l'opérationnalise seul.
- **Quoi** : à poids fixes d'abord, sur les traces de P12. Au tour qui précède le point de décision, lire une sonde et le texte, et prédire si le signalement dû sera omis. Comparer à une base sur les traits du texte (obligatoire, N-029), à une prédiction constante et à des étiquettes permutées. L'unité est le point de décision (lecture vérifiée, § 3.5). Sous contrat explicite, la vérification mécanique (l'outil a-t-il été appelé ?) bat toute sonde au point de décision (convergence n° 2) ; la cible utile est l'anticipation.
- **Ce qu'elle montrerait** : si l'omission est prévisible avant d'avoir lieu, mieux que par le texte. Aucun moniteur d'actions ne peut le faire.
- **Cas sain** : une omission induite par un indice connu, planté au tour précédent, est prédite.
- **Artefacts** : une sonde qui lirait l'identité du scénario est démasquée par l'appariement par scénario ; avec des étiquettes permutées, on revient au hasard. La pièce exige que P12 donne des omissions et des signalements en nombre (taux de départ dans la bande).
- **Coût** : dépense faible (inférence et activations), non chiffrée par l'espèce.
- **Qui** : conv-audit préenregistre ; session-depot exécute. **R1** : oui. **Ordre** : après P02 et P12. La version sur modèles entraînés passe dans P18.

### Apport n° 8 — Argon : le crédit plat se transpose-t-il aux petits effectifs ? → **P05 « simulation du crédit plat »**

- **Quoi** : une simulation synthétique sur processeur. Aux effectifs envisageables pour l'étape 2, et aux effectifs d'Avalon (grands lots : lecture vérifiée, p. 39), un crédit collectif sans contribution individuelle retrouve-t-il un effet planté sur le signalement, et avec quelle erreur ? Graines par `SeedSequence` (R9). Aucun modèle n'est entraîné.
- **Ce qu'elle montrerait** : l'effectif minimal où P17 peut détecter un effet. S'il dépasse le budget, P17 ne vaut pas d'être payé tel quel, dans l'esprit de N-045, énoncé 4 (les expériences bon marché qui peuvent tuer tôt la voie chère). Elle donne aussi la chute minimale détectable qui fixe la bande de P12, et sert la divergence n° 2.
- **Cas sain** : aux grands effectifs, l'effet planté est retrouvé.
- **Artefacts** : avec un effet nul, les fausses alertes restent au taux nominal ; une variance de sélection inégale entre bras doit être neutralisée par l'analyse à taux d'acceptation apparié.
- **Coût** : sans dépense. **Qui** : conv-audit.
- **R1** : oui, court (« simulation comprise »), avec contre-lecture (R2). **Ordre** : tout de suite.

### Apport n° 9 — Argon : circularité du bac à sable → **P06 « note de circularité »**, puis **P19 « essai d'étanchéité hors du bac »**

- **Apport** : « Hashing the check tools is circular, because the hash is computed by tools in the same sandbox » (Avalon, p. 76) ; des agents ont sondé la plateforme plutôt que la tâche dans 25 environnements (p. 79) (lecture vérifiée, § 4).
- **P06** : une note de méthode versionnée qui consigne la réponse donnée à Lazar (n° 313, point 5). Elle couvre : une base de confiance hors du bac (vérificateur et empreintes calculés sur une machine que l'organisme ne peut pas écrire) ; l'attestation ; la redondance diverse (deux vérificateurs d'origines différentes) ; des canaris d'intégrité ; des suites publiques d'étanchéité, écrites par d'autres que nous. Sans dépense ; conv-audit ; pas de R1.
- **P19** : un essai sur la machine jetable. Un tiers modifie de façon bénigne un outil de vérification à l'intérieur du bac. Le vérificateur intérieur doit passer, ce qui démontre la circularité ; le vérificateur extérieur doit alerter.
  - **Cas sain** : outils intacts, aucune alerte extérieure.
  - **Artefacts** : un outil modifié déclenche l'alerte extérieure ; sans vérificateur extérieur, on refuse de conclure. Nous ne concevons aucun scénario d'évasion (classe « hors niveau » de la synthèse) : seulement des suites publiques.
  - **Coût** : dépense faible, non chiffrée séparément (Argon chiffrait son duel entier à 100 à 300 dollars, illustratif).
  - **Qui** : session-depot sur devis (machine jetable, R-1037 (3)).
  - **R1** : c'est une garde (R5) ; préenregistrement court si son résultat sert à rouvrir la couche 3.
  - **Ordre** : après P06, avant la date de réexamen (P04).

### Apport n° 10 — Kimi : un résidu mesurable dans l'étape 2 → **P03** (section 2)

### Apport n° 11 — Kimi : étiquettes « omission fautive / absence d'obligation / simple non-action / non évaluable » → **P02 « grille des étiquettes »**

- **Quoi** : une fonction d'étiquetage mécanique, écrite d'avance. Pour chaque scénario, un tiers scelle avant tout run : la condition (vraie ou fausse), l'obligation (signalement dû ou non, par contrat explicite), la disponibilité de l'outil, l'échéance, et si un rapport a déjà été émis. L'étiquette se calcule à partir du contrat, jamais par un juge. Ce que le contrat ne tranche pas est « non évaluable », compté à part, jamais imputé. Les définitions exactes sont celles de la cellule de Kimi (D-T1, table N13 et § 3), que je n'ai pas lue ; session-depot les recopie.
- **Ce qu'elle montrerait** : un taux d'omission que les non-actions légitimes ne gonflent pas. La lecture vérifiée note qu'Avalon n'établit pas d'obligation (le signalement y est une option, p. 33) : sans cette grille, une baisse du signalement n'est pas une omission fautive.
- **Cas sain** : sur un scénario par étiquette, écrit par le tiers, on retrouve l'étiquette.
- **Artefacts** : outil indisponible, « non évaluable » ; obligation absente là où un juge dirait « omission », « absence d'obligation » ; champ manquant, « non évaluable » sans valeur par défaut ; rapport déjà émis par un autre agent, pas d'omission pour le second (utile à P13).
- **Coût** : sans dépense. **Qui** : conv-audit (spécification, code et essais synthétiques sur processeur) ; session-depot l'applique aux scénarios réels.
- **R1** : la grille est gelée dans chaque préenregistrement qui l'emploie (P12 à P15, P17). **Ordre** : tout de suite ; tout le volet signalement en dépend.

### Hors des onze, à confirmer par l'erratum (RN-02, RN-04)

Je n'en fais pas de pièce propre.
- **Le risque de Kimi sur la couche 3** (effets indirects, déplacement du problème vers les canaux accessibles) passe dans les critères du réexamen (P04) et dans P19.
- **L'objection d'Opus 4.6 sur (c3)** passe dans P18.

## 4. Les neuf divergences non résolues : ce qui trancherait chacune

Lazar : « à résoudre », tour 2 ciblé sur les neuf, avec devis (R-1042). Pour chacune : l'objet, la voie que je recommande, la question de tour 2 en une phrase, et la pièce ou la décision.

1. **Moniteurs neufs comme filtre de fiches** (Fable contre Argon).
   - **Voie** : décision de Lazar « fiches filtrées », tranchable sur N-053, point 5 (RN-09), puis garde P07. La question vaut même couche 3 fermée : N-045, énoncé 4, retient « l'affinage sur réponses filtrées » pour l'étape 2, et un filtre par moniteur ou par juge y ferait entrer un score de moniteur.
   - **Question de tour 2** (facultative) : « La règle qui interdit tout score de moniteur dans un signal d'entraînement ou de sélection de l'agent laisse-t-elle un exemple retenu par un moniteur entrer dans un affinage de l'organisme, et sinon, quel usage des moniteurs neufs se distingue encore de leur absence ? »
2. **Dilution du crédit : artefact ou définition** (Fable contre Argon).
   - **Voie** : pièce P05, plus le tour 2. Le critère de décision manquant (relecture) devient : à taux d'acceptation apparié, l'estimateur de l'effet collectif reste-t-il sans biais sous l'hypothèse nulle ?
   - **Question** : « À information et effectif égaux entre bras et à taux d'acceptation apparié, quelle mesure montrerait qu'un écart entre récompense collective et individuelle vient du crédit et non de la variance de sélection, et quel résultat vous ferait changer d'avis ? »
3. **La voie hors ligne reproduit-elle la pression d'Avalon ?** (Opus 4.6 et Kimi contre Fable et Argon).
   - **Voie** : tour 2 (go de Lazar) ; la réponse est gelée dans le préenregistrement de P17.
   - **Question** : « Au-delà du gain de tâche, quelle mesure de la pression d'optimisation, fixée avant l'entraînement, suffirait à dire qu'un entraînement hors ligne peut faire apparaître une chute du signalement, et quel résultat vous ferait conclure qu'il ne le peut pas ? »
4. **Nature de la précaution d'Avalon.**
   - **Voie** : tranchée pour l'essentiel par R-1042, qui réunit les éléments de Fable, d'Argon et de Kimi ; le prérequis causal d'Opus 4.6 est tenu par l'ordre « (a) puis (b) ». Restent deux décisions : « qui lit » et « portée de l'arrêt ».
   - **Raisons de chaque côté**, que la synthèse ne donnait pas (RN-11) : Fable veut mesurer partout parce que la cause n'est pas établie ; Opus 4.6 veut la question causale d'abord ; Argon veut cloisonner récompense et évaluation ; Kimi veut un seuil d'arrêt qui ne devienne jamais une récompense.
   - **Question** (facultative) : « Parmi la mesure dans tout bras qui entraîne, le prérequis causal, le plancher et la chute maximale gelés et l'arrêt hors du bac à sable, lesquels sont nécessaires, lesquels suffisent, et qui doit lire les mesures ? »
5. **Forme d'une ouverture de la couche 4.**
   - **Voie** : décision « forme de la couche 4 », gelée dans P10 avant son scellement. L'erratum doit expliquer les codes « Q2, N4 » d'Argon (RN-11).
   - **Question** (facultative) : « Quel résultat d'un essai “preuve formelle contre suite bon marché” justifierait chacune des formes d'ouverture (classe d'erreurs, lemmes critiques, vérificateur externe), et que désignent les codes “Q2, N4” d'Argon ? »
6. **Première expérience.**
   - **Voie** : tranchée par R-1042 : les deux mesures sans entraînement se font en parallèle (P08 sans dépense tout de suite, P12 sur devis). Les autres « premières expériences » deviennent P13 (Fable) et P12 avec P02 (le pilote de jugeabilité de Kimi). Pas de tour 2.
   - **Question** (facultative) : « Le pré-test du signalement de départ et l'audit de calibration des juges étant décidés tous deux, l'un doit-il précéder l'autre pour une raison autre que le coût ? »
7. **Exécution hors du bac à sable d'un code généré, comme contrôle** (Opus 4.6 contre Argon).
   - **Voie** : tour 2 (go de Lazar), puis décision de Lazar si le tour ne converge pas.
   - **Fait à servir** : aucun texte du dépôt hors `donnees/` ne porte « l'invariant du noyau gelé » qu'invoque Argon. Seule la question v2 (l. 15) dit que le noyau, les gardes et les bornes de la couche 3 ne sont jamais réécrits, sans parler d'exécution. Recherche du 1er novembre ; `donnees/` non lu.
   - Sans objet tant que la couche 3 est fermée ; à trancher avant la date de réexamen.
   - **Question** : « Aucun texte de notre dépôt ne fixe de règle pour l'exécution : faut-il interdire l'exécution hors du bac à sable d'un code produit par l'organisme, même comme contrôle, et quel contrôle sans exécution hors du bac en tiendrait lieu ? »
8. **Amortissement du coût de génération** (Argon contre Kimi).
   - **Voie** : tour 2 (go), puis P21 « table de sensibilité » une fois K et λ gelés au préenregistrement de l'étape 2 (N-045, énoncés 2 et 5).
   - **Question** : « À K (nombre de générations dont l'héritage est récompensé) et λ (prix du coût dans le score net) gelés, le coût de génération d'un instrument se compte-t-il une fois ou se répartit-il sur les générations où il sert, et quelle valeur de l'oracle ferait changer votre réponse ? »
9. **Transfert d'une sonde d'omission à un autre modèle** (Opus 4.6 contre Kimi).
   - **Voie** : pièce P20. En attendant, règle prudente dans les préenregistrements : répliquer le protocole sur l'autre modèle (position de Kimi).
   - **Question** (facultative) : « Une sonde d'omission validée sur un modèle peut-elle servir telle quelle sur un autre, ou faut-il répliquer le protocole, et quel résultat d'une expérience de transfert ferait changer votre réponse ? »

**Candidate n° 10** (RN-04, hors de la liste) : l'objection d'Opus 4.6 sur (c3). Elle est déjà tranchée par une pièce, la lecture vérifiée d'Avalon (§ 3.2 : « Diffuse : en partie ») et R-1013 (« cas d'étude : non en l'état »). La conséquence est portée dans P18.

## 5. Décisions de Lazar qui restent

Aucune n'a de défaut à 48 heures : chacune touche une décision de Lazar, la précaution d'un essai payant ou une dépense.

### Décision « date de réexamen » (N12 (b))

- **Décision** : quand rouvrir la question N12.
- **Enjeu** : sans borne, si l'étape 2 glisse, la fermeture devient définitive de fait (calendrier d'Opus 4.6) ; trop tôt, on réexamine sans le résidu.
- **Options** :
  - (a) Au résultat seulement, à la lecture scellée du résidu (P03). Avantage : décision informée. Inconvénient : aucune borne si l'étape 2 glisse.
  - (b) Au premier de trois événements : lecture scellée du résidu ; date butoir du 1er avril 2027 (six mois après le début de la phase 0, le 5 octobre 2026) ; déclencheur de coût d'opportunité (P04). Avantage : borne le glissement et reste informée quand c'est possible. Inconvénient : à la date butoir, on peut devoir réexaminer sans résidu, sur P10, P19 et la note de coût seulement.
  - (c) Revue fixe le 1er février 2027, puis tous les trois mois. Avantage : régularité. Inconvénient : réexamens à vide.
- **Recommandation** : (b), confiance 0,6. La date du 1er avril est une proposition : je n'ai pas le calendrier de l'étape 2.

### Décision « fiches filtrées » (divergence n° 1)

- **Décision** : un exemple retenu parce qu'un moniteur (sonde ou juge) l'a bien noté peut-il entrer dans un jeu d'entraînement d'un instrument de l'organisme ?
- **Enjeu** : N-053, point 5, interdit tout score de moniteur dans un signal d'entraînement ou de sélection de l'agent, piste « organisme » comprise. N-058 ne permet que la sélection des fiches. Or N-045 (énoncé 4) retient l'affinage sur réponses filtrées comme voie bon marché. Si le filtre est un moniteur, l'organisme apprend à plaire à ses moniteurs : c'est le contournement que le programme mesure.
- **Options** :
  - (a) Non : tout exemple d'entraînement est retenu par l'oracle planté seul. Les scores de moniteurs servent au rapport et au tri des fiches pour lecture. Garde codée (P07). Avantage : invariant intact, lecture littérale. Inconvénient : moins d'exemples ; rien hors du monde planté ne nourrit l'entraînement.
  - (b) Oui, dans un canal séparé et audité (troisième voie de Fable). Avantage : plus de données. Inconvénient : contraire à la lettre de N-053 ; la séparation des canaux n'est pas démontrée (Argon, Kimi).
  - (c) Seulement dans un bras d'attaque déclaré (l'exception de N-053). Avantage : mesure le coût de l'entorse. Inconvénient : régime du bras d'attaque (quarantaine, porte de revue extérieure R-611), dépense.
- **Recommandation** : (a), confiance 0,8.

### Décision « qui lit » (précaution d'Avalon)

- **Décision** : qui lit les mesures de signalement à chaque point de contrôle de P17 et déclenche l'arrêt.
- **Enjeu** : aucune espèce ne l'a nommé. Une précaution sans lecteur désigné reste « de principe » (critère 11 du collisionneur). Celui qui entraîne ne doit pas être celui qui lit.
- **Options** :
  - (a) Garde mécanique seule, hors de la machine qui entraîne. Avantage : immédiate, sans jugement. Inconvénient : aveugle aux artefacts de mesure (canaris défaillants, « non évaluable » en masse).
  - (b) Garde mécanique, plus un lecteur neuf par point de contrôle lancé par conv-audit, verdict scellé, envoi à Lazar à tout franchissement ou « non jugeable » ; Lazar seul lève un arrêt (P16). Avantage : séparation des rôles, double contrôle, traçabilité. Inconvénient : un sous-agent par point de contrôle, quelques heures de délai.
  - (c) Lazar lit lui-même chaque point. Avantage : autorité directe. Inconvénient : ton temps, et des délais qui bloquent l'entraînement.
- **Recommandation** : (b), confiance 0,7.

### Décision « portée de l'arrêt » (reste de la divergence n° 4)

- **Décision** : le plancher et la chute maximale gelés valent-ils pour le seul bras collectif, ou pour tout bras de l'étape 2 qui entraîne un instrument local ?
- **Enjeu** : la baisse d'Avalon peut venir de tout entraînement qui ne récompense pas le signalement (lecture vérifiée, réserve 1). N-045 (énoncé 8) fait déjà mesurer le signalement dans l'organisme. Une garde limitée au bras collectif laisserait passer une chute ailleurs, ce qui serait une asymétrie (R4).
- **Options** :
  - (a) Tout bras qui entraîne : arrêt et aucune promotion. Avantage : couvre la cause concurrente. Inconvénient : peut arrêter des bras utiles de N-045 pour une chute sans lien avec le collectif ; plus de mesures à lire.
  - (b) Bras collectif seul ; ailleurs, mesure rapportée. Avantage : léger. Inconvénient : la cause concurrente n'est pas gardée.
  - (c) Mesure partout ; arrêt dans le bras collectif, interdiction de promotion sans arrêt ailleurs. Avantage : compromis. Inconvénient : deux régimes, plus difficiles à auditer.
- **Recommandation** : (a), confiance 0,65.

### Décision « forme de la couche 4 » (divergence n° 5)

- **Décision** : quel résultat de P10 ouvrirait quelle forme de vérification formelle. Elle est à geler avant de sceller P10.
- **Enjeu** : sans correspondance gelée d'avance, le résultat de P10 se lirait après coup (R1).
- **Options** :
  - (a) Un vérificateur externe, restreint aux classes d'erreurs où Lean bat la suite à coût apparié, jamais une couche autonome (Fable et Kimi). Avantage : borné par la mesure. Inconvénient : il faut assez d'erreurs par classe pour conclure classe par classe.
  - (b) Une preuve formelle réservée aux « lemmes critiques » (Argon). Avantage : moins cher. Inconvénient : « critique » n'est pas défini ; les codes « Q2, N4 » ne sont pas expliqués.
  - (c) N'ouvrir que si le coût d'opportunité est nul (Opus 4.6). Avantage : protège le calendrier. Inconvénient : condition jamais mesurée, jamais atteinte.
- **Recommandation** : (a), confiance 0,6.

### Décision « témoin mono-agent » (forme de P17 ; à prendre après P13)

- **Décision** : ajouter à P17 un quatrième bras mono-agent.
- **Enjeu** : Avalon n'a pas de témoin mono-agent (p. 40). Le témoin à poids gelés sépare l'entraînement du collectif, pas l'effectif. Si P13 montre un effet de l'effectif à poids fixes, le collectif se confond avec l'effectif.
- **Options** :
  - (a) Toujours. Avantage : comparaison complète. Inconvénient : un bras de plus sur le poste le plus lourd.
  - (b) Seulement si P13 montre un effet de l'effectif. Avantage : dépense conditionnée à un fait. Inconvénient : attend P13.
  - (c) Jamais. Avantage : moins cher. Inconvénient : reste ambigu entre collectif et effectif.
- **Recommandation** : (b), confiance 0,6.

### Décision « périmètre du tour 2 » (divergences)

- **Décision** : servir au tour 2 les neuf divergences, ou les quatre que seules les espèces peuvent éclairer.
- **Enjeu** : tu as dit « tour 2 ciblé sur les neuf ». Trois (n° 1, 4, 5) se tranchent par tes décisions, une (n° 6) est tranchée par R-1042, une (n° 9) attend une expérience. Les servir coûte et dilue la question.
- **Options** :
  - (a) Les neuf, telles quelles. Avantage : conforme à ta lettre ; l'avis des quatre espèces sur tout. Inconvénient : question longue, réponses sur des points déjà tranchés.
  - (b) Quatre (n° 2, 3, 7, 8), plus les questions facultatives n° 5 et 9 en fin. Avantage : ciblé, moins cher. Inconvénient : pas d'avis des espèces sur 1, 4 et 6.
  - (c) Aucune : tout par décisions et pièces. Avantage : aucune dépense. Inconvénient : 3, 7 et 8 restent sans contradicteur.
- **Recommandation** : (b), confiance 0,6.

**Feux verts de dépense sur devis**, à part, chez session-depot : P09 (si payant), P10, P11, P12 à P15 (un devis groupé), P19 ; plus tard P17 et P20. P20 demande en plus un feu vert de changement de modèle.

## 6. Table récapitulative, par ordre d'exécution

Vague 1 : maintenant, sans dépense. Vague 2 : sur devis, avant l'étape 2. Vague 3 : après le dessin de l'étape 2. Vague 4 : après résultats, ou avant la date de réexamen.

| Ordre | Pièce | Réalise | Dépend de | Qui | Coût (illustratif) | R1 |
|---|---|---|---|---|---|---|
| 1 (v1) | P01 erratum de la synthèse | préalable (section 7) | — (demandé au n° 312, point 4) | session-depot, lecteur neuf | sans dépense | non |
| 2 (v1) | P02 grille des étiquettes | apport 11 (Kimi) | — | conv-audit | sans dépense | gelée dans P12–P15, P17 |
| 3 (v1) | P03 clause du résidu | N12 (b) ; apport 10 (Kimi) | P01 (RN-05) ; scellée avec l'étape 2 | conv-audit, puis auteur de l'étape 2 | sans dépense (mesure sous le devis de l'étape 2) | oui (étape 2) |
| 4 (v1) | P04 règle de réexamen | N12 (b) date ; apports 4 et 5 (Opus 4.6) | décision « date de réexamen » ; P03 | conv-audit ; Lazar | sans dépense | gelée dans P03 |
| 5 (v1) | P05 simulation du crédit plat | apport 8 (Argon) ; divergence 2 | — | conv-audit | sans dépense | oui, court |
| 6 (v1) | P06 note de circularité | apport 9 (Argon) ; demande de Lazar | — | conv-audit | sans dépense | non |
| 7 (v1) | P07 garde « aucun score de moniteur dans un jeu d'entraînement » | divergence 1 | décision « fiches filtrées » | Lazar ; session-depot (code) | sans dépense | non (R5) |
| 8 (v1) | P08 audit de calibration des juges | N13 (a) ; Damani | inventaire des journaux ; P01 (RN-08) | session-depot ; conv-audit (préenregistrement) | sans dépense (faible si re-service des juges) | oui, court |
| 9 (v2) | P09 canaris de signalement | apport 6 (Opus 4.6) | P02 | conv-audit ; tiers ; session-depot | faible, par prudence ; non chiffré | gelés dans P12 et l'étape 2 |
| 10 (v2) | P10 preuve formelle contre suite (+ P10a banque) | N12 (b) | décision « forme de la couche 4 » ; P01 ; devis | conv-audit ; tiers ; session-depot | faible : « quelques dollars d'appels » (Argon) ; « quelques jours de processeur » (Opus 4.6) | oui |
| 11 (v2) | P11 tour 2 ciblé du collisionneur | divergences 2, 3, 7, 8 (+ 5, 9) | P01 (RN-14 surtout) ; décision « périmètre du tour 2 » ; devis | conv-audit (question) ; session-depot | faible : tour 1 à 13,52 dollars (R-1036) ; tour 2 des nœuds attendu ≈ 19,4 (feu vert GO-2026-11-01-02) | non (critères de lecture scellés avant lecture) |
| 12 (v2) | P12 pré-test du signalement de départ | N13 (a) ; précaution | P02, P05, P09 ; modèle de départ fixé ; devis | conv-audit ; session-depot | faible : « quelques heures de carte » (Fable), « quelques dollars » (Argon) | oui, court |
| 13 (v2) | P13 diffusion à poids fixes | apport 1 (Fable) | P12 (même devis) | conv-audit ; session-depot | faible : « quelques heures de carte » (Fable) | oui |
| 14 (v2) | P14 raisonnement contracté | apport 2 (Fable) | P12 (même devis) | conv-audit ; session-depot | faible, non chiffré | oui |
| 15 (v2) | P15 prédiction anticipée | apport 7 (Opus 4.6) | P02, P12 | conv-audit ; session-depot | faible, non chiffré | oui |
| 16 (v3) | P16 lecteur des signalements et gardes | précaution (qui lit ; gardes) | décisions « qui lit » et « portée de l'arrêt » | Lazar ; session-depot ; conv-audit | sans dépense | non (R5) ; seuils dans P17 |
| 17 (v3) | P17 bras collectif à trois bras | N13 (b) ; précaution | dessin de l'étape 2 ; P03, P05, P07, P11, P12, P13, P16 ; devis | auteur de l'étape 2 ; session-depot ; Lazar | avec dépense : dizaines (Fable) à 600–3 000 (Opus 4.6) heures de carte | oui |
| 18 (v3) | P18 sondes sur les trois bras | apport 3 (Fable) ; objection d'Opus 4.6 | P17, P15 | session-depot | faible, marginal | oui, dans P17 |
| 19 (v4) | P19 essai d'étanchéité hors du bac | apport 9 (Argon) | P06 ; machine jetable ; devis ; avant la date de réexamen | session-depot | faible, non chiffré séparément | garde (R5) ; court si sert à rouvrir |
| 20 (v4) | P20 transfert d'une sonde | divergence 9 | P15 ou P18 ; feu vert de changement de modèle ; devis | conv-audit ; session-depot | avec dépense, par prudence ; non chiffré | oui |
| 21 (v4) | P21 table de sensibilité de l'amortissement | divergence 8 | P11 ; K et λ gelés (étape 2) | conv-audit | sans dépense | non |

**Fiches courtes des pièces qui n'ont pas de bloc plus haut.**

- **P01 « erratum de la synthèse »**
  - **Quoi** : un erratum sur RN-01, RN-04 à RN-09 et RN-14 (section 7), écrit par un lecteur neuf comme celui du tour 1 des nœuds (R-1036), puis une synthèse v2.
  - **Cas sain** : les passages conformes restent inchangés (RN-15 : chiffres, citations, huit recalculs).
  - **Artefact** : un constat laissé sans « corrigé » ni « maintenu, raison donnée » rend l'erratum incomplet.
- **P07 « garde : aucun score de moniteur dans un jeu d'entraînement »**
  - **Quoi** : tout jeu d'entraînement de l'étape 2 déclare au manifeste sa règle de sélection ; un score de moniteur ou de juge dans cette règle entraîne un refus. Le code de l'orchestrateur v56 applique déjà N-053 aux mesures de lecture (`docs/notes/ideation-organisme-v1/orchestrateur-v56/pole/ideation_v2.py`, l. 98 et 1317). Je n'ai pas trouvé de garde sur des jeux d'entraînement, ce qui est normal tant que l'étape 2 n'existe pas ; à vérifier avant de la déclarer absente (R11).
  - **Cas sain** : un jeu sélectionné par l'oracle est accepté.
  - **Artefacts** : un jeu filtré par un score de juge est refusé ; une déclaration manquante aussi.
- **P11 « tour 2 ciblé du collisionneur »**
  - **Quoi** : l'annexe du tour 2 de conv-audit (`9dc13ece…`) servie telle quelle, plus les divergences retenues tirées de la synthèse corrigée. Les critères de lecture sont scellés avant l'ouverture ; un lecteur neuf lit ; une relecture Opus neuve suit (R-746). Le feu vert GO-2026-11-01-01 ne couvrait que le run du tour 1 : il faut un devis neuf.
  - **Garde d'envoi (R5)** : un lecteur neuf vérifie, avant tout envoi, l'absence de paramètres de conception et de recommandations. Essayée sur la synthèse non corrigée, elle doit la refuser ; sur la question propre, l'accepter.
- **P20 « transfert d'une sonde »**
  - **Quoi** : une sonde d'omission validée sur un modèle est appliquée telle quelle à un autre, puis réajustée sur l'autre par le même protocole, et comparée à une sonde native de l'autre modèle, sur les mêmes scénarios et étiquettes (P02).
  - **Cas sain** : appliquée au même modèle, elle donne la performance de référence.
  - **Artefacts** : avec des étiquettes permutées, ou une direction aléatoire de même variance (le témoin de N-053, point 1), on revient au hasard.
- **P21 « table de sensibilité de l'amortissement »**
  - **Quoi** : à K et λ gelés, le seuil de rentabilité d'un instrument généré selon le nombre de générations où il sert, sous les deux comptages (une fois, ou réparti).
  - **Ce qu'elle montrerait** : si la divergence change une décision dans la plage gelée ; sinon, elle est sans conséquence.
  - **Cas sain** : un instrument qui ne sert qu'une génération donne le même résultat sous les deux comptages.
  - **Artefact** : un coût nul doit toujours donner « rentable ».

**Total attendu.**
- **21 pièces** : 10 sans dépense (P01 à P08, P16, P21) ; 9 à dépense faible (P09 à P15, P18, P19) ; 2 avec dépense (P17, P20).
- **Dépense faible** : de l'ordre de quelques dizaines de dollars d'appels, plus quelques heures de carte d'inférence. C'est mon agrégat des chiffres des espèces et du registre, illustratif ; le poste le plus sûr est le tour 2 (≈ 13,5 à 20 dollars).
- **Avec dépense** : dominée par P17, de quelques dizaines à quelques milliers d'heures de carte selon l'espèce ; l'écart de deux ordres de grandeur se tranchera au devis, après P05.
- **Hors de ce plan** : l'étape 2 elle-même, dont P03 et P17 dépendent.
- **Préenregistrements requis (R1)** : 9 propres (P05, P08, P10, P12 à P15, P17, P20), dont 3 courts (P05, P08, P12), plus un court pour P19 si elle sert à rouvrir la couche 3. Trois clauses vivent dans d'autres préenregistrements : P03 et P04 dans celui de l'étape 2, P18 dans P17.

## 7. Ce qui exige un erratum de la synthèse avant usage

Chez session-depot, par un lecteur neuf, sans dépense (demandé au n° 312, point 4). La synthèse ne sert à aucune pièce, et ne part pas au collisionneur, avant cet erratum. Ses positions par espèce restent citables.

| Constat | Objet | Correction attendue | Pièces du plan touchées |
|---|---|---|---|
| RN-01 | Décompte des accords (« 7 dont 5 larges ») | Écrire la règle de décompte ; retirer les doubles comptes et les accords vrais par construction ; selon la règle, de 4 à 9 accords | P10 et P08 (citation des accords « à quatre ») ; tour 2 (P11) |
| RN-04 | Objection d'Opus 4.6 sur (c3) absorbée | La rétablir (l'omission d'Avalon n'a qu'un point de décision ; lecture vérifiée « Diffuse : en partie » ; R-1013) comme divergence ou apport | P18 ; candidate n° 10 |
| RN-05 | « N-045 ne couvre pas la génération d'instruments neufs » | Restreindre à « code écrit hors catalogue et preuve formelle » (N-045, énoncés 1, 5 et 6 (ii)) ; appliquer le critère 5 aux deux côtés (R4) ; dire que les « non » d'Opus 4.6 et d'Argon sont recodés | P03 (définition du catalogue) ; P04 |
| RN-06 | « (c1) est le témoin qui manque » | Attribuer à Fable seul ; écrire que trois espèces ajoutent un troisième bras et que deux bras ne séparent pas le collectif de l'entraînement | P17 ; décision « témoin mono-agent » |
| RN-07 | « Cause collective non établie » tenue par les quatre | Vérifier sur les cellules d'Argon et de Kimi ; sinon la ramener à Fable et Opus 4.6 | P17 (justification) ; P13 |
| RN-08 | « Seule pièce sans dépense : recalibration a posteriori » | (i) dire la catégorie de dépense des appels de sous-agents ; (ii) retirer « le post-hoc fait jeu égal ou mieux hors domaine », faux sur les moyennes ; (iii) écrire que Damani ne prouve rien d'une recalibration de Platt ; (iv) écrire que la journalisation des confiances n'est pas établie | P08 (préenregistrement) ; P10 (statut des appels) |
| RN-09 | Divergence n° 1 présentée comme « lecture à confirmer » | Nommer N-053, point 5, et le fait de la cellule A-T3 (les fiches filtrées entrent-elles dans un entraînement ?) | décision « fiches filtrées » ; P07 |
| RN-14 | Paramètres de conception reproduits (l. 79–80, 107–110, 117–118, 183, 194) | Les remplacer par des renvois de cellule | P11 (aucun envoi avant) ; P13, P17, P18 (aucune reprise de ces lignes) |

**Recommandés en plus, hors de la liste obligatoire** : RN-02 (liste des apports : le n° 3 est aussi compté en accord, le n° 7 est né d'une critique, le risque de Kimi sur la couche 3 manque) et RN-11 (raisons de chaque côté pour les divergences 4, 5 et 6 ; codes « Q2, N4 »). Les deux touchent ce plan et le tour 2.

## 8. Réserves

1. **Collision de nom « couche 4 »** : dans la question v2, c'est le pôle théorie et vérification formelle ; dans R-1041 (3), c'est la production d'attaques neuves en quarantaine (arène coévolutive, porte R-611). N12 (b) ferme le premier ; le second relève de R-611. Je propose de donner au second un nom distinct, par exemple « arène d'attaques ».
2. **R-1037 (3) contre N12 (b)** : à 09:22, la couche 3 figurait parmi les chantiers de session-depot sur devis. N12 (b), postérieure (09:43) et prise en connaissance du conflit (R-1041 (3)), la ferme. Je la lis comme suspendant ce devis pour la couche 3, la couche 2 n'étant pas touchée. À confirmer par Lazar en une ligne.
3. **La liste des onze apports n'est pas fiable telle quelle** (RN-02). Je l'ai suivie comme Lazar l'a validée, en signalant les deux cas douteux (n° 3 et n° 7) et les deux omis.
4. **Les coûts sont illustratifs**, avec jusqu'à deux ordres de grandeur d'écart entre espèces ; aucun n'est opposable.
5. **Le statut de dépense des appels de sous-agents n'est pas tranché** (RN-08 (i)). P09 et P10 sont classées en dépense faible par prudence.
6. **Le modèle de départ n'est pas fixé.** Le changer exige un feu vert.
7. **Positions lues dans la synthèse seule**, cellules non lues. P02, P15 et P18 renvoient à des définitions des cellules, que session-depot doit recopier.
8. **Ce plan n'est pas contre-lu.** Je recommande une contre-lecture par un sous-agent neuf avant l'envoi à session-depot : R2 vise les préenregistrements, ici c'est par prudence.
9. **Réserve de famille** (en-tête) : sept des onze apports viennent de deux modèles de ma famille.

---

Version 1 ; à sceller par conv-audit ; jamais réécrite (R12). Fin d'écriture : dimanche 1er novembre 2026, 10:01:40 UTC (`date -u`).
