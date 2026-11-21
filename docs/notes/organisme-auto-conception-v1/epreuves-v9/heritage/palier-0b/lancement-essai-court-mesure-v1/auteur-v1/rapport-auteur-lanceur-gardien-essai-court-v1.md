# Rapport de l'auteur du lanceur et du gardien — palier 0b, essai court de mesure — v1

Mandat : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/mandat-auteur-lanceur-et-gardien-essai-court-palier-0b-v1.md` (sha256 32580fd6…8d84, vérifiée). Complément 1 v3 extrait de `origin/main` par `git show` redirigé : `complement-1-v3.md`, sha256 1484cd75…7268 (vérifiée). Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-lanceur-gardien-palier-0b/` (noté D ci-dessous). Rien lancé du vrai programme, rien écrit sous `/home/user/palier-0b-racine/`, aucun commit, aucune dépense, aucun refus de permission rencontré.

## Fichiers et empreintes (sha256)

À employer (D/) :
- `lancer-essai-court-v1.sh` — 5c6cc113a65fd87155d79bffd5227fe37deb652892f93ccc575c07665b40073d
- `demarrer-essai-court-v1.sh` — b9d3730676eb3cf9074165a32066c95c38557875dbd1cd87429ff2e684632a43
- `gardien-essai-court-v1.py` — aad04e635adc1008dcf1e3e45d98f654b5539f99c8adba3351cb0b872b6dcefd
- `demarrer-gardien-essai-court-v1.sh` — aef4ae3b48b9ae784e0a413db4b94f65bc497290f46696c602551b250547f7bf
- `verifier-commande-v1.py` (contrôle à l'octet de la commande) — 594e8f8cc7db26a6053f272ba96048fd04497cc248b5804ccf81ae89c2d04729

Essais (D/essais/) : `programme-factice-v1.py` 259cef4c…ad8c ; `fabriquer-lanceur-factice-v1.py` 2a9fed06…ba6a ; `preparer-racine-factice-v1.sh` a57bf287…809b ; `essais-lanceur-refus-v1.sh` 296123dc…f912 ; `essai-projection-v1.py` 67544760…c91e ; `preparer-scenarios-v1.sh` 5fc5a59b…4dd1 ; `jouer-scenario-v1.sh` b14f69f7…f051. Traces : `essais/refus/*/`, `essais/scenarios/s1…s9/tenue/`. Notes au fil de l'eau : `notes-avancement-v1.md`.

Emploi prévu (dans cet ordre, les quatre fichiers copiés dans `/home/user/journaux-palier-0b-essai-court-v1/`) :
1. `bash …/demarrer-essai-court-v1.sh /home/user/journaux-palier-0b-essai-court-v1` (lance `lancer-essai-court-v1.sh` pris à côté du script) ;
2. `bash …/demarrer-gardien-essai-court-v1.sh /home/user/journaux-palier-0b-essai-court-v1` (valeurs d'emploi par défaut : sorties de l'essai court, 8 000 000 000 o, n = 13, 45 min, 60 s, 60 s, 648).

## Essais et résultats

Commande : `verifier-commande-v1.py complement-1-v3.md lancer-essai-court-v1.sh /home/user/palier-0b-racine/diag/heritage-palier-0b-v1/etapes-3-a-6-essai-court-mesure-v1` → une seule ligne `env -C` de chaque côté ; tout sauf le dernier argument : 619 octets, sha256 a0dc38a4…bd59 des deux côtés ; « ÉGAL à l'octet sauf le dernier argument ».

Refus de départ du vrai lanceur (`essais-lanceur-refus-v1.sh`, mode `--verifier-seulement` sur racine factice `essais/racine-factice`, tête 702a6edd…a28b, empreinte 259cef4c…ad8c ; la commande n'est jamais exécutée dans ce mode) — attendu = obtenu pour tous, 0 échec :
v0 cas sain → 0 ; v1 dossier des sorties existant → 10 ; v2 tête fausse → 11 ; v2b racine sans dépôt → 11 ; v3 fichier suivi modifié → 12 ; v3b fichier non suivi seul → 0 (voir écart 2) ; v4 empreinte fausse → 13 ; v4b programme absent → 13 ; v5 usage → 2 ; v6 `code-de-sortie.txt` déjà là → 4, non écrasé ; v7 tenue absente → 3 ; dossier des sorties neuf jamais créé. Départ refusé aussi par `demarrer-essai-court-v1.sh` sur fichiers déjà présents (code 4) et par `demarrer-gardien-essai-court-v1.sh` sans fichiers du départ (code 3).

Projection (`essai-projection-v1.py`, valeurs calculées à la main écrites en littéraux) : A (Δt 600 s, n 13, s4 1,2e8) → 32 400 s et 6 480 000 000 o ; B (n 2) → 58 320 s, 648 000 o ; C (n 7) → 291 600 s, 324 000 000 o ; D (n 1), E (n 0) → impossible. 0 échec.

Scénarios de bout en bout (vrai script de départ, vrai gardien, lanceur factice tiré du vrai par programme : 6 lignes changées — 5 constantes et la commande ; intervalle 1 s) :

| Arrêt | Cas | Réglage | Attendu | Obtenu |
|---|---|---|---|---|
| place | sain s1 | seuil 1 o | aucun arrêt | aucun `arret-gardien.txt`, code 0, inventaires 3 et 4 + compagnons, gardien fini sur « programme absent » |
| place | artefact s2 | seuil 1e18 o (au-dessus de la place réelle, ~42 Go) | arrêt du groupe | « arrêt de place », signal de fin au groupe 18540, absent en 1 s, code 143 |
| mesure (n) | sain s3 | seuil 13, programme fini à n = 12 | aucun arrêt | aucun, code 0 |
| mesure (n) | artefact s4 | seuil 13 | arrêt à n = 13, mesure | arrêt à n = 13 ; Δt 6,007583 s × 648/12 = 324,4 s ; s4 1 404 928 o alloués × 54 = 75 866 112 o ; apparents 1 373 728 × 54 = 74 181 312 o — refaits à la main, égaux (1 373 728 = 13 × 100 000 + 18 dossiers × 4096) |
| mesure (durée) | sain s5 | 30 s, étape 4 ≈ 10 s | aucun arrêt | aucun, code 0 |
| mesure (durée) | artefact s6 | 5 s | arrêt après 5 s | arrêt à 6,0 s, n = 6 ; 5,998525 × 129,6 = 777,4 s ; 69 632 × 129,6 = 9 024 307 o (à la main, égaux) |
| mesure n < 2 | artefact s8 | 3 s, n = 1 | « projection impossible » | « projection impossible (n = 1 < 2) », arrêt fait |
| arrêt forcé | artefact s7 | programme qui ignore le signal de fin ; délai d'emploi 60 s | arrêt forcé du groupe à 60 s | fin 16:25:38.763 ; forcé 16:26:38.764 ; chef et enfant (19457, 19478) absents ; pas de `code-de-sortie.txt` (lanceur tué) |
| identité | artefact s9 | groupe écrit faux (3999999) | aucun signal | « aucun signal envoyé : identité non confirmée (groupe lu 21641 différent du groupe écrit 3999999) » ; programme factice arrêté ensuite par moi par son groupe (21641) ; gardien fini |

Le cas sain de l'arrêt forcé est s2/s4/s6/s8 (le signal de fin suffit, aucun arrêt forcé envoyé). s5 et s7 ont tourné en même temps : s7 (seuil de place au-dessus de tout) n'a pas touché s5 (le gardien n'adresse que son groupe). Processus factices : tous absents à la fin (vérifiés par `stat -c %n /proc/PID`).

## Écarts et choix (à trancher par la session si besoin)

1. Le lanceur a un mode `--verifier-seulement RACINE TETE EMPREINTE PROGRAMME SORTIES` (paramètres factices exigés par le mandat) ; ce mode n'exécute jamais la commande. Le mode d'emploi n'a qu'un argument et prend les valeurs réelles écrites en constantes.
2. « Sans modification » est lu comme : aucun fichier SUIVI modifié (index et arbre), `git status --porcelain --untracked-files=no`. Les fichiers non suivis (par exemple les dossiers d'essais sous `diag/`) ne bloquent pas (v3b). Si la mère veut aussi les non suivis, retirer `--untracked-files=no`.
3. Le lanceur pose un piège sur le signal de fin pour écrire le code (143) après la mort du programme ; après un arrêt forcé, aucun code n'est écrit (s7). Il écrit aussi le code des refus (10 à 13) et refuse (4) si `code-de-sortie.txt` existe.
4. Fichiers ajoutés : `pgid` lu dans `/proc/PID/stat` après `setsid` ; `pid-gardien-essai-court.txt` et `sortie-gardien-essai-court.txt` (script de départ du gardien, non demandé en toutes lettres) ; ligne de journal enrichie de « étape en cours » et « arrêt du programme » (fichier `arret.txt`), tirés du complément.
5. Inventaire : le complément veut des empreintes, ce qui oblige à lire les octets ; ils sont hachés sans être interprétés. Le gardien ne décide sur aucun contenu. L'inventaire passe après les contrôles ; une étape 4 complète (plusieurs Go) bloquerait le gardien pendant le hachage — sans objet en essai court, où le manifeste de l'étape 4 n'existe pas. Pas d'archive (le mandat ne la demande pas).
6. Pendant l'attente après le signal de fin (au plus 60 s, plus 10 s après l'arrêt forcé), aucune ligne de minute n'est écrite.
7. 8 Go = 8 000 000 000 octets ; « libres » = `f_bavail × f_frsize` (place disponible hors réserve), sur le système de fichiers du dossier des sorties ou de son plus proche parent présent.
8. s4 rendu en octets alloués (`st_blocks × 512`, base de la place projetée) et en octets apparents ; les deux projections de place sont écrites.
9. La durée de l'étape 4 se compte depuis t3. L'arrêt de mesure suit la lettre (manifeste 3 présent et n ≥ seuil, ou durée), même si le manifeste 4 existait.
10. Identité avant tout signal : processus vivant (non zombie), même démarrage, même heure de départ qu'à la prise de garde, groupe lu = groupe écrit. Le gardien doit donc être lancé pendant que le programme vit (juste après le départ).
11. Le vrai lanceur n'a jamais exécuté sa commande ; son déroulé (contrôles, piège, code) est éprouvé par une copie qui diffère de 6 lignes. Les contrôles sur la vraie racine n'ont pas été joués (interdit d'y toucher). Je conseille à la session de lancer d'abord `lancer-essai-court-v1.sh <tenue-de-vérification> --verifier-seulement /home/user/palier-0b-racine d7f949ac…c3 1f04cb46…b14 <programme> <sorties>` (lecture git seule).

## Relevé de méthode

**Chaîne de raisonnement.**
1. La commande à porter est la ligne 37 du complément 1 v3 (`complement-1-v3.md`, 1484cd75…7268), dernier argument remplacé (mandat, 32580fd6…8d84, point 1).
2. La ligne du lanceur lui est égale à l'octet sauf le dernier argument : calcul rejouable `verifier-commande-v1.py` (619 octets, a0dc38a4…bd59 des deux côtés).
3. Les noms surveillés sont ceux du programme : `etape-N/manifeste.json` et `.sha256` (programme extrait au commit 8262c442, sha256 1f04cb46…db14 = empreinte attendue, lignes 139–142 ; `tirages.py` lignes 252–256, 380–382), `arret.txt` (ligne 148), `etape-4/couche-mecanique/bras-1-a-3/<proposeur>/<dose>/<source>` (programme ligne 199, `etapes.py` lignes 180–186, 223).
4. Les refus de départ rendent les codes prévus et ne créent rien : essais v0 à v7 (`essais/refus/`), pas 1.
5. Les deux arrêts se déclenchent quand le seuil est atteint et seulement alors : s1 à s8 (tableau), pas 3.
6. L'arrêt ne touche que le groupe écrit et seulement si l'identité tient : s9, et s5 intact pendant s7.
7. Les projections suivent la formule du complément : essai-projection (A à E) et deux mesures refaites à la main (s4, s6).
8. Le vrai programme mourra du signal de fin adressé au groupe, et ses descendants sont dans ce groupe : supposé, appuyé seulement sur l'absence de `subprocess`, `multiprocessing`, `setsid`, `signal` dans `etapes.py`, `organisme.py`, `mecanique.py`, `executeur.py` (extraits au commit 8262c442) ; autres modules non lus ; sinon, l'arrêt forcé à 60 s couvre le cas (s7).
9. La place de l'essai court reste sous le seuil de 8 Go assez longtemps pour mesurer n = 13 : supposé (dépend de la place libre réelle au départ, non mesurée par moi).

**Objets de contrôle.** Arrêt de place : faux par construction (seuil 1 o, s1) → attendu aucun arrêt, rendu aucun arrêt ; vrai par construction (seuil 1e18 o, s2) → attendu arrêt du groupe, rendu arrêt. Arrêt de mesure par n : faux (n max 12 < 13, s3) → rien ; vrai (s4) → arrêt à 13. Par durée : faux (s5) → rien ; vrai (s6) → arrêt. Arrêt forcé : faux (s2, programme qui meurt au signal de fin) → pas de forcé ; vrai (s7) → forcé à 60 s. Garde d'identité : vraie identité (s2 à s8) → signal ; fausse (s9) → aucun signal. Refus du lanceur : cas sain v0 → départ permis ; artefacts v1, v2, v3, v4 → refus. Projection : n ≥ 2 → valeurs égales au calcul à la main ; n < 2 → impossible. Aucun mécanisme n'a « réussi » là où la conclusion était fausse.

**Premier pas non justifié.** Pas 8 : la conduite du vrai programme au signal de fin (mort rapide, descendants dans le groupe) n'est pas éprouvée ; la justifierait la lecture des modules non lus ou un essai du vrai programme dans un dossier jetable, hors de mon mandat.

**Mode d'échec affecté.** Sans objet : je suis l'auteur, non un relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation.

**Trouvaille de côté.** (a) Le complément veut un gardien qui « n'arrête rien » ; le mandat (décision R-4605) en veut un qui arrête : le mandat prime (« à suivre sauf où ce mandat dit autre chose ») et le gardien le suit. (b) Le complément veut des archives d'étape ; le mandat ne les demande pas : non faites. (c) La place libre du système de fichiers du dossier de travail était d'environ 42 Go pendant les essais (journaux) — même système de fichiers que la racine réelle non vérifié.

**Évaluateur et conseil.** Juges : le relecteur S, puis les essais ci-dessus (factices, admis sur cas sain et artefact pour chaque arrêt). Le produit pourrait être bien jugé sans le mériter par : le programme factice, plus simple que le vrai (un seul processus, pas de grosse écriture de fichiers ; le hachage d'une étape 4 réelle et le comportement du vrai programme au signal ne sont pas éprouvés) ; le lanceur factice qui diffère du vrai de 6 lignes (l'égalité du reste est garantie par fabrication, pas relue ligne à ligne) ; des intervalles d'une seconde au lieu de 60 (le délai forcé de 60 s, lui, a été éprouvé à sa valeur d'emploi).
