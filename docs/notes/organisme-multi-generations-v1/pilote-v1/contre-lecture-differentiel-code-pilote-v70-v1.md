# Contre-lecture du différentiel v69 → v70 du code du pilote MR-2 — v1

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), contre-lecteur **neuf**, sous-agent de la session
  `session_01QPDgKgACWyCkCN8HjqwNXy`. Je n'ai écrit ni le code (Claude Opus 5.5), ni le texte, ni la mesure, ni la contre-lecture
  précédente. Réserve de lignée : même maison que le développeur ; Fable 5.2 est proposeur du pilote.
- **Demande** : message de la mère (cinq points de vérification, verdict parmi trois). Pièces lues, chacune égale à son compagnon
  avant lecture : rapport du développeur (`4deb6e41354a1d9e4f2730b167c6737ed86538bccfc91c29f566e5da92aa9afa`), contre-lecture
  précédente (`935e44bc6d21cbc36206424486c39ed5569f594978c6e490b2c1c04dc487a613`) et ses outils (mutations W1 à W5), décisions
  R-2548 et R-2596, paquets v65 à v70, différentiel v2, patch, bloc gelé, journaux des essais et du banc.
- **Heures** (`date -u`, 13 novembre 2026) : début 21:29:23 ; chaîne des paquets 21:30 ; 109 essais 21:30:23 à 21:34:06 ;
  épreuves directes 21:33 à 21:38 ; quinze mutations 21:34:37 à 21:49:32 ; fin : dernière ligne.
