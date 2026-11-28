# Vérification de la chaîne v2 de P4-instrument — lentille « dépense et arrêts » — v1

- Vérificateur neuf, le 2026-10-20, de 22:25 à 23:05 UTC environ. Je n'ai écrit ni la chaîne v1, ni la v2, ni aucune
  relecture, ni le module.
- Rapport : `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md`.
- Racine abrégée : `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/`.
- Pièces lues : `…/chaine-v2/` (sceaux compagnons tous vérifiés : chaque fichier a l'empreinte du tableau du rapport du
  correcteur) ; `…/chaine-v2/RAPPORT-CORRECTION-v1.md` ; `…/chaine-v2/NOTES-CHAINE-v2.md` (`1691bf25…`) ;
  `…/relecture-chaine-depense/relecture-chaine-depense-v1.md` ; `…/relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md`
  (constats 03 à 08) ; `…/ecrire_candidat2_v1.py` ; candidat 2 d'essai (`1398e10c…`, il porte les paires 1 à 5 de la
  chaîne v2) ; module v2 et v3 (`controler_go`, `controler_accord`, `rejouer_garde_de_calcul`, identiques dans les
  deux) ; `.claude/hooks/garde_calcul.py` ; `registres/go.md` et `registres/decisions.md` en entier ; l'en-tête de
  `registres/arrets.md`.
- Garde gelée vérifiée sur le fichier : `579f65c8ae3002d8e5c61698d636549b0401da3acff6bce718ae88e93664a6f2` dans
  l'arbre de travail et à `7a54d43` (`git show`).
- Ce que j'ai tenu : dépôt de travail lu seulement (commandes git de lecture seulement, `GIT_OPTIONAL_LOCKS=0` ; liste
  des `__pycache__` du dépôt identique avant et après, `journaux/pycache-depot-avant.txt` = `…-apres.txt`, `5cc8050f…` ;
  l'index et la tête du dépôt ont changé à 22:43:46 UTC par le commit R-302 de la session, pas par moi) ; aucun outil
  de location réel (faux outils dans le PATH des bancs ; faux `git` pour le clonage de la récupération : aucun réseau) ;
  ni `prereg/P3-consignes-v1.md`, ni aucun fichier `textes-actions-*`, ni rien sous `donnees/` ; aucune clé affichée
  (jetons factices, comptés absents de toutes les sorties) ; `-B` et `PYTHONDONTWRITEBYTECODE=1` partout ; aucun
  `__pycache__` sous mon dossier ni sous `…/chaine-v2/`.

## Verdict

**Conforme après corrections.** Toutes les décisions de la session de ma lentille sont appliquées, chacune avec ses cas
de banc ; j'ai rejoué les bancs du correcteur (arrêt, surveillance, vérifications, et les 22 cas « dépense » du
lanceur) : verdicts identiques, zéro écart. Aucune création n'est possible après un contrôle en échec (relecture du
lanceur, et écriture finale de `lancement.txt` rendue impossible : arrêt ligne 367, aucune création). Restent un
constat majeur (cinq formes voisines de révocation passent encore jusqu'à la création), trois mineurs (étiquette
« p4-v1 » suivie d'un saut de ligne acceptée par l'arrêt et la surveillance ; récupération refusée en code 2 sans état
ni heure limite ; ligne prête pour `registres/arrets.md` à cinq cellules au lieu de quatre) et quatre informations.

## Décision par décision

