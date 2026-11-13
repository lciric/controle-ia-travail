# Rapport du développeur — code v71 du pilote MR-2 (module de la sonde ; corrections de la contre-lecture du différentiel v69 → v70) — v1

- **Développeur** : modèle A (auteur), le même que celui du code v70 ; sous-agent de la session
  `session_01QPDgKgACWyCkCN8HjqwNXy`. Je n'ai pas écrit la contre-lecture de la v70 (un autre modèle que le mien).
- **Mandat** : message de la mère (code v71 du seul module de la sonde : les deux majeurs A-1 et A-2, les mineurs qui touchent
  ce module, le registre des lancements de la sonde si il tient dans le module et le lanceur ; mot de Lazar R-2604). Pièces
  lues (celles qui ont un compagnon, **égales à leur compagnon avant lecture**) : contre-lecture `contre-lecture-differentiel-code-pilote-v70-v1.md`
  (`f6bc1b0010dffa0f27757e46e1a20b02aeef847f7287f006a343631fe4121198`, sur `main`) et ses épreuves E1, E2 (`dec551f3…`) et E3
  (`ac873aab…`) ; `registres/decisions.md` R-2598 et R-2604 ; `registres/go.md`, lignes GO-2026-11-13-04 et GO-2026-11-13-05
  (sur `main`, tête `c2fab6cc`).
- **Heures** (`date -u`, 13 novembre 2026) : début 22:21:05 ; lectures ≈ 22:21 à 22:27 ; code et essais ≈ 22:28 à 22:45 ;
  essais complets 22:41:10 → 22:45:11 ; jalon 1 de l'organisme ≈ 22:45 ; banc 22:45:27 → 23:12:41 ; essais finaux 23:12:57 → 23:16:51 ;
  fin : 23:22:34 (dépôt du rapport).
- **Aucune dépense, aucun appel de modèle, aucune machine, aucune clé lue ni affichée ; la sonde n'a pas été jouée** (seulement
  sur la doublure des essais : boucle locale, clés factices posées par les essais). Réseau : une récupération git à refspec
  explicite (`refs/heads/prep/pilote-mr2-v1` du dépôt de travail, pour comparer la branche avant le commit) et la poussée de cette
  seule branche, par refspec explicite ; rien d'autre. Lancements d'essais et de banc sous `env -i` (PATH, OMP_NUM_THREADS=2,
  HOME et TMPDIR de mon bac), un processus de calcul à la fois, `ulimit -v 6000000`. Aucun refus de permission, de classifieur
  ni de crochet.

## 0. Verdict