- **Aucune dépense, aucun appel de modèle, aucun loueur, aucune clé lue ni affichée ; ni la sonde ni le pilote joués en mode
  réel.** Réseau : deux récupérations git à refspec explicite (la branche `prep/pilote-mr2-v1` du dépôt de travail ;
  `refs/heads/main` du dépôt public de l'organisme, pour le commit `94bfd92`, prérequis du paquet v65) ; rien d'autre que la
  boucle locale des essais (doublures, clés factices posées par les essais). Tous mes lancements sous `env -i` (PATH,
  OMP_NUM_THREADS=2, HOME et TMPDIR de mon bac) : aucune variable de l'environnement réel n'a atteint un essai. Un processus de
  calcul à la fois, `ulimit -v 6000000`. Aucune écriture git hors de mon arbre de lecture (retiré à la fin) ; rien poussé ; rien
  versé. Aucun refus de permission ni de classifieur.

## 0. Verdict

**Autorisable pour la sonde.**

La sonde ne peut dépenser que sous ses deux lignes, lues au montant exact avant tout dossier et tout relais ; les clés ne
passent que par leur nom, au seul relais ; chaque relais est borné à sa part (8,07 USD au plus pour 8,052896 de pire cas) ; le
relevé garde les champs d'usage bruts. Les cinq majeurs et les huit mineurs de la contre-lecture précédente sont corrigés, le
point (7) durci. Les trois écarts écrits sont acceptables, le deuxième avec une réserve.

**Constats neufs : 0 bloquant, 2 majeurs, 8 mineurs.** Les deux majeurs ne touchent pas la dépense de la sonde : ils touchent
la **lecture de son relevé**, donc la porte du mode réel du pilote. A-1 : la sonde peut confirmer à tort la règle de comptage
d'Astra (porte ouverte à tort, cas étroit). A-2 : elle refusera sans doute Argon sur une forme de réponse que la commande et le
relais admettent (porte fermée à tort, cas probable). **Avant le pilote**, donc : A-1 fermé par une lecture écrite de la mère
(section 6) ou par le code ; A-2 par le code si le cas se présente. Un code v71 du seul module de la sonde est probable ; la
commande et le relais n'ont pas à changer, donc le relevé fait sous la v70 peut rester la pièce, sans seconde dépense.

## 1. Intégrité (conforme)

| contrôle | résultat |
|---|---|
| branche `prep/pilote-mr2-v1` | tête `c1af9438032bcf38062e0b5097719743af8a1aa3` |
| 18 compagnons du dossier `code-v70/` | tous « OK » (`sha256sum -c`) |
| chaîne des paquets | dépôt public `94bfd92` → v65 `4660197e…` (tête `cef5ea60`) → v66 (`7e415cba`) → v67 (`ab53b7f4`) → v68 (`276b6afd`) → v69 (`2ca17ea3`) → v70 `838ddd2c…` (tête `932a5ffc2459c4cd5bb1dc45e9102af8078274bb`) ; chaque paquet égal à son compagnon, `git bundle verify` conforme, prérequis égal à la tête précédente |
| ajouts seulement | `git diff --name-status 2ca17ea 932a5ff` : dix « A », aucun fichier d'avant modifié |
| différentiel v2 | recalculé (dix paires, ordre du rapport) : `ce225d6e…`, **égal à l'octet** |
| patch | `git format-patch --stdout 2ca17ea..932a5ff` : `c84f5d3f…`, **égal à l'octet** |
| code gelé entre le jalon 1 et la tête | identique (`git diff --stat 9613640 932a5ff` : les essais et le banc seulement) |
| bloc gelé | `bloc` sans relevé, rejoué : 45 lignes, **égal à l'octet** à `EMPREINTES-code-pilote-v70.txt` (`16a368b6…`) |
| W1 à W5 du banc | égales mot pour mot à celles de l'outil du contre-lecteur précédent (`mutations_contre_lecteur_v69_v1.py`) |
| lignes s1 et s2 | absentes de `registres/go.md` (aucune ligne à 4,39 ni 3,68 USD) |

## 2. Ce que j'ai rejoué

Pièces dans `contre-lecture-code-v70-outils/` (à côté de ce rapport), chacune avec son compagnon.

- **Essais** (`essais-109-contre-lecteur-v70.txt`), dans mon arbre reconstruit, environnement vidé :
  `109 passed, 166 subtests passed in 222.44s (0:03:42)`, code 0 (21:30:23 → 21:34:06).
- **Mutations** (`mutations-contre-lecteur-v70-v1.json`, journal `…-journal.txt`), par le banc du développeur, quinze dont M23
  et les cinq du contre-lecteur précédent :

| # | garde mutée | fichier | issue | essai qui tue |
|---|---|---|---|---|
| M23 | borne de sortie au-delà de ce que paie le plafond de session | proposeurs | tuée (raison attendue) | `Configuration.test_artefacts` |
| W1 | l'environnement entier passe au relais | proposeurs | tuée (raison attendue) | `test_environnement_du_relais_w1` |
| W2 | l'engagement ne lie plus le fichier des mondes | cœur | tuée (raison attendue) | `test_artefact_engagement_autre_fichier_des_mondes_w2` |
| W3 | consigne lue par la commande non comparée | proposeurs | tuée (raison attendue) | `test_artefacts_temoin_un_par_un` |
| W4 | gabarit du texte servi non relu | cœur | tuée (raison attendue) | `test_artefacts_texte` |
| W5 | manifeste altéré admis à la mesure | lanceur | tuée (raison attendue) | `test_mesure_manifeste_altere_w5` |
| D1a | règle des graines écrite avec l'étiquette v68 | cœur | tuée (raison attendue) | `RegleDesGraines.test_sain` |
| D2a | coût excessif sans arrêt | proposeurs | tuée (raison attendue) | `test_cout_excessif_arret` |
| D2g | relais sans verrou | relais | tuée (raison attendue) | `test_cout_excessif_arret` |
| D3a | `mesurer` : fichier des mondes libre | lanceur | tuée (raison attendue) | `test_mesure_autres_mondes_d3` |
| D4a | relevé non validé en mode réel | lanceur | tuée (raison attendue) | `test_sain_bout_en_bout` |
| D4h | conclusions du relevé non recalculées | sonde | tuée (raison attendue) | `test_artefacts_releve` |
| D4n | verdict d'Astra sans seuil | sonde | tuée (raison attendue) | `test_verdicts` |
| D4o | lignes de GO de la sonde non lues | lanceur | tuée (raison attendue) | `test_artefacts_sonde` |
| d7b | graine ignorée au rapatriement | audit | tuée (raison attendue) | `test_rapatriement_artefacts` |

  Essais sains sur la copie non mutée : code 0, aucun échec. Ligne de résumé du banc : `{"tuée (raison attendue)": 15}`, code 0
  (21:34:37 → 21:49:32). M23, survivante d'un passage interrompu du développeur, est bien tuée sur la tête `932a5ff`.

- **Épreuves directes**, sans réseau (`epreuves_contre_lecteur_v70_v1.py`, `epreuve_argon_champ_absent_v70_v1.py`,
  `lignes_go_sonde_contre_lecteur_v70_v1.py`, `chiffres_contre_lecteur_v70_v1.py` et leurs sorties), citées E1 à E3.
- **Essais par la ligne de commande** (`essais-ligne-de-commande-contre-lecteur-v70-v1.txt`), cités F1 à F10.

## 3. Les constats de la contre-lecture précédente, un par un

Lignes : celles de la tête v70 (`orchestrator/…`).

| constat | jugement | où | preuve |
|---|---|---|---|
| **D-1** règle des graines | **corrigé** | `pole/pilote_mr2_v70.py` l. 90-98 (étiquette figée, `REGLE_EPISODES` bâtie depuis la constante), l. 284 (dérivation) ; lanceur l. 76-78, l. 114 (ligne du bloc), l. 153 (manifeste) | la règle écrite dit ce que fait la ligne 284 (16 octets, gros-boutiste, étiquette, barre, empreinte en hexadécimal) ; `test_regle_des_graines_redonne_les_episodes` passé ; D1a tuée |
| **D-2 (a)** coût au-dessus du pire cas | **corrigé** | `pole/proposeurs_pilote_v70.py` l. 41-42, l. 359-361 ; lanceur l. 279-284 ; relais l. 377-378, l. 409-415 | arrêt du pilote, l'appel au relevé, relais verrouillé ; D2a et D2g tuées |
| **D-2 (b)** réflexion comptée deux fois | **corrigé sous condition de la sonde** | commande l. 133-171 ; relais l. 101-118 ; configuration v11, `reflexion_comprise` | la règle est un champ gelé ; elle n'est pas vérifiée (écart 2, section 4) ; réserve A-1 |
| **D-3** `mesurer` et `lire` liés aux mondes du manifeste | **corrigé** | lanceur l. 395-397 et l. 403 (`mesurer`), l. 435-436 et l. 444-446 (`lire`) | D3a tuée ; essais `test_mesure_autres_mondes_d3`, `test_mesure_manifeste_mondes_d3`, `test_lecture_artefacts` passés |
| **D-4** rien n'attend de confirmation | **corrigé, avec deux défauts neufs dans la lecture du relevé (A-1, A-2)** | `pole/sonde_pilote_v70.py` l. 244-284 (`exiger_releve`) ; lanceur l. 196-210 (mode réel), l. 322-380 (`sonde`), l. 115-118 (bloc) | F2 à F5, E1a à E1e ; D4a, D4h, D4n, D4o tuées |
| **D-5** cinq gardes sans artefact | **corrigé** | W1 : relais l. 312, l. 355, l. 467 ; proposeurs l. 419-421, l. 448-450 ; W2 : cœur l. 887-897 ; W3 : proposeurs l. 272-279 ; W4 : cœur, `verifier_texte_servi` (l. 728 et suivantes) ; W5 : lanceur l. 392-394 | W1 à W5 **tuées** chez moi, chacune par l'essai écrit pour elle |
| **d-1** `recrite` au manifeste | corrigé | cœur l. 718-720 | public : `admise` et `loi_sha256` seulement |
| **d-2** délai de l'adaptateur compté 0 | corrigé | proposeurs l. 309-312 | compté au plafond de session |
| **d-3** raison d'arrêt effacée ; délai par lecture | corrigé, une limite (a-8) | relais l. 150-156, l. 165-170, l. 204-209 | le délai total n'est contrôlé qu'à l'arrivée d'une ligne |
| **d-4** `CARTES-partiel.json` | corrigé | `pole/audit_pilote_v70.py` l. 35 | pièce permise |
| **d-5** refus du scénario après le dossier | corrigé | lanceur l. 200-201 | dans `exiger_mode_reel` ; F5 et F6 : aucun dossier créé |
| **d-6** huit chiffres quelconques | corrigé | commande l. 71, l. 104-126 | `-99999999` et `-20261301` refusés, `-20261101` et `-2026-11-01` admis (sortie des chiffres) |
| **d-7** loi ou graine dans un fichier au nom permis | corrigé, fermé par excès (a-6) | audit l. 38-41, l. 89-126 ; lanceur l. 471-474, l. 552-555 | d7b tuée |
| **d-8** 7,98 et non 7,97 | corrigé au rapport | rapport du développeur, section 10 | recalculé : 7,975968 à la borne gelée, 8,052896 avec la borne courte ; parts 2,59 / 1,80 / 1,84 / 1,84 ; s1 4,39 ; s2 3,68 |
| **point (7)** doublure non signalée | corrigé | lanceur l. 244-245, l. 301, l. 309, l. 456-457 | mode `reel_sur_doublure` au manifeste et au relevé, recopié par `lire` |

## 4. Les trois écarts écrits du développeur

**Écart 1 — l'empreinte du relevé au bloc gelé, pas à la configuration : acceptable.** La garantie demandée tient par un autre
chemin : `bloc --releve-sonde` ne rend un bloc que si le relevé passe `exiger_releve` (lanceur l. 118 ; F2 à F4 : refus, code
2) ; le texte scellé recopie ce bloc ; le mode réel recalcule le bloc avec le relevé qu'on lui passe et exige l'égalité (lanceur
l. 208-210). Un texte scellé sur le bloc provisoire (« absent ») ne peut jamais partir. Une configuration v12 n'aurait rien
ajouté. Limite, dite en a-2 : le relevé n'est lié qu'à la commande, au relais et à l'identité des proposeurs, pas à l'empreinte
de la configuration ni du code.

**Écart 2 — la règle de comptage écrite de mémoire, le mode réel refusant tant que la sonde ne l'a pas confirmée : acceptable,
avec la réserve A-1.** Vérifié dans le code : `exiger_mode_reel` exige l'option (l. 196-199), puis `exiger_releve` (l. 208), qui
recalcule les conclusions depuis les champs bruts et exige `verdict_egal_a_la_regle` (sonde l. 209, l. 275-283). Vérifié par
essai :

- F5 : `jouer --mode reel` sans `--releve-sonde`, toutes les autres options données : `refus : mode réel : options exigées
  absentes : ['releve_sonde']`, code 2, aucun dossier.
- E1a : relevé absent : refus. E1c : Astra, réflexion ajoutée en vrai (2 jetons de sortie, 300 de réflexion) : `astra ne confirme
  pas ['verdict_egal_a_la_regle'] (verdict … non_comprise, règle gelée : True)`. E1d : Argon, réflexion comprise en vrai : refus.
  E1e : aucune réflexion aux deux appels : `indetermine`, refus. F2 et F3 : `bloc --releve-sonde` refuse ces mêmes relevés.
- E1b : un relevé conforme à la règle est admis.

La réserve : la confirmation n'est pas sûre dans une zone étroite (A-1). Et pour Claude la sonde ne vérifie rien de la règle
(« sans champ ») : elle vérifie seulement que la sortie comptée tient sous 256 jetons, ce qui est la question utile.

**Écart 3 — les prix hors du code : acceptable, à écrire au texte.** Le code ne peut pas lire la console. Le relevé donne, par
appel, les jetons bruts et le coût calculé aux prix de la configuration. Deux remarques : (i) rien dans le code n'attend ce
rapprochement, il doit donc être un préalable écrit du texte et une ligne de la décision de la mère avant `bloc
--releve-sonde` ; (ii) sur une sonde de quelques centimes, la console arrondie peut ne pas trancher un prix par million de
jetons : mieux vaut que Lazar lise aussi le barème affiché des quatre modèles. Le plafond n'est dur que si les prix sont les
vrais.

## 5. Dépense sans ligne : les chemins

Un seul endroit du code v70 ouvre une connexion vers un fournisseur : `appel_reel` du relais (l. 185-213), atteint seulement
si le relais est lancé avec un appelant égal à son dialecte et si la variable de clé est dans son environnement. Aucun code de
location de machine (ni Vast.ai ni Hetzner) dans les sept fichiers. Qui lance un relais ainsi :

| chemin | garde | jugement |
|---|---|---|
| `sonde` (lanceur l. 322-345) | configuration de l'arbre seulement (aucune option) ; `lire_go_de_la_sonde` (l. 332) **avant** le dossier (l. 336) et les relais (l. 343) : deux identifiants distincts, type calcul, accordé par Lazar, période de validité, aucune extension, montant **exact** (4,39 et 3,68), périmètre avec « sonde » et « crédits de Claude » ou « hors crédits » ; puis état de chaque relais (plafond = part, deux appels, clé présente) avant le premier appel | tenu. F7 à F10 : refus, code 2, aucun dossier. D4o tuée |
| `jouer --mode reel` | `exiger_mode_reel` (l. 193-218) avant tout : options, configuration de l'arbre, numpy, texte scellé, relevé de la sonde, bloc, lignes π1 et π2, engagement des mondes, un seul lancement par texte | tenu. F5, F6 : refus sans dossier |
| `jouer --mode a_blanc` | appelant « factice: », donc amont en mémoire et aucune clé passée au relais (proposeurs l. 378-381 ; relais l. 465) | aucun appel possible |
| essais et banc | doublure de la boucle locale sur une copie de l'arbre, clés factices, environnement bâti par l'essai | aucun appel réel, même lancés avec un environnement plein |
| **relais lancé à la main** | aucune | limite connue (a-7) : la garde vit dans le lanceur ; le crochet `garde_calcul.py` ne regarde que les locations de machine |

Les lignes de la sonde ne peuvent pas servir au pilote ni l'inverse (montant exact ; épreuve des lignes : refus). Les lignes
proposées par le développeur, recopiées mot pour mot, sont lues à 4,39 et 3,68 USD — **à condition d'inscrire l'identifiant
nu** : avec « (s1) » dans la cellule de l'identifiant, comme dans son modèle, la ligne n'est pas reconnue et la sonde refuse
(épreuve des lignes).

Un manque : rien n'empêche de rejouer la sonde sous les mêmes lignes (a-1).

## 6. Constats neufs

### Majeurs

**A-1 — La sonde peut confirmer à tort la règle de comptage d'Astra (et celle d'Argon si `totalTokenCount` manque).**
Où : `pole/sonde_pilote_v70.py` l. 89-93 (`verdict_reflexion`), l. 201 (appliqué aux deux appels), l. 185-190.
Le critère « comprise » est : sortie ≥ réflexion et écart ≤ 32. Il suppose une réponse d'un mot, mais il est appliqué aussi à
l'appel à 256 jetons, dont la réponse est longue ; et il ne demande pas que la réflexion dépasse 32 jetons. Deux mondes où la
réflexion d'Astra est **ajoutée** (non comprise), règle gelée « comprise » :
- E2a : appel d'un mot, 3 jetons de sortie et 2 de réflexion ; appel court, 130 et 126 : verdict « comprise », relevé **admis**.
- E2b : aucune réflexion à l'appel d'un mot (indéterminé) ; appel court 130 et 126 : verdict « comprise », relevé **admis**.
- E2c (réflexion nette à l'appel d'un mot, 2 et 300) : « contradictoire », refus : la garde tient là.
Conséquence si le cas se produit : le mode réel part avec une sortie d'Astra sous-comptée, le plafond n'est plus dur. Le cas est
étroit : il faut que la documentation citée de mémoire soit fausse et que l'appel d'un mot ne tranche pas.
Correctif (module de la sonde seul) : le critère d'Astra, et celui d'Argon sans total, ne juge que l'appel à la borne gelée ;
« comprise » exige réflexion > 32 et réflexion ≤ sortie ≤ réflexion + 32 ; « non comprise » exige sortie ≤ 32 < réflexion ; tout
le reste « indéterminé ». Un artefact par cas (E2a, E2b).
**Sans code neuf**, avant `bloc --releve-sonde` : la mère lit au relevé les champs bruts d'Astra à l'appel `borne_gelee` et
n'accepte que `reasoning_tokens` > 32 avec `completion_tokens` entre `reasoning_tokens` et `reasoning_tokens` + 32 ; elle
l'écrit au registre. Sinon : nœud.

