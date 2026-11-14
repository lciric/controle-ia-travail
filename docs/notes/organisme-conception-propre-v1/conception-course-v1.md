# Conception — course de l'atelier d'idées sur la conception de l'organisme lui-même, une génération — v1

Écrite par un préparateur neuf, sous-agent de la session mère, le 13 novembre 2026 (entre 23:05 et 23:30 UTC, heures
relevées par `date -u`). Demande de Lazar : R-2593 (« lancons l'organisme d'ideation pour produire des idees neuves de
conception de l'organsime, que ce soit le juge ou autre ») et R-2609 (GO de principe, dépense accordée par anticipation,
**bornée à 25 USD pour une génération**, ligne de GO inscrite au montant du pire cas du devis). Rôle : **atelier d'idées**
(N-065, rôle 2) — les fiches sont du matériau, jamais une preuve ; tout usage décisif passe par un préenregistrement (R1).
Modèle suivi : la préparation « bassins étroits » (`docs/notes/organisme-bassins-etroits-v1/`), dont les constats de la
vérification du lanceur v3 (`verification-courte-lanceur-v3-v2.md`, `9c1caa7e…` : B1, M1, M2, mineurs) sont corrigés ici.

Dans ce texte, « modèle A » est le modèle de Claude que le code étiquette `opus` (proposeur) et `opus-juge` (juge) ;
« modèle B » celui qu'il étiquette `fable`. Argon (`gemini-4-argon`) et Kimi (`kimi-k3.1-pro`) sont nommés.

Pièces : question `question-organisme-conception-propre-v1.md` ; témoins `temoins-plantes-v1.md`,
`temoins-organisme-conception-propre-v1.json`, `temoins-lecteur-v1.json`, `temoins-hasard-v1.json` (outil
`outils/tirer_fiches_hasard_v1.py`) ; catalogue `catalogue-conceptions-publiees-v1.md` ; consigne du lecteur
`consigne-lecteur-v1.md` ; devis `devis-v1.md` ; lanceur `scripts/lancer_course_ideation_conception_propre_v1.py` et ses
essais ; rapport `rapport-preparateur-v1.md`.

## 1. Ce que la course fait : une génération, plafond bas

- **Orchestrateur** : clone en lecture `/home/user/lciric/ideation-organism`, jamais modifié. Le lanceur épingle **l'arbre
  du dossier `orchestrator/`** (objet git `ee84d6ec…`, identique aux commits `be6b5af9…` et `1168b02…`, ce dernier local et
  non poussé, R-2594) et les empreintes des neuf fichiers de la chaîne de lancement (mêmes que le lanceur v3 des bassins) :
  un commit qui ne touche que la page publique du dépôt ne bloque pas la course, un octet changé dans l'orchestrateur la
  bloque. Course à fiches, comme le 8 novembre (sans `--course-2`).
- **Pièces servies** (liste blanche construite par l'orchestrateur lui-même, sans appel) : la question ; `faits-v1.md`
  (`docs/notes/collisionneur-bassins-etroits-v1/faits-v1.md`, `d19b5400…`, description filtrée de l'organisme : aucune loi
  plantée, aucune graine, aucun score), aux proposeurs et au juge ; les témoins de l'orchestrateur. **Aucun matériau de
  notre part** (ni recoupement, ni catalogue) n'est servi aux proposeurs : la question est posée avant (N-044, point 4).
- **Proposeurs et parts** (inchangés depuis les bassins, gardes de taille déjà éprouvées) : modèle A et modèle B, deux passes,
  six fiches au plus par passe, plafond de session 2,0 USD chacun par passe ; Argon (proposeur externe imposé par le code
  avec le moteur réel), plafonds 1,3 (passe 1) et 1,9 (passe 2), contrôle externe 1,7. Parts égales entre les deux modèles
  de Claude ; Argon borné par sa garde avant envoi. Graine de la course : 2026111401.
- **Juge de l'organisme** : le code exige au moins un juge (`opus-juge`, plafond 1,5) et un juge externe déclaré (`argon-juge`,
  différé). **Le juge différé n'est jamais joué** : ce lanceur n'a pas de bras ; la consigne en attente reste scellée, sans
  appel. Le juge `opus-juge` note les fiches pendant la course ; **ses notes ne servent à rien dans la sélection** (§ 4.8).