**Code v71 écrit : nouveau module de la sonde (`pole/sonde_pilote_v71.py`) et nouveau lanceur (`demonstrations/pilote_mr2_v71.py`,
qui charge ce module et porte le registre des lancements de la sonde) ; rien d'autre ne change : cœur, proposeurs, audit,
commande, relais et configuration v11 sont ceux de la v70, à l'octet. A-1 et A-2 corrigés ; a-1, a-2 et a-3 corrigés pour la
sonde ; a-4 à a-8 hors du module (dits un par un, section 3). Essais : 115 passés, 195 sous-essais passés, en 234,60 s. Banc restreint à la sonde : 46 mutations, **46 tuées pour la raison attendue**.**
Le bloc gelé versé (`EMPREINTES-code-pilote-v71.txt`) dit « relevé de la sonde absent » : il est **provisoire** ; le bloc à
recopier au texte sera celui que rend `bloc --releve-sonde` après la sonde, jouée sous ce code (le relevé porte désormais les
empreintes du code et de la configuration qui l'ont fait, a-2 : un relevé fait sous la v70 ne serait pas lu par la v71).

## 1. Arbre, branche, fichiers

- Arbre de l'organisme : `/home/user/pilote-v70/organisme` (chaîne v65 → v70 vérifiée pour la v70) ; branche
  `prep/organisme-v71-pilote-mr2-v1` partie de `932a5ffc2459c4cd5bb1dc45e9102af8078274bb` (tête v70) ; commits `e7daf32` (seul commit : code, essais, banc ; tête `e7daf32fd090ec6be8331ee1216cec3f061e5f93`).
- Fichiers neufs (`orchestrator/`) : `pole/sonde_pilote_v71.py` (455 lignes), `demonstrations/pilote_mr2_v71.py` (593),
  `essais/test_pilote_mr2_v71.py` (2 402), `essais/mutations_pilote_mr2_v71.py` (235). **Ajouts seulement** ; aucun fichier de
  la v70 ni d'avant n'est modifié. Les noms des relais et des pièces du pilote restent ceux de la v70 (l'audit v70, inchangé,
  les rapatrie) ; le relevé de la sonde s'appelle `releve-sonde-pilote-v71.json` (version `releve-sonde-pilote-v71`).
- Pourquoi un lanceur v71 : le lanceur v70 charge `sonde_pilote_v70` par son nom ; changer de module sans réécrire un fichier
  (R12) exige un lanceur neuf. Le lanceur v71 est celui de la v70 hormis : le module chargé, ses noms (version, marqueurs du bloc,
  liste des fichiers gelés : le lanceur et le module de la sonde v71 à la place des v70), `attendu_du_releve` (a-2), la
  sous-commande `sonde` (a-1, a-2, a-3) et ses options. Le différentiel le montre (section 8).

## 2. Majeurs

| constat | issue | où (v71) | correction | essais ; mutations |
|---|---|---|---|---|
| **A-1** la sonde peut confirmer à tort « comprise » pour Astra (E2a : 3 et 2 puis 130 et 126 ; E2b : 2 et 0 puis 130 et 126 admis) | corrigé | sonde l. 135-187 (`champs`, `verdict_reflexion`, `verdict_d_ensemble`), l. 305-331 (`conclusions`) | voir ci-dessous | `SondeFonctions.test_verdicts` (E2a, E2b, E2c, E2d, chaque vote sain et artefact), `test_conclusions_des_releves_du_contre_lecteur` ; `ModeReelBoutEnBout.test_releves_du_contre_lecteur_a1` (E2a, E2b, E2c et un appel contredisant l'autre, **par la chaîne entière** : doublure, commande, relais, sonde, relevé, puis `exiger_releve` et `bloc --releve-sonde` : refus « astra ne confirme pas ['verdict_egal_a_la_regle'] ») ; A1a à A1h, D4m, D4n |
| **A-2** la sonde exige `candidatesTokenCount` présent ; la commande et le relais le lisent 0 | corrigé | sonde l. 80-131 (`usage_brut`, `champs_absents`, `corps_reduit`, `lecture_de_la_commande`, `jetons_de_l_usage`, `usage_entier`, `sortie_comptee`), l. 135-144 (`champs`) | l'usage est lu **par la fonction même de la commande gelée** (`lire_dialecte`, chargée depuis le chemin de la configuration, dont l'empreinte est vérifiée) sur un corps réduit à l'usage brut ; les champs bruts sont gardés **tels quels** (absent ≠ nul), avec la liste des champs absents ; le verdict prend les mêmes valeurs par défaut que la commande (Argon : candidats et pensées absents = 0 ; Astra : réflexion absente ou nulle = 0) | `SondeFonctions.test_lecture_de_l_usage_par_la_commande` (E3 : usage entier, 256 jetons comptés ; un champ **nul** reste illisible, comme pour la commande ; jetons de la sonde = jetons de `lire_dialecte` sur le corps entier) ; `ModeReelBoutEnBout.test_argon_candidats_absents_a2` (E3 par la chaîne entière : relevé admis, `bloc` le cite ; champ nul : refusé) ; A2a, A2b, A2c |

**A-1, la règle écrite.** Par appel, avec c la sortie du fournisseur (`completion_tokens` ; Argon : `candidatesTokenCount`), t la
réflexion (`reasoning_tokens` ; `thoughtsTokenCount`) et O les octets du texte visible (relu du corps du relais par la
commande gelée), trois votes, chacun sûr sous sa seule hypothèse :

1. t > c → « non comprise » (si la réflexion était comprise, c compterait t, donc c ≥ t) ;
2. t > 0 et c − t ≤ O + 16 < c → « comprise » (si la réflexion était ajoutée, c ne compterait que le texte visible : au plus
   un jeton par octet de texte, plus 16 jetons de forme au plus, donc c ≤ O + 16) ;
3. Argon, `totalTokenCount` entier et t > 0 : total = entrée + c + t → « non comprise » ; total = entrée + c (et t ≤ c) →
   « comprise » (règle de la v70, gardée).

Un vote : ce verdict ; deux votes différents : « contradictoire » ; aucun : « indéterminé » ; t = 0 : « indéterminé ». Sur deux
appels, un appel « contradictoire » rend l'ensemble contradictoire (la v70 l'ignorait). Le mode réel exige le verdict égal à la
règle gelée. Différences avec le correctif proposé par le contre-lecteur (critère sur le seul appel à la borne gelée, réflexion
> 32 et réflexion ≤ sortie ≤ réflexion + 32) : (i) au lieu de **supposer** une réponse d'un mot, la longueur du texte visible
est **lue** ; (ii) l'appel à 256 jetons peut trancher aussi, ce qui diminue le risque a-4 : si le modèle ne réfléchit pas sur la
consigne d'un mot mais passe la borne courte en réflexion (cas probable pour « Écris un très long texte… »), la v71 conclut sur
cet appel ; (iii) le seuil de 32 jetons de réflexion disparaît : à « OK » (2 octets), la réflexion comprise est reconnue dès
17 jetons. Hypothèse dite, la seule du vote 2 : un jeton de texte porte au moins un octet du texte rendu, et au plus 16 jetons
sont comptés sans texte visible (forme du message). Si elle tombait (plus de 16 jetons de sortie sans octet visible, la
réflexion étant ajoutée), un « comprise » à tort redeviendrait possible ; le vote 1 et le vote 3 n'en dépendent pas. Relevés du contre-lecteur, par la v71 : E2a « indéterminé », refusé ; E2b « indéterminé »,
refusé ; E2c « non comprise », refusé ; E2d (Argon sans total, 3 et 2) « indéterminé » ; un appel « comprise » et l'autre
réflexion > sortie : « contradictoire », refusé ; aucune réflexion à l'appel d'un mot et toute la borne courte en réflexion
comprise (256 et 256, rien de visible) : « comprise », admis.