**A-2 — La sonde lit l'usage d'Argon plus durement que la commande et le relais : un appel court tout en réflexion sera
refusé.**
Où : `pole/sonde_pilote_v70.py` l. 98-100 (`usage_entier` exige `candidatesTokenCount` présent), l. 108-111 ; contre la
commande l. 149-150 et le relais l. 109 (champ absent lu 0).
Preuve : E3. Corps d'Argon tronqué à 256 jetons, tous de réflexion, sans `candidatesTokenCount` (un champ nul peut être omis
du JSON ; je le crois courant, non vérifié) : la commande lit 256 jetons de sortie, usage entier ; le relais lit (21, 256) ; la
sonde conclut `usage_entier` faux et `borne_tenue` faux. Le relevé est alors refusé par le mode réel alors que le fournisseur
tient sa borne et que le pilote lirait cette réponse sans peine. C'est le cas que l'appel à 256 jetons cherche à produire.
Sens de l'erreur : porte fermée à tort ; aucune dépense, aucun résultat faussé ; un tour de plus.
Correctif (module de la sonde seul) : la sonde compte la sortie par la fonction même de la commande gelée (`lire_dialecte`,
déjà chargée pour la règle des identifiants, l. 46-52), et garde à part les champs bruts avec la liste des champs absents ; un
artefact (E3).

