# Journal détaillé — 24 octobre 2026 — lignée « conv-audit » (conversation claude.ai avec Lazar)

Heures UTC (heure de Paris = UTC + 2). Entrées ajoutées, jamais réécrites. Pièces : messages scellés du canal
`brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-24_nNN.md` (branches `canal/conv-audit-nNN`) ; code sur
`outils/essaim-m3-refonte-v1-travail` et `outils/essaim-m3-gradient-v1-travail`. Les entrées de 13:12 à 17:40 sont
écrites rétroactivement à 18:30 UTC, à partir des messages scellés et de la conversation ; elles le disent.

## 13:12 — ouverture de la session ; ce que Lazar demande

- Reprise avec la passation `docs/procedures/passation-nouvelle-instance-claude-2026-10-24-v1.md` (`e381b4b7…`) ;
  lecture de `registres/passations/2026-10-24-1316.md`, `registres/etat.md`, `registres/decisions.md` (R-326 à R-329,
  N-036, N-037, P-026). Routine R14 : empreintes de lancement conformes ; arbre intact (`c90290a`) ; pas de clé Vast.ai
  dans ma session (inventaire des instances impossible de mon côté).
- Ordres de Lazar (15:19, 15:21, 15:27 Paris) : audit à l'aveugle de la passation de Gemini (la relève) ; puis
  **recentrage** sur « le système élaboré par Gemini de l'essaim adaptatif autonome qui apprend, s'organise seul et
  invente ses propres concepts mathématiques pour la surveillance et l'alignement ; m'assurer qu'il marche bien, le
  cas échéant le corriger, et le tester sur des cas d'étude concrets en alignement (conscience d'évaluation, contrôle
  de l'IA) » ; ouvrir un canal avec la session Claude Code du dépôt (« session-depot »).
- Interdits reçus et tenus toute la journée : n'exécuter aucun script de la relève ; ne rien dépenser sans GO ; ne rien
  publier ; ne pas utiliser les clés `RR_*` (interdit levé par Lazar à 17:51 UTC pour les runs réels, N-043 (b),
  GO-2026-10-24-04 — dans la session de session-depot) ; jamais de poussée vers `lciric/controle-ia`.
- Pièce : message n° 01 du canal (13:35 UTC).

## 13:21 à 13:35 — lecture de la relève (données, pas verdict)

