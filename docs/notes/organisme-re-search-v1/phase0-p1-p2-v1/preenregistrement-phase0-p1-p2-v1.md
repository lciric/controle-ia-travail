# Préenregistrement — phase 0 de P1 (le monde planté répond) et de P2 (répétition des formes contre une référence tirée dans la grammaire), organisme d'idéation, v1

**Ce texte remplace un brouillon non scellé du même nom, écrit par deux instances en parallèle (fichiers du dossier modifiés entre 04:56 et 05:03 UTC d'après leurs dates sur disque) ; ce brouillon n'a été ni scellé, ni versé, ni exécuté sur les vraies mesures.** Depuis la reprise, le modèle I est l'auteur unique de ce texte, des quatre modules et des essais du dossier, et les assume en entier ; personne d'autre n'écrit dans ce dossier. Reprise commencée à 2026-11-18T05:06:24Z ; ce texte achevé à 2026-11-18T05:16:52Z (`date -u`, jamais écrit à la main).

Gabarit suivi : `prereg/gabarit-preregistrement-v1.md` (8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e), sections dans son ordre, plus les sections propres à cette tâche (hors table ; ce que la phase 0 ne dit pas ; écarts et choix ; ce qui a été vu avant scellement ; lancement).

- Auteur : modèle I (développeur unique de la phase 0, session du compte organisme).
- Date (UTC) : 2026-11-18, heures ci-dessus.
- Statut : **rien n'est exécuté sur la configuration de ce texte**, **rien n'est adopté dans l'organisme**, la note de conception de la suite reste suspendue. Aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau. Aucune hypothèse ni revendication du programme n'est changée.
- Commit du code d'analyse : ce texte, les quatre modules et les essais sont versés ensemble, au même commit, sur la branche `lot/compte-organisme-v1` ; ce texte est scellé d'abord, son empreinte est ensuite posée dans le lanceur, puis le code est scellé (compagnons `.sha256`). Le lanceur écrit le commit exact au manifeste (`git rev-parse HEAD`) et refuse de partir si l'empreinte de ce texte n'est pas celle qu'il porte.
- Code (dossier `docs/notes/organisme-re-search-v1/phase0-p1-p2-v1/`, noms neufs, R12) : `mondes_reponses_p1p2_v1.py` (grammaire et tirage des lois, évaluation vectorisée, sondes, prédicats, répondeurs, formes, validation d'une carte) ; `questionneurs_p1_v1.py` (espace des candidates, questionneurs factices, partie, ordre de présentation, statistiques) ; `mesure_forme_p2_v1.py` (forme, règle M2, références, quota, M4) ; `lanceur_phase0_p1p2_v1.py` (gardes, application des critères gelés, manifeste) ; essais `test_phase0_p1p2_v1.py`.
- Documents qui font foi et pièces lues (empreintes recalculées à la rédaction, sceaux vérifiés) :
  - propositions `docs/notes/organisme-re-search-v1/propositions-conception-re-search-v1.md` (2b882f8d02d2953072c30a977cd5011eb36810b5f9083617c5d35de80d50f42e), sections P1, P2, « Ce qui borne toutes les propositions », récapitulatif des devis ;
  - contre-lecture `contre-lecture-re-search-organisme-v1.md` (f81c778d2fa1c08ab8f56f452b407cbf9afb0eb2cef3a0ffa91129f241c90c24) : constats P-1 à P-4 et A-1 à A-3, qui s'imposent ici (P-5 à P-8 et A-4 lus et pris en compte) ;
  - analyse `analyse-journaux-re-search-v1.md` (8a82b5ee1eb709ac752212a40fc181b7a7c236c4b5c5dfa0315825bfb3ae08bc) et son programme `analyse_journaux_re_search_v1.py` (3abb28aacf2f1cee5d0d97a9dd7e8993f1d54dbeb6bcdfb6780322e4b533c8ed) : définition de la forme, règle M2, règle M4, structure des sources ;
  - dépôt public de l'organisme, lecture seule, commit a41b7b5 : `README.md` sections 2 et 3 (04ac692e9500dd3793b214f7aa579706b5d963868f86ae4290cce49f44afbea0) ; `orchestrator/pole/evaluateur_lois_v62.py` (26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632), sémantique des six types ; `monde_noyau.py` (b2aaf3958525e399f0c6453eace41550146327623f95578d64e158bb13e8cae0) et `monde_banque.py` (33088eb9088549a20ffd489687928a1f1469d1df85a025db29bc9ce3f93e7b18) : ni l'un ni l'autre ne porte de générateur de lois (le premier rend la loi d'une fiche ou sa marginale aveugle, le second lit une banque figée), d'où la grammaire de tirage écrite ici ;
  - sources des mesures, **lues seulement au lancement, par le lanceur**, empreintes vérifiées (recalculées à la rédaction sans ouvrir le contenu) : course v67 `/home/user/ideation-organism/resultats/course-v67/poste-local-v1/boucle-reelle-v66.json` (21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71) ; en **description seulement**, les propositions des deux attaques de Goodhart, copies en lecture seule sous le dossier `scratchpad/goodhart/` de la session : `attaque-goodhart-v3.json` (e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505) et `attaque-goodhart-v5.json` (cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf), empreintes conformes à l'inventaire `goodhart-inventaire-v1.txt` (b9cc703dc35024b6f757d011a8946f575c08cb45219d38eddb6704e2f4e71f47) ; lecture permise par l'accord écrit de la mère R-3157 ; le lanceur inscrit chaque fichier ouvert, avec son empreinte, au journal des fichiers ouverts du run.
- Conventions : aucun nom de modèle de la famille du rédacteur ; développeur « modèle I », contre-lecteur « modèle J ». Les proposeurs de nos journaux sont nommés comme dans l'analyse (argon, kimi).

## Bloc « effort et échantillonnage gelés » (conditions de la mère R-3186, P1 a)

Budget de questions, nombre de mondes, tailles des sondes et de l'espace, tirages, bras, règle des refus et quotas sont gelés ici et au manifeste du run. Le lanceur recalcule l'empreinte du bloc (JSON canonique de `bloc_effort(CONFIG)`) et **refuse de partir si cette empreinte n'est pas écrite dans ce texte** :

**Empreinte du bloc « effort et échantillonnage gelés » : 2df0dadb03ebe3f042858cef5ac5f418501b92db1aeefe00b1e586672a825d0c**

```
{
 "p1": {
  "bras_hasard": [
   "aleatoire",
   "bissection"
  ],
  "bras_inverse_10": [
   "aleatoire",
   "bissection"
  ],
  "bras_principal": [
   "aleatoire",
   "aleatoire#2",
   "aleatoire#ordre",
   "bissection",
   "bissection#2",
   "bissection#ordre",
   "repeteur",
   "repeteur#ordre",
   "disperseur",
   "oracle"
  ],
  "bras_structurelle": [
   "aleatoire",
   "bissection",
   "repeteur",
   "disperseur"
  ],
  "mondes": 200,
  "points_de_carte": [
   0,
   4,
   8,
   16
  ],
  "politique_refus": "arret",
  "predicats_principaux": 42,
  "predicats_structurels": 51,
  "questions_T": 16,
  "sonde_questions": 2048,
  "sonde_score": 256,
  "taille_espace_H": 65536,
  "taux_inversion_artefact": 0.1,
  "tirages_bootstrap": 10000
 },
 "p2": {
  "quota_plage_sensibilite": [
   1,
   2,
   3
  ],
  "quota_principal": 2,
  "tirages_reference": 10000,
  "tirages_reference_m4": 1000
 },
 "proposeurs_reels": "aucun en phase 0 (questionneurs factices) ; réglages des proposeurs de la phase 1 (effort de raisonnement, température, plafond de jetons, nombre de parties) à geler au manifeste de la phase 1, avant tout appel",
 "racine_graines": 20261118
}
```

Sens : racine des graines 20261118 ; P1 : 200 mondes, |H| = 65 536, T = 16 questions par partie, cartes à 0, 4, 8 et 16 questions, sonde des questions 2 048 instances, sonde de score 256, 42 prédicats (variante principale) et 51 (structurelle), inversion de 10 %, 10 000 rééchantillonnages, refus sous la règle « arrêt » ; P2 : 10 000 tirages de référence, 1 000 pour M4, quota principal 2, plage {1, 2, 3}. Les proposeurs réels n'ont aucun réglage en phase 0 ; ceux de la phase 1 (effort de raisonnement, température, plafond de jetons, nombre de parties) seront gelés au manifeste de la phase 1, avant tout appel, par le même mécanisme et sous un préenregistrement propre.

## Hors table : P1 lève un indécidable, l'écart est déclaré (conditions de la mère R-3181 ; constat P-1)

La table de décision attache chaque essai à une ligne qui change. **P1 répond à la ligne C5, restée indécidable** ; selon le constat P-2 de la contre-lecture, la lettre de C5 penche même vers « ne change pas », le répondeur étant le maillon le mieux validé de l'article. P1 n'est donc pas ouvert par la règle fixée d'avance : **c'est un essai hors table, pour lever un indécidable, et cet écart est déclaré ici.** Sa phase 0 ne coûte rien et ne décide rien pour l'organisme : elle dit seulement si l'instrument du monde répondeur ordonne des questionneurs de qualité connue. Ouvrir la voie, et toute phase 1 (payante, pire cas 267,84 USD dans la proposition, à refaire selon P-4 et P-6), reste la décision de Lazar. **P2**, lui, découle d'un verdict « change » de la table (ligne C3), qui ne tient qu'à la lettre (A-1) ; sa phase 0 peut refermer cette ligne, jamais la rouvrir.

## Hypothèse

**H-P1 (validité de l'instrument du monde répondeur).** Sur des mondes plantés tirés dans la grammaire fermée des lois de l'organisme, où le monde répond lui-même, par le code, Oui ou Non à des questions fermées sur sa loi, la divergence finale entre la carte et la loi du monde ordonne des questionneurs factices de qualité connue d'avance (bissection meilleure qu'aléatoire, aléatoire meilleur que répéteur) ; deux copies du même questionneur (graines différentes) ne se distinguent pas, et l'ordre de présentation des prédicats et des traits non plus, avec des intervalles assez étroits, rapportés à l'écart entre les questionneurs bornes (aléatoire, bissection), pour que cet écart soit lisible. Aucun juge n'intervient : la vérité du monde planté seule (N-058). Renvoi : proposition P1, phase 0 ; ligne C5 de la table (hors table).

**H-P2 (référence de construction de la répétition des formes).** La part de cartes qui répètent une forme déjà proposée dans la course v67 (9 sur 23, 0,391304, règle M2 de l'analyse) peut être atteinte par la seule petitesse de la grammaire. Si des cartes tirées au hasard dans la grammaire, aux mêmes emplacements et sous la même règle, répètent une forme dans plus d'un quart des cas (médiane des tirages), le « mode dominant » de S1 est un effet de la grammaire et la ligne C3 se referme. Renvoi : proposition P2, phase 0 (a) et (b) ; constats A-1, A-2, A-3, P-8.

Hypothèses de travail (déclarées, non vérifiables ici) : la grammaire de tirage écrite ici représente la grammaire servie aux proposeurs (non lue) ; la règle de carte commune (médoïde) isole l'effet du choix des questions.

## Prédiction chiffrée et signe attendu

- **P1.** À T = 16, signes attendus : aléatoire − bissection > 0 et répéteur − aléatoire > 0, pour la différence des médianes et pour celle des moyennes ; A/A et ordre de présentation : écarts ≈ 0, intervalles de largeur inférieure à la moitié de l'écart aléatoire − bissection. Ordre de grandeur : non prédit à cette échelle. Confiance : ≈ 80 % pour bissection contre aléatoire ; **≈ 55 % seulement pour répéteur contre aléatoire** (sur les petits mondes d'essai, ce signe n'était pas stable d'une série de graines à l'autre, section « Ce qui a été vu ») ; ≈ 65 % pour la famille A/A entière (trois comparaisons, critère de largeur exigeant). Réfutation de H-P1 : un des deux écarts d'ordre dont l'intervalle n'exclut pas 0 (pour l'une ou l'autre statistique) ou de signe inverse ; ou une comparaison de la famille A/A non conforme.
- **P2.** Aucune prédiction de signe forte : médiane de la référence R1 attendue entre 0,15 et 0,35 (la grammaire de tirage compose beaucoup de formes, mais fixe et softmax n'ont chacun qu'une forme). Ce qui compterait comme réfutation de H-P2 (« la grammaire suffit ») : médiane R1 au plus 0,25.

## Métrique

**P1.**
- Monde : une loi de l'espace H tirée sans remise (200 mondes, un par partie, frais) ; H = 65 536 = 2^16 lois candidates tirées une fois dans la grammaire, disjointes des lois de référence de production (garde ci-dessous). Le questionneur connaît H, jamais l'indice du monde.
- Questions : grammaire fermée de prédicats, écrite avant tout monde (`grammaire_predicats`). Variante principale **empirique** (42) : pour chaque trait j ∈ {0, 1}, issue a ∈ {0, 1, 2} et seuil s ∈ {−1 ; −0,5 ; 0 ; 0,5 ; 1}, « P(a | z_j > s) > P(a | z_j ≤ s) » (30) ; pour chaque issue, « P(a | g = 1) > P(a | g = 0) » (3) ; pour chaque issue et c ∈ {0,2 ; 1/3 ; 0,5}, « P(a) > c » (9) ; probabilités moyennées sur une sonde des questions fixe de 2 048 instances (z ~ N(0, 1)², g ~ Bernoulli(1/2)). Variante **structurelle**, rapportée à part (51) : les 42, plus « la racine est de type t » (6) et « la loi dépend de z0 », « de z1 », « de g » (3). Réponse Oui ou Non calculée par le code sur la loi du monde.
- **Ordre de présentation (conditions de la mère R-3186, P1 b)** : à chaque partie, la permutation des prédicats présentés au questionneur et l'ordre des deux traits (z0 puis z1, ou z1 puis z0) sont tirés par la graine dérivée de la partie (rôle « ordre ») ; le questionneur choisit une position dans l'ordre présenté, le monde répond au prédicat qu'elle désigne. Le répéteur et le disperseur suivent l'ordre présenté des traits.
- Carte : à 0, 4, 8 et 16 questions, médoïde de l'ensemble S_t des candidates qui contredisent le moins de réponses (règle commune). **La carte à zéro question est écrite et rapportée pour chaque questionneur** (conditions de la mère R-3186, P1 d ; constat P-7) : médoïde de H, la même pour tous, sauf l'oracle (artefact).
- Score (M-P1a) : KL(loi du monde ‖ carte), moyenne sur une sonde de score fixe de 256 instances, en nat ; en information, carte exacte et égalité de forme. Aucune note d'un modèle.
- **Statistiques gelées (défaut de la masse en 0)** : chaque comparaison est une différence appariée par monde, calculée par **deux statistiques sur les mêmes 10 000 rééchantillonnages des mondes** : différence des **médianes** (lettre de la proposition) et différence des **moyennes**. Raison : quand plus de la moitié des parties d'un bras recouvrent le monde exactement (divergence nulle), la médiane vaut 0 et ne voit pas une dégradation, même massive, qui ne touche qu'une minorité de mondes (vu sur les petits mondes d'essai sous inversion de 10 % des réponses ; essai `test_masse_en_zero_la_mediane_ne_voit_pas_la_moyenne_voit`) ; la moyenne la voit. **Règle** (section « Seuil ») : les critères d'ordre, d'A/A et de disparition exigent les deux statistiques ; le critère de dégradation (inversion) est jugé sur les moyennes seules, la médiane y étant rapportée sans décider. Intervalles : quantiles empiriques 2,5 % et 97,5 % (méthode `inverted_cdf`) ; pour la famille A/A, intervalle corrigé de Bonferroni sur trois comparaisons (quantiles 0,05/6 et 1 − 0,05/6) pour le « contient 0 », et intervalle à 95 % pour la largeur.
- Mesures rapportées sans décision : M-P1b rendement par question, précoce ((KL0 − KL4)/4) et tardif ((KL4 − KL16)/12), médianes (constat P-7) ; M-P1c information par question (log2 du rapport des tailles successives de S_t) ; M-P1d part des questions de même direction que la précédente, nombre de couples (direction, issue) ouverts, questions reposées ; M-P1e temps processeur par partie (coût : 0 USD) ; A/A de la bissection ; ordre de présentation du répéteur ; disperseur contre aléatoire ; variante structurelle ; dispersion de l'écart A/A sur 8 mondes (taille de la phase 1 proposée), rapportée à l'écart aléatoire − bissection (information pour P-3, sans décision).

**P2.**
- Forme d'une loi : définition de l'analyse, figée : arbre JSON de la loi, chaque feuille numérique (réel, entier) remplacée par un jeton unique ; types, noms de clés et longueurs de listes gardés. Sensibilité A-3 : feuilles entières gardées.
- Part (règle M2 de l'analyse, figée) : une carte répète une forme déjà proposée si sa forme figure parmi les cartes d'une génération antérieure, ou plus haut dans la liste du même proposeur à la même génération (ordre des identifiants) ; part = cartes qui répètent / cartes.
- **Cartes hors softmax (conditions de la mère R-3186, P2 b ; A-1)** : la part est calculée et rapportée **avec** les softmax (toutes les cartes, base de la décision, lettre de la proposition) **et sans** (cartes non softmax qui répètent / cartes non softmax), observée et en référence (HS) ; la décision est prise sur toutes les cartes, et toute divergence entre les deux lectures est écrite par le code comme réserve A-1 (section « Critères »).
- Référence : mêmes emplacements (génération, proposeur, identifiant) que les 23 cartes, chaque loi remplacée par un tirage dans la grammaire, même règle ; 10 000 tirages ; médiane, quantiles 2,5 % et 97,5 %, part des tirages au moins égale à l'observée.
- **Quota (option iii) rejoué hors ligne, sans vérité (conditions de la mère R-3186, P2 a)** : nombre de cartes qu'un quota de q cartes d'une même forme par proposeur et par génération refuserait (au-delà de la q-ième, ordre des identifiants), toutes cartes et hors softmax. **q = 2 fixé à l'écriture de ce texte sans lire l'oracle, aucun verdict ni les 23 cartes** (une carte et un raffinement d'une même forme par proposeur et par génération) ; **plage de sensibilité gelée {1, 2, 3}** ; le code ne passe au rejeu que les champs génération, proposeur, identifiant et loi (projection), refuse tout q hors de la plage. Description seulement : aucune décision.
- M4 (suites des deux attaques de Goodhart, **description seulement**) : dans une suite, part des propositions dont la forme figure plus tôt dans la même suite (règle de l'analyse) ; référence R1 aux mêmes longueurs, 1 000 tirages ; avec et sans softmax.
- **Aucune nouveauté (conditions de la mère R-3186, P2 d)** : aucune « nouveauté » n'est attribuée à une forme du seul fait qu'elle est absente de l'archive ou des cartes antérieures ; « ne répète pas » veut dire seulement « forme non vue plus tôt au sens de M2 ». La sortie porte cette mention (`aucune_nouveaute`) et aucune autre clé qui parle de nouveauté (essai).

## Seuil

- **C-P1-1, ordre** : pour chacun des deux écarts (aléatoire − bissection ; répéteur − aléatoire) et pour **chacune des deux statistiques** (médianes, moyennes), point et borne basse de l'intervalle à 95 % strictement positifs. Conjonction (intersection-union) : aucune correction de multiplicité requise.
- **C-P1-2, famille A/A (conditions de la mère R-3181 et R-3186, P1 b)** : trois comparaisons appariées, aléatoire copie 2 − aléatoire (A/A), aléatoire sous un autre ordre de présentation − aléatoire, bissection sous un autre ordre − bissection (même graine de questionneur, seule la graine de l'ordre change). Pour chacune et pour chaque statistique : l'intervalle corrigé de Bonferroni (niveau 1 − 0,05/3) **contient 0**, **et** la largeur de l'intervalle à 95 % est **strictement inférieure à 0,5 ×** l'écart ponctuel aléatoire − bissection de la même statistique, mêmes mondes (écart entre les questionneurs bornes ; un écart nul ou négatif fait échouer la largeur). L'A/A propre est la première comparaison ; les deux autres forment le critère d'ordre de présentation.
- **C-P1-3, inversion de 10 % des réponses (artefact)** : borne basse de l'intervalle à 95 % de moyenne(KL bissection sous inversion) − moyenne(KL bissection exacte) strictement positive.
- **C-P1-4, répondeur au hasard (artefact)** : borne basse de aléatoire − bissection ≤ 0 pour les deux statistiques.
- **C-P1-5, fuite** : part des mondes recouverts exactement à zéro question > 0,05 pour l'oracle (doit être signalé), ≤ 0,05 pour chacun des autres bras (hasard : 1/65 536 par monde) ; divergence de l'oracle nulle à chaque point de carte.
- **C-P1-6, refus** : aucun refus hors grammaire sur l'ensemble des parties (questionneurs factices : un refus est un défaut du code).
- **P2** : la médiane de la référence R1 (forme principale, toutes cartes) **dépasse strictement 0,25** → la ligne C3 se referme. Parts possibles : multiples de 1/23 ; 0,25 n'est pas atteignable, aucune égalité au seuil.
- Taux d'erreur visés : 0,05 par intervalle ; famille A/A à 0,05 au total pour le « contient 0 » (Bonferroni) ; sous un instrument parfait, la probabilité qu'une des trois comparaisons échoue au « contient 0 » est donc au plus 0,05.

## Plan d'analyse

**Grammaire de tirage des lois, écrite exactement (conditions de la mère R-3186, P2 c ; constat P-8).** Loi de tirage R1 (`tirer_loi`) : type de chaque nœud **uniforme sur les six types** (fixe, softmax, melange, si_sinon, par_sous_population, transformee), sauf à la profondeur 2 (racine à 0) où il est uniforme sur {fixe, softmax}. Paramètres : fixe, probas ~ Dirichlet(1, 1, 1) ; softmax, poids 3 × 2 i.i.d. ~ N(0 ; 1,5²), biais 3 i.i.d. ~ N(0 ; 1) ; melange, nombre de composantes m uniforme sur {2, 3}, poids ~ Dirichlet(1, …, 1) de dimension m, composantes tirées selon R1 à la profondeur suivante ; si_sinon, avec probabilité 1/2 condition sur un trait (indice uniforme sur {0, 1}, seuil ~ N(0 ; 0,5²)), sinon sur la sous-population (valeur uniforme sur {0, 1}), branches « si » et « sinon » tirées selon R1 ; par_sous_population, lois « 0 » et « 1 » tirées selon R1, sans défaut ; transformee, base tirée selon R1, et sous-ensemble non vide des quatre opérations uniforme sur les 15 (masque entier uniforme sur 1…15 : bit 1 melange_aveugle avec λ ~ U(0,05 ; 0,5) et probas ~ Dirichlet(1, 1, 1) ; bit 2 puissance ~ U(0,5 ; 2) ; bit 4 inclinaison 3 i.i.d. ~ N(0 ; 1) ; bit 8 oscillation avec amplitude ~ U(0,2 ; 1,5), fréquence ~ U(0,5 ; 3), trait uniforme sur {0, 1}, phase ~ U(0 ; 2π), issue uniforme sur {0, 1, 2}). Variantes rapportées : **R2**, type de la racine aux fréquences des types observées dans les 23 cartes (comptées par le lanceur au lancement), enfants selon R1 ; **HS**, emplacements non softmax seulement, racine uniforme sur les cinq autres types, enfants selon R1 ; **SEQ**, suite de 23 tirages R1 sans structure de générations (part = 1 − formes distinctes / 23). Sémantique des lois : celle de `evaluateur_lois_v62.py` ; la réécriture vectorisée lui est égale à 1e-12 près sur 200 lois tirées couvrant les six types (essai).

**P1, déroulement.** (1) Sondes des questions (2 048) et de score (256). (2) Lois de référence de production : les lois `plantees` et `cartes` de la course v67, évaluées par l'évaluateur de l'organisme (lecture seule) ; garde de disjonction : toute loi tirée pour H à 0,30 nat ou moins (divergence moyenne dans un sens ou l'autre) d'une loi de référence est retirée et comptée (seuil de la mémoire de l'organisme, selon les propositions). (3) Espace H de 65 536 lois. (4) 200 mondes tirés sans remise dans H. (5) Bras joués sur les mêmes mondes : **principal** (répondeur exact, variante empirique) : aléatoire, aléatoire copie 2, aléatoire sous un autre ordre, bissection, bissection copie 2, bissection sous un autre ordre, répéteur, répéteur sous un autre ordre, disperseur, oracle ; **inversion de 10 %** : aléatoire, bissection ; **répondeur au hasard** : aléatoire, bissection ; **structurelle** : aléatoire, bissection, répéteur, disperseur. Questionneurs : aléatoire (uniforme sur les positions non posées) ; bissection (entropie maximale du partage de S_t, égalités tirées) ; répéteur (toujours le premier trait présenté ; ses 15 prédicats reposés une fois épuisés) ; disperseur (directions prises à tour de rôle — traits dans l'ordre présenté, puis g, marginale [, racine] — jamais deux fois de suite la même tant qu'une autre reste) ; oracle (artefact : carte = monde). Budget : T = 16 questions par partie, **sans arrêt au premier succès**. (6) Critères ci-dessous, appliqués par le code, puis lus par un lecteur neuf (R13).

**Règle des refus et des questions sans réponse, fixée d'avance (conditions de la mère R-3186, P1 c).** Une question hors grammaire (indice hors de la liste, non entier, booléen) ou absente (le questionneur ne pose rien) est **refusée et comptée** ; elle n'est **jamais répondue « Inconnu »**. Phase 0 (questionneurs factices, règle « arrêt ») : un refus est un défaut du code, la partie s'arrête par une exception nommée et P1 est arrêtée et rapportée (C-P1-6). Phase 1 (proposeurs réels, règle « question perdue », déjà écrite dans le code) : la question refusée consomme une unité du budget et ne reçoit **aucune réponse** (aucune mise à jour de S_t ; ni Oui, ni Non, ni Inconnu). Une question déjà posée est répondue de nouveau, consomme le budget et est comptée (questions reposées). Une réponse qui n'est pas exactement un booléen est refusée (garde de fuite). En phase 1, une **carte** absente, illisible ou hors grammaire est refusée, comptée et remplacée par la loi fixe uniforme (1/3, 1/3, 1/3), jamais par la médoïde de H ni par une carte antérieure (`carte_du_proposeur`).

**Décision écrite sur l'effet de l'ordre de présentation (conditions de la mère R-3186, P1 b), avant toute phase 1.** L'effet est mesuré dans la famille A/A (C-P1-2). S'il tient (les deux comparaisons d'ordre conformes) : l'ordre est déclaré sans effet mesurable à la précision de l'instrument ; en phase 1 il reste tiré par graine dérivée à chaque partie, jamais fixé, les deux parties A/A d'un proposeur ont des ordres différents, et l'effet n'est pas modélisé. S'il ne tient pas : verdict « instrument sensible à l'ordre de présentation », **aucune phase 1** sous cet instrument ; rapporté tel quel.

**P2, déroulement.** (1) Lecture des 23 cartes de la course v67 (`releve.cartes`), forme et règle M2 ; **garde de reproduction** : 9 répétitions sur 23 exigées (chiffre de l'analyse, `S1.M2`), sinon arrêt de P2. (2) Parts observées : toutes cartes, hors softmax, entiers gardés ; décompte par type. (3) Références R1, R2, HS, SEQ, 10 000 tirages chacune, forme principale et entiers gardés. (4) Décision et lectures (critères gelés). (5) Rejeu du quota pour q ∈ {1, 2, 3}, sans vérité. (6) Description seulement : attaques de Goodhart, par bras (« retour », « temoin »), part M4 observée comparée aux parts de l'analyse (0,414583 ; 0,32043 ; 0,359626 ; 0,165945 ; un écart est rapporté, pas réparé), part hors softmax, référence R1 aux mêmes longueurs ; aucune décision n'en est tirée.

**Graines (R9).** `numpy.random.SeedSequence(20261118, spawn_key=(k,))`, k = entier des 8 premiers octets du sha256 du nom de la tâche : « p1/sonde-questions », « p1/sonde-score », « p1/espace », « p1/mondes », « p1/partie/<bras>/<questionneur>/<indice du monde>/<rôle> » (rôles : questionneur, ordre, répondeur), « p1/bootstrap/<comparaison> », « p1/information/aa-sur-8-mondes », « p2/reference/<variante> », « p2/m4/<source>/<bras> ». Le manifeste écrit la racine, la règle, la liste des tâches, la configuration et son empreinte, le bloc d'effort et son empreinte, les versions (python, numpy, modules), les empreintes du code, de ce texte, de la contre-lecture et des sources, le commit.

**Comparaisons multiples.** Une seule conjonction décisive par instrument (P1 : ordre, famille A/A, gardes ; P2 : la médiane R1) ; famille A/A corrigée de Bonferroni ; tout le reste est rapporté sans décision.

## Critères de lecture gelés

**P1** (lecture proposée par le code, prononcée par un lecteur neuf ; les gardes priment) :

| gardes C-P1-3 à C-P1-6 | ordre C-P1-1 | A/A propre (C-P1-2, 1re) | ordre de présentation (C-P1-2, 2e et 3e) | verdict |
|---|---|---|---|---|
| une au moins échoue | — | — | — | **garde défaillante** : arrêt, audit du code, aucune phase 1 |
| tiennent | ne tient pas | — | — | **instrument non discriminant (ordre)** : arrêt, rapporté, aucune phase 1 |
| tiennent | tient | ne tient pas | — | **instrument non discriminant (A/A)** : arrêt, rapporté, aucune phase 1 |
| tiennent | tient | tient | ne tient pas | **instrument sensible à l'ordre de présentation** : arrêt, rapporté, aucune phase 1 |
| tiennent | tient | tient | tient | **instrument discriminant** : une phase 1 peut être proposée à Lazar, sur devis (non engagée) |

- Audit de symétrie (R4), déclenché sans changer le verdict, et rapporté avec ses motifs : l'aléatoire recouvre exactement le monde dans au moins 95 % des parties à T = 16 (instrument trop facile) ; un intervalle d'ordre de largeur nulle ; ou un résultat négatif trop net (écart d'ordre inversé, borne haute < 0). Action : relecture du code de la carte et des répondeurs avant tout rapport.
- Les mesures rapportées (M-P1b à M-P1e, variante structurelle, disperseur, A/A de la bissection, ordre du répéteur, dispersion sur 8 mondes) ne changent pas le verdict.

**P2** :

| médiane de R1 (forme principale, toutes cartes) | lecture |
|---|---|
| > 0,25 | **C3 se referme (ne change pas)** : la part observée est à la portée de la grammaire seule |
| ≤ 0,25 | **C3 n'est pas refermée par la référence** ; s'y ajoutent, écrites par le code : « part observée au-dessus du quantile 95 % de R1 » si moins de 5 % des tirages l'atteignent, sinon « part observée non distincte de R1 : réserve » ; et, si la part hors softmax observée ne dépasse pas 0,25, « A-1 : dans la boucle de production, le seuil n'est franchi que par les softmax » |

- Réserves écrites par le code, sans changer la décision : « A-1 » si la décision diffère sous la référence HS (sans les softmax) ; « P-8 » si elle change sous R2 ; « A-3 » si elle change avec les entiers gardés.
- Ce que P2 ne peut pas faire : rouvrir une ligne. Une ligne non refermée reste « change » à la lettre, avec ses réserves ; aucune adoption, aucune phase 1 sans décision de Lazar sur devis.
- Audit de symétrie (R4) : déclenché si la médiane de R1 tombe entre 5/23 et 7/23 (à moins de 1/23 du seuil, dans un sens comme dans l'autre) : la décision est rapportée avec R2, HS, SEQ et entiers gardés côte à côte, et la dépendance à la loi de tirage est dite.
- Rejeu du quota et attaques de Goodhart : description seulement, aucune lecture de décision ; aucune nouveauté attribuée.

## Liste d'arrêt

| condition | action |
|---|---|
| empreinte de ce texte ≠ celle qu'attend le lanceur, ou compagnon `.sha256` absent ou non conforme | refus de partir (code 2), rien écrit |
| empreinte du bloc « effort et échantillonnage gelés » de la configuration absente de ce texte | refus de partir (code 2), rien écrit |
| contre-lecture absente, non scellée, ou qui ne cite pas l'empreinte de ce texte | refus de partir (code 2), rien écrit |
| un module de code sans compagnon `.sha256` ou non conforme | refus de partir (code 2), rien écrit |
| une source (course v67, attaques) d'empreinte inattendue | refus de partir (code 2), rien écrit |
| dossier de sortie déjà présent | refus (R12), rien écrit |
| réponse qui n'est pas un booléen ; question hors grammaire ou absente (règle « arrêt ») | refus écrit (exception nommée), la partie s'arrête ; P1 arrêtée et rapportée |
| ordre de présentation qui n'est pas une permutation des prédicats | arrêt de P1, motif écrit |
| loi de référence ou tirée de type hors gabarit ; grammaire des prédicats différente de celle écrite | arrêt de P1, motif écrit |
| garde de disjonction : plus de 50 × |H| lois retirées | arrêt de P1, motif écrit |
| M2 non reproduite (≠ 9 sur 23) | arrêt de P2, motif écrit (P1 continue) |
| quota ou plage différents de ceux gelés ; carte sans les champs lus par le quota | arrêt de P2, motif écrit |
| suite interrompue dans une source de Goodhart | arrêt de P2, motif écrit |
| verdict autre que « instrument discriminant » | aucune phase 1 ; rapporté tel quel |
| tout refus de permission, de crochet ou de classifieur pendant le run | arrêt, rapport tel quel |

Aucun repli silencieux : chaque arrêt écrit son motif dans la sortie (`arret`), et la sortie, le manifeste et le journal des fichiers ouverts sont scellés.

## Borne de ce que l'instrument P1 permettra de revendiquer (conditions de la mère R-3186, P1 e)

Au mieux, et seulement sous le verdict « instrument discriminant » : sur des mondes tirés dans la grammaire fermée écrite ici, avec les prédicats écrits ici et la règle de carte commune (médoïde), la divergence finale à la loi du monde **ordonne des questionneurs factices de qualité connue**, à une précision mesurée (largeur A/A rapportée à l'écart entre les bornes), sans effet mesurable de l'ordre de présentation. Rien de plus : rien sur les proposeurs réels (aucun ne joue), rien sur la boucle de production (aucun essai de lien), rien sur une composition de proposeurs (N-058 : elle se juge sur l'oracle de la boucle et le coût), rien hors de cette grammaire, rien sur des prédicats d'une autre forme, rien sur la recherche en langue naturelle de l'article. Le code porte cette borne dans la sortie (`borne_de_ce_que_l_instrument_permet_de_revendiquer`).

## Ce que la phase 0 ne dit pas

- Rien sur les proposeurs réels : aucun ne joue (aucun appel de modèle) ; leur position entre les bornes est l'objet d'une phase 1 non engagée, qui exigera son propre préenregistrement, ses réglages gelés, et une puissance calculée avant tout devis (P-4).
- Rien n'est adopté : aucun module de l'organisme n'est changé, la mémoire non plus ; l'option (ii) de P2 (indice servi) n'est pas essayée ; l'option (iii) est seulement rejouée hors ligne sur les 23 cartes, sans vérité ; la note de conception reste suspendue.
- P2 ne dit pas si la répétition est un défaut des proposeurs : seulement si la grammaire suffit à l'expliquer, sous la loi de tirage écrite ici ; une ligne refermée ne prouve pas que les proposeurs sont divers. Aucune forme n'est dite nouvelle.
- P2, phase 0 (c) et (d) de la proposition (proposeur scripté sur mondes plantés ; vérité par carte pour toutes les cartes) ne sont pas faites ici.
- La description des attaques de Goodhart ne qualifie aucune composition de proposeurs (N-058) et n'entre dans aucune décision.
- Aucune dépense, aucune machine, aucun accès réseau.

## Écarts à la proposition et choix déclarés

1. **Monde dans un espace énuméré commun.** La proposition dit « bissection gloutonne par gain d'information sur l'ensemble énuméré des lois candidates » : le monde est une loi de H. H est commun aux 200 mondes (un monde frais par partie, N-049, mais un seul espace de candidates), pour prendre |H| = 2^16 = 2^T, taille à laquelle même une bissection parfaite ne garantit pas d'isoler le monde.
2. **Carte par une règle commune (médoïde).** Les questionneurs factices n'écrivent pas de carte eux-mêmes ; la règle commune isole le choix des questions. La carte est aussi écrite à zéro question (P-7).
3. **Disjonction.** Faute d'accès aux témoins du pôle hors de la course v67, la garde porte sur les lois plantées et les cartes de cette course seulement (limite déclarée).
4. **Répéteur et disperseur.** « Toujours le même trait » est lu comme le premier trait présenté (15 prédicats, reposés quand épuisés) ; « jamais deux fois le même trait » est impossible en 16 questions sur 4 directions : lu comme « jamais deux fois de suite », directions à tour de rôle.
5. **A/A doublé et étendu** (conditions de la mère R-3181 et R-3186) : seuil de largeur gelé à la moitié de l'écart aléatoire − bissection ; l'ordre de présentation entre dans la même famille ; Bonferroni sur trois.
6. **Deux statistiques.** La proposition dit « médianes » pour l'ordre ; le défaut de la masse en 0 impose une statistique qui voit la dégradation : les moyennes sont exigées de concert pour l'ordre, l'A/A et la disparition, et seules pour la dégradation (inversion). C'est plus strict que la lettre de la proposition, jamais plus lâche.
7. **Répondeur au hasard.** « L'ordre disparaît » est lu comme « l'avantage de la bissection disparaît » (borne basse ≤ 0) : sous des réponses au hasard, la bissection peut faire pire que l'aléatoire (ses partages équilibrés réduisent S_t à un sous-ensemble tiré au hasard), ce qui n'est pas un défaut de l'instrument.
8. **Fuite** : la proposition dit « recouvrement parfait au premier tour signalé et refusé » ; ici, la carte à zéro question de l'oracle est le monde : le signalement est une garde (C-P1-5), et la réponse non booléenne est refusée.
9. **P2, structure appariée.** La référence garde les emplacements (générations, proposeurs, ordre) des 23 cartes pour que M2 s'applique à l'identique ; SEQ, sans structure, est rapportée.
10. **P2, phase 0 (b)** : seul le quota (iii) est rejoué ; l'option (ii) demande un proposeur, elle n'est pas rejouable hors ligne.
11. **Attaques de Goodhart** : 1 000 tirages de référence (et non 10 000), pour un coût de calcul raisonnable ; description seulement.

## Ce qui a été vu avant scellement (déclaré, R1 et R4)

- Des pièces déjà versées : la part observée de S1 (9 sur 23, 0,391304), les types des 23 cartes (9 softmax), le constat A-1 (7 des 9 répétitions sont des softmax ; hors softmax 2 sur 14) et les parts M4 des attaques. La règle de décision de P2 est celle de la proposition, écrite avant ; la loi de tirage R1, le quota et sa plage sont écrits ici sans avoir ouvert les cartes ni calculé aucune référence sur elles.
- Les cartes de la course v67 et les sorties des attaques n'ont pas été ouvertes pour cette tâche : seules leurs empreintes ont été recalculées (conformes). La structure de ces fichiers (`releve.cartes`, `releve.plantees`, `suites`, `condition`, `tentatives`, `interrompue`) est prise du programme d'analyse versé.
- Des **petits mondes d'essai** seulement (racine 4242 ; H = 256 lois, T = 8, 150 mondes, sondes de 512 et 128 instances ; et H = 32, 12 mondes pour le lanceur de bout en bout), pour les essais R5. Vu par le brouillon puis par les essais de cette version : bissection nettement meilleure qu'aléatoire (exacte dans ≈ 95 % des parties contre ≈ 40 %) ; répéteur pire qu'aléatoire sur la série de graines des essais, non distinct sur une autre série du brouillon ; inversion de 10 % : dégradation massive en moyenne, invisible à la médiane sur une série ; réponses au hasard : avantage de la bissection effacé ; famille A/A (copie, ordre de l'aléatoire, ordre de la bissection) : intervalles corrigés contenant 0. Une première version du brouillon, où le monde était tiré hors de H, donnait une bissection qui ne battait pas l'aléatoire : abandonnée pour revenir au cadre de la proposition (monde dans l'ensemble énuméré). Ces observations ont fixé les choix 1, 6 et 7 ; aucune n'a été faite à l'échelle ni avec les graines de ce texte.

## Lancement (après contre-lecture et versement, jamais avant)

`cd /home/user/controle-ia-travail/docs/notes/organisme-re-search-v1/phase0-p1-p2-v1 && python3 -B lanceur_phase0_p1p2_v1.py --sortie <dossier neuf> --contre-lecture <rapport de contre-lecture scellé>` ; le lanceur porte l'empreinte attendue de ce texte et refuse de partir sinon, ou sans contre-lecture scellée qui cite cette empreinte. Durée non mesurée à l'échelle (processeur seul) ; estimée de l'ordre de dix minutes à une heure. Le lancement lui-même est une décision à part ; ce texte ne l'engage pas.

## Contre-lecture

À faire par le modèle J, sous-agent neuf qui n'a écrit aucune pièce de cette tâche (R2), sur ce texte scellé et son empreinte, **avant toute exécution** (conditions de la mère R-3181). Fichiers à lui donner explicitement : ce préenregistrement ; les quatre modules de code et l'essai (même dossier) ; les propositions (sections P1, P2, « Ce qui borne », devis) ; la contre-lecture d'ensemble (P-1 à P-8, A-1 à A-4) ; l'analyse et son programme (forme, M2, M4) ; `evaluateur_lois_v62.py` de l'organisme. Son rapport est scellé et cite l'empreinte de ce texte (le lanceur l'exige). Toute remarque acceptée donne une version v2 de ce texte (nom neuf, R12) et un lanceur v2 qui porte la nouvelle empreinte ; le traitement de chaque remarque (acceptée, refusée et pourquoi) est écrit dans cette v2.
