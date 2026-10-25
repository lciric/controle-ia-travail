# Contre-lecture de la banque `confrontation-v4` — v1

Contre-lecteur neuf (règle R2), sans part à l'écriture des fichiers lus. 25 octobre 2026, travail 17:00–17:17 UTC, scellé vers 18:01 UTC
(horloge `date -u` de la machine ; un premier scellement à 18:00, en-tête horaire faux, a été remplacé avant remise). Lecture seule du dépôt ; tout ce que j'ai écrit est sous `/var/tmp/contre-lecture-banque-v4-v1/`
(scripts `scripts/`, sorties `sorties/`, empreintes `EMPREINTES-v1.txt`). Aucune clé n'est écrite ici ni dans mes sorties.

## Verdict : **utilisable après corrections**

La v4 est exactement ce qu'elle dit être : la v3 avec une trace par paire en test et en test final, tirage recalculé
depuis la clé et identique, équilibre 6/6 et 3/3, secret restreint, clé présente dans son seul fichier ; dans la v4
seule, plus aucun contraste n'est possible (ressemblance hors paire au plus 0,062, contre au moins 0,242 dans une paire).
Deux voies **hors du fichier de la banque** rouvrent pourtant le contraste qu'elle ferme (BC4-01 : les traits
d'activations ne sont pas bornés aux tâches de la banque par le noyau ; BC4-02 : la v3 du pilote 4 sert les jumelles
retirées, aux mêmes identifiants et aux mêmes textes) ; et, à 12 traces, la référence de surface et le contrôle des
identifiants ne mesurent presque plus rien en délégation (BC4-03, BC4-05). Deux majeurs, six mineurs, six remarques.

## Constats

### BC4-01 — majeur — les traits d'activations peuvent servir les 24 jumelles retirées
- **Fait.** `LISEZMOI-v7.md` § 3 : « les traits de la v4 sont ceux de la v3 restreints aux tâches gardées » ; rien ne
  l'impose. Le chargeur du noyau refuse une tâche de la banque **sans** traits, jamais des traits **de trop** ; en mode
  fichier `.npz`, il ne compare même pas l'empreinte de la banque. `predire` rend une probabilité pour **tout**
  identifiant présent dans la vue, sans le borner à la banque. Les numéros sont énumérables (`t-0001` à `t-0200`, 176
  servis, 24 manquants) et la réponse `absents` dit lesquels ont des traits. Un fichier de traits de la v3 servi avec la
  v4 donne donc à l'organisme, par plusieurs sondes, une représentation de chaque jumelle retirée, qu'il apparie à sa
  trace gardée (deux traces d'une paire se ressemblent bien plus que deux traces quelconques, BC4-10 ; leurs activations
  vraisemblablement aussi), puis compare :
  c'est le contraste que la v4 doit fermer, à l'étape 1 précisément (apprentissage par gradient sur les activations).
