# Commande de location et de lancement du volet A de « Neuron Lens » — v8, sans ssh (proposée, **non exécutée**)

Remplace la v7 (`commande-volet-a-v7.md`, `b36146d0…`, archivée) après sa contre-lecture 9, ciblée
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-9-commande-v7.md`, `214e280b…`), faite et intégrée par la session de
reprise (autre compte, `prep/neuron-lens-v1`). Suites données :
- P-1 → étape 1 : l'outil du loueur est mis sur le `PATH` du shell de la session (`command -v vastai` et `vastai show user` au code 0
  exigés) ; la minuterie et la garde sont lancées par `setsid nohup`, dans la même commande que le calcul de la durée, et leur PID est
  vérifié vivant (étapes 7 et 8) ;
- P-2 → artefact « lsremote » (enveloppe de `git` qui falsifie `ls-remote`) joué à blanc : code 14, aucune ligne « pousse » ;
- P-3 → artefacts joués à blanc : `find` en échec (14), `find` muet avec un fichier de 96 Mio (le second contrôle refuse le commit : 15),
  copie impossible (15), index verrouillé (`git add` impossible : 15), état non inscriptible (15) ; non jouée, déclarée : la
  restauration impossible de la version déjà poussée d'un fichier qui grossit ;
- P-4 → essai v7 : objets lus comptés par dépôt (aucun dépôt sans objet lu exigé), erreurs de `git` et de `grep` comptées comme écarts,
  poussées de l'essai non masquées, dépôt témoin empaqueté avec un blob ET un message porteurs d'une forme ; code attendu par cas et
  verdict final automatique ;
- P-5 → `suivi_vast_v4 absente … --non-vide` ; étape 13 : témoin, sinon `--non-vide`, sinon (plus aucune instance sur le compte) liste
  `[]` acceptée, et le dire ;
- P-6 → l'amorce v6 inscrit les noms des fichiers exclus dans l'état poussé (`exclus_fichiers=`) ; dit ci-dessous : un fichier exclu
  est irrécupérable sans ssh (garder l'instance ne fait que payer le stockage) ;
- P-7 → `suivi_vast_v4` : `instance`, `instances` et `logs` rendent le code 1 sur erreur ;
- P-8 → table de destruction annotée ; ligne ajoutée pour l'échec du clone d'entrée ;
- P-9 → « Secrets » reformulé (fichiers de l'arbre de travail, résultats poussés et journaux) ; étape 12 : la version déjà poussée d'un
  fichier qui a grossi est à la tête ; pièce versée pour `pip` 26.2.2 (`verification-pip-26-2-2-v1.txt`, roue `fd7f4dfa…`,
  `Requires-Python >=3.10`) ;
- P-10 → amorce v6 : tête locale contrôlée, échec de la liste du second contrôle rattrapé ;
- P-11 → info, inchangés (liste des essais rapides héritée de la v3 ; code 14 mesuré sans délai réseau) ;
- docstring des secrets courts → `suivi_vast_v4`.
Raison de « pour un jeton de lettres, chiffres, `_` et `-`, la base 64 standard ne contient ni `+` ni `/` » (contre-lecture 9) : un tel
caractère demande un groupe de 6 bits commençant par cinq 1 ; ces octets ont le bit fort à 0 ; seul `_` porte cinq 1 consécutifs, à une
position impaire, alors que les groupes commencent aux positions paires. La sécurité n'en dépend pas : les deux familles de formes
sont produites pour tout secret.

Historique : v7 ← contre-lecture 8 ; v6 ← contre-lecture 7 ; v5 ← contre-lecture 6 ; v4 et v3 (`992e11ac…`, dont le feu R-2749 est
tombé : pas de ssh depuis le conteneur). Décision de la mère R-2752 : commande sans ssh — branche dédiée du dépôt réduit, script de
démarrage de l'instance, résultats poussés sur une branche du dépôt de travail privé, suivi filtré. Consigne de la mère R-2772 (nouveau
compte) : rien ne part avant la commande contre-lue et scellée, puis la demande de feu citant la commande, le commit réduit, la liste et
l'empreinte du paquet ; une seule instance.

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien ne part sans un **nouveau feu écrit de la
mère, avec le numéro de ligne**, citant cette v8 et ses empreintes. Toute heure consignée vient de `date -u` dans la même commande.
Jamais vers `main`, jamais vers `lciric/controle-ia`, rien dans `registres/`. Ne jamais toucher les instances 58936096, 58936099,
58936100, 60480302, 60599797, ni les serveurs `poste-temoin-bailey-*`, ni aucune instance ou serveur d'une autre session (inventaire
du 14 novembre 13:50 UTC, lecture seule : chez le loueur, 58936096, 58936099, 58936100 « exited » et 60480302 « running » ; deux
serveurs Hetzner `poste-temoin-bailey-v9` et `-v12`).

**Secrets** : `VAST_API_KEY` reste dans le conteneur, lue par son nom. Le seul secret passé à la machine est le jeton du programme :
`GH_TOKEN` reçoit la valeur de `CONTROLE_IA_GITHUB_TOKEN_2`, développée par le shell du lancement, jamais affichée ni écrite. Elle
figure (a) dans la configuration de l'instance chez le loueur jusqu'à sa destruction (et dans ce que le loueur en écrit sur la machine,
non vérifié), (b) dans la ligne de commande du processus de création de l'outil du loueur, le temps de l'appel (visible par `ps` dans le
conteneur de la session), (c) sur la machine, dans l'environnement du processus d'entrée et dans la ligne de commande de chaque `git`
le temps de son exécution (en-tête `-c http.extraHeader`, base 64). Aucun fichier de l'arbre de travail, aucun résultat poussé, aucun
journal et aucun objet git des dépôts de l'essai ne la contient (essayé à blanc, sous 7 formes, avec témoins positifs) ; l'adresse du
dépôt et la configuration git ne la contiennent pas ; la course tourne **sans** elle (`env -u GH_TOKEN`). Le modèle et les lentilles
sont publics.

**Suivi** : tout appel à l'outil du loueur dont la sortie pourrait porter la configuration passe par
`src/controle_ia/neuron_lens/suivi_vast_v4.py` (champs filtrés ; refus de toute sortie portant un secret, brut, encodé pour une
adresse ou en base 64 ; refus de tourner si `CONTROLE_IA_GITHUB_TOKEN_2` manque au shell ; sortie vide = erreur ; code 1 sur erreur).
Un résultat `erreur` n'est jamais lu comme une absence. Le fonctionnement est fermé : une sortie à secret est refusée entière, jamais
expurgée ; si les journaux du loueur deviennent illisibles pour cette raison, le suivi passe par la branche des résultats seule, et la
mère est prévenue.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : `vastai` 1.11.0, installé dans un environnement à part de l'espace de travail ; clé lue par son nom ; **mis sur le
   `PATH` du shell de la session** (la création, la minuterie, la garde `garde_depense_v3` et la destruction l'appellent par son nom) :
   `export PATH=<environnement de l'outil>/bin:$PATH; export VASTAI_OUTIL=$(command -v vastai)` ; puis `command -v vastai` et
   `vastai show user --raw > /dev/null` au code 0 exigés (sortie jetée). Sinon arrêt.
