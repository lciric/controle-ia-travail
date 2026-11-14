# Commande de location et de lancement du volet A de « Neuron Lens » — v7, sans ssh (proposée, **non exécutée**)

Remplace la v6 (`commande-volet-a-v6.md`, `a0cf3804…`, archivée) après sa contre-lecture 8, ciblée
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-8-commande-v6.md`, `6964ad1a…`), faite et intégrée par la session de
reprise (autre compte, `prep/neuron-lens-v1`). Suites données :
- N-1 → l'amorce v5 inscrit `exclus=<n>` dans l'état poussé ; règle de destruction : `exclus` non nul → pas de destruction sans la
  mère (le fichier exclu est perdu à la destruction ; aucun fichier de plus de 95 Mo n'est attendu de la course, supposé : les sorties
  de `volet_a_course_v4` sont des mesures et des décisions en JSON) ;
- N-2 → `suivi_vast_v3` : sortie vide ou blanche = erreur (seul `[]` est une liste vide), témoin de lecture pour `absente` ;
- N-3 → amorce v5 : copie, état, `git add`, `git commit` en échec = poussée en échec ; « pousse » écrit seulement si la tête distante
  (`ls-remote`) égale la tête locale ; artefact « crochet » (commit refusé pendant la course) joué à blanc ;
- N-4 → essai à blanc v6 : témoins positifs (une forme par fichier ; un dépôt témoin dont un message de commit porte une forme), objets
  git décompressés balayés, erreur de `grep` non masquée ; « brute = adresse pour ce jeton » écrit ;
- N-5 → étape 0 : `suivi_vast_v3 verifier` et lecture de la liste avant la location ; création interdite si le suivi échoue ou si la
  variable du jeton manque ;
- N-6 → tableau « dernière ligne du journal et état poussé → destruction ou non » (étape 11) ; la dernière ligne sans course lancée
  ne contient plus « echec » (« fin sans poussee finale (aucune course lancee, aucun resultat a sauver) ») ;
- N-7 → constat de l'essai v6 : la **liste** du dépôt réduit est stable tant que ses fichiers ne changent pas (`da640eb0…` aux commits
  `11ed9ec3` et `4f7e2265`), mais le **commit réduit** et le **paquet** changent avec le commit source (le message du commit réduit
  nomme le commit source) ; au feu, liste attendue `da640eb0…` ; une liste différente exige un nouvel essai à blanc ;
- N-8 a → `find` non masqué et second contrôle des fichiers indexés ; b → un fichier déjà poussé qui grossit garde à la tête sa version
  déjà poussée (cas « grossit » joué à blanc) ; c → `pip` 26.2.2 existe sur l'index public (roue téléchargée le 14 novembre, conteneur
  de la session) ; d → sans course lancée, poussée finale de 2 essais à 5 s ; e, f → info, inchangés ;
- N-9 a → enveloppes de `show instance` déballées ; b → délai capturé ; c → `new_contract` extrait par motif si la sortie n'est pas du
  JSON pur ;
- N-10 → info ; N-11 → étape 6 écrite `( sleep $D; vastai destroy instance <ID> ) &` ; N-12 → première poussée (« commit verifie »)
  avant l'installation de l'environnement : le code 14 tombe en moins d'une minute ;
- § 3 → formes base 64 « url-safe » ajoutées (pour un jeton fait de lettres, chiffres, `_` et `-`, elles sont identiques aux
  standards : aucun groupe de 6 bits `111110` ou `111111` ne peut s'y former ; essai sur un secret synthétique qui discrimine) ; base 64
  coupée en lignes et secrets de 8 à 13 octets : limites déclarées.
En cours d'intégration, l'essai à blanc v5 a eu un compteur faux (cas « crochet » : il comptait la ligne « etat non pousse : … ») ;
l'amorce était juste ; essai v6 = v5 avec le compteur ancré sur l'heure (journal v5 versé aussi).

Historique : la v6 remplaçait la v5 (`112de376…`) après la contre-lecture 7 ; la v5 la v4 (`417ca3b4…`) ; la v4 la v3 (`992e11ac…`),
dont le feu (R-2749) est tombé : le conteneur de la session ne peut pas joindre la machine par ssh. Décision de la mère R-2752 :
commande sans ssh — branche dédiée du dépôt réduit, script de démarrage de l'instance, résultats poussés sur une branche du dépôt de
travail privé, suivi filtré.

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien ne part sans un **nouveau feu écrit de la
mère, avec le numéro de ligne**, citant cette v7 et ses empreintes. Toute heure consignée vient de `date -u` dans la même commande.
Jamais vers `main`, jamais vers `lciric/controle-ia`, rien dans `registres/`. Ne jamais toucher les instances 58936096, 58936099,
58936100, 60480302, 60599797, ni aucune instance ou serveur d'une autre session (inventaire du 14 novembre 13:50 UTC, lecture seule :
chez le loueur, 58936096, 58936099, 58936100 « exited » et 60480302 « running » ; deux serveurs Hetzner d'une autre session).

**Secrets** : `VAST_API_KEY` reste dans le conteneur, lue par son nom. Le seul secret passé à la machine est le jeton du programme :
`GH_TOKEN` reçoit la valeur de `CONTROLE_IA_GITHUB_TOKEN_2`, développée par le shell du lancement, jamais affichée ni écrite. Elle
figure (a) dans la configuration de l'instance chez le loueur jusqu'à sa destruction, (b) dans la ligne de commande du processus de
création de l'outil du loueur, le temps de l'appel (visible par `ps` dans le conteneur de la session), (c) sur la machine, dans
l'environnement du processus d'entrée et dans la ligne de commande de chaque `git` le temps de son exécution (en-tête
`-c http.extraHeader`, base 64). Aucun **fichier** ni **objet git** de la machine, des résultats poussés ou des journaux ne la contient
(essayé à blanc, sous 7 formes, avec témoins positifs) ; l'adresse du dépôt et la configuration git ne la contiennent pas ; la course
tourne **sans** elle (`env -u GH_TOKEN`). Le modèle et les lentilles sont publics.

**Suivi** : tout appel à l'outil du loueur dont la sortie pourrait porter la configuration passe par
`src/controle_ia/neuron_lens/suivi_vast_v3.py` (champs filtrés ; refus de toute sortie portant un secret, brut, encodé pour une
adresse ou en base 64 ; refus de tourner si `CONTROLE_IA_GITHUB_TOKEN_2` manque au shell ; sortie vide = erreur). L'outil doit être sur
le `PATH` du Python lancé, ou désigné par `VASTAI_OUTIL=<chemin>`. Un résultat `erreur` n'est jamais lu comme une absence. Le
fonctionnement est fermé : une sortie à secret est refusée entière, jamais expurgée ; si les journaux du loueur deviennent illisibles
pour cette raison, le suivi passe par la branche des résultats seule, et la mère est prévenue.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : `vastai` 1.11.0, installé dans un environnement à part de l'espace de travail ; clé lue par son nom ;
   `export VASTAI_OUTIL=<chemin de l'outil>`.