### Mineurs

- **a-1** Aucun registre des lancements pour la sonde : elle se rejoue sous les mêmes lignes tant qu'elles sont valides, 8,05
  USD au pire à chaque fois (lanceur l. 330-336). Le pilote a cette garde (l. 213-217). Correctif : la même, par identifiant de
  ligne. D'ici là : la ligne dit « une seule exécution », toute reprise est un nœud.
- **a-2** `exiger_releve` ne compare ni `configuration_sha256` ni `code_sha256` du relevé à ceux de l'arbre, et ne relit pas
  les pièces des appels (réponses brutes, corps du relais) contre les empreintes du relevé. E1b : un relevé bâti à la main, sans
  aucune pièce, est admis. La protection est ailleurs (texte scellé, contre-lu) : la mère vérifie donc, au versement, les
  pièces contre le relevé et la ligne de dépense au journal des relais. Correctif : comparer les deux empreintes ; `bloc
  --releve-sonde` relit les pièces du dossier.
- **a-3** Un arrêt levé par `appeler` sans porter l'appel (témoin d'isolement non conforme, corps du relais absent, proposeurs
  l. 320-350) laisse un appel payé hors du relevé et hors de la dépense (lanceur l. 281-284 pour le pilote, l. 358-360 pour la sonde). D-2 n'a corrigé
  que le coût excessif. Le journal du relais le porte : le rapprochement des coûts le montre. Correctif : porter l'appel à
  toute `ArretPilote` levée après l'envoi.