2. **Suivi prêt** (gratuit) : `[ ${#CONTROLE_IA_GITHUB_TOKEN_2} -ge 8 ]` (longueur seule, jamais la valeur) ;
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v4 verifier` → code 0 exigé ;
   `… suivi_vast_v4 instances` → code 0 exigé, liste consignée (identifiants et états seulement) ; une instance d'une autre session qui y
   figure et doit durer (60480302, « running » au relevé) sert de **témoin** à l'étape 13. Un échec, une forme inattendue ou un refus →
   **aucune création**, message à la mère.
3. `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; print(json.load(sys.stdin)["credit"])'` → **crédit relevé**
   (seul ce champ est imprimé), consigné au journal. Crédit < 12 USD → arrêt, message à la mère.
4. Prix du jour :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=8 disk_space>=80 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.90 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA consignés. Aucune offre → arrêt. (Ni le coût du
   trafic ni le critère « vérifié » du loueur ne sont dans le filtre ; le trafic est surveillé par la garde au prix total.)
5. **Dépôt réduit** au commit scellé de la course :
   `python scripts/depot_reduit_neuron_lens_volet_a_v10.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256`, `rapport.json` (commit
   réduit, empreinte de la liste, empreinte du paquet), paquet `neuron-lens-volet-a-reduit.bundle` ; liste attendue `801b0202…` (celle
   de l'essai à blanc v7 ; une liste différente exige un nouvel essai à blanc ; le commit réduit et le paquet changent avec le commit
   source, dont le message du commit réduit porte le nom). Le commit réduit est poussé sur la **branche dédiée**
   `course/neuron-lens-volet-a-reduit-v10` du dépôt de travail :
   `git fetch <paquet> course:refs/heads/course/neuron-lens-volet-a-reduit-v10 && git push origin course/neuron-lens-volet-a-reduit-v10` ;
   puis `git ls-remote origin refs/heads/course/neuron-lens-volet-a-reduit-v10` = commit réduit, et
   `git ls-remote origin refs/heads/calcul/neuron-lens-volet-a-v1` **vide** (branche des résultats absente ; sinon arrêt).

