# Contre-lecture (R2) des pièces de lancement de la confirmation de Bailey — v1

Workflow `contre-lecture-pieces-confirmation-bailey`, run `wf_6e05bb10-9d6`, deux contre-lecteurs neufs, sur le commit `9b31c38d` :
`lancer-conduite-v15.py`, `poste-hetzner-v13.sh`, `construire-donnees-demarrage-v13.py`, `manifeste-local-v7.json` (sous `runs/temoin-bailey-v1-20261111/`),
et le générateur `generer-pieces-confirmation-bailey-v2.py`. Retours consignés tels quels.

## Traitement

- Aucun bloquant ; verdicts : « scellable » et « scellable après corrections ».
- Point « à corriger » (angle « exécution », point 1, fenêtre de 24 h comptée en essais) : appliqué tel que proposé, par le générateur v3
  (`generer-pieces-confirmation-bailey-v3.py`) : `DEBUT_POSTE` après la ligne « début », et la borne de 85 500 s en tête de la boucle de recherche.
  Le poste v13 régénéré ne diffère du poste relu que par ces deux lignes ; la borne est éprouvée (cas sain : essais ; au-delà : sortie à n = 1).
- Remarque « vastai accepte-t-il les champs de processeur » (angle « différences », remarque 5) : recherche à blanc avec la chaîne exacte du poste,
  `runs/temoin-bailey-v1-20261111/releve-recherche-a-blanc-poste-v13-*.txt` : code 0, offres toutes au filtre.
- Remarques sans changement des pièces (en changer serait une différence non nommée) : commentaires hérités du v12 au-dessus de `set -uo pipefail` ;
  clé `cout_avec_200_go` qui porte le coût carte et 110 Go du § 2.4 ; exclusion des `.battement` inopérante (héritée) ; `storage_cost` nul
  (hérité ; un « aucune offre » à 24 h sera rapporté comme cause technique si les états montrent un plantage) ; gardes d'entrée de la conduite au-delà
  de la liste littérale, qui ne font que refuser avant toute création ; contrôle redondant inatteignable après l'écriture du PID.
- Ordre de lancement : constructeur v13 joué dans un dossier neuf hors du dépôt, effacé après la création ; empreinte affichée par le constructeur
  comparée à celle de `poste-hetzner-v13.sh.sha256` ; relevé du § 2.5 fait par la session avant la création.

## Retour 1 — angle « différences » — verdict : scellable