- **a-4** La consigne d'un mot (« Réponds par le seul mot OK. ») peut ne faire réfléchir ni Astra ni Argon : verdict
  « indéterminé », mode réel refusé, sonde à refaire (limite dite par le développeur). Avec A-1 corrigé, c'est plus probable
  encore. Correctif, si une configuration v12 se fait : une consigne à réponse d'un mot qui demande un calcul.
- **a-5** Prix : voir l'écart 3 (console arrondie, barème à lire).
- **a-6** d-7 ferme par excès : un nombre de vingt chiffres ou une clé nommée `"graine"`, `"secret"` ou `"phrase"` dans une
  carte d'un modèle refuse tout le rapatriement (audit l. 38-40, l. 121-122 ; « rien copié alors »). Sûr, mais la machine tourne
  pendant le nœud : à prévoir à la liste d'arrêt du texte.
- **a-7** Le relais et la commande se lancent à la main sans aucune ligne de GO ; le crochet du dépôt ne les voit pas. Inchangé
  depuis la v69. À écrire à la procédure : jamais de relais hors du lanceur.
- **a-8** d-3 : le délai total du flux n'est contrôlé qu'à l'arrivée d'une ligne (relais l. 165-170) ; un flux muet tient
  jusqu'au délai de lecture, soit deux fois le délai au pire. La commande et l'adaptateur tiennent le délai total : suffisant.

