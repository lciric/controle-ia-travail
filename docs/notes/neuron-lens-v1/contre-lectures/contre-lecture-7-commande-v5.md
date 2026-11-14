# Contre-lecture 7 de la commande v5 sans ssh (amorce v2, suivi v1, dépôt réduit v6, essai à blanc v2) — rapport (texte rendu, recopié)

Contre-lecteur : sous-agent neuf, « modèle D », lancé par la session de reprise (autre compte) au commit `f922e81e` de
`prep/neuron-lens-v1`, rapport lu entre 13:48 et 13:53 UTC (`date -u` : 13:48:12 avant le lancement, 13:53:25 après la lecture) ;
lecture seule (`sha256sum -c`, `diff`, lecture ; essais du suivi exécutés). Le rapport est recopié tel qu'il a été rendu (mise en forme
seule) ; les suites données sont à la fin.

EMPREINTES (sha256sum -c, depuis chaque dossier) : OK pour les sept pièces (commande-volet-a-v5.md, amorce_neuron_lens_volet_a_v2.sh,
suivi_vast_v1.py, test_neuron_lens_suivi_vast_v1.py, depot_reduit_neuron_lens_volet_a_v6.py, essai_a_blanc_amorce_neuron_lens_v2.sh,
essai-a-blanc-amorce-v2.txt). Essais du suivi : 3 passés (vérifié, exécutés). `bash -n` non lancé sur l'amorce ; lecture seule, rien
exécuté d'autre. L'arbre git est propre (aucune modification non commitée).

## Verdicts
1. Commande v5 : scellable après corrections mineures (remarques 1, 2, 3).
2. Amorce v2 : scellable après corrections (remarques 4, 5, 6).
3. Suivi et son essai : scellable après corrections (remarques 7, 8, 9).
4. Dépôt réduit v6 : scellable après corrections mineures (remarque 10). Le diff v5→v6 se limite au nom de l'amorce (v1→v2) et aux
   en-têtes (vérifié par diff).
5. Essai à blanc v2 et son journal : scellable après corrections mineures (remarques 11 à 13).

## Suites de la contre-lecture 6 : état de chaque suite
- 1 (sorties brutes, filtrage, balayage) : faite pour l'essentiel (suivi_vast_v1, commande l.67-70, l.75). Réserves aux remarques 7 à 9.
- 2 (sérialisation `--args`) : la commande ne dépend plus des guillemets de l'outil ; elle documente `["-c","<texte>"]` et le texte est
  sans apostrophe interne (vérifié l.44). La lecture de la source de l'outil 1.11.0 n'est pas refaite par moi (supposé). Le comportement
  de `argparse.REMAINDER` avec un premier argument `-c` n'est pas prouvé par un essai ; je le range en « supposé ».
- 3 (CUDA) : filtre `cuda_max_good>=13.0` appliqué l.29 et l.6 (vérifié). Le fondement (dépendance `nvidia-nccl-cu13`) n'est pas
  vérifiable ici (supposé).
- 4 (première poussée fatale, cause affichée, branche des résultats absente) : faite (amorce l.102 code 14 ; l.65 cause ; commande
  l.36-37). Réserves aux remarques 4 à 6.
- 5 (poussée finale persistante) : faite (l.75, 10 essais de 60 s). Réserve à la remarque 4.
- 6 (jeton hors de pip et pytest ; tail) : faite (l.93-94, 108, 111, `env -u GH_TOKEN`). Non prouvée par l'essai, remarque 12.
- 10 (« exited », fichiers > 100 Mo) : « exited » écrit dans la commande (l.70) mais en conflit avec un cas non traité (remarque 4) ;
  fichiers > 95 Mo : signalés seulement (remarque 5).
- 11 (journal complet : balayage et artefacts) : fait (journal l.1-47, balayage l.47). Limites aux remarques 11 à 13.

## Remarques
1. Mineure. commande-volet-a-v5.md l.14 : « citant cette v4 et ses empreintes » (reste de la v4). Corriger en « cette v5 ». La commande
   ne liste aucune empreinte (amorce v2, suivi v1, dépôt réduit v6, journal) alors que le feu doit les citer ; ajouter un tableau des
   empreintes (info : pas de tableau en v4 non plus).
