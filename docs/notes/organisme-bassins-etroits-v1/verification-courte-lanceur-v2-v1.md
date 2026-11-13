# Vérification courte du lanceur v2 de l'atelier d'idées sur les bassins étroits — v1

Vérificateur : **Claude Fable 5.2** (`claude-fable-5-2`), le contre-lecteur du v1 (`3aaf9981…`) ; auteur des pièces : Claude
Opus 5.5. 13 novembre 2026, de 14:30 à 14:50 UTC (heures relevées par `date -u`). Demande de la mère reçue en cours de
session ; mêmes interdits que ma consigne d'origine. **Aucune dépense, aucun appel de modèle, aucun réseau, aucune opération
git dans le dépôt de travail, `.claude/` lu et non modifié, rien corrigé.** Aucun refus de permission ni de classifieur.

## Verdict

**« Autorisable »**, sous deux conditions d'emploi qui ne demandent pas de changer le fichier :

- **C1 — une seule invocation à la fois.** Une seule session lance ; jamais deux commandes du lanceur en parallèle, jamais une
  seconde avant le retour de la première (constat R1 : rien, dans le code, n'empêche deux courses de partir ensemble).
- **C2 — avant d'écrire la règle, la mère confronte le recoupement à l'idée du témoin « vrai »** (estimateur de Chao, espèces
  non vues, Good et Turing, masse manquante). S'il l'énonce, les témoins sont à changer, donc le lanceur aussi, puisqu'il les
  épingle (constat R6).

Le bloquant et les neuf majeurs du v1 sont corrigés pour de bon ; aucune garde du v1 n'est affaiblie. **Restent : 0 bloquant,
0 majeur, 9 mineurs.**

## Ce que j'ai fait

- Empreintes vérifiées : lanceur v2 `c6d82d8c…`, essais `4038ca4e…`, rapport v2 `337b2fd5…`, conception v2 `b6c7035e…`,
  témoins v2 `f1ddcef9…`, devis v2 `23077e8b…`, consigne des corrections `e9bef586…`, différentiel `1c818120…` (égal, octet
  pour octet, au `diff -u` que j'ai recalculé).
- Lanceur v2 lu en entier (1 394 lignes) ; essais lus en entier (1 075 lignes) ; conception, témoins et devis v2 lus.
- Comparaison fonction par fonction du v1 et du v2 (par l'arbre syntaxique) : 34 fonctions et 51 constantes identiques ;
  19 fonctions changées, 3 retirées, 13 neuves, toutes lues.
- **Suite rejouée : 122 passés**, aucun sauté (14:35 UTC) ; clone de l'orchestrateur resté propre.
- Trois outils scellés (`verification-outils-v2/`) : orchestrateur réel sans appel ; neuf épreuves du lancement détaché sur le
  faux orchestrateur ; huit mutations neuves.
- Un essai à part, sans effet : un processus témoin détaché (session neuve) lancé depuis une commande de ma session a survécu
  à la fin de cette commande et a fini seul 40 secondes plus tard. La prémisse de M7 tient dans ma session, sur 40 secondes.

## 1. Constat par constat

| Constat du v1 | Issue | Ce qui me le prouve |
|---|---|---|
| **B1** | corrigé | outil 1 : `construire_liste_blanche` du v2 contre l'orchestrateur réel rend la liste, compagnon vérifié ; essais B1 |
| **M1** | corrigé | `depense_course` (l. 760-801) : 0 seulement après fin propre et sans aucun dossier ; épreuve P6 ; mutants N1, N2 |
| **M2** | corrigé | seuil 10⁻⁵ (P6 : 5 × 10⁻⁶ relance, 1,1 × 10⁻⁵ et 0,01 verrouillent) ; contrôle externe 1,7 ; planchers à 3 caractères par jeton 1,4477 et 1,4769 |
| **M3** | corrigé | `bras_relancable` (l. 883-894) ; essais M3 ; épreuve P4 |
| **M4** | corrigé | `choisir_fiches_recues` ne lit plus le manifeste de fin ; doublons sur signalement seul ; toute donnée mal formée arrête |
| **M5** | corrigé | générations 2 et 3 refusées sans la confirmation scellée (l. 961-963) ; le contenu du fichier n'est pas contrôlé (voulu) |
| **M6** | décidé et écrit | la mère lit ; `lecteur`, `lu_le`, deux empreintes comparées à celles de la course ; versions `-v<N>` |
| **M7** | corrigé, quatre réserves | § 2 ; R1 à R4 |
| **M8** | corrigé par attestation | `piece_generation_1` ; neuf artefacts ; réserve R7 |
| **M9** | (a) gardé, (b) écrit, (c) et (d) refusés avec raison | § 6 ; R6. Le refus de durcir les témoins faux est fondé : l'orchestrateur impose « faux = inéligible », et un témoin plus dur ferait échouer un juge sain |
| m1, m2, m3, m6, m7, m8 | corrigés | lus ; essais ; les six survivants du v1 sont tués. m8 ne couvre que la course (R4) |
| m4, m9, m10 | écrits | conception v2 § 3.3 et § 8, devis v2 § 5 |
| m5 | refus fondé | l'étiquette `G1-R3` est nommée par la question scellée ; la tête de la pièce dit que le numéro n'est pas un rang |
| m11 | proposé | à écrire avec la règle (R8) |
| m12 | refus fondé | question scellée, cœur mot pour mot ; réserve sur le commit écrite |

m6 vérifié à part (outil 1) : la commande du bras, avec `--moteur claude-sdk --confirmer-moteur-reel`, est acceptée par
l'analyseur réel ; les treize contrôles d'arguments de `principal` sont tenus ; `verifier_commande_externe_reelle` (fonction
pure) passe ; la branche des sessions Claude n'est pas prise au bras, donc aucun relais Claude n'est exigé. **Le bras n'a
toujours été exécuté par personne**, ni réel ni simulé contre l'orchestrateur réel.

## 2. Le lancement détaché, état par état

Ce que rend la même commande, relancée (essais du v2 et mes épreuves P1 à P7) :

| État du disque et des processus | Ce que fait la commande | Code |
|---|---|---|
| superviseur vivant (course ou bras, toute génération) | rien ; compte rendu avec le PID et la commande d'arrêt | 3 |
| fini, code scellé par le superviseur | manifeste de fin scellé (« clôture »), rien d'autre | 0 |
| puis, si la dépense relevée dépasse 10⁻⁵ USD ou si le code n'est pas 0 | refus « verrouillée » | 2 |
| superviseur mort sans code scellé | clôture « mort sans fin propre » ; 20 USD (course) ou 3,1 USD (bras) comptés ; verrou | 0 puis 2 |
| PID repris par un autre processus | tenu pour mort (heure de départ du processus comparée) | — |
| superviseur fini mais non récolté (zombie) | tenu pour mort | — |
| arrêt `kill -TERM <PID du superviseur>` | signal relayé par PID ; code scellé ; clôture au lancement suivant | 0 |
| lanceur mort entre le détachement et le manifeste de départ (P2) | tout lancement refusé (« état inconnu ») ; la course tourne, non suivie | 2 |
| superviseur tué, orchestrateur encore vivant (P3) | clôture « mort » ; plafond compté ; verrou ; l'orphelin n'est pas signalé | 0 puis 2 |
| deux invocations entrelacées (P1) | **deux courses partent** ; ensuite « 2 courses réussies : nœud » | 0 et 0 |

Sûreté de l'argent : dans tous les états sauf le dernier, aucune seconde course ne peut partir et toute mort compte son
plafond. Le dernier est R1.

## 3. Mutations neuves (outil 3 ; base : 122 passés)

| Mutant | Garde affaiblie | Issue |
|---|---|---|
| V1 | PID repris tenu pour vivant | tué |
| V5 | un processus en marche ne retient que sa génération | tué |
| V14 | superviseur sans session neuve | tué |
| V15 | signaux non relayés | tué |
| V2 | zombie tenu pour vivant | **survit** |
| V3 | relance permise jusqu'à 1 USD de dépense relevée | **survit** |
| V10 | bras mort sans fin propre non compté | **survit** |
| V16 | bras précédent sans code scellé non verrouillant | **survit** (une autre garde verrouille encore) |

Le code tient ces quatre points (mes épreuves P4, P6, P7 le montrent) ; ce sont les essais qui ne les tiennent pas (R5).

## 4. Devis v2 contre le lanceur

Juste : Claude 0,4 + 4,0 + 4,0 + 1,5 = 9,9 ; hors Claude 1,7 + 1,3 + 1,9 + 2,5 + 0,6 = 8,0 ; génération **17,9** ; trois
générations **53,7** ; borne 60. Plafonds du devis et du lanceur identiques (lus par programme). Somme transmise à
l'orchestrateur 7,6 < 8 ; pire cas « course externe + bras » 8,0 ≤ 8,0 : **marge nulle**, admise par l'orchestrateur à 10⁻⁹
près. Garde de la course 400 000 caractères, inchangée.

## 5. La règle de permission et l'épingle

- Les trois règles `Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v2.py N)` sont exactes,
  sans motif ; les trois refus `Edit(//…)` ont la forme validée pour le v3. C'est ce que Lazar a accordé, à ceci près, que le
  rapport dit lui-même : **trois** commandes et non « la seule ». Rien de plus large ; le v1 ne reçoit aucune règle.
- **Insertion dans `.claude/settings.json`** (`904654c7…`, qui ne porte aujourd'hui que `hooks`) : le fragment proposé donne
  `"allow"` et `"deny"` nus ; ils doivent être placés **sous une clé `"permissions"`** au premier niveau, à côté de `"hooks"`.
  Collés tels quels au premier niveau, ils ne seraient pas lus : la commande demanderait une permission (échec sûr).
- **Insertion dans `.claude/hooks/garde_calcul.py`** (`184b3bbd…`) : l'épingle n'est décrite qu'en prose. Elle s'insère comme
  une fonction sœur de `garder_lanceur_v3`, appelée dans `decider` après elle, sans toucher à celle du v3 : motif de citation
  borné comme celui du v3 (pour que `tests/test_lancer_…_v2.py` ne soit pas une citation), égalité stricte avec l'une des
  trois commandes, dossier courant, fichier non lien, constante `c6d82d8c…` et compagnon. **Non écrite, donc non
  vérifiée** ; à écrire avant la règle `allow` ou avec elle, et à éprouver par les sept essais que le rapport nomme.
- `kill -TERM <PID>` n'est pas bloqué par le crochet (ce n'est pas un arrêt par motif) et n'a pas de règle `allow` : l'arrêt
  d'une course demandera une permission. À savoir ; ne pas élargir la règle pour autant.

## 6. Le témoin « vrai » réécrit (M9)

Chargé avec les trois autres par le chargeur réel de l'orchestrateur, aucun signal de la garde lexicale (outil 1). L'idée
(borne de Chao f1² / (2 f2) sur les groupes de doublons, éprouvée contre l'oracle) n'est ni dans la question ni dans les
faits (recherche par mots : aucun de « Chao », « espèce », « richesse », « non vu », « capture », « masse manquante »). Son
avantage tient à l'oracle du monde planté, ce qu'un juge sain note à 2 ou plus. La garde est réelle : génération 1 refusée
si l'attestation de relecture ne certifie pas `temoin_vrai_absent` ; générations 2 et 3 refusées si l'attestation de la
génération précédente ne certifie pas `temoin_vrai_absent_des_fiches_validees`. Un échec arrête donc **avant** la dépense.
Fragilité : R6.

## Constats restants (tous mineurs)

**R1 — Deux invocations entrelacées lancent deux courses.** Lanceur l. 1259 (lecture de l'état) à l. 1303 (création du dossier
de run) : aucun verrou. Épreuve P1 (entrelacement forcé à la sonde du bac à sable) : deux codes 0, deux courses jouées, puis
« 2 courses réussies : nœud ». La fenêtre réelle va de la lecture de l'état à la création du dossier (sonde du bac à sable
comprise ; durée non mesurée). Au pire, à la génération 3, les deux passent la garde de cumul avec la même dépense relevée :
la borne de 60 peut être franchie. Je le tiens pour mineur parce qu'une règle d'emploi l'écarte entièrement (C1), ce qui
n'était pas le cas des majeurs du v1. *Correction pour une version suivante* : un fichier verrou créé en mode exclusif avant
la lecture de l'état, gardé jusqu'au manifeste de départ.

**R2 — Orchestrateur orphelin non signalé** (P3). Si le superviseur meurt seul, la clôture dit « mort » alors que
l'orchestrateur vit et dépense encore ; son PID est dans `superviseur-…/pid-orchestrateur.json`, sans heure de départ du
processus, et la clôture ne le cite pas. L'argent est gardé (plafond compté, verrou). *Emploi* : après toute clôture « mort
sans fin propre », lire ce fichier et arrêter ce PID s'il vit.

**R3 — Fenêtre entre le détachement et le manifeste de départ** (P2 ; l. 1322-1342, et l. 1365-1374 au bras). Si le lanceur
meurt là, la course tourne sans manifeste : tout est refusé (sûr), mais le PID du superviseur n'est écrit nulle part.

**R4 — Au bras, une exception au détachement n'est pas gardée** (P5 ; l. 1364-1365) : trace Python, puis refus définitif
« préfixe du cache déjà présent ». Sans dépense ; nœud. m8 n'a été appliqué qu'à la course.

**R5 — Gardes d'argent sans artefact dans la suite** : mutants V3 (seuil sans dépense), V10 (bras mort compté), V2, V16.
Mes épreuves P4, P6 et P7 peuvent être reprises telles quelles.

**R6 — Le témoin vrai est une réponse naturelle à la question.** Compter les « espèces non vues » est un outil classique
pour dire combien de bassins restent. Si le recoupement l'énonce, la génération 1 est refusée ; si une seule des fiches
validées de la génération 1 l'énonce (même non transmise : le critère porte sur toutes les fiches, les cinq transmises
n'étant pas connues à l'heure de l'attestation), la génération 2 est refusée. Coût nul, mais témoins neufs, donc lanceur neuf
et nouveau cycle. D'où C2.

**R7 — L'attestation de relecture du recoupement est signée par la mère**, qui le fournit aussi : si elle l'a écrit, c'est
une attestation de soi (ma proposition M8 demandait un lecteur qui ne l'a pas écrit). À dire dans `lecteur`, ou à faire
relire.

**R8 — Règle et épingle** : clé `"permissions"` manquante dans le fragment ; épingle à écrire et à éprouver ; `-I -B` sur la
commande du crochet (m11) ; ordre d'écriture (§ 5).

**R9 — Le compte rendu et la clôture passent par toutes les gardes d'entrée** (l. 1255-1258) : après l'échéance du GO
(30 novembre), ou si une ligne du registre qui cite le GO est mal formée, la commande refuse au lieu de dire « en marche » ou
de clore. Sans dépense. De même, un superviseur qui échoue à son démarrage, ou un bras que l'orchestrateur refuse sans trace,
comptent leur plafond et verrouillent alors que rien n'a été payé : prudent, à savoir.

## Ce que je n'ai pas vérifié

- Aucune course ni aucun bras réels ; l'orchestrateur réel n'a jamais tourné sous le superviseur détaché (bac à sable, kit
  d'agent et commande d'Argon dans une session de processus sans terminal).
- La survie d'un processus détaché au-delà de 40 secondes, entre deux tours de la session, ou dans la session qui lancera.
- Le bac à sable (dit actif par la mère, non sondé par moi) ; les relais ; le compte de jetons d'Argon.
- Le recoupement et son attestation (absents) ; la confirmation de la règle de passage (absente) ; l'épingle (non écrite).
- La durée réelle de la fenêtre de R1.
- Les mutations du préparateur : résultat lu (22 tués, base passée), non rejouées.

## Outils (scellés, `docs/notes/organisme-bassins-etroits-v1/verification-outils-v2/`)

| Fichier | Empreinte SHA-256 |
|---|---|
| `verifier_orchestrateur_reel_v2.py` | `bd2878de799542491bdc4e9fd0443525d85f1a74aa53291fc90806f11e34e7dd` |
| `resultat-verifier-orchestrateur-reel-v2.json` | `fa2c67e01506cf1de721b2b8579fed9dcdded218142711e6ddc06c567a5da4fd` |
| `eprouver_detache_v2.py` | `5cc074c7846ff229787453f2cbdf9574509e1635bde99c9e042fd8fb84fb7399` |
| `resultat-eprouver-detache-v2.json` | `7ed028c44db99504baa0dd6540b5515298a8dc132bd682039dbc9bb0d8d76a10` |
| `mutations_neuves_lanceur_v2.py` | `285f07620baf81dc062726879cd3581b89a47657634b0c7143eda94a819ccf39` |
| `resultat-mutations-neuves-lanceur-v2.json` | `77bb2a09f32f78369c79a1666c7d597c21bf9c37a290f378840468a8e0f0761e` |

Fichiers relus inchangés après mes outils : lanceur v2 `c6d82d8c…`, essais `4038ca4e…`, `.claude/settings.json` `904654c7…`,
`.claude/hooks/garde_calcul.py` `184b3bbd…`.