2. **Suivi prêt** (gratuit) : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ]` (longueur seule, jamais la valeur) ;
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v3 verifier` → code 0 exigé ;
   `… suivi_vast_v3 instances` → liste consignée (identifiants et états seulement) ; une instance d'une autre session qui y figure
   sert de **témoin** à l'étape 13. Un échec, une forme inattendue ou un refus → **aucune création**, message à la mère.
3. `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; print(json.load(sys.stdin)["credit"])'` → **crédit relevé**
   (seul ce champ est imprimé), consigné au journal. Crédit < 12 USD → arrêt, message à la mère.
4. Prix du jour :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=8 disk_space>=80 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.90 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA consignés. Aucune offre → arrêt. (Ni le coût du
   trafic ni le critère « vérifié » du loueur ne sont dans le filtre ; le trafic est surveillé par la garde au prix total.)
5. **Dépôt réduit** au commit scellé de la course :
   `python scripts/depot_reduit_neuron_lens_volet_a_v9.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256`, `rapport.json` (commit
   réduit, empreinte de la liste, empreinte du paquet), paquet `neuron-lens-volet-a-reduit.bundle` ; liste attendue `da640eb0…`. Le
   commit réduit est poussé sur la **branche dédiée** `course/neuron-lens-volet-a-reduit-v9` du dépôt de travail :
   `git fetch <paquet> course:refs/heads/course/neuron-lens-volet-a-reduit-v9 && git push origin course/neuron-lens-volet-a-reduit-v9` ;
   puis `git ls-remote origin refs/heads/course/neuron-lens-volet-a-reduit-v9` = commit réduit, et
   `git ls-remote origin refs/heads/calcul/neuron-lens-volet-a-v1` **vide** (branche des résultats absente ; sinon arrêt).