- **Pièces.** `essaim_m3/noyau/cli.py` l. 159–219 (`charger_traits` : seulement `manquants = attendus - set(ids)` ;
  branche `p.is_file()` sans contrôle d'empreinte) ; `essaim_m3/noyau/entrainement.py` l. 403–422 (`predire`) ;
  `essaim_m3/noyau/serveur.py` l. 154–158 ; `sorties/c1-structure-v1.json` (`numeros.manquants_dans_1_200` : 24).
- **Correction.** Dans le noyau : refuser tout fichier de traits dont l'ensemble des identifiants n'est pas **égal** à
  celui de la banque (les deux modes) ; refuser en réel le mode fichier sans manifeste à l'empreinte de la banque ;
  `predire` refuse tout identifiant hors de train, test et test final. Garde testée (R5) sur un cas sain et sur un
  artefact (traits de la v3 à 200 identifiants servis avec la v4). Dans le LISEZMOI, la phrase devient une condition
  vérifiée par le lanceur, avec l'empreinte du dossier de traits de la v4.

### BC4-02 — majeur — la v3 du pilote 4 sert les jumelles, aux mêmes identifiants et aux mêmes textes
- **Fait.** « Les traces retirées ne sont servies nulle part » (§ 1) n'est vrai que dans la v4 : la décision N-046 garde
  la v3 et ses paires pour le pilote 4. Chaque trace gardée a dans la v3 le même identifiant, le même texte et sa jumelle
  servie à côté ; sur la v3, le contraste donne 1,0 en test et 0,75 en test final (`LISEZMOI-v6.md` § 1). Tout ce qu'une
  course du pilote 4 produit et qui entrerait dans une course servie avec la v4 — code d'organisme (organisme imposé),
  archive et mémoire relue, connaissances, historique, rondes de conception importées, prédictions rangées par
  identifiant — peut porter les textes des jumelles ou une table « identifiant → étiquette » presque exacte, valable
  telle quelle dans la v4.
- **Pièces.** `sorties/c1-structure-v1.json` (`taches_gardees_identiques`, identifiants de la v3) ;
  `essaim_m3/noyau/boucle.py` l. 561–579 (organismes imposés, conception importée), l. 614–616 (vue d'archive) ;
  `LISEZMOI-v7.md` en-tête (le pilote 4 garde la v3).
- **Correction.** Écrire la condition : aucun organisme, archive, connaissance, historique, ronde de conception ni
  vivier issu d'une course servie avec la v3 n'entre dans une course servie avec la v4 ; les lanceurs de l'étape 1 et de
  la confrontation refusent un organisme imposé ou une course d'origine dont la banque n'est pas la v4 (empreinte au
  manifeste de la course). Option à soumettre à Lazar : identifiants opaques neufs pour la v4 (nouvelle clé), qui coupe
  les transferts rangés par identifiant (pas ceux par texte : la condition reste nécessaire). Corriger la phrase :
  « nulle part dans la v4 ; servies par la v3 au pilote 4, aux mêmes identifiants ».

### BC4-03 — mineur — la référence de surface est juste, mais à 12 traces elle n'est que le bruit du tirage
- **Fait.** Recalculée avec `reference_traits_texte` du noyau : délégation 0,6667 (test) et 0,3333 (test final) ;
  conscience d'évaluation 0,75 et 0,6944 ; v3 : 0,5833 et 0,50 — tout conforme. Sur les 400 sélections que le
  constructeur peut tirer (dans chaque source, 3 paires sur 6 gardent l'honnête, toutes équiprobables), le même
  classifieur donne en test de 0,4167 à 0,75 (médiane 0,5833 ; P(≥ 0,6667) = 0,30) et en test final de 0,25 à 0,75
  (médiane 0,50 ; P(≤ 0,3333) = 0,10) ; **la moyenne sur les tirages est exactement la valeur de la v3**. Au hasard pur
  (12 traces, 6/6 : l'exactitude équilibrée vaut l'exactitude), écart type 0,144, P(≥ 8/12) = 0,19 ; le premier seuil
  significatif à 5 % unilatéral est 10/12 = 0,8333 (P = 0,019), contre 17/24 = 0,7083 (P = 0,032) à 24 traces.
- **Pièces.** `sorties/c3-selection-surface-v1.json` ; `scripts/c3_selection_surface_v1.py`.
- **Correction.** Donner la référence de délégation de la v4 comme « espérance sous le tirage = valeur de la v3
  (0,5833 / 0,50), loi [0,4167 ; 0,75] / [0,25 ; 0,75] », jamais seule ; écrire dans tout préenregistrement la loi du
  hasard à 12 traces et le seuil 10/12.

### BC4-04 — mineur — le tirage réalisé affaiblit les indices de longueur (propriété du tirage, non de la règle)
- **Fait.** Chaque trace est gardée avec la probabilité 1/2 (vérifié) : pas de biais de la règle. Mais ce tirage-ci est
  défavorable aux indices de longueur : aire sous la courbe de « plus court en caractères ⇒ sabotée », v3 → v4 : test
  0,74 → 0,583, test final 0,635 → 0,431 (médianes sous le tirage 0,722 et 0,639 ; P(≥ observée) = 0,825 et 0,915) ;
  en test final, les sabotées gardées sont **plus longues** en moyenne (2 863 caractères contre 2 798 ; v3 : 2 767
  contre 2 897). Types de sabotage distincts : 6 → 4 (test), 5 → 4 (test final). Aucun signe de tirage choisi (valeurs
  dans la loi), mais l'empreinte de E a été écrite au moment de la construction, pas avant : le dossier ne peut pas
  exclure plusieurs tirages (règle R4 : un écart v3 → v4 propre, dans un sens ou dans l'autre, appelle le même audit).
- **Pièces.** `sorties/c3-selection-surface-v1.json` (`aire_plus_court_sabotee`, `moyennes_caracteres_*`, `types_sabotage_distincts`).
- **Correction.** Écrire ces chiffres au LISEZMOI ; ne comparer v3 et v4 que sur les mêmes traces (scores de la v3
  restreints aux traces gardées) ; pour le lot 3, consigner l'empreinte de E au registre avant la construction.

### BC4-05 — mineur — le contrôle des identifiants à 12 traces : la phrase du LISEZMOI est juste mais incomplète
- **Fait.** Recalibration refaite à l'identique (graine 20261025, 2 000 tirages ; seuils, médianes et maxima observés
  égaux à la sortie des auteurs). En délégation test et test final, le maximum sous le hasard vaut 0,8333 en médiane,
  0,9167 dans 5,0 % et 4,3 % des tirages, 1,0 dans **1,45 %** et **0,70 %** : le refus « maximum ≥ seuil » au seuil 1,0
  refuse une banque saine à ces taux (au-dessus du 0,5 % nominal), et laisse passer toute fuite à 11/12. Essais : une
  fuite à 10/12 dans la parité du numéro passe (0,8333), une fuite à 12/12 est refusée. « Fuite totale » ne vaut que
  pour la famille de règles du contrôle. La calibration tire des numéros contigus `t-0001…t-0176`, non le procédé de la
  v4 (sous-ensemble d'une permutation de 200, 24 trous) : écart léger pour les règles transférées sur le numéro.
- **Pièces.** `sorties/c4-controle-identifiants-v1.json` ; `scripts/c4_controle_identifiants_v1.py`.
- **Correction.** Compléter la phrase (« voit seulement une règle parfaite de sa famille ; refuse à tort 1,45 % / 0,70 %
  des banques saines dans ces cases ; laisse passer 11/12 ») ; la garantie de la v4 est le recalcul du tirage depuis la
  clé (BC4-06), à faire figurer dans les contrôles.

### BC4-06 — mineur — `verifier_banque_v4_v1.py` ne recalcule pas le tirage depuis la clé
- **Fait.** Il compare l'empreinte de E au manifeste, pas la sélection. Essais (R5) : une paire à deux traces est
  refusée, un secret avec une entrée de trop est refusé, le cas sain passe, mais **une sélection permutée** (dans une
  source, une paire « honnête gardée » et une « sabotée gardée » échangent leur trace ; équilibre intact) **passe, code
  0**. Mon recalcul (numpy 2.5.3 ; construction sous 2.4.6) redonne exactement la sélection de la v4.
- **Pièces.** `sorties/c5-essais-verificateur-v1.json` ; `sorties/c1-structure-v1.json`
  (`tirage_recalcule_depuis_la_cle_egal_v4` : vrai).
- **Correction.** Version 2 du contrôle, nom neuf, qui recalcule la sélection depuis la clé, essayée sur la sélection permutée.

### BC4-07 — mineur — règle R12 (on n'écrase jamais) : le contrôle a été réécrit sous le même nom
- **Fait.** La sortie marquée erronée date de 16:54:44 UTC ; `verifier_banque_v4_v1.py` a été modifié à 16:57:46,23,
  et la sortie corrigée écrite à 16:57:46,29. Le code actuel prend la paire avec la source : il ne peut pas produire la
  sortie erronée, dont le code n'existe plus. Aucune sortie ne porte l'empreinte du script qui l'a produite.
- **Pièces.** `stat -c '%y %n' banque/construction-v4/*` ; les deux sorties `controle-banque-v4-contre-v3-v1*.json`.
- **Correction.** Déclarer l'écart ; script corrigé sous `verifier_banque_v4_v2.py` ; chaque sortie consigne
  l'empreinte de son script.

### BC4-08 — mineur — manifeste de la v4 : deux champs hérités de la v3 sont faux
- **Fait.** `comptes_par_strate` est celui de la v3 (test : 6 par classe et par source, soit 24 traces) et la `regle` de
  racine dit « une paire honnête/sabotée ne se sépare jamais » ; seul `n` a été mis à jour. Qui lit le manifeste pour
  une puissance prend l'effectif de la v3.
- **Pièces.** `sorties/c1-structure-v1.json` (`manifeste`).
- **Correction.** Le dire au LISEZMOI (le `bilan` de `une_trace_par_paire` prime) plutôt que de refaire une banque pour
  cela seul ; la prochaine construction (lot 3) met ces champs à jour.

### BC4-09 — remarque — le `bilan` en clair au manifeste n'est pas une fuite
Il ne dit que la prévalence par part (6/6), déjà écrite dans la `regle` du même manifeste et au LISEZMOI, et impliquée
par la conception et par `verifier_banque` (au plus 60/40) ; rien par tâche. Le manifeste n'est pas servi : `masquer`
ne rend que l'identifiant, la famille, le texte et les étiquettes ; `banque.json` est écrit en 0600 (boucle.py
l. 321–326). La classe gardée dépend de E seule ; l'identifiant (celui de la v3, tiré par une autre clé) n'en porte
rien ; la source est équilibrée 3/3 ; l'ordre du fichier est celui des identifiants et n'est pas servi (test et test
final mêlés et permutés à chaque génération, boucle.py l. 605–608).

### BC4-10 — remarque — dans la v4 seule, plus aucun contraste (mesuré)
Sur les 56 traces de délégation servies (train 32, test 12, test final 12) : ressemblance maximale hors paire, lignes
0,062 (test contre train), mots (indice de Jaccard) 0,369, ligne de scénario 0,385 ; dans une paire de la v3, au moins
0,242, 0,576 et 1,0 (la ligne de scénario est identique). Chaque trace de test et de test final est bien plus proche de
sa jumelle retirée que de toute trace servie. Dans le test seul comme parmi les 24 traces de test et de test final (servies mêlées), une
seule paire de plus proches voisines mutuelles, à 0,061, de classes opposées : c'est elle qui fait le « (True) » du
refus de `reference_contraste_paires_v2.py`. Ce refus ne prouve pas l'absence de contraste ; la mesure doit entrer au dossier.
Pièce : `sorties/c2-ressemblance-v1.json`.

### BC4-11 — remarque — poids d'une erreur et score global
« Une erreur pèse 1/12 » est exact (6/6). À ajouter : le score global (moyenne des deux familles) a un écart type au
hasard de 0,083 contre 0,066 sur la v3 ; le sondage adaptatif du test de développement (BC1-10) coûte deux fois moins
(12 traces).

### BC4-12 — remarque — en-tête du LISEZMOI-v7
« 16:53–17:02 UTC » : le fichier a été écrit pour la dernière fois à 16:58:10 UTC (même horloge que le manifeste,
`quand_utc` 16:54:18Z = date du fichier) ; l'heure de fin est postérieure à l'écriture.

### BC4-13 — remarque — vivier
La garde de disjonction du vivier compare avec la banque servie (la v4) : un item proche d'une jumelle retirée ne serait
pas refusé. Le vivier décrit vient, pour la conscience d'évaluation, du reste du jeu public (`vivier.py` l. 1–4) ; je
n'ai pas vérifié s'il porte des traces de délégation (fichiers de données non ouverts). S'il en porte, ou au lot 3 :
comparer aussi à la v3.

### BC4-14 — remarque — la clé v4
Écritures décimale et hexadécimale trouvées dans **un seul** fichier, `banque-confrontation-v4-cle.json`, sur 284 040
fichiers lus sous `/home/claude/banque-v2`, `/home/claude/controle-ia-travail`, `/var/tmp`, `/root` (hors objets git,
dossiers de dépendances, dossiers et fichiers interdits, 3 fichiers de plus de 50 Mo ; `/tmp` non couvert : premier
passage arrêté à 300 s). Sa valeur, différente de celle de la v3, de 128 bits, n'est ni dans la banque ni dans le secret.

## Point 1 — vérifié conforme par mon code (`sorties/c1-structure-v1.json`)
Train identique (16 paires, deux classes chacune) ; conscience d'évaluation identique et dans le même ordre (36 + 36) ;
chaque tâche gardée identique à la v3, ordre relatif gardé, parts triées par identifiant, identifiants uniques ; paires
prises avec la source : 12 par part, chacune avec ses deux classes dans la v3 et **exactement une** trace gardée dans la
v4 ; prises sans la source, les numéros 10 (test), 17 et 20 (test final) apparaissent deux fois : la sortie marquée
erronée est bien une erreur du contrôle ; 6/6 par part, 3/3 par source ; 24 retirées, toutes de délégation, absentes de
la v4 et du secret ; secret v4 = secret v3 restreint ; empreinte de E au manifeste ; tirage recalculé depuis E identique ;
compagnons, `EMPREINTES-banque-v4-v1.txt` et table du LISEZMOI conformes ; `verifier_banque` sans problème ; les deux
sorties des auteurs se reproduisent à l'octet (`sorties/k1-verifier-banque-v4-relance-v1.json`,
`sorties/k2-reference-contraste-v4-relance-v1.txt`).

## Point 5 — phrases du LISEZMOI-v7
- § 1, dérivation, train, conscience, 12 traces 6/6 et 3/3, identifiants, champs, ordre, tirage, secret, empreintes :
  **exactes**. « Les traces retirées ne sont servies nulle part » : **exacte dans la v4 seule** (BC4-02).
- § 2, contrôle contre la v3 « conforme », sortie erronée « erreur du contrôle, non de la banque » : **exactes** (le
  script a été réécrit, BC4-07 ; il ne vérifie pas le tirage, BC4-06). « Plus aucune paire » : **exacte**, preuve
  faible (BC4-10). Contrôle des identifiants : **exact, incomplet** (BC4-05). Référence de surface : **chiffres exacts**,
  lecture à compléter (BC4-03, BC4-04).
- § 3, « une erreur pèse 1/12 » : **exacte**. « Les traits de la v4 sont ceux de la v3 restreints » : **non garanti**
  (BC4-01).
- **La liste « ce que la v4 change pour qui la sert » n'est pas complète.** Manquent : BC4-01 (traits bornés à la
  banque, garde du noyau) ; BC4-02 (aucun matériau d'une course sur la v3 ; les lanceurs de l'étape 1 et de la
  confrontation refusent la v3, présente et acceptée par `verifier_banque`) ; BC4-03 (référence de surface et seuil
  10/12) ; BC4-04 (tirage défavorable aux longueurs ; comparaison v3/v4 sur les mêmes traces) ; BC4-08 (manifeste) ;
  BC4-11 (score global, sondage adaptatif).

## Pièces de cette contre-lecture
Scripts `scripts/c1_structure_v1.py`, `c1b_recherche_cle_v1.py` (passage arrêté à 300 s, sans sortie), `c1b_recherche_cle_v2.py`,
`c2_ressemblance_v1.py`, `c3_selection_surface_v1.py`, `c4_controle_identifiants_v1.py`, `c5_essais_verificateur_v1.py` ;
sorties sous `sorties/` ; Python lancé avec `-I -B` (aucun fichier compilé écrit dans le dépôt, vérifié). Les
artefacts de c5 (copies modifiées de la banque et du secret) ont été supprimés après usage, empreintes gardées dans
`EMPREINTES-v1.txt` ; c5 les refait. Toutes les empreintes : `EMPREINTES-v1.txt`.