## 1. Location (une seule instance), minuterie, garde, rappel
6. Création (image `python:3.12-bookworm` : git, venv et coreutils compris ; `torch` installé par `pip` avec ses bibliothèques CUDA),
   sortie réduite à `success` et `new_contract` :
   ```
   GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 80 --label neuron-lens-volet-a \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e COMMIT_REDUIT=<COMMIT_REDUIT> -e GO_ID=GO-2026-11-14-05 -e RUN_ID=<AAAAMMJJ-HHMMSS>-neuron-lens-volet-a -e CACHE_HF=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-volet-a-v1 -e PERIODE_POUSSE_S=1800" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-volet-a-reduit-v10 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_volet_a_v6.sh' \
     2>&1 | PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v4 creation
   ```
   → **identifiant d'instance** (`new_contract`, éventuellement « extrait par motif ») et heure de création consignés. (Les `$` des
   arguments sont entre apostrophes : développés sur la machine, pas dans le conteneur ; seul `$CONTROLE_IA_GITHUB_TOKEN_2` de `--env`
   est développé par le shell du lancement. `--args` est une liste transmise telle quelle, `["-c", "<texte>"]`, d'après la source de
   l'outil 1.11.0 : lu, non éprouvé.) Code non nul (aucun `new_contract`) → `… suivi_vast_v4 instances` pour savoir si une instance a
   été créée malgré tout ; arrêt, message à la mère.
