# Relecture de la chaîne de lancement de P4-instrument — lentille « dépense et arrêts » — v1

- Relecteur : sous-agent neuf, le 2026-10-20 (de 18:10 à 18:50 UTC environ). Je n'ai écrit ni le texte, ni le module,
  ni la chaîne.
- Racine abrégée ici en `…/p4-instrument/` :
  `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/`.
- Texte qui fait foi : `…/p4-instrument/P4-instrument-v1-brouillon4.md` (`32d821fb…`, vérifié). Plan v2 :
  `…/p4-instrument/plan-code-et-chaine-v2.md` (`7c65e4f6…`, vérifié). Le texte prime sur le plan.
- Chaîne relue : `…/p4-instrument/chaine/` ; les 27 fichiers du rendu du rédacteur ont l'empreinte qu'il annonce (vérifié
  un à un). Module de P4 appelé par la chaîne : `…/p4-instrument/module/instrument_p4_v1.py` (`6e0e026e…`), fonctions
  `controler_go`, `controler_accord`, `rejouer_garde_de_calcul`. Garde gelée : `.claude/hooks/garde_calcul.py`
  (`579f65c8…`). Registres copiés pour les bancs : `registres/go.md` (`05e7fccd…`), `registres/decisions.md`
  (`cc1b108d…`).
- Ce que j'ai tenu : dépôt de travail lu seulement (aucune écriture ; seules commandes git : `git log`, lecture ; la liste
  des `__pycache__` du dépôt est identique avant et après, `journaux/pycache-depot-avant.txt` = `…-apres.txt`,
  `7b52f3f5…`) ; aucun outil de location réel (faux outils dans un PATH de banc ; la copie du lanceur remplace `V` et le
  banc refuse de tourner s'il reste un chemin vers l'outil réel) ; HOME redirigé, clé d'API retirée, jetons factices ;
  aucun réseau ; ni `prereg/P3-consignes-v1.md` ni aucun fichier `textes-actions-*` lus (le reste de la récupération,
  qui les lit, n'a pas été joué : seul son bloc de destruction l'a été) ; aucune clé affichée.
- Transparence : l'index git du dépôt de travail a changé à 18:31:00 UTC, après le commit R-289 de la session parente
  (18:28:05 UTC). Aucune de mes commandes n'écrit l'index.

## Verdict