- **Commande**, seule et exacte, depuis la racine du dépôt :
  `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_conception_propre_v1.py 1`.
  Le lanceur garde lui-même (M1) : options `-I -B` (drapeaux de l'interpréteur), ligne de commande d'origine exacte
  (`sys.orig_argv`), argument unique `1`, dossier courant = racine du dépôt, interpréteur `/usr/local/bin/python3`, et sa
  propre empreinte égale à son compagnon `.sha256` (garde contre l'accident ; contre une réécriture des deux, c'est
  l'épingle du crochet qui garde).
- **Lancement détaché** sous un superviseur (session de processus neuve, signaux relayés par PID, code de sortie scellé) ;
  la même commande, relancée : en marche (code 3), orchestrateur orphelin (4), clôture (0), refus (2). **M2** : tout ce qui
  peut échouer (git, empreintes, mesures, environnement, manifeste de pré-départ scellé) est fait **avant** le détachement ;
  après lui, une seule écriture (le manifeste de départ, court) ; si elle échoue, le lanceur imprime le PID du superviseur et
  la commande d'arrêt par PID (code 5), et le superviseur a déjà scellé son propre PID dans son dossier : l'invocation
  suivante retrouve la course par le manifeste de pré-départ. Aucune commande git après le détachement.
- **Dépense lisible et scellée dans le dépôt** (leçon de B1 et de m1) : à la clôture, le lanceur écrit dans le dossier de run
  du dépôt (`runs/course-ideation-conception-propre-v1/<identifiant>/`) un **relevé de dépense** scellé et des **copies
  scellées, octet pour octet**, des pièces dont dépendent la dépense, la relance et la lecture (code du superviseur,
  manifeste de fin de l'orchestrateur, tentatives de contrôle, trois listes de fiches, lecture de la course, témoins servis),
  avec l'empreinte de chaque source. Après la clôture, cumul et relance ne lisent **que le dépôt**. Un run clos sans relevé
  lisible compte son plafond entier.
- **Relance** : **une seule au total** (comme R-2558 pour la ligne des bassins), et seulement si la course précédente a fini
  proprement, sans aucune fiche, avec un relevé lisible, et si la garde de cumul tient. Jamais après des fiches (R3).
- **Garde de cumul** : dépense relevée + plafond de la course (14,9) + réserve du lecteur (4,0) ≤ min(25, plafond de la
  ligne de GO). Avec une ligne au pire cas du devis (21 USD), la relance n'est possible que si la première tentative a coûté
  au plus 2,1 USD (défaut au contrôle).
- **Ligne de GO** : le lanceur ne connaît pas son identifiant d'avance ; il exige **une seule** ligne principale de type
  calcul, accordée par Lazar, en cours de validité, non révoquée, dont le périmètre contient « organisme d'idéation » et
  « propre conception », au plafond d'au moins 21 USD ; il transmet son identifiant à l'orchestrateur (`GO_ID`).
- **Environnement** transmis par liste de noms permis (cause du 401 de R-2549) : `PATH`, `LANG`, `LC_ALL`, `TZ`, `TMPDIR` ;
  `HOME` neuf hors du dépôt, `GO_ID` et `PYTHONPYCACHEPREFIX` fixés par le lanceur ; noms seulement au manifeste.

## 2. Ce que l'organisme rend

Des **fiches** au gabarit de l'orchestrateur (`pole/ideation_v2.py`, `GABARIT`) : nom, type, énoncé, loi prédictive
(espace d'instances, prédiction, signe, métrique), perte de traduction, questions servies, avantage, originalité, demande à
l'organisme, coût, piège, « cosmétique si », antériorités. La question impose dans ces champs : une seule étiquette de levier
(`levier:juge`, `levier:proposeurs`, `levier:composition`, `levier:cout`), une demande `modification` ou `ajout`, une
métrique lue par l'oracle et le coût, un contrôle négatif. Au plus 36 fiches (3 proposeurs × 2 passes × 6). Seules les
**fiches validées** (gardien de l'orchestrateur, hors quarantaine de la garde lexicale « niveau méthode ») sont lues ; les
refusées et les mises en quarantaine sont comptées par motif et rapportées.

## 3. Entre la course et la lecture

La mère (ou Lazar) lit en entier les fiches validées copiées dans le dépôt et scelle une **attestation** :
`attestations/attestation-lecture-g1-v<N>.json` = `{"lecteur", "lu_le", "fiches_validees_sha256",
"aucune_recette_aucun_secret": true, "envoi_au_lecteur_externe_permis": true}`. Sans elle, rien n'est envoyé au lecteur
(fournisseur externe). Les notes du juge de l'organisme ne sont **pas** ouvertes à ce moment.

## 4. Règle de sélection, écrite avant la course

Elle classe les fiches **sans le juge de l'organisme** (N-058 : la composition se juge sur l'oracle et le coût ; ici, les
idées ne sont jamais classées par le verdict du juge). Elle ne prétend pas mesurer la valeur d'une idée : elle retient les
idées qui satisfont des conditions vérifiables sur leur texte, qui ne sont pas une conception publiée du catalogue, et qui
coûtent le moins à éprouver ; la valeur se mesure plus tard, sur une famille de mondes jamais vue (§ 9).

### 4.1 Admissibilité, par programme (aucun modèle)

Une fiche est **admissible** si elle est validée, si `questions_servies` contient **exactement une** étiquette de levier, et
si `demande_organisme.nature` ∈ {`modification`, `ajout`}. Les autres sont « hors question », comptées, jamais classées.

### 4.2 Le lecteur

Un **lecteur neuf d'une famille de modèles absente des proposeurs et du juge** : recommandé, Kimi (`kimi-k3.1-pro`, famille
Moonshot ; relais `relais_kimi_v4.py`, clé lue par son nom `KIMI_API_KEY` par le relais seul ; prix lus le 30 octobre 2026 :
2 USD par million de jetons d'entrée, 10 de sortie, `conception-juge-tournoi-elo-v2.md`, `0ac81c9a…`, § 2.1). Le choix de la
famille est un **nœud** (rapport, N1) : Astra (`gpt-6-astra`) ou Lazar lui-même sont les autres voies ; la règle ne change
pas. Le lecteur n'est ni proposeur, ni juge de l'organisme, ni auteur des témoins.

### 4.3 Ce que le lecteur reçoit, et dans quel ordre

La consigne `consigne-lecteur-v1.md`, la question, `faits-v1.md`, le catalogue fermé `catalogue-conceptions-publiees-v1.md`
(12 entrées), puis la **pile** : les fiches réelles admissibles et les **20 témoins** (§ 5), toutes sous la vue servie
(sans auteur, identifiant, passe, empreinte ni marque de témoin), étiquetées `F01…` dans un ordre tiré au hasard, par lots de
20 au plus. **Deux lectures indépendantes** (sessions neuves), chacune avec son propre ordre. Graines (R9) :
`numpy.random.SeedSequence(2026111302).spawn(4)` → enfants 0 et 1 : ordres des deux lectures ; enfant 2 : départage ;
enfant 3 : permutation du témoin à score permuté (§ 4.7) ; `SeedSequence(2026111303)` : test du § 6.

### 4.4 Les huit points vérifiés (détail dans la consigne du lecteur)

R1 prédiction fermée ; R2 mesure par l'oracle et le coût, sans verdict de juge ; R3 contraintes tenues ; R4 garantie du
juge (sans objet hors `levier:juge`, mis à 1 par le programme) ; R5 exécutable ; R6 réfutable à coût borné ; R7 mécanisme
qui implique le signe prédit sans contredire les faits ; N conception publiée du catalogue (code `C1` à `C12`, ou `aucune`).

### 4.5 Preuve et accord, par programme

- Un 1 à R1–R7 n'est compté que si son `passage` se trouve **mot pour mot** dans la vue servie de la fiche (espaces
  normalisés) ; sinon il compte 0 (« non prouvé », compté et rapporté).
- Une occupation `Ck` n'est comptée que si `passage_fiche` est dans la fiche et `passage_catalogue` dans l'entrée `Ck` ;
  sinon la lecture compte `aucune` pour cette fiche, et l'occupation non prouvée est rapportée.
- **Valeur retenue** : R = 1 seulement si **les deux lectures** donnent 1 prouvé ; N = `aucune` seulement si **les deux**
  donnent `aucune` (une occupation prouvée par une seule lecture suffit à occuper).

### 4.6 Classement

1. **Portes** : R2 = 1, R3 = 1, R7 = 1. Une fiche admissible qui en manque une est « écartée » (motif rapporté).
2. **Nouveauté** : parmi les fiches passées, N = `aucune` → « neuve » ; sinon « occupée » (classée à part, rapportée : c'est
   la part de réinvention).
3. **Ordre des neuves** : S = R1 + R4 + R5 + R6 (0 à 4), décroissant ; puis le coût de l'expérience décisive déclaré
   (`processeur` avant `depense`) ; puis le départage tiré (enfant 2). Jamais la note d'un juge, jamais l'auteur.
4. **Désignées** : les **deux premières neuves**. Moins de deux neuves : celles qui existent, et c'est dit.

### 4.7 Témoin à score permuté

Sur les fiches réelles admissibles, les vecteurs (R1…R7, N, coût) sont **permutés entre fiches** (enfant 3), puis le même
classement est appliqué : les deux premières de ce classement forment le **témoin à score permuté**, scellé avec le
classement. Il sert de bras témoin à l'essai ultérieur (§ 9) : deux idées choisies par la même chaîne, mais sans
l'information de la règle. Le nombre de fiches communes aux deux paires est rapporté.

### 4.8 Le verdict du juge de l'organisme

Les notes de `opus-juge` sont scellées par l'orchestrateur pendant la course, copiées dans le dépôt à la clôture, et **ne
sont ouvertes qu'après le scellement du classement**. On rapporte alors, à titre d'information, la concordance (τ de Kendall)
entre la note totale du juge et le score composite du § 6 sur les fiches réelles. Rien n'en revient au classement. Les
comptes par proposeur (fiches passées, neuves, désignées) sont rapportés et **ne servent jamais à choisir la composition**
(N-058).

## 5. Témoins plantés (détail et sources : `temoins-plantes-v1.md`)

Vingt témoins, écrits ou tirés avant la course, mêlés sans marque à la pile du lecteur ; les quatre premiers servent aussi au
juge de l'organisme (classes imposées par le code).

| Famille | Témoins | Ce qu'on mesure sur eux |
|---|---|---|
| **Conceptions publiées**, réécrites dans le vocabulaire de l'organisme, sans nom ni référence | 7 : POPPER (C2, aussi faux d'antériorité pour le juge), Co-Scientist (C1), The AI Scientist (C3), Fork-and-Flush (C5), PACE (C7), réserve réutilisable de Dwork et al. (C11), Pay Only for Disagreement (C9) | **sensibilité du critère N** : part reconnue, avec la bonne entrée ; quatre d'entre eux (C2, C7, C9, C11) passent tout le reste, et ne sont arrêtés que par N |
| **Fausses fiches** visant un critère | 3 : sans prédiction fermée (R1 ; aussi faux de falsifiabilité pour le juge), composition choisie sur les promotions par dollar (R2, N-058), prime de nouveauté servie aux proposeurs (R3, N-053) | **spécificité** de R1, R2, R3 |
| **Vrai et jumeau** | 2 : arrêt des générations par capture et recapture entre deux proposeurs (absent du catalogue), et sa réécriture | **faux rejets** de la règle ; constance entre une idée et sa réécriture |
| **Idées tirées au hasard** | 8 : assemblées par programme à graine scellée (`outils/tirer_fiches_hasard_v1.py`), forme complète, fond non pensé | si la règle sépare une idée pensée d'un assemblage correct en forme (§ 6, test) |

Les valeurs attendues de chaque témoin, critère par critère, sont scellées dans `temoins-lecteur-v1.json` ; l'exactitude du
lecteur sur chaque critère est rapportée.

## 6. Lisibilité du classement et contrôle des comparaisons multiples

Le classement est **lisible** seulement si toutes ces conditions tiennent (fixées ici, avant la course) :

- **L1** — au moins **5 des 7** conceptions publiées reçoivent, dans au moins une lecture, une occupation prouvée par
  l'entrée attendue (§ 4.5) ;
- **L2** — chaque fausse fiche reçoit 0 au critère qu'elle vise, **dans les deux lectures** ;
- **L3** — le vrai et le jumeau passent les trois portes et restent « neufs » ;
- **L4** — accord entre les deux lectures sur R7 et sur N (occupée ou non), toutes fiches de la pile : κ de Cohen ≥ 0,4 pour
  chacun ; si κ n'est pas défini (une marge constante), accord brut ≥ 0,8 ;
- **L5** — **le seul test de la course** : score composite C = 1[portes passées et N = `aucune`] × (1 + S), de 0 à 5 ;
  H₀ : les fiches réelles admissibles et les huit idées tirées au hasard ont la même loi de C ; H₁ : C plus grand chez les
  fiches réelles ; statistique = différence des moyennes ; test par permutation unilatéral, 100 000 permutations
  (`SeedSequence(2026111303)`) ; **rejet si p ≤ 0,05**. Prédiction : signe positif.

**Comparaisons multiples** : L5 est l'unique test qui décide ; L1 à L4 sont des conditions de lecture, non des tests. Les
huit comparaisons critère par critère entre fiches réelles et idées tirées au hasard sont rapportées avec valeurs p ajustées
par Holm, à titre descriptif, jamais pour décider. Les deux idées désignées sont le maximum d'une sélection parmi au plus
36 : leurs scores sont biaisés vers le haut par la sélection, et aucune revendication ne s'appuie sur eux ; l'essai
ultérieur (§ 9) comparera chacune au témoin à score permuté et à l'organisme inchangé, Holm sur l'ensemble de ses
comparaisons, à préenregistrer.

## 7. Ce qui serait un échec (dit avant)

- **E1** — aucune fiche validée : course en défaut ; une relance au plus, aux conditions du § 1 ; sinon fin, rapportée.
- **E2** — classement **non lisible** (L1, L2, L3 ou L4 manque) : aucune idée désignée ; la lecture est rapportée telle
  quelle ; un nouveau lecteur ou une règle neuve font une version neuve (nœud).
- **E3** — **L5 non rejetée** : la règle ne sépare pas les fiches de l'organisme d'assemblages tirés au hasard ; aucune
  idée désignée ; résultat négatif rapporté (la règle ne mesure que la forme, ou l'organisme ne fait pas mieux que le
  hasard sur cette question : on ne tranche pas entre les deux).
- **E4** — moins de deux neuves : désignation partielle ou nulle, dite.
- **E5** (information, non un échec de la règle) — plus de 80 % des fiches passées sont occupées : l'organisme réinvente.
- **R4 du programme** : un résultat trop propre (lisibilité parfaite, κ = 1, toutes les publiées reconnues, aucune idée tirée
  au hasard passée) déclenche le même audit qu'un échec : contrôle des passages cités, relecture d'un échantillon par la
  mère.

## 8. Ce qui reste à écrire avant la lecture (non prêt ici)

L'**outil du lecteur** (pile, vues servies, ordres, lots, appels par le relais Kimi, réponses scellées) et le **programme de
classement** (preuves, accord, portes, classement, témoin permuté, L1 à L5, rapport) : à écrire, essayer sur des lectures
factices (cas sain et artefacts, R5), contre-lire par un autre modèle, sceller, **avant** que les fiches soient envoyées au
lecteur. Leur comportement est entièrement fixé par les § 4 à 7 ; un écart à ce texte serait un écart déclaré.

## 9. Suite, hors de cette course (devis à part)

Les deux idées désignées, et les deux du témoin à score permuté, seront essayées sur une **famille de mondes plantés
jamais vue** (N-044, point 1), contre l'organisme inchangé, à coût égal, métriques de l'oracle et du coût, sous un
préenregistrement scellé (R1) et un devis propre. Rien de cette suite n'est payé par la ligne de cette course.

## 10. Limites

- Les témoins écrits à la main le sont par le modèle A, qui est aussi proposeur ; « tiers » vaut pour l'instance. Leurs
  longueurs (1 500 à 3 700 caractères) et le style mécanique des idées tirées au hasard peuvent les rendre reconnaissables.
- La nouveauté est relative à un catalogue de 12 entrées ; une fiche « neuve » ici peut être publiée ailleurs (R8 : zone
  vierge = question).
- Les critères vérifient la forme et la cohérence, R7 seul approche le fond ; L5 dit si cela suffit à séparer du hasard.
- Le juge de l'organisme est du modèle A, comme un proposeur ; ses notes ne servent pas.
- Citations obligatoires (N-064) mises dans la question servie : elles font connaître aux proposeurs POPPER et
  Co-Scientist, deux entrées du catalogue.
- Une génération : aucune conclusion sur l'effet des générations, ni sur la valeur relative des proposeurs.