| décision | correction lue | cas du correcteur, rejoués ici | cas du vérificateur | état |
|---|---|---|---|---|
| RC-depense-01, RC-fidelite-06 (arrêt par identifiant) | `arreter_p4_v1.sh` (étiquette relue, `vastai stop instance`, état relu arrêté deux fois, 60 × 10 s, heure, ligne prête) ; surveillance : `sortir()` l. 107-116 sur FIN, ÉCHEC D'AMORCE, REDÉMARRAGE, ÉTAT TERMINAL, PLAFOND ; cinq minutes l. 157-165 sur tout KO | A00 à A13 ; M00 à M04c, S20, S21 ; C02 à C26 : identiques | AX02 à AX05, SX02 : conformes ; AX01, SX01 : VC2-depense-02 ; ligne prête : VC2-depense-04 | corrigé, deux réserves mineures |
| RC-depense-02 (récupération en échec) | `gardee()` l. 101-114 (état, heure limite = création + 9 600 s + 24 h) sur les sorties en code 1 ; 3 Go l. 92-95 ; liste relue jusqu'à l'absence l. 514-533 | 27 artefacts de la répétition, chacun avec état et heure limite (journal lu) | RX01, RX02 : VC2-depense-03 | corrigé sauf les refus en code 2 |
| RC-depense-03, -08, -09, RC-fidelite-03 (formes voisines ; rejeu juste avant la création ; GO à frontières) | `revocations_voisines` l. 187-210 ; `go` l. 228-232 ; lanceur l. 346-349 (garde épinglée puis `verifications go` sur les registres courants, après l'offre et le crédit) ; `GO_A_FRONTIERES` l. 91 | V42 à V59b, R00, R00b, A09, A09b ; L20 à L23, L30 à L32, G06, A18 : identiques | V00 à V12, H06 à H09, G00 à G04, XL06 conformes ; X01 à X05, XL01 à XL05 : VC2-depense-01 | corrigé pour la liste de la décision ; résidu majeur |
| RC-depense-04 (garde gelée épinglée) | lanceur `garde_intacte` l. 121-125, appelée l. 180, 346, 352 (`git diff --quiet S --` et `579f65c8…`) ; module commun l. 233-239 | G15, G15b ; L40, L41 : identiques | XG01 (garde modifiée committée dans S : refus), XG02 (arbre à l'empreinte gelée mais ≠ S : refus), XG03 (sain) | corrigé |
| RC-depense-05, RC-fidelite-05 (forme des 150 USD) | `FORME_DEPENSE` l. 89, `accord` l. 251-275 (somme au centime, Y < 150, alerte à 120) | A08 à A08g ; A16, A17 : identiques | F00 à F09 ; la phrase exacte du texte (paire 1, exemple « 47,83 … 53,24 ») est acceptée par l'expression, en NFC, sans espace insécable | corrigé |
| RC-depense-06 (surveillance) | intervalle 10 à 300 s l. 46-47 ; sommeil borné l. 149-154 ; étiquette au départ l. 67-75 ; identifiant et création lus l. 55-65 | S10…, S14 à S19 : identiques | SX02 conforme ; SX01 : VC2-depense-02 | corrigé, une réserve mineure |
| RC-depense-07 (étiquette entière avant destruction) | récupération l. 509 (comparaison en Python, exacte) | artefact « p4-v1 x » de la répétition (lu) | — | corrigé |
| RC-depense-10 (un accord, un lancement) | marqueur fixe et marqueur des traces, `set -C`, l. 108-114 et 359-366 ; branche relue l. 359-361 | M00 à M03 : identiques | XE01, XE02, XM00 conformes ; XM01 : VC2-depense-06 (information) | corrigé |
| RC-depense-11 (lignes relues avant de quitter l'arrêt sur erreur) | l. 367-377, puis `trap - ERR` l. 378 | M20, M21 : identiques | XE01 : `lancement.txt` vers `/dev/full` après le marqueur : code 2, arrêt ligne 367, aucune création | corrigé |
| RC-fidelite-04 (téléchargement et stockage à cinq minutes) | cinq minutes l. 30-31, 123-124 | C21 à C23b : identiques | — | corrigé |
| RC-fidelite-07 (arrêt du module pendant le run) | répétition, passage 5 (`duree_max_s` 0,001 s) | journal lu : passage 5 en code 1, résumé avec motif (M5), partiels poussés, récupération code 0 et destruction | non rejoué (35 minutes de suite) | corrigé |
| RC-fidelite-08 (accord après S) | lanceur l. 115-119 | N10 : identique | — | corrigé |

## Constats

### VC2-depense-01 — majeur — Cinq formes voisines de révocation passent encore, jusqu'à la création

- **Où** : `…/chaine-v2/verifications_p4_v1.py`, `revocations_voisines`, l. 198 (première cellule reconnue seulement
  sans gras : `re.fullmatch(r"go-…", k[0])`), l. 200-201 (registre des GO : seul le type est lu ; un type connu,
  par exemple « décision », dont une cellule commence par « Révocation de … », passe), l. 205 (même chose pour
  `r-\d{3,4}`), l. 207-208 (registre des décisions : seule la troisième cellule `k[2]` est lue ; une colonne omise ou
  une cellule vide en trop décale la décision). Ni `controler_go` du module (`ligne.startswith("| R-")`, `k[2]`) ni la
  garde gelée (`LIGNE_GO`, type « révocation » exact) ne les voient.
- **Cas** : `journaux/banc-voisines-v2.log` X01 (décision sans colonne de date), X02 (cellule vide en trop), X03
  (identifiant de décision en gras), X04 (identifiant de GO en gras, type « révocation », qui révoque
  GO-2026-10-20-07), X05 (GO de type « décision » dont le périmètre commence par « Révocation de GO-2026-10-20-07 ») :
  aucune ligne trouvée. `journaux/banc-lanceur-verif-v1.log` XL01 à XL05 (lanceur réel, registres d'essai) : code 0,
  une création factice chacun. Témoin XL06 (forme de la liste : tiret insécable, sans gras) : code 2, aucune création.
- **Pourquoi majeur** : même mécanisme que RC-depense-03 (dépenser contre une révocation de Lazar, sans bruit, R5).
  X05 est plausible : R-281 a fait du type « décision » le type des « autres nœuds tranchés par Lazar ».
- **Correction** (éprouvée : fonction `proposees` de `bancs/banc_voisines_v2.py`) : dans `revocations_voisines`,
  (a) retirer `*`, `_` et `` ` `` de la première cellule avant de la reconnaître ; (b) au registre des décisions, lire
  toutes les cellules `k[1:]`, pas seulement `k[2]` ; (c) au registre des GO, bloquer aussi, quel que soit le type,
  toute ligne dont une cellule commence par un début de révocation et nomme l'un des cinq identifiants. Résultat :
  X01 à X05 bloqués ; témoins V10 (mention libre) et V12 (GO de calcul qui cite la phase) passent ; **aucune fausse
  alerte sur les registres réels**, relus deux fois (go.md `0ede5bed…` puis `c0506de3…` ; decisions.md `6d033ecf…`
  puis `5d423453…`). Ajouter X01 à X05 au banc des vérifications et XL01 à XL05 au banc du lanceur ; rejouer les bancs
  et la répétition (l'empreinte du module commun change). Texte : phrases ci-dessous.

### VC2-depense-02 — mineur — Étiquette « p4-v1 » suivie d'un saut de ligne acceptée par l'arrêt et la surveillance

- **Où** : `arreter_p4_v1.sh` l. 45 (`champ` imprime la valeur), l. 51-52 (comparaison en bash de `$(…)`, qui retire
  les sauts de ligne finaux) ; `surveiller_p4_v1.sh` l. 67-75 (même forme). La relecture d'après l'arrêt, elle, compare
  en Python, exactement (l. 68-70).
- **Cas** (`journaux/banc-arrets-verif-v1.log`) : AX01, étiquette `"p4-v1\n"` : l'arrêt est demandé (1 demande), puis
  60 relectures sans reconnaissance : code 1 ; SX01 : surveillance acceptée au départ, arrêt demandé au plafond,
  code 3. Témoins AX02 « P4-V1 », AX03 « p4-v1 » suivi d'une espace, AX04 étiquette numérique : refus en code 2,
  aucune demande. Risque faible (le lanceur pose `--label p4-v1`), mais la décision dit « étiquette ENTIÈRE ».
- **Correction** : comparer dans Python et rendre un code, comme `recuperation_p4_v1.sh` l. 509
  (`sys.exit(0 if d.get("label") == "p4-v1" else 1)`), dans les deux scripts ; cas de banc `"p4-v1\n"` : code 2,
  aucune demande d'arrêt, surveillance refusée au départ.

### VC2-depense-03 — mineur — Récupération refusée en code 2 après la lecture des traces : ni état ni heure limite

- **Où** : `recuperation_p4_v1.sh` l. 92-95 (place insuffisante) et l. 115 (clonage impossible) : sortie en code 2 ;
  `gardee` (l. 101-114) n'est appelée que sur les sorties en code 1 (l. 119, l. 537). L'heure limite est pourtant
  calculée l. 91. Le texte (paire 5) dit : « Récupération en échec : aucune destruction ; la récupération écrit l'état
  de l'instance et l'heure limite de destruction ».
- **Cas** : RX01 (place 2,9 Go, faux `df`) et RX02 (clonage refusé par un faux `git`, sans réseau) : code 2, aucune
  ligne « heure limite », état non relu, aucune destruction.
- **Correction** : définir `gardee` avant le contrôle de place et l'appeler avant ces deux `exit 2` ; cas de banc
  RX01 et RX02 (attendu : code 2, une ligne « heure limite de destruction », état relu, aucune destruction).

### VC2-depense-04 — mineur (forme) — « Ligne prête pour registres/arrets.md » à cinq cellules ; le registre en a quatre

- **Où** : `arreter_p4_v1.sh` l. 84-85 ; `registres/arrets.md` l. 5 : « | date (UTC) | cible (PID ou identifiant) |
  raison | vérification après arrêt | », dates « AAAA-MM-JJ HH:MM ».
- **Cas** : AX05, ligne écrite « | 2026-10-20 | instance 99999999 (étiquette p4-v1) | P4-instrument | arrêt demandé
  par la session | arrêt par son identifiant (…) : demandé à …, relu arrêté (exited, stopped) à … | » ; le cas A00 du
  correcteur exige cette forme à cinq cellules.
- **Correction** : écrire
  `| AAAA-MM-JJ HH:MM | instance Vast.ai **ID** (P4-instrument, étiquette p4-v1 ; `vastai stop instance ID`) | MOTIF | demandé à …, relu arrêté (exited, stopped) deux fois de suite à … (arreter_p4_v1.sh) |`
  (heure de l'arrêt relu) ; A00 à quatre cellules.

### VC2-depense-05 — information — Après la création, un refus en code 2 de la surveillance ou du contrôle à cinq minutes n'arrête rien

- **Où** : `controle_cinq_minutes_p4_v1.sh` l. 47-65 (traces incomplètes, identifiant autre, tests attendus absents :
  code 2, « rien n'est arrêté ») ; `surveiller_p4_v1.sh` l. 64-75 (état illisible au départ, même passager : code 2,
  aucune surveillance) ; `arreter_p4_v1.sh` l. 47-50 (état illisible : aucune nouvelle lecture).
- **Effet** : l'instance reste en marche, seule la session veille ; le code est non nul et le message le dit (pas de
  repli silencieux). **Proposition** : une ligne de plus dans `lancement.txt` : « code 2 du contrôle à cinq minutes ou
  de la surveillance après la création : `arreter_p4_v1.sh <id> <dossier neuf>` à la main, puis nœud » ; ou trois
  lectures de l'état avant de refuser.

### VC2-depense-06 — information — Le marqueur « un accord, un lancement » vit dans le bloc-notes et les traces

- **Cas** : XM01 (marqueur fixe et dossier des traces effacés, branche absente) : seconde création factice, attendue
  par construction. XE01 et XE02 : marqueur resté après un refus, relance refusée.
- **Effet** : si le bloc-notes (`/tmp`) est perdu, la seule barrière restante est la branche de résultats, absente si
  l'instance échoue avant sa poussée initiale (scénario de RC-depense-10). Proposition, pour la version suivante ou en
  geste de session : verser la copie du marqueur avec les traces dès la création, ou pousser une référence au commit S
  avant la création (proposition d'origine de RC-depense-10).

### VC2-depense-07 — information — Formes hors de la décision : elles passent, ou bloquent, par construction

- H06 « Lazar révoque R-269 », H07 « **Suspension de R-269** », H08 « R 269 » : passent (mention libre au sens de la
  précision 5). H09 « Retrait de l'instance 56799469 du registre (R-262 inchangé) » : bloque en code 2 sans rien
  révoquer. Une ligne de registre ne se modifie jamais : une fausse alerte ne se lève que par une chaîne et un S
  nouveaux (nœud de Lazar). Aujourd'hui : aucune cellule de décision réelle ne commence par un début de révocation.

### VC2-depense-08 — information — Chemins des journaux et rejeu de la garde aux contrôles

- Les journaux livrés citent `…/chaine-v2/travail/…` (banc de l'arrêt, cas A11 ; répétition, « dépôt répété »), dossier
  déplacé depuis en `…/chaine-v2-travail/`. Sans effet sur les empreintes ; à dire au versement.
- `controles_avant_depense_p4_v1.sh` bloc 12 (l. 357-359) rejoue la garde du clone de S même si le bloc 4 a refusé son
  empreinte (le KO est déjà compté : aucune création). La phrase de la paire 3 (« avant chaque rejeu ») est exacte
  pour le lanceur ; pour les contrôles, l'empreinte est exigée mais ne conditionne pas le rejeu.

## Ce qui tient

- **Aucune création après un contrôle en échec** : chaque contrôle du lanceur sort avant la ligne 381 (`exit` sous
  `set -e` et piège ERR, ou `|| { …; exit 2; }`) ; la seule commande qui crée est l. 381 ; aucun autre script de la
  chaîne ne crée. Rejoué : 19 cas d'arrêt du rejeu du lanceur et 5 du banc du vérificateur (XL06, XG01, XG02, XE01,
  XE02), zéro création.
- **Arrêt par identifiant exécuté et vérifié** : appelé d'elle-même par la surveillance à chacune de ses sorties
  (SX02 : PLAFOND, arrêt confirmé, code 0) et par le contrôle à cinq minutes sur tout KO ; deux lectures arrêtées de
  suite ; délai borné (60 lectures) ; R10 tenu (aucune forme d'arrêt par motif ; `kill -TERM` par PID seulement dans
  `p4_instance_v1.sh` l. 174).
- **Garde gelée épinglée** : empreinte vérifiée sur le fichier et à `7a54d43` ; refus quand elle diffère de S ou de
  l'empreinte (XG01, XG02, L40, L41).
- **Accord** : forme des 150 USD lue et somme refaite (F00 à F09) ; GO à frontières de mot (G00 à G04) ; accord présent
  dans l'arbre de S refusé (N10).

## Texte à ajouter au candidat (si VC2-depense-01 est corrigé)

1. Paire 2 (revocation-voisine) : remplacer la parenthèse « (espaces libres, casse, accents ou tirets autres ; type
   « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; cellule de décision qui commence par
   « Révocation », « révoque », « annulation » ou « retrait » ; plusieurs identifiants dans une même cellule) » par :

```
(espaces libres, casse, accents ou tirets autres ; identifiant de ligne en gras ; colonne omise ou en trop ;
    type « Révocation », « revocation » ou absent de l'en-tête du registre des GO ; toute cellule d'une ligne de GO,
    de tout type, ou d'une ligne de décision qui commence par « Révocation », « révoque », « annulation » ou « retrait » ;
    plusieurs identifiants dans une même cellule)
```

2. Paire 9 (precision-5) : remplacer « une mention libre, hors de la tête d'une cellule de décision et hors d'une
   ligne de GO de type « révocation » ou inconnu, ne bloque pas. » par :

```
une mention libre, hors de la tête d'une cellule (registre des décisions, ou registre des GO de tout type) et hors
   d'une ligne de GO de type « révocation » ou inconnu, ne bloque pas.
```

## Bancs joués

Sous `…/verification-chaine-v2-depense/` : scripts dans `bancs/`, journaux dans `journaux/`, pièces par cas dans
`artefacts/` (clones d'essai, sorties, journaux des faux outils). Empreintes : `empreintes-v1.sha256`.

| banc | journal | cas | écarts |
|---|---|---|---|
| `bancs/banc_voisines_v2.py` (fonctions pures du module commun ; registres réels lus) | `banc-voisines-v2.log`, `banc-voisines-v2-registres-2.log` | 41 | X01 à X05 (VC2-depense-01) ; correction proposée : 0 écart, 0 fausse alerte |
| `bancs/banc_arrets_verif_v1.sh` (arrêt, surveillance, récupération réels ; faux outil, faux `df`, faux `git`) | `banc-arrets-verif-v1.log` | 9 | AX01, SX01 (VC2-depense-02) ; RX01, RX02 (VC2-depense-03) |
| `bancs/banc_lanceur_verif_v1.sh` (en-tête du banc du lanceur repris tel quel ; C d'essai `8f4814ad…`) | `banc-lanceur-verif-v1.log` | 14 | XL01 à XL05 (VC2-depense-01) |
| `bancs/banc_lanceur_rejeu_v1.sh` (22 cas « dépense » du banc du lanceur, recopiés tels quels) | `rejeu-banc-lanceur-v1.log` | 22 | 0 |
| `…/chaine-v2/essais_arret_p4_v1.sh`, `essais_surveillance_p4_v1.sh`, `essais_verifications_p4_v1.sh` (rejoués tels quels) | `rejeu-banc-arret-v1.log`, `rejeu-banc-surveillance-v1.log`, `rejeu-banc-verifications-v1.log` | 16, 60, 167 (21, 93, 182 lignes « CONFORME ») | 0 ; verdicts identiques aux journaux livrés, ligne à ligne (registres réels plus récents pour R00 ; le rapport du correcteur annonce 177 lignes pour les vérifications, son journal en a 182) |

`banc_voisines_v1.py` et son journal sont la première passe (deux attentes mal posées, F09 et H06 à H09, corrigées
dans la v2, sans changer aucun constat). `banc_lanceur_rejeu_v1.sh` a été réécrit une fois avant tout lancement
(bornes de lignes fausses, erreur de syntaxe).

## Limites

- Bancs sur un C d'essai et le module v2, pas sur le vrai C ; la répétition jouet (passage 5) est lue, non rejouée.
- Formats des réponses de l'outil de location : ceux de la chaîne de P3, non revérifiés ici.
- Hors lentille, non jugés : fenêtres des textes, schéma des tableaux, traces de la session, rapports attendus.