## 7. Ce qu'il faut avant la sonde, puis avant le pilote

Avant la sonde : les deux lignes inscrites avec l'identifiant nu (section 5) ; « une seule exécution » écrit à leur périmètre
(a-1) ; `--borne-courte` donné ; les trois clés exportées par leur nom dans la seule session qui lance.

Avant le pilote : lecture écrite de la mère sur A-1 ; pièces du relevé vérifiées (a-2) ; prix lus par Lazar (écart 3) ; si le
relevé est refusé pour Argon sur la forme A-2 ou si un verdict est indéterminé (a-4), code v71 du module de la sonde (A-1, A-2,
a-1, a-2), commande et relais inchangés pour que le relevé fait sous la v70 reste la pièce — décision de la mère ; le bloc
définitif change alors de toute façon.

Si la mère préfère une seule sonde, sûre d'ouvrir le mode réel : corriger A-1 et A-2 d'abord. Mon jugement reste que la sonde
peut partir sur la v70 : elle ne dépense que sous ses lignes, ses champs bruts sont gardés, et ce sont eux qui diront comment
écrire la lecture.

## 8. Ce que je n'ai pas vérifié

Les 137 autres mutations du banc (lues, non rejouées) ; le banc ne juge chaque mutation que sur l'essai attendu (dit par le
développeur) ; les essais à blanc A et B versés (lus au rapport, non rejoués) ; la génération des mondes ; toute route réelle :
identifiants servis, bornes admises, `output_config.effort`, forme réelle du flux de Claude, omission des champs nuls par Argon
(A-2), contenu de `completion_tokens` chez Astra ; les prix ; le brouillon 4 du texte et la section 11 du rapport du développeur
(ce que le texte doit changer : lue, non contre-lue ligne à ligne).

