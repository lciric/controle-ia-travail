# Contre-lecture du lanceur de la course « conception propre » de l'organisme d'idéation — v1

Contre-lecteur neuf, **modèle B** (autre que l'auteur du lanceur, qui est le modèle A), sous-agent de la session mère.
13 novembre 2026, de 23:37 à 23:52 UTC (heures relevées par `date -u`). **Aucun modèle appelé, aucune course lancée, aucune
dépense, aucune valeur de clé lue ni affichée (présence de noms seulement), rien commité, rien poussé ; arbre principal non
modifié hors ce rapport et son compagnon ; clone de l'orchestrateur lu, resté propre.** Aucun refus de permission.

## Verdict

**« Autorisable »**, sous les cinq conditions d'emploi C1 à C5 ci-dessous (sans C1 et C2, je dirais « après corrections »).
Aucune correction du code n'est exigée avant le lancement ; les corrections listées valent pour un v2 éventuel (R12).
**0 bloquant, 2 majeurs d'emploi, 8 mineurs.** Les huit points demandés : M1 corrigé ; M2 corrigé ; cause du 401 fermée ;
dépense impossible sans la ligne et bornée à 21 USD par la garde de cumul ; une seule relance au total ; relevé scellé dans
le dépôt ; aucune clé ni adresse d'hôte transmise ; aucun classement par le juge. **Réserve : l'arrêt par `kill -TERM`
n'est pas propre avec l'orchestrateur réel (A1)**, et la mémoire de la dépense ne vaut que poussée (A2).

## Ce que j'ai lu et vérifié

- Empreintes contre compagnons avant lecture : lanceur `709cf1c7…`, essais `772f882e…`, conception `be3ba97e…`, devis
  `ce679a53…`, rapport du préparateur `3b06afbb…`, outils et résultats du banc (tous « OK »), vérification du v3 `9c1caa7e…`.
- Lanceur lu en entier (1 248 lignes) ; ligne GO-2026-11-13-06 ; R-2549, R-2556, R-2558, R-2609, R-2611, R-2615.
- Orchestrateur (arbre `ee84d6ec…`, commit local `1168b02…`, propre, fichiers ignorés compris) : chemin réellement pris par
  la commande (`demonstrations/ideation_v8.py` → … → `ideation_v2.py`, `pole/ideation_v2.py`), contrôle, journal des coûts,
  juge différé, signaux, `pole/relais_reel.py`.
- Gardes de production jouées **en lecture seule** par `/usr/local/bin/python3 -I -B` (23:46 UTC), sans lancement :
  interpréteur OK ; ligne de GO trouvée, une seule, **GO-2026-11-13-06, 21 USD, Lazar, jusqu'au 30 novembre** ; orchestrateur
  à l'arbre épinglé ; cinq pièces à leur empreinte ; aucun run ; garde de cumul 0 + 14,9 + 4,0 ≤ 21 ; sommes 9,9 ≤ 10 et
  7,6 < 8, exposition externe 4,9 ; **bac à sable actif, `/proc` neuf** (`bwrap` et `socat` présents) ; environnement transmis
  dans cette session : `GO_ID`, `HOME`, `PATH`, `PYTHONPYCACHEPREFIX` seulement, 192 noms exclus.

## Constats

### Majeurs (d'emploi ; l'argent reste gardé)

**A1 — `kill -TERM <PID du superviseur>` n'arrête pas proprement l'orchestrateur réel.** Lanceur l. 39, 205-207, 746, 765,
1064. Le superviseur relaie bien le signal par PID (essai `test_arret_par_pid_relaye`), mais le chemin de l'orchestrateur
que prend cette commande n'a **aucun gestionnaire de SIGTERM** (il n'existe que dans `pole/noyau_v56.py`, non emprunté) :
l'orchestrateur meurt sur-le-champ, sans manifeste de fin ni tentative scellée, et ses `except BaseException` (qui tuent le
groupe de la commande d'Argon et comptent la session : `pole/adaptateurs.py` l. 743-748, `pole/ideation_v2.py` l. 2196,
2616) ne jouent pas. La commande d'Argon, lancée dans sa propre session de processus, **survit** (appel en cours payé
jusqu'à son plafond de session), et le lanceur ne la voit pas : il ne cherche d'orphelin qu'au PID de l'orchestrateur.
Épreuve E3 (superviseur du lanceur, enfant qui imite ces `except`) : SIGTERM → code scellé −15, rien d'écrit, petit-enfant
vivant ; **SIGINT → fin propre écrite, petit-enfant tué, code −2**. Conséquence d'un arrêt par TERM : plafond entier
compté (14,9), dépense illisible, génération verrouillée — sens fermé, mais la course est perdue.
*Correctif d'emploi* : C1. *Correctif de code (v2)* : le superviseur traduit TERM en INT pour l'orchestrateur, puis TERM
après un délai ; à la clôture, dire les survivants du groupe par PID.