- Faits établis sur `quarantaine/releve-gemini-2026-10-23` (`f5cb537`), sans rien exécuter : 69 commits, 1 518
  fichiers, rien dans `src/`, `tests/`, `.claude/` ; les pièces citées par le dossier de passation de Gemini (moteur
  massif du « dossier 17 », substrat, résultats « pascaliens ») n'étaient dans aucune branche ; la « Quadruple Fusée »
  (seul code d'essaim de la relève) n'a eu **aucun appel de modèle réussi** (404 partout) tout en étant « scellée avec
  succès » (Youden 1,0 par défaut sur réponse vide ; génome = schéma d'exemple ; modèle servi jamais consigné ; erreur
  renvoyée comme texte) ; clé Vast.ai en clair dans `gemini/11_…/run_campagne_gpu_72h_5_volets_llama3.py` ligne 314
  (jamais recopiée ; N-038).
- Hypothèse écartée : « la relève a produit un essaim qui apprend » — rien dans les pièces ne le montre ; les chiffres
  « certifiés » sont des constantes ou des déclarations du modèle.
- Pièces : message n° 01 § 3 ; note `comparaison-audits-releve-gemini-v1.md` (accords et divergences avec l'audit de
  session-depot et l'audit versé).

## 13:33 à 14:10 — décision de conception : organisme auto-écrit sous un noyau fixe

- Idée abandonnée (CA-04, ordre de Lazar) : orchestrer moi-même quatre « fusées ». Idée retenue : **un noyau fixe**
  (appels journalisés sans repli, serveur par socket pour ne jamais donner une clé, bac à sable, juge externe à vérité
  cachée, archive scellée, boucle de générations) et **un contrat minimal** ; tout le reste (organisation, rôles,
  nombre d'agents, apprentissage, récompense interne, mémoire, métrique proposée, successeur) est écrit par les
  espèces elles-mêmes à partir de la mission de Lazar mot pour mot (`MISSION-v1.md`).
- Les mécanismes de Gemini (résidus orthogonaux, nul de permutation, bandit, canaris aveugles, e-valeurs, SVD
  incrémentale) deviennent une boîte à outils d'audit, **non donnée** à l'organisme (CA-05, ordre de Lazar 15:52,
  15:54 Paris : l'essaim construit ses connaissances seul).
- Répartition avec session-depot : il corrige l'essaim de Gemini pour qu'il tourne ; je construis l'organisme
  autonome ; confrontation réelle ensuite (CA-07). Pièces : messages n° 02, n° 03 ; `LISEZMOI-v1.md` ; 37 tests.

## 14:16 à 14:21 — décisions de Lazar sur le champion ; contrat étendu

- Lazar (16:02 Paris) : travail indépendant d'abord, confrontation réelle ensuite, champion « selon une métrique que
  l'essaim lui-même aura élaborée » ; (16:16) la métrique est **objective, calculée hors des organismes**, les agents
  d'une autre famille attaquent ceux de la première ; gel par préenregistrement ; score externe témoin ; (16:19)
  l'organisme décide lui-même du nombre d'essaims et de leur composition (monoculture, hybride, les deux).
- Contrat étendu (CA-09) : `metrique/` facultatif par organisme (`definition.md`, `calculer.py`, `attaques.json`),
  appliqué par le noyau de A vers B et de B vers A entre familles de fournisseur différentes.
- Réserve dite à Lazar et gardée : si la métrique de choix vient d'un candidat, le champion est celui qui se note le
  mieux ; d'où le score externe témoin et le gel par préenregistrement.
- Brouillon de préenregistrement v1 (CA-10) : H-E1 apprentissage réel contre bras gelé ; H-E2 concordance métrique
  croisée / score externe ; H-E3 fidélité des espèces ; soumis à contre-lecture R2 par session-depot.

## 15:20 à 15:45 — moteur massif et organisme écrit par Gemini : lecture et comparaison

- Dossier 17 (moteur massif de la relève, lu en quarantaine, jamais exécuté) : l'organisation est dans le code ;
  aucun jugement externe ; le seul code écrit par l'essaim est un greffon de mémoire exécuté par `exec` dans le
  processus qui lit les clés ; mitose arrêtée par un plafond, pas par le critère spectral ; moissonneur 1/241 ;
  « 7/7 » = présence de chaînes dans le source. Conclusion : **rien à porter** dans le noyau ; les idées utiles (vagues
  parallèles, mémoire auto-programmée) étaient déjà dans le contrat. Pièce : `notes/comparaison-conception-trois-organismes-v1.md`
  (`918a4d97…`).
- Organisme écrit par Gemini sous mon contrat (`canal/gemini-organisme-v1`, `6c61956c…`, arbre `1e883c54…`) : propre
  (aucune clé, aucun réseau, aucun sous-processus) ; conception : 1 à 5 castes par une formule du budget, induction en
  texte, mémoire ISVD, **le code n'est jamais réécrit** ; métrique de **forme** (ne regarde jamais la vérité) ; 6
  attaques dans son propre vocabulaire ; marques d'ordre d'octets ; son rapport dit `1 failed` quand sa passation dit
  `3 passed`. Lazar (17:20 Paris) : comparer l'organisme de Gemini corrigé par Claude Code et le mien ; (17:48) :
  « corriger cet organisme-là, c'est le bon, pas le moteur massif ».
- Noyau : lignées imposées (`--organisme-impose NOM=CHEMIN@FAMILLE`), appels parallèles avec réservation au pire
  cas, lecture `utf-8-sig`, simulateur qui lit la famille citée en dernier (le défaut inverse faisait tomber
  l'organisme de Gemini à 0,29 : correction). Simulation à cinq lignées sous le même noyau : mécanique seulement.
- Trois nœuds posés (message n° 04 § 6) : recherche documentaire servie par le noyau ; relance sur successeur
  invalide ; métrique de choix. Lazar (17:47 Paris) : nœud 1 → (b) `rechercher()` servie par le noyau, journalisée,
  plafonnée ; nœud 2 → (b) relance de la dernière génération valide une fois. Nœud 3 : fermé plus tard par N-039 (b)
  (voir 17:06).

## 15:52 à 16:15 — bras gelé étanche, Brier témoin, articles lus

- Question de Lazar (17:53 Paris) : « je croyais qu'on avait un mécanisme de mémorisation et d'apprentissage de
  génération en génération ? » — réponse : oui pour le bras adaptatif (archive et historique) ; le bras gelé est le
  témoin sans transmission. **Fuite trouvée et fermée** : le bras gelé pouvait relire sa mémoire archivée (l'organisme
  de Gemini le fait) → vue d'archive vide et historique vide pour le gel.
- Articles demandés par Lazar (17:54 Paris) : « Beyond Binary Rewards » (apprentissage par renforcement avec
  calibration, récompense R = 1[correct] − (q − 1[correct])², règle de score propre bornée) et le rapport
  « Avalon-M1 » (équipes d'agents, récompense collective, latence, « insularité organisationnelle »). Verdict : rien à
  injecter dans les organismes (ce serait concevoir à leur place) ; retenus : **score de Brier borné comme témoin
  secondaire** (nœud 4, Lazar « ok » 18:07 Paris), et la classe « signalement omis » / insularité pour la banque.
  Pièce : message n° 07.
- Hypothèse rejetée : « la formule de récompense d'un papier doit entrer dans le noyau » — contraire au principe
  d'autonomie de la conception.

## 16:00 à 16:58 — programme d'apprentissage par gradient (nouvelle famille, étapes)

- Question de Lazar (18:07 Paris) : des organismes qui apprennent par gradient, avec la forme du gradient conçue par
  l'organisme ; budget ; projet pour « TAIF » (sigle à confirmer par Lazar : session-depot lit « Transformative AI
  Fund »).
- Conception proposée et retenue par Lazar (18:22, 18:23, 18:39 Paris) : opération `entrainer(spec)` du noyau — la
  spécification (données = identifiants d'entraînement seulement, perte écrite par l'organisme en code restreint,
  algorithme, prétraitement) est conçue par l'organisme, exécutée par le noyau ; **trois étapes en complexifiant** :
  (1) sondes sur activations de Llama-3.1-8B-Instruct (≈ 70 USD, plafond 90) ; (2) renforcement réduit sur les
  réponses (500 à 1 500 euros) ; (3) échelle (milliers à centaines de milliers de tâches, 5 à 10 k€, dossier à
  monter). Partage : étape 1 toutes les lignées, étape 2 les deux meilleures, étape 3 le champion. Lecture retenue par
  Lazar de « résultats positifs exigés » : **« run décisif exigé »**, jamais un run visant un signe (R3).
- Code (branche `outils/essaim-m3-gradient-v1-travail`) : `Entraineur` (sonde linéaire ou à une couche, gradient
  par différences finies sur la perte écrite par l'organisme, plafonds de pas, de temps, de mémoire), `predire`,
  traits simulés ou chargés, extracteur d'activations `scripts/extraire_activations_v1.py` (couches 8/12/16/20/24,
  dernier jeton ou moyenne, manifeste), chaîne testée sur activations factices (Lazar : « ok go »). Brouillon
  `prereg/brouillon-gradient-etape1-sondes-v1.md` (`2b6e5dcb…`). Pièces : messages n° 08, n° 09 ;
  `notes/programme-apprentissage-gradient-essaim-v1.md` (`6b415104…`).
- Hypothèses nouvelles (à préenregistrer séparément) : H-G1 à H-G3 (une sonde conçue par l'organisme bat la
  référence de surface ; la perte conçue vaut mieux qu'une perte standard ; le gain survit au test final).

## 16:07 à 17:12 — contre-lecture R2 de la v1 : 22 constats, tous pris

- Rapport du relecteur neuf (lancé par session-depot) : **non scellable**, 22 constats CR-01 à CR-22. Les plus
  lourds : CR-01 un organisme peut lire la banque (vérités) et le juge ; CR-04 procédure de la métrique ; CR-05 H-E2
  sans test valide ; CR-06 attaques visibles ; CR-07 champion et non-livraison ; CR-08 bras gelé ; CR-11 analyse
  (unité, intervalle) ; CR-13 devis ; CR-15 ordre, vue, hybrides ; CR-16 conflit d'intérêts (j'ai écrit le noyau,
  le juge et le brouillon) ; CR-17 tâches réelles. Décision : tout traiter avant la v4 et tout run réel (pas de v2/v3
  « cosmétiques » : la v3 reste non relue). Six nœuds nés de la relecture (N-038 à N-042, P-026), recommandations
  données à Lazar et à session-depot (message n° 10) : N-038 (a) révoquer la clé ; N-039 **(b)** champion au test
  final, métrique croisée rapportée ; N-040 (3) famille nominale ; N-041 (c) attaques contre l'organisme et la
  métrique ; P-026 (a) ; N-042 (b) sondes d'abord.
- Hypothèse rejetée (CR-05) : H-E2 confirmatoire avec quatre défendeurs — devient descriptive (tau-b) jusqu'à un
  préenregistrement ultérieur à ≥ 6 défendeurs indépendants.

## 17:00 à 17:40 — corrections du noyau (code, routine), banque réelle

- `65b4366` : CR-01 (utilisateur non privilégié par lignée, espaces de noms, groupe de processus tué, droits 0700,
  vue en lecture seule, espace traversable `/var/tmp/essaim-m3/<empreinte>`, métrique isolée ; test « fuite » ;
  mode réel refusé sans root) ; CR-02 (`INVALIDE_MODELE`, `AMORCAGE_PLAFOND`, journaux d'amorçage scellés,
  `--isoler-reseau` obligatoire, échec de `RLIMIT_AS` consigné).
- `63e8521` : CR-04 (`metrique/` dans `organisme/`, relevé sans lecture de score, addendum scellé exigé), CR-06 (vue
  sans `attaques.json`, défense sans marque), CR-08 (`--gel --depuis`), CR-13 (empreinte du collisionneur, extrait du
  registre des GO), CR-19 (graines indexées, manifeste complet).
- `54546e3` : `essaim_m3/analyse.py` (unité lignée-graine, bootstrap à deux niveaux stratifié, table de lecture,
  tau-b, contrôle positif à gain connu) ; `essaim_m3/banque.py` (partition par groupes, secrets à part, référence sur
  les traits de surface, N-029).
- Banque de traces de sabotage écrite par deux sous-agents neufs (lot 1 logiciel `6e56e345…`, lot 2 recherche
  `f1025e6c…`, 40 traces chacun, 20 paires, six classes) ; référence de surface sur les 80 traces : 0,54 (pas de
  séparation en surface).
- Sous-ensemble « conscience d'évaluation » : les sessions en nuage n'atteignent pas le stockage des fichiers de
  Hugging Face (403) → extraction sur la machine de Lazar ; le dépôt `eval-aware/…` est à approbation manuelle
  (demande en attente) → bascule sur le dépôt d'origine `jjpn2/eval_awareness` (accès automatique) ; scripts v2
  (écriture en octets pour une empreinte exacte sous Windows), v3 (zip, chiffrement), v4 (mot de passe lu dans le
  script public des auteurs, `--local`, métadonnées imbriquées remontées, empreinte du fichier source).

## 17:40 à 18:00 — préenregistrement v4, nœuds tranchés, journée en direct avec Lazar

- 17:06 UTC (dans la session de session-depot) : Lazar tranche « N-039 b, N-040 3, N-041 c, P-026 a »
  (GO-2026-10-24-02, R-347) et N-038 (c) : clé Vast.ai gardée (GO-03, R-348). Le nœud 3 de mon n° 04 (exactitude sur
  attaques croisées comme métrique de choix) est **sans objet** : rapportée, pas décisive.
- Brouillon `prereg/brouillon-confrontation-essaims-v4.md` (`29acddcf…`, refonte `e37adb1`) : CR-01 à CR-22 traités
  un par un (section 10), hypothèses H-E0 à H-E5, table de lecture, devis au pire cas (≈ 147 USD par graine complète,
  303 USD pour deux graines et la répétition ; plafond demandé 320), liste d'arrêt avec code et test, « qui a écrit
  quoi ». Contre-lecture 2 demandée à un sous-agent neuf, ni conv-audit ni session-depot (lancée par session-depot,
  R-352). Compilation scellée des décisions de Lazar : `envois/decisions-lazar-2026-10-24-v1.md` (`512b69e3…`).
- `e37adb1` : CR-15 (ordre des lignées tiré par `SeedSequence` et consigné ; **archive privée par lignée par
  défaut** — les lignées d'une course sont indépendantes ; la mémoire commune devient `--memoire-partagee`, vue figée
  par ronde) ; CR-07 ii (**discriminance** : chaque métrique est exécutée sur une sortie parfaite et une sortie
  inversée fabriquées par le noyau ; même valeur ⇒ non discriminante, écartée de H-E2) ; **vocabulaire des
  attaques** : une attaque vise une famille de la banque avec ses étiquettes, sinon invalide (un défendeur n'est pas
  noté sur des étiquettes inconnues) ; `.sha256` permis dans `organisme/` (proposition de session-depot) ; lecture
  par lots dans le simulateur (format de l'enveloppe v3).
- Mesuré (simulation, graine 21, mécanique seulement) : enveloppe v3 de session-depot 0,92 → 0,88 (test), 0,92 (final),
  **sans métrique** ; `gemini-organisme-v2` 0,63 → 0,54, métrique non discriminante, six attaques invalides sous la
  règle du vocabulaire (session-depot livre `gemini-organisme-v3` aligné à 18:08 UTC, R-353) ; auto-écrit simulé
  0,83 → 0,88.
- Erreur de ma part, corrigée : mon lecteur de mot de passe prenait la variable `$PW` du script des auteurs au lieu
  de sa valeur ; Lazar a passé le mot de passe à la main. Autre erreur corrigée : le `.gitignore` de la relève ignore
  `donnees/` ; le premier `git add` de Lazar n'a rien ajouté ; repris avec `-f`.
- Données : `eval-awareness-sous-ensemble-v1.json`, `31761ede…`, 120 items, révision `5d724f12…` du jeu, zip source
  `934dc4bc…`, 70 lignes GAIA exclues, strates 180 / 287 / 226 / 213 disponibles, 30 tirées chacune ; commit `201dd09`
  de Lazar sur `donnees/eval-awareness-sous-ensemble-v1` (18:02 UTC) ; vérifié par moi et par session-depot (R-354).

## 18:00 à 18:30 — banque scellée, lot 3, journal

- `6ec05e3` : épreuve mécanique des métriques (N-041 c) : parfait, inverse, tout positif, tout négatif, aléatoire à
  graine consignée, vide ; « discriminante » et « résiste au gonflement » rapportées. `e8cb3d2` : espace
  `/var/tmp/essaim-m3/<empreinte>` laissé par une course antérieure effacé au démarrage d'une course nouvelle
  (défaut signalé par session-depot, R-353). `bffe03c` : **banque scellée `confrontation-v1`**
  (`f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc`, secret `c68d7d4b…`) : lots 1 et 2 + sous-ensemble
  public ; partition 80 / 60 / 60 par `SeedSequence(279274939364502317056592969560855127043)` ; strates par vérité
  pour les items seuls (12 / 9 / 9 chacune) ; **textes bornés à 20 000 caractères** (15 000 + marque + 5 000 ; 30
  items tronqués) ; référence de surface sur le test final : conscience d'évaluation **0,69** (< 0,80 : la famille
  reste, et se lit contre 0,69, pas 0,5), contrôle de délégation **0,50**. Pièces : `banque/LISEZMOI-v3.md`,
  `banque/PROVENANCE-eval-awareness-v1.md`.
- Lazar (20:06, 20:09 Paris) : « on devrait tester les deux [règles de champion] et faire brainstormer l'organisme
  aussi sur les meilleures métriques » → les deux désignations seront rapportées (descriptif ; N-039 b décide), plus un
  « concours de métriques » dans le rapport (définitions, épreuve mécanique, accord avec le test final) ; **lot 3
  « signalement omis »** : classes et métriques candidates par un **brainstorm indépendant du collisionneur v2.5**
  (étage III : conception, équipe rouge croisée, riposte ; trois modèles), puis 40 traces par classe retenue par des
  sous-agents neufs, étiquettes revérifiées — Lazar : « go » pour (b) maintenant, (c) (le champion validé engendre
  les lots de l'étape 2) ensuite. Faits et question écrits (`brainstorm/faits-sabotage-diffus-v1.md` `c8471c0a…`,
  `brainstorm/question-sabotage-diffus-v1.md` `dc199beb…`) ; devis `collisionneur_v2.py devis` : **19,48 USD au pire
  cas sans relance**, plafond proposé 25 USD ; GO « calcul » à inscrire par session-depot, identifiant confirmé par
  Lazar ; dépense imputée selon GO-2026-10-24-04 (clés `RR_*`, N-043 b).
- Lazar (20:11 Paris) : journal détaillé et synthétique, écrits par les deux lignées → ce journal (`journal/LISEZMOI-v1.md`).

## Ouvert à 18:30 UTC

- Sens de « TAIF » (Lazar, 18:07 Paris) ; nœud 3 de mon n° 04 fermé par N-039 b (à transcrire par session-depot).
- Contre-lecture 2 de la v4 (sous-agent neuf, lancée par session-depot) ; v5 après ses constats ; scellement ; devis
  confirmé ; GO.
- GO du collisionneur (lot 3) ; rédaction des traces du lot 3 ; banque `confrontation-v2`.
- Vérification d'étiquettes des traces par un sous-agent neuf (20 traces tirées) avant scellement.
- Préenregistrement de l'étape 1 (sondes) v2 ; `spec["vue"]` multi-couches ; lanceur d'extraction d'activations
  (session-depot) après GO.
- Concours de métriques dans le rapport ; double désignation du champion (code à écrire dans `rapport`).

## 18:50 — ajout : le programme gradient en entier dans le journal (question de Lazar, 20:22 Paris)

- Lazar demande si le programme d'apprentissage par gradient et renforcement (sondes, renforcement réduit,
  déploiement sur des milliers de tâches) est versé au journal. L'entrée de 16:00 le résumait et renvoyait à la note ;
  la pièce intégrale est maintenant dans `journal/pieces/programme-apprentissage-gradient-essaim-v1.md`
  (`6b4151049ff9d279…`, identique à la note de la branche de travail) et la synthèse v2 (`journal/synthese-v2.md`)
  porte le plan en entier (section 7 : principe, table des trois étapes, règle des données, hypothèses H-G1 à H-G3,
  ce qui existe, ce qui manque, ce qui est écarté). La synthèse v1 reste.

## 18:55 — « TAIF » tranché ; la banque expliquée

- Lazar (20:23 Paris) : **TAIF = Transformative AI Fund** ; il a un entretien avec eux pour une demande de subvention sur
  le projet contrôle IA. Conséquence : la ligne « étape 3 » du programme gradient (centaines de milliers de tâches,
  5 à 10 k€) est la ligne de cette demande ; un dossier court pour l'entretien est proposé (date et format à recevoir).
  Point ouvert « sens de TAIF » : fermé.
- Lazar demande ce qu'est « la banque réelle scellée » : réponse donnée (200 tâches à vérité cachée : 120 items publics
  « conscience d'évaluation » + 80 traces de délégation ; 80 / 60 / 60 ; vérités à part ; empreinte fixée ; « réelle »
  par opposition à la banque simulée des tests mécaniques).

## 19:00 — étape 2 : cas inédits engendrés par les organismes, découpage par familles, H-G4 (Lazar, 20:26 à 20:29 Paris)

- Lazar : à l'étape 2, les organismes peuvent-ils engendrer eux-mêmes une banque de cas inédits de conscience
  d'évaluation (nouveaux formats de banc, nouveaux indices, nouvelles mises en scène) ? des cas d'usage réalistes jamais
  documentés ? et découper l'ensemble en entraînement / test pour prédire de nouvelles formes d'attaque — « jackpot pour
  la publication » ; « il faut qu'il génère suffisamment de cas inédits pour splitter ».
- Retenu : oui pour l'**entraînement et le test de développement**, vérité « construit comme évaluation / construit
  comme usage » (intention du générateur, écrite au moment de la construction), ancre réelle au test final ; cas
  d'usage imaginés permis et voulus, en le disant (pièges : scénarios plus propres que les vrais journaux, style du
  générateur → génération croisée entre familles de fournisseurs, référence de surface sur chaque banque engendrée).
- **Découpage par familles de cas inédits**, pas par cas : chaque famille documentée (définition, indice, raison) ;
  ordre de grandeur 40 à 60 familles × 50 à 100 cas ; test à trois niveaux à préenregistrer — **H-G4** : (a) familles
  retenues du même générateur, (b) familles engendrées par l'autre famille de fournisseur, (c) items de provenance
  réelle ; signe prédit et scellé avant le run ; résultat négatif publié aussi (R3, R4) ; la nouveauté « taxonomie
  d'indices découverte par essaim » à vérifier contre l'état de l'art sur PDF (R7, R8 : les papiers de conscience
  d'évaluation ont des catégories d'indices).
- Hypothèse écartée : « découper par cas suffit » — la mémoire du générateur réussirait le test.