## 9. Pièces de cette contre-lecture

Dossier `docs/notes/organisme-multi-generations-v1/pilote-v1/contre-lecture-code-v70-outils/` (chemins de mon bac masqués en
« BAC »), chaque fichier avec son compagnon :

| fichier | sha256 |
|---|---|
| `essais-109-contre-lecteur-v70.txt` | `7b9cc255c4272e5ef3cae076d6547f664fe58ca38aaad15c44bac3ebf84ebec8` |
| `mutations-contre-lecteur-v70-v1.json` | `020e004a2d99cc44920a0ce4b839a1f929bf5805f5b5f5914961c3c8bc1dd8d3` |
| `mutations-contre-lecteur-v70-v1-journal.txt` | `2dc6a736e704965e60a023547b2dd837e5e943e081238d3428284b4264b8d381` |
| `epreuves_contre_lecteur_v70_v1.py` (E1, E2) | `dec551f39bbd2e39529f07c72376cade33c7bcf2fcb61ff8fd97444c8b632353` |
| `epreuves-contre-lecteur-v70-v1.txt` | `23b1a97e51b1e5a5fd1eef82a6e47762cc578a7ee5d1af90b2e16a4a8a2f837d` |
| `epreuve_argon_champ_absent_v70_v1.py` (E3) | `ac873aab5ce3c629993b53ac4b06e20de7a1030d17ca6087e405061339f4a3ee` |
| `epreuve-argon-champ-absent-v70-v1.txt` | `f06b0609aeac7885dcc381ce8d1a8066fdfcf015fe88bfd232947b762a1fb7e8` |
| `lignes_go_sonde_contre_lecteur_v70_v1.py` | `f933b2ecc529426b1b79ef1edc24034ba58d17899c0e68969ded3f83933f06aa` |
| `lignes-go-sonde-contre-lecteur-v70-v1.txt` | `21120f819adc8f574abfa9dd520002e4c7d355e117184f6e319f91cf5652ac8b` |
| `chiffres_contre_lecteur_v70_v1.py` | `76128a349b4206f1bc895313c72cedc97a2c45ca2d4c74ebe9d1ef3fee468e11` |
| `chiffres-contre-lecteur-v70-v1.txt` | `c407d52bbe88251e7356351e6278b5d588410ea7cd15e79aff64e8b82690f3a2` |
| `essais-ligne-de-commande-contre-lecteur-v70-v1.txt` (F1 à F10) | `ac4dd9cdb876e7fd0ded96eaaf856ad72ae5a90b46ca683259e0a0b6261d6166` |

Dossiers provisoires de mes runs, supprimés par leur chemin exact à la fin : mon arbre de lecture du dépôt de programme
(retiré par `git worktree remove`), mon clone de l'organisme, les copies du banc et des essais, mes épreuves. Rien d'autre n'a
été supprimé ; ni l'arbre principal ni `/home/user/wt-pilote-v70` n'ont été touchés, hormis ce rapport et son dossier
d'outils, écrits dans l'arbre principal **sans commit** (la mère verse).

Fin de la rédaction : 2026-11-13 21:50:39 UTC (`date -u`).