## 1. Location (une seule instance), minuterie, garde, rappel
6. Création (image `python:3.12-bookworm` : git, venv et coreutils compris ; `torch` installé par `pip` avec ses bibliothèques CUDA),
   sortie réduite à `success` et `new_contract` :
   ```
   GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 80 --label neuron-lens-volet-a \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e COMMIT_REDUIT=<COMMIT_REDUIT> -e GO_ID=GO-2026-11-14-05 -e RUN_ID=<AAAAMMJJ-HHMMSS>-neuron-lens-volet-a -e CACHE_HF=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-volet-a-v1 -e PERIODE_POUSSE_S=1800" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-volet-a-reduit-v9 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_volet_a_v5.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v3 creation
   ```
   → **identifiant d'instance** (`new_contract`, éventuellement « extrait par motif ») et heure de création consignés. (Les `$` des
   arguments sont entre apostrophes : développés sur la machine, pas dans le conteneur ; seul `$CONTROLE_IA_GITHUB_TOKEN_2` de `--env`
   est développé par le shell du lancement. `--args` est une liste transmise telle quelle, `["-c", "<texte>"]`, d'après la source de
   l'outil 1.11.0 : lu, non éprouvé.) Code non nul (aucun `new_contract`) → `… suivi_vast_v3 instances` pour savoir si une instance a
   été créée malgré tout ; arrêt, message à la mère.
7. **Minuterie de destruction par identifiant**, posée aussitôt (R10), durée comptée depuis la création :
   `D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --minuterie-seulement --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION>)`
   puis `( sleep "$D"; vastai destroy instance <ID> ) &` (PID du sous-shell consigné ; c'est lui qu'on arrête).