2. Mineure. commande l.43-44 et l.46-47. (a) `--env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 …"` : la valeur développée figure dans la
   ligne de commande du processus `vastai` du conteneur (visible par `ps` de la session) ; acceptable, à signaler. (b) Si `vastai create`
   échoue, il peut afficher le message d'erreur de l'API ; la commande ne passe pas la sortie de `create` par le balayage du suivi.
   Proposer de passer la sortie de `create --raw` par `balayer` (ou de ne garder que `new_contract`). Supposé, non vérifié sur l'outil.
3. Mineure. commande l.11 et l.67-72 : « Fin » (l.12) et l.13 ne disent pas que l'instance « exited » peut contenir les seuls exemplaires
   des résultats quand la poussée finale a échoué (voir remarque 4). Corriger : avant toute destruction d'une instance sortie, lire l'état
   poussé (l.71-72) et le journal ; si le journal contient « poussee en echec » ou si l'état poussé n'est pas l'état final, ne pas détruire
   sans décision de la mère (la minuterie à 90 % la détruit de toute façon : à signaler).
4. Moyenne. amorce l.72-77 et l.131-141 (poussée finale). Si les 10 poussées finales échouent, le script sort quand même avec le code
   d'origine (0 en cas de « course terminee », trap l.72-77) et le conteneur s'arrête : les résultats ne sont que sur le disque d'un
   conteneur « exited ». Combiné à la règle de la commande « exited → détruire aussitôt », cela perd la course. De plus, la poussée finale
   persistante (10 × 60 s) est coupée par la minuterie ou la garde à 90 % si elles tombent pendant ces 10 minutes (la commande l'écrit en
   commentaire seulement). Correction : (a) sortir avec un code distinct (ex. 15) si la poussée finale échoue après une course réussie,
   journalisé en dernière ligne ; (b) la commande doit interdire la destruction dans ce cas (remarque 3) ; (c) documenter l'interaction
   avec la minuterie. Vérifié dans le texte.
5. Moyenne. amorce l.51-57. Le fichier de plus de 95 Mo est détecté APRÈS `git add -A` et le commit, et seulement signalé. Si un fichier
   de `runs/` ou `diag/` dépasse la limite de l'hébergeur (100 Mo), le commit local le contient définitivement : toutes les poussées
   suivantes (périodiques et finale) échouent, même après suppression du fichier, car il est dans l'historique de la branche locale.
   Correction : tester la taille avant `git add`, exclure le fichier (par ex. ne pas le copier, journaliser) et poursuivre ; sinon
   `git reset` du commit fautif. La détection par `find -size +95M` n'est pas testée par l'essai à blanc (aucun cas). Vérifié dans le
   texte ; non exécuté.
6. Mineure. amorce. (a) l.45 `[ -d "$RESULTATS" ] || return 0` : retour silencieux « réussi » sans poussée (repli silencieux au sens
   R5). Inoffensif aujourd'hui (l.85 crée l'arbre avant toute poussée sauf la sortie 10), mais mieux : journaliser « pas d'arbre des
   résultats » et rendre 1, ou limiter au cas du code 10. (b) l.66 : après la dernière tentative infructueuse, le script dort encore 60 s
   (ou 16 s) avant de sortir ; inutile, à tester `i<n`. (c) l.2-19 : l'en-tête décrit les codes 10, 11, 12 mais pas 13
   (COMMANDE_COURSE hors mode jouet, l.121, sans ligne de journal) ni 14. (d) l.93 : `pip install --upgrade pip` non épinglé ; non
   reproductible (info). (e) le piège EXIT couvre les sorties normales et les signaux terminaux ; un `kill -9` ou une destruction par la
   plateforme n'est pas couvert (info, attendu). (f) l.102 : le code 14 survient après l'installation de torch (5 à 10 min) : « avant
   toute dépense de carte graphique » est vrai pour la course, mais la location court déjà ; reformuler dans la commande l.58-59 (info).
7. Moyenne (R5, repli silencieux). suivi_vast_v1.py l.20-21 et l.62-71. Si aucune variable de la liste n'est définie (ou de moins de 8
   caractères) dans le shell du suivi, `valeurs_secretes` rend une liste vide et le balayage ne détecte rien, sans avertissement : un
   suivi lancé depuis un shell sans `CONTROLE_IA_GITHUB_TOKEN_2` imprime tout, journaux compris. Le test n'exerce pas ce cas. Correction :
   refuser de tourner (ou avertir en tête de sortie et sortir en erreur pour `logs`) si `CONTROLE_IA_GITHUB_TOKEN_2` n'est pas défini ;
   ajouter l'essai (cas sain et cas artefact : variable absente).
