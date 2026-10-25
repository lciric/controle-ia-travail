# Contre-lecture 4 — traitement des constats PG3-01 à PG3-16 dans `pilote-gemini-organisme-v4-question-v2.md` et dans `lancer_pilote_gemini_v4_question_v2.sh`

- **Contre-lecteur** : sous-agent neuf, modèle Claude Opus 5.5 (`claude-opus-5-5`). Je n'ai écrit aucune pièce. J'ai lu seulement `pieces/` et `EMPREINTES-pieces.txt`. Je n'ai utilisé ni git, ni le réseau, ni d'autre agent, et je n'ai exécuté aucun script des pièces. Commandes lancées : `date -u`, `ls`, `sha256sum`, `grep`, `diff`, `wc`, `od`, `sed`, `tr` (lecture seule).
- **Début (UTC)** : 2026-10-25 00:10:57. **Fin (UTC)** : 2026-10-25 00:29:37 (heure lue juste avant l'écriture de ce rapport).
- **Empreinte SHA-256 du texte vérifié** (je l'ai calculée moi-même) : `4b89795cd571c5246a2a0de7c2aaace3a3431784d3ffe6a7f48859efa1a800e5`, égale à l'attendue. Script : `d0293ad4dd14dc3400ebd2c2ceab07375a3fbf9c4b683fd36d8bba94e0153794`, égale à l'attendue et à celle qu'inscrit le texte (l. 24). Les 21 pièces, ces deux-là comprises, sont égales à `EMPREINTES-pieces.txt`. Les empreintes que le texte cite pour la v1 (`6ef15677…`), le rapport 3 (`928463e0…`) et les quatre pièces de simulation (`0bf93757…`, `39241a6a…`, `7aa87221…`, `9a2186ec…`) sont égales aux pièces jointes.
- **Verdict** : **scellable après corrections** (il faut une nouvelle version du script et du texte, R12). PG3-01, le constat majeur, est traité : aucune valeur de score n'est lisible ni poussée en clair avant le moment du plan § 3. Ce qui empêche de sceller tel quel :
  - après un refus du noyau au code 7, le script crée lui-même l'obstacle qui interdit la tentative suivante que le texte permet (PG4-01) ;
  - des variables prévues pour la simulation restent actives en mode réel et contournent la garde « une seule course » et la source des registres (PG4-02) ;
  - un canal latéral : l'extrait laisse calculer une fonction du score `test` de g0 (PG4-03) ;
  - des gardes nouvelles du script n'ont pas d'essai d'artefact (PG4-04).
- **Décompte** : 16 constats et l'observation. **15 traités, 1 en partie (PG3-07), 0 non traité** ; l'observation est traitée. Constats nouveaux : **8**, soit 4 mineurs (PG4-01 à PG4-04) et 4 de forme (PG4-05 à PG4-08). Aucun n'est bloquant ni majeur.
- **Validateur** (`validateur-prereg.py`, fonction `problemes`) :
  - **Sur le texte tel quel**, il rend deux messages, dans cet ordre :
    1. « contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport) ». L'entrée de la l. 396 est reconnue par `ENTREE` (l. 29) ; son morceau, qui va jusqu'à la fin du texte, ne contient aucune empreinte de 64 caractères (l. 50-56).
    2. « marqueurs de gabarit restants : <<CL4_EMPREINTE_BROUILLON>>, <<CL4_EMPREINTE_RAPPORT>>, <<CL4_VERDICT>>, <<EMPREINTES_PIECES>>, <<ENTROPIE>>, <<GRAINE>> » (l. 27, 57-59). Il y a 7 occurrences : l. 202, 212, 213, 398, 399, 400, 402.
  - Ce qui est conforme : les huit sections exigées sont présentes en `## ` et non vides, avec des apostrophes droites (vérifiées octet par octet) ; il n'y a aucun « À REMPLIR » ; les entrées 1, 2 et 3 ont chacune deux empreintes distinctes ; la ligne « contre-lecture 4 » de la l. 402, en minuscule, n'est pas reconnue comme une entrée.
  - **Une fois les 7 occurrences remplies** (empreintes en 64 caractères hexadécimaux minuscules ; graine et entropie en entiers ; verdict en texte) : **liste vide**. Le morceau de l'entrée 4 contiendra alors trois empreintes (brouillon, rapport, fichier d'empreintes).
  - Ce que le validateur ne voit pas : la justesse des valeurs (E de 128 bits, graine dérivée de E, brouillon égal à `4b89795c…`, fichier d'empreintes présent avec son compagnon), le verdict, et « et eux seuls ».

## Traitement des constats de la contre-lecture 3

| constat | traitement | ce qui le montre |
|---|---|---|
| PG3-01 (majeur) sortie du lanceur avec les scores, poussée en clair | **traité** | Sorties séparées dans le texte (l. 206, 216-223) et dans le script (l. 176-177, 184-191). `cli.lancer` n'imprime de score qu'en l. 280, sur la sortie standard (`noyau-cli.py`). Dans les modules du noyau joints, la sortie d'erreur ne reçoit que des refus (`noyau-cli.py` l. 115-386), et la sortie de l'organisme va dans `erreurs.txt` et `sortie.txt` de son dossier (`noyau-bac_a_sable.py` l. 174, 246-247). Archive fermée, puis copies retirées (script l. 227-243 ; simulation : 1 429 entrées = 1 429, copies retirées, `simulation-LANCEMENT` l. 19). `course/` et `ferme/` sont exclus de la liste à pousser (script l. 246 ; `simulation-A-POUSSER` l. 1-35). Restes : canal latéral (PG4-03) et liste construite par exclusion (PG4-07). Collisionneur non vérifiable ici. |
| PG3-02 `<espace>`, copies du conteneur, journal (c) | **traité** | Interdits nommés (l. 249-252). Lecture du journal par son chemin exact seulement (l. 223-228). Journaux recopiés (l. 234-236 ; script l. 209-216). `<espace>` archivé puis retiré (l. 252-255 ; script l. 230-231, 238 ; espace de la simulation en `/var/tmp/essaim-m3/506417cda04c9838`, extrait l. 772). Reste de forme : PG4-08 (ii). |
| PG3-03 exposition de la réponse | **traité** | l. 237-246. C'est exact au regard du code : `historique` n'est passé qu'à `planifier_castes_question_ouverte` (`gemini-v4-principal.py` l. 321-323), dont la pression ne varie qu'avec au moins deux entrées, donc reste constante à g1 (`gemini-v4-mitose_spectrale.py` l. 108-114) ; les consignes et le fichier écrit n'en contiennent rien (`gemini-v4-principal.py` l. 356-368, 424-434, 490-598) ; jusqu'à 4 exemplaires de 220 caractères au plus (`gemini-v4-memoire_isvd.py` l. 179-180) ; traces `verite=` d'entraînement (`gemini-v4-principal.py` l. 842-845). La simulation montre un exemplaire de test avec son étiquette (`simulation-reponse-question` l. 117). |
| PG3-04 1 800 s ; « attendu 5 » | **traité** | « pour réduire le risque », coupure et troncature dites d'avance, texte d'abstention ou texte minimal (l. 103-109 ; code l. 551-569, 914-921) ; « 5 castes planifiées », contributions possiblement moins nombreuses (l. 95-97) ; critère 2 (v) (l. 292-293). |
| PG3-05 cas de la question ; moment de l'audit | **traité** | Critère 2 (i) et (iv) (l. 287-293) ; la raison d'arrêt est lisible dans l'extrait (événement `arret`, `rapport.lignees.*.fin` : `outils-extrait_mecanique.py` l. 54, 204, 211). Critère 1 : audit sur fichiers fermés après le moment, sinon matériau (a)–(d) (l. 284-286). |
| PG3-06 lectures interdites et réponse | **traité** | l. 296-304 : prose seulement, citation non visée ; nombres de la réponse rapportés comme « dires non vérifiés » ; mise en rapport avec les scores interdite. |
| PG3-07 refus avant tout appel | **en partie** | Règle écrite (l. 179-182, 310, 316 ; script l. 47-54, 225). Mais un refus du noyau au code 7 laisse `course/`, que le script archive en `ferme.tar.gz`, et la tentative suivante est alors refusée (PG4-01). L'essai A12 ne couvre qu'un refus du script lui-même (`simulation-essais` l. 12-13). |
| PG3-08 simulation citée d'une pièce contraire | **traité** | l. 45-54 : la question servie est `d967b212…` (extrait l. 807) ; tête `5aca4aaf…` et code identique à `cec6dce` (`simulation-LANCEMENT` l. 4, 6) ; deux générations `OK` (extrait l. 65, 128) ; 5 castes (`simulation-reponse-question` l. 102-107) ; textes dits factices. |
| PG3-09 banque, mission, arbre de travail | **traité** | l. 69-72, 79-84, 185-186, 311 ; script l. 75-85 (`git diff` sur le commit et sur l'arbre de travail, `git status --porcelain --untracked-files=all`, `sha256sum`) ; artefacts A5 et A6 refusés. |
| PG3-10 essais sautés | **traité** | l. 192-196, 315 ; script l. 134-163. Essais en root, sauts limités à l'essai réseau, total de 114, 19 essais cités exigés (même liste dans le texte, l. 331-341, et dans le script, l. 43) ; artefact A9. |
| PG3-11 « listes closes » | **traité** | l. 230-232 ; conforme à `outils-extrait_mecanique.py` l. 34-55, 181, 204. |
| PG3-12 corps de la question | **traité** | l. 57-59 ; le texte servi en simulation dit « Pour chacun des points suivants, une réponse argumentée est attendue » (`simulation-reponse-question` l. 15). |
| PG3-13 `EXCEPTION` | **traité** | l. 138. |
| PG3-14 verdict sans marqueur ; marqueurs comme noms | **traité** | Contre-lecture 3 inscrite en entier (l. 390-395). `<<CL4_VERDICT>>` et « la correction fait une nouvelle version » (l. 400). Champs nommés sans chevrons (l. 401-402). |
| PG3-15 portée des essais | **traité** | l. 316, 317, 323, 207-208 (essai en ligne de commande : `tests-test_noyau.py` l. 2574-2577). Vérification après départ par `isolation` et `collisionneur_conforme` (script l. 205-207 ; `simulation-LANCEMENT` l. 15). Reste de forme : PG4-08 (iv). |
| PG3-16 précisions | **traité** | Commits et arbre en entier (l. 38-43) ; convention du collisionneur (l. 125) ; répertoire de `find` (l. 196) ; `commit` égal à la tête (l. 84-85) ; « deux écritures et une vérification » (l. 128) ; compagnon de `LANCEMENT.md` (script l. 58, 247) ; archive tar et identité du code de g1 vérifiée après le moment (l. 142-145) ; `n_reponses_test` (l. 146-147). Reste de forme : « aucune autre course » sans vérification consignée (PG4-08 (v)). |
| observation (`statut_execution.json`, `erreurs.txt`) | **traité** | Ligne de la liste d'arrêt l. 325 et table l. 367 ; la transmission à session-depot n'est pas vérifiable ici. |

**Réponse à la question 2 (chemins vers un score avant le § 3).**

- **Fichiers poussés** (simulation : `simulation-A-POUSSER` l. 1-35 ; en réel s'y ajoute `appel-controle-*`) :
  - `LANCEMENT.md` : notes mécaniques seulement (script l. 61-244).
  - `essais-v1.xml` et `essais-v1.txt` : produits avant la course, sur des données de test, sans rien de la course.
  - `sortie-erreur-lanceur.txt` : dans le code joint, refus et traces Python seulement ; les messages d'exception du noyau joint portent des coûts ou des chemins, jamais un score.
  - Journaux recopiés : statut, espèce, rôle, usage, coût, empreintes du prompt et du texte, nombre de caractères ; ni texte ni étiquette (`noyau-appels.py` l. 187-195).
  - Extrait : aucune valeur de score, mais un canal latéral (PG4-03).
  - Réponse : l'exposition déclarée, c'est-à-dire au plus 4 débuts de raisonnement de g0, étiquette comprise, que personne ne doit confronter à la banque.
  - Entrées : question, registre, organisme d'origine (16 fichiers, sans mémoire).
- **Archive fermée** : `ferme.tar.gz` contient `course/`, `ferme/` et `<espace>` ; c'est le gzip poussé tel quel, fermé par la règle et par sa forme binaire, non chiffré, comme la contre-lecture 3 le demandait.
- **Fichiers retirés** : `course/`, `ferme/` et `<espace>` après vérification du compte des entrées.
- **En cas d'échec** : il n'y a pas de fuite ; les copies restent ouvertes dans l'arbre de travail du dépôt (PG4-07).

## Constats nouveaux

### PG4-01 — mineur — un refus du noyau au code 7 produit `ferme.tar.gz`, et la tentative suivante est alors refusée comme « course déjà partie »
- **Où** : plan § 1, l. 179-182 ; liste d'arrêt, l. 310 et l. 316 (« avant le manifeste : tentative suivante permise ») ; script l. 48-53, 200-243.
- **Ce qui est** :
  - `Noyau.__init__` crée `course/` (`noyau-boucle.py` l. 160), puis `lignees/` et `confrontation/` (l. 165-167), `<espace>/travail` (l. 170-172) et `archive/` (l. 243, `noyau-archive.py` l. 65-68), **avant** les gardes du mode réel (collisionneur, registre, root, isolation réseau, `unshare -n` : l. 277-294) et avant le manifeste (l. 295-298). Le refus sort au code 7 (`noyau-cli.py` l. 264-275).
  - Le script consigne alors « aucune course écrite … une tentative suivante est permise » (l. 225). Mais `course/` existe, donc il archive `course/` et `ferme/` en `ferme.tar.gz` (l. 227-243).
  - Avec `TENTATIVE=2`, la boucle de la l. 50 trouve ce `ferme.tar.gz` et refuse : « une course est déjà partie … (R3) ». Ce message est faux.
  - Le cas le plus probable de refus avant le manifeste (empreinte du collisionneur, isolation réseau) clôt donc le pilote. Pour reprendre, il faudrait supprimer une pièce (R12) ou utiliser un autre script, ce qui fait une nouvelle version de ce texte.
  - L'essai A12 ne couvre qu'un refus du script (reste < 40 USD, l. 12-13 du journal). Le même chemin vaut pour une exception non rattrapée dans `Noyau.__init__` (code 1).
- **Correction** : n'archiver en `ferme.tar.gz` que si `course/manifeste-run.json` existe. Sans manifeste, vérifier que `course/` ne contient aucun fichier ordinaire et que la sortie standard est vide, puis les laisser en place (ils ne déclenchent plus la garde de la l. 50) ou les archiver sous un autre nom (`refus-avant-manifeste-v1.tar.gz`). Ajouter un essai d'artefact : un refus du noyau après la création de `course/`, par exemple une famille inconnue dans `--organisme-impose`, qui lève à `noyau-boucle.py` l. 238-239, suivi d'une tentative 2 acceptée.

### PG4-02 — mineur — des variables de simulation restent actives en mode réel et contournent la garde « une seule course » et `origin/main`
- **Où** : script l. 27 (`PILOTE_RACINE`), l. 30 (`SUFFIXE_ESSAI`), l. 112-113 (`REGISTRE_GO_SOURCE`), l. 118 (`DEPENSES_SOURCE`). Seul `ESSAI_ARTEFACT` est réservé à la simulation. L'usage réel (l. 12) ne les nomme pas.
- **Ce qui est** :
  - Ces variables sont lues en mode réel. Avec `PILOTE_RACINE`, le dossier du pilote sort de `essaim-m3-refonte-v1/pilotes/`, contrairement à la l. 183, et la recherche d'une course antérieure (l. 48-53) porte sur un autre dossier.
  - Avec `SUFFIXE_ESSAI`, un dossier `…-v1<suffixe>` échappe au motif `$NOM-tentative*`. Une course partie sous ce dossier ne bloque donc pas une course sans suffixe, et inversement. C'est un contournement de R3 par une seule variable.
  - Avec `REGISTRE_GO_SOURCE` et `DEPENSES_SOURCE`, les registres viennent d'un fichier quelconque au lieu d'`origin/main` (l. 190-191, 314). Ni le chemin de `$PILOTE` ni la source des registres ne sont consignés dans `LANCEMENT.md` (l. 61-67, 122).
  - Les essais de simulation ont justement été lancés avec `PILOTE_RACINE` (`simulation-extrait` l. 2). Une variable héritée de cette session passerait sans rien dire (R5).
- **Correction** : en mode réel, refuser avant `mkdir` si l'une de `PILOTE_RACINE`, `SUFFIXE_ESSAI`, `REGISTRE_GO_SOURCE`, `DEPENSES_SOURCE`, `ESSAI_ARTEFACT` est définie. Consigner `$PILOTE` et la source des registres. Ajouter un essai d'artefact.

### PG4-03 — mineur — canal latéral : la taille de `contexte.json` de g001, dans l'extrait, dépend de l'écriture du score `test` de g0
- **Où** : plan § 3 (a), l. 229-232 (« sans score ») ; `outils-extrait_mecanique.py` l. 158-169, 202.
- **Ce qui est** :
  - L'extrait liste, pour chaque génération, les fichiers du dossier de travail archivé avec leur taille. `contexte.json` y figure : il est copié par `deposer` (`noyau-archive.py` l. 101-102) et la simulation donne 83 982 octets à g000 et 87 086 à g001 (`simulation-extrait` l. 201-202, 511-512).
  - À g1, ce fichier contient `historique`, avec `"score"` de g0 (`noyau-boucle.py` l. 565 ; `noyau-archive.py` l. 210-216), écrit par `json.dumps(…, indent=1)` (`noyau-bac_a_sable.py` l. 199-200).
  - Tout le reste de son contenu se déduit de ce qui est lisible : la banque, les graines (événements de l'extrait), la question, le coût, les appels, les statuts, les chemins, par les fonctions déterministes du noyau (`taches.masquer` et `contrat.mission_texte`, non jointes ; l'ordre des tâches ne change pas la longueur totale). La taille donne donc exactement le nombre de caractères de l'écriture du score `test` de g0, par exemple 3 pour `0.5` et 18 pour `0.6083333333333333`.
  - C'est quelques bits sur un score, lisibles dès la fin dans une pièce poussée. Aucune valeur n'est lisible directement. Aucun autre fichier listé ne dépend d'un score du juge : la mémoire, l'état et le journal de l'organisme n'en reçoivent pas (`gemini-v4-principal.py` l. 924-984).
- **Correction** : au choix de l'auteur.
  - Ou bien déclarer l'exposition au § 3 : « la taille de `contexte.json` de g001 (`fichiers_travail`) dépend de la longueur d'écriture du score `test` de g0 ; personne ne la calcule ni ne la met en rapport avec rien avant le moment du point 3 ». Cela ne demande aucun changement de code.
  - Ou bien une nouvelle version de l'outil qui omet `octets` pour `contexte.json`. Cela fait un nouveau commit et une nouvelle version de ce texte.

### PG4-04 — mineur — gardes nouvelles du script sans essai d'artefact (R5) ; un cas annoncé absent du journal
- **Où** : l. 341-345 ; `simulation-essais-lanceur-v2-v1.log` l. 1-17.
- **Ce qui est** :
  - Le journal montre A1 à A13. Aucun artefact n'y figure pour les gardes suivantes : préenregistrement (empreinte, compagnon, graine, marqueurs : script l. 91-94) ; différences de code (tête, arbre de travail, fichiers non suivis, ancêtre, commit absent : l. 71-81) ; nombre de fichiers de l'organisme (l. 103) ; ligne du GO sans « calcul » (l. 116) ; appel de contrôle absent (l. 128) ; root et clés (l. 134, 180-181) ; échec, saut non permis ou total différent de 114 (l. 156-159) ; archive incomplète et espace hors de `/var/tmp` (l. 231, 241) ; tentative après un refus du noyau (PG4-01).
  - « désélection de l'essai réseau acceptée » (l. 344) n'apparaît pas dans le journal joint. Le cas sain a tourné sans argument (`simulation-LANCEMENT` l. 9).
- **Correction** : ajouter ces artefacts à l'essai du script (certains sont possibles en simulation par `ESSAI_ARTEFACT`), ou nommer au texte les gardes du script restées sans essai, comme pour les trois gardes du noyau (l. 316). Joindre le cas de désélection ou retirer la phrase.

### PG4-05 — forme — le script vérifie moins que ce que le texte ou ses propres notes disent
- (i) L'appel de contrôle : le script vérifie seulement que le fichier n'est pas vide (l. 128), puis écrit « (statut OK vérifié par le lanceur) » (l. 130). Or l. 24-25 du texte : « refuse … à chaque écart ». Écrire plutôt « statut vérifié par l'outil de session-depot, non par ce script ».
- (ii) La ligne du GO : `grep '^| GO-2026-10-24-07 |'` peut rendre plusieurs lignes (l. 114). « calcul » et le nom du pilote peuvent alors venir de deux lignes différentes (l. 116-117), alors que le texte veut « une ligne … de type calcul, nommant … » (l. 129-130). Exiger les deux sur la même ligne.
- (iii) La clé Gemini : à défaut de `GEMINI_API_KEY_2`, le script accepte `GEMINI_API_KEY` et note « n° 1 » (l. 181-182). Or le texte dit « la clé Gemini n° 2 exportée sous le nom `GEMINI_API_KEY` » (l. 99-100), et la note peut être fausse si session-depot a déjà exporté la n° 2 sous ce nom. Consigner le nom de la variable source, pas un numéro.
- (iv) Un journal d'appels absent, ou présent sous forme de lien, n'est pas noté (l. 211-215 ; R5).
- (v) La ligne de `depenses.md` exigée (nommant le pilote et le GO, l. 119) n'est pas décrite au texte (l. 130-131).

### PG4-06 — forme — compagnons des copies et liste à pousser (R6)
- Les copies reçoivent `journal-appels-gNNN.jsonl.sha256-archive` et `reponse-question-g001.md.sha256-archive` (script l. 213, 219). Ce sont les compagnons de l'archive, qui nomment le fichier d'origine (`noyau-archive.py` l. 32) : `sha256sum -c` ne s'applique pas à la copie. Le texte dit « avec son compagnon » et « avec leurs compagnons » (l. 234-236, 258). Écrire un vrai `.sha256` pour chaque copie (en gardant `-archive` si l'auteur le veut) et le dire.
- `A-POUSSER-v1.txt` est exclu de `EMPREINTES-pilote-v1.txt` et n'a pas de compagnon (l. 248). Il faut l'y inclure.

### PG4-07 — forme — la liste « poussé en clair » se fait par exclusion ; `course/` reste dans l'arbre de travail du dépôt
- Le texte donne une liste close de noms (l. 256-261). Le script, lui, liste tout fichier de `$PILOTE` hors de `course/` et `ferme/` (l. 246). Les deux coïncident au cas nominal (`simulation-A-POUSSER`), mais un fichier imprévu dans `$PILOTE` serait poussé sans qu'on le remarque. Construire la liste à partir des noms du texte et consigner, ou refuser, tout autre fichier.
- `course/`, avec `banque.json`, `juge/` et le reste, se trouve dans l'arbre de travail du dépôt pendant toute la course. Il y reste si l'archive est incomplète, ou si le script s'arrête sur son piège d'erreur (l. 60) après la course. Aucun `.gitignore` ne l'écarte : un `git add -A` de passation l'ajouterait. Écrire `$PILOTE/.gitignore` (`course/`, `ferme/`) avant la course.

### PG4-08 — forme — énoncés du texte
- (i) « Dès la fin, sont lisibles et seulement eux : (a)–(d) » (l. 228-237) omet les entrées poussées en clair : `question.md`, `registre-go.md`, l'appel de contrôle, `outils/…/organisme/` et les fichiers d'empreintes. Les ajouter en (e).
- (ii) La liste « personne ne lit » (l. 249-252) omet `course/lignees/` et `archive/*/g001/organisme.tar.gz`. Ces deux emplacements portent `etat_generation_precedente.json` de g0, c'est-à-dire son `journal_generation.json` avec `details_votes_test`, l'étiquette de chaque tâche de test (`gemini-v4-principal.py` l. 628-631, 975). Ils restent couverts par la liste close et par la fermeture mécanique ; il suffit d'ajouter « notamment » ou de les nommer.
- (iii) « codes 2 à 6 … code 7 » (l. 180) omet le code 1 (`SystemExit` de `_organismes_imposes`, exception non rattrapée : `noyau-cli.py` l. 65-80). « le noyau n'y écrit que ses refus (`refus : …`) » (l. 220-221) omet aussi « mode réel non demandé » et « espèce inconnue » (l. 217, 386). Écrire plutôt « tout refus avant le manifeste ».
- (iv) l. 316 : « clés absentes … vérifiés après départ par `manifeste.isolation` et `manifeste.collisionneur_conforme` ». Ces champs ne disent rien des clés, que vérifient le script (l. 180-181) et `cli.lancer` (code 4).
- (v) « aucune autre course ne tourne … ; s'il en tourne une, le pilote attend » (l. 110-111) : aucune vérification n'est consignée dans `LANCEMENT.md`.

## Non vérifiable ici

- Collisionneur (`collisionneur_v2.py`, non joint) : ce qu'il écrit sur les sorties standard et d'erreur, y compris par `logging` et `warnings`. L'affirmation de la l. 222-223 (« les `print` du collisionneur … sont sur la sortie standard ») en dépend, et avec elle le contenu de `sortie-erreur-lanceur.txt`.
- Modules du noyau non joints (`serveur.py`, `contrat.py`, `taches.py`, `fichiers.py`, `__main__.py`, `banque.py`, …) : leurs écritures sur la sortie d'erreur ; donc « vérifié par recherche dans `essaim_m3/noyau/` » n'est vérifiable que pour les six modules joints. Également le format de `score["score"]`, qui fixe l'ampleur de PG4-03.
- `tests-test_outils.py` (16 essais, dont `test_extrait_mecanique_sain_puis_artefacts`) n'est pas joint à cette lecture ; la configuration de `pytest` du dépôt (`junit_logging`) n'est pas jointe non plus : par défaut, `essais-v1.xml` ne porte aucune sortie capturée.
- Le contenu du résultat de l'appel de contrôle (outil de session-depot), qui est poussé en clair.
- Git (commits cités, `origin/main`, branches), registres (`go.md`, `depenses.md`, reste de la ligne), et la transmission de l'observation à session-depot.
- Le cas de désélection de l'essai réseau annoncé à la l. 344 (PG4-04).