7. **Minuterie de destruction par identifiant**, posée aussitôt (R10), durée comptée depuis la création, dans **une seule commande**
   (le processus est détaché de l'appel du shell, l'outil est trouvé par le `PATH` hérité de l'étape 1) :
   ```
   D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --minuterie-seulement --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION>) && [ -n "$D" ] && \
     setsid nohup bash -c "sleep $D; vastai destroy instance <ID>" > docs/notes/neuron-lens-v1/minuterie-volet-a-v1.log 2>&1 < /dev/null & echo "PID minuterie $! ; durée $D s"
   ```
   puis `ps -p <PID> -o pid,args` → vivant exigé (sinon arrêt, destruction aussitôt, message à la mère). C'est ce PID qu'on arrête
   (le `sleep` qu'il porte s'arrête avec lui ou reste orphelin, inoffensif).
8. **Garde de dépense**, détachée de la même façon (PID consigné et vérifié vivant) :
   `setsid nohup env PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl > docs/notes/neuron-lens-v1/garde-volet-a-v1.log 2>&1 < /dev/null & echo "PID garde $!"`
   → compte rendu à la mère à 60 % (6 USD, elle décide de la suite) ; destruction réessayée et vérifiée à 90 % (9 USD ; code 4 et
   message immédiat à la mère si elle échoue).
9. **Rappel indépendant** : `send_later` à 80 % de la durée de la minuterie, « vérifier et détruire l'instance <ID> ».

## 2. Sur la machine (script `scripts/amorce_neuron_lens_volet_a_v6.sh`, sans intervention)
10. Commit égal à `COMMIT_REDUIT` et arbre propre, sinon arrêt (code 10, visible dans les journaux seulement) ; première poussée
    (« commit verifie ») impossible → arrêt (code 14, avant l'installation de l'environnement : 19 s à blanc, sans délai réseau) ;
    environnement aux versions épinglées (`pip` 26.2.2 compris) ; carte graphique exigée (code 11) ; essais rapides (liste de la v3), un
    échec, un essai sauté ou un arbre sali = arrêt (code 12) ; course `volet_a_lancer_v3` sans le jeton (`COMMANDE_COURSE` hors du mode
    jouet → code 13) ; poussée sur `calcul/neuron-lens-volet-a-v1` des `runs/<run_id>/`, `diag/<run_id>/` et d'un fichier d'état
    `etat-neuron-lens-volet-a.txt` (`run_id`, `etat`, `heure`, `commit_reduit`, `exclus`, `exclus_fichiers`) à chaque étape, toutes
    les 30 min pendant la course, à la fin et à tout arrêt (sauf le code 10) ; une poussée n'est déclarée faite (« pousse : … ») que si
    chaque étape de sa préparation a réussi et si la tête distante égale la tête locale ; un fichier de plus de 95 Mo est exclu avant
    `git add` (il reste sur le disque de l'instance ; s'il avait déjà été poussé plus petit, cette version reste à la tête) ; poussée
    finale persistante après une course (10 essais espacés de 60 s, ≈ 10 min) ; si elle échoue : code 15 si la course a réussi, sinon
    le code de la course. Le conteneur s'arrête à la fin du script.

## 3. Suivi, retour et destruction (conteneur de la session)
11. Suivi, **jamais par une sortie brute de l'outil du loueur** :
    `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v4 logs <ID> 40` (lignes `AMORCE …`) et
    `… suivi_vast_v4 instance <ID>` (code 1 sur erreur) ; état de la course :
    `git fetch origin +refs/heads/calcul/neuron-lens-volet-a-v1:refs/remotes/origin/calcul/neuron-lens-volet-a-v1` puis
    `git show refs/remotes/origin/calcul/neuron-lens-volet-a-v1:etat-neuron-lens-volet-a.txt`.
    **Règle de destruction** d'une instance sortie (« exited », stockage facturé) ou arrêtée, lue sur la **dernière ligne** du journal
    (`logs`) et sur l'**état poussé** :

    | dernière ligne du journal | état poussé | destruction |
    |---|---|---|
    | « fin sans arbre des resultats : … » (code 10, ou autre échec avant l'arbre : `rev-parse`, `git worktree`) | aucun | aussitôt |
    | message `fatal:` de git sans aucune ligne `AMORCE` (échec du clone d'entrée) | aucun | aussitôt |
    | « fin sans poussee finale (aucune course lancee, aucun resultat a sauver) : … » | aucun ou non final | aussitôt |
    | « fin : arret code N (…) », course non lancée (codes 11 à 14, ou 1, 2, 127 : `pip`, environnement…) | « arret code N … », `exclus=0` | aussitôt |
    | « fin : course terminee » ou « fin : arret code N (course en echec …) » | égal à la dernière ligne, `exclus=0` | aussitôt, après l'étape 12 |
    | toute ligne ci-dessus | `exclus` non nul | **pas sans la mère** |
    | « POUSSEE FINALE EN ECHEC : … » (code 15 ou course en échec) | non final | **pas sans la mère**, message immédiat |
    | toute autre (journal coupé, variables exigées absentes, signal, ligne inconnue) | quelconque | **pas sans la mère**, message immédiat |

    « Pas sans la mère » : sans ssh, un fichier exclu ou des résultats non poussés sont **irrécupérables** ; garder l'instance ne fait
    que payer le stockage le temps qu'elle décide. La minuterie et la garde à 90 % restent armées et la détruiront à leur échéance : le
    dire dans le message. Si elles tombent pendant la poussée finale (≈ 10 min), les résultats non poussés sont perdus ; la durée de la
    minuterie, comptée sur le plafond, le rend improbable au devis (borne haute 7 USD sur 10, supposé : `garde_depense_v3` contre-lu lors
    des contre-lectures 3 à 5, non relu ici).
12. Fin : récupération par la branche des résultats ; `verifier_resultat` sur chaque fichier de `diag/<run_id>/` ; fichiers exclus lus
    dans l'état poussé (`exclus_fichiers`) et le journal ; pour un fichier qui a grossi, c'est la version déjà poussée qui est à la tête
    de la branche ; copie dans `prep/neuron-lens-v1` ; commit ; poussée de la branche seule.
13. `vastai destroy instance <ID>` ; `… suivi_vast_v4 absente <ID> --temoin <témoin de l'étape 2>` → code 0 exigé ; si le témoin a
    disparu entre-temps, `absente <ID> --non-vide` ; si plus aucune instance n'existe sur le compte, `absente <ID>` sur la liste `[]`, et
    le dire ; minuterie et garde arrêtées **par PID** ; rappel annulé ; crédit relevé de nouveau ; lignes proposées à la mère pour
    `registres/arrets.md` et `registres/depenses.md`.

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_v7.sh` ; journal complet versé (`docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v7.txt`,
empreinte au compagnon). Joué le 14 novembre à 14:48:22 UTC sur le commit source `2851f10e…` (commit réduit `54b36c48…`, 73 fichiers,
liste `801b0202…`, paquet `6c99249c…`) ; **verdict automatique : conforme, 0 écart** ; chaque cas avec son code attendu :
- nominal : liste réelle des essais rapides plus une sonde qui échoue si `GH_TOKEN` est dans l'environnement de pytest, 62 passés ;
  course jouet sans jeton ; fichier de 96 Mio exclu, resté sur le disque de la machine, `exclus=1`, `exclus_fichiers` renseigné ;
  « course terminee », code 0 ;
- artefacts (R5) : mauvais commit → 10 ; arbre non propre → 10 ; essai en échec → 12 ; essai sauté → 12 ; arbre sali → 12 ; carte
  absente → 11 ; première poussée impossible → 14 ; poussée finale impossible → 15 ; commit refusé par un crochet → 15 ; fichier déjà
  poussé qui grossit → version de 1 Mio gardée à la tête, `exclus_fichiers=diag/r-grossit/g.bin`, code 0 ; **tête distante falsifiée
  → 14** ; **`find` en échec → 14** ; **`find` muet et fichier de 96 Mio → second contrôle, 15, fichier absent de la branche** ;
  **copie impossible → 15** ; **index verrouillé → 15** ; **état non inscriptible → 15** ; pour chacun des sept derniers artefacts à
  refus, aucune ligne « pousse » après le premier refus ; sonde « sans jeton » jouée seule avec le jeton présent → code 1 ;
- balayage du jeton factice sous 7 formes (pour ce jeton, brute = adresse) : témoins 7 sur 7 ; dépôt témoin empaqueté (1 paquet) :
  blob et message détectés ; **0 fichier** et **0 ligne d'objet git** sur 18 dépôts, chacun avec des objets lus.
Observé : la poussée initiale du dépôt réduit vers le dépôt nu de l'essai affiche un avertissement de négociation de git (« push
negotiation failed; proceeding anyway »), sans effet (la poussée a réussi : tous les clones l'ont lue).
Non couverts, déclarés : le chemin réel de la machine (création de l'environnement, `pip`, carte réelle, vraie course), le code 13, le
clone HTTPS réel (le clone de l'essai est local : l'en-tête n'y sert pas), la sérialisation réelle de `--args` par l'outil du loueur,
les signaux et l'abandon par `set -e`, la restauration impossible de la version déjà poussée d'un fichier qui grossit, les formes réelles
des sorties de l'outil (seule `instances` est essayée avant la location, étape 2), la survie réelle de la minuterie détachée.

## Jeton
Le jeton du programme permet l'écriture sur tout le dépôt de travail, `main` compris ; « jamais vers `main` » n'est garanti que par
l'amorce (poussée vers `refs/heads/calcul/neuron-lens-volet-a-v1` seulement). Si un jeton restreint à une branche existe, il est
préférable (point signalé à la mère ; elle le porte à Lazar avec la demande de feu, R-2772).

## Devis (inchangé depuis la v3, borne haute)
3,5 à 5,5 h, soit 3,2 à 5 USD à 0,90 USD/h, jusqu'à 7 USD si l'audit R4 « trop beau » se déclenche ; installation de `torch` et de ses
bibliothèques CUDA par `pip` en plus (≈ 5 à 10 min). Le débit réel n'est pas mesuré avant la course : la garde le surveille (6 USD
compte rendu, 9 USD arrêt dur). Si la version de CUDA de l'hôte ne convient pas à `torch` 2.14.1, l'amorce s'arrête au code 11 (quelques
minutes de location perdues).

## Empreintes des pièces citées
Toutes scellées (compagnon `.sha256`) ; la commande elle-même est au compagnon de ce fichier. Le commit réduit et le paquet de la
course sont rendus par le dépôt réduit v10 au commit final et cités dans la demande de feu.

| pièce | empreinte |
|---|---|
| `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-9-commande-v7.md` | `214e280b7ca5ac7ae79677152c5303348b08962fb61f0ccbcd91d409f6c7131a` |
| `scripts/amorce_neuron_lens_volet_a_v6.sh` | `986bc1328334bb6dd02633322408a48fe3641b2ad42aed40dbd8d15f4dbe2cdb` |
| `src/controle_ia/neuron_lens/suivi_vast_v4.py` | `73dc8c46a505db32e0003afee6bae140b19058d6ab84334e1ef9bd52a2bec550` |
| `tests/test_neuron_lens_suivi_vast_v4.py` | `ec959e75c3c67bee412e527dac383d9d63aeb0fd693413d1f9d3147ea668ac07` |
| `scripts/depot_reduit_neuron_lens_volet_a_v10.py` | `177b94db10cf8c53bc077e013ba48bc5b1049a709142ba7b5f40c02bf48f1628` |
| `scripts/essai_a_blanc_amorce_neuron_lens_v7.sh` | `ad7be61ec60857e82745577e6fb4278d510b9789ab6b8b7204e84c2c425e49d6` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v7.txt` | `179726b7d2212208a6b65fadc003cc1c2e6c9f78f8ca754a361c42d9bd2b6b26` |
| `docs/notes/neuron-lens-v1/verification-pip-26-2-2-v1.txt` | `d1476842a453614d51cf265bbf0f62cd6561d165783f7be6194fd3e92387ee26` |
| `src/controle_ia/neuron_lens/garde_depense_v3.py` | `692fa80e842f18a54e7bc937b19c7cb9ff71678c02153eb0c46ec8e34b97cc3d` |
| `src/controle_ia/neuron_lens/volet_a_lancer_v3.py` | `a52506f897adf9f55e3dbce8b6a832d086b0d23866b1ab6d75e122fff906b036` |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| `requirements-neuron-lens-volet-a-v1.txt` | `f61477e91763fa251fbd45e93fb17819883c70c45a60fb5ebd90b01feaca2312` |
| archivées, non employées : `docs/notes/neuron-lens-v1/commande-volet-a-v7.md` | `b36146d052daab3afa15c0d70b16ca31d73414dd804147464bedc034ff74981a` |
| `scripts/amorce_neuron_lens_volet_a_v5.sh` | `d0fbe933e1bb22b01509676301459db3d4713203ec90a5cf1c6c3e0fc3919939` |
| `src/controle_ia/neuron_lens/suivi_vast_v3.py` | `59b7bfafc56e422f360e628c14e05224c6fff9eed60e9aac21208e47b28b836b` |
| `scripts/depot_reduit_neuron_lens_volet_a_v9.py` | `70cc611a82efce7a454892c8deefe944b4786c529b0e7a0be8809a530704ee82` |
| `scripts/essai_a_blanc_amorce_neuron_lens_v6.sh` | `9b70de5f02dc061c46811a514626c65727a2b67425bb9ce27f3a1b620d1482f5` |
| `docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v6.txt` | `acc224366cfb5dbeb6849ef345f33465daf38c9031bd84f8d5f917242dfed1ad` |