8. **Garde de dépense** en arrière-plan (PID consigné) :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl`
   → compte rendu à la mère à 60 % (6 USD, elle décide de la suite) ; destruction réessayée et vérifiée à 90 % (9 USD ; code 4 et
   message immédiat à la mère si elle échoue).
9. **Rappel indépendant** : `send_later` à 80 % de la durée de la minuterie, « vérifier et détruire l'instance <ID> ».

## 2. Sur la machine (script `scripts/amorce_neuron_lens_volet_a_v5.sh`, sans intervention)
10. Commit égal à `COMMIT_REDUIT` et arbre propre, sinon arrêt (code 10, visible dans les journaux seulement) ; première poussée
    (« commit verifie ») impossible → arrêt (code 14, en moins d'une minute, avant l'installation de l'environnement) ; environnement
    aux versions épinglées (`pip` 26.2.2 compris) ; carte graphique exigée (code 11) ; essais rapides (liste de la v3), un échec, un essai
    sauté ou un arbre sali = arrêt (code 12) ; course `volet_a_lancer_v3` sans le jeton (`COMMANDE_COURSE` hors du mode jouet → code
    13) ; poussée sur `calcul/neuron-lens-volet-a-v1` des `runs/<run_id>/`, `diag/<run_id>/` et d'un fichier d'état
    `etat-neuron-lens-volet-a.txt` (`run_id`, `etat`, `heure`, `commit_reduit`, `exclus`) à chaque étape, toutes les 30 min pendant la
    course, à la fin et à tout arrêt (sauf le code 10) ; une poussée n'est déclarée faite (« pousse : … ») que si la tête distante égale
    la tête locale ; un fichier de plus de 95 Mo est exclu avant `git add` (il reste sur le disque de l'instance ; s'il avait déjà été
    poussé plus petit, cette version reste à la tête) ; poussée finale persistante après une course (10 essais espacés de 60 s, ≈ 10
    min) ; si elle échoue : code 15 si la course a réussi, sinon le code de la course. Le conteneur s'arrête à la fin du script.

## 3. Suivi, retour et destruction (conteneur de la session)
11. Suivi, **jamais par une sortie brute de l'outil du loueur** :
    `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v3 logs <ID> 40` (lignes `AMORCE …`) et
    `… suivi_vast_v3 instance <ID>` ; état de la course :
    `git fetch origin +refs/heads/calcul/neuron-lens-volet-a-v1:refs/remotes/origin/calcul/neuron-lens-volet-a-v1` puis
    `git show refs/remotes/origin/calcul/neuron-lens-volet-a-v1:etat-neuron-lens-volet-a.txt`.
    **Règle de destruction** d'une instance sortie (« exited », stockage facturé) ou arrêtée, lue sur la **dernière ligne** du journal
    (`logs`) et sur l'**état poussé** :

    | dernière ligne du journal | état poussé | destruction |
    |---|---|---|
    | « fin sans arbre des resultats : … » (code 10) | aucun | aussitôt |
    | « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : … » | aucun ou non final | aussitôt |
    | « fin : arret code N (…) », course non lancée (codes 11 à 14, ou 1, 2, 127 : `pip`, `git worktree`…) | « arret code N … », `exclus=0` | aussitôt |
    | « fin : course terminee » ou « fin : arret code N (course en echec …) » | égal à la dernière ligne, `exclus=0` | aussitôt, après l'étape 12 |
    | toute ligne ci-dessus | `exclus` non nul | **pas sans la mère** (fichier exclu perdu à la destruction) |
    | « POUSSEE FINALE EN ECHEC : … » (code 15 ou course en échec) | non final | **pas sans la mère**, message immédiat |
    | toute autre (journal coupé, signal, ligne inconnue) | quelconque | **pas sans la mère**, message immédiat |

    Dans les cas « pas sans la mère », la minuterie et la garde à 90 % restent armées et détruiront l'instance à leur échéance : le dire
    dans le message. Si elles tombent pendant la poussée finale (≈ 10 min), les résultats non poussés sont perdus ; la durée de la
    minuterie, comptée sur le plafond, le rend improbable au devis (borne haute 7 USD sur 10, supposé : `garde_depense_v3` contre-lu
    lors des contre-lectures 3 à 5, non relu ici).
12. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque fichier de `diag/<run_id>/` ; fichiers exclus
    relevés dans le journal, et, pour un fichier qui a grossi, la version déjà poussée lue dans l'historique de la branche ; copie dans
    `prep/neuron-lens-v1` ; commit ; poussée de la branche seule.
13. `vastai destroy instance <ID>` ; `… suivi_vast_v3 absente <ID> --temoin <témoin de l'étape 2>` → code 0 exigé (absence prouvée
    seulement sur une liste lue sans erreur qui contient le témoin ; si le témoin a disparu entre-temps, `absente <ID>` sans témoin sur
    une liste non vide, et le dire) ; minuterie et garde arrêtées **par PID** ; rappel annulé ; crédit relevé de nouveau ; lignes
    proposées à la mère pour `registres/arrets.md` et `registres/depenses.md`.

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_v6.sh` ; journal complet versé (`docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v6.txt`,
empreinte au compagnon ; le journal v5, au compteur faux du cas « crochet », est versé aussi). Joué le 14 novembre à 14:32:40 UTC sur
le commit source `4f7e2265…` (commit réduit `a0946872…`, 73 fichiers, liste `da640eb0…`, paquet `bd48f192…`) :
- cas nominal, **liste réelle** des essais rapides plus une sonde qui échoue si `GH_TOKEN` est dans l'environnement de pytest :
  62 passés ; course jouet sans jeton ; poussées périodiques vérifiées ; fichier de 96 Mio exclu (journalisé, resté sur le disque de la
  machine, `exclus=1`) ; état final « course terminee », code 0 ;
- artefacts (R5) : mauvais commit → 10 ; arbre non propre → 10 ; essai en échec → 12 ; essai sauté → 12 ; arbre sali → 12 ; carte
  graphique absente (garde jouée en mode jouet) → 11 ; première poussée impossible → 14, dernière ligne « fin sans poussee finale… » ;
  poussée finale impossible après une course réussie → **15**, « POUSSEE FINALE EN ECHEC… » ; commit refusé pendant la course
  (crochet) → **15**, 3 refus journalisés, aucune ligne « pousse » après le premier refus, fichier écrit après le crochet absent de la
  branche ; fichier déjà poussé (1 Mio) qui grossit à 96 Mio → version de 1 Mio gardée à la tête, `exclus=1`, code 0 ; la sonde
  « sans jeton » jouée seule avec le jeton présent échoue (code 1) ;
- balayage du jeton factice sous 7 formes (pour ce jeton, brute = adresse) : témoins détectés 7 sur 7 et dépôt témoin détecté ;
  **0 fichier** (disques des machines d'essai, dépôt distant, journaux) et **0 ligne** d'objet git décompressé (12 dépôts).
Non couverts, déclarés : le chemin réel de la machine (création de l'environnement, `pip`, carte réelle, vraie course), le code 13, le
clone HTTPS réel (le clone de l'essai est local : l'en-tête n'y sert pas), la sérialisation réelle de `--args` par l'outil du loueur,
les signaux et l'abandon par `set -e`, les formes réelles des sorties de l'outil (essayées seulement à l'étape 2, avant la location).

## Jeton
Le jeton du programme permet l'écriture sur tout le dépôt de travail, `main` compris ; « jamais vers `main` » n'est garanti que par
l'amorce (poussée vers `refs/heads/calcul/neuron-lens-volet-a-v1` seulement). Si un jeton restreint à une branche existe, il est
préférable (point signalé à la mère, non tranché).

## Devis (inchangé depuis la v3, borne haute)
3,5 à 5,5 h, soit 3,2 à 5 USD à 0,90 USD/h, jusqu'à 7 USD si l'audit R4 « trop beau » se déclenche ; installation de `torch` et de ses
bibliothèques CUDA par `pip` en plus (≈ 5 à 10 min). Le débit réel n'est pas mesuré avant la course : la garde le surveille (6 USD
compte rendu, 9 USD arrêt dur). Si la version de CUDA de l'hôte ne convient pas à `torch` 2.14.1, l'amorce s'arrête au code 11 (quelques
minutes de location perdues).

## Empreintes des pièces citées
Toutes scellées (compagnon `.sha256`) ; la commande elle-même est au compagnon de ce fichier. Le commit réduit et le paquet de la
course sont rendus par le dépôt réduit v9 au commit final et cités dans la demande de feu.

| pièce | empreinte |
|---|---|
| `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-8-commande-v6.md` | `6964ad1ac38e571a5f7e3eac37171184dd35cc0905c6ae301dc797e69000c875` |
| `scripts/amorce_neuron_lens_volet_a_v5.sh` | `d0fbe933e1bb22b01509676301459db3d4713203ec90a5cf1c6c3e0fc3919939` |
| `src/controle_ia/neuron_lens/suivi_vast_v3.py` | `59b7bfafc56e422f360e628c14e05224c6fff9eed60e9aac21208e47b28b836b` |
| `tests/test_neuron_lens_suivi_vast_v3.py` | `963d2a729b1cec105ab1a3cf534642338b9d65575e9abfca05553214a3a7df9b` |
| `scripts/depot_reduit_neuron_lens_volet_a_v9.py` | `70cc611a82efce7a454892c8deefe944b4786c529b0e7a0be8809a530704ee82` |
| `scripts/essai_a_blanc_amorce_neuron_lens_v6.sh` | `9b70de5f02dc061c46811a514626c65727a2b67425bb9ce27f3a1b620d1482f5` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v6.txt` | `acc224366cfb5dbeb6849ef345f33465daf38c9031bd84f8d5f917242dfed1ad` |
| `src/controle_ia/neuron_lens/garde_depense_v3.py` | `692fa80e842f18a54e7bc937b19c7cb9ff71678c02153eb0c46ec8e34b97cc3d` |
| `src/controle_ia/neuron_lens/volet_a_lancer_v3.py` | `a52506f897adf9f55e3dbce8b6a832d086b0d23866b1ab6d75e122fff906b036` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `requirements-neuron-lens-volet-a-v1.txt` | `f61477e91763fa251fbd45e93fb17819883c70c45a60fb5ebd90b01feaca2312` |
| archivées, non employées : `scripts/essai_a_blanc_amorce_neuron_lens_v5.sh` | `1f61f65cde50640293791790728f006d50238fb8836f8b1796fe63b68c8cdda0` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v5.txt` | `330f761e8ba357fdf460efdca789f66c1debe69363dc1fa54f281dba8fefaa99` |
| `docs/notes/neuron-lens-v1/commande-volet-a-v6.md` | `a0cf38041e462807f1ac0211aa9bade9d211402765acf61b3f656902e029c111` |
| `scripts/amorce_neuron_lens_volet_a_v4.sh` | `26c78c11eee0dd506fc5669fde50da9af0a0fd00f195d0d8828c5a742e8125c8` |
| `src/controle_ia/neuron_lens/suivi_vast_v2.py` | `957ad4a633f18300e0551fad30b97b7db8a92d366728c2fa6218c2919bf02480` |
| `scripts/depot_reduit_neuron_lens_volet_a_v8.py` | `dcabac908d52c6075daf477ccc489a79005c50b398c34c8c4b10973c04d24dbe` |