**Conforme après corrections.** Aucun chemin ne mène à une création après un contrôle en échec : chaque contrôle du
lanceur sort avant la création (relecture des lignes 30 à 317 ; huit cas d'arrêt du banc, zéro création). R10 est
tenu partout. Deux constats majeurs : l'arrêt de l'instance n'est ni exécuté ni vérifié par la chaîne, alors que la
recharge automatique du compte (R-283) retire le seul plafond matériel ; et des révocations écrites sous des formes
voisines de celles du texte passent sans bruit. Sept constats mineurs, deux informations.

## Ce qui tient (vérifié par les bancs de cette relecture)

- **Registre réel** : le registre des GO courant est celui que le brouillon 4 a lu (`05e7fccd…`) ; sa copie passe le
  contrôle « GO et dépense » au 2026-10-20 (V00 : échéance 2026-11-30, plafond « 10 USD par lancement… », garde
  acceptée).
- **GO cité** : GO-2026-10-20-07 seul ; huit colonnes, type « calcul », accordé par Lazar ; échéance de sa colonne
  (le jour même accepté, le lendemain refusé). La garde gelée, rejouée, refuse en plus une échéance impossible
  (2026-11-31), une date d'octroi future, une autre ligne à sept colonnes, un GO en double à espaces différents
  (V03, V04, V07, V08 : le module seul les acceptait). Registre absent, illisible ou en UTF-8 invalide, garde absente :
  refus (V09 à V12).
- **Plafond par lancement** : préfixe exact « 10 USD par lancement » exigé ; « 10 USD », espace insécable,
  « ≤ 10 USD… », « 100 USD… » refusés (V20 à V24).
- **Borne de l'étape** : strictement entre 0 et 10 USD, finie ; « 10 », « 1e1 », « nan », « inf », « -1 », « 0 »,
  « 5,41 », « abc » refusés ; 9,99 accepté (V30, V31). Le lanceur recalcule 5,41 USD depuis ses constantes.
- **Révocations aux formes exactes** : chacun des cinq identifiants, au périmètre et à la référence (V40, V41) ;
  « **Révocation de R-262** » et « **Révocation de R-269** » (V50) ; ligne de révocation à sept colonnes (V44) ; voisin
  GO-2026-10-20-071 refusé par la garde (V45, confirme T14 du rédacteur).
- **Accord du jour** : date, forme exacte, citation, doublon, identifiant, GO échu (A00 à A08).
- **Lanceur** : GO échu, plafond sans « par lancement », garde qui refuse, accord de demain, crédit `NaN`, instance de
  P4 déjà en marche (un seul lancement à la fois), instance tolérée relue « exited » mais pas « stopped » : code 2,
  aucune création (L10 à L17).
- **R10** : aucune des cinq formes d'arrêt par motif de la garde gelée dans les 4 887 lignes de la chaîne ; arrêts par
  PID (`p4_instance_v1.sh` l. 170) ou par `timeout` ; destruction par identifiant.
- **Destruction** : seulement sans KO ; refusée sur une autre étiquette, un échec de l'outil, une instance encore
  listée, une liste illisible, un outil absent (D01, D03 à D06).
- **Codes** : ceux annoncés en tête de chaque script (lanceur 0, 2, 3, 4 ; récupération 0, 1, 2, 4 ; surveillance 0, 2 ;
  cinq minutes 0, 1, 2) ; observés : 0 et 2 au lanceur, 0 et 1 au bloc de destruction, 0 à la surveillance.

## Constats

### RC-depense-01 — majeur — L'arrêt de l'instance n'est ni exécuté ni vérifié par la chaîne

- **Où** : `surveiller_p4_v1.sh` l. 15 (« Ce script n'arrête rien ») et l. 76 à 90 (cinq motifs de sortie, tous en
  code 0) ; `controle_cinq_minutes_p4_v1.sh` l. 17 et 132 ; `lancer_p4_v1.sh` l. 322 à 324 (la consigne d'arrêt est
  écrite dans `lancement.txt`, rien de plus) ; `recuperation_p4_v1.sh` l. 403 à 436 (l'état n'est relu que dans la
  branche qui détruit).
- **Cas** (`journaux/banc-depense-arrets-v1.log`) : S00, fin de l'amorce, instance en marche : sortie « FIN » en
  code 0, aucun arrêt demandé, aucun état relu ensuite. S01, plafond de 9 600 s atteint : « PLAFOND » écrit, aucun
  arrêt. D07, récupération en échec, instance en marche : aucun état relu, aucun arrêt.
- **Pourquoi c'est majeur** : la borne de l'étape (texte, Plan d'analyse, point 7 : 9 600 s × 1,30 USD) et la liste
  d'arrêt (l. 618 à 627) reposent sur « arrêt de l'instance par son identifiant ». Rien dans la chaîne ne l'exécute ni
  ne relit que l'instance est arrêtée. Après la sortie de la surveillance, plus rien ne veille. Le conteneur relance
  l'amorce à chaque sortie (arrêt de P3, `registres/arrets.md` l. 25) : l'instance reste en marche et facturée. Fait
  neuf depuis P3 : le compte se recharge seul (R-283), le crédit ne plafonne plus rien. Une instance oubliée à
  1,30 USD de l'heure dépasse le plafond de 10 USD par lancement environ quatre heures après les 9 600 s
  (10 − 3,47 − 0,22 − 1,00 = 5,31 USD de marge).
- **Correction proposée** : un script neuf `arreter_p4_v1.sh <identifiant> <dossier neuf>` : étiquette relue « p4-v1 »
  (refus sinon), `vastai stop instance <identifiant>`, état relu jusqu'à « exited, stopped » deux fois de suite (délai
  borné), codes 0, 1, 2, aucun jeton affiché. La surveillance l'appelle sur chaque motif de sortie (FIN, ÉCHEC
  D'AMORCE, REDÉMARRAGE, PLAFOND ; ÉTAT TERMINAL : relecture seule) ; le contrôle à cinq minutes l'appelle sur tout KO
  (liste d'arrêt). La récupération relit l'état au départ et refuse (code 2) une instance qui n'est pas relue arrêtée.
  Banc : cas sain ; étiquette autre ; arrêt refusé par l'outil ; état jamais arrêté ; outil absent. Si la session
  préfère garder l'arrêt à la main (comme P3), garder au moins la relecture d'état de la récupération.

### RC-depense-02 — mineur — Récupération en échec : instance gardée sans état relu ni échéance

- **Où** : `recuperation_p4_v1.sh` l. 403 (aucune lecture de l'instance s'il y a un KO) et l. 436 (message final).
- **Cas** : D07 (message « INSTANCE … NON DÉTRUITE : NŒUD DE LAZAR », sans dire si elle tourne).
- **Pourquoi** : le texte borne le disque de l'instance arrêtée à 24 heures (0,72 USD) et se tait sur l'échec de la
  récupération (T8 du rédacteur, confirmé). L'attente du nœud peut dépasser la borne sans alerte. Aucune étape ne relit
  la dépense réelle (factures) pour la comparer à 5,41 USD ; la récupération clone le dépôt entier (environ 1,2 Go)
  sans contrôle de place (1,2 à 1,3 Go libres pendant ce travail).
- **Correction proposée** : sur échec, relire et écrire l'état de l'instance et l'heure limite (création + 9 600 s +
  24 h) dans la dernière ligne ; contrôle de place avant le clonage (3 Go, comme le lanceur) ; après la destruction,
  relire la dépense de l'instance et la consigner contre la borne (`registres/depenses.md`). Au texte : une règle pour
  la récupération en échec (instance gardée arrêtée, destruction au plus tard à une échéance, nœud de Lazar).

### RC-depense-03 — majeur — Révocations sous des formes voisines : vues ni par le module ni par la garde

- **Où** : `instrument_p4_v1.py` l. 524 (`ligne.startswith("| GO-")`), l. 527 (`k[2] != "révocation"`), l. 535
  (`ligne.startswith("| R-")`), l. 537 (préfixe exact) ; appelé par `verifications_p4_v1.py` l. 112 et par le lanceur
  l. 149 et 159. La garde gelée lit les lignes avec des espaces libres (l. 41) mais ne cherche que la révocation du GO
  cité (l. 97 et 98).
- **Cas** (`journaux/banc-depense-verifications-v1.log`) : V42, ligne `|GO-2026-10-21-01|…|révocation|révoque X|…|`
  sans espace après la barre : acceptée pour X = GO-2026-10-04-08, GO-2026-10-20-06, R-262, R-269 (seule la révocation
  de GO-2026-10-20-07 est rattrapée, par la garde) ; V43, type « Révocation », « revocation », « RÉVOCATION » :
  accepté ; V51, `|R-998|…|**Révocation de R-26x**…|` : accepté ; V52 « **Révocation de R-262 et de R-269** »,
  V53 « **Révocation de R-269.** », V54 « **Révocation de la délégation R-269** » : acceptés ; C01, C02 : même verdict
  par la ligne de commande du module. `journaux/banc-depense-lanceur-v1.log` : L20 à L23, création factice.
- **Pourquoi c'est majeur** : une révocation est le levier d'arrêt de Lazar ; la manquer, c'est dépenser contre sa
  décision. La forme exacte protège l'accord (refus si la forme manque) mais ouvre la révocation (acceptation si la
  forme dévie) : repli silencieux (R5 ; en-tête de `registres/go.md` : registre mal formé, blocage). Une ligne que la
  garde lit comme ligne du registre est ignorée par le module.