8. Moyenne. suivi_vast_v1.py l.24-28. Le balayage ne cherche que la valeur brute. L'amorce construit l'en-tête
   `Authorization: Basic base64("x-access-token:<jeton>")` ; si un journal (trace curl, message d'erreur) restitue cet en-tête, la forme
   encodée n'est pas détectée. Correction : balayer aussi la forme base64 de `x-access-token:<jeton>` (et du jeton seul), avec les trois
   alignements possibles du base64 si on cherche une sous-chaîne dans un flux plus large, ainsi que la forme encodée pour une URL. Le
   fonctionnement fermé (la sortie est refusée entièrement) peut en outre rendre `vastai logs` inutilisable si le loueur imprime lui-même
   les variables d'environnement dans les journaux ; dans ce cas il faudrait expurger (remplacer par `***`) plutôt que refuser, en gardant
   la détection comme alarme (supposé : comportement du loueur non vérifié).
9. Mineure. suivi / essai. (a) Le filtrage « champs imbriqués » est une liste blanche de neuf clés (l.17, l.31) : vrai pour tout champ à
   secret (`extra_env`, `onstart`, etc.). Le test (l.14, l.17) place bien le jeton dans `extra_env` sous forme de liste de listes et de
   dictionnaire : la preuve par liste blanche est correcte (vérifié). Mais `label` et `status_msg` sont du texte libre non filtré : ils
   passent par le balayage seul. Aucun essai ne met le secret dans un champ gardé de l'appel `instance` (seul le cas `logs` est essayé,
   test l.30-36). Ajouter l'essai. (b) l.43 : le contenu d'erreur de `vastai` est imprimé (200 caractères de la dernière ligne), balayé
   ensuite par `main` : correct. (c) l.44-45 et l.52 : réponse enveloppée (dictionnaire à clé `instances` ou liste, selon la version de
   l'outil, supposé) → `filtrer` rend `{}` sans le dire ; `{}` n'est pas `{"absente": true}`. À traiter explicitement (signaler « forme
   inattendue »). (d) l.36 : `vastai` doit être sur le `PATH` du Python lancé (la commande l.25 dit « environnement à part ») ; sinon
   traceback `FileNotFoundError`. À préciser dans la commande (supposé). (e) l.48-52 : en cas d'erreur, `instances` rend un dictionnaire
   `{"erreur":…}` au lieu d'une liste ; l'étape 13 (« instance absente ») repose sur lecture humaine : une erreur ne doit pas se lire comme
   absence. Ajouter dans la commande : « un résultat contenant `erreur` n'est pas une preuve d'absence ».
10. Mineure. depot_reduit_v6.py l.50. L'expression de garde des secrets ne couvre ni `github_pat_…` ni `gho_/ghs_/ghu_/ghr_` ; seul
    `ghp_` y est. Le jeton du programme peut être d'un autre type (non vérifié). Élargir : `gh[opsur]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}`.
    Info : le `.gitignore` généré (l.77) contient `.venv/`, `__pycache__/`, `.pytest_cache/` ; cela rend l'arbre propre après pip et
    pytest en mode réel (vérifié dans le texte). Les huit fichiers d'essai de l'amorce (l.33) figurent tous dans la liste du dépôt réduit
    (vérifié par comparaison) ; le suivi n'y est pas (inutile sur la machine).
11. Mineure. essai-a-blanc-amorce-v2.txt l.1 : « commit source HEAD » (nom mobile, pas un commit) ; la traçabilité R6/R12 exige le hachage
    du commit source. Mieux : résoudre HEAD en hachage avant l'appel (script l.12, l.36), et verser dans le journal `liste_sha256` et
    `paquet_sha256` de `rapport.json`, pour prouver que l'arbre essayé est celui qui sera réellement poussé.
12. Moyenne. Couverture de l'essai à blanc (script et journal). (a) Le mode jouet saute les lignes 92 à 99 et 124-125 de l'amorce
    (création de l'environnement, installation par pip, exigence de la carte graphique, vraie commande de course) : le chemin réel n'est
    pas essayé. Surtout, le code 11 (carte graphique absente) n'a aucun cas d'artefact, de même que le code 10 par « arbre non propre »
    (l.84) et l'état « arbre sali par les essais » (l.115). La commande l.80-83 annonce « 10, 12, 12, 14 », ce que le journal confirme
    (l.22-25) ; mais l'annonce « 10 à 14 » (l.64) dépasse les cas essayés. Au minimum : ajouter un cas où `VENV_JOUET` est un interprète
    sans GPU ne suffit pas car le mode jouet saute la garde ; proposer un mode d'essai de la garde GPU (variable de test) ou le signaler
    comme non couvert. (b) L'absence du jeton dans l'environnement de pytest et de pip n'est pas prouvée : seul le processus de course
    factice écrit « course sans jeton » (journal l.13). Proposer un essai « sauté-comme-échec » : un test de la liste factice qui échoue si
    `GH_TOKEN` est présent dans `os.environ`, essayé en cas sain et en cas artefact (amorce modifiée sans `env -u`). (c) Le clone de
    l'essai est un `file://` : l'en-tête HTTP est ignoré, donc l'essai ne prouve pas que le jeton n'est pas écrit par le clone HTTPS réel.
    Raisonnement par lecture (`-c` avant `clone` ne persiste pas ; l'adresse d'origine est sans jeton, l.40-41 et commande l.18-22) :
    cohérent, mais non éprouvé (supposé).
13. Mineure. Balayage du jeton (script l.45 ; journal l.47). Il ne cherche que la forme brute (voir remarque 8) et pas l'en-tête encodé ;
    il ne couvre ni `/proc/*/environ` ni la ligne de commande des processus (le jeton y figure forcément dans `git -c http.extraHeader=…`,
    et en brut dans l'environnement du processus 1 de la machine). Cela ne sort pas du disque poussé mais l'énoncé « ni le disque … ne le
    contiennent » (commande l.20-22) vaut pour les fichiers, non pour la mémoire des processus ni pour la configuration du loueur (déjà
    reconnue l.19-20). Reformuler. Ajouter la forme base64 au balayage. Le journal montre les causes de poussée refusée réduites à « and
    the repository exists. » (l.29-44) : cette dernière ligne de git est peu utile ; garder les deux dernières lignes (borne de 200
    caractères).

## Autres points vérifiés (sans remarque)
- Filtre de l'offre (l.29) : `gpu_name=RTX_4090 num_gpus=1 … cuda_max_good>=13.0 dph_total<=0.90 rentable=true` ; création sur UNE offre
  à la fois ; disque 80 ≥ 80 ; image `python:3.12-bookworm`. Cohérent avec le prix plafond de 0,90 USD/h. Ni les coûts de trafic ni le
  critère « vérifié » du loueur ne sont dans le filtre (info).
- Cohérence des noms : commande v5 ↔ amorce v2 (l.44) ↔ dépôt réduit v6 (l.45) ↔ branche `course/neuron-lens-volet-a-reduit-v6`
  (commande l.34-36, l.44 ; essai l.14) ↔ branche des résultats `calcul/neuron-lens-volet-a-v1` (commande l.37, l.43 ; amorce l.28).
  Cohérents. L'état poussé s'appelle `etat-neuron-lens-volet-a.txt` partout.
- Gardes de la commande : minuterie avant la passe (l.48-50), garde à 60 % / 90 % (l.51-54), rappel à 80 % (l.55), destruction par
  identifiant puis vérification (l.75-76), arrêts par PID (l.50-51, l.75-76), instances d'autres sessions protégées (l.15-16). Conformes
  à R10 sur le texte ; je n'ai pas lu `garde_depense_v3` (hors liste).
- Amorce : codes 10 (l.83-84), 11 (l.97), 12 (l.113, l.115), 13 (l.121), 14 (l.102) ; la sortie finale conserve le code de la course
  (l.141) ; `set +x` (l.21) et aucun `set -x` ailleurs (vérifié par lecture) ; jeton jamais passé à pip, pytest, course
  (`env -u GH_TOKEN`, l.93-94, 108, 122, 124) ; adresse d'origine sans jeton.

Limites de son contrôle : il n'a exécuté que les essais du suivi ; rien du réseau, du loueur, de l'amorce ni de l'essai à blanc. Tout ce
qui touche à l'outil du loueur (forme des sorties, `--args`, contenu des journaux) reste « supposé ».