## 3. Mineurs, un par un

| constat | ce que j'en fais | où | essai ; mutation |
|---|---|---|---|
| **a-1** sonde rejouable sous les mêmes lignes | **corrigé** (registre des lancements de la sonde, dans le module et le lanceur) | sonde l. 405-452 ; lanceur l. 350, l. 364, options l. 517-521 | voir section 4 |
| **a-2** relevé non lié à la configuration ni au code ; pièces non relues | **corrigé** : `exiger_releve(conf, chemin, attendu)` exige `configuration_sha256` et `code_sha256` égaux à ceux de l'arbre qui lit (`attendu_du_releve`, lanceur l. 104-108) ; huit appels exactement ; puis **chaque fait égal aux faits relus de ses pièces** (`faits_depuis_les_pieces`, l. 263-302 : réponse brute, corps du relais, témoin, chacune égale à son compagnon, le corps lié à l'empreinte de la réponse brute). Au **bloc et au mode réel** (pas seulement au bloc, comme le proposait le contre-lecteur) : un seul chemin de lecture ; le dossier de la sonde accompagne donc son relevé. La borne de chaque appel est lue de la ligne de la commande (`borne_sortie`) et comparée à la configuration (la v70 la prenait du relevé) | sonde l. 350-402 ; lanceur l. 104-108, l. 133, l. 223 | `test_artefacts_releve` : « configuration », « code », « faits_hors_pieces », « usage_hors_pieces », « borne_forgee », relevé sans ses pièces, pièce altérée, corps remplacé et rescellé ; `test_sain_sonde` (chaque fait = ses pièces) ; a2a à a2g |
| **a-3** appel payé hors du relevé | **corrigé pour la sonde** : les faits de chaque appel sont tirés de ses pièces ; à tout arrêt, l'appel en cours est porté au relevé (partiel) dès que sa réponse brute existe, sa dépense comptée ; un refus survenu après l'envoi d'un appel laisse un relevé partiel (la v70 le relevait comme un refus sans relevé quand aucun fait n'était encore écrit). **Pas pour le pilote** (`jouer`, lanceur et proposeurs) : hors du mandat ; le journal du relais le porte et le rapprochement des coûts le montre | lanceur l. 357-384 | `test_appel_parti_puis_arrete_porte_au_releve_a3` (témoin non conforme sans l'appel ; refus avant l'envoi : aucun relevé, aucun lancement consigné ; pièces altérées après l'envoi : relevé partiel) ; a3a, a3b |
| **a-4** consigne d'un mot peut ne pas faire réfléchir | **non corrigé** (la consigne est dans la configuration, gardée) ; **risque diminué** par A-1 tel que je l'ai écrit : l'appel à 256 jetons peut trancher | — | `test_releves_du_contre_lecteur_a1` (cas « courte seule ») |
| **a-5** prix | hors du code (inchangé) : la console et le barème affiché des quatre modèles à lire par Lazar avant `bloc --releve-sonde` ; le relevé le rappelle (`a_lire_hors_du_code`) | — | — |
| **a-6** d-7 ferme par excès | hors du module (audit, inchangé) : à la liste d'arrêt du texte | — | — |
| **a-7** relais et commande lancés à la main | hors du module (relais et commande inchangés, pour garder leurs empreintes) : voir section 4 | — | — |
| **a-8** délai total du flux contrôlé à l'arrivée d'une ligne | hors du module (relais, inchangé) ; la commande et l'adaptateur tiennent le délai total | — | — |

## 4. Point 6 du contre-lecteur : registre des lancements de la sonde ; relais à la main

**Registre (a-1), fait.** La sous-commande `sonde` exige `--registre-lancements FICHIER` : chemin absolu, **hors de l'arbre et
de tout dépôt git** (même règle que le registre du pilote). Avant tout dossier et tout relais : si l'un des deux identifiants de
GO figure déjà à une ligne du registre, refus (code 2), sauf **reprise écrite** : `--reprise R-NNNN --registre-decisions
registres/decisions.md`, où `R-NNNN` est **une seule** ligne du registre des décisions qui cite les deux identifiants et les
mots « reprise de la sonde », jamais employée par un lancement antérieur ; une reprise sans lancement antérieur est refusée.
Le lancement est consigné (identifiants, heure, dossier, reprise, version du module) quand les relais sont prêts, avant le
premier appel, comme pour le pilote (m-6) : un refus avant tout envoi ne consomme pas la ligne. Essais :
`SondeFonctions.test_registre_des_lancements` (fonctions : chemin relatif, dans l'arbre, premier lancement, second refusé, une
seule des deux lignes déjà employée, reprise mal écrite, ne citant pas les deux lignes, déjà servie, registre illisible) et
`ModeReelBoutEnBout.test_registre_des_lancements_a1` (par la ligne de commande : second lancement refusé sans dossier créé,
reprise admise une fois et relevé valide, reprise réemployée refusée, registre dans l'arbre refusé). Mutations a1a à a1f.
**Limite** : le registre est un fichier ; un lancement depuis une autre machine ou avec un autre fichier ne le voit pas. À écrire
à la procédure : un seul chemin, fixé (proposé en section 10), son contenu versé avec le relevé.

**Relais lancé à la main (a-7) : non fait.** La garde vivrait dans le relais (refuser de démarrer sans un jeton signé par le
lanceur, par exemple) : cela change le relais, donc son empreinte, la configuration qui la porte, et le relevé de la sonde ne
vaudrait plus pour le pilote. Hors du mandat (« commande et relais inchangés »). Reste une règle de procédure : jamais de relais
hors du lanceur ; les clés ne sont exportées que dans la seule session qui lance la sonde.

## 5. Écarts et limites, dits

1. **A-1** : critère différent de celui que proposait le contre-lecteur (section 2), plus permissif là où il est sûr (l'appel
   court peut trancher, réflexion comprise reconnue dès 17 jetons sur « OK »), plus strict là où le contre-lecteur supposait
   (la réponse d'un mot n'est plus supposée). À juger à la relecture courte.
2. **a-2** : lecture des pièces au mode réel aussi : le dossier entier de la sonde doit accompagner le relevé sur la machine
   (il est versé : section 10).
3. Le relevé lie le code entier de l'arbre (28 empreintes) : tout changement du code gelé après la sonde demande une sonde neuve
   (et une reprise écrite, ou des lignes neuves).
4. Les essais de bout en bout jouent la sonde sur une doublure ; la forme réelle des réponses (flux de Claude, champs omis,
   comptes de réflexion) reste à voir au relevé.

## 6. Essais

`essais/test_pilote_mr2_v71.py` (les 109 essais de la v70 portés sur le lanceur et le module v71, et 6 neufs) :
**115 passés, 195 sous-essais passés, en 234,60 s** (23:12:57 → 23:16:51 ; journal `essais-pilote-v71.txt`). Essais neufs :
`test_registre_des_lancements`, `test_lecture_de_l_usage_par_la_commande`, `test_conclusions_des_releves_du_contre_lecteur`
(classe `SondeFonctions`), `test_releves_du_contre_lecteur_a1`, `test_argon_candidats_absents_a2`,
`test_registre_des_lancements_a1`, `test_appel_parti_puis_arrete_porte_au_releve_a3` (classe `ModeReelBoutEnBout`) ;
`test_verdicts` réécrit (nouvelle règle) ; `test_sortie_comptee` remplacé par `test_lecture_de_l_usage_par_la_commande` ;
`test_sain_sonde` et `test_artefacts_releve` renforcés (chaque fait égal à ses pièces, verdict par appel, registre ; huit
artefacts neufs). La doublure des fournisseurs accepte des corps imposés par appel (`surcharge`) pour jouer les relevés du
contre-lecteur par la chaîne entière. Les 109 essais de la v70, rejoués sur la tête v71 (fichiers de la v70 inchangés) : 109 passés, 166
sous-essais, 215,11 s (23:16:59 → 23:20:35 ; `essais-pilote-v70-sur-la-tete-v71.txt`). Un premier passage complet des essais
v71 avant le commit (22:41:10 → 22:45:11) : 115 passés, 195 sous-essais ; un passage partiel antérieur avait montré un défaut
d'ordre des essais dans `test_sain_sonde` (registre relu après qu'un autre essai l'eut complété), corrigé avant le commit.

## 7. Banc de mutations (restreint à la sonde)

`essais/mutations_pilote_mr2_v71.py` : **46 mutations**, sur la tête `e7daf32` — les **vingt mutations de la sonde du banc
v70** (D4a à D4t ; textes ajustés au code v71 là où il a changé : D4a, D4k, D4m, D4n ; D4p, D4q, D4s, D4t visent les proposeurs
v70, inchangés) et **26 neuves** : A1a à A1h (verdict : vote « réflexion > sortie », borne basse et borne haute du vote
« comprise », marge de forme nulle, contradiction d'un appel oubliée, réflexion nulle tranchée, octets visibles ignorés, critère
de la v70 rétabli de bout en bout), A2a à A2c (candidats absents non lus comme 0 ; absent lu comme nul, en fonction et de bout en
bout), a1a à a1f (registre non lu, lancement non consigné, reprise réemployée, reprise ne citant pas les deux lignes, registre
dans un dépôt, une seule ligne déjà employée admise), a2a à a2g (configuration et code non comparés, faits non relus des pièces,
borne courte non comparée à la configuration, pièce sans compagnon, corps non lié à la réponse brute, bloc qui cite un relevé
sans le lire), a3a et a3b (appel parti non porté ; refus après l'envoi sans relevé). Méthode de la v70 : copie neuve de
`orchestrator/` par mutation, remplacement présent une seule fois (contrôle à sec : aucun défaut), essais sains d'abord sur la
copie non mutée (code 0, aucun échec), « tuée » seulement si l'essai attendu échoue, sélection resserrée sur cet essai.

**Bilan : `{"tuée (raison attendue)": 46}`, code 0, 22:45:27 → 23:12:41** (`mutations-pilote-v71.json`, journal
`mutations-pilote-v71-journal.txt`). Deux mutations (a2e, a2f) restent refusées par une garde voisine, sous un autre motif :
l'essai attendu exige le motif de la garde mutée, d'où « tuée » ; la garde voisine (faits relus des pièces) suffirait seule à
refuser ces relevés. Réserve de méthode (comme en v70) : chaque mutation est jugée sur son essai attendu, pas sur la suite
entière.

## 8. Différentiel v70 → v71, paquet, patch

- **`differentiel-v70-v71.patch`** (`26affb5b3201b6ab832b2e83c168127da7fdd0afdde7d872688055c5351e47eb`, 1 690 lignes,
  4 en-têtes) : `git -c core.quotepath=off diff --no-index --no-color A B` de chaque paire, lancé depuis `orchestrator/`, dans cet
  ordre : module de la sonde v70 → v71, lanceur v70 → v71, essais v70 → v71, banc v70 → v71 ; sorties mises bout à bout.
- Paquet **`organisme-v71-pilote-mr2-v1.bundle`** (`733368fc8f80003d4a134ca55b7ca04391f3fd6dbc0bec73f139ba2956c06a5c`) : branche
  `prep/organisme-v71-pilote-mr2-v1`, tête `e7daf32fd090ec6be8331ee1216cec3f061e5f93`, **prérequis
  `932a5ffc2459c4cd5bb1dc45e9102af8078274bb`** (tête v70, paquet v70 `838ddd2c…`) ; `git bundle verify` conforme.
- **`organisme-v71-contre-932a5ff.patch`** (`47f9fe20fcaf8742a695239c917f62490c401409ea7a9f8047b393c29031c6a8`) :
  `git -c core.quotepath=off diff --no-color 932a5ff e7daf32` — un différentiel simple et non `git format-patch`, pour qu'aucun
  message de commit (ni sa ligne d'attribution) n'entre dans un fichier versé (R-2598). Le paquet porte le commit.
- Ajouts seulement : `git diff --name-status 932a5ff e7daf32` : quatre « A » (module de la sonde, lanceur, essais, banc).
- Identifiants des proposeurs : le code, ses essais et le bloc gelé les portent tels que la configuration v11 les nomme
  (identifiants servis et demandés, noms des relais) ; ce rapport n'en écrit aucun pour l'auteur ni pour le contre-lecteur.

## 9. Bloc gelé (provisoire)

- **`EMPREINTES-code-pilote-v71.txt`** (`8e76eac8527cd6ad6a968c4ca677ffec6d6fd94b55d11d876d86f7611ba06dad`), 45 lignes,
  marqueurs `<!-- empreintes-du-code-pilote-v71 : début/fin -->`, rendu par `bloc` (sans relevé) sur la tête `e7daf32`.
  **Provisoire** : sa ligne « releve-de-la-sonde absent (le mode réel le refuse) » sera remplacée par l'empreinte du relevé
  (`bloc --releve-sonde`), seul bloc à recopier au texte.
- Différences avec le bloc v70 (`16a368b6…`) : les marqueurs (v71) et deux lignes d'empreintes — le lanceur
  (`demonstrations/pilote_mr2_v71.py`, `c1a2a55c…`, à la place de `pilote_mr2_v70.py`) et le module de la sonde
  (`pole/sonde_pilote_v71.py`, `ff6e992e…`, à la place de `sonde_pilote_v70.py`). Tout le reste est égal à l'octet : gabarit
  servi `e77d3041…`, bornes, plafonds, parts, réglages, règles de comptage, lignes π1 (20,00) et π2 (21,72), lignes s1 (4,39) et
  s2 (3,68), octets, numpy 2.5.3, règle des graines, et les 26 autres empreintes (configuration v11 `9240c624…` comprise).

## 10. La sonde : commande exacte, ordre

Lignes inscrites (sur `main`, `registres/go.md`, lignes 317 et 318), lues par le lecteur gelé au montant exact (essai à sec,
sans relais ni appel) : **GO-2026-11-13-04** (s1, 4.39 USD, échéance 2026-11-30, périmètre avec « sonde » et « crédits de
Claude ») et **GO-2026-11-13-05** (s2, 3.68 USD, même échéance, « sonde » et « hors crédits »). Pire cas inchangé : 8,052896 USD
(4,382336 sur crédits de Claude ; 3,670560 hors crédits) ; attendu : quelques centimes.

**Commande exacte** (depuis la racine du dépôt de travail, `main` à jour ; l'arbre v71 reconstruit depuis les paquets, ici
nommé `ARBRE_V71` ; les trois clés exportées **par leur nom** dans la seule session qui lance :
`RR_ANTHROPIC_API_KEY_RIGAUD`, `GEMINI_API_KEY`, `OPENAI_API_KEY`) :

```
python3 -I -B ARBRE_V71/orchestrator/demonstrations/pilote_mr2_v71.py sonde \
    --go-sonde-credits GO-2026-11-13-04 --go-sonde-hors GO-2026-11-13-05 \
    --registre-go registres/go.md \
    --registre-lancements /home/user/hors-depot/lancements-sonde-pilote-mr2.jsonl \
    --sortie /home/user/hors-depot/sonde-pilote-v71 --borne-courte
python3 -I -B ARBRE_V71/orchestrator/demonstrations/pilote_mr2_v71.py bloc \
    --releve-sonde /home/user/hors-depot/sonde-pilote-v71/releve-sonde-pilote-v71.json
```

(`python3` : un interpréteur avec numpy, celui des essais ; `/home/user/hors-depot/` : un dossier hors de tout dépôt, à créer ;
le dossier de sortie ne doit pas exister.) Essai à sec, sans relais ni appel : cette ligne, avec deux chemins de mon bac à la
place des deux chemins hors dépôt et une copie de `registres/go.md` de `main`, analysée par l'analyseur du lanceur v71, la
sous-commande remplacée par un enregistreur (options lues telles qu'écrites, aucun dossier créé) ; les deux lignes lues par le
lecteur gelé (s1 4.39, s2 3.68, échéance 2026-11-30) ; un registre vide admet un premier lancement.

**Ordre** : relecture courte de la v71 → la commande ci-dessus (une seule exécution) → dossier de la sonde versé entier (relevé,
pièces des huit appels, journaux des relais) avec la ligne du registre des lancements → console et barème lus par Lazar (prix)
→ si le relevé confirme la configuration : `bloc --releve-sonde` (refus sinon, avec la conclusion qui manque) → bloc recopié au
texte → contre-lecture → scellement. Si le relevé dément la configuration (règle de comptage, identifiant, borne, en-tête
d'espace) ou reste « indéterminé » : nœud de la mère ; une seconde sonde sous les mêmes lignes exige une reprise écrite.

## 11. Ce que le texte doit changer avant le scellement (en plus de la section 11 du rapport v70)

- « code v71 gelé » partout où la v70 était citée (lanceur `pilote_mr2_v71.py`) ; le bloc gelé « empreintes-du-code-pilote-v71 ».
- Préalable : « sonde faite sous le code v71, une seule fois (registre des lancements), relevé et pièces versés, son empreinte
  au bloc gelé ; le dossier de la sonde accompagne le relevé sur la machine ».
- Métrique : la règle de lecture de la réflexion (section 2, trois votes) au lieu de « vérifiée par la sonde » seul.
- Commande du mode réel : `jouer --mode reel … --releve-sonde RELEVE` avec le dossier de la sonde à côté du relevé.

## 12. Ce qui reste avant le premier appel

Relecture courte de la v71 par un autre modèle que le mien ; la sonde (Lazar ou la mère, sous les deux lignes) ; le relevé
versé ; les prix ; le bloc définitif ; le texte (section 11) et sa contre-lecture ; le scellement ; puis l'ordre du rapport v70
(section 11).

## 13. Nettoyage

Après la poussée de `prep/pilote-mr2-v1`, je retire par leur chemin exact : l'arbre de travail `/home/user/wt-pilote-v70`
(`git worktree remove`, permis par la mère une fois la branche poussée) et mes dossiers provisoires du bac
(`…/scratchpad/pilote-v70-dev`, `…/scratchpad/pilote-v71-dev`) ; je le dis dans mon message de fin (ce rapport est scellé avant).
Je garde l'arbre de l'organisme `/home/user/pilote-v70/organisme` (23 Mo, branche `prep/organisme-v71-pilote-mr2-v1` à
`e7daf32`) : il peut servir d'arbre v71 à la relecture ou à la sonde après vérification contre le paquet ; la mère peut le
retirer.