J'ai contre-lu les pièces sous l'angle des différences, au commit 9b31c38d (branche claude/compassionate-meitner-d4ryyk, identique à l'origine après fetch). Je n'ai trouvé aucun bloquant.

1. Générateur. Rejoué dans le bloc-notes avec les arguments GO-2026-11-17-07, 554a74d0…7f3e (empreinte entière) et a904aa39…8c5849, il redonne les trois pièces à l'octet près : conduite v15, poste v13 et constructeur v13.

2. Manifeste v6 → v7. Exactement trois champs changent, et ce sont ceux que nomme le § 4 : B (75 → 85), commit_code (f60c2620 → a904aa391cdcf2650b747fe64e48caa0ec8c5849) et go_id (GO-2026-11-10-10 → GO-2026-11-17-07).

3. Conduite v13 → v15.
- Les différences nommées par l'addendum sont toutes là :
  - lanceur_v21 (empreinte 75cf4049…, identique à celle de a904aa39) ;
  - t_max_pilote_s=1800 passé à la conduite et exigé ;
  - relance_seule retirée, ainsi que REPRISE et TOURS_COMPLETS_PREMIERE ;
  - ANTERIEURES vide ;
  - manifeste v7 ;
  - GO neuf ;
  - noms neufs : sortie-conduite-v15, bilan-lancement-v15.json, lancement-v15.pid.
- S'y ajoutent les gardes d'entrée : empreinte de l'addendum, empreinte entière dans l'objet du GO, contrôle du manifeste, plafond de 1 800 s. Elles ne peuvent que refuser le départ (remarque 1).
- Je les ai éprouvées dans /tmp. Le GO réel passe ; elles refusent un GO sans l'empreinte entière, un manifeste à B = 75, une instance antérieure et un plafond de 1 801 s.
- La garde de durée de lanceur_v21 tient : arrêt avant le run principal si t > 1 800.

4. Poste v12 → v13. Toutes les différences sont nommées :
- empreintes de la ligne 104 portées sur la conduite v15 et le manifeste v7 ;
- commit f60c2620 remplacé par a904aa39 dans les deux lignes de garde (git cat-file -e et git diff --quiet … HEAD -- src/). L'arbre src/ de la tête est égal à celui de a904aa39 ; a904aa39 est un ancêtre de la branche ; les fichiers de CHEMINS_ARCHIVE sont identiques entre 873ab00c et a904aa39 ;
- filtre du § 2.4 : cpu_cores_effective>=32 et cpu_ghz>=2.4 ajoutés à la requête de la ligne 143 du v12, puis plafond `cout(o) <= 1.6` sur la grandeur cout du choix d'offre, avant de prendre le minimum ;
- GO_ID exporté = GO-2026-11-17-07 ;
- liste des répertoires (détaillée au point 5) ;
- noms neufs : journal /root/poste-hetzner-v13.log, offre-choisie-v13.json, poste-fini-v13.json, poste-hetzner-v13-etat.txt, lancement-v15.out, lancement-v15.err, lancement-v15.pid, bilan-lancement-v15.json, sortie-conduite-v15.

5. Liste des répertoires.
- Nom : repertoires-sortie-conduite-v15-v1.txt (<C> = sortie-conduite-v15).
- Les commandes sont mot pour mot celles du § 3. Elle est écrite après la sortie de la boucle `kill -0` et avant poste-fini-v13.json, scellée par `LC_ALL=C sha256sum` puis poussée avec son compagnon. Les deux fichiers figurent aussi dans la dernière poussée.
- Je l'ai rejouée dans /tmp sur des répertoires imbriqués et vides ; `sha256sum -c` rend « OK ».

6. Constructeur v12 → v13. Seuls changent le script assemblé (poste-hetzner-v13.sh), le nom du serveur et son étiquette.

7. Ligne de GO GO-2026-11-17-07 (lue sur origin/main).
- Type « calcul ».
- L'objet cite fb6c2f34, f9c8c66e et l'empreinte entière 554a74d0…7f3e (vérifiée par sha256sum et par scellement.verifier).
- Une seule mention « (B = 85, garde d'horloge à B − 2) ».
- Plafond 90 USD, échéance 2026-11-30, aucune révocation.
- verifier_go(go, 85) passe ; avec B = 75, il refuse.

8. Noms neufs. Aucun des noms écrits ou poussés n'existe sur la branche (git ls-files local, ls-tree de la branche distante), ni sur disque. Aucun n'est ignoré par git. Les compagnons des quatre pièces sont encore absents : c'est attendu, puisqu'ils seront scellés après cette contre-lecture.

9. Voie de dépense. Aucune hors du GO : coût plafonné à 1,6 USD/h au choix d'offre, B = 85 lu dans le manifeste et recoupé avec le GO, aucune instance antérieure.

Rien n'a été modifié dans le dépôt (git status vide) ; mes essais dans le bloc-notes sont nettoyés. Je n'ai lancé ni la conduite ni le poste, et aucune commande vastai.

Une seule limite. Je n'ai pas pu vérifier hors ligne que vastai 1.11.0 accepte les champs cpu_cores_effective et cpu_ghz (remarque 5).

### 1. remarque — runs/temoin-bailey-v1-20261111/lancer-conduite-v15.py 55-68

**Constat.** Les gardes d'entrée vont au-delà de la liste littérale du § 4 (« = v13 sans relance_seule, avec lanceur_v21, t_max_pilote_s=1800, aucune instance antérieure, manifeste v7, GO neuf, noms neufs »). Deux sont couvertes par le texte : le plafond « exactement 1 800 » (§ 4, l. 345-346) et l'empreinte de l'addendum dans l'objet du GO (§ 6, étape 2). Le contrôle du manifeste v7 (B = 85, go_id, commit_code) n'est pas nommé. Toutes ces gardes refusent seulement, avant le PID et avant toute création : aucune dépense possible. Éprouvées dans /tmp : le cas réel passe, les quatre artefacts sont refusés.

**Correction proposée.** Aucune modification du code. Dans la note de scellement, nommer ces gardes comme des refus d'entrée, sans effet sur la conduite, en renvoyant au § 4, l. 345-346 et au § 6, étape 2.

### 2. remarque — runs/temoin-bailey-v1-20261111/lancer-conduite-v15.py 88-97

**Constat.** Deux différences d'ordre, non nommées et sans effet de dépense. (a) L'existence du bilan est testée avant l'écriture du PID ; en v13, elle l'était après. (b) Le contrôle « conduite mal construite » vient après pidf.write_text. S'il tombait, le PID resterait, le poste écrirait « conduite lancée » puis « conduite terminée », sans liste des répertoires. Ce contrôle est inatteignable avec les constantes actuelles (vérifié : relance_seule None, t_max 1800.0).

**Correction proposée.** Laisser tel quel : changer l'ordre serait une différence de plus. Le dire dans la note de scellement : « contrôle redondant, inatteignable ; s'il tombait, aucune instance n'est créée ».

### 3. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 37-46, 131, 141

**Constat.** Commentaires d'en-tête hérités du v12, laissés exprès par le générateur (remplacements seulement après « set -uo pipefail »). La l. 44 dit « lance `lancer-conduite-v13.py` sous GO_ID=GO-2026-11-10-10 », la l. 46 dit « poste-fini-v1.json », la l. 131 dit « 200 Go », et la clé JSON l. 141 s'appelle « cout_avec_200_go » alors que cout prend 110 Go. Aucun effet sur l'exécution. L'en-tête des l. 2-5 nomme correctement la v13.

**Correction proposée.** Aucune modification, pour ne pas ajouter de différence. Signaler dans la note de scellement que les l. 37-46 décrivent la v1 historique et que « cout_avec_200_go » porte le coût avec 110 Go.

### 4. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 104

**Constat.** Hérité du v12, ce n'est pas une différence. Le motif d'exclusion « $BASE/sortie-conduite-v15/*.battement » est un chemin absolu dans .git/info/exclude : il ne correspond à rien. Le fichier .battement sera donc poussé, comme sortie-conduite-v13/arrets-v5.jsonl.battement est suivi aujourd'hui. Aucun effet sur la liste des répertoires ni sur la dépense.

**Correction proposée.** Rien pour cette pièce. Pour une pièce future seulement : motif relatif à la racine, `/runs/temoin-bailey-v1-20261111/sortie-conduite-v15/*.battement`.

### 5. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 148

**Constat.** Sans réseau, je n'ai pas pu vérifier que vastai 1.11.0 accepte les champs cpu_cores_effective et cpu_ghz dans `search offers`. Le relevé de 00:51Z cité au § 1 (filtre du § 2.4, deux offres) suggère que la requête a été jouée, mais il est sous la cloison et je ne l'ai pas ouvert. Si un champ était refusé : « recherche d'offres en échec » à chaque essai, puis « aucune offre en 24 h », sans aucune dépense. Si un champ était ignoré en silence : le filtre ne serait qu'une préférence (l'addendum le dit déjà), et le plafond de 1,6 USD/h resterait tenu par choisir_offre.py.

**Correction proposée.** Avant le lancement, la session consigne que le relevé releve-offres-filtre-addendum-7-20261117-0051.txt a été fait avec exactement la chaîne de requête de la l. 148, sous vastai 1.11.0 ; sinon, elle rejoue une recherche à blanc avec cette chaîne exacte (lecture seule, aucune création) et consigne le nombre d'offres rendues.

### 6. remarque — runs/temoin-bailey-v1-20261111/construire-donnees-demarrage-v13.py 49-50

**Constat.** Le corps de création est écrit sous le même nom qu'en v12, « creation-hetzner-v1.json », dans le dossier passé en argument, avec O_TRUNC. Ce fichier est hors du dépôt et n'est jamais poussé, mais un dossier réutilisé serait écrasé (R12, au sens large).

**Correction proposée.** Lancer le constructeur v13 avec un dossier neuf, hors du dépôt (par exemple un sous-dossier « hetzner-v13 »), et le consigner dans l'ordre de lancement.

### 7. remarque — runs/temoin-bailey-v1-20261111/ —

**Constat.** Les compagnons lancer-conduite-v15.py.sha256 et manifeste-local-v7.json.sha256 sont absents (attendu avant le scellement). Sans eux, le poste s'arrête à la l. 108 (« empreinte … différente : rien ne tourne ») et la conduite à la l. 63 (GardeArret de scellement.verifier). J'ai vérifié que le format de scellement.sceller (« empreinte  nom ») est lu par `sha256sum -c`.

**Correction proposée.** Après cette contre-lecture, lancer `PYTHONPATH=src python -m controle_ia.scellement sceller` sur lancer-conduite-v15.py, manifeste-local-v7.json, poste-hetzner-v13.sh et construire-donnees-demarrage-v13.py. Committer et pousser sur claude/compassionate-meitner-d4ryyk avant de construire les données de démarrage, puis vérifier que l'arbre src/ de la tête reste égal à a904aa39 (`git diff --quiet a904aa39 HEAD -- src/`).

## Retour 2 — angle « exécution et sûreté » — verdict : scellable après corrections

Rien de bloquant. Les quatre pièces ne diffèrent de leurs bases (conduite v13, poste v12, constructeur v12, manifeste v6) que par ce que nomme l'addendum 7, § 6 étape 2. Le manifeste ne change que sur B = 85, commit_code a904aa39 et go_id. Le poste change sur les noms, les deux lignes de la garde du commit, le filtre du § 2.4 (recherche et plafond de 1,6 sur cout), le GO_ID, la ligne d'empreintes portée sur la conduite v15 et le manifeste v7, et la liste des répertoires telle que le § 3 la fixe. La conduite passe à lanceur_v21, t_max_pilote_s=1800, sans relance_seule ni instance antérieure, plus des gardes d'entrée qui refusent en cas de doute. Le générateur v2, rejoué dans le scratchpad, redonne les trois pièces à l'octet près.

Essais faits (rien sur le réseau, aucune dépense) :
- bash -n et py_compile passent, le manifeste se lit en JSON.
- vastai 1.11.0 (venv local) lit la requête et ses deux champs nouveaux sans « Unrecognized field ».
- choisir_offre : 1,6 exact accepté, avec ou sans stockage ; 1,60001 refusé ; refusé aussi quand le stockage pousse au-delà ; la moins chère est retenue parmi celles qui passent.
- Bloc de la liste : 7 entrées sur une sortie factice (répertoire vide, nom avec espace, ordre C), compagnon « OK » à sha256sum -c, liste écrite hors de la sortie. Sortie absente : aucune liste, état écrit. Sortie vide : liste de 0 octet, scellée.
- pousser, sur un dépôt nu local : seuls les fichiers prévus partent (un fichier non listé de BASE reste local).
- gardes_d_entree sur la vraie ligne GO-2026-11-17-07 de origin/main (32c698e2) :
  - avec le vrai manifeste, refus aujourd'hui (compagnon manifeste-local-v7.json.sha256 absent) ;
  - avec une copie scellée du manifeste, passe ;
  - refus sur chaque artefact : empreinte tronquée dans le GO, GO absent, B = 75, go_id ancien, commit f60c2620, manifeste altéré, plafond 1799, instance antérieure, addendum altéré.
- verifier_go(85) passe, et B = 75 est refusé.
- La conduite construite porte relance_seule None, t_max 1800 et disque 110.
- src/ de la tête est égal à a904aa39, et lanceur_v21 a l'empreinte 75cf4049.
- Les noms neufs sont absents de la branche et du disque.
- L'archive du code se fabrique au commit a904aa39.
- Le dépôt n'est pas modifié ; mes essais sont effacés du scratchpad.

Un point à corriger : la fenêtre de 24 h du § 2.4 n'est pas tenue par l'horloge. Le reste est en remarques, surtout des défauts hérités du v12 qu'on ne corrige pas sans addendum.

### 1. à corriger — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 54, 147-156

**Constat.** La fenêtre « aucune offre conforme dans les 24 h qui suivent le lancement du poste : rien ne tourne » (addendum 7, § 2.4) est comptée en essais, pas en temps. L'essai n commence à environ (n−1)×(600 s + durée de la recherche et des poussées), après l'installation (apt, clonage, pip, environ 3 à 5 min après la création Hetzner). Le 144e essai part donc vers 24 h 02 à 24 h 15 après le lancement du poste. Si une offre apparaît à ce moment, la création se fait hors de la fenêtre : écart au texte scellé (rare, borné à un ou deux essais). Défaut hérité de la boucle du v12, mais le § 2.4 fait partie des différences permises.

**Correction proposée.** Dans le générateur (nouvelle version, generer-pieces-confirmation-bailey-v3.py, R12), ajouter après la ligne 54 du poste « DEBUT_POSTE=$(date -u +%s) ». Ajouter aussi, en première ligne du corps de la boucle de la ligne 147 (avant « if vastai search offers »), « [ $(( $(date -u +%s) - DEBUT_POSTE )) -lt 85500 ] || break » : 23 h 45 depuis le début du script, ce qui laisse la marge du démarrage. Puis régénérer, recomparer et faire contre-lire la différence. Autre voie : garder la v13 telle quelle et consigner dans l'ordre de lancement que la borne est de 144 essais, avec un écart possible d'environ 15 min au-delà de 24 h.

### 2. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 104, 84-87

**Constat.** L'exclusion « printf '%s\n' "$BASE/sortie-conduite-v15/*.battement" >> .git/info/exclude » écrit un chemin absolu. git le lit comme ancré à la racine du dépôt, donc il ne correspond à rien : vérifié dans le scratchpad, le fichier arrets-v5.jsonl.battement est ajouté par git add -A. Une fois suivi, le battement est réécrit toutes les 30 s par le veilleur. S'il change entre le commit et « git pull --rebase », git refuse (« cannot pull with rebase: You have unstaged changes », vérifié), et les 4 nouveaux essais échouent aussi, faute de nouvel add. Pendant la conduite, la poussée suivante (10 min plus tard) rattrape. Après la fin de la conduite, le veilleur est normalement arrêté, et les deux dernières poussées (liste, puis marque de fin) ne courent aucun risque. Il reste un risque faible (environ 1 à 3 % par poussée) quand un veilleur de destruction survit à la conduite (instance non détruite) : liste, marque et derniers transferts absents de la branche. Le § 3 traite ce cas (sans marque : destruction de la machine du poste par la session, liste absente rapportée). Défaut hérité du v12, identique.

**Correction proposée.** Aucune pour ce run : un correctif serait une différence non nommée par l'addendum 7. Le consigner dans l'ordre de lancement. Pour une version future : écrire le motif relatif à la racine (« /runs/temoin-bailey-v1-20261111/sortie-conduite-v15/*.battement »), ou utiliser « git -c rebase.autoStash=true pull --rebase ».

### 3. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 136-137

**Constat.** Dans choisir_offre.py, une seule offre avec « storage_cost »: null fait planter tout le choix (TypeError, vérifié) : code 1, compté comme « aucune offre conforme ». La trace part dans /root/poste-hetzner-v13.log, qui n'est jamais poussé. Une valeur nulle persistante donnerait 24 h d'attente et un faux « confirmation non lancée (aucune offre) ». Défaut hérité du v12 (même expression dans min()). Note aussi : dans vastai 1.11.0, le dph_total de la recherche comprend déjà 5 GiB de stockage (--storage 5.0 par défaut). cout compte donc 115 GiB, une surestimation de l'ordre de 0,001 USD/h, prudente, et c'est bien la grandeur « cout » que nomme le § 2.4.

**Correction proposée.** Aucune pour ce run (grandeur cout fixée par le § 2.4). Avant de déclarer « aucune offre » à 24 h, la session lit les états poussés ; si le doute porte sur un plantage, elle le rapporte comme cause technique et non comme absence d'offre.

### 4. remarque — runs/temoin-bailey-v1-20261111/lancer-conduite-v15.py 55-68, 88-97

**Constat.** La conduite a des gardes d'entrée en plus de celles qu'énumère le § 6, étape 2 :
- addendum 7 scellé à l'empreinte entière attendue ;
- B, go_id et commit_code du manifeste vérifiés ;
- constantes du plafond et des instances antérieures ;
- PID et bilan vérifiés ensemble avant l'écriture du PID ;
- vérification de la conduite construite (relance_seule None, t_max 1800).
Toutes refusent en cas de doute, se jouent avant l'écriture du PID et avant toute création (aucune écriture dans la sortie avant le contrôle « sortie non neuve » de conduire), et s'accordent avec le § 4 (« refuse de partir si la valeur n'est pas exactement 1 800 ») et avec le § 6 (empreinte de l'addendum vérifiée dans l'objet du GO). Essayées sur cas sain et sur artefacts (R5) : chacune tombe. La docstring de gardes_d_entree dit « lève SystemExit », alors que scellement.verifier et ligne_go lèvent GardeArret : sans effet, les deux sortent avant le PID, et le poste conclut « conduite non lancée », exit 3, poussée. Temps jusqu'au PID mesuré à environ 0,1 s, loin des 20 s du poste.

**Correction proposée.** Aucune.

### 5. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 108 ; conduite l. 63

**Constat.** Au commit 9b31c38d, les compagnons lancer-conduite-v15.py.sha256 et manifeste-local-v7.json.sha256 n'existent pas. Le poste (sha256sum -c) et la conduite (scellement.verifier(MANIFESTE)) refusent donc de partir tant qu'ils ne sont pas sur la branche clonée. Vérifié : avec le vrai manifeste, gardes_d_entree tombe aujourd'hui sur « empreinte compagnon … absente » ; avec une copie scellée, elle passe. Le poste ne vérifie pas sa propre empreinte : seul l'affichage du constructeur (« script sans secrets <sha> ») la porte.

**Correction proposée.** Sceller les quatre pièces (et le constructeur), committer, pousser sur claude/compassionate-meitner-d4ryyk avant de construire les données de démarrage. Puis vérifier que l'empreinte affichée par construire-donnees-demarrage-v13.py est égale à celle de poste-hetzner-v13.sh.sha256 avant la création Hetzner.

### 6. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 37-47, 131, 141 ; constructeur l. 4

**Constat.** Commentaires périmés, hérités et intacts au-dessus de « set -uo pipefail » :
- les lignes 37 à 47 décrivent la v1 (« conduite v5 », « lancer-conduite-v13.py sous GO_ID=GO-2026-11-10-10 », « 200 Go ») ;
- la ligne 131 dit « 200 Go » ;
- la clé « cout_avec_200_go » de offre-choisie-v13.json porte un coût calculé sur 110 Go ;
- la docstring du constructeur dit « Lit poste-hetzner-v1.sh ».
Aucun effet sur l'exécution.

**Correction proposée.** Aucune pour ce run (en changer serait une différence non nommée). Lire « cout_avec_200_go » comme le coût carte et 110 Go du § 2.4 dans l'ordre de lancement et dans le rapport.

### 7. remarque — runs/temoin-bailey-v1-20261111/construire-donnees-demarrage-v13.py 49-50

**Constat.** Le constructeur écrit toujours « creation-hetzner-v1.json » (O_TRUNC) dans le dossier passé en argument : il écrase une construction antérieure si le même dossier est réutilisé (R12). Le fichier contient les secrets, hors du dépôt, en droits 600 (dossier 700, vérifié). Essais avec de faux secrets : refus sans clés, sur un caractère interdit et sur « @@ » dans une valeur ; les trois blocs sont remplacés une fois ; user_data de 12 469 octets (< 32 Kio), bash -n sans erreur ; aucun secret affiché. Défaut hérité.

**Correction proposée.** Passer un dossier neuf hors du dépôt (par exemple ~/hetzner-bailey-v13/) et l'effacer après la création.

### 8. remarque — runs/temoin-bailey-v1-20261111/poste-hetzner-v13.sh 118-129

**Constat.** Le relevé du crédit du § 2.5 (has_billing, autobill_threshold, autobill_amount, billing_failed, credit ≥ seuil) n'est pas dans le poste, et ce n'est pas à lui de le faire : le § 6 ne le permet pas, et le § 2.5 le place au lancement du poste, consigné dans l'ordre de lancement, sans reprise pendant l'attente. L'inventaire R10 (étiquette « temoin-bailey-c6- », égale à PREFIXE_ETIQUETTE de lanceur_v21) vient avant toute création. Aucun arrêt par motif, aucun kill (seulement kill -0 sur le PID). Secrets jamais affichés (aucun set -x, journal resté dans /root, non poussé). Toute sortie par exit 3 après le clonage pousse son état.

**Correction proposée.** Aucune : la session fait et consigne le relevé du § 2.5 avant de créer la machine Hetzner.