**A2 — Le relevé et les manifestes ne protègent que commités et poussés.** `runs/course-ideation-conception-propre-v1/`
vit dans l'arbre de travail (non ignoré par git, non commité par le lanceur : M2 l'interdit après le détachement). Si le
conteneur est remplacé avant le commit (c'est arrivé le 13 novembre, B1 du v3), le lanceur ne voit **aucun run** et permet
une course neuve, puis une relance : la borne de 21 USD ne tient plus. *Correctif d'emploi* : C2.

### Mineurs

- **m1 — Code 5 puis perte du dossier hors dépôt : course tenue pour « rien lancé ».** L. 755 et 806 : sans manifeste de
  départ, si `<sorties>/<id>/superviseur-course` manque, le run compte 0 USD, aucune fiche, et **ne compte pas** parmi les
  deux courses. Épreuve E1 : course finie avec fiches (4,5 USD), manifeste de départ non écrit, dossier hors dépôt perdu →
  relevé 0, course neuve lancée. Double panne ; *correctif (v2)* : pré-départ présent et dossier `<sorties>/<id>` absent
  (il est créé avant le pré-départ) → « inconnu », plafond compté, nœud. *Emploi* : C3.
- **m2 — Clôture non reprenable.** L. 1089 et 1107 : une panne entre le relevé et le manifeste de fin (épreuve E2) sort par
  une trace Python, puis toute invocation refuse (« releve-depense.json existe déjà »). Sens fermé, nœud à la main.
  *Correctif (v2)* : relevé déjà présent, scellé et sans fin → le relire et écrire la fin.
- **m3 — Un essai scellé est périmé depuis l'inscription de la ligne.**
  `test_go_registre_reel_ne_contient_pas_encore_la_ligne` (essais l. 818) échoue maintenant : **130 passés, 1 échoué**, et
  non plus 131. Le fichier est dans `tests/` de l'arbre : la routine `python -m pytest -q` échoue d'un essai. Le banc du
  préparateur (`-x`) tuerait aujourd'hui tout mutant par cet essai : il n'est plus décisif tel quel. *Correctif* : essais v2
  avant S7 (l'essai affirme que le registre réel rend GO-2026-11-13-06 à 21 USD).
- **m4 — Trois gardes sans essai qui les isole** (mutants survivants, code juste à la lecture) : « sortie sans manifeste de
  fin → plafond » (l. 835) ; pièces hors liste blanche, enveloppe et commande d'Argon (l. 462-475 : l'essai ne touche que
  la question, que la liste blanche rattrape) ; bac « inactif » (l. 688 : rattrapé par « /proc neuf »).
- **m5 — Les plafonds des relais ne sont pas vus par le lanceur**, et l'orchestrateur vérifie seulement que le relais Claude
  suffit (plafond − réserve − dépense ≥ 8,5) et que ses modèles permis sont exactement les deux de la course, jamais qu'il
  est ≤ 10. Un relais absent ou mal réglé fait refuser l'orchestrateur après le détachement : **une des deux courses est
  consommée** sans dépense. *Emploi* : C4.
- **m6 — Les notes du juge sont copiées à côté des fiches** (l. 156-158 : `notes-par-juge.json`, `lecture-course.json`,
  `manifeste-fin.json`, clés d'anonymisation). Le lanceur ne classe rien, et l'orchestrateur non plus dans la course (juge
  externe différé : « aucun classement ni agrégat », `pole/ideation_v2.py` l. 2594-2597 ; `classements-par-juge.json` n'est
  pas écrit). La règle « ouvertes après le scellement du classement » (conception § 4.8) reste donc de procédure. *Emploi* : C5.
- **m7 — m2 du v3 inchangé** (dit par le préparateur) : orphelin non vu si le superviseur meurt entre le lancement de
  l'orchestrateur et l. 212 ; un signal reçu dans cette fenêtre tue le superviseur. Argent gardé.
- **m8 — M1 garde contre l'accident seulement** (l. 314 ; dit dans l'en-tête) : fichier et compagnon réécrits ensemble
  passent. *Emploi* : C3 (empreinte comparée à celle de la ligne de GO).

### Ce qui tient

- **M1** : options, commande d'origine exacte, argument, dossier courant, lien, place, empreinte — avant le verrou et toute
  écriture (l. 297-321, 1227-1245) ; mutants Y01 et X01 à X06 tués.
- **M2** : aucune commande git ni calcul après le détachement ; pré-départ scellé avant ; code 5 avec PID ; course
  retrouvée par le PID scellé du superviseur ; détachement incertain → jamais de manifeste de refus.
- **401** : environnement par liste de noms (l. 651-671) ; un nom en `CLAUDE`, `ANTHROPIC`, `CCR` ou de clé dans la liste
  fait refuser ; la variable d'hôte de R-2549 est présente dans cette session et **exclue** ; mutant Y08 tué. Limite
  inchangée (m6 du v3) : la preuve réelle est le premier contrôle ; Argon passe avant Claude, donc un nouveau défaut
  côté Claude coûterait le contrôle d'Argon (≤ 1,7 ; attendu ≈ 0,25) et la première des deux courses.
- **GO et plafonds** : une seule ligne par son contenu, type, Lazar, période, révocation, plafond ≥ 21 (mutants Y02 à Y05
  tués) ; cumul : relevé + 14,9 + 4,0 ≤ min(25, ligne) → relance seulement si la première tentative a coûté ≤ 2,1 ; totaux
  10 et 8 transmis, exposition externe 4,9 (contrôle 1,7 ; passes 1,3 et 1,9) ; **une tentative de contrôle par invocation**,
  aucun rejeu de session, juge externe jamais joué (lu dans l'orchestrateur) ; coûts de contrôle compris dans le journal lu.
- **Une relance** : deux courses au plus, seulement après fin propre, sans fiche, relevé lisible (Y21, Y22, Y27, Y28 tués).
- **Relevé** : scellé, lié au manifeste de fin par son empreinte, copies octet pour octet ; après clôture, le dépôt seul.
- **Clé** : le lanceur ne lit aucune clé ; `RR_ANTHROPIC_API_KEY_RIGAUD` et `ANTHROPIC_BASE_URL`, présents dans cette
  session (noms seulement), sont exclus de la course. `pole/relais_reel.py` lit la clé par `--variable-cle`, ne lit pas
  `ANTHROPIC_BASE_URL` (amont par `--amont`, défaut l'interface publique) et joint l'amont sans mandataire : lancé par
  `env -i`, il l'atteint (essai sans clé ni appel de modèle, 23:47 UTC). L'adresse du relais local est posée par
  l'orchestrateur lui-même pour ses sessions : c'est le dessin, pas une fuite de l'hôte.
- **Orphelin** : dit en clair, code 4, à la clôture et aux invocations suivantes (Y16, X24 tués).

## Conditions d'emploi

- **C1 (A1)** — Lancer au premier plan (ni `&` ni `nohup` : SIGINT hérité « ignoré » rendrait l'arrêt propre impossible).
  Arrêt : **`kill -INT <PID du superviseur>`** d'abord ; attendre la fin ; `kill -TERM` seulement s'il ne finit pas. Avant
  d'arrêter, relever par PID les descendants de l'orchestrateur ; après, vérifier par PID qu'aucun ne vit.
- **C2 (A2)** — Commiter et pousser le dossier de run **dès le lancement** (pré-départ, départ, liste blanche, mesure), puis
  **dès la clôture**, avant toute autre action ; dépense consignée dans `registres/depenses.md`.
- **C3 (m1, m8)** — Avant de lancer : `sha256sum -c` du compagnon du lanceur et comparaison à `709cf1c7…` de la ligne de
  GO ; commande exacte au registre (R-2611). Si le lancement rend le code 5 ou une trace : clôturer dans le même conteneur,
  sinon nœud, aucune relance.
- **C4 (m5)** — Relais lancés et vérifiés avant la commande : relais Claude `--plafond-usd 10`, modèles permis = les deux de
  la course exactement, clé par `--variable-cle RR_ANTHROPIC_API_KEY_RIGAUD` sous `env -i`, sans `ANTHROPIC_BASE_URL` ;
  relais Gemini v2 `--max-appels 8` ; ne pas les relancer entre la course et la relance.
- **C5 (m6)** — L'outil du lecteur et le programme de classement ne lisent que `copies/sortie--fiches-validees.json` ; les
  copies des notes du juge, de la lecture de la course et du manifeste de fin restent fermées jusqu'au classement scellé.

## Essais et mutations (arbre temporaire à moi, retiré)

- **Essais** rejoués deux fois (23:40 et 23:42 UTC) sur une copie : **130 passés, 1 échoué** (m3) ; les deux essais contre
  l'orchestrateur réel passent ; un second échec dans ma première copie venait de mon dossier (dépôt attendu par
  l'enveloppe), levé comme le fait le banc.
- **Mutations à la main : 28**, distinctes des 25 du préparateur, essai périmé écarté (23:43 à 23:49 UTC, base 130 passés) :
  **23 tuées, 5 survivantes**. Tuées : argument unique ; révocation, accordant, période, deux lignes de GO ; exposition de
  la course ; nom d'hôte transmis ; garde des drapeaux ; fiches illisibles ; superviseur tenu pour fini ; signal non
  relayé ; PID réutilisé ; session non neuve ; run sans manifeste ; orphelin à la clôture ; fichiers ignorés du clone ;
  identifiant de GO transmis ; garde de cumul ; relance sans code scellé ; total Claude transmis ; superviseur inconnu ;
  course partie comptée « rien » ; tentative non scellée. Survivantes : trois lacunes d'essai (m4) et deux équivalentes
  (relevé illisible non remonté au plafond : la relance est déjà refusée ; nom de clé du lecteur retiré d'une liste qui ne
  sert qu'à garder la liste des noms permis).
- **Épreuves à moi** (faux orchestrateur des essais) : E1 (m1), E2 (m2), E3 (A1, TERM contre INT).

## Non vérifié

La réaction de l'orchestrateur réel à SIGINT en course (lue dans le code, jouée sur un enfant qui l'imite seulement) ; le
sort des processus du kit d'agent à la mort de l'orchestrateur ; la borne en dollars d'un appel d'Argon au-delà de la garde
avant envoi (le relais Gemini v2 n'a qu'un nombre d'appels) ; l'état et les réglages des relais ; l'outil du lecteur.