- **Correction proposée** (dans `verifications_p4_v1.py go`, qui ajoute déjà ce que le module ne lit pas, ou dans
  `controler_go`) : lire les lignes comme la garde (`^\|\s*(GO-…)\s*\|`, `^\|\s*(R-\d{3,4})\s*\|`) ; comparer le type
  sans casse ni accent, et refuser toute ligne de GO dont le type n'est pas dans la liste de l'en-tête ; au registre
  des décisions, refuser toute cellule de décision qui commence par « **Révocation » (sans casse ni accent) et nomme
  l'un des cinq identifiants. La forme exacte reste celle à écrire ; la chaîne refuse plus, jamais moins. Rejouer le
  banc des vérifications et celui du lanceur avec ces artefacts.

### RC-depense-04 — mineur — Garde gelée rejouée sans relecture de son empreinte

- **Où** : `lancer_p4_v1.sh` l. 149, 157 à 160 (garde de l'arbre de travail du dépôt, par le module) et l. 314 et 315
  (`python3 "$DEPOT/.claude/hooks/garde_calcul.py"`) ; `instrument_p4_v1.py` l. 575.
- **Cas** : V60 (garde de l'arbre de travail neutralisée, `0dcc4f15…` au lieu de `579f65c8…` : GO accordé demain et
  ligne à sept colonnes acceptés) ; L40 (création factice).
- **Pourquoi** : les contrôles propres à la garde (date d'octroi, lignes mal formées, doublons) ne sont pas refaits par
  le module. Les contrôles avant dépense éprouvent la garde de S sur un clone neuf (bloc 12), pas celle que le lanceur
  rejoue au moment de la création.
- **Correction proposée** : avant le premier rejeu, exiger `git -C "$DEPOT" diff --quiet "$S" --
  .claude/hooks/garde_calcul.py` et l'empreinte `579f65c8…` (celle de `7a54d43`) ; sinon « garde de calcul
  modifiée : pas de création » (code 2). Cas de banc : garde modifiée, aucune création.

### RC-depense-05 — mineur (point du texte) — Plafond de la phase (150 USD) lu par personne

- **Où** : texte, l. 55 à 57 (« la session vérifie … et l'écrit dans la ligne d'accord », sans forme) ; aucun script de
  la chaîne ne lit `registres/depenses.md` ; `controler_accord` (l. 542 à 565) ne lit que forme, date et citation.
- **Cas** : A10 (accord qui écrit « 153,41 USD, au-dessus des 150 USD de la phase » : conforme) ; L50 (création
  factice). Confirme C5 et T6 du rédacteur.
- **Correction proposée** : une forme au candidat, par exemple « dépense de la phase 0 : `X USD` consignés + borne
  `5,41 USD` = `Y USD` < 150 USD », et un contrôle (Y = X + 5,41 < 150 ; alerte écrite si Y ≥ 120). Sinon, écrire au
  texte que ce plafond n'est gardé par aucune garde de la chaîne.

### RC-depense-06 — mineur — Surveillance : intervalle libre, étiquette jamais relue

- **Où** : `surveiller_p4_v1.sh` l. 30 (`INTERVALLE` de l'environnement, sans contrôle), l. 91 (sommeil entier même à
  quelques secondes du plafond), l. 31 (identifiant et création passés à la main), l. 50 à 59 (état sans étiquette).
- **Cas** : S02 (INTERVALLE=9000 : sommeil de 9 000 s demandé à 10 s du plafond ; la sortie « PLAFOND » arriverait
  environ 2,5 heures trop tard, environ 3,25 USD au prix plafond) ; S03 (INTERVALLE=abc : 21 sommeils en échec,
  44 appels de l'outil en 3,9 s, boucle sans pause) ; S04 (instance d'étiquette « rr-autre-projet » suivie sans refus).
- **Correction proposée** : refuser INTERVALLE hors de 10 à 300 s (code 2) ; dormir au plus jusqu'au plafond ;
  relire l'étiquette « p4-v1 » au départ (code 2 sinon) ; lire l'identifiant et la création dans `lancement.txt`, comme
  le contrôle à cinq minutes.

### RC-depense-07 — mineur — Destruction : étiquette lue mot à mot

- **Où** : `recuperation_p4_v1.sh` l. 407 à 416 (`set -- $LU`, puis comparaison du premier mot).
- **Cas** : D02 (étiquette « p4-v1 rr-autre » : instance détruite, code 0).
- **Correction proposée** : comparer l'étiquette entière dans le programme Python qui lit la réponse (sortie
  « oui »/« non ») ; cas de banc « p4-v1 x » : refus.

### RC-depense-08 — mineur — Révocation consignée pendant l'appel : seule la garde relit, pour le seul GO cité

- **Où** : `lancer_p4_v1.sh` l. 149 à 162 (GO, module, accord), l. 168 à 311 (offres, instances, crédit), l. 314 et 315
  (garde : GO cité seulement), l. 325 (création).
- **Cas** : L30 (« **Révocation de R-269** » consignée au registre des décisions pendant l'appel du crédit : création
  factice ; ordre des appels relu : offres, instances, crédit, création) ; L31 (révocation de GO-2026-10-04-08 au
  registre des GO pendant l'appel : création factice). Le cas G06 du rédacteur ne couvre que le GO cité.
- **Correction proposée** : rejouer `verifications_p4_v1.py go` sur les registres courants juste avant la création
  (après la ligne 311, avec la garde) : quelques secondes.

### RC-depense-09 — mineur — Accord : GO cité reconnu par sous-chaîne

- **Où** : `instrument_p4_v1.py` l. 557 (`GO_CITE in corps`).
- **Cas** : A09 (accord qui cite « GO-2026-10-20-071 » : « cite GO-2026-10-20-07 », conforme).
- **Correction proposée** : motif à frontières, comme pour les révocations (`(?<![\w-])GO-2026-10-20-07(?![\w-])`).

### RC-depense-10 — information — Un même accord peut servir à une seconde création le même jour

- **Où** : `lancer_p4_v1.sh` l. 121 à 129 et 162 (accord relu, jamais « consommé ») ; seule barrière : branche
  `calcul/p4-reel-v1` absente (`controles_avant_depense_p4_v1.sh` l. 186 et 187), poussée par l'instance seulement après
  son clonage (`p4_instance_v1.sh` l. 105 à 116).
- **Constat** (lecture) : une première instance qui échoue avant sa poussée initiale (jeton GitHub refusé, comme pour
  T0.4 les 4 et 5 octobre, `registres/depenses.md`) ne laisse aucune branche ; après sa destruction, un second appel
  avec le même accord passe tous les contrôles. La tête du lanceur dit « aucun relancement » ; rien ne l'impose.
- **Correction proposée** (si Lazar veut « un accord, un lancement ») : pousser depuis la session, juste avant la
  création, une référence `refs/tags/lancement-p4-instrument-v1` au commit S, et refuser si elle existe.

### RC-depense-11 — information — Ligne « creation » écrite après `set +e`

- **Où** : `lancer_p4_v1.sh` l. 318 à 324.
- **Constat** : si l'écriture de `lancement.txt` échoue (disque plein), la création a lieu quand même ; le contrôle à
  cinq minutes refusera alors de tourner (traces illisibles) et la création de la surveillance devra venir d'ailleurs.
  Le lanceur exige 3 Go libres au départ : risque faible.
- **Correction proposée** : écrire et relire ces lignes avant `trap - ERR`.

Hors lentille, une ligne : les jetons passent en argument de la commande de création (`--env`, l. 327), visibles dans
la table des processus de la machine pendant l'appel (repris de P3) ; ils ne sont jamais affichés.

## Points du texte (pour le candidat)

- **TX-1 Révocation** : dire que toute ligne que la garde gelée lit comme ligne du registre, de type « révocation » à la
  casse et aux accents près, ou toute cellule de décision qui commence par « **Révocation » et nomme l'un des cinq
  identifiants, arrête le lancement (refus plus large que la forme exacte, jamais plus étroit) — RC-depense-03.
- **TX-2 Plafond de la phase** : une forme exacte dans la ligne d'accord, ou la mention qu'aucune garde ne le lit
  — RC-depense-05.
- **TX-3 Arrêt** : qui exécute l'arrêt par identifiant (surveillance ou session) et comment il est vérifié (instance
  relue arrêtée) — RC-depense-01.
- **TX-4 Récupération en échec** : instance gardée arrêtée, échéance de destruction, nœud de Lazar — RC-depense-02.
- **TX-5 Un accord, un lancement** : à dire, ou à lever — RC-depense-10.
- Je n'ai pas rejugé T1 à T3 du rédacteur (hors lentille) ; mes bancs ont tourné sur un texte d'essai qui les corrige
  (`outils_essais_p4_v1.py candidat`, commit cité `7a54d43…`, « Tests attendus : `1102` », scripts de l'instance et
  ligne « Lancement » cités).

## Bancs joués

Tous sous `…/p4-instrument/relecture-chaine-depense/`, sur processeur, avec le Python de la session, `-B` et
`PYTHONDONTWRITEBYTECODE=1`. Chaque journal commence par l'empreinte des fichiers qu'il éprouve.

| banc (outils/) | journal (journaux/) | cas | écarts au texte |
|---|---|---|---|
| `banc_depense_verifications_v1.sh` (`5d30d573…`) : module commun `go` et `accord`, ligne de commande du module, sur une copie de `src/`, de la garde et des registres | `banc-depense-verifications-v1.log` (`a9a370b9…`) | 74 | 17 : RC-03 (12), RC-04 (1), RC-05 (1), RC-09 (1), RC-03 par la ligne de commande (2) |
| `banc_depense_lanceur_v1.sh` (`3514397d…`) : lanceur réel (trois lignes changées : DEPOT, B, V), dépôt d'essai minimal, dépôt nu local, faux outil, faux contrôles | `banc-depense-lanceur-v1.log` (`396d6377…`) | 18 | 8 : RC-03 (4), RC-08 (2), RC-04 (1), RC-05 (1) |
| `banc_depense_arrets_v1.sh` (`e6b32b58…`) : surveillance réelle, bloc de destruction de la récupération (l. 399 à 438, extrait tel quel, `7372d90b…`) | `banc-depense-arrets-v1.log` (`5f904dae…`) | 13 | 1 : RC-07 ; constats RC-01, RC-02, RC-06 établis par les cas S00 à S04 et D07 |

Dépôts jouets et artefacts : `banc-v/`, `banc-l/`, `banc-arrets/` (sorties de chaque cas, journaux du faux outil).

## Limites de cette relecture

- Les contrôles avant dépense n'ont pas été joués de bout en bout (ils relisent les données et les textes de P3) ; leur
  partie « GO et dépense » appelle le même module commun, éprouvé ici. La récupération n'a été jouée que dans son bloc
  de destruction. Le scellement, les répétitions et le contrôle à cinq minutes n'ont été relus que pour la dépense.
- Les formats des réponses de l'outil de location sont ceux de la chaîne de P3, non revérifiés ici.
- La borne de l'étape suppose un téléchargement d'environ 20 Go ; rien dans la chaîne ne le relit (point de devis, non
  vérifié ici).
